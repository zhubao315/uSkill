"""uSkill Converter Module.

This module provides functionality to convert SOP text files
into standardized uSkill definitions with proper naming conventions
and error handling.

The parser keeps *all* source content traceable: numbered/bulleted items
become steps, while headings, prose constraints, nested details and tables
are preserved in the skill's ``source.context`` and folded into the prompt
template instead of being silently dropped.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import yaml  # type: ignore

from .errors import ConversionFailedError
from .schema import (
    DEFAULT_TEMPLATE_VERSION,
    ControlConfig,
    ExecuteConfig,
    OutputConfig,
    ParamType,
    SkillCategory,
    SkillInputConfig,
    SkillMeta,
    SkillParam,
    SourceTrace,
    USkill,
)

# Step prefix patterns for SOP parsing
STEP_PREFIX = re.compile(r"^\s*(?:\d+[.)]|[-*+])\s+")

# List item with capture groups: indent, marker, text
_LIST_ITEM = re.compile(r"^(\s*)(?:\d+[.)]|[-*+])\s+(.*)$")

# Markdown heading
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")

# Table separator row like |---|:--:|
_TABLE_SEP = re.compile(r"^\|?\s*:?-{2,}.*$")

# Maximum skill ID component length
MAX_SKILL_ID_COMPONENT_LENGTH = 32

# File encoding constant
DEFAULT_ENCODING = "utf-8"

BlockKind = Literal["heading", "paragraph", "list_item", "table_row"]


class ConversionError(ConversionFailedError):
    """Custom error for SOP conversion failures."""

    def __init__(self, message: str, source_path: str | None = None):
        super().__init__(message)
        self.source_path = source_path


@dataclass
class SopBlock:
    """A structured block of a parsed SOP document."""

    kind: BlockKind
    text: str
    depth: int = 0
    heading_level: int = 0


@dataclass
class SopDocument:
    """Structured representation of a parsed SOP."""

    blocks: list[SopBlock] = field(default_factory=list)

    @property
    def steps(self) -> list[SopBlock]:
        """Top-level list items are candidate steps."""
        return [b for b in self.blocks if b.kind == "list_item" and b.depth == 0]

    @property
    def paragraphs(self) -> list[SopBlock]:
        return [b for b in self.blocks if b.kind == "paragraph"]


def _slugify(value: str, max_length: int = MAX_SKILL_ID_COMPONENT_LENGTH) -> str:
    """Convert string to URL-safe slug.

    Args:
        value: Input string to slugify.
        max_length: Maximum length of output slug.

    Returns:
        URL-safe slug string.
    """
    lowered = value.strip().lower()
    # Keep alphanumeric, Chinese characters, and hyphens
    lowered = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", lowered)
    slug = lowered.strip("-") or "step"
    return slug[:max_length]


def extract_steps(text: str) -> list[str]:
    """Extract steps from SOP text.

    Parses numbered lists, bullet points, or paragraphs as steps.

    Note:
        Legacy API kept for backward compatibility. It only returns list
        items and therefore loses non-list content. Prefer :func:`parse_sop`
        which preserves the whole document structure.

    Args:
        text: SOP text content.

    Returns:
        List of extracted step strings.
    """
    if not text or not text.strip():
        return []

    steps: list[str] = []
    for line in text.splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        if STEP_PREFIX.match(cleaned):
            step_text = STEP_PREFIX.sub("", cleaned).strip()
            if step_text:
                steps.append(step_text)

    if steps:
        return steps

    # Fallback: split by double newlines (paragraphs)
    paragraphs = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    return paragraphs


def parse_sop(text: str) -> SopDocument:
    """Parse SOP text into structured blocks without losing content.

    Recognized structures: markdown headings, paragraphs, (nested)
    numbered/bulleted list items, and markdown table rows.

    Args:
        text: SOP text content.

    Returns:
        A SopDocument containing every block of the original text.
    """
    doc = SopDocument()
    if not text or not text.strip():
        return doc

    paragraph_buf: list[str] = []

    def flush_paragraph() -> None:
        if paragraph_buf:
            doc.blocks.append(SopBlock(kind="paragraph", text=" ".join(paragraph_buf).strip()))
            paragraph_buf.clear()

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            continue

        heading = _HEADING.match(stripped)
        if heading:
            flush_paragraph()
            doc.blocks.append(
                SopBlock(
                    kind="heading",
                    text=heading.group(2).strip(),
                    heading_level=len(heading.group(1)),
                )
            )
            continue

        item = _LIST_ITEM.match(line)
        if item:
            flush_paragraph()
            depth = len(item.group(1)) // 2
            doc.blocks.append(SopBlock(kind="list_item", text=item.group(2).strip(), depth=depth))
            continue

        if stripped.startswith("|") and not _TABLE_SEP.match(stripped):
            flush_paragraph()
            doc.blocks.append(SopBlock(kind="table_row", text=stripped))
            continue

        paragraph_buf.append(stripped)

    flush_paragraph()
    return doc


def _build_step_details(doc: SopDocument, step_pos: int) -> str:
    """Collect nested details that belong to the step at ``step_pos``."""
    details: list[str] = []
    for block in doc.blocks[step_pos + 1 :]:
        if block.kind == "list_item" and block.depth > 0:
            details.append(f"- {block.text}")
        else:
            break
    return "\n".join(details)


def _build_sop_context(doc: SopDocument) -> str:
    """Collect everything that is not a top-level step (headings, prose,
    tables, nested details) so constraints survive the conversion."""
    parts: list[str] = []
    for _i, block in enumerate(doc.blocks):
        if block.kind == "heading":
            parts.append(f"[heading] {block.text}")
        elif block.kind == "paragraph":
            parts.append(f"[constraint] {block.text}")
        elif block.kind == "table_row":
            parts.append(block.text)
        elif block.kind == "list_item" and block.depth > 0:
            parts.append(f"[sub-step] {'  ' * block.depth}- {block.text}")
    return "\n".join(parts)


def _generate_skill_id(
    sop_slug: str, index: int, step_slug: str, version: str = DEFAULT_TEMPLATE_VERSION
) -> str:
    """Generate a standardized skill ID.

    Format: uskill-atomic-{sop_slug}-{index:02d}-{step_slug}-v{version}
    """
    version_tag = version.replace(".", "-")
    return f"uskill-atomic-{sop_slug}-{index:02d}-{step_slug}-v{version_tag}"


def _build_prompt_template(sop_name: str, step: str, details: str = "", context: str = "") -> str:
    """Build prompt template for a skill, preserving source context."""
    parts = [
        "You are executing an atomic SOP skill.",
        f"SOP: {sop_name}",
        f"Step objective: {step}",
    ]
    if details:
        parts.extend(["", "Step details (from source SOP):", details])
    if context:
        parts.extend(["", "Source SOP context and constraints (must be respected):", context])
    parts.append("Use {{context}} when provided and produce a structured result.")
    template = "\n".join(parts)
    if len(template) > 9900:  # keep well below the schema's 10000 limit
        template = template[:9900] + "\n…[truncated]"
    return template


def convert_sop_text(
    text: str,
    sop_name: str,
    sop_path: str = "",
    domain: str = "general",
    owner: str = "uSkills",
    version: str = DEFAULT_TEMPLATE_VERSION,
) -> list[USkill]:
    """Convert SOP text to a list of uSkill definitions.

    Args:
        text: SOP text content.
        sop_name: Name of the SOP.
        sop_path: Path to the source SOP file.
        domain: Skill domain category.
        owner: Skill owner name.
        version: Version for generated skill IDs/metadata.

    Returns:
        List of USkill instances.

    Raises:
        ConversionError: If no steps can be extracted.
    """
    doc = parse_sop(text)
    step_blocks = doc.steps

    if step_blocks:
        global_context = _build_sop_context(doc)
        steps_with_meta = [
            (block.text, _build_step_details(doc, pos))
            for pos, block in enumerate(doc.blocks)
            if block.kind == "list_item" and block.depth == 0
        ]
    else:
        # Legacy fallback: treat paragraphs as steps, no residual context.
        steps = extract_steps(text)
        global_context = ""
        steps_with_meta = [(s, "") for s in steps]

    if not steps_with_meta:
        raise ConversionError(
            f"No steps could be extracted from SOP: {sop_name}",
            source_path=sop_path,
        )

    skills: list[USkill] = []
    sop_slug = _slugify(sop_name)
    context_trace = global_context[:8000]

    for index, (step, details) in enumerate(steps_with_meta, start=1):
        step_slug = _slugify(step, max_length=24)
        skill_id = _generate_skill_id(sop_slug, index, step_slug, version)

        step_context = "\n".join(x for x in (context_trace, details) if x)[:8000]

        skill = USkill(
            skill_id=skill_id,
            meta=SkillMeta(
                name=f"{sop_name} Step {index}",
                version=version,
                category=SkillCategory.atomic,
                domain=domain,
                description=step,
                tags=["converted", "sop", "atomic", sop_slug],
                owner=owner,
            ),
            input=SkillInputConfig(
                params=[
                    SkillParam(
                        name="context",
                        type=ParamType.string,
                        required=False,
                        default=None,
                        description="Execution context shared across the SOP chain.",
                    )
                ]
            ),
            execute=ExecuteConfig(
                prompt_template=_build_prompt_template(sop_name, step, details, global_context),
                steps=[step],
                temperature=0.1,
                tools=[],
                fallback=["manual-review"],
            ),
            output=OutputConfig(
                format="json",
                params=["status", "result", "notes"],
                validation_rules=[
                    "status must be one of success, partial, failed",
                    "result must summarize the step execution",
                ],
            ),
            control=ControlConfig(
                timeout=30,
                retry=1,
                interrupt=True,
                breakpoint_allowed=True,
                mockable=True,
            ),
            source=SourceTrace(
                sop_name=sop_name,
                sop_path=sop_path,
                step_index=index,
                raw_step=step,
                context=step_context,
            ),
        )
        skills.append(skill)

    return skills


def convert_sop_file(
    path: str | Path,
    output_dir: str | Path | None = None,
    domain: str = "general",
    owner: str = "uSkills",
    version: str = DEFAULT_TEMPLATE_VERSION,
) -> list[Path]:
    """Convert a SOP file to uSkill YAML files.

    Args:
        path: Path to source SOP file.
        output_dir: Output directory for generated skills.
        domain: Skill domain category.
        owner: Skill owner name.
        version: Version for generated skill IDs/metadata.

    Returns:
        List of paths to generated skill files.

    Raises:
        FileNotFoundError: If source file does not exist.
        ConversionError: If conversion fails.
    """
    source_path = Path(path)

    try:
        text = source_path.read_text(encoding=DEFAULT_ENCODING)
    except FileNotFoundError as err:
        raise FileNotFoundError(f"SOP file not found: {source_path}") from err
    except UnicodeDecodeError as err:
        raise ConversionError(
            f"Failed to read file with {DEFAULT_ENCODING} encoding: {err}",
            source_path=str(source_path),
        ) from err

    if not text.strip():
        raise ConversionError(
            f"SOP file is empty: {source_path}",
            source_path=str(source_path),
        )

    skills = convert_sop_text(
        text,
        source_path.stem,
        str(source_path),
        domain=domain,
        owner=owner,
        version=version,
    )

    output_root = Path(output_dir) if output_dir else source_path.parent / "generated"
    output_root.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for skill in skills:
        target = output_root / f"{skill.skill_id}.yaml"
        content = yaml.safe_dump(
            json.loads(skill.model_dump_json(by_alias=True)),
            allow_unicode=True,
            sort_keys=False,
        )
        target.write_text(content, encoding=DEFAULT_ENCODING)
        written.append(target)

    return written


def convert_sop_to_dict(
    text: str,
    sop_name: str,
    sop_path: str = "",
    domain: str = "general",
    owner: str = "uSkills",
    version: str = DEFAULT_TEMPLATE_VERSION,
) -> list[dict[str, Any]]:
    """Convert SOP text to list of skill dictionaries."""
    skills = convert_sop_text(text, sop_name, sop_path, domain, owner, version)
    return [json.loads(skill.model_dump_json()) for skill in skills]
