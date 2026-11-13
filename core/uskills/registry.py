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
from pathlib import Path
from typing import Any

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
        modes = (
            ["name", "tag", "domain", "keyword", "dependency"]
            if mode == "auto"
            else [mode]
        )
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


__all__ = ["SkillRegistry", "SearchHit"]
