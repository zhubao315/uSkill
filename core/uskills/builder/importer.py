"""Unified importer for skill sources.

Accepts: Markdown / plain text / SOP documents, raw prompt text,
legacy skill YAML/JSON, standard SKILL.md and Agent Skill directories.
Everything is returned as an untrusted :class:`SourceDoc`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..agentskills import inspect_agent_skill
from ..standards_compat import detect_format

DEFAULT_ENCODING = "utf-8"

TEXT_SUFFIXES = {".md", ".markdown", ".txt"}


@dataclass
class SourceDoc:
    """Normalized, untrusted source document."""

    text: str
    origin: str
    kind: str  # "markdown" | "text" | "prompt" | "skill-v1" | "agent-skill"
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def name(self) -> str:
        p = Path(self.origin)
        return p.stem if self.origin else "source"


def import_source(path_or_text: str | Path, *, kind_hint: str | None = None) -> SourceDoc:
    """Import one source from a path or raw text.

    Raises FileNotFoundError for path-like inputs that do not exist;
    free-form text (multi-line or without a file extension) is imported
    as an inline prompt.
    """
    candidate = Path(str(path_or_text))
    if not candidate.exists():
        looks_like_path = "\n" not in str(path_or_text) and (
            candidate.suffix.lower() in TEXT_SUFFIXES | {".yaml", ".yml", ".json"}
            or "/" in str(path_or_text)
        )
        if looks_like_path:
            raise FileNotFoundError(f"Source not found: {candidate}")
    if candidate.exists():
        fmt = detect_format(candidate)
        if fmt == "agent-skill" or (kind_hint == "agent-skill"):
            pkg = inspect_agent_skill(candidate)
            meta = {"frontmatter": pkg.frontmatter, "files": pkg.files}
            return SourceDoc(pkg.body, str(candidate), "agent-skill", meta)
        if fmt == "skill-v1":
            text = candidate.read_text(encoding=DEFAULT_ENCODING)
            return SourceDoc(text, str(candidate), "skill-v1")
        if candidate.suffix.lower() in TEXT_SUFFIXES or candidate.suffix == "":
            text = candidate.read_text(encoding=DEFAULT_ENCODING)
            kind = "markdown" if candidate.suffix.lower() in {".md", ".markdown"} else "text"
            return SourceDoc(text, str(candidate), kind)
        text = candidate.read_text(encoding=DEFAULT_ENCODING)
        return SourceDoc(text, str(candidate), "text")

    if kind_hint:
        return SourceDoc(str(path_or_text), "<inline>", kind_hint)
    return SourceDoc(str(path_or_text), "<inline>", "prompt")
