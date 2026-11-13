"""Skill evaluation harness (evidence-based quality).

Answers one question: **does this skill actually improve task completion?**

Design constraints:

* the model never grades itself alone — deterministic graders are required;
* comparison runs No-Skill baseline vs Skill-assisted with identical
  model/tools/params;
* results are recorded per version for regression tracking.
"""

from __future__ import annotations

import json
import re
import statistics
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .runtime import SkillRuntime, StepState
from .schema import USkill


class EvalAssertion(BaseModel):
    """One deterministic assertion on the output."""

    model_config = ConfigDict(extra="forbid")

    type: str = Field(..., pattern=r"^(contains|regex|json_key|equals|json_type)$")
    key: str | None = None
    value: Any = None

    def check(self, output: Any) -> bool:
        text = output if isinstance(output, str) else json.dumps(output, ensure_ascii=False)
        if self.type == "contains":
            return str(self.value) in text
        if self.type == "regex":
            return re.search(str(self.value), text, re.DOTALL) is not None
        if self.type == "json_key":
            return isinstance(output, dict) and self.key in output
        if self.type == "json_type":
            target = output.get(self.key) if isinstance(output, dict) else output
            py_types: dict[str, type | tuple[type, ...]] = {
                "string": str, "integer": int, "number": (int, float),
                "boolean": bool, "object": dict, "array": list,
            }
            expected = py_types.get(str(self.value), object)
            return bool(isinstance(target, expected))
        if self.type == "equals":
            return bool(output == self.value)
        return False


class EvalCase(BaseModel):
    """One evaluation case: an input plus expected behavior."""

    model_config = ConfigDict(extra="forbid")

    task_id: str
    user_input: dict[str, Any] = Field(default_factory=dict)
    baseline_prompt: str | None = Field(
        default=None, description="Instruction used for the No-Skill baseline"
    )
    assertions: list[EvalAssertion] = Field(default_factory=list)
    security_probe: bool = Field(
        default=False, description="Case checks the skill resists prompt injection"
    )


class EvalSuite(BaseModel):
    """Versioned collection of evaluation cases for one skill."""

    model_config = ConfigDict(extra="forbid")

    skill: str
    version: str = "0.0.0"
    cases: list[EvalCase] = Field(default_factory=list)

    @classmethod
    def load(cls, path: str | Path) -> EvalSuite:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(**data)

    def save(self, path: str | Path) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(json.loads(self.model_dump_json()), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return target


@dataclass
class EvalResult:
    """Outcome of running one case with one configuration."""

    task_id: str
    passed: bool
    detail: str = ""
    output: Any = None


@dataclass
class EvalReport:
    """Aggregated comparison report."""

    skill: str
    baseline: list[EvalResult] = field(default_factory=list)
    assisted: list[EvalResult] = field(default_factory=list)
    latency_ms: dict[str, float] = field(default_factory=dict)

    @property
    def baseline_rate(self) -> float:
        return _rate(self.baseline)

    @property
    def assisted_rate(self) -> float:
        return _rate(self.assisted)

    @property
    def delta(self) -> float:
        return self.assisted_rate - self.baseline_rate

    def to_dict(self) -> dict[str, Any]:
        return {
            "skill": self.skill,
            "baseline_success_rate": round(self.baseline_rate, 4),
            "assisted_success_rate": round(self.assisted_rate, 4),
            "delta_pp": round(self.delta * 100, 2),
            "cases": {
                r.task_id: {
                    "baseline": r.passed,
                    "assisted": next(
                        (x.passed for x in self.assisted if x.task_id == r.task_id), None
                    ),
                }
                for r in self.baseline
            },
        }

    def to_markdown(self) -> str:
        rows = ["| task | baseline | assisted |", "| --- | --- | --- |"]
        for r in self.baseline:
            a = next((x for x in self.assisted if x.task_id == r.task_id), None)
            rows.append(
                f"| `{r.task_id}` | {'✓' if r.passed else '✗'} | "
                f"{'✓' if a and a.passed else '✗'} |"
            )
        return "\n".join(
            [
                f"# Eval report: {self.skill}",
                "",
                f"- baseline success: {self.baseline_rate:.0%}",
                f"- assisted success: {self.assisted_rate:.0%}",
                f"- delta: {self.delta * 100:+.1f} pp",
                "",
                *rows,
            ]
        )


def _rate(results: list[EvalResult]) -> float:
    if not results:
        return 0.0
    return sum(1 for r in results if r.passed) / len(results)


def run_case(runtime: SkillRuntime, skill: USkill, case: EvalCase) -> EvalResult:
    """Run one case with the skill and check deterministic assertions."""
    try:
        record = runtime.run(skill, case.user_input)
    except Exception as exc:  # noqa: BLE001 - evaluation must not crash
        return EvalResult(case.task_id, False, f"execution error: {exc}")
    if record.status is not StepState.COMPLETED:
        return EvalResult(case.task_id, False, f"status={record.status.value} error={record.error}")
    output = record.result
    for assertion in case.assertions:
        if not assertion.check(output):
            return EvalResult(
                case.task_id, False, f"assertion {assertion.type}({assertion.key or assertion.value}) failed", output
            )
    return EvalResult(case.task_id, True, "ok", output)


def run_baseline(runtime: SkillRuntime, case: EvalCase, model: str = "gpt-4o-mini") -> EvalResult:
    """No-Skill baseline: same model, plain instruction, no skill contract."""
    from .runtime import MockProvider  # local import to avoid cycles at module load

    provider = runtime.provider
    if case.baseline_prompt is None or isinstance(provider, MockProvider):
        return EvalResult(case.task_id, False, "no baseline prompt defined")
    try:
        response = provider.complete(
            [_sys(), _user(case.baseline_prompt, case.user_input)],
            model=model,
            temperature=0.1,
            json_mode=True,
            timeout=60,
        )
    except Exception as exc:  # noqa: BLE001
        return EvalResult(case.task_id, False, f"baseline error: {exc}")
    try:
        output = json.loads(response.text)
    except json.JSONDecodeError:
        output = response.text
    for assertion in case.assertions:
        if not assertion.check(output):
            return EvalResult(case.task_id, False, "baseline assertion failed", output)
    return EvalResult(case.task_id, True, "ok", output)


def _sys() -> Any:
    from .runtime import Message

    return Message("system", "You are a helpful assistant. Answer the task directly.")


def _user(prompt: str, inputs: dict[str, Any]) -> Any:
    from .runtime import Message

    return Message("user", prompt + "\n\nInput:\n" + json.dumps(inputs, ensure_ascii=False))


def run_eval_suite(
    runtime: SkillRuntime,
    skill: USkill,
    suite: EvalSuite,
    *,
    repeats: int = 1,
) -> EvalReport:
    """Run baseline vs skill-assisted over the suite and compare."""
    report = EvalReport(skill=suite.skill)
    latencies: list[float] = []
    for case in suite.cases:
        report.baseline.append(run_baseline(runtime, case, model=skill.execute.model))
        results = []
        for _ in range(repeats):
            start = time.monotonic()
            result = run_case(runtime, skill, case)
            latencies.append((time.monotonic() - start) * 1000.0)
            results.append(result)
        passed = [r for r in results if r.passed]
        # Majority vote across repeats; deterministic assertion outcome.
        assisted = passed[0] if len(passed) * 2 > len(results) else results[0]
        report.assisted.append(assisted)
    report.latency_ms = {"mean": statistics.mean(latencies) if latencies else 0.0}
    return report


__all__ = [
    "EvalAssertion",
    "EvalCase",
    "EvalSuite",
    "EvalResult",
    "EvalReport",
    "run_case",
    "run_baseline",
    "run_eval_suite",
]
