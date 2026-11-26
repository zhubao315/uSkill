---
name: uskill-thinking-systems-thinking
description: "让系统思维变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-systems-thinking.md"
  original_id: "SKL-5111"
  version: "3.0.0"
  trust: untrusted
---

# 系统思维

⚙️ AI-Co 运行配置块
触发场景: 用户说'系统思维'、'系统性思考'、'全局视角'、'因果回路'
复用率预估: 高
一键调用: |
  识别要素→分析关系→绘制回路→识别杠杆点
输入Schema: problem_description(string,必填), system_boundary(enum,默认moderate), time_horizon(string,默认3年), stakeholders(list), existing_data(object), intervention_intent(string), output_format(enum,默认full)
输出Schema: system_map{variables[],feedback_loops[],causal_loop_diagram}, system_archetypes[], leverage_points[], intervention_recommendations[], mental_models_applied[]
AI可执行度: 100%

# 🎯 目标

运用系统思维方法论，识别复杂系统中的反馈回路、杠杆点和系统原型，为组织问题分析、政策评估、环境系统理解和产品生态系统设计提供结构化的系统诊断与干预方案。

**核心价值**：将隐性的系统结构显性化，避免线性思维导致的政策副作用，发现高杠杆干预点。

**适用场景**：组织效率瓶颈诊断、公共政策副作用预测、产品生态系统涌现行为分析、环境与经济系统耦合建模。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `problem_description` | string | 是 | - | 需要分析的系统问题描述，越具体越好 |
| `system_boundary` | enum | 否 | "moderate" | 系统边界范围：narrow / moderate / broad |
| `time_horizon` | string | 否 | "3年" | 分析的时间跨度 |
| `stakeholders` | list | 否 | [] | 已知的利益相关方列表 |
| `existing_data` | object | 否 | {} | 已有的数据、指标或历史信息 |
| `intervention_intent` | string | 否 | "" | 用户期望的干预方向（可选） |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `problem_description` 长度不少于 20 字，必须包含至少一个可观测的现象或症状
- `system_boundary` 选择 broad 时，必须提供 `stakeholders` 列表
- `time_horizon` 格式为数字+时间单位（天/周/月/年）
- 若 `existing_data` 包含时序数据，优先用于识别趋势和周期

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "system_map": {
      "type": "object",
      "properties": {
        "variables": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "type": "enum",
              "enum": ["stock", "flow", "auxiliary"],
              "description": {"type": "string"},
              "measurable": {"type": "boolean"}
            }
          }
        },
        "feedback_loops": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {"type": "string"},
              "type": {"type": "string", "enum": ["reinforcing", "balancing"]},
              "variables": {"type": "array", "items": {"type": "string"}},
              "delay": {"type": "string"},
              "polarity": {"type": "string"}
            }
          }
        },
        "causal_loop_diagram": {"type": "string"}
      }
    },
    "system_archetypes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "match_confidence": {"type": "number", "minimum": 0, "maximum": 1},
          "description": {"type": "string"},
          "typical_behavior": {"type": "string"}
        }
      }
    },
    "leverage_points": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "level": {"type": "string"},
          "description": {"type": "string"},
          "impact_potential": {"type": "string", "enum": ["high", "medium", "low"]},
          "implementation_difficulty": {"type": "string", "enum": ["high", "medium", "low"]},
          "time_to_effect": {"type": "string"},
          "risks": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "intervention_recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "action": {"type": "string"},
          "target_loop": {"type": "string"},
          "expected_effect": {"type": "string"},
          "side_effects": {"type": "array", "items": {"type": "string"}},
          "monitoring_metrics": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "mental_models_applied": {"type": "array", "items": {"type": "string"}}
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
    "suggestion": {"type":

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
