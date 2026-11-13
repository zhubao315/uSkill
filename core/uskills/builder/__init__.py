"""Skill Builder: unified import, task IR, quality scoring, review pipeline.

Principles (from the engineering charter):

* AI/text output is untrusted: every candidate passes programmatic checks.
* Deterministic, evidence-backed scoring — no vibes-based numbers.
* Generated skills are Draft: publication requires human review (lifecycle).
"""

from .importer import SourceDoc, import_source
from .ir import StepKind, TaskIR, build_ir
from .pipeline import BuildCandidate, BuildReport, build_skills
from .quality import QualityScore, score_skill
from .scan import ScanFinding, scan_risk_level, scan_scripts

__all__ = [
    "SourceDoc",
    "import_source",
    "StepKind",
    "TaskIR",
    "build_ir",
    "QualityScore",
    "score_skill",
    "BuildCandidate",
    "BuildReport",
    "build_skills",
    "ScanFinding",
    "scan_scripts",
    "scan_risk_level",
]
