"""Risk classification L0–L4, derived from actual capabilities.

Risk is what a skill *can* do, never what its author claims: derived from
the executable surface (scripts on disk), the permission class of every
resolvable tool, declared network use, and whether execution pauses for a
human. Skill YAML is data; this module is the judge.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any

from ..schema import USkill


class RiskLevel(IntEnum):
    L0 = 0  # pure text instructions
    L1 = 1  # read-only data processing
    L2 = 2  # gated tool use
    L3 = 3  # scripts / file modification / shell
    L4 = 4  # external systems / sensitive data / high-risk actions


RISK_LABELS: dict[int, str] = {
    0: "pure text instructions",
    1: "read-only data processing",
    2: "restricted tool use",
    3: "scripts or file/shell access",
    4: "external systems or sensitive data",
}


@dataclass
class RiskAssessment:
    level: RiskLevel
    factors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "level": f"L{int(self.level)}",
            "label": RISK_LABELS[int(self.level)],
            "factors": self.factors,
        }


def assess_skill_risk(
    skill: USkill,
    *,
    has_scripts: bool = False,
    tool_permissions: list[str] | None = None,
) -> RiskAssessment:
    """Derive the risk level of a skill from its real capabilities.

    ``tool_permissions`` lists the permission classes of every tool the
    skill can actually reach (registered or resolvable). Unregistered
    declared tools do NOT raise the level — the runtime cannot invoke
    them, which is exactly the point.
    """
    factors: list[str] = []
    level = RiskLevel.L0

    if has_scripts:
        level = max(level, RiskLevel.L3)
        factors.append("skill directory contains scripts (executable surface)")

    perms = set(tool_permissions or [])
    if perms:
        level = max(level, RiskLevel.L2)
        factors.append(f"reachable tools: {sorted(perms)}")
    if perms & {"write", "shell"}:
        level = max(level, RiskLevel.L3)
        factors.append("tools with write/shell permission")
    if perms & {"network", "sensitive_data"}:
        level = max(level, RiskLevel.L4)
        factors.append("tools with network or sensitive-data permission")

    if skill.execute.requires_approval:
        factors.append("execution gated by human approval (mitigation)")

    return RiskAssessment(level=level, factors=factors or ["pure text instructions"])


def skill_directory_flags(skill_dir: str | Path) -> dict[str, Any]:
    """Inspect a two-layer skill directory for capability flags."""
    root = Path(skill_dir)
    scripts_dir = root / "scripts"
    scripts = (
        sorted(p.name for p in scripts_dir.iterdir() if p.is_file())
        if scripts_dir.is_dir()
        else []
    )
    return {"has_scripts": bool(scripts), "scripts": scripts}


def tool_permissions_for(skill: USkill, registry: Any = None) -> list[str]:
    """Permission classes of declared tools that are actually resolvable."""
    perms: list[str] = []
    if registry is None:
        return perms
    for name in skill.execute.tools:
        tool = registry.get(name)
        if tool is not None:
            perms.append(str(tool.permission.value if hasattr(tool.permission, "value") else tool.permission))
    return perms


__all__ = [
    "RiskLevel",
    "RISK_LABELS",
    "RiskAssessment",
    "assess_skill_risk",
    "skill_directory_flags",
    "tool_permissions_for",
]
