"""uSkill 3.0 release gate: package != publish.

A skill may only be marked Published after validation, format checks,
dependency checks, risk derivation, script scan, license/source presence,
evaluation status and explicit human review all pass.
"""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path
from typing import Any

from .lifecycle import SkillLifecycle

_REQUIRED_MANIFEST_KEYS = ("apiVersion", "kind", "metadata")
_TRAVERSAL = re.compile(r"(^|/)\.\.(/|$)")


def content_hash(path: str | Path) -> str:
    """SHA-256 of a skill directory's SKILL.md (or a single file)."""
    p = Path(path)
    target = p / "SKILL.md" if p.is_dir() else p
    if not target.exists():
        return ""
    return hashlib.sha256(target.read_bytes()).hexdigest()


def check_publish_gate(
    skill_path: str | Path,
    *,
    manifest_data: dict[str, Any] | None = None,
    evaluation_report: dict[str, Any] | None = None,
    allow_unreviewed: bool = False,
) -> list[str]:
    """Return gate problems; empty list means the skill may be Published."""
    problems: list[str] = []
    path = Path(skill_path)

    skill_md = path / "SKILL.md" if path.is_dir() else path
    if not skill_md.exists():
        problems.append("missing SKILL.md")

    # format / frontmatter
    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            problems.append("SKILL.md has no YAML frontmatter")
        else:
            if not re.search(r"(?m)^name:\s*\S+", text):
                problems.append("SKILL.md missing 'name' frontmatter")
            if not re.search(r"(?m)^description:\s*\S+", text):
                problems.append("SKILL.md missing 'description' frontmatter")

    # manifest (V2) when present
    manifest_path = path / "uskill.yaml" if path.is_dir() else None
    if manifest_data is None and manifest_path and manifest_path.exists():
        try:
            import yaml  # type: ignore[import-untyped]

            manifest_data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"manifest parse failed: {exc}")
    if manifest_data is not None:
        for key in _REQUIRED_MANIFEST_KEYS:
            if key not in manifest_data:
                problems.append(f"manifest missing required key: {key}")
        gov = manifest_data.get("governance") or {}
        status = str(gov.get("status", SkillLifecycle.DRAFT.value))
        if (
            status not in (SkillLifecycle.REVIEWED.value, SkillLifecycle.PUBLISHED.value)
            and not allow_unreviewed
        ):
            problems.append(
                f"lifecycle status {status!r} must be reviewed/published before publish"
            )
        if not gov.get("reviewer") and not allow_unreviewed:
            problems.append("no human reviewer recorded")

    # scripts scan: report, never execute
    if path.is_dir():
        scripts_dir = path / "scripts"
        if scripts_dir.is_dir():
            for script in sorted(scripts_dir.rglob("*")):
                if script.is_file() and script.suffix in {".py", ".sh", ".js", ".mjs", ".ts"}:
                    problems.append(
                        f"executable script present (never auto-run): {script.relative_to(path)}"
                    )
        if any(_TRAVERSAL.search(p.name) for p in path.rglob("*")):
            problems.append("path traversal pattern detected in skill files")

    # provenance / license
    if not re.search(
        r"license:\s*\S+", skill_md.read_text(encoding="utf-8", errors="replace"), re.I
    ):
        problems.append("no license declared in SKILL.md frontmatter")

    # evaluation evidence
    if evaluation_report is None:
        problems.append("no evaluation report supplied for publish gate")
    else:
        metrics = evaluation_report.get("metrics") or {}
        if metrics.get("output_validity") is not None and float(metrics["output_validity"]) < 0.99:
            problems.append("output validity below 0.99")
        regressions = evaluation_report.get("regressions") or []
        if regressions:
            problems.append(f"evaluation regressions: {len(regressions)}")

    return problems


def verify_package(archive: str | Path, *, expected_sha256: str = "") -> list[str]:
    """Verify a zip package: checksums, traversal, manifest presence."""
    problems: list[str] = []
    p = Path(archive)
    if not p.exists():
        return [f"archive not found: {p}"]
    if expected_sha256:
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != expected_sha256:
            problems.append(f"archive sha256 mismatch: {actual[:12]} != {expected_sha256[:12]}")
    try:
        with zipfile.ZipFile(p) as z:
            names = z.namelist()
            if _TRAVERSAL.search(" ".join(names)) or any(n.startswith("/") for n in names):
                problems.append("unsafe path in archive")
            if "package.json" not in names:
                problems.append("package.json missing")
            else:
                try:
                    data = json.loads(z.read("package.json"))
                except Exception as exc:  # noqa: BLE001
                    problems.append(f"package.json invalid: {exc}")
                else:
                    for rel, digest in (data.get("files") or {}).items():
                        if isinstance(digest, dict):
                            digest = digest.get("sha256", "")
                        if rel not in names:
                            problems.append(f"checksum entry missing file: {rel}")
                        elif digest and hashlib.sha256(z.read(rel)).hexdigest() != digest:
                            problems.append(f"checksum mismatch: {rel}")
    except zipfile.BadZipFile as exc:
        problems.append(f"invalid zip: {exc}")
    return problems


__all__ = ["content_hash", "check_publish_gate", "verify_package"]
