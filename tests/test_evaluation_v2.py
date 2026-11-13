"""Sprint 4 evaluation extensions: metrics, matrix, regression gate, judge."""

from __future__ import annotations

import json
from pathlib import Path

from core.uskills.evaluation import (
    EvalAssertion,
    EvalCase,
    EvalReport,
    EvalResult,
    EvalSuite,
    check_release_gate,
    compare_reports,
    estimate_cost,
    judge_eval_suite,
    matrix_summary,
    run_eval_matrix,
    run_eval_suite,
)
from core.uskills.governance.policy import Permission
from core.uskills.runtime import MockProvider, SkillLibrary, SkillRuntime, ToolRegistry
from core.uskills.schema import USkill
from core.uskills.validator import load_skill

REPO = Path(__file__).resolve().parent.parent


def summarize_skill(model: str = "gpt-4o-mini") -> USkill:
    return USkill(
        **{
            "skill_id": f"uskill-atomic-ev-{model.replace('.', 'p').replace('-', 'p')}-v1-0-0",
            "meta": {"name": f"ev-{model}", "category": "atomic", "description": "eval target"},
            "input": {"params": [{"name": "text", "type": "string", "required": True}]},
            "execute": {"prompt_template": "sum {{text}}", "model": model},
            "output": {"format": "json", "params": ["summary"]},
            "control": {"timeout": 5, "retry": 0},
        }
    )


def suite(task: str = "t1", output: str = "summary") -> EvalSuite:
    return EvalSuite(
        skill="ev",
        version="1.0.0",
        cases=[
            EvalCase(
                task_id=task,
                user_input={"text": "hello"},
                assertions=[EvalAssertion(type="json_key", key=output)],
            )
        ],
    )


class TestMetrics:
    def test_cost_uses_pricing_table_or_none(self) -> None:
        usage = {"prompt_tokens": 1_000_000, "completion_tokens": 500_000}
        cost = estimate_cost(usage, "gpt-4o-mini")  # 0.15 + 0.30
        assert cost is not None and abs(cost - 0.45) < 1e-9
        assert estimate_cost(usage, "mythical-model-9000") is None

    def test_consistency_none_for_single_repeat(self) -> None:
        report = run_eval_suite(
            SkillRuntime(MockProvider('{"summary": "s"}')), summarize_skill(), suite()
        )
        assert report.metrics["consistency"] is None  # not fabricated 1.0

    def test_consistency_measured_over_repeats(self) -> None:
        # alternating pass/fail across repeats -> agreement 0.5
        provider = MockProvider(script=['{"summary": "s"}', "not json"])
        report = run_eval_suite(SkillRuntime(provider), summarize_skill(), suite(), repeats=2)
        assert report.metrics["consistency"] == 0.5

    def test_output_validity_vs_success(self) -> None:
        # engine-accepted output (text format, no contract) that fails a
        # stricter eval assertion: validity 1.0, success 0.0
        skill = summarize_skill()
        data = skill.model_dump(mode="json", by_alias=True)
        data["output"] = {"format": "text", "params": []}
        provider = MockProvider("plain prose, no json here")
        report = run_eval_suite(SkillRuntime(provider), USkill(**data), suite())
        assert report.metrics["output_validity"] == 1.0
        assert report.metrics["task_success_rate"] == 0.0

    def test_tokens_and_latency_recorded(self) -> None:
        provider = MockProvider('{"summary": "s"}')
        report = run_eval_suite(SkillRuntime(provider), summarize_skill(), suite())
        assert report.metrics["tokens_total"] == 30  # mock usage per call
        assert report.metrics["usage"]["prompt_tokens"] == 10
        assert report.metrics["cost_usd"] is not None
        assert report.metrics["latency_ms"]["mean"] >= 0.0

    def test_tool_success_rate(self) -> None:
        calls: list[int] = []

        def ok_tool(payload: dict) -> str:
            calls.append(1)
            return "done"

        def bad_tool(payload: dict) -> str:
            raise ConnectionError("nope")

        registry = ToolRegistry()
        registry.register_tool("good", ok_tool)
        registry.register_tool("evil", bad_tool, permission=Permission.shell)
        composite = USkill(
            **{
                "skill_id": "uskill-composite-tools-v1-0-0",
                "meta": {"name": "tools", "category": "composite", "description": "d"},
                "input": {"params": [{"name": "text", "type": "string", "required": True}]},
                "execute": {
                    "prompt_template": "use {{good}} and {{evil}}",
                    "model": "gpt-4o-mini",
                    "tools": ["good", "evil"],
                    "fallback": ["partial-execution"],
                },
                "output": {"format": "json", "params": ["result"]},
                "control": {"timeout": 5, "retry": 0},
            }
        )
        provider = MockProvider('{"result": "r"}')
        report = run_eval_suite(
            SkillRuntime(provider, registry=registry), composite, suite(output="result")
        )
        # honest accounting: good ran OK, evil denied by permission policy and
        # skipped by partial-execution fallback -> 1 of 2 tool steps succeeded
        assert report.assisted[0].tool_calls == 2
        assert report.metrics["tool_success_rate"] == 0.5

    def test_metrics_serializable(self) -> None:
        report = run_eval_suite(
            SkillRuntime(MockProvider('{"summary": "s"}')), summarize_skill(), suite()
        )
        json.dumps(report.to_dict(), ensure_ascii=False)


class TestRegressionGate:
    def _report(self, task: str, passed: bool) -> EvalReport:
        rep = EvalReport(skill="ev", model="gpt-4o-mini")
        rep.assisted = [EvalResult(task, passed, completed=True)]
        return rep

    def test_compare_detects_regression_and_improvement(self) -> None:
        previous = self._report("t1", True).to_dict()
        current = self._report("t1", False)
        diff = compare_reports(current, previous)
        assert diff["regressed_cases"] == ["t1"]
        assert diff["delta_pp"] == -100.0

    def test_gate_blocks_unexplained_regression(self) -> None:
        previous = self._report("t1", True).to_dict()
        problems = check_release_gate(self._report("t1", False), previous)
        assert problems and "regression" in problems[0]

    def test_gate_passes_when_stable(self) -> None:
        previous = self._report("t1", True).to_dict()
        assert check_release_gate(self._report("t1", True), previous) == []

    def test_gate_success_rate_drop_threshold(self) -> None:
        previous = {
            "assisted_detail": {},  # no per-case data: rate-based rule only
            "assisted_success_rate": 0.9,
        }
        current = EvalReport(skill="ev")
        current.assisted = [EvalResult(f"t{i}", i == 0, completed=True) for i in range(9)]
        problems = check_release_gate(current, previous, max_drop_pp=10.0)
        assert problems and "dropped" in problems[0]
        assert check_release_gate(current, previous, max_drop_pp=100.0) == []


class TestMatrix:
    def test_matrix_runs_per_model(self) -> None:
        models = ["model-a", "model-b"]
        seen_models: list[str] = []

        class Recording(MockProvider):
            def complete(self, *a, **kw):  # type: ignore[no-untyped-def]
                seen_models.append(str(kw.get("model", "?")))
                return super().complete(*a, **kw)

        reports = run_eval_matrix(
            lambda: SkillRuntime(Recording('{"summary": "s"}')),
            summarize_skill(),
            suite(),
            models,
        )
        assert set(reports) == set(models)
        assert set(seen_models) == set(models)
        summary = matrix_summary(reports)
        assert all(row["success_rate"] == 1.0 for row in summary.values())
        json.dumps(summary)


class TestJudge:
    def test_judge_recorded_separately_and_advisory(self) -> None:
        runtime = SkillRuntime(MockProvider('{"summary": "s"}'))
        report = run_eval_suite(runtime, summarize_skill(), suite())
        assert report.assisted[0].passed

        judge_runtime = SkillRuntime(
            MockProvider('{"score": 4, "rationale": "complete and structured"}')
        )
        judge_eval_suite(judge_runtime, report, model="judge-model-1")

        assert len(report.judgments) == 1
        j = report.judgments[0]
        assert j.score == 4 and j.judge_model == "judge-model-1"
        # determinism untouched: a harsh judge must never flip pass/fail
        report2 = run_eval_suite(
            SkillRuntime(MockProvider('{"summary": "s"}')), summarize_skill(), suite()
        )
        harsh = SkillRuntime(MockProvider('{"score": 0, "rationale": "harsh"}'))
        judge_eval_suite(harsh, report2, model="judge-x")
        assert report2.judgments[0].score == 0
        assert report2.assisted[0].passed

        data = report.to_dict()
        assert data["judgments"]["records"][0]["judge_model"] == "judge-model-1"
        assert "advisory" in data["judgments"]["note"]
        # deterministic gate section carries no judge fields
        assert "judge" not in json.dumps(data["cases"])

    def test_judge_failure_recorded_not_faked(self) -> None:
        runtime = SkillRuntime(MockProvider('{"summary": "s"}'))
        report = run_eval_suite(runtime, summarize_skill(), suite())
        failing = SkillRuntime(MockProvider(errors={0: RuntimeError("judge down")}))
        judge_eval_suite(failing, report, model="judge-x")
        assert report.judgments[0].score is None
        assert "judge error" in report.judgments[0].error
        json.dumps(report.to_dict())


class TestRealDatasets:
    """Offline structural + runner checks for shipped eval datasets.

    Real-model scores must be produced in deployment; CI only proves the
    suites load, bind to real skills, and run through the harness.
    """

    def _suites(self) -> list[tuple[EvalSuite, Path]]:
        out: list[tuple[EvalSuite, Path]] = []
        for path in sorted((REPO / "evals/datasets").glob("*.suite.json")):
            out.append((EvalSuite.load(path), path))
        assert len(out) >= 3
        return out

    def test_datasets_bind_to_real_repo_skills(self) -> None:
        skill_files = {
            s.skill_id: p
            for p in (REPO / "skills").rglob("*.yaml")
            if p.stem != "uskill"
            for s in [load_skill(p)]
        }
        for suite_obj, path in self._suites():
            assert suite_obj.skill in skill_files, f"{path.name}: {suite_obj.skill}"

    def test_suites_are_deterministic_and_have_assertions(self) -> None:
        for suite_obj, path in self._suites():
            assert suite_obj.version, path.name
            for case in suite_obj.cases:
                assert case.assertions, f"{path.name}:{case.task_id} lacks assertions"

    def test_all_datasets_run_offline_end_to_end(self) -> None:
        library = SkillLibrary()
        library.load_directory(REPO / "skills")
        payload = {
            "summary": "s", "key_points": ["k"],
            "translated_text": "t", "detected_source_lang": "zh", "confidence": 0.9,
            "keywords": ["w"], "translation": "tr", "processing_time": "1s",
            "result": "r",
        }
        for suite_obj, path in self._suites():
            skill = library.resolve(suite_obj.skill)
            assert skill is not None, path.name
            provider = MockProvider(json.dumps(payload, ensure_ascii=False))
            runtime = SkillRuntime(provider, library=library)
            report = run_eval_suite(runtime, skill, suite_obj)
            assert report.metrics["task_success_rate"] == 1.0, path.name
            assert report.metrics["consistency"] is None
        assert provider.calls  # model path exercised
