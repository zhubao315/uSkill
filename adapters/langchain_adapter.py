"""Framework adapters for uSkill.

Adapters convert uSkill definitions into framework tool specifications
(LangChain tool spec, OpenAI function spec). They intentionally do NOT
implement execution: every adapter routes real runs through the core
runtime so execution semantics cannot diverge per framework.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from core.uskills.schema import USkill
from core.uskills.validator import load_skill


class LangChainAdapter:
    """Adapter for converting uSkill to LangChain / OpenAI specifications."""

    def __init__(self, skill_path: str | Path | USkill):
        """Initialize with a skill file path or an in-memory USkill."""
        self.skill: USkill = (
            skill_path if isinstance(skill_path, USkill) else load_skill(skill_path)
        )

    def to_tool_spec(self) -> dict[str, Any]:
        """Convert uSkill to LangChain tool specification."""
        return {
            "name": self._sanitize_name(self.skill.meta.name),
            "description": self.skill.meta.description,
            "args_schema": self._build_args_schema(),
            "metadata": {
                "skill_id": self.skill.skill_id,
                "category": self.skill.meta.category.value,
                "domain": self.skill.meta.domain,
                "version": self.skill.meta.version,
                "tags": self.skill.meta.tags,
            },
        }

    def to_prompt_template(self) -> str:
        """Get the prompt template for this skill."""
        return self.skill.execute.prompt_template

    def to_function_spec(self) -> dict[str, Any]:
        """Convert uSkill to OpenAI function calling specification."""
        return {
            "name": self._sanitize_name(self.skill.meta.name),
            "description": self.skill.meta.description,
            "parameters": {
                "type": "object",
                "properties": self._build_properties(),
                "required": self._get_required_params(),
            },
        }

    def run(self, inputs: dict[str, Any], runtime: Any) -> Any:
        """Execute the skill through the shared core runtime.

        Adapters never re-implement execution; they delegate to
        ``core.uskills.runtime.SkillRuntime`` and return its RunRecord.
        """
        return runtime.run(self.skill, inputs)

    def _build_args_schema(self) -> dict[str, Any]:
        """Build arguments schema (proper JSON Schema draft)."""
        return {
            "type": "object",
            "properties": self._build_properties(),
            "required": self._get_required_params(),
        }

    def _build_properties(self) -> dict[str, Any]:
        """Build JSON Schema properties, including nested array/object types."""
        properties: dict[str, Any] = {}
        for param in self.skill.input.params:
            if param.schema_ is not None:
                prop = dict(param.schema_)
            else:
                prop = {"type": param.type.value}
                if param.type.value == "array" and param.items_type is not None:
                    prop["items"] = {"type": param.items_type.value}
                elif param.type.value == "array":
                    prop["items"] = {}
                elif param.type.value == "object":
                    prop["additionalProperties"] = True
            if param.description:
                prop["description"] = param.description
            if param.default is not None:
                prop["default"] = param.default
            properties[param.name] = prop
        return properties

    def _get_required_params(self) -> list[str]:
        """Get list of required parameter names."""
        return [p.name for p in self.skill.input.params if p.required]

    @staticmethod
    def _sanitize_name(name: str) -> str:
        """Sanitize skill name for use as function name."""
        import re

        sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", name)
        sanitized = re.sub(r"_+", "_", sanitized)
        sanitized = sanitized.strip("_").lower()
        return sanitized or "skill"


def as_langchain_spec(path: str | Path | USkill) -> dict[str, Any]:
    """Convert a uSkill file (or USkill) to LangChain tool specification."""
    return LangChainAdapter(path).to_tool_spec()


def as_openai_function(path: str | Path | USkill) -> dict[str, Any]:
    """Convert a uSkill file (or USkill) to OpenAI function specification."""
    return LangChainAdapter(path).to_function_spec()
