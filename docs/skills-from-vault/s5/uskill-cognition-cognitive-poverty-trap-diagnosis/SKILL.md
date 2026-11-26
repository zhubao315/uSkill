---
name: uskill-cognition-cognitive-poverty-trap-diagnosis
description: "让cognitive poverty trap diagnosis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-poverty-trap-diagnosis.md"
  original_id: "SKL-6831"
  version: "3.0.0"
  trust: untrusted
---

# cognitive poverty trap diagnosis

# Poverty Trap Diagnosis Framework

## 🎯 目标

Diagnose systemic resource-constraint traps in any domain using the 4-mechanism framework from Banerjee & Duflo's poverty research. This skill transforms the book's empirical findings into a reusable analytical method applicable to organizational, community, product, or policy contexts where scarcity creates self-reinforcing feedback loops.

**Core thesis:** Poverty traps are not monolithic — they decompose into four distinct mechanisms (Information, Risk, Bandwidth, Institutional), each requiring a different intervention strategy. Effective diagnosis must identify which mechanisms dominate in a given context before prescribing solutions.

## 📥 输入

| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `target_population` | string | ✅ | The group or system under analysis (e.g., "rural smallholder farmers", "early-stage startup founders", "first-gen college students") |
| `resource_constraint` | string | ✅ | The primary scarce resource (e.g., financial capital, health 00-META, education quality, market 00-META) |
| `context_description` | string | ✅ | Situational context including geography, institutional environment, and relevant systemic factors |
| `available_data` | object | ❌ | Optional empirical data: surveys, behavioral observations, outcome metrics, cost structures |
| `comparison_baseline` | string | ❌ | A non-constrained comparison group or theoretical baseline for gap analysis |
| `intervention_budget` | string | ❌ | Resource envelope for potential interventions (affects feasibility filtering) |
| `time_horizon` | string | ❌ | Short-term (0-6mo), medium-term (6-24mo), or long-term (2yr+) orientation |

## 📤 输出

```json
{
  "diagnosis_id": "string",
  "trap_profile": {
    "information_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "info_access_gaps": ["string"],
      "quality_info_cost_assessment": "string",
      "low_cost_delivery_strategies": ["string"]
    },
    "risk_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "systemic_risk_amplifiers": ["string"],
      "conservative_cascade_indicators": ["string"],
      "risk_transfer_mechanisms": ["string"]
    },
    "bandwidth_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "cognitive_load_sources": ["string"],
      "decision_fatigue_indicators": ["string"],
      "simplification_opportunities": ["string"]
    },
    "institutional_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "friction_costs": ["string"],
      "nudge_designs": ["string"],
      "behavioral_interventions": ["string"]
    }
  },
  "dominant_trap_ranking": ["string"],
  "intervention_roadmap": [
    {
      "mechanism": "string",
      "intervention": "string",
      "expected_roi": "string",
      "implementation_difficulty": "low | medium | high",
      "priority": 1
    }
  ],
  "self_check_results": [
    {
      "check": "string",
      "passed": true,
      "notes": "string"
    }
  ]
}
```

## 📋 执行步骤

### Step 1: 情境映射 (Context Mapping)
Map the target population and resource constraint into the diagnostic space. Identify the baseline conditions: What does "non-constrained" look like for this population? Establish measurable indicators for each trap mechanism. Document the institutional landscape — who are the gatekeepers, intermediaries, and service providers?

**Deliverable:** A context map with population characteristics, constraint definitions, and baseline gap estimates.

### Step 2: 信息陷阱诊断 (Information Trap Diagnosis)
Analyze information 00-META asymmetries:
- **Access gaps:** What critical information does the target population lack? Where do they currently get information, and what is the quality gap?
- **Cost of quality info:** Calculate the effective cost (time, money, cognitive effort) of accessing accurate, actio

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
