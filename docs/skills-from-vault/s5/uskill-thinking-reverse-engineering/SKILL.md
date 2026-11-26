---
name: uskill-thinking-reverse-engineering
description: "让逆向工程思维变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-reverse-engineering.md"
  original_id: "SKL-5118"
  version: "3.0.0"
  trust: untrusted
---

# 逆向工程思维

# 🎯 目标

运用逆向工程思维方法论，从可观测的结果出发，反向推导原因、机制和因果链条，为问题诊断、竞品分析、系统理解和根因分析提供结构化的逆向推理框架。

**核心价值**：将"结果"转化为"可复制的知识"，从成功中学习、从失败中避免。

**适用场景**：产品竞品分析、技术故障诊断、成功案例研究、系统行为逆向分析、市场现象归因。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `observed_result` | string | 是 | - | 需要逆向分析的可观测结果 |
| `result_type` | enum | 否 | "unknown" | 结果类型：success / failure / neutral / unknown |
| `available_evidence` | list | 否 | [] | 可获取的证据和数据 |
| `analysis_depth` | enum | 否 | "standard" | 分析深度：surface / standard / deep |
| `context` | string | 否 | "" | 结果发生的背景信息 |
| `comparison_targets` | list | 否 | [] | 需要对比的案例（可选） |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `observed_result` 必须是具体的、可观测的结果描述
- `available_evidence` 至少包含 1 条证据或数据点
- `analysis_depth` = deep 时，要求提供 `available_evidence` 至少 3 条
- 不支持纯假设性的结果分析

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "result_analysis": {
      "type": "object",
      "properties": {
        "result": {"type": "string"},
        "type": {"type": "string"},
        "observable_indicators": {"type": "array", "items": {"type": "string"}},
        "anomalies": {"type": "array", "items": {"type": "string"}},
        "baseline_comparison": {"type": "string"}
      }
    },
    "reverse_causal_chain": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step": {"type": "number"},
          "effect": {"type": "string"},
          "cause": {"type": "string"},
          "mechanism": {"type": "string"},
          "evidence": {"type": "array", "items": {"type": "string"}},
          "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
          "alternative_explanations": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "root_cause_analysis": {
      "type": "object",
      "properties": {
        "primary_cause": {"type": "string"},
        "contributing_causes": {"type": "array", "items": {"type": "string"}},
        "enabling_factors": {"type": "array", "items": {"type": "string"}},
        "root_cause_confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "five_whys_log": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "level": {"type": "number"},
              "question": {"type": "string"},
              "answer": {"type": "string"}
            }
          }
        }
      }
    },
    "mechanism_decomposition": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "component": {"type": "string"},
          "function": {"type": "string"},
          "interaction": {"type": "string"},
          "criticality": {"type": "string", "enum": ["critical", "important", "supportive"]}
        }
      }
    },
    "competitive_analysis": {
      "type": "object",
      "properties": {
        "target": {"type": "string"},
        "success_factors": {"type": "array", "items": {"type": "string"}},
        "differentiation": {"type": "array", "items": {"type": "string"}},
        "replicability": {"type": "string", "enum": ["high", "medium", "low"]},
        "lessons_learned": {"type": "array", "items": {"type": "string"}}
      }
    },
    "diagnostic_recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "finding": {"type": "string"},
          "recommendation": {"type": "string"},
          "priority": {"type": "string", "enum": ["high", "medium", "low"]},
          "implementation_effort": {"type": "string", "enum": ["low", "medium", "high"]}
        }
      }
    },
    "knowledge_extracted": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "principle": {"type": "string"},
          "applicability": {"type": "string"},
          "transferability": {"type": "string", "enu

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
