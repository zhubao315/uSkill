"""Task-level intermediate representation (IR).

The IR sits between raw SOP text and skill candidates so that step
*semantics* (atomic / decision / approval / loop) are classified before
any skill is generated. Classification is keyword-heuristic, deterministic
and evidence-bearing — never an LLM vibe.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import StrEnum

from ..converter import SopDocument, parse_sop


class StepKind(StrEnum):
    ATOMIC = "atomic"
    DECISION = "decision"
    APPROVAL = "approval"
    LOOP = "loop"


# Deterministic marker vocabularies (zh + en). Order = precedence.
_MARKERS: dict[StepKind, re.Pattern[str]] = {
    StepKind.APPROVAL: re.compile(
        r"审批|审核|批准|复核|人工确认|转人工|需.*授权|主管|approval|approve|review by|sign-?off",
        re.I,
    ),
    StepKind.DECISION: re.compile(
        r"如果|若|当.{1,20}时|否则|判断|是否|根据.{0,12}(选择|决定)|条件|if\b|else|whether|decide",
        re.I,
    ),
    StepKind.LOOP: re.compile(
        r"循环|重复|直到|每(次|日|周|月)|批量处理|遍历|for each|loop|repeat|until", re.I
    ),
}


@dataclass
class StepIR:
    text: str
    kind: StepKind = StepKind.ATOMIC
    nested_details: list[str] = field(default_factory=list)
    evidence: str = ""

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "kind": self.kind.value,
            "details": self.nested_details,
            "evidence": self.evidence,
        }


@dataclass
class TaskIR:
    """Structured understanding of one source document."""

    source_name: str
    goal: str = ""
    steps: list[StepIR] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    context: str = ""

    def kind_summary(self) -> dict[str, int]:
        summary: dict[str, int] = {}
        for s in self.steps:
            summary[s.kind.value] = summary.get(s.kind.value, 0) + 1
        return summary

    @property
    def has_approval(self) -> bool:
        return any(s.kind is StepKind.APPROVAL for s in self.steps)

    def to_dict(self) -> dict:
        return {
            "source_name": self.source_name,
            "goal": self.goal,
            "steps": [s.to_dict() for s in self.steps],
            "constraints": self.constraints,
            "step_kind_summary": self.kind_summary(),
        }


def classify_step(text: str) -> tuple[StepKind, str]:
    """Classify one step; returns (kind, evidence description)."""
    for kind in (StepKind.APPROVAL, StepKind.DECISION, StepKind.LOOP):
        m = _MARKERS[kind].search(text)
        if m:
            return kind, f"{kind.value} marker: '{m.group(0)}'"
    return StepKind.ATOMIC, "no decision/approval/loop markers"


def build_ir(text: str, source_name: str = "source") -> TaskIR:
    """Derive a TaskIR from raw SOP/prompt text (deterministic)."""
    doc: SopDocument = parse_sop(text)
    ir = TaskIR(source_name=source_name)

    headings = [b.text for b in doc.blocks if b.kind == "heading"]
    paragraphs = [b.text for b in doc.blocks if b.kind == "paragraph"]
    ir.goal = headings[0] if headings else (paragraphs[0][:200] if paragraphs else source_name)
    ir.constraints = paragraphs[1:] if not headings else paragraphs
    ir.context = "\n".join(
        f"{b.kind}: {b.text}" for b in doc.blocks if b.kind in ("heading", "paragraph", "table_row")
    )

    top_positions = [i for i, b in enumerate(doc.blocks) if b.kind == "list_item" and b.depth == 0]
    for pos in top_positions:
        block = doc.blocks[pos]
        kind, evidence = classify_step(block.text)
        step = StepIR(text=block.text, kind=kind, evidence=evidence)
        for later in doc.blocks[pos + 1 :]:
            if later.kind == "list_item" and later.depth > 0:
                step.nested_details.append(later.text)
            else:
                break
        ir.steps.append(step)
    return ir
