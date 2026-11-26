---
name: uskill-thinking-probabilistic
description: "让概率思维变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-probabilistic.md"
  original_id: "SKL-5113"
  version: "3.0.0"
  trust: untrusted
---

# 概率思维

# 🎯 目标

运用概率思维方法论，在不确定性环境下进行结构化决策，包括先验概率设定、贝叶斯信念更新、期望值计算和概率校准，为投资决策、风险评估、不确定性决策和预测校准提供理性的分析框架。

**核心价值**：将模糊的不确定性转化为可计算的概率分布，避免确定性偏差和过度自信。

**适用场景**：投资标的评估、项目风险量化、预测校准训练、战略决策的不确定性分析、医学/法律中的证据评估。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `decision_context` | string | 是 | - | 需要概率分析的决策场景描述 |
| `possible_outcomes` | list | 是 | - | 可能结果列表，每个结果包含描述和初始判断 |
| `prior_beliefs` | object | 否 | {} | 已有的先验信念（概率分布或主观判断） |
| `new_evidence` | list | 否 | [] | 新证据列表，用于贝叶斯更新 |
| `evidence_reliability` | object | 否 | {} | 证据可靠性评估（每个证据的可信度） |
| `risk_tolerance` | enum | 否 | "moderate" | 风险偏好：conservative / moderate / aggressive |
| `time_horizon` | string | 否 | "" | 决策的时间跨度 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `possible_outcomes` 至少包含 2 个互斥结果
- `new_evidence` 中的每个证据必须有 `evidence_reliability` 对应评估
- `prior_beliefs` 如果提供，概率之和必须为 1.0（±0.01 容差）
- `risk_tolerance` 影响期望值计算中的风险调整权重

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
        "time_horizon": {"type": "string"},
        "key_uncertainties": {"type": "array", "items": {"type": "string"}},
        "reference_class": {"type": "string"}
      }
    },
    "probability_distribution": {
      "type": "object",
      "properties": {
        "outcomes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "outcome": {"type": "string"},
              "prior_probability": {"type": "number", "minimum": 0, "maximum": 1},
              "evidence_impact": {"type": "array", "items": {"type": "object"}},
              "posterior_probability": {"type": "number", "minimum": 0, "maximum": 1},
              "confidence_level": {"type": "string", "enum": ["high", "medium", "low"]}
            }
          }
        },
        "total_probability": {"type": "number"},
        "distribution_shape": {"type": "string"}
      }
    },
    "bayesian_update_log": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "evidence": {"type": "string"},
          "reliability": {"type": "number", "minimum": 0, "maximum": 1},
          "likelihood_ratio": {"type": "number"},
          "prior": {"type": "number"},
          "posterior": {"type": "number"},
          "update_magnitude": {"type": "string", "enum": ["large", "moderate", "small"]}
        }
      }
    },
    "expected_value_analysis": {
      "type": "object",
      "properties": {
        "outcomes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "outcome": {"type": "string"},
              "probability": {"type": "number"},
              "value": {"type": "number"},
              "expected_contribution": {"type": "number"}
            }
          }
        },
        "total_expected_value": {"type": "number"},
        "risk_adjusted_value": {"type": "number"},
        "variance": {"type": "number"},
        "downside_risk": {"type": "number"}
      }
    },
    "calibration_check": {
      "type": "object",
      "properties": {
        "overconfidence_risk": {"type": "string", "enum": ["high", "medium", "low", "none"]},
        "base_rate neglect": {"type": "boolean"},
        "availability_bias_risk": {"type": "string", "enum": ["high", "medium", "low", "none"]},
        "suggested_calibration": {"type": "string"}
      }
    },
    "decision_recommendation": {
      "type": "object",
      "properties": {
        "recommended_option": {"type": "string"},
        "reasoning": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "sensitivity_factors": {"type": "array", "items": {"type": "string"}},
        "pre_commitment": {"type": "string"}
      }
    },
    "thinking_models

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
