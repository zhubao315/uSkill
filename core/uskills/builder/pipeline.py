"""Builder pipeline: source → IR → candidates → scores → draft outputs.

Output is always Draft-stage: skills land under ``<output>/drafts/`` tagged
``draft`` with a machine-readable report. Publication is a governance step
(lifecycle Review/Publish), never a side effect of conversion.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..converter import convert_sop_text
from ..evaluation import EvalAssertion, EvalCase, EvalSuite
from ..governance.lifecycle import SkillLifecycle
from ..schema import USkill
from .importer import SourceDoc, import_source
from .ir import build_ir
from .quality import QualityScore, score_skill


@dataclass
class BuildCandidate:
    skill: USkill
    score: QualityScore
    lifecycle: SkillLifecycle = SkillLifecycle.DRAFT

    def to_dict(self) -> dict[str, Any]:
        return {
            "skill_id": self.skill.skill_id,
            "lifecycle": self.lifecycle.value,
            "quality": self.score.to_dict(),
        }


@dataclass
class BuildReport:
    source: str
    ir: dict[str, Any]
    candidates: list[BuildCandidate] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def any_review_required(self) -> bool:
        return any(c.score.review_required for c in self.candidates)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "ir": self.ir,
            "candidates": [c.to_dict() for c in self.candidates],
            "notes": self.notes,
            "review_required": self.any_review_required,
            "policy": "generated skills are Draft; publish requires human review",
        }


def _eval_draft(skill: USkill) -> EvalSuite:
    """Seed eval cases from the skill contract (deterministic)."""
    inputs = {p.name: ("x" if p.type.value == "string" else 1) for p in skill.input.params}
    cases = [
        EvalCase(
            task_id="normal-001",
            user_input=inputs,
            baseline_prompt=f"Perform: {skill.meta.description[:120]}",
            assertions=[
                EvalAssertion(type="json_key", key=p) for p in skill.output.params
            ] or [EvalAssertion(type="contains", value="result")],
        ),
        EvalCase(
            task_id="empty-input-001",
            user_input={k: ("" if isinstance(v, str) else v) for k, v in inputs.items()},
            baseline_prompt=f"Perform: {skill.meta.description[:120]}",
            assertions=[EvalAssertion(type="contains", value="result")],
        ),
    ]
    return EvalSuite(skill=skill.skill_id, version="0.1.0-draft", cases=cases)


def build_skills(
    source: str | Path | SourceDoc,
    output_dir: str | Path,
    *,
    domain: str = "general",
    owner: str = "uSkill-builder",
) -> BuildReport:
    """Run the full builder pipeline for one source document."""
    src = source if isinstance(source, SourceDoc) else import_source(source)
    ir = build_ir(src.text, src.name)
    notes: list[str] = []

    if not ir.steps:
        notes.append("no structured steps found; document may need manual authoring")
        return BuildReport(source=src.origin, ir=ir.to_dict(), notes=notes)

    kinds = ir.kind_summary()
    if kinds.get("approval"):
        notes.append(
            f"{kinds['approval']} approval step(s) detected: generated skills "
            "carry requires_approval=true; runtime pauses for human sign-off"
        )
    if kinds.get("decision"):
        notes.append(
            f"{kinds['decision']} decision step(s) detected: review granularity "
            "before splitting into separate skills"
        )
    if kinds.get("loop"):
        notes.append(
            f"{kinds['loop']} loop step(s) detected: enforce iteration budgets in "
            "workflow config"
        )

    skills = convert_sop_text(src.text, src.name, src.origin, domain=domain, owner=owner)

    candidates: list[BuildCandidate] = []
    out_root = Path(output_dir)
    drafts_dir = out_root / "drafts"
    evals_dir = out_root / "evals-draft"
    for skill in skills:
        if ir.has_approval:
            skill.execute.requires_approval = True
        # Tag drafts so tooling can filter them; lifecycle is DRAFT.
        if "draft" not in skill.meta.tags and len(skill.meta.tags) < 20:
            skill.meta.tags = [*skill.meta.tags, "draft"]

        score = score_skill(skill)
        candidates.append(BuildCandidate(skill=skill, score=score))

        drafts_dir.mkdir(parents=True, exist_ok=True)
        (drafts_dir / f"{skill.skill_id}.json").write_text(
            json.dumps(json.loads(skill.model_dump_json(by_alias=True)), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        suite = _eval_draft(skill)
        evals_dir.mkdir(parents=True, exist_ok=True)
        suite.save(evals_dir / f"{skill.skill_id}.suite.json")

    report = BuildReport(source=src.origin, ir=ir.to_dict(), candidates=candidates, notes=notes)
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "build-report.json").write_text(
        json.dumps(report.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return report
