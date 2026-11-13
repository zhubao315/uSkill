"""Unified exception hierarchy for uSkill.

All uSkill exceptions derive from :class:`USkillError` so callers can catch
a single base type. Existing module-specific errors (``ConversionError``,
``ValidationError``) were migrated to derive from this base while keeping
their historic import locations working.
"""

from __future__ import annotations


class USkillError(Exception):
    """Base class for all uSkill errors."""


class USkillValidationError(USkillError):
    """Raised when a skill file or data fails schema/semantic validation."""


class ConversionFailedError(USkillError):
    """Raised when an SOP cannot be converted into skills."""


class ExecutionFailedError(USkillError):
    """Raised when a skill run fails in a non-recoverable way."""


class ProviderError(USkillError):
    """Raised when a model provider call fails."""

    def __init__(self, message: str, *, retryable: bool = False) -> None:
        super().__init__(message)
        self.retryable = retryable


class PermissionDeniedError(USkillError):
    """Raised when a runtime action violates the permission policy."""


class ApprovalRequiredError(USkillError):
    """Raised when a run is waiting for human approval."""


__all__ = [
    "USkillError",
    "USkillValidationError",
    "ConversionFailedError",
    "ExecutionFailedError",
    "ProviderError",
    "PermissionDeniedError",
    "ApprovalRequiredError",
]
