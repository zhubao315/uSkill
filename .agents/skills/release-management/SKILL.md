---
name: release-management
description: Handles version bumps, changelog, tags and release verification for uSkill. Use when preparing any release or hotfix.
---

# Release Management

## Pre-flight

1. Version is edited in exactly one place: `core/uskills/_version.py`.
2. `CHANGELOG.md` has an entry for the new version (Keep a Changelog format).
3. Schema format changes? Update `SCHEMA_VERSION` in `core/uskills/schema.py`
   only for breaking skill-format changes, and regenerate
   `standards/uskill.schema.json` via `uskills schema`.
4. `python -m build` + install test passes.
5. Full gate: pytest, ruff, mypy, `uskills validate skills/`, `uskills doctor`,
   evaluation suites green.

## Release

1. Tag `vX.Y.Z` matching `_version.py`; push tag and let CI publish.
2. Create the GitHub Release from CHANGELOG notes; state clearly what is
   implemented+tested vs planned.
3. Never rewrite published tags or historical skill assets.

## Rules

- No claims of unimplemented capability in release notes.
- Deprecated features need a migration note and at least one minor-version
  of compatibility.
