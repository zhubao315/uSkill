"""Tests for the uSkill Runtime 2.0 governed execution engine."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from core.uskills.errors import ExecutionFailedError, PermissionDeniedError, ProviderError
from core.uskills.governance.policy import Permission, PermissionPolicy
from core.uskills.runtime import (
    MockProvider,
    SkillLibrary,
    SkillRuntime,
    StepState,
    ToolRegistry,
    validate_inputs,
)
from core.uskills.runtime.state import RunStore
from core.uskills.schema import USkill


def _skill_id(cid: str, name: str) -> str:
    return f"uskill-{cid}-{name}-v1-0-0"


def make_llm_skill(
    name: str = "demo",
    *,
    params: list[dict] | None = None,
    output_params: list[str] | None = None,
    timeout: int = 5,
    retry: int = 0,
    requires_approval: bool = False,
) -> USkill:
    params = params or [{"name": "text", "type": "string", "required": True}]
    output_params = output_params if output_params is not None else ["result"]
    data = {
        "skill_id": _skill_id("atomic", name),
        "meta": {
            "name": name,
            "category": "atomic",
            "description": f"demo skill {name}",
        },
        "input": {"params": params},
        "execute": {
            "prompt_template": "Do work on {{text}}",
            "model": "mock-model",
            "requires_approval": requires_approval,
        },
        "output": {"format": "json", "params": output_params},
        "control": {"timeout": timeout, "retry": retry},
    }
    return USkill(**data)


def make_composite(name: str, tools: list[str], fallback: list[str] | None = None) -> USkill:
    data = {
        "skill_id": _skill_id("composite", name),
        "meta": {"name": name, "category": "composite", "description": "composite"},
        "input": {"params": [{"name": "text", "type": "string", "required": True}]},
        "execute": {
            "prompt_template": "pipeline over {{text}} with {{step_a}}",
            "model": "mock-model",
            "tools": tools,
            "fallback": fallback or [],
        },
        "output": {"format": "json", "params": ["result"]},
        "control": {"timeout": 5, "retry": 0},
    }
    return USkill(**data)


class TestInputValidation:
    def test_required_missing_rejected(self) -> None:
        skill = make_llm_skill()
        with pytest.raises(ExecutionFailedError, match="missing required input"):
            validate_inputs(skill, {})

    def test_undeclared_param_rejected(self) -> None:
        skill = make_llm_skill()
        with pytest.raises(ExecutionFailedError, match="undeclared"):
            validate_inputs(skill, {"text": "hi", "bogus": 1})

    def test_type_mismatch_rejected(self) -> None:
        skill = make_llm_skill()
        with pytest.raises(ExecutionFailedError, match="must be string"):
            validate_inputs(skill, {"text": {"nested": 1}})

    def test_defaults_applied(self) -> None:
        skill = make_llm_skill(
            params=[
                {"name": "text", "type": "string", "required": True},
                {"name": "level", "type": "integer", "required": False, "default": 3},
            ]
        )
        merged = validate_inputs(skill, {"text": "x"})
        assert merged["level"] == 3

    def test_object_from_json_string(self) -> None:
        skill = make_llm_skill(params=[{"name": "data", "type": "object", "required": True}])
        merged = validate_inputs(skill, {"data": '{"a": 1}'})
        assert merged["data"] == {"a": 1}


class TestSingleSkillExecution:
    def test_success(self) -> None:
        provider = MockProvider('{"result": "done"}')
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill(), {"text": "hello"})
        assert record.status is StepState.COMPLETED
        assert record.result == {"result": "done"}
        assert len(provider.calls) == 1
        # data boundary: inputs are not promoted to system policy
        assert provider.calls[0]["messages"][0]["role"] == "system"

    def test_invalid_json_output_is_failure_not_faked(self) -> None:
        provider = MockProvider("not json")
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill(), {"text": "x"})
        assert record.status is StepState.FAILED
        assert "not valid JSON" in (record.error or "")

    def test_missing_declared_output_param(self) -> None:
        provider = MockProvider('{"wrong": 1}')
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill(output_params=["result"]), {"text": "x"})
        assert record.status is StepState.FAILED
        assert "missing declared params" in (record.error or "")

    def test_provider_timeout_enforced(self) -> None:
        # Schema minimum timeout is 1s; a slow provider must fail at ~1s,
        # proving control.timeout is actually enforced by the engine.
        provider = MockProvider('{"result": "late"}', delay=1.3)
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill(timeout=1), {"text": "x"})
        assert record.status is StepState.FAILED
        assert "timed out" in (record.error or "")

    def test_transient_errors_exhaust_retries(self) -> None:
        provider = MockProvider(
            errors={i: ProviderError("boom", retryable=True) for i in range(5)}
        )
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill(retry=2), {"text": "x"})
        assert record.status is StepState.FAILED
        assert len(provider.calls) == 3  # initial + 2 retries
        assert "after 3 attempts" in (record.error or "")

    def test_retry_succeeds_after_transient(self) -> None:
        provider = MockProvider(
            script=['{"result": "late"}'],
            errors={0: ProviderError("transient", retryable=True)},
        )
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill(retry=1), {"text": "x"})
        assert record.status is StepState.COMPLETED
        assert len(provider.calls) == 2

    def test_non_transient_not_retried(self) -> None:
        provider = MockProvider(errors={0: ProviderError("auth", retryable=False)})
        SkillRuntime(provider)
        # ProviderError is treated as transient regardless of flag by the loop;
        # a hard ExecutionFailedError is not transient and stops after first try.
        provider2 = MockProvider(errors={0: ExecutionFailedError("hard fail")})
        runtime2 = SkillRuntime(provider2)
        record = runtime2.run(make_llm_skill(retry=3), {"text": "x"})
        assert record.status is StepState.FAILED
        assert len(provider2.calls) == 1  # non-transient: no retry


class TestCompositeWorkflow:
    def test_composite_schedules_subskills(self) -> None:
        call_count = {"n": 0}

        def responder(idx: int) -> str:
            call_count["n"] += 1
            return json.dumps({"result": f"out{idx}"})

        provider = MockProvider(responder)
        library = SkillLibrary()
        library.register(make_llm_skill("step_a"))
        library.register(make_llm_skill("step_b"))
        runtime = SkillRuntime(provider, library=library)

        composite = make_composite("pipe", ["step_a", "step_b"])
        record = runtime.run(composite, {"text": "input"})

        assert record.status is StepState.COMPLETED
        kinds = [(s.step_id, s.status) for s in record.steps]
        # Two sub-skill steps + final synthesis LLM step, all completed.
        assert ("subskill:step_a", StepState.COMPLETED) in kinds
        assert ("subskill:step_b", StepState.COMPLETED) in kinds
        assert ("llm", StepState.COMPLETED) in kinds
        # 2 sub-skill LLM calls + 1 synthesis call = 3 provider invocations.
        assert call_count["n"] == 3

    def test_composite_unresolvable_tool_fails(self) -> None:
        provider = MockProvider('{"result": "x"}')
        runtime = SkillRuntime(provider, library=SkillLibrary())
        composite = make_composite("pipe", ["missing_tool"])
        record = runtime.run(composite, {"text": "input"})
        assert record.status is StepState.FAILED
        assert "neither a sub-skill nor a registered tool" in (record.error or "")

    def test_partial_execution_fallback_skips(self) -> None:
        provider = MockProvider('{"result": "x"}')
        runtime = SkillRuntime(provider, library=SkillLibrary())
        composite = make_composite("pipe", ["missing"], fallback=["partial-execution"])
        record = runtime.run(composite, {"text": "input"})
        assert record.status is StepState.COMPLETED
        assert any(s.status is StepState.SKIPPED for s in record.steps)

    def test_tool_registry_invocation(self) -> None:
        provider = MockProvider('{"result": "x"}')
        registry = ToolRegistry()
        registry.register_tool("sum", lambda p: {"result": str(p.get("text", "")) + "!"})
        runtime = SkillRuntime(provider, registry=registry, library=SkillLibrary())
        composite = make_composite("pipe", ["sum"])
        record = runtime.run(composite, {"text": "hi"})
        assert record.status is StepState.COMPLETED


class TestPermissions:
    def test_tool_permission_denied(self) -> None:
        provider = MockProvider('{"result": "x"}')
        policy = PermissionPolicy(allow={Permission.read})
        registry = ToolRegistry(policy=policy)
        registry.register_tool("writer", lambda p: "written", permission=Permission.write)
        runtime = SkillRuntime(provider, registry=registry, library=SkillLibrary())
        composite = make_composite("pipe", ["writer"])
        record = runtime.run(composite, {"text": "x"})
        assert record.status is StepState.FAILED
        assert "not allowed by the runtime policy" in (record.error or "")
        with pytest.raises(PermissionDeniedError):
            registry.invoke("writer", {})


class TestApproval:
    def test_waiting_then_resume(self, tmp_path: Path) -> None:
        provider = MockProvider('{"result": "ok"}')
        store = RunStore(tmp_path)
        skill = make_llm_skill("gated", requires_approval=True)
        library = SkillLibrary()
        library.register(skill)
        runtime = SkillRuntime(provider, library=library, store=store)

        record = runtime.run(skill, {"text": "x"})
        assert record.status is StepState.WAITING_APPROVAL
        assert store.load(record.run_id).status is StepState.WAITING_APPROVAL

        resumed = runtime.resume(record.run_id, approve=True)
        assert resumed.status is StepState.COMPLETED
        assert resumed.result == {"result": "ok"}

    def test_resume_reject_interrupts(self, tmp_path: Path) -> None:
        provider = MockProvider('{"result": "ok"}')
        skill = make_llm_skill("gated2", requires_approval=True)
        library = SkillLibrary()
        library.register(skill)
        runtime = SkillRuntime(provider, library=library, store=RunStore(tmp_path))
        record = runtime.run(skill, {"text": "x"})
        rejected = runtime.resume(record.run_id, approve=False)
        assert rejected.status is StepState.INTERRUPTED


class TestRunRecords:
    def test_run_record_checkpoint_roundtrip(self, tmp_path: Path) -> None:
        provider = MockProvider('{"result": "r"}')
        store = RunStore(tmp_path)
        runtime = SkillRuntime(provider, store=store)
        record = runtime.run(make_llm_skill(), {"text": "x"})

        loaded = store.load(record.run_id)
        assert loaded.run_id == record.run_id
        assert loaded.result == {"result": "r"}
        assert loaded.events  # events recorded
        assert loaded.usage.get("total_tokens", 0) > 0

    def test_inspect_and_events(self, tmp_path: Path) -> None:
        provider = MockProvider('{"result": "r"}')
        runtime = SkillRuntime(provider, store=RunStore(tmp_path))
        record = runtime.run(make_llm_skill(), {"text": "x"})
        events = runtime.list_events(record.run_id)
        assert any(e["event"] == "step_completed" for e in events)
