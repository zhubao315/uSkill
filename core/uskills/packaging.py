"""Skill packaging: verifiable distribution units (zip + checksum + manifest).

A package is a plain zip (Git/object-store friendly) plus an embedded
``package.json`` with per-file sha256 checksums, so recipients can verify
integrity and see exactly which compatibility layers are inside. No
service, no registry server — verification is offline and deterministic.
"""

from __future__ import annotations

import hashlib
import json
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .standards_compat import FORMAT_AGENT_SKILL, FORMAT_SKILL_V1, detect_format


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@dataclass
class PackageResult:
    path: Path
    sha256: str
    files: list[str]
    manifest: dict[str, Any]


def package_skill(
    path: str | Path,
    output_dir: str | Path = "dist",
    *,
    force: bool = False,
) -> PackageResult:
    """Package one skill (Agent Skill dir or legacy skill file) as a zip.

    The embedded ``package.json`` records format, per-file checksums and
    a compatibility note; the archive itself is checksummed for transport.
    """
    src = Path(path)
    fmt = detect_format(src)
    if fmt == FORMAT_AGENT_SKILL:
        files = sorted(p for p in src.rglob("*") if p.is_file())
        name = src.name
        layers = ["SKILL.md (Agent Skills standard layer)"]
        if any(p.name in ("uskill.yaml", "uskill.yml") for p in files):
            layers.append("uskill.yaml (uSkill governance layer)")
    elif fmt == FORMAT_SKILL_V1:
        files = [src]
        name = src.stem
        layers = ["skill-v1 YAML (migrate to two-layer before wide distribution)"]
    else:
        raise ValueError(f"cannot package unsupported path/format: {src} ({fmt})")

    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    archive = out_root / f"{name}-package.zip"
    if archive.exists() and not force:
        raise ValueError(f"{archive} exists (use force)")

    file_entries = [
        {"path": p.relative_to(src.parent).as_posix(), "sha256": _sha256(p)}
        for p in files
    ]
    package_manifest = {
        "name": name,
        "format": fmt,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "compatibility_layers": layers,
        "files": file_entries,
        "verification": "sha256 per file; compare after unzip",
        "policy": "packages are inert: running them requires a governed runtime",
    }

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in files:
            zf.write(p, p.relative_to(src.parent).as_posix())
        zf.writestr("package.json", json.dumps(package_manifest, ensure_ascii=False, indent=2))

    return PackageResult(
        path=archive,
        sha256=_sha256(archive),
        files=[e["path"] for e in file_entries] + ["package.json"],
        manifest=package_manifest,
    )


__all__ = ["PackageResult", "package_skill"]
