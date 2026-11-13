"""Permission policy and governance primitives for uSkill Runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

from ..errors import PermissionDeniedError


class Permission(StrEnum):
    """Coarse permission classes enforced by the runtime."""

    read = "read"
    write = "write"
    network = "network"
    shell = "shell"
    sensitive_data = "sensitive_data"


@dataclass
class PermissionPolicy:
    """Least-privilege permission allowlist enforced at runtime.

    Skill YAML text is never a security boundary: even if a skill claims
    it may do something, the runtime refuses unless the permission is in
    this policy.
    """

    allow: set[Permission] = field(default_factory=lambda: {Permission.read})

    def check(self, permission: Permission | str) -> None:
        perm = Permission(permission)
        if perm not in self.allow:
            raise PermissionDeniedError(
                f"permission {perm.value!r} is not allowed by the runtime policy "
                f"(allowed: {sorted(p.value for p in self.allow)})"
            )

    def grants(self, permission: Permission | str) -> bool:
        try:
            self.check(permission)
            return True
        except PermissionDeniedError:
            return False


__all__ = ["Permission", "PermissionPolicy"]
