"""Skill lifecycle: gated publishing pipeline.

Draft → Validated → Reviewed → Published → Deprecated

A skill may never jump to Published without passing the gates; a model
that *generated* a skill must not be the only reviewer of it.
"""

from __future__ import annotations

from enum import StrEnum


class SkillLifecycle(StrEnum):
    DRAFT = "draft"
    VALIDATED = "validated"
    REVIEWED = "reviewed"
    PUBLISHED = "published"
    DEPRECATED = "deprecated"


ALLOWED_TRANSITIONS: dict[SkillLifecycle, set[SkillLifecycle]] = {
    SkillLifecycle.DRAFT: {SkillLifecycle.VALIDATED, SkillLifecycle.DEPRECATED},
    SkillLifecycle.VALIDATED: {SkillLifecycle.REVIEWED, SkillLifecycle.DRAFT, SkillLifecycle.DEPRECATED},
    SkillLifecycle.REVIEWED: {SkillLifecycle.PUBLISHED, SkillLifecycle.DRAFT, SkillLifecycle.DEPRECATED},
    SkillLifecycle.PUBLISHED: {SkillLifecycle.DEPRECATED},
    SkillLifecycle.DEPRECATED: set(),
}


class LifecycleError(ValueError):
    """Raised on an illegal lifecycle transition."""


def can_transition(current: SkillLifecycle, target: SkillLifecycle) -> bool:
    return target in ALLOWED_TRANSITIONS[current]


def assert_transition(current: SkillLifecycle, target: SkillLifecycle) -> None:
    if not can_transition(current, target):
        raise LifecycleError(
            f"illegal lifecycle transition {current.value} -> {target.value}; "
            f"allowed from {current.value}: "
            f"{sorted(t.value for t in ALLOWED_TRANSITIONS[current])}"
        )


__all__ = [
    "SkillLifecycle",
    "ALLOWED_TRANSITIONS",
    "LifecycleError",
    "can_transition",
    "assert_transition",
]
