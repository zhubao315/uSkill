"""Tests for the evaluation harness (deterministic graders + comparison)."""

from __future__ import annotations

from core.uskills.evaluation import EvalAssertion, EvalCase, EvalSuite, run_case, run_eval_suite
from core.uskills.runtime import MockProvider, SkillRuntime
from core.uskills.validator import load_skill


def _runtime(script: str) -> SkillRuntime:
    return SkillRuntime(MockProvider(script))


class TestAssertions:
    def test_contains(self) -> None:
        assert EvalAssertion(type="contains", value="risk").check({"text": "a risk here"})

    def test_regex(self) -> None:
        assert EvalAssertion(type="regex", value=r"\d+ bugs").check("found 3 bugs")

    def test_json_key_and_type(self) -> None:
        assert EvalAssertion(type="json_key", key="keywords").check({"keywords": []})
        assert EvalAssertion(type="json_type", key="n", value="integer").check({"n": 2})

    def test_equals(self) -> None:
        assert EvalAssertion(type="equals", value="x").check("x")


class TestEvalSuite:
    def test_case_passes_with_matching_output(self) -> None:
        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        case = EvalCase(
            task_id="t1",
            user_input={"text": "abc"},
            assertions=[EvalAssertion(type="json_key", key="keywords")],
        )
        result = run_case(_runtime('{"keywords": ["a"], "summary": "s"}'), skill, case)
        assert result.passed

    def test_case_fails_on_bad_output(self) -> None:
        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        case = EvalCase(
            task_id="t1",
            user_input={"text": "abc"},
            assertions=[EvalAssertion(type="json_key", key="keywords")],
        )
        result = run_case(_runtime('{"nope": 1}'), skill, case)
        assert not result.passed

    def test_suite_roundtrip(self, tmp_path) -> None:
        suite = EvalSuite(
            skill="demo",
            version="1.0.0",
            cases=[EvalCase(task_id="a", user_input={"text": "x"})],
        )
        path = suite.save(tmp_path / "eval" / "suite.json")
        loaded = EvalSuite.load(path)
        assert loaded.cases[0].task_id == "a"

    def test_baseline_vs_assisted_comparison(self) -> None:
        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        suite = EvalSuite(
            skill=skill.skill_id,
            cases=[
                EvalCase(
                    task_id="t1",
                    user_input={"text": "abc"},
                    baseline_prompt="extract keywords",
                    assertions=[EvalAssertion(type="json_key", key="keywords")],
                )
            ],
        )

        # Stub provider that behaves like a model but is NOT MockProvider,
        # so run_baseline actually executes. It always answers correctly.
        class StubProvider:
            name = "stub"

            def __init__(self, answer: str) -> None:
                self.answer = answer

            from core.uskills.runtime.providers import ProviderCapabilities

            capabilities = ProviderCapabilities()

            def complete(self, messages, **kwargs):
                from core.uskills.runtime.providers import ProviderResponse

                return ProviderResponse(text=self.answer, model="stub", usage={})

        from core.uskills.runtime import SkillRuntime

        # Both baseline and skill-assisted pass: delta == 0.
        report = run_eval_suite(
            SkillRuntime(StubProvider('{"keywords": ["k"], "summary": "s"}')), skill, suite
        )
        assert report.baseline_rate == 1.0
        assert report.assisted_rate == 1.0
        assert report.delta == 0.0
        assert "baseline success" in report.to_markdown()

    def test_comparison_shows_skill_improvement(self) -> None:
        skill = load_skill("skills/atomic/text_keyword_extract.yaml")
        suite = EvalSuite(
            skill=skill.skill_id,
            cases=[
                EvalCase(
                    task_id="t1",
                    user_input={"text": "abc"},
                    baseline_prompt="extract keywords",
                    assertions=[EvalAssertion(type="json_key", key="keywords")],
                )
            ],
        )

        class StubProvider:
            name = "stub"

            from core.uskills.runtime.providers import ProviderCapabilities

            capabilities = ProviderCapabilities()

            def complete(self, messages, **kwargs):
                from core.uskills.runtime.providers import ProviderResponse

                # Baseline call carries the baseline prompt: answer wrongly.
                user_text = messages[-1].content
                answer = (
                    "{}"
                    if "extract keywords" in user_text
                    else '{"keywords": ["k"], "summary": "s"}'
                )
                return ProviderResponse(text=answer, model="stub", usage={})

        from core.uskills.runtime import SkillRuntime

        report = run_eval_suite(SkillRuntime(StubProvider()), skill, suite)
        # The skill makes the task pass while the bare baseline fails.
        assert report.baseline_rate == 0.0
        assert report.assisted_rate == 1.0
        assert report.delta == 1.0
