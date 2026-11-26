---
name: uskill-thinking-second-order
description: "让二阶思维变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-second-order.md"
  original_id: "SKL-5114"
  version: "3.0.0"
  trust: untrusted
---

# 二阶思维

# 🎯 目标

运用二阶思维方法论，超越直接效应分析，系统识别决策的连锁反应、间接效应和长期后果，为政策制定、商业决策、投资判断和人生规划提供更全面的影响评估。

**核心价值**：避免"按下葫芦浮起瓢"的决策陷阱，预见并管理非预期后果。

**适用场景**：政策副作用预测、商业战略长期影响评估、投资决策的隐性风险识别、人生重大选择的全面后果分析。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `decision_or_action` | string | 是 | - | 需要分析的决策或行动 |
| `first_order_effects` | list | 否 | [] | 用户已识别的一阶效应（可选补充） |
| `affected_stakeholders` | list | 否 | [] | 可能受影响的利益相关方 |
| `time_horizon` | enum | 否 | "medium" | 分析时间跨度：short / medium / long |
| `context` | string | 否 | "" | 决策背景信息 |
| `constraints` | list | 否 | [] | 已知的约束条件 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `decision_or_action` 必须是具体的、可执行的决策或行动
- `time_horizon` = long 时，要求提供 `affected_stakeholders` 至少 3 个
- `constraints` 应明确标注不可违反的硬约束
- 不支持分析"什么都不做"作为决策（除非明确选择不行动）

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "decision_analysis": {
      "type": "object",
      "properties": {
        "decision": {"type": "string"},
        "intent": {"type": "string"},
        "assumptions": {"type": "array", "items": {"type": "string"}},
        "constraints": {"type": "array", "items": {"type": "string"}}
      }
    },
    "effect_chain": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "order": {"type": "number"},
          "effect": {"type": "string"},
          "mechanism": {"type": "string"},
          "affected_party": {"type": "string"},
          "probability": {"type": "string", "enum": ["high", "medium", "low"]},
          "magnitude": {"type": "string", "enum": ["high", "medium", "low"]},
          "delay": {"type": "string"},
          "reversibility": {"type": "string", "enum": ["reversible", "partially", "irreversible"]}
        }
      }
    },
    "feedback_loops": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {"type": "string", "enum": ["reinforcing", "balancing"]},
          "description": {"type": "string"},
          "trigger_condition": {"type": "string"},
          "amplification_factor": {"type": "string"}
        }
      }
    },
    "unintended_consequences": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "consequence": {"type": "string"},
          "likelihood": {"type": "string", "enum": ["high", "medium", "low"]},
          "impact": {"type": "string"},
          "early_warning_sign": {"type": "string"},
          "mitigation": {"type": "string"}
        }
      }
    },
    "stakeholder_impact_map": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "stakeholder": {"type": "string"},
          "first_order_impact": {"type": "string"},
          "second_order_impact": {"type": "string"},
          "third_order_impact": {"type": "string"},
          "net_assessment": {"type": "string", "enum": ["positive", "negative", "mixed", "uncertain"]}
        }
      }
    },
    "temporal_analysis": {
      "type": "object",
      "properties": {
        "immediate_effects": {"type": "array", "items": {"type": "string"}},
        "short_term_effects": {"type": "array", "items": {"type": "string"}},
        "medium_term_effects": {"type": "array", "items": {"type": "string"}},
        "long_term_effects": {"type": "array", "items": {"type": "string"}},
        "tipping_points": {"type": "array", "items": {"type": "string"}}
      }
    },
    "mitigation_strategies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "risk": {"type": "string"},
          "strategy": {"type": "string"},
          "cost": {"type": "string", "enum": ["low", "medium", "high"]},
          "effectiveness": {"type": "string", "enum": ["high", "medium", "low"]},
          "monitoring_metric": {"type": "string"}
        }
      }
    },
    "decision_quality_check": {
 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
