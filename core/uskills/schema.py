"""uSkill Schema Definitions.

This module defines the core Pydantic models for uSkill, providing
type-safe validation and JSON Schema export capabilities.

Versioning policy
-----------------
* ``SCHEMA_VERSION`` tracks the skill-file format (1.1.0 since the V1.1
  release). New *optional* fields are backward compatible and do not bump
  it; breaking changes would.
* The Python package version lives in ``core/uskills/_version.py``.
"""

from __future__ import annotations

import re
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

# Schema version for compatibility tracking
SCHEMA_VERSION = "1.1.0"

# Default template version used when converting SOPs into new skills.
DEFAULT_TEMPLATE_VERSION = "1.1.0"

# Canonical JSON Schema dialect emitted by Pydantic V2 for this model.
# The exported document declares this dialect explicitly instead of a
# hand-written draft-07 marker that would not match the generated syntax.
JSON_SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"

# Skill ID pattern: uskill-{category}-{name}-{version}
SKILL_ID_PATTERN = re.compile(
    r"^uskill-(atomic|composite|domain|governance)-[\w\u4e00-\u9fff-]+-v\d+-\d+-\d+$"
)


class SkillCategory(StrEnum):
    """Skill category enumeration."""

    atomic = "atomic"
    composite = "composite"
    domain = "domain"
    governance = "governance"


class ParamType(StrEnum):
    """Allowed JSON types for skill parameters.

    Strict enumeration replaces the previous free-form string so typos
    such as ``strin`` are rejected at validation time.
    """

    string = "string"
    number = "number"
    integer = "integer"
    boolean = "boolean"
    object = "object"
    array = "array"


class SkillMeta(BaseModel):
    """Skill metadata configuration."""

    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=1, max_length=200, description="Skill display name")
    version: str = Field(
        default=DEFAULT_TEMPLATE_VERSION,
        pattern=r"^\d+\.\d+\.\d+$",
        description="Semantic version (e.g., 1.1.0)",
    )
    category: SkillCategory = Field(..., description="Skill category")
    domain: str = Field(default="general", min_length=1, max_length=100, description="Skill domain")
    description: str = Field(..., min_length=1, max_length=2000, description="Skill description")
    tags: list[str] = Field(
        default_factory=list, max_length=20, description="Skill tags for categorization"
    )
    owner: str = Field(default="community", min_length=1, max_length=100, description="Skill owner")

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: list[str]) -> list[str]:
        """Validate and clean tags."""
        return [tag.strip().lower() for tag in v if tag.strip()]


class SkillParam(BaseModel):
    """Skill input parameter definition.

    Constraints (``enum`` / ``minimum`` … / ``pattern`` / ``nullable``) mirror
    JSON Schema keywords and are enforced by the runtime before any model
    call; they also feed the parameter's JSON Schema fragment.
    """

    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=1, max_length=100, description="Parameter name")
    type: ParamType = Field(..., description="Parameter JSON type")
    required: bool = Field(default=True, description="Whether parameter is required")
    description: str = Field(default="", max_length=500, description="Parameter description")
    default: Any | None = Field(default=None, description="Default value if not required")
    items_type: ParamType | None = Field(
        default=None,
        description="Element type when type=array, used to build nested JSON Schema",
    )
    schema_: dict[str, Any] | None = Field(
        default=None,
        alias="schema",
        serialization_alias="schema",
        description="Optional full JSON Schema override for this parameter",
    )
    enum: list[Any] | None = Field(
        default=None, max_length=100, description="Allowed values (JSON Schema enum)"
    )
    minimum: int | float | None = Field(default=None, description="Inclusive lower bound (number/integer)")
    maximum: int | float | None = Field(default=None, description="Inclusive upper bound (number/integer)")
    min_length: int | None = Field(default=None, ge=0, description="Min length (string/array)")
    max_length: int | None = Field(default=None, ge=0, description="Max length (string/array)")
    pattern: str | None = Field(default=None, max_length=500, description="Regex constraint (string)")
    nullable: bool = Field(default=False, description="Whether an explicit null value is allowed")

    @field_validator("pattern")
    @classmethod
    def _compile_pattern(cls, v: str | None) -> str | None:
        if v is not None:
            try:
                re.compile(v)  # reject invalid regex at definition time
            except re.error as exc:
                raise ValueError(f"invalid regex in pattern constraint: {exc}") from exc
        return v

    def has_constraints(self) -> bool:
        """True when this param declares JSON-Schema constraint keywords."""
        return any(
            getattr(self, attr) is not None
            for attr in ("enum", "minimum", "maximum", "min_length", "max_length", "pattern")
        ) or self.schema_ is not None or (
            self.type is ParamType.array and self.items_type is not None
        )

    def json_schema_fragment(self) -> dict[str, Any]:
        """JSON Schema for this parameter (schema override wins)."""
        if self.schema_ is not None:
            return self.schema_
        frag: dict[str, Any] = {"type": self.type.value}
        if self.type is ParamType.array and self.items_type is not None:
            frag["items"] = {"type": self.items_type.value}
        if self.enum is not None:
            frag["enum"] = self.enum
        if self.minimum is not None:
            frag["minimum"] = self.minimum
        if self.maximum is not None:
            frag["maximum"] = self.maximum
        if self.type is ParamType.string:
            if self.min_length is not None:
                frag["minLength"] = self.min_length
            if self.max_length is not None:
                frag["maxLength"] = self.max_length
            if self.pattern is not None:
                frag["pattern"] = self.pattern
        elif self.type is ParamType.array:
            if self.min_length is not None:
                frag["minItems"] = self.min_length
            if self.max_length is not None:
                frag["maxItems"] = self.max_length
        if self.nullable:
            frag["type"] = [frag["type"], "null"]
        return frag


class SkillInputConfig(BaseModel):
    """Skill input configuration."""

    model_config = ConfigDict(extra="forbid")

    params: list[SkillParam] = Field(
        default_factory=list, max_length=50, description="Input parameters"
    )


class ExecuteConfig(BaseModel):
    """Execution configuration for skill."""

    model_config = ConfigDict(extra="forbid")

    prompt_template: str = Field(
        ..., min_length=1, max_length=10000, description="Prompt template with variables"
    )
    steps: list[str] = Field(default_factory=list, max_length=100, description="Execution steps")
    temperature: float = Field(default=0.1, ge=0.0, le=2.0, description="LLM temperature parameter")
    model: str = Field(
        default="gpt-4o-mini", min_length=1, max_length=100, description="LLM model name"
    )
    tools: list[str] = Field(default_factory=list, max_length=20, description="Required tools")
    fallback: list[str] = Field(
        default_factory=list, max_length=10, description="Fallback strategies"
    )
    requires_approval: bool = Field(
        default=False,
        description="If true, the runtime pauses the run for human approval "
        "before executing this skill",
    )
    depends_on: dict[str, list[str]] = Field(
        default_factory=dict,
        max_length=20,
        description="DAG edges for composite sub-skills: tool name -> names of "
        "sub-skills that must complete before it starts. Empty = declared order.",
    )

    @field_validator("prompt_template")
    @classmethod
    def validate_template_variables(cls, v: str) -> str:
        """Validate template variable syntax."""
        # Check for unclosed braces
        open_count = v.count("{")
        close_count = v.count("}")
        if open_count != close_count:
            raise ValueError(
                f"Template has mismatched braces: {open_count} open vs {close_count} close"
            )
        return v


class OutputConfig(BaseModel):
    """Output configuration for skill."""

    model_config = ConfigDict(extra="forbid")

    format: str = Field(
        default="json",
        pattern=r"^(json|yaml|text|markdown)$",
        description="Output format",
    )
    params: list[str] = Field(default_factory=list, max_length=50, description="Output parameters")
    validation_rules: list[str] = Field(
        default_factory=list, max_length=20, description="Output validation rules"
    )
    schema_: dict[str, Any] | None = Field(
        default=None,
        alias="schema",
        serialization_alias="schema",
        description="Optional full JSON Schema for the output document; when "
        "absent a permissive object schema is derived from params",
    )

    def json_schema(self) -> dict[str, Any] | None:
        """Validation schema for JSON output (None for free-form formats)."""
        if self.schema_ is not None:
            return self.schema_
        if self.format != "json":
            return None
        if not self.params:
            return None
        return {
            "type": "object",
            "properties": {name: {} for name in self.params},
            "required": list(self.params),
        }


class ControlConfig(BaseModel):
    """Execution control configuration."""

    model_config = ConfigDict(extra="forbid")

    timeout: int = Field(default=30, ge=1, le=3600, description="Execution timeout in seconds")
    retry: int = Field(default=1, ge=0, le=10, description="Retry count on failure")
    interrupt: bool = Field(default=True, description="Allow execution interruption")
    breakpoint_allowed: bool = Field(default=True, description="Allow breakpoints")
    mockable: bool = Field(default=True, description="Allow mock execution")
    repair: int = Field(
        default=2,
        ge=0,
        le=5,
        description="Bounded repair budget: re-asks the model with the validation "
        "error attached when JSON output fails the output schema (0 disables)",
    )
    backoff_base: float = Field(
        default=0.0,
        ge=0.0,
        le=60.0,
        description="Exponential backoff base in seconds for transient retries "
        "(delay = base * 2**attempt, capped at 30s; 0 = no wait)",
    )
    max_workers: int = Field(
        default=2, ge=1, le=8, description="Max parallel steps within one DAG level"
    )


class SourceTrace(BaseModel):
    """Source traceability information."""

    model_config = ConfigDict(extra="forbid")

    sop_name: str = Field(..., min_length=1, max_length=200, description="Source SOP name")
    sop_path: str = Field(default="", max_length=500, description="Source SOP file path")
    step_index: int = Field(..., ge=0, description="Step index in source SOP")
    raw_step: str = Field(..., min_length=1, max_length=2000, description="Raw step content")
    context: str = Field(
        default="",
        max_length=8000,
        description="Surrounding SOP context (headings, constraints, conditions) "
        "preserved from the source document so nothing is silently lost",
    )


class USkill(BaseModel):
    """Main uSkill model definition."""

    model_config = ConfigDict(extra="forbid")

    skill_id: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Unique skill identifier",
    )
    meta: SkillMeta = Field(..., description="Skill metadata")
    input: SkillInputConfig = Field(..., description="Input configuration")
    execute: ExecuteConfig = Field(..., description="Execution configuration")
    output: OutputConfig = Field(..., description="Output configuration")
    control: ControlConfig = Field(..., description="Control configuration")
    source: SourceTrace | None = Field(
        default=None,
        description="Source traceability. Optional so standalone, hand-authored "
        "skills do not need to fake an SOP origin.",
    )

    @field_validator("skill_id")
    @classmethod
    def validate_skill_id(cls, v: str) -> str:
        """Validate skill ID format."""
        if not SKILL_ID_PATTERN.match(v):
            raise ValueError(
                f"Invalid skill_id format. Expected: uskill-{{category}}-{{name}}-v{{version}}, "
                f"got: {v}"
            )
        return v


def exported_json_schema() -> dict[str, Any]:
    """Export USkill JSON Schema.

    The document declares the same JSON Schema dialect that Pydantic V2
    actually emits (2020-12), keeping the ``$schema`` marker honest.

    Returns:
        JSON Schema dictionary for USkill model.
    """
    schema = USkill.model_json_schema(ref_template="#/$defs/{model}")
    schema["$schema"] = JSON_SCHEMA_DIALECT
    schema["$id"] = f"https://zhubao315.github.io/uSkill/schema/v{SCHEMA_VERSION}.json"
    return schema


def get_schema_version() -> str:
    """Get current schema version."""
    return SCHEMA_VERSION
