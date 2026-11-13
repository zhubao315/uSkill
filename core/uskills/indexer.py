"""uSkill Indexer Module.

This module builds skill indexes from directories of uSkill files,
generating markdown documentation for skill catalogs.

Improvements over the first version:

* scans ``.yaml`` / ``.yml`` / ``.json`` (previously only ``.yaml``);
* skips ``uskill.*`` manifest files (different schema);
* skills without ``source`` trace are grouped as "(standalone)";
* invalid files are reported with details instead of being silently skipped;
* duplicate skill IDs across files are detected and surfaced.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .validator import load_skill

STANDALONE_GROUP = "(standalone)"


def _skill_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in ("*.yaml", "*.yml", "*.json"):
        files.extend(root.rglob(pattern))
    return sorted(
        set(
            f
            for f in files
            if f.stem != "uskill" and "evals" not in f.parts
        )
    )


def _collect(skills_dir: str | Path) -> dict[str, Any]:
    """Single scan used by both index building and stats."""
    root = Path(skills_dir)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    category_stats: dict[str, int] = defaultdict(int)
    errors: list[dict[str, str]] = []
    ids_seen: dict[str, list[str]] = defaultdict(list)

    for path in _skill_files(root):
        try:
            skill = load_skill(path)
        except Exception as exc:
            errors.append({"path": str(path), "error": str(exc).splitlines()[0]})
            continue
        group = skill.source.sop_name if skill.source else STANDALONE_GROUP
        grouped[group].append(
            {
                "skill_id": skill.skill_id,
                "name": skill.meta.name,
                "category": skill.meta.category.value,
                "domain": skill.meta.domain,
                "version": skill.meta.version,
            }
        )
        category_stats[skill.meta.category.value] += 1
        ids_seen[skill.skill_id].append(str(path))

    duplicates = {sid: paths for sid, paths in ids_seen.items() if len(paths) > 1}
    return {
        "grouped": grouped,
        "category_stats": dict(category_stats),
        "errors": errors,
        "duplicates": duplicates,
        "total_skills": sum(len(v) for v in grouped.values()),
    }


def _anchor(value: str) -> str:
    """Convert string to markdown anchor."""
    lowered = value.strip().lower()
    chars: list[str] = []
    for char in lowered:
        if char.isalnum() or "\u4e00" <= char <= "\u9fff":
            chars.append(char)
        elif char in {"-", " ", "_"}:
            chars.append("-")
    return "".join(chars).strip("-") or "section"


def _format_skill_entry(skill_data: dict[str, Any]) -> str:
    """Format a single skill entry for markdown table."""
    return (
        f"| `{skill_data['skill_id']}` | {skill_data['name']} | "
        f"{skill_data['category']} | {skill_data['domain']} | "
        f"{skill_data['version']} |"
    )


def build_skills_index(skills_dir: str | Path, output_path: str | Path) -> Path:
    """Build markdown skills index from skill directory.

    Args:
        skills_dir: Directory containing skill files.
        output_path: Output path for generated index.

    Returns:
        Path to generated index file.
    """
    data = _collect(skills_dir)
    grouped: dict[str, list[dict[str, Any]]] = data["grouped"]
    errors: list[dict[str, str]] = data["errors"]
    duplicates: dict[str, list[str]] = data["duplicates"]

    total_skills = data["total_skills"]
    total_groups = len(grouped)

    entries: list[str] = [
        "# 技能仓库",
        "",
        f"共收录 **{total_skills}** 个技能，来源于 **{total_groups}** 个 SOP / 技能源。",
        "",
    ]

    if errors:
        entries.extend(['!!! warning "加载警告"', ""])
        entries.append(f"    {len(errors)} 个技能文件加载失败：")
        entries.append("")
        for item in errors:
            entries.append(f"    - `{item['path']}`: {item['error']}")
        entries.append("")

    if duplicates:
        entries.extend(['!!! danger "重复 Skill ID"', ""])
        for sid, paths in sorted(duplicates.items()):
            entries.append(f"    - `{sid}` 出现在: {', '.join(paths)}")
        entries.append("")

    entries.extend(["## 分类统计", ""])
    for category, count in sorted(data["category_stats"].items()):
        entries.append(f"- **{category}**: {count} 个技能")

    entries.extend(["", "## 分类导览", ""])
    for source_name, items in sorted(grouped.items()):
        anchor = _anchor(source_name)
        entries.append(f"- [{source_name}](#{anchor}) ({len(items)} 个技能)")

    for source_name, items in sorted(grouped.items()):
        entries.extend(
            [
                "",
                f"## {source_name}",
                "",
                f"技能数：**{len(items)}**",
                "",
                "| Skill ID | Name | Category | Domain | Version |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for item in items:
            entries.append(_format_skill_entry(item))

    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(entries) + "\n", encoding="utf-8")
    return target


def get_skill_stats(skills_dir: str | Path) -> dict[str, Any]:
    """Get statistics about skills in directory."""
    data = _collect(skills_dir)
    return {
        "total_skills": data["total_skills"],
        "total_sources": len(data["grouped"]),
        "categories": data["category_stats"],
        "invalid_files": len(data["errors"]),
        "duplicate_ids": len(data["duplicates"]),
    }
