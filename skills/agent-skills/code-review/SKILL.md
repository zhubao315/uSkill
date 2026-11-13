---
name: code-review
description: Reviews code diffs and pull requests for correctness, security, and style issues. Use when asked to review a change, audit a PR, or assess merge risk. Do not use for writing new code or running tests.
license: MIT
metadata:
  version: 1.0.0
  owner: uSkill
---

# Code Review

## When to use

- The user asks to review a diff, patch, or pull request.
- Merge-risk assessment before release.

**Do NOT use for**: writing new code, refactoring requests, or running the
test suite yourself.

## Instructions

1. Read the full diff before judging any hunk.
2. Classify findings by severity: `blocker` / `major` / `minor`.
3. Check the categories in `references/review-policy.md` in order.
4. Report only real issues; an empty findings list is a valid result.
5. Every finding must cite file and line range.

## Output contract

Return JSON:

```json
{
  "findings": [
    {"severity": "major", "file": "path", "lines": "10-12", "issue": "...", "fix": "..."}
  ],
  "verdict": "approve | request_changes",
  "summary": "one sentence"
}
```

## References

- `references/review-policy.md` — full severity definitions and category checklist.
- The `uskill.yaml` manifest next to this file carries the uSkill runtime
  contract (typed outputs, permissions, provenance). Keep it beside
  SKILL.md; it is a uSkill extension, not part of the open spec.
