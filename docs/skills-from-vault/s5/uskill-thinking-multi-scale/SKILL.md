---
name: uskill-thinking-multi-scale
description: "让多尺度思考变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-multi-scale.md"
  original_id: "SKL-5116"
  version: "3.0.0"
  trust: untrusted
---

# 多尺度思考

# 🎯 目标

运用多尺度思考方法论，在时间、空间和抽象层级三个维度上进行系统分析，通过宏观与微观的交替视角，为战略规划、问题诊断、研究设计和系统分析提供层次化的洞察框架。

**核心价值**：避免单一尺度的盲点，发现跨尺度的涌现性质和约束关系。

**适用场景**：企业战略规划（公司-部门-团队-个人）、技术架构设计（系统-模块-组件-函数）、政策分析（国家-地区-社区-个人）、研究设计（理论-假设-实验-数据）。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `problem_description` | string | 是 | - | 需要多尺度分析的问题描述 |
| `analysis_dimensions` | list | 否 | ["time", "space", "abstraction"] | 分析维度：time / space / abstraction |
| `primary_scale` | string | 否 | "" | 用户当前关注的主要尺度 |
| `scale_granularity` | enum | 否 | "standard" | 尺度粒度：coarse / standard / fine |
| `stakeholder_perspective` | string | 否 | "" | 利益相关方视角（可选） |
| `constraints` | list | 否 | [] | 已知的约束条件 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `problem_description` 必须涉及多层次或多尺度的现象
- `analysis_dimensions` 至少包含 1 个维度
- `scale_granularity` = fine 时，每个维度至少 4 个尺度层级
- 不支持单一尺度即可解决的简单问题

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "scale_framework": {
      "type": "object",
      "properties": {
        "dimensions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "dimension": {"type": "string", "enum": ["time", "space", "abstraction"]},
              "scales": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {"type": "string"},
                    "level": {"type": "number"},
                    "description": {"type": "string"},
                    "key_elements": {"type": "array", "items": {"type": "string"}}
                  }
                }
              }
            }
          }
        },
        "scale_interactions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "scales": {"type": "array", "items": {"type": "string"}},
              "interaction_type": {"type": "string", "enum": ["constraint", "emergence", "feedback", "alignment"]},
              "description": {"type": "string"}
            }
          }
        }
      }
    },
    "multi_scale_analysis": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dimension": {"type": "string"},
          "scale_level": {"type": "string"},
          "analysis": {"type": "string"},
          "key_insights": {"type": "array", "items": {"type": "string"}},
          "cross_scale_effects": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "scale_conflicts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "conflict": {"type": "string"},
          "scales_involved": {"type": "array", "items": {"type": "string"}},
          "tension_type": {"type": "string", "enum": ["optimization", "timing", "priority", "resource"]},
          "resolution_approach": {"type": "string"}
        }
      }
    },
    "emergent_properties": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "property": {"type": "string"},
          "emerging_from": {"type": "string"},
          "scale": {"type": "string"},
          "significance": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "scale_specific_recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "scale": {"type": "string"},
          "recommendation": {"type": "string"},
          "rationale": {"type": "string"},
          "trade_offs": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "integration_synthesis": {
      "type": "object",
      "properties": {
        "cross_scale_insights": {"type": "array", "items": {"type": "string"}},
        "leverage_points": {"type": "array", "items": {"type": "string"}},
   

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
