"""uSkill Manifest V2 (``uskill.yaml``).

The manifest is uSkill's *augmentation layer* that sits next to a standard
Agent Skill directory (``skill-name/SKILL.md``). It never modifies the
official frontmatter; instead it carries the uSkill-specific engineering
contract: typed inputs/outputs, execution mode, tool permissions,
governance and provenance.

This is a uSkill-owned extension format, not part of the Agent Skills
open specification.
"""

from __future__ import annotations

import json
import re
from enum import StrEnum
from pathlib import Path
from typing import Any, Literal

import yaml  # type: ignore
from pydantic import BaseModel, ConfigDict, Field

from .governance.lifecycle import SkillLifecycle

API_VERSION: Literal["uskills/v2"] = "uskills/v2"
KIND: Literal["Skill"] = "Skill"

_NAME_OK = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class ExecutionMode(StrEnum):
    """How a skill is executed.

    Not every skill is a single LLM call; the mode makes execution
    semantics explicit.
    """

    instruction = "instruction"  # plain instructions loaded by an agent
    llm = "llm"  # model invocation driven by a prompt/contract
    tool = "tool"  # thin wrapper over a registered tool
    script = "script"  # deterministic script entry point
    workflow = "workflow"  # orchestrates multiple skills/tools


class ToolPermission(StrEnum):
    """Coarse permission classes enforced by the runtime."""

    read = "read"
    write = "write"
    network = "network"
    shell = "shell"
    sensitive_data = "sensitive_data"


class ManifestMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$", max_length=64)
    description: str = Field(..., min_length=1, max_length=1024)
    version: str = Field(default="0.1.0", pattern=r"^\d+\.\d+\.\d+$")
    license: str = Field(default="MIT", max_length=200)
    tags: list[str] = Field(default_factory=list, max_length=20)
    owner: str = Field(default="community", max_length=100)


class ManifestExecution(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mode: ExecutionMode = Field(default=ExecutionMode.instruction)
    entry: str = Field(
        default="SKILL.md",
        max_length=500,
        description="Entry document or script path, relative to the skill directory",
    )
    timeout: int = Field(default=30, ge=1, le=3600)
    retry: int = Field(default=0, ge=0, le=10)
    requires_approval: bool = Field(default=False)


class ManifestTool(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(..., min_length=1, max_length=100)
    permission: ToolPermission = Field(default=ToolPermission.read)
    description: str = Field(default="", max_length=500)


class ManifestSecurity(BaseModel):
    model_config = ConfigDict(extra="forbid")

    untrusted_source: bool = Field(
        default=False,
        description="True when skill content was imported from an external source",
    )
    allowed_permissions: list[ToolPermission] = Field(
        default_factory=lambda: [ToolPermission.read],
        description="Runtime-enforced permission allowlist (default least-privilege)",
    )
    risk_level: str = Field(
        default="",
        pattern=r"^$|^L[0-4]$",
        description="Derived risk level (L0-L4) from actual capabilities; empty = not yet assessed",
    )


class ManifestProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source: str = Field(
        default="authored",
        pattern=r"^(authored|imported|converted|generated)$",
    )
    imported_from: str = Field(default="", max_length=500)
    content_sha256: str = Field(default="", max_length=64, description="sha256 of SKILL.md")
    notes: str = Field(default="", max_length=2000)


class ManifestEvaluation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dataset: str = Field(default="", max_length=500, description="Relative dataset path")
    min_trigger_precision: float = Field(default=0.9, ge=0.0, le=1.0)
    min_output_validity: float = Field(default=0.99, ge=0.0, le=1.0)


class ManifestGovernance(BaseModel):
    """Persistent lifecycle state for a skill (3.0)."""

    model_config = ConfigDict(extra="forbid")

    status: SkillLifecycle = Field(default=SkillLifecycle.DRAFT)
    reviewer: str = Field(default="")
    reviewed_at: str = Field(default="")
    reason: str = Field(default="", max_length=1000)
    validation_report: str = Field(default="")
    evaluation_report: str = Field(default="")
    content_hash: str = Field(default="")
    history: list[dict[str, Any]] = Field(default_factory=list)


class USkillManifest(BaseModel):
    """uSkill Manifest V2 document (``uskill.yaml``)."""

    model_config = ConfigDict(extra="forbid")

    apiVersion: Literal["uskills/v2"] = Field(default=API_VERSION)
    kind: Literal["Skill"] = Field(default=KIND)
    metadata: ManifestMetadata
    compatibility: dict[str, Any] = Field(default_factory=dict)
    execution: ManifestExecution = Field(default_factory=ManifestExecution)
    inputs: dict[str, Any] = Field(default_factory=dict, description="JSON Schema for inputs")
    outputs: dict[str, Any] = Field(default_factory=dict, description="JSON Schema for outputs")
    tools: list[ManifestTool] = Field(default_factory=list, max_length=50)
    security: ManifestSecurity = Field(default_factory=ManifestSecurity)
    provenance: ManifestProvenance = Field(default_factory=ManifestProvenance)
    evaluation: ManifestEvaluation = Field(default_factory=ManifestEvaluation)
    governance: ManifestGovernance = Field(default_factory=ManifestGovernance)

    # apiVersion/kind are constrained by Literal (emits const in JSON Schema);
    # wrong values are rejected by Pydantic before any custom logic.


def load_manifest(path: str | Path) -> USkillManifest:
    """Load and validate a ``uskill.yaml`` manifest file."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Manifest file not found: {file_path}")
    data = yaml.safe_load(file_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Manifest root must be a mapping: {file_path}")
    return USkillManifest(**data)


def dump_manifest(manifest: USkillManifest, path: str | Path) -> Path:
    """Serialize a manifest to ``uskill.yaml`` inside ``path`` (dir or file)."""
    target = Path(path)
    if target.is_dir() or not target.suffix:
        target.mkdir(parents=True, exist_ok=True)
        target = target / "uskill.yaml"
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
    content = yaml.safe_dump(
        json.loads(manifest.model_dump_json(by_alias=True)),
        allow_unicode=True,
        sort_keys=False,
    )
    target.write_text(content, encoding="utf-8")
    return target


def validate_manifest_file(path: str | Path) -> tuple[bool, str]:
    """Validate a manifest file and return (is_valid, message)."""
    try:
        manifest = load_manifest(path)
        return True, f"valid manifest: {manifest.metadata.name}@{manifest.metadata.version}"
    except Exception as e:
        return False, f"error: {e}"


def manifest_from_legacy_skill(skill: Any, *, content_sha256: str = "") -> USkillManifest:
    """Derive a V2 manifest from a legacy USkill definition.

    Used by migration/import tooling so old YAML keeps its governance
    contract when exposed through the new two-layer layout.
    """
    from .schema import USkill  # local import to avoid cycles

    if not isinstance(skill, USkill):
        raise TypeError("manifest_from_legacy_skill expects a USkill instance")

    inputs_schema = {
        "type": "object",
        "properties": {
            p.name: {
                "type": p.type.value,
                **({"items": {"type": p.items_type.value}} if p.items_type else {}),
                **({"description": p.description} if p.description else {}),
            }
            for p in skill.input.params
        },
        "required": [p.name for p in skill.input.params if p.required],
    }
    outputs_schema = {
        "type": "object",
        "properties": {name: {} for name in skill.output.params},
    }
    mode = ExecutionMode.workflow if skill.meta.category.value == "composite" else ExecutionMode.llm
    name = skill.skill_id.split("-", 2)[-1].rsplit("-v", 1)[0]
    if not _NAME_OK.match(name):
        slug = re.sub(r"[^a-z0-9-]+", "-", skill.skill_id.lower()).strip("-")
        name = slug[:64] if _NAME_OK.match(slug[:64] or "") else "converted-skill"

    return USkillManifest(
        metadata=ManifestMetadata(
            name=name,
            description=skill.meta.description[:1024],
            version=skill.meta.version,
            tags=skill.meta.tags,
            owner=skill.meta.owner,
        ),
        execution=ManifestExecution(
            mode=mode,
            entry="SKILL.md",
            timeout=skill.control.timeout,
            retry=skill.control.retry,
            requires_approval=skill.execute.requires_approval,
        ),
        inputs=inputs_schema,
        outputs=outputs_schema,
        tools=[ManifestTool(id=t, permission=ToolPermission.read) for t in skill.execute.tools],
        security=ManifestSecurity(
            untrusted_source=False,
            allowed_permissions=[ToolPermission.read],
        ),
        provenance=ManifestProvenance(
            source="converted",
            imported_from=skill.source.sop_path if skill.source else "",
            content_sha256=content_sha256,
            notes=f"converted from legacy skill {skill.skill_id}",
        ),
    )


__all__ = [
    "API_VERSION",
    "KIND",
    "ExecutionMode",
    "ToolPermission",
    "USkillManifest",
    "load_manifest",
    "dump_manifest",
    "validate_manifest_file",
    "manifest_from_legacy_skill",
]
