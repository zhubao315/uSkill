"""Skill Registry: local skill repository with metadata search.

Storage is the filesystem (Git-friendly), in line with the lightweight
charter — no database. The indexer stays responsible for generated
Markdown catalogs; THIS module is the query surface (five search modes,
per the 2.0 charter):

* ``name``       — exact/partial name, slug or skill_id
* ``tag``        — tag membership
* ``domain``     — domain equality
* ``keyword``    — description/name text match
* ``dependency`` — skills whose declared tools/DAG reference the query
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC
from pathlib import Path
from typing import Any

from .agentskills import SKILL_FILE, inspect_agent_skill, validate_agent_skill
from .schema import USkill
from .validator import load_skill


@dataclass
class SearchHit:
    skill_id: str
    name: str
    path: str
    category: str
    domain: str
    tags: list[str] = field(default_factory=list)
    matched_by: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "name": self.name,
            "path": self.path,
            "category": self.category,
            "domain": self.domain,
            "tags": self.tags,
            "matched_by": self.matched_by,
        }


class SkillRegistry:
    """Filesystem-backed registry with metadata search and health checks."""

    def __init__(self, root: str | Path = "skills"):
        self.root = Path(root)
        self._entries: list[tuple[Path, USkill]] = []
        self.broken: list[tuple[Path, str]] = []
        self.load()

    def load(self) -> int:
        """(Re)load every loadable legacy skill under ``root``."""
        self._entries = []
        self.broken = []
        for pattern in ("*.yaml", "*.yml", "*.json"):
            for path in sorted(self.root.rglob(pattern)):
                if path.stem == "uskill" or "evals" in path.parts:
                    continue
                try:
                    self._entries.append((path, load_skill(path)))
                except Exception as exc:  # noqa: BLE001 - report, keep going
                    self.broken.append((path, str(exc)))
        return len(self._entries)

    # -- basic access -------------------------------------------------------

    def all(self) -> list[USkill]:
        return [skill for _, skill in self._entries]

    def get(self, skill_id: str) -> USkill | None:
        return next((s for _, s in self._entries if s.skill_id == skill_id), None)

    def path_of(self, skill_id: str) -> Path | None:
        return next((p for p, s in self._entries if s.skill_id == skill_id), None)

    # -- five search modes ----------------------------------------------------

    def search(self, query: str, *, mode: str = "auto", limit: int = 50) -> list[SearchHit]:
        """Search skills; ``auto`` runs all modes with mode-priority ranking."""
        q = query.strip().lower()
        if not q:
            return []
        modes = ["name", "tag", "domain", "keyword", "dependency"] if mode == "auto" else [mode]
        hits: dict[str, SearchHit] = {}
        for m in modes:
            for path, skill in self._entries:
                if skill.skill_id in hits:
                    continue
                how = self._matches(skill, q, m)
                if how:
                    hits[skill.skill_id] = SearchHit(
                        skill_id=skill.skill_id,
                        name=skill.meta.name,
                        path=str(path),
                        category=skill.meta.category.value,
                        domain=skill.meta.domain,
                        tags=list(skill.meta.tags),
                        matched_by=how,
                    )
        return list(hits.values())[:limit]

    @staticmethod
    def _matches(skill: USkill, q: str, mode: str) -> str:
        slug = skill.skill_id.split("-", 2)[-1].rsplit("-v", 1)[0]
        name = skill.meta.name.lower()
        if mode == "name":
            if q == skill.skill_id or q == name or q == slug.lower():
                return "name:exact"
            if q in name or q in slug.lower() or q in skill.skill_id:
                return "name:partial"
        elif mode == "tag":
            if q in {t.lower() for t in skill.meta.tags}:
                return "tag"
        elif mode == "domain":
            if q == skill.meta.domain.lower():
                return "domain"
        elif mode == "keyword":
            if q in skill.meta.description.lower() or q in name:
                return "keyword"
        elif mode == "dependency":
            declared = {t.lower() for t in skill.execute.tools}
            if any(q == d or q in d or d in q for d in declared) or q in {
                k.lower() for k in skill.execute.depends_on
            }:
                return "dependency"
        return ""

    # -- health ---------------------------------------------------------------

    def health(self) -> dict[str, Any]:
        """Registry health: counts, broken files, duplicate ids."""
        ids = [s.skill_id for _, s in self._entries]
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        return {
            "skills": len(ids),
            "broken": [{"path": str(p), "error": e} for p, e in self.broken],
            "duplicate_ids": dupes,
            "ok": not self.broken and not dupes,
        }


__all__ = ["SkillRegistry", "SearchHit", "SkillRecord", "SkillRegistryV3"]


# ---------- Unified record -------------------------------------------------


@dataclass
class SkillRecord:
    """One normalized skill asset. Multiple records may share an identity."""

    skill_id: str
    name: str
    description: str
    format: str  # "legacy-yaml" | "manifest-v2" | "agent-skill" | "agent-skill+manifest"
    path: str
    category: str = ""
    domain: str = ""
    tags: list[str] = field(default_factory=list)
    content_hash: str = ""
    version: str = ""
    source: str = "local"
    source_url: str = ""
    license: str = ""
    compatible_agents: list[str] = field(default_factory=list)
    lifecycle_status: str = "draft"
    eval_status: str = "unknown"
    risk_level: str = "L0"
    trust_status: str = "untrusted"
    discovered_at: str = ""
    issues: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "name": self.name,
            "description": self.description,
            "format": self.format,
            "path": self.path,
            "category": self.category,
            "domain": self.domain,
            "tags": self.tags,
            "content_hash": self.content_hash,
            "version": self.version,
            "source": self.source,
            "source_url": self.source_url,
            "license": self.license,
            "compatible_agents": self.compatible_agents,
            "lifecycle_status": self.lifecycle_status,
            "eval_status": self.eval_status,
            "risk_level": self.risk_level,
            "trust_status": self.trust_status,
            "discovered_at": self.discovered_at,
            "issues": self.issues,
        }


# ---------- Registry 3.0 additions ---------------------------------------


class SkillRegistryV3:
    """Extends SkillRegistry with multi-format discovery and unified records."""

    def __init__(self, root: str | Path = "skills", *, extra_roots: list[str | Path] | None = None):
        self.roots = [Path(root)] + [Path(p) for p in (extra_roots or [])]
        self.records: list[SkillRecord] = []
        self.broken: list[dict[str, str]] = []
        self.duplicates: dict[str, list[str]] = {}
        self.load()

    @staticmethod
    def _now() -> str:
        from datetime import datetime

        return datetime.now(UTC).isoformat(timespec="seconds")

    def _safe_rel(self, p: Path, base: Path) -> str:
        try:
            return str(p.relative_to(base))
        except ValueError:
            return str(p)

    def load(self) -> int:
        self.records = []
        self.broken = []
        self.duplicates = {}
        for base in self.roots:
            self._load_legacy(base)
            self._load_agent_skills(base)
        self._detect_duplicates()
        return len(self.records)

    # -- legacy --------------------------------------------------------------

    def _load_legacy(self, base: Path) -> None:
        if not base.exists():
            return
        for pattern in ("*.yaml", "*.yml", "*.json"):
            for path in sorted(base.rglob(pattern)):
                if path.stem == "uskill" or "evals" in path.parts:
                    continue
                try:
                    # from .validator import load_skill  (real module)
                    skill = load_skill(path)  # noqa: F821 - provided by real module
                    self.records.append(
                        SkillRecord(
                            skill_id=skill.skill_id,
                            name=skill.meta.name,
                            description=skill.meta.description,
                            format="legacy-yaml",
                            path=self._safe_rel(path, base),
                            category=skill.meta.category.value,
                            domain=skill.meta.domain,
                            tags=list(skill.meta.tags),
                            discovered_at=self._now(),
                        )
                    )
                except Exception as exc:  # noqa: BLE001
                    self.broken.append({"path": str(path), "error": str(exc)})

    # -- agent skills ---------------------------------------------------------

    def _load_agent_skills(self, base: Path) -> None:
        if not base.exists():
            return
        for skill_md in sorted(base.rglob(SKILL_FILE)):  # noqa: F821 - imported in real module
            root = skill_md.parent
            if any(part in {".git", "node_modules", "__pycache__"} for part in root.parts):
                continue
            if any(r.skill_id == f"agent-skill:{self._safe_rel(root, base)}" for r in self.records):
                continue
            try:
                pkg = inspect_agent_skill(root)  # noqa: F821
                valid, issues = validate_agent_skill(root)  # noqa: F821
                name = pkg.name or root.name
                desc = pkg.description or ""
                # content hash of SKILL.md is the version identity
                chash = pkg.sha256
                has_manifest = (root / "uskill.yaml").exists()
                record = SkillRecord(
                    skill_id=f"agent-skill:{self._safe_rel(root, base)}",
                    name=name,
                    description=desc[:1024],
                    format="agent-skill+manifest" if has_manifest else "agent-skill",
                    path=self._safe_rel(root, base),
                    tags=list(pkg.frontmatter.get("tags") or []),
                    content_hash=chash,
                    version=str(pkg.frontmatter.get("version") or ""),
                    source="local",
                    license=str(pkg.frontmatter.get("license") or ""),
                    compatible_agents=["agent-skills-compatible"],
                    trust_status="untrusted",
                    discovered_at=self._now(),
                    issues=[] if valid else issues,
                )
                self.records.append(record)
                if not valid:
                    self.broken.append({"path": str(skill_md), "error": "; ".join(issues[:3])})
            except Exception as exc:  # noqa: BLE001
                self.broken.append({"path": str(skill_md), "error": str(exc)})

    # -- dedup / conflict -----------------------------------------------------

    def _detect_duplicates(self) -> None:
        by_hash: dict[str, list[str]] = {}
        for record in self.records:
            if record.content_hash:
                by_hash.setdefault(record.content_hash, []).append(record.skill_id)
        self.duplicates = {h: ids for h, ids in by_hash.items() if len(ids) > 1}
        # same name + different content = conflict, surface as broken
        by_name: dict[str, set[str]] = {}
        for record in self.records:
            by_name.setdefault(record.name.lower(), set()).add(
                record.content_hash or record.skill_id
            )
        for name, hashes in by_name.items():
            if len(hashes) > 1:
                self.broken.append(
                    {"path": f"name:{name}", "error": "same name, different content hashes"}
                )

    # -- query surface --------------------------------------------------------

    def all_records(self) -> list[SkillRecord]:
        return list(self.records)

    def record(self, skill_id: str) -> SkillRecord | None:
        return next((r for r in self.records if r.skill_id == skill_id), None)

    SEARCH_FIELDS = (
        "name",
        "description",
        "keyword",
        "tag",
        "domain",
        "dependency",
        "source",
        "agent",
        "risk",
        "lifecycle",
        "evaluation",
        "format",
    )

    def search_records(
        self,
        query: str,
        *,
        mode: str = "auto",
        category: str | None = None,
        source_type: str | None = None,
        status: str | None = None,
        limit: int = 50,
    ) -> list[SkillRecord]:
        q = query.strip().lower()
        modes = self.SEARCH_FIELDS if mode == "auto" else (mode,)
        out: list[SkillRecord] = []
        for record in self.records:
            if category and record.category.lower() != category.lower():
                continue
            if source_type and record.format != source_type:
                continue
            if status and record.lifecycle_status.lower() != status.lower():
                continue
            if q and not any(self._record_matches(record, q, m) for m in modes):
                continue
            out.append(record)
        return out[:limit]

    @staticmethod
    def _record_matches(r: SkillRecord, q: str, mode: str) -> bool:
        hay = {
            "name": r.name.lower(),
            "description": r.description.lower(),
            "keyword": f"{r.name} {r.description}".lower(),
            "tag": " ".join(t.lower() for t in r.tags),
            "domain": r.domain.lower(),
            "dependency": " ".join(f.lower() for f in r.format.split()),
            "source": r.source.lower(),
            "agent": " ".join(a.lower() for a in r.compatible_agents),
            "risk": r.risk_level.lower(),
            "lifecycle": r.lifecycle_status.lower(),
            "evaluation": r.eval_status.lower(),
            "format": r.format.lower(),
        }
        value = hay.get(mode, "")
        return q in value if value else False

    def health(self) -> dict[str, Any]:
        return {
            "skills": len(self.records),
            "by_format": {
                f: sum(1 for r in self.records if r.format == f)
                for f in sorted({r.format for r in self.records})
            },
            "broken": self.broken,
            "duplicates": self.duplicates,
            "ok": not self.broken and not self.duplicates,
        }

    def report(self) -> dict[str, Any]:
        return {
            "generated_at": self._now(),
            "roots": [str(p) for p in self.roots],
            "health": self.health(),
            "records": [r.to_dict() for r in self.records],
        }


__all__ = ["SkillRecord", "SkillRegistryV3"]
