"""uSkill Agent Install Hub (3.0 Phase 2).

AgentTargetAdapter instances describe WHERE a given Agent discovers skills.
No adapter executes an Agent, downloads remote content, or overwrites an
existing skill without an explicit, confirmed InstallPlan.

All paths are derived from official documentation / well-known environment
variables; see docs/workbench/AGENT_CONNECTORS.md for citations.
"""

from __future__ import annotations

import hashlib
import os
import shutil
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

from .agentskills import SKILL_FILE, inspect_agent_skill


class InstallScope(StrEnum):
    USER = "user"
    PROJECT = "project"


class SyncStatus(StrEnum):
    UP_TO_DATE = "up-to-date"
    UPDATE_AVAILABLE = "update-available"
    LOCALLY_MODIFIED = "locally-modified"
    CONFLICT = "conflict"
    MISSING = "missing"
    UNMANAGED = "unmanaged"


@dataclass
class SkillLocation:
    scope: InstallScope
    path: Path
    priority: int = 50


@dataclass
class InstalledSkill:
    name: str
    path: Path
    content_hash: str = ""
    source: str = "unmanaged"

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "path": str(self.path),
            "content_hash": self.content_hash,
            "source": self.source,
        }


@dataclass
class InstallAction:
    kind: str  # "copy" | "symlink" | "external-tool"
    source: Path
    target: Path
    reason: str = ""


@dataclass
class InstallPlan:
    target_agent: str
    scope: InstallScope
    skill_name: str
    source_path: Path
    actions: list[InstallAction] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    rollback: list[str] = field(default_factory=list)
    approved: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_agent": self.target_agent,
            "scope": self.scope.value,
            "skill_name": self.skill_name,
            "source_path": str(self.source_path),
            "actions": [
                {
                    "kind": a.kind,
                    "source": str(a.source),
                    "target": str(a.target),
                    "reason": a.reason,
                }
                for a in self.actions
            ],
            "conflicts": self.conflicts,
            "risks": self.risks,
            "rollback": self.rollback,
            "approved": self.approved,
        }


@dataclass
class InstallRecord:
    skill_identity: str
    source_hash: str
    installed_hash: str
    target_agent: str
    target_scope: str
    target_path: str
    installed_version: str = ""
    install_method: str = "copy"
    installed_at: str = ""
    last_synced_at: str = ""
    sync_status: str = SyncStatus.UP_TO_DATE.value

    def to_dict(self) -> dict[str, Any]:
        return dict(vars(self))


class AgentTargetAdapter(ABC):
    """Describes one agent's skill directories and install behavior."""

    name: str = "base"
    official_docs: str = ""

    def __init__(self, *, project_root: Path | None = None, home: Path | None = None):
        self.project_root = project_root or Path.cwd()
        self.home = home or Path.home()

    @abstractmethod
    def detect(self) -> bool:
        """Whether this agent appears to be installed/configured."""

    @abstractmethod
    def list_skill_locations(self) -> list[SkillLocation]:
        """All directories this agent scans, with discovery priority."""

    def get_installed_skills(self) -> list[InstalledSkill]:
        out: list[InstalledSkill] = []
        seen: set[str] = set()
        for location in sorted(self.list_skill_locations(), key=lambda x: x.priority):
            if not location.path.is_dir():
                continue
            for skill_md in sorted(location.path.glob(f"*/{SKILL_FILE}")):
                root = skill_md.parent
                if root.name in seen:
                    continue
                seen.add(root.name)
                pkg = inspect_agent_skill(root)
                out.append(
                    InstalledSkill(
                        name=pkg.name or root.name,
                        path=root,
                        content_hash=pkg.sha256,
                        source=f"{self.name}:{location.scope.value}",
                    )
                )
        return out

    def preview_install(self, source_skill: Path, scope: InstallScope) -> InstallPlan:
        """Build a plan. Never writes. Must be confirmed before install()."""
        pkg = inspect_agent_skill(source_skill)
        name = pkg.name or source_skill.name
        locations = [loc for loc in self.list_skill_locations() if loc.scope == scope]
        if not locations:
            return InstallPlan(
                self.name,
                scope,
                name,
                source_skill,
                conflicts=[f"no {scope.value} skill location for {self.name}"],
            )
        target_dir = locations[0].path / name
        plan = InstallPlan(
            target_agent=self.name, scope=scope, skill_name=name, source_path=source_skill
        )
        if target_dir.exists():
            existing = inspect_agent_skill(target_dir)
            if existing.sha256 == pkg.sha256:
                plan.risks.append("identical skill already installed (no-op)")
            else:
                plan.conflicts.append(
                    f"{target_dir} already exists with different content "
                    f"(installed={existing.sha256[:12]}, source={pkg.sha256[:12]})"
                )
            plan.rollback.append(f"preserve existing directory: {target_dir}")
        else:
            plan.actions.append(
                InstallAction("copy", source_skill, target_dir, "copy verified skill directory")
            )
            plan.rollback.append(f"remove installed directory: {target_dir}")
        plan.risks.append("scripts in the skill are never executed during install")
        plan.risks.append("external source remains untrusted until validated")
        return plan

    def install(self, plan: InstallPlan) -> InstallRecord:
        """Execute an APPROVED plan atomically (copy to temp, then rename)."""
        if not plan.approved:
            raise PermissionError("InstallPlan must be approved before install()")
        if plan.conflicts:
            raise RuntimeError(
                "cannot install with unresolved conflicts: " + "; ".join(plan.conflicts)
            )
        record = InstallRecord(
            skill_identity=plan.skill_name,
            source_hash=_file_hash(plan.source_path / SKILL_FILE),
            installed_hash="",
            target_agent=self.name,
            target_scope=plan.scope.value,
            target_path="",
            install_method="copy",
            installed_at=_now(),
        )
        for action in plan.actions:
            if action.kind != "copy":
                raise ValueError(f"unsupported install action: {action.kind}")
            if action.target.exists():
                raise FileExistsError(f"refusing to overwrite: {action.target}")
            action.target.parent.mkdir(parents=True, exist_ok=True)
            tmp = action.target.with_name(action.target.name + ".uskills-tmp")
            if tmp.exists():
                shutil.rmtree(tmp)
            shutil.copytree(action.source, tmp)
            tmp.rename(action.target)
            record.installed_hash = _file_hash(action.target / SKILL_FILE)
            record.target_path = str(action.target)
        return record

    def uninstall(self, name: str, scope: InstallScope) -> bool:
        for loc in self.list_skill_locations():
            if loc.scope != scope:
                continue
            target = loc.path / name
            if target.is_dir():
                shutil.rmtree(target)
                return True
        return False

    def check_conflicts(self, skill_name: str) -> list[str]:
        conflicts = []
        for loc in self.list_skill_locations():
            target = loc.path / skill_name
            if target.exists():
                conflicts.append(str(target))
        return conflicts

    def sync_status(self, record: InstallRecord) -> SyncStatus:
        path = Path(record.target_path)
        if not path.exists():
            return SyncStatus.MISSING
        current = _file_hash(path / SKILL_FILE)
        if current != record.installed_hash:
            return SyncStatus.LOCALLY_MODIFIED
        if current != record.source_hash:
            return SyncStatus.UPDATE_AVAILABLE
        return SyncStatus.UP_TO_DATE


class CodexAdapter(AgentTargetAdapter):
    name = "codex"
    official_docs = "https://developers.openai.com/codex/skills/"

    def detect(self) -> bool:
        home_base = Path(os.environ.get("CODEX_HOME", self.home / ".codex"))
        return (home_base / "skills").is_dir() or shutil.which("codex") is not None

    def list_skill_locations(self) -> list[SkillLocation]:
        codex_home = Path(os.environ.get("CODEX_HOME", self.home / ".codex"))
        return [
            SkillLocation(InstallScope.PROJECT, self.project_root / ".agents" / "skills", 10),
            SkillLocation(InstallScope.USER, codex_home / "skills", 20),
            SkillLocation(InstallScope.USER, self.home / ".agents" / "skills", 30),
        ]


class ClaudeCodeAdapter(AgentTargetAdapter):
    name = "claude-code"
    official_docs = "https://docs.claude.com/en/docs/claude-code/skills"

    def detect(self) -> bool:
        return (self.home / ".claude").is_dir() or shutil.which("claude") is not None

    def list_skill_locations(self) -> list[SkillLocation]:
        return [
            SkillLocation(InstallScope.PROJECT, self.project_root / ".claude" / "skills", 10),
            SkillLocation(InstallScope.USER, self.home / ".claude" / "skills", 20),
        ]


class OpenCodeAdapter(AgentTargetAdapter):
    name = "opencode"
    official_docs = "https://opencode.ai/docs/skills/"

    def detect(self) -> bool:
        config = Path(os.environ.get("XDG_CONFIG_HOME", self.home / ".config")) / "opencode"
        return config.is_dir() or shutil.which("opencode") is not None

    def list_skill_locations(self) -> list[SkillLocation]:
        config = Path(os.environ.get("XDG_CONFIG_HOME", self.home / ".config")) / "opencode"
        return [
            SkillLocation(InstallScope.PROJECT, self.project_root / ".opencode" / "skills", 10),
            SkillLocation(InstallScope.USER, config / "skills", 20),
            SkillLocation(InstallScope.USER, self.home / ".agents" / "skills", 30),
        ]


def all_adapters(**kwargs: Any) -> list[AgentTargetAdapter]:
    return [CodexAdapter(**kwargs), ClaudeCodeAdapter(**kwargs), OpenCodeAdapter(**kwargs)]


def _file_hash(path: Path) -> str:
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _now() -> str:
    from datetime import UTC, datetime

    return datetime.now(UTC).isoformat(timespec="seconds")


__all__ = [
    "InstallScope",
    "SyncStatus",
    "SkillLocation",
    "InstalledSkill",
    "InstallAction",
    "InstallPlan",
    "InstallRecord",
    "AgentTargetAdapter",
    "CodexAdapter",
    "ClaudeCodeAdapter",
    "OpenCodeAdapter",
    "all_adapters",
]
