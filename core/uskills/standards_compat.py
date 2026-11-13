"""Standards compatibility layer: format detection, migration, reports.

Supports the three coexisting formats:

* ``skill-v1``    legacy USkill YAML (skill_id/meta/...)
* ``manifest-v2`` uSkill Manifest (apiVersion uskills/v2, uskill.yaml)
* ``agent-skill`` standard Agent Skills directory (SKILL.md)

Migration never overwrites and never silently drops data: every lossy
field is listed in the returned :class:`MigrationReport`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml  # type: ignore

from .agentskills import SKILL_FILE, export_agent_skill, validate_agent_skill
from .manifest import USkillManifest, manifest_from_legacy_skill
from .schema import exported_json_schema
from .validator import load_skill

FORMAT_UNKNOWN = "unknown"
FORMAT_SKILL_V1 = "skill-v1"
FORMAT_MANIFEST_V2 = "manifest-v2"
FORMAT_AGENT_SKILL = "agent-skill"

# Fields discouraged in V1 authoring (warned, still loadable).
DEPRECATED_V1_FIELDS: dict[str, str] = {
    "execute.model": (
        "hard-coding a vendor model name couples the skill to one provider; "
        "prefer provider profiles at deploy time (kept for compatibility)"
    ),
}


def manifest_json_schema() -> dict[str, Any]:
    """JSON Schema for the uSkill Manifest (uskill.yaml)."""
    schema = USkillManifest.model_json_schema(ref_template="#/$defs/{model}")
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["$id"] = "https://zhubao315.github.io/uSkill/schema/manifest-v2.json"
    return schema


def detect_format(path: str | Path) -> str:
    """Classify a path as one of the supported formats (never raises)."""
    p = Path(path)
    if p.is_dir():
        if (p / SKILL_FILE).exists():
            return FORMAT_AGENT_SKILL
        for name in ("uskill.yaml", "uskill.yml"):
            if (p / name).exists():
                return FORMAT_MANIFEST_V2
        return FORMAT_UNKNOWN
    if not p.exists():
        return FORMAT_UNKNOWN
    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception:
        return FORMAT_UNKNOWN
    if isinstance(data, dict):
        if data.get("apiVersion") == "uskills/v2":
            return FORMAT_MANIFEST_V2
        if "skill_id" in data and "meta" in data:
            return FORMAT_SKILL_V1
    return FORMAT_UNKNOWN


def deprecation_warnings(skill: Any) -> list[str]:
    """Field-level deprecation warnings for a loaded V1 skill."""
    warnings: list[str] = []
    for dotted, message in DEPRECATED_V1_FIELDS.items():
        section, _, attr = dotted.partition(".")
        obj = getattr(skill, section, None)
        if obj is not None and getattr(obj, attr, None) not in (None, ""):
            warnings.append(f"{dotted}: {message}")
    return warnings


@dataclass
class MigrationReport:
    """Machine-readable outcome of one migration."""

    source: str
    target: str
    format: str
    actions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    lossy: list[str] = field(default_factory=list)
    ok: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "target": self.target,
            "format": self.format,
            "ok": self.ok,
            "actions": self.actions,
            "warnings": self.warnings,
            "lossy_fields": self.lossy,
        }


def migrate_skill(
    path: str | Path,
    output_dir: str | Path,
    *,
    force: bool = False,
    dry_run: bool = False,
) -> MigrationReport:
    """Migrate one legacy V1 skill into a two-layer Agent Skill directory.

    Creates ``<out>/<name>/SKILL.md`` + ``uskill.yaml``. The legacy file is
    never modified. ``dry_run`` reports actions without writing.
    """
    src = Path(path)
    fmt = detect_format(src)
    if fmt != FORMAT_SKILL_V1:
        report = MigrationReport(str(src), "", fmt, ok=False)
        report.actions.append("refused: only legacy skill-v1 files are migrated")
        return report

    skill = load_skill(src)
    manifest = manifest_from_legacy_skill(skill)
    out_root = Path(output_dir)
    target = out_root / manifest.metadata.name
    report = MigrationReport(str(src), str(target), FORMAT_AGENT_SKILL)
    report.warnings.extend(deprecation_warnings(skill))

    from .agentskills import inspect_compatibility

    report.lossy = inspect_compatibility(manifest)
    body = (
        f"# {skill.meta.name}\n\n{skill.meta.description}\n\n"
        "## Instructions\n\n" + skill.execute.prompt_template
    )

    if dry_run:
        report.actions.append(f"would create {target}/SKILL.md + uskill.yaml")
        return report
    if target.exists() and not force:
        report.ok = False
        report.actions.append(f"refused: {target} exists (use force)")
        return report

    export_agent_skill(manifest, body, out_root, force=force)
    valid, issues = validate_agent_skill(target)
    if not valid:
        report.warnings.append(f"exported skill failed validation: {issues}")
    report.actions.append(f"created {target}/SKILL.md + uskill.yaml")
    report.actions.append("legacy file left untouched")
    return report


def migrate_directory(
    root: str | Path,
    output_dir: str | Path,
    *,
    force: bool = False,
    dry_run: bool = False,
) -> list[MigrationReport]:
    """Migrate every legacy skill under ``root`` (manifest/evals skipped)."""
    root_path = Path(root)
    reports: list[MigrationReport] = []
    patterns = ("*.yaml", "*.yml", "*.json")
    files = sorted(
        p
        for pattern in patterns
        for p in root_path.rglob(pattern)
        if p.stem != "uskill" and "evals" not in p.parts
    )
    for file_path in files:
        if detect_format(file_path) == FORMAT_SKILL_V1:
            reports.append(migrate_skill(file_path, output_dir, force=force, dry_run=dry_run))
    return reports


__all__ = [
    "FORMAT_AGENT_SKILL",
    "FORMAT_MANIFEST_V2",
    "FORMAT_SKILL_V1",
    "FORMAT_UNKNOWN",
    "MigrationReport",
    "detect_format",
    "deprecation_warnings",
    "manifest_json_schema",
    "migrate_skill",
    "migrate_directory",
    "exported_json_schema",
]
