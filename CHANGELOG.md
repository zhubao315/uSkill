# Changelog

All notable changes to uSkill are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).
The package version is defined in `core/uskills/_version.py`.

## [1.2.0] - 2026-11-13

### Added
- **Governed Runtime 2.0** (`core/uskills/runtime/`): Provider abstraction
  (Mock / OpenAI Chat Completions / OpenAI Responses API), real enforcement
  of `control.timeout` and `control.retry`, composite skills that truly
  schedule sub-skills, JSON output validation, permission-gated tool
  registry, human approval gates with resume/reject, run records checkpointed
  to disk with per-step status/timings/usage and event trails.
- **Agent Skills open-standard compatibility** (`agentskills.py`): validate,
  inspect, import and export standard `skill-name/SKILL.md` packages
  (name/description limits, directory match, progressive-disclosure checks,
  reference existence) without touching official frontmatter.
- **uSkill Manifest V2** (`manifest.py`, `uskill.yaml`): typed I/O JSON
  Schema, execution modes (instruction/llm/tool/script/workflow), tool
  permissions, security and provenance with content hashes; converter from
  legacy skills.
- **Evaluation harness** (`evaluation.py`, `uskills eval`): versioned suites,
  deterministic graders, No-Skill baseline vs Skill-assisted comparison,
  markdown/JSON reports.
- **Governance** (`governance/`): least-privilege permission policy,
  append-only audit log, Draft→Published lifecycle gates.
- CLI: `init`, `run`, `eval`, `inspect`, `import-skill`, `export-skill`,
  `doctor`; `uskill` alias for the `uskills` command.
- Four project development skills under `.agents/skills/` and `AGENTS.md`.
- Two-layer demo skill `skills/agent-skills/code-review/`.
- `LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`.

### Changed
- Template-variable validation is now part of `validate_skill_file` /
  `validate_skill_data` (semantic errors fail validation; ambiguous cases
  report warnings).
- SOP conversion preserves non-step content (headings, constraints, nested
  details, tables) in `source.context` and the prompt template; new
  `parse_sop()` structured parser.
- `SkillParam.type` is a strict enum; optional `schema`/`items_type` for
  nested JSON Schema in adapters.
- `source` (SOP traceability) is now optional for standalone skills.
- JSON Schema export declares the 2020-12 dialect Pydantic actually emits.
- Package version single-sourced from `_version.py`; `requires-python`
  raised to >=3.11 (3.10 reached EOL); openai moved to optional `[llm]` extra.
- CI: Python matrix (3.11–3.13), lint/type/test/coverage/schema/skills
  validation, package build + install test.
- Documentation and links unified on the `uSkill` name.

### Deprecated / notes
- `SkillExecutor` is now a compatibility facade over `SkillRuntime`;
  prefer `SkillRuntime` directly. Existing API and result envelope preserved.

## [1.1.0] - historical
- First tagged line with AIConverter prototype, single-shot executor,
  Pydantic V2 schema export, MkDocs site (see git history).

## [0.1.0-preview.1] / [0.0.1]
- Initial prototypes.
