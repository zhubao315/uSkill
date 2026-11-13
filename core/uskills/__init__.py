"""uSkill core package.

This package provides the core functionality for uSkill including:

- Schema definitions and validation (``schema`` / ``validator``)
- SOP to Skill conversion, including AI-powered (``converter`` / ``ai_converter``)
- Governed execution runtime (``runtime`` / ``executor``)
- Skill indexing and cataloging (``indexer``)
- Agent Skills open-standard compatibility (``agentskills``)
- uSkill Manifest V2 and governance (``manifest`` / ``governance``)
- Skill evaluation harness (``evaluation``)
"""

from ._version import __version__
from .agentskills import (
    AgentSkillPackage,
    export_agent_skill,
    import_agent_skill,
    inspect_agent_skill,
    validate_agent_skill,
)
from .ai_converter import AIConverter, ConversionReport
from .converter import (
    ConversionError,
    convert_sop_file,
    convert_sop_text,
    convert_sop_to_dict,
    extract_steps,
    parse_sop,
)
from .errors import (
    ApprovalRequiredError,
    ConversionFailedError,
    ExecutionFailedError,
    PermissionDeniedError,
    ProviderError,
    USkillError,
    USkillValidationError,
)
from .evaluation import EvalCase, EvalResult, EvalSuite, run_eval_suite
from .executor import SkillExecutor
from .governance import Permission, PermissionPolicy
from .indexer import build_skills_index, get_skill_stats
from .manifest import USkillManifest, validate_manifest_file
from .runtime import SkillRuntime
from .schema import (
    SCHEMA_VERSION,
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
    exported_json_schema,
    get_schema_version,
)
from .validator import (
    ValidationError,
    extract_template_variables,
    load_skill,
    validate_directory,
    validate_skill_data,
    validate_skill_file,
    validate_skill_id,
    validate_template_variables,
)

__all__ = [
    "__version__",
    # Schema
    "SCHEMA_VERSION",
    "ControlConfig",
    "ExecuteConfig",
    "OutputConfig",
    "ParamType",
    "SkillCategory",
    "SkillInputConfig",
    "SkillMeta",
    "SkillParam",
    "SourceTrace",
    "USkill",
    "exported_json_schema",
    "get_schema_version",
    # Converter
    "ConversionError",
    "convert_sop_file",
    "convert_sop_text",
    "convert_sop_to_dict",
    "extract_steps",
    "parse_sop",
    # AI
    "AIConverter",
    "ConversionReport",
    # Executor / Runtime
    "SkillExecutor",
    "SkillRuntime",
    # Indexer
    "build_skills_index",
    "get_skill_stats",
    # Agent Skills
    "AgentSkillPackage",
    "validate_agent_skill",
    "import_agent_skill",
    "export_agent_skill",
    "inspect_agent_skill",
    # Manifest / governance
    "USkillManifest",
    "validate_manifest_file",
    "Permission",
    "PermissionPolicy",
    # Evaluation
    "EvalCase",
    "EvalResult",
    "EvalSuite",
    "run_eval_suite",
    # Validator
    "ValidationError",
    "extract_template_variables",
    "load_skill",
    "validate_directory",
    "validate_skill_data",
    "validate_skill_file",
    "validate_skill_id",
    "validate_template_variables",
    # Errors
    "USkillError",
    "USkillValidationError",
    "ConversionFailedError",
    "ExecutionFailedError",
    "ProviderError",
    "PermissionDeniedError",
    "ApprovalRequiredError",
]
