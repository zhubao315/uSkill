"""Deterministic, evidence-backed skill quality scoring (0-100).

Every point awarded carries a human-readable evidence string. The scorer
never asks a model for opinions; it inspects the artifact.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from ..schema import USkill

_SECRET = re.compile(r"(api[_-]?key|secret|token|password)\s*[:=]\s*\S", re.I)


@dataclass
class Dimension:
    name: str
    max: int
    score: int
    evidence: list[str] = field(default_factory=list)


@dataclass
class QualityScore:
    total: int
    dimensions: list[Dimension]

    @property
    def review_required(self) -> bool:
        return self.total < 70

    def to_dict(self) -> dict[str, Any]:
        return {
            "total": self.total,
            "review_required": self.review_required,
            "dimensions": [
                {
                    "name": d.name,
                    "max": d.max,
                    "score": d.score,
                    "evidence": d.evidence,
                }
                for d in self.dimensions
            ],
        }


def score_skill(skill: USkill) -> QualityScore:
    """Score one skill candidate across seven dimensions."""
    dims: list[Dimension] = []

    # 1. Goal clarity (15)
    desc = skill.meta.description.strip()
    goal = Dimension("goal_clarity", 15, 0)
    if 20 <= len(desc) <= 300:
        goal.score = 15
        goal.evidence.append(f"description length {len(desc)} in [20,300]")
    elif desc:
        goal.score = 8
        goal.evidence.append(f"description present but length {len(desc)} outside [20,300]")
    else:
        goal.evidence.append("description missing")
    dims.append(goal)

    # 2. Input completeness (15)
    inp = Dimension("input_completeness", 15, 0)
    from ..validator import validate_template_variables

    names = [p.name for p in skill.input.params]
    ok, undefined = validate_template_variables(skill.execute.prompt_template, names)
    if ok:
        inp.score += 10
        inp.evidence.append("all template variables declared")
    else:
        inp.evidence.append(f"undefined template vars: {undefined}")
    documented = [p for p in skill.input.params if p.description]
    if skill.input.params and len(documented) == len(skill.input.params):
        inp.score += 5
        inp.evidence.append("all params documented")
    else:
        inp.evidence.append("some params lack descriptions")
    dims.append(inp)

    # 3. Output verifiability (20)
    out = Dimension("output_verifiability", 20, 0)
    if skill.output.params:
        out.score += 12
        out.evidence.append(f"declared output params: {skill.output.params}")
    if skill.output.format == "json":
        out.score += 4
        out.evidence.append("json format enables schema checks")
    if skill.output.validation_rules:
        out.score += 4
        out.evidence.append(f"{len(skill.output.validation_rules)} validation rules")
    if not out.evidence:
        out.evidence.append("no output params, no json format, no validation rules")
    dims.append(out)

    # 4. Step integrity (15)
    st = Dimension("step_integrity", 15, 0)
    if skill.execute.steps:
        st.score += 8
        st.evidence.append(f"{len(skill.execute.steps)} execution steps")
    if "{{" in skill.execute.prompt_template:
        st.score += 7
        st.evidence.append("prompt binds declared inputs")
    if not st.evidence:
        st.evidence.append("no execution steps and no bound inputs in prompt")
    dims.append(st)

    # 5. Boundary awareness (10)
    bd = Dimension("boundary_awareness", 10, 0)
    ctx = (skill.source.context if skill.source else "") or ""
    if ctx:
        bd.score += 5
        bd.evidence.append("source context/constraints preserved")
    if any(k in (desc + ctx).lower() for k in ("不适用", "不要", "仅当", "not for", "do not")):
        bd.score += 5
        bd.evidence.append("negative boundary stated")
    else:
        bd.evidence.append("no explicit negative boundary")
    dims.append(bd)

    # 6. Traceability (10)
    tr = Dimension("traceability", 10, 0)
    if skill.source and skill.source.sop_path:
        tr.score = 10
        tr.evidence.append(f"source path {skill.source.sop_path}")
    elif skill.source:
        tr.score = 6
        tr.evidence.append("source name only (no file path)")
    else:
        tr.evidence.append("no source provenance")
    dims.append(tr)

    # 7. Safety & discoverability (15)
    saf = Dimension("safety_discoverability", 15, 0)
    blob = skill.execute.prompt_template + desc
    if _SECRET.search(blob):
        saf.evidence.append("possible embedded secret — must fix")
    else:
        saf.score += 10
        saf.evidence.append("no secret-like literals")
    if skill.meta.tags:
        saf.score += 5
        saf.evidence.append(f"tags: {skill.meta.tags}")
    else:
        saf.evidence.append("no tags (discoverability)")
    dims.append(saf)

    total = sum(d.score for d in dims)
    return QualityScore(total=total, dimensions=dims)
