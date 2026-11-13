"""Tool Registry and Skill Library for uSkill Runtime.

Tools are real callables registered centrally with an ID, description,
JSON schemas and a permission class. A skill's YAML text only *declares*
which tools it wants; the runtime decides whether they may run.

The Skill Library indexes loaded USkill objects so composite skills can
resolve and execute their sub-skills for real.
"""

from __future__ import annotations

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeoutError
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..errors import ExecutionFailedError, ProviderError
from ..governance.policy import Permission, PermissionPolicy
from ..schema import USkill
from ..validator import load_skill

# Errors that retry logic may consider transient.
TRANSIENT_ERRORS: tuple[type[BaseException], ...] = (
    ProviderError,
    FutureTimeoutError,
    TimeoutError,
    ConnectionError,
)


@dataclass
class ToolDef:
    """A registered, callable tool."""

    id: str
    description: str
    func: Callable[..., Any]
    permission: Permission = Permission.read
    input_schema: dict[str, Any] | None = None
    output_schema: dict[str, Any] | None = None
    timeout: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class ToolRegistry:
    """Central registry of invokable tools (incl. MCP-proxied ones)."""

    def __init__(self, policy: PermissionPolicy | None = None):
        self._tools: dict[str, ToolDef] = {}
        self.policy = policy or PermissionPolicy()

    def register(self, tool: ToolDef) -> None:
        if tool.id in self._tools:
            raise ValueError(f"tool already registered: {tool.id}")
        self._tools[tool.id] = tool

    def register_tool(
        self,
        id: str,
        func: Callable[..., Any],
        description: str = "",
        permission: Permission = Permission.read,
        timeout: float | None = None,
        **kwargs: Any,
    ) -> ToolDef:
        tool = ToolDef(
            id=id, description=description, func=func, permission=permission,
            timeout=timeout, metadata=kwargs,
        )
        self.register(tool)
        return tool

    def get(self, tool_id: str) -> ToolDef | None:
        return self._tools.get(tool_id)

    def names(self) -> list[str]:
        return sorted(self._tools)

    def invoke(self, tool_id: str, payload: dict[str, Any]) -> Any:
        """Invoke a tool through the permission gate and timeout guard."""
        tool = self.get(tool_id)
        if tool is None:
            raise ExecutionFailedError(f"unknown tool: {tool_id!r}")
        self.policy.check(tool.permission)
        if tool.timeout:
            with ThreadPoolExecutor(max_workers=1) as pool:
                future = pool.submit(tool.func, payload)
                try:
                    return future.result(timeout=tool.timeout)
                except FutureTimeoutError as exc:
                    raise ExecutionFailedError(
                        f"tool {tool_id!r} timed out after {tool.timeout}s"
                    ) from exc
        return tool.func(payload)


class SkillLibrary:
    """In-memory index of usable skills, resolvable by several keys."""

    def __init__(self) -> None:
        self._skills: dict[str, USkill] = {}

    def register(self, skill: USkill) -> None:
        keys = {skill.skill_id, skill.meta.name}
        slug = skill.skill_id.split("-", 2)[-1].rsplit("-v", 1)[0]
        keys.add(slug)
        keys.add(slug.replace("-", "_"))
        for key in keys:
            self._skills[key] = skill

    def load_directory(self, root: str | Path) -> int:
        """Load all legacy skill YAML/JSON files under ``root``.

        Files named ``uskill.*`` are manifest documents, not skills, and
        are skipped.
        """
        count = 0
        root_path = Path(root)
        for pattern in ("*.yaml", "*.yml", "*.json"):
            for path in sorted(root_path.rglob(pattern)):
                if path.stem == "uskill":
                    continue
                try:
                    self.register(load_skill(path))
                    count += 1
                except Exception:
                    continue
        return count

    def resolve(self, name: str) -> USkill | None:
        return self._skills.get(name)

    def names(self) -> list[str]:
        return sorted({s.meta.name for s in self._skills.values()})

    def all(self) -> list[USkill]:
        seen: dict[str, USkill] = {}
        for skill in self._skills.values():
            seen[skill.skill_id] = skill
        return list(seen.values())


__all__ = ["ToolDef", "ToolRegistry", "SkillLibrary", "TRANSIENT_ERRORS"]
