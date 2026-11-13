"""Sprint 3 runtime controls: constraints, repair loop, cancel, backoff,
idempotency, DAG scheduling and extended providers."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from pydantic import ValidationError

from core.uskills.errors import ExecutionFailedError, ProviderError
from core.uskills.runtime import (
    AnthropicProvider,
    CancelToken,
    LocalProvider,
    MockProvider,
    OpenAICompatibleProvider,
    SkillLibrary,
    SkillRuntime,
    StepState,
    ToolRegistry,
    create_provider,
    topo_levels,
    validate_inputs,
)
from core.uskills.runtime.providers import Message
from core.uskills.runtime.state import RunRecord
from core.uskills.schema import USkill


def make_llm_skill(
    name: str = "demo",
    *,
    params: list[dict] | None = None,
    output_params: list[str] | None = None,
    timeout: int = 5,
    retry: int = 0,
) -> USkill:
    params = params or [{"name": "text", "type": "string", "required": True}]
    output_params = output_params if output_params is not None else ["result"]
    return USkill(
        **{
            "skill_id": f"uskill-atomic-{name}-v1-0-0",
            "meta": {"name": name, "category": "atomic", "description": f"demo skill {name}"},
            "input": {"params": params},
            "execute": {"prompt_template": "Do work on {{text}}", "model": "mock-model"},
            "output": {"format": "json", "params": output_params},
            "control": {"timeout": timeout, "retry": retry},
        }
    )


def make_composite(name: str, tools: list[str], depends: dict[str, list[str]] | None = None) -> USkill:
    execute: dict[str, Any] = {
        "prompt_template": "pipeline over {{text}}",
        "model": "mock-model",
        "tools": tools,
    }
    if depends:
        execute["depends_on"] = depends
    return USkill(
        **{
            "skill_id": f"uskill-composite-{name}-v1-0-0",
            "meta": {"name": name, "category": "composite", "description": "composite"},
            "input": {"params": [{"name": "text", "type": "string", "required": True}]},
            "execute": execute,
            "output": {"format": "json", "params": ["result"]},
            "control": {"timeout": 5, "retry": 0},
        }
    )


class TestParamConstraints:
    def test_enum_enforced(self) -> None:
        skill = make_llm_skill(
            "constrained", params=[{"name": "text", "type": "string"}, {"name": "mode", "type": "string", "enum": ["fast", "deep"]}]
        )
        merged = validate_inputs(skill, {"text": "a", "mode": "fast"})
        assert merged["mode"] == "fast"
        with pytest.raises(ExecutionFailedError, match="constraints"):
            validate_inputs(skill, {"text": "a", "mode": "turbo"})

    def test_numeric_bounds(self) -> None:
        skill = make_llm_skill(
            "bounded", params=[{"name": "n", "type": "integer", "minimum": 1, "maximum": 10}]
        )
        assert validate_inputs(skill, {"n": 5}) == {"n": 5}
        with pytest.raises(ExecutionFailedError, match="maximum"):
            validate_inputs(skill, {"n": 11})
        with pytest.raises(ExecutionFailedError, match="minimum"):
            validate_inputs(skill, {"n": 0})

    def test_pattern_and_length(self) -> None:
        skill = make_llm_skill(
            "coded",
            params=[{"name": "code", "type": "string", "pattern": "^[A-Z]{3}$", "min_length": 3}],
        )
        assert validate_inputs(skill, {"code": "ABC"}) == {"code": "ABC"}
        with pytest.raises(ExecutionFailedError, match="does not match"):
            validate_inputs(skill, {"code": "abc1"})

    def test_invalid_regex_rejected_at_definition(self) -> None:
        with pytest.raises(ValidationError):
            make_llm_skill("bad", params=[{"name": "x", "type": "string", "pattern": "([unclosed"}])

    def test_nullable(self) -> None:
        strict = make_llm_skill("strict", params=[{"name": "v", "type": "string", "required": False}])
        with pytest.raises(ExecutionFailedError, match="must not be null"):
            validate_inputs(strict, {"v": None})
        ok = make_llm_skill(
            "nullable",
            params=[{"name": "v", "type": "string", "required": False, "nullable": True}],
        )
        assert validate_inputs(ok, {"v": None}) == {"v": None}

    def test_array_item_type_enforced(self) -> None:
        skill = make_llm_skill("arr", params=[{"name": "xs", "type": "array", "items_type": "integer"}])
        assert validate_inputs(skill, {"xs": [1, 2]}) == {"xs": [1, 2]}
        with pytest.raises(ExecutionFailedError, match="constraints"):
            validate_inputs(skill, {"xs": [1, "two"]})

    def test_full_schema_override(self) -> None:
        skill = make_llm_skill(
            "cfg",
            params=[
                {
                    "name": "cfg",
                    "type": "object",
                    "schema": {
                        "type": "object",
                        "required": ["host"],
                        "properties": {"host": {"type": "string"}},
                    },
                }
            ],
        )
        assert validate_inputs(skill, {"cfg": {"host": "a"}}) == {"cfg": {"host": "a"}}
        with pytest.raises(ExecutionFailedError, match="host"):
            validate_inputs(skill, {"cfg": {"port": 1}})

    def test_constraints_enforced_before_model_call(self) -> None:
        provider = MockProvider('{"result": "x"}')
        runtime = SkillRuntime(provider)
        skill = make_llm_skill("gated", params=[{"name": "text", "type": "string", "min_length": 5}])
        with pytest.raises(ExecutionFailedError, match="too short"):
            runtime.run(skill, {"text": "tiny"})
        assert provider.calls == []  # never reached the model


class TestOutputRepairLoop:
    def test_repair_recovers_invalid_output(self) -> None:
        provider = MockProvider(script=["not json at all", '{"result": "fixed"}'])
        runtime = SkillRuntime(provider)
        record = runtime.run(make_llm_skill("repairable"), {"text": "x"})
        assert record.status is StepState.COMPLETED
        assert record.result == {"result": "fixed"}
        assert len(provider.calls) == 2
        assert "failed validation" in provider.calls[1]["messages"][1]["content"]

    def test_repair_budget_is_bounded(self) -> None:
        provider = MockProvider("still not json")
        runtime = SkillRuntime(provider)
        skill = make_llm_skill("stubborn")
        record = runtime.run(skill, {"text": "x"})
        assert record.status is StepState.FAILED
        assert len(provider.calls) == 1 + skill.control.repair  # default repair = 2
        assert "not valid JSON" in (record.error or "")

    def test_repair_disabled_with_zero_budget(self) -> None:
        provider = MockProvider("nope")
        data = make_llm_skill("no-repair").model_dump(mode="json", by_alias=True)
        data["control"]["repair"] = 0
        record = SkillRuntime(provider).run(USkill(**data), {"text": "x"})
        assert record.status is StepState.FAILED
        assert len(provider.calls) == 1

    def test_full_output_schema_validated(self) -> None:
        data = make_llm_skill("typed-out", output_params=[]).model_dump(mode="json", by_alias=True)
        data["output"]["schema"] = {
            "type": "object",
            "required": ["score"],
            "properties": {"score": {"type": "integer", "minimum": 0, "maximum": 100}},
        }
        provider = MockProvider(script=['{"score": 999}', '{"score": 42}'])
        record = SkillRuntime(provider).run(USkill(**data), {"text": "x"})
        assert record.status is StepState.COMPLETED
        assert record.result == {"score": 42}  # out-of-range rejected, then repaired

    def test_schema_passed_to_capable_providers(self) -> None:
        provider = MockProvider('{"result": "ok"}')
        SkillRuntime(provider).run(make_llm_skill("schema-hint"), {"text": "x"})
        assert provider.calls[0]["json_schema"] is not None


class TestCancellation:
    def test_pre_cancelled_run_never_calls_provider(self) -> None:
        provider = MockProvider('{"result": "x"}')
        token = CancelToken()
        token.cancel("user stop")
        record = SkillRuntime(provider).run(make_llm_skill(), {"text": "x"}, cancel_token=token)
        assert record.status is StepState.CANCELLED
        assert provider.calls == []
        assert any(e["event"] == "run_cancelled" for e in record.events)
        assert all(s.status is StepState.CANCELLED for s in record.steps)

    def test_cancel_between_steps(self) -> None:
        token = CancelToken()

        def script(idx: int) -> str:
            if idx == 0:  # first sub-skill finished -> caller cancels
                token.cancel("changed my mind")
            return '{"result": "done"}'

        provider = MockProvider(script=script)
        lib = SkillLibrary()
        for sub in ("step_a", "step_b"):
            lib.register(make_llm_skill(sub))
        runtime = SkillRuntime(provider, library=lib)
        record = runtime.run(
            make_composite("dag-cancel", ["step_a", "step_b"]), {"text": "x"}, cancel_token=token
        )
        assert record.status is StepState.CANCELLED
        steps = {s.step_id: s for s in record.steps}
        assert steps["subskill:step_a"].status is StepState.COMPLETED
        assert steps["subskill:step_b"].status is StepState.CANCELLED

    def test_cancelled_state_roundtrips(self) -> None:
        record = RunRecord(run_id="run-x", skill_id="s", status=StepState.CANCELLED)
        clone = RunRecord.from_dict(record.to_dict())
        assert clone.status is StepState.CANCELLED


class TestBackoff:
    def test_exponential_backoff_schedule(self, monkeypatch: pytest.MonkeyPatch) -> None:
        sleeps: list[float] = []
        import core.uskills.runtime.engine as engine_mod

        monkeypatch.setattr(engine_mod.time, "sleep", lambda s: sleeps.append(s))
        provider = MockProvider(
            errors={i: ProviderError("blip", retryable=True) for i in range(5)}
        )
        data = make_llm_skill("backoff", retry=2).model_dump(mode="json", by_alias=True)
        data["control"]["backoff_base"] = 0.5
        record = SkillRuntime(provider).run(USkill(**data), {"text": "x"})
        assert record.status is StepState.FAILED
        assert sleeps == [0.5, 1.0]  # base * 2**attempt
        assert any(e["event"] == "step_backoff" for e in record.events)

    def test_zero_backoff_never_sleeps(self, monkeypatch: pytest.MonkeyPatch) -> None:
        def boom(_s: float) -> None:
            raise AssertionError("must not sleep")

        import core.uskills.runtime.engine as engine_mod

        monkeypatch.setattr(engine_mod.time, "sleep", boom)
        provider = MockProvider(
            errors={i: ProviderError("blip", retryable=True) for i in range(5)}
        )
        record = SkillRuntime(provider).run(make_llm_skill("nosleep", retry=2), {"text": "x"})
        assert record.status is StepState.FAILED


class TestToolIdempotency:
    def test_non_idempotent_tool_not_retried(self) -> None:
        calls: list[dict] = []

        def flaky_tool(payload: dict[str, Any]) -> str:
            calls.append(payload)
            raise ConnectionError("network blip")

        registry = ToolRegistry()
        registry.register_tool("pay", flaky_tool, idempotent=False)
        runtime = SkillRuntime(MockProvider('{"result": "d"}'), registry=registry)
        record = runtime.run(make_composite("billing", ["pay"]), {"text": "x"}, retries=3)
        assert record.status is StepState.FAILED
        assert len(calls) == 1  # side effect executed exactly once
        assert "auto-retry disabled" in (record.error or "")

    def test_idempotent_tool_still_retried(self) -> None:
        calls: list[dict] = []

        def flaky_tool(payload: dict[str, Any]) -> str:
            calls.append(payload)
            if len(calls) < 2:
                raise ConnectionError("blip")
            return "paid"

        registry = ToolRegistry()
        registry.register_tool("read-balance", flaky_tool)  # default idempotent
        runtime = SkillRuntime(MockProvider('{"result": "d"}'), registry=registry)
        record = runtime.run(make_composite("check", ["read-balance"]), {"text": "x"}, retries=2)
        assert record.status is StepState.COMPLETED
        assert len(calls) == 2


class TestDAGScheduling:
    def test_topo_levels_diamond(self) -> None:
        levels = topo_levels(["a", "b", "c", "d"], {"b": ["a"], "c": ["a"], "d": ["b", "c"]})
        assert levels == [["a"], ["b", "c"], ["d"]]

    def test_topo_levels_detects_cycle(self) -> None:
        with pytest.raises(ExecutionFailedError, match="cycle"):
            topo_levels(["a", "b"], {"a": ["b"], "b": ["a"]})

    def test_topo_levels_rejects_unknown_dep(self) -> None:
        with pytest.raises(ExecutionFailedError, match="undeclared"):
            topo_levels(["a"], {"a": ["ghost"]})

    def test_dag_end_to_end_respects_dependencies(self) -> None:
        lib = SkillLibrary()
        for sub in ("extract", "summarize", "translate", "merge"):
            lib.register(make_llm_skill(sub))
        provider = MockProvider(script=lambda i: '{"result": "done"}', delay=0.2)
        runtime = SkillRuntime(provider, library=lib)
        record = runtime.run(
            make_composite(
                "pipeline",
                ["extract", "summarize", "translate", "merge"],
                depends={
                    "summarize": ["extract"],
                    "translate": ["extract"],
                    "merge": ["summarize", "translate"],
                },
            ),
            {"text": "x"},
        )
        assert record.status is StepState.COMPLETED
        evs = record.events

        def ev_index(event: str, step: str) -> int:
            return next(
                i for i, e in enumerate(evs) if e["event"] == event and e.get("step_id") == step
            )

        # dependencies honored: extract completes before summarize/translate start
        assert ev_index("step_completed", "subskill:extract") < ev_index(
            "step_started", "subskill:summarize"
        )
        # level parallelism: both branches start before either finishes
        assert ev_index("step_started", "subskill:translate") < ev_index(
            "step_completed", "subskill:summarize"
        )
        assert ev_index("step_started", "subskill:summarize") < ev_index(
            "step_completed", "subskill:translate"
        )
        # merge runs last, after both branches
        assert ev_index("step_completed", "subskill:translate") < ev_index(
            "step_started", "subskill:merge"
        )

    def test_dag_failure_blocks_dependents(self) -> None:
        lib = SkillLibrary()
        lib.register(make_llm_skill("a1"))
        lib.register(make_llm_skill("b1"))
        # first provider call (sub a1) succeeds; later calls (sub b1) never valid
        provider = MockProvider(script=lambda i: '{"result": "done"}' if i == 0 else "garbage")
        runtime = SkillRuntime(provider, library=lib)
        record = runtime.run(
            make_composite("faildag", ["a1", "b1"], depends={"b1": ["a1"]}), {"text": "x"}
        )
        assert record.status is StepState.FAILED
        statuses = {s.step_id: s.status for s in record.steps}
        assert statuses["subskill:a1"] is StepState.COMPLETED
        assert statuses["subskill:b1"] is StepState.FAILED
        assert statuses["llm"] is StepState.PENDING

    def test_empty_depends_on_keeps_sequential_order(self) -> None:
        lib = SkillLibrary()
        for sub in ("x1", "x2"):
            lib.register(make_llm_skill(sub))
        runtime = SkillRuntime(MockProvider('{"result": "d"}'), library=lib)
        record = runtime.run(make_composite("seq", ["x1", "x2"]), {"text": "x"})
        assert record.status is StepState.COMPLETED


class TestProvidersV3:
    def test_factory_kinds(self) -> None:
        assert create_provider(
            "openai-compatible", api_key="test", base_url="http://gw.local/v1"
        )
        assert isinstance(create_provider("local"), LocalProvider)
        with pytest.raises(ValueError, match="Unknown provider"):
            create_provider("telepathy")

    def test_local_provider_defaults(self) -> None:
        prov = LocalProvider()
        assert str(prov.client.base_url).startswith("http://localhost:11434")
        # honest capability claim: local servers vary, no native structured output
        assert prov.capabilities.structured_output is False

    def test_compatible_provider_reads_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("USKILLS_OPENAI_BASE_URL", "http://gateway.internal/v1")
        prov = OpenAICompatibleProvider(api_key="k")
        assert "gateway.internal" in str(prov.client.base_url)

    def test_anthropic_adapter_with_fake_client(self) -> None:
        captured: dict[str, Any] = {}

        class FakeMessages:
            def create(self, **kwargs: Any) -> Any:
                captured.update(kwargs)
                return SimpleNamespace(
                    content=[SimpleNamespace(text='{"result": "hi"}')],
                    model="claude-test",
                    usage=SimpleNamespace(input_tokens=7, output_tokens=5),
                    stop_reason="end_turn",
                )

        prov = AnthropicProvider(client=SimpleNamespace(messages=FakeMessages()))
        resp = prov.complete(
            [Message("system", "sys"), Message("user", "hi")],
            model="claude-test",
            json_mode=True,
        )
        assert resp.text == '{"result": "hi"}'
        assert resp.usage["total_tokens"] == 12
        assert captured["system"].startswith("sys")
        assert "JSON" in captured["system"]  # json_mode instruction injected
        assert captured["messages"] == [{"role": "user", "content": "hi"}]

    def test_anthropic_error_classified_as_provider_error(self) -> None:
        class Failing:
            def create(self, **_kwargs: Any) -> Any:
                raise RuntimeError("kaboom")

        prov = AnthropicProvider(client=SimpleNamespace(messages=Failing()))
        with pytest.raises(ProviderError, match="kaboom"):
            prov.complete([Message("user", "x")], model="claude-test")

    def test_runtime_with_anthropic_adapter(self) -> None:
        class FakeMessages:
            def create(self, **_kwargs: Any) -> Any:
                return SimpleNamespace(
                    content=[SimpleNamespace(text='{"result": "via-anthropic"}')],
                    model="claude-test",
                    usage=SimpleNamespace(input_tokens=1, output_tokens=1),
                    stop_reason="end_turn",
                )

        prov = AnthropicProvider(client=SimpleNamespace(messages=FakeMessages()))
        record = SkillRuntime(prov).run(make_llm_skill("ant"), {"text": "x"})
        assert record.status is StepState.COMPLETED
        assert record.result == {"result": "via-anthropic"}


class TestControlSchema:
    def test_new_control_fields_are_bounded(self) -> None:
        data = make_llm_skill("ctl").model_dump(mode="json", by_alias=True)
        data["control"]["repair"] = 99  # le=5
        with pytest.raises(ValidationError):
            USkill(**data)
        data = make_llm_skill("ctl2").model_dump(mode="json", by_alias=True)
        data["control"]["backoff_base"] = -1
        with pytest.raises(ValidationError):
            USkill(**data)

    def test_uskill_model_dump_alias_roundtrip(self) -> None:
        data = make_llm_skill("rt").model_dump(mode="json", by_alias=True)
        assert USkill(**data).skill_id == "uskill-atomic-rt-v1-0-0"
