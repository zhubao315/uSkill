# Changelog

All notable changes to uSkill are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).
The package version is defined in `core/uskills/_version.py`.

## [Unreleased] — 2.0 演进（Sprint 0–2）

### Added
- **Sprint 0 audits** (`docs/audit/`, `docs/ROADMAP_2.0.md`): evidence-linked
  project/architecture/security/test-coverage/ecosystem gap analysis; no code
  changes.
- **Standards compatibility** (`standards_compat.py`): `detect_format()`
  (skill-v1 / manifest-v2 / agent-skill), `MigrationReport` (lossy fields are
  never silently dropped), idempotent `migrate_skill` / `migrate_directory`
  with dry-run; deprecated-field warnings. `uskills migrate` command;
  `uskills schema --target skill|manifest|both`; `standards/manifest/v1,v2`
  and `standards/compatibility` documentation.
- **Skill Builder** (`core/uskills/builder/`, `uskills build`): unified
  importer (Markdown/text/prompt/legacy YAML/SKILL.md dir), deterministic
  task IR with step-kind classification (atomic/decision/approval/loop,
  evidence-bearing), evidence-backed quality score (0–100, review_required
  below 70, secret literals zero out safety), Draft-only output pipeline
  (`drafts/`, `evals-draft/` suites, `build-report.json`) with
  `requires_approval` propagation — generated skills can never auto-publish.

### Changed
- Manifest `apiVersion`/`kind` are `Literal`-constrained (JSON Schema
  `const`); canonical version string unified to `uskills/v2`.
- `import_source` raises `FileNotFoundError` for missing path-like inputs
  while still accepting free-form inline prompt text.

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
