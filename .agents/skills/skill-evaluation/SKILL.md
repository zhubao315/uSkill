---
name: skill-evaluation
description: Runs evaluation suites and regression comparisons for skills in this repository. Use when a skill changed, before release, or when asked whether a skill actually helps.
---

# Skill Evaluation

Core question: **does this skill improve task completion versus no skill?**

## Steps

1. Each skill ships `evals/dataset.json` (EvalSuite: task_id, user_input,
   baseline_prompt, assertions).
2. `python cli/uskills_cli.py eval --skill <file.yaml> --suite <suite.json>
   --provider mock` for deterministic CI checks; swap `--provider
   openai-chat` for real-model runs.
3. Read the report: baseline vs assisted success rates and delta.
4. Deterministic graders decide pass/fail; model-based rubric grading is
   supplementary evidence, never the sole gate.
5. On regression (assisted < baseline, or new security case failure),
   block the release and file findings.

## Gates (initial, configurable per skill)

- trigger precision ≥ 0.90, output validity ≥ 0.99
- no regression vs previous published version
- security probe cases all pass

## Rules

- Never fabricate improvement numbers; without a real run, report "待评测".
- The eval runner must not share state with the skill generator.
