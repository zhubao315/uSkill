"""uSkill Validator Module.

This module provides functionality to validate uSkill YAML/JSON files
against the standard schema, check template variable consistency, and run
semantic checks as one complete pipeline.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, cast

import yaml  # type: ignore

from .errors import USkillValidationError
from .schema import USkill


class ValidationError(USkillValidationError):
    """Custom error for uSkill validation failures."""

    def __init__(self, message: str, file_path: str | None = None):
        super().__init__(message)
        self.file_path = file_path


def load_skill(path: str | Path) -> USkill:
    """Load and validate a uSkill from a YAML or JSON file.

    Args:
        path: Path to the skill file.

    Returns:
        Validated USkill instance.

    Raises:
        FileNotFoundError: If file does not exist.
        ValidationError: If file content is invalid.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Skill file not found: {file_path}")

    try:
        content = file_path.read_text(encoding="utf-8")
        if file_path.suffix.lower() in (".yaml", ".yml"):
            data = yaml.safe_load(content)
        else:
            data = json.loads(content)

        return USkill(**cast(dict[str, Any], data))
    except Exception as e:
        raise ValidationError(str(e), file_path=str(file_path)) from e


def validate_skill_semantics(skill: USkill) -> tuple[list[str], list[str]]:
    """Run semantic checks on a structurally valid skill.

    Structural validation (Pydantic) cannot see cross-field problems.
    This function returns ``(errors, warnings)``:

    * errors (fail validation): undefined ``{{variables}}`` in the prompt
      template; composite skills that declare no tools to orchestrate.
    * warnings (non-blocking): optional params without a default, which is
      legal but ambiguous for executors.
    """
    errors: list[str] = []
    warnings: list[str] = []

    param_names = [p.name for p in skill.input.params]
    ok, undefined = validate_template_variables(skill.execute.prompt_template, param_names)
    if not ok:
        errors.append(
            f"prompt_template uses undefined input params: {sorted(undefined)} "
            f"(declared params: {param_names})"
        )

    optional_no_default = [
        p.name for p in skill.input.params if not p.required and p.default is None
    ]
    if optional_no_default:
        warnings.append(f"optional params without default value: {sorted(optional_no_default)}")

    if skill.meta.category.value == "composite" and not skill.execute.tools:
        errors.append("composite skill declares no tools to orchestrate")

    return errors, warnings


def validate_skill_file(path: str | Path, check_semantics: bool = True) -> tuple[bool, str]:
    """Validate a skill file: structure first, then semantics.

    Args:
        path: Path to the skill file.
        check_semantics: Whether to run cross-field semantic checks
            (template variables, composite tool declarations, ...).

    Returns:
        Tuple of (is_valid, message).
    """
    try:
        skill = load_skill(path)
    except Exception as e:
        return False, f"error: {e}"

    if check_semantics:
        errors, warnings = validate_skill_semantics(skill)
        if errors:
            return False, f"semantic errors: {'; '.join(errors)}"
        suffix = f" (warnings: {'; '.join(warnings)})" if warnings else ""
        return True, f"valid: {skill.skill_id}{suffix}"

    return True, f"valid: {skill.skill_id}"


def validate_skill_data(data: dict[str, Any], check_semantics: bool = True) -> tuple[bool, str]:
    """Validate raw skill dictionary.

    Args:
        data: Skill data dictionary.
        check_semantics: Whether to run semantic checks as well.

    Returns:
        Tuple of (is_valid, message).
    """
    try:
        skill = USkill(**data)
    except Exception as e:
        return False, f"error: {e}"

    if check_semantics:
        errors, warnings = validate_skill_semantics(skill)
        if errors:
            return False, f"semantic errors: {'; '.join(errors)}"
        suffix = f" (warnings: {'; '.join(warnings)})" if warnings else ""
        return True, f"valid: {skill.skill_id}{suffix}"

    return True, f"valid: {skill.skill_id}"


def validate_skill_id(skill_id: str) -> tuple[bool, str]:
    """Validate skill ID format.

    Args:
        skill_id: The skill ID string to validate.

    Returns:
        Tuple of (is_valid, message).
    """
    try:
        # We reuse the model validator to keep CLI and Core consistent.
        USkill.validate_skill_id(skill_id)
        return True, "valid"
    except ValueError as e:
        return False, str(e)


def extract_template_variables(template: str) -> list[str]:
    """Extract variable names from prompt template.

    Looks for {{variable_name}} patterns.

    Args:
        template: Prompt template string.

    Returns:
        List of unique variable names.
    """
    pattern = re.compile(r"\{\{([\w-]+)\}\}")
    return sorted(list(set(pattern.findall(template))))


def validate_template_variables(template: str, params: list[str]) -> tuple[bool, list[str]]:
    """Check if all template variables are defined in input params.

    Args:
        template: Prompt template string.
        params: List of defined parameter names.

    Returns:
        Tuple of (is_all_defined, list_of_undefined_variables).
    """
    variables = extract_template_variables(template)
    undefined = [v for v in variables if v not in params]
    return len(undefined) == 0, undefined


def _skip_as_skill(path: Path) -> bool:
    """True for JSON/YAML that is not a skill: manifests live in the
    ``uskill.*`` branch; eval datasets live under ``evals/``."""
    return "evals" in path.parts


def validate_directory(
    path: str | Path, recursive: bool = True, check_semantics: bool = True
) -> dict[str, tuple[bool, str]]:
    """Validate all skill files in a directory.

    Files named ``uskill.yaml`` / ``uskill.yml`` are treated as uSkill
    Manifest V2 documents and validated by the manifest module instead of
    the legacy skill schema. Data under ``evals/`` is skipped.

    Args:
        path: Path to directory.
        recursive: Whether to search subdirectories.
        check_semantics: Whether to run semantic checks on each skill.

    Returns:
        Dictionary mapping file paths to (is_valid, message) tuples.
    """
    from .manifest import validate_manifest_file

    root = Path(path)
    results: dict[str, tuple[bool, str]] = {}

    patterns = ["*.yaml", "*.yml", "*.json"]
    files: list[Path] = []
    for pattern in patterns:
        if recursive:
            files.extend(root.rglob(pattern))
        else:
            files.extend(root.glob(pattern))

    for file_path in sorted(set(files)):
        if _skip_as_skill(file_path):
            continue
        if file_path.stem == "uskill":
            results[str(file_path)] = validate_manifest_file(file_path)
        else:
            results[str(file_path)] = validate_skill_file(
                file_path, check_semantics=check_semantics
            )

    return results
