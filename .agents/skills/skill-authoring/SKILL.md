---
name: skill-authoring
description: Creates and improves standard Agent Skills (SKILL.md + uskill.yaml) in this repository. Use when adding a new skill or refactoring an existing one.
---

# Skill Authoring

Workflow for producing skills that load on any Agent-Skills-compatible
agent and carry the uSkill engineering contract.

## Steps

1. `python cli/uskills_cli.py init <skill-name>` — scaffolds the two-layer
   layout (SKILL.md + uskill.yaml + references/ + scripts/ + evals/).
2. Name rules: lowercase letters/digits, single hyphens, matches directory,
   ≤64 chars. Description ≤1024 chars and must say *what* and *when*.
3. Keep SKILL.md body under 500 lines and ~5k tokens; push domain detail
   into `references/`, deterministic steps into `scripts/`.
4. Declare positive triggers **and** negative triggers (similar tasks that
   must NOT invoke this skill).
5. Fill `uskill.yaml` (typed inputs/outputs via JSON Schema, execution mode,
   least-privilege permissions, provenance).
6. `python cli/uskills_cli.py validate skills/agent-skills/<name>/` must pass.
7. Add `evals/dataset.json` cases — a skill without evals is a draft.

## Rules

- Never stuff custom fields into the official SKILL.md frontmatter.
- Never auto-generate a skill and mark it Published; the generator model is
  not the reviewer.
