---
name: uskill-thinking-analogical
description: "让类比推理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-analogical.md"
  original_id: "SKL-5115"
  version: "3.0.0"
  trust: untrusted
---

# 类比推理

# 🎯 目标

运用类比推理方法论，通过跨领域的结构映射，从已知领域迁移模型和解决方案到新领域，为创新启发、教学解释、方案借鉴和概念理解提供系统化的类比分析框架。

**核心价值**：将陌生问题转化为熟悉问题，利用已有知识加速理解和创新。

**适用场景**：创新方案构思、复杂概念教学、跨行业方案借鉴、新产品设计启发、组织变革路径规划。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `target_domain` | string | 是 | - | 需要理解或解决的目标领域问题 |
| `source_domain_hint` | string | 否 | "" | 用户提示的可能类比源域（可选） |
| `problem_type` | enum | 否 | "understanding" | 问题类型：understanding / innovation / explanation / design |
| `mapping_depth` | enum | 否 | "structural" | 映射深度：surface / structural / deep |
| `constraints` | list | 否 | [] | 目标域的约束条件 |
| `existing_analogies` | list | 否 | [] | 用户已有的类比想法（可选验证） |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `target_domain` 必须是具体的、可描述的问题或概念
- `mapping_depth` = deep 时，要求提供 `constraints` 至少 2 条
- `source_domain_hint` 如果提供，系统将优先评估该类比的适用性
- 不支持纯抽象概念的类比（需要具体的结构或过程）

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "target_analysis": {
      "type": "object",
      "properties": {
        "problem": {"type": "string"},
        "key_elements": {"type": "array", "items": {"type": "string"}},
        "relationships": {"type": "array", "items": {"type": "string"}},
        "constraints": {"type": "array", "items": {"type": "string"}},
        "goal": {"type": "string"}
      }
    },
    "analogy_candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source_domain": {"type": "string"},
          "structural_similarity": {"type": "number", "minimum": 0, "maximum": 1},
          "surface_similarity": {"type": "number", "minimum": 0, "maximum": 1},
          "mapping_quality": {"type": "string", "enum": ["excellent", "good", "fair", "poor"]},
          "strengths": {"type": "array", "items": {"type": "string"}},
          "limitations": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "selected_analogy": {
      "type": "object",
      "properties": {
        "source_domain": {"type": "string"},
        "selection_reason": {"type": "string"},
        "structural_mapping": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "source_element": {"type": "string"},
              "target_element": {"type": "string"},
              "mapping_type": {"type": "string", "enum": ["direct", "analogous", "functional"]},
              "confidence": {"type": "string", "enum": ["high", "medium", "low"]}
            }
          }
        },
        "process_mapping": {"type": "array", "items": {"type": "object"}},
        "principle_mapping": {"type": "array", "items": {"type": "object"}}
      }
    },
    "insights_generated": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "insight": {"type": "string"},
          "source": {"type": "string"},
          "implications": {"type": "array", "items": {"type": "string"}},
          "novelty": {"type": "string", "enum": ["high", "medium", "low"]},
          "actionability": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "analogical_reasoning": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step": {"type": "number"},
          "reasoning": {"type": "string"},
          "evidence": {"type": "string"},
          "confidence": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "limitations_and_caveats": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "limitation": {"type": "string"},
          "impact": {"type": "string"},
          "mitigation": {"type": "string"}
        }
      }
    },
    "validation_results": {
      "type": "object",
      "properties": {
        "structural_fit": {"type": "number", "minimum": 0, "maximum": 1},
        "surface_fit": {"

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
