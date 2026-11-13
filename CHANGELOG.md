# Changelog

All notable changes to uSkill are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).
The package version is defined in `core/uskills/_version.py`.

## [2.0.0] - 2026-11-13

> Agent Skill Engineering Platform — 六个 Sprint（审计 → 标准 → Builder →
> Runtime → Evaluation → 治理分发 → 发布工程）全部完成。向后兼容是契约：
> 全部 1.x 技能文件无需修改即可加载/校验/执行。`git tag` 与推送由维护者
> 手动触发（本仓库不自动发布）。

### Added
- **Sprint 6 release engineering**: `uskills list` (registry listing with
  health exit codes), `uskills test` (suite-as-tests), `uskills audit`
  (redacted JSONL viewer), `run --audit <path>` (audit trail from the
  CLI), `eval/test --mock-response` (deterministic offline regression
  runs); CI adds `ruff format --check`, `--cov-fail-under=80` (measured
  91%; CLI module 84% vs 70% gate) and an eval regression gate against
  committed mock baselines (`evals/reports/`); migration guide
  (`docs/migration.md`) and a re-grouped docs nav (入门/概念/指南/参考);
  full CLI reference (`docs/cli.md`); Python 3.11–3.13 test matrix
  (3.10 EOL).
- **Sprint 5 governance & distribution**: capability-derived risk levels
  L0–L4 (`governance/risk.py`, `uskills risk`; unregistered tool
  declarations do NOT elevate — the runtime cannot invoke them); static
  script scan on import (`builder/scan.py`: process exec, dynamic code,
  file write/delete, network, env-secrets → import report notes +
  `manifest.security.risk_level` + `untrusted_source=true`; scripts are
  never executed); audit-log redaction (sensitive-key masking, bulk
  values stored as sha256 digests); `SkillRegistry` with five search
  modes + `health()` and `uskills search`; `package_skill` + `uskills
  package` (zip with embedded per-file-sha256 `package.json`, offline
  verifiable); MCP bridge (`adapters/mcp_bridge.py`) registering MCP
  tool declarations into the governed ToolRegistry with `network`
  permission and non-idempotent defaults; Manifest gains
  `security.risk_level`.
- **Sprint 4 evaluation**: honest metrics (output validity, consistency —
  `null` for single repeats, latency mean/p95, token usage, cost via a
  pricing table — `null` for unknown models, tool success rate, security
  probe rate); multi-model benchmark matrix (`eval --models a,b,c` +
  `run_eval_matrix`/`matrix_summary`); version comparison (`--compare`)
  and the release regression gate (`--gate --max-drop-pp`, non-zero exit
  on unexplained regressions, CI-blockable); LLM-as-a-Judge with a fixed
  rubric and recorded judge model, stored separately and never flipping
  deterministic pass/fail (`--judge`); three versioned eval datasets under
  `evals/datasets/` for shipped skills (incl. injection probes).
- **Sprint 3 runtime controls**: JSON-Schema input constraints (`enum`,
  `minimum`/`maximum`, `min_length`/`max_length`, `pattern`, `nullable`,
  array `items_type`, full `schema` override) enforced before any model
  call; full output JSON Schema validation with a bounded repair loop
  (`control.repair`, default 2, 0 disables — never unbounded retries);
  cooperative `CancelToken` (+ `CANCELLED` state); exponential backoff
  (`control.backoff_base`, capped at 30s); `idempotent=False` tools are
  never auto-retried; composite DAG scheduling via `execute.depends_on`
  with Kahn levels, level-parallelism (`control.max_workers`), and
  cycle/unknown-dependency rejection.
- Providers: `anthropic` (Messages API, lazy import), `openai-compatible`
  (env-configurable `USKILLS_OPENAI_BASE_URL`), `local` (Ollama/llama.cpp/
  vLLM via the OpenAI wire protocol); conservative capability declarations
  with the engine's schema re-validation as the real gate.
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

### Fixed
- Generated skill index (indexer) now emits anchors compatible with the
  site slugify; navigation links for CJK SOP names resolve (previously
  mkdocs reported "no such anchor").
- Docs site configures `toc.slugify = slugify_unicode` so generated
  skill-catalog anchors preserve CJK headings (matches `indexer._anchor`).
- GitHub Pages landing page rebuilt for 2.0: hero + run-preview terminal,
  stats band, six-stage engineering loop, capability cards, offline
  tabbed quickstart, version timeline; custom `home` template and
  responsive landing CSS (light/dark).

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
