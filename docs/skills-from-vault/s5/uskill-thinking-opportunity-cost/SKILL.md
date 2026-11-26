---
name: uskill-thinking-opportunity-cost
description: "让机会成本分析变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-opportunity-cost.md"
  original_id: "SKL-5117"
  version: "3.0.0"
  trust: untrusted
---

# 机会成本分析

# 🎯 目标

运用机会成本分析方法论，系统评估放弃选项的价值，识别显性和隐性成本，进行比较优势分析，为投资配置、时间管理、职业选择和资源分配提供经济学视角的决策支持。

**核心价值**：将"选择的代价"显性化，避免忽视隐性成本导致的次优决策。

**适用场景**：投资组合优化、时间分配决策、职业路径选择、项目优先级排序、资源分配策略。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `decision_context` | string | 是 | - | 需要分析的决策场景 |
| `options` | list | 是 | - | 可选方案列表，每个选项包含描述 |
| `chosen_option` | string | 否 | "" | 用户倾向或已选的方案（可选） |
| `constraints` | list | 否 | [] | 资源、时间、能力等约束条件 |
| `time_horizon` | string | 否 | "1年" | 分析的时间跨度 |
| `value_dimensions` | list | 否 | ["financial", "time", "opportunity"] | 价值评估维度 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `options` 至少包含 2 个备选方案
- `constraints` 应明确不可违反的硬约束
- `time_horizon` 影响机会成本的评估范围
- 不支持无备选方案的单一选择

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "decision_framing": {
      "type": "object",
      "properties": {
        "question": {"type": "string"},
        "constraints": {"type": "array", "items": {"type": "string"}},
        "time_horizon": {"type": "string"},
        "value_dimensions": {"type": "array", "items": {"type": "string"}}
      }
    },
    "options_analysis": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "option": {"type": "string"},
          "description": {"type": "string"},
          "explicit_costs": {"type": "array", "items": {"type": "object"}},
          "explicit_benefits": {"type": "array", "items": {"type": "object"}},
          "implicit_costs": {"type": "array", "items": {"type": "object"}},
          "opportunity_cost_of_choosing": {"type": "object"},
          "risk_profile": {"type": "object"},
          "time_profile": {"type": "object"},
          "total_value_assessment": {"type": "object"}
        }
      }
    },
    "opportunity_cost_matrix": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "chosen": {"type": "string"},
          "forgone": {"type": "string"},
          "opportunity_cost": {"type": "object"},
          "regret_potential": {"type": "string", "enum": ["high", "medium", "low"]},
          "reversibility": {"type": "string", "enum": ["reversible", "partially", "irreversible"]}
        }
      }
    },
    "comparative_advantage": {
      "type": "object",
      "properties": {
        "analysis": {"type": "string"},
        "best_option_per_dimension": {"type": "array", "items": {"type": "object"}},
        "overall_best": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]}
      }
    },
    "hidden_costs_identified": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "cost": {"type": "string"},
          "associated_option": {"type": "string"},
          "magnitude": {"type": "string", "enum": ["high", "medium", "low"]},
          "visibility": {"type": "string", "enum": ["obvious", "subtle", "hidden"]}
        }
      }
    },
    "recommendation": {
      "type": "object",
      "properties": {
        "recommended_option": {"type": "string"},
        "reasoning": {"type": "string"},
        "key_trade_offs": {"type": "array", "items": {"type": "string"}},
        "sensitivity_factors": {"type": "array", "items": {"type": "string"}},
        "implementation_notes": {"type": "array", "items": {"type": "string"}}
      }
    },
    "thinking_models_applied": {"type": "array", "items": {"type": "string"}}
  }
}
```

## 异常输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "error": {"type": "string"},
    "error_code": {"type": "string"},
    "suggestion": {"type": "string"},
    "partial_result": {"type": "object"}
  }
}
```

---

## 📋 执行步骤

## Step 1: 决策框架构建

**输入**：`decision_context` + `constraints` + `time_horizon`

**动作**：
1. 精确表述需要回答的决策问题
2. 界定资源约束和时间范围
3. 明确价值评估维度
4. 识别决策的关键权衡

**输出**：决策框架文档

**检查点**：
- 决策问题是否清晰？
- 约束条件是否完整？
- 价值维度是否合理？

**

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
