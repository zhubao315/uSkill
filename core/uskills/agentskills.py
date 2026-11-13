"""Agent Skills open-standard compatibility layer.

The Agent Skills open specification (agentskills.io, stewarded by the
Linux Foundation Agentic AI Foundation) defines a portable skill folder:

    skill-name/
    ├── SKILL.md          # required: YAML frontmatter + body instructions
    ├── scripts/          # optional deterministic scripts
    ├── references/       # optional progressive-disclosure docs
    └── assets/           # optional resources

This module validates, imports, exports, and inspects that layout **without
ever modifying the official frontmatter**. uSkill's own engineering contract
lives in a separate ``uskill.yaml`` manifest next to ``SKILL.md``.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml  # type: ignore

from .manifest import USkillManifest, dump_manifest

# Official name rules: 1-64 chars, lowercase letters/digits/hyphens.
_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_MAX_NAME = 64
_MAX_DESCRIPTION = 1024

SKILL_FILE = "SKILL.md"
OPTIONAL_DIRS = ("scripts", "references", "assets")

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.DOTALL)


@dataclass
class AgentSkillPackage:
    """Parsed Agent Skills directory."""

    path: Path
    name: str | None = None
    description: str | None = None
    frontmatter: dict[str, Any] = field(default_factory=dict)
    body: str = ""
    has_skill_md: bool = False
    files: list[str] = field(default_factory=list)

    @property
    def sha256(self) -> str:
        skill_md = self.path / SKILL_FILE
        if not skill_md.exists():
            return ""
        return hashlib.sha256(skill_md.read_bytes()).hexdigest()


def _parse_frontmatter(skill_md_path: Path) -> tuple[dict[str, Any], str, list[str]]:
    errors: list[str] = []
    text = skill_md_path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text, ["missing YAML frontmatter (file must start with ---)"]
    raw, body = match.group(1), match.group(2)
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return {}, body, [f"invalid YAML frontmatter: {exc}"]
    if not isinstance(data, dict):
        return {}, body, ["frontmatter must be a YAML mapping"]
    return data, body, errors


def inspect_agent_skill(path: str | Path) -> AgentSkillPackage:
    """Parse an Agent Skill directory into an AgentSkillPackage."""
    root = Path(path)
    pkg = AgentSkillPackage(path=root)
    skill_md = root / SKILL_FILE
    if skill_md.exists():
        pkg.has_skill_md = True
        fm, body, _ = _parse_frontmatter(skill_md)
        pkg.frontmatter = fm
        pkg.body = body
        pkg.name = fm.get("name") if isinstance(fm.get("name"), str) else None
        pkg.description = (
            fm.get("description") if isinstance(fm.get("description"), str) else None
        )
    for item in sorted(root.rglob("*")):
        if item.is_file():
            pkg.files.append(str(item.relative_to(root)))
    return pkg


def validate_agent_skill(path: str | Path) -> tuple[bool, list[str]]:
    """Validate a directory against the Agent Skills spec.

    Checks the required file, frontmatter shape, the strict name rules
    (and directory-name match), description limits, and references.

    Returns:
        (is_valid, list_of_issues). Empty issue list on success.
    """
    root = Path(path)
    issues: list[str] = []

    if not root.is_dir():
        return False, [f"not a directory: {root}"]

    skill_md = root / SKILL_FILE
    if not skill_md.exists():
        return False, [f"missing required file {SKILL_FILE}"]

    pkg = inspect_agent_skill(root)
    fm = pkg.frontmatter

    name = fm.get("name")
    if not isinstance(name, str) or not name:
        issues.append("frontmatter 'name' is required")
    else:
        if len(name) > _MAX_NAME:
            issues.append(f"name must be <= {_MAX_NAME} chars")
        if not _NAME_RE.match(name):
            issues.append("name must be lowercase letters/digits separated by single hyphens")
        if name != root.name:
            issues.append(f"name {name!r} must match parent directory {root.name!r}")

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc:
        issues.append("frontmatter 'description' is required")
    elif len(desc) > _MAX_DESCRIPTION:
        issues.append(f"description must be <= {_MAX_DESCRIPTION} chars")

    for key, _value in fm.items():
        if key not in {
            "name",
            "description",
            "license",
            "compatibility",
            "allowed-tools",
            "metadata",
        }:
            issues.append(f"unsupported frontmatter key {key!r} (do not extend the official schema)")
    if "license" in fm and not isinstance(fm["license"], str):
        issues.append("license must be a string")
    if "allowed-tools" in fm and not isinstance(fm["allowed-tools"], list):
        issues.append("allowed-tools must be a list")

    body_lines = len(pkg.body.splitlines())
    if body_lines > 500:
        issues.append(f"{SKILL_FILE} body is {body_lines} lines; keep under 500 (progressive disclosure)")

    if issues:
        return False, issues

    for ref in _referenced_paths(pkg.body, root):
        if not (root / ref).exists():
            issues.append(f"referenced file does not exist: {ref}")

    return (not issues), issues


def _referenced_paths(body: str, root: Path) -> list[str]:
    """Relative path references inside references/scripts/assets dirs."""
    refs: set[str] = set()
    pattern = re.compile(r"(?:references|scripts|assets)/[\w./-]+")
    for match in pattern.finditer(body):
        refs.add(match.group(0))
    return sorted(refs)


def import_agent_skill(
    path: str | Path,
    output_dir: str | Path | None = None,
    *,
    force: bool = False,
) -> tuple[Path, USkillManifest, list[str]]:
    """Import a standard Agent Skill folder into the uSkill two-layer form.

    Keeps SKILL.md as-is and generates a ``uskill.yaml`` manifest beside it.
    Never silently drops data: conversion notes are returned.

    Returns:
        (skill_dir, manifest, notes).
    """
    src = Path(path)
    valid, issues = validate_agent_skill(src)
    if not valid and not force:
        raise ValueError(f"refusing to import invalid Agent Skill: {issues}")

    pkg = inspect_agent_skill(src)
    notes = [
        "SKILL.md kept verbatim (standard layer unchanged)",
        "generated uskill.yaml manifest (uSkill augmentation layer)",
    ]

    from .builder.scan import scan_risk_level, scan_scripts
    from .governance.risk import RiskLevel

    scripts_dir = src / "scripts"
    scripts_present = scripts_dir.is_dir() and any(p.is_file() for p in scripts_dir.rglob("*"))
    findings = scan_scripts(scripts_dir)
    risk: RiskLevel = max(
        scan_risk_level(findings) if findings else RiskLevel.L0,
        RiskLevel.L3 if scripts_present else RiskLevel.L0,
    )
    if findings:
        notes.append(
            f"SECURITY SCAN: {len(findings)} high-risk pattern(s) in scripts/ "
            f"(min derived risk L{int(scan_risk_level(findings))}); "
            "scripts are NEVER executed by uSkill"
        )
        for f in findings[:5]:
            notes.append(f"  - scripts/{f.file}:{f.line_no} {f.pattern_id}: {f.description}")
    elif scripts_present:
        notes.append(
            "scripts/ present: executable surface raises floor risk to L3 "
            "(static scan found no high-risk patterns; scripts are NEVER executed)"
        )

    from .manifest import (
        ManifestMetadata,
        ManifestProvenance,
        ManifestSecurity,
        dump_manifest,
    )


    manifest = USkillManifest(
        metadata=ManifestMetadata(
            name=pkg.name or src.name,
            description=(pkg.description or "")[:_MAX_DESCRIPTION],
            version=str(pkg.frontmatter.get("metadata", {}).get("version", "0.1.0")),
            license=str(pkg.frontmatter.get("license", "MIT"))[:200],
            owner=str(pkg.frontmatter.get("metadata", {}).get("owner", "imported")),
        ),
        compatibility={"agents": ["agent-skills"]},
        security=ManifestSecurity(
            untrusted_source=True,
            risk_level=f"L{int(risk)}",
        ),
        provenance=ManifestProvenance(
            source="imported",
            imported_from=str(src),
            content_sha256=pkg.sha256,
            notes=f"imported at runtime; {len(issues)} validation note(s)",
        ),
    )

    target = Path(output_dir) if output_dir else src
    dump_manifest(manifest, target)
    return target, manifest, notes


def export_agent_skill(
    manifest: USkillManifest,
    skill_md: str,
    output_dir: str | Path,
    *,
    force: bool = False,
) -> Path:
    """Export a uSkill Manifest + instructions into a standard Agent Skill dir.

    The official frontmatter only carries spec fields; uSkill governance
    travels in the companion uskill.yaml, so no data is silently dropped.
    """
    name = manifest.metadata.name
    out = Path(output_dir) / name
    if out.exists() and not force:
        raise FileExistsError(f"target exists (use force to overwrite): {out}")
    out.mkdir(parents=True, exist_ok=True)

    frontmatter: dict[str, Any] = {"name": name, "description": manifest.metadata.description}
    if manifest.metadata.license:
        frontmatter["license"] = manifest.metadata.license
    if manifest.tools:
        frontmatter["allowed-tools"] = [t.id for t in manifest.tools]

    (out / SKILL_FILE).write_text(
        "---\n"
        + yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
        + "---\n\n"
        + skill_md.strip()
        + "\n",
        encoding="utf-8",
    )
    dump_manifest(manifest, out)
    return out


def inspect_compatibility(manifest: USkillManifest) -> list[str]:
    """Report which uSkill-specific capabilities are NOT expressible in pure
    Agent Skills frontmatter (so users know what is lost on a one-way export)."""
    notes: list[str] = []
    if manifest.execution.mode.value != "instruction":
        notes.append(
            f"execution.mode={manifest.execution.mode.value!r} has no Agent Skills equivalent"
        )
    if manifest.inputs or manifest.outputs:
        notes.append("typed input/output JSON Schema is uSkill-only")
    if any(t.permission.value != "read" for t in manifest.tools):
        notes.append("tool permission enforcement is uSkill-runtime-only")
    if manifest.security.allowed_permissions:
        notes.append("security.allowed_permissions is uSkill-only")
    if manifest.provenance.content_sha256:
        notes.append("content hash / provenance is uSkill-only")
    return notes


def agent_skill_to_dict(pkg: AgentSkillPackage) -> dict[str, Any]:
    return {
        "path": str(pkg.path),
        "name": pkg.name,
        "description": pkg.description,
        "has_skill_md": pkg.has_skill_md,
        "files": pkg.files,
        "sha256": pkg.sha256,
    }


__all__ = [
    "AgentSkillPackage",
    "SKILL_FILE",
    "OPTIONAL_DIRS",
    "inspect_agent_skill",
    "validate_agent_skill",
    "import_agent_skill",
    "export_agent_skill",
    "inspect_compatibility",
    "agent_skill_to_dict",
]
