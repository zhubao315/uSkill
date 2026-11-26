---
name: uskill-thinking-first-principles
description: "让第一性原理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-first-principles.md"
  original_id: "SKL-5112"
  version: "3.0.0"
  trust: untrusted
---

# 第一性原理

⚙️ AI-Co 运行配置块
触发场景: 用户说'第一性原理'、'本质思考'、'根本原因'、'底层逻辑'、'假设拆解'
复用率预估: 高
一键调用: |
  拆解假设→识别基本事实→重构认知→创新方案
输入Schema: problem_or_claim: string, domain: string?, current_approach: string?, depth_level: surface|standard|deep, goal: string?, known_facts: list?, output_format: summary|standard|full
输出Schema: original_claim, assumption_decomposition[], foundational_facts[], reconstructed_reasoning[], novel_insights[], reconstructed_approach, thinking_models_applied[]
AI可执行度: 100%

# 🎯 目标

运用第一性原理思维方法，从基本事实和不可进一步分解的前提出发进行推理，拆解隐含假设，重构对问题的认知框架，为创新思考、问题根因分析、技术方案评估和商业模型设计提供根本性的洞察。

**核心价值**：打破类比思维的限制，从物理现实和基本逻辑出发发现真正创新的可能性。

**适用场景**：颠覆式创新构思、技术路线根本性评估、商业模型底层逻辑验证、复杂问题的根因分析。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `problem_or_claim` | string | 是 | - | 需要分析的问题、观点或"常识性"论断 |
| `domain` | string | 否 | "" | 所属领域（技术/商业/社会/个人） |
| `current_approach` | string | 否 | "" | 当前主流做法或已有方案 |
| `depth_level` | enum | 否 | "standard" | 分析深度：surface / standard / deep |
| `goal` | string | 否 | "" | 用户期望达成的目标或解决的问题 |
| `known_facts` | list | 否 | [] | 已知的基本事实或约束条件 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `problem_or_claim` 必须是可以被质疑和拆解的具体论断或问题
- `depth_level` = deep 时，要求提供 `known_facts` 至少 3 条
- `current_approach` 为空时，系统将先识别主流做法再进行拆解
- 不支持纯主观偏好类问题（如"什么是最好的颜色"）

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "original_claim": {"type": "string"},
    "assumption_decomposition": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "assumption": {"type": "string"},
          "category": {"type": "string", "enum": ["explicit", "implicit", "unconscious"]},
          "validity": {"type": "string", "enum": ["valid", "questionable", "invalid"]},
          "evidence_for": {"type": "array", "items": {"type": "string"}},
          "evidence_against": {"type": "array", "items": {"type": "string"}},
          "impact_if_wrong": {"type": "string"}
        }
      }
    },
    "foundational_facts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "fact": {"type": "string"},
          "source": {"type": "string"},
          "certainty": {"type": "string", "enum": ["certain", "high", "medium", "low"]},
          "testable": {"type": "boolean"}
        }
      }
    },
    "reconstructed_reasoning": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step": {"type": "number"},
          "premise": {"type": "string"},
          "inference": {"type": "string"},
          "conclusion": {"type": "string"},
          "gap_check": {"type": "boolean"}
        }
      }
    },
    "novel_insights": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "insight": {"type": "string"},
          "basis": {"type": "string"},
          "implications": {"type": "array", "items": {"type": "string"}},
          "feasibility": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "reconstructed_approach": {
      "type": "object",
      "properties": {
        "description": {"type": "string"},
        "key_principles": {"type": "array", "items": {"type": "string"}},
        "advantages_over_current": {"type": "array", "items": {"type": "string"}},
        "challenges": {"type": "array", "items": {"type": "string"}},
        "validation_needed": {"type": "array", "items": {"type": "string"}}
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

## Step 1: 问题澄清与边界界定

**输入**：`problem_or_claim` + `domain`

**动作**：
1. 精确复述用户的问题或论断
2. 界定问题的领域范围
3. 识别当前主

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
