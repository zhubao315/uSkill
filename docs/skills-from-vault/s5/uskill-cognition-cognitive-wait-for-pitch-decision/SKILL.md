---
name: uskill-cognition-cognitive-wait-for-pitch-decision
description: "让cognitive wait for pitch decision变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-wait-for-pitch-decision.md"
  original_id: "SKL-6847"
  version: "3.0.0"
  trust: untrusted
---

# cognitive wait for pitch decision

# Wait for the Pitch Decision / 等待击球法则

## Goal

Most people should do nothing most of the time. Truly life-changing decisions number only a few in a lifetime. This skill trains you to classify decisions, define clear "strike zone" criteria, and concentrate resources when the right opportunity arrives — minimizing decision fatigue and maximizing compounding returns.

## Core Insight

> "The big money is not in the buying and selling, but in the waiting." — Charlie Munger

Decision fatigue erodes judgment. Compounding favors concentration. Good opportunities are rare — but when they appear, acting decisively yields outsized returns.

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `decision` | string | Yes | The decision or opportunity currently under consideration |
| `domain` | string | No | Life domain: `investment`, `career`, `relationship`, `business`, `health`, `other` |
| `current_knowledge_level` | string | No | Your current understanding/preparedness: `low`, `medium`, `high` |
| `time_pressure` | string | No | Perceived urgency: `none`, `low`, `medium`, `high` |
| `criteria_met` | object | No | Key-value pairs of your strike zone criteria and whether each is met |

## Output

```json
{
  "decision_class": "routine | important | life-changing",
  "strike_zone_hit": true,
  "criteria_assessment": {
    "met": ["criterion_1", "criterion_2"],
    "not_met": ["criterion_3"],
    "unknown": ["criterion_4"]
  },
  "recommendation": "act_now | prepare_and_wait | dismiss",
  "confidence": 0.0,
  "preparation_actions": ["action_1", "action_2"],
  "rationale": "Explanation of the recommendation"
}
```

## Execution Steps

### Step 1: Classify the Decision

Categorize the decision into one of three tiers:

- **Routine** — Low consequence, reversible, frequent (daily meals, minor purchases). Decide quickly or automate.
- **Important** — Moderate consequence, partially reversible (job changes, large purchases). Apply standard analysis.
- **Life-changing** — High consequence, largely irreversible, rare (career pivot, marriage, major investment). Enter the strike zone protocol.

### Step 2: Define Strike Zone Criteria

For important and life-changing decisions, list all criteria that must be met before acting. Only act when **ALL** criteria are satisfied.

Example strike zone for a career change:
- [ ] Compensation ≥ current + 30%
- [ ] Role aligns with 10-year vision
- [ ] Company has strong fundamentals
- [ ] Team culture fits personal values
- [ ] No better alternative exists in 6-month horizon

### Step 3: Fill Waiting Time with Preparation

While waiting for criteria to be met:
- **Learn**: Deepen domain knowledge, study comparable cases
- **Build**: Develop skills, relationships, and resources needed for when the moment arrives
- **Monitor**: Track whether conditions are moving toward or away from your strike zone
- **Refine**: Adjust criteria based on new information

### Step 4: Concentrate When Criteria Are Met

When ALL strike zone criteria are hit:
- Act decisively and with full conviction
- Allocate disproportionate resources — this is the moment the preparation was for
- Avoid half-measures; the rarity of the opportunity justifies bold action
- Document the decision for future retrospective

## Exception Handling

| Situation | Action |
|---|---|
| Time pressure is genuine (not perceived) | Verify with a pre-mortem: "What if I don't act now?" If irreversible loss is certain, act |
| Too many criteria never met | Re-evaluate criteria — they may be too restrictive; adjust or accept the opportunity is not for you |
| Emotional pressure to act | Apply the "24-hour rule" — sleep on it. If still feels urgent after cooling down, re-evaluate |
| Criteria met but anxiety persists | Normal. Anxiety ≠ bad decision. Review your criteria objectively; if all are met, execute |

## Self-Check

After applying this skill, verify:

- [ ] Did I correctly classify the decision tier?
- [ ] Did I resist acting on incomp

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
