---
name: repo-audit
description: Audits the uSkill repository structure, dependencies, packaging and CI health. Use before releases, after major refactors, or when asked for a repo audit.
---

# Repo Audit

Purpose: keep the engineering baseline of uSkill trustworthy.

## Checklist

1. `python -m pytest` — all tests green; note any skips.
2. `ruff check .` and `mypy core/` — zero findings.
3. `python cli/uskills_cli.py validate skills/` — all assets valid.
4. `python cli/uskills_cli.py doctor` — environment and asset health.
5. Packaging: `python -m build` produces wheel+sdist; `pip install dist/*.whl`
   then `uskills --version` matches `core/uskills/_version.py`.
6. Version consistency: package version, git tag, CHANGELOG top entry agree.
7. Dependencies: check for stale pins or missing optional extras.
8. Links: no references to the legacy `uSkills` repo name in docs/CI badges.

## Output

Write findings to `docs/audit/` with severity (P0/P1/P2) and file evidence.

## Rules

- Never report an issue without a concrete file/line reference.
- Never "fix" by deleting history or existing skill assets.
