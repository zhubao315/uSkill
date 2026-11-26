---
name: uskill-thinking-critical-thinking
description: "让批判性思维变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-critical-thinking.md"
  original_id: "SKL-6850"
  version: "3.0.0"
  trust: untrusted
---

# 批判性思维

description: |
  当用户需要分析论证、识别偏见、评估证据、进行独立思考时使用此 Skill。
  触发词包括：'批判性思维'、'论证分析'、'偏见'、'证据评估'、'独立思考'。
  当用户讨论决策、分析、辩论时，
  即使未直接说"批判性思维"，也应使用此 Skill。
  不适用于简单事实核查（使用信息污染检测）。遇到深度分析时优先使用。

---

# uSkill-110: 批判性思维

## 🎯 目标

> 帮助用户进行独立、客观、深入的思考，识别和避免思维陷阱。

**核心价值**：批判性思维是信息时代的生存技能。它帮助我们区分事实与观点、逻辑与情绪。

**适用场景**：
- 决策分析
- 论证评估
- 偏见识别
- 证据评估
- 信息筛选

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `argument_or_claim` | `string` | ✅ | — | 需要分析的论点或主张 |
| `context` | `string` | ❌ | — | 背景信息 |
| `analysis_depth` | `enum` | ❌ | `standard` | `shallow` / `standard` / `deep` |
| `focus_areas` | `array` | ❌ | `all` | 关注的分析领域 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话批判性分析结论",
  "critical_id": "CT-YYYY-MMDD-NNN",

  "argument_analysis": {
    "premises": [
      {
        "premise": "string",
        "type": "factual|value|assumption",
        "evidence": "string",
        "strength": "strong|moderate|weak"
      }
    ],
    "conclusion": "string",
    "inference_quality": "valid|invalid|uncertain",
    "logical_gaps": ["string"]
  },

  "bias_detection": {
    "detected_biases": [
      {
        "bias": "string",
        "description": "string",
        "evidence": "string",
        "impact": "low|medium|high"
      }
    ],
    "overall_bias_risk": "low|medium|high",
    "debiasing_suggestions": ["string"]
  },

  "evidence_evaluation": {
    "evidence_quality": {
      "relevance": "high|medium|low",
      "sufficiency": "sufficient|insufficient|mixed",
      "reliability": "high|medium|low",
      "currency": "current|somewhat_outdated|outdated"
    },
    "missing_evidence": ["string"],
    "additional_evidence_needed": ["string"]
  },

  "alternative_perspectives": [
    {
      "perspective": "string",
      "argument": "string",
      "strength": "string",
      "weakness": "string"
    }
  ],

  "critical_questions": [
    {
      "question": "string",
      "purpose": "string",
      "expected_insight": "string"
    }
  ],

  "reasoning_framework": {
    "inductive_reasoning": "string",
    "deductive_reasoning": "string",
    "abductive_reasoning": "string"
  },

  "conclusion_assessment": {
    "overall_quality": "strong|moderate|weak",
    "confidence_level": "number",
    "key_caveats": ["string"],
    "recommendation": "string"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 论证分析

- **输入**：`argument_or_claim`
- **动作**：
  1. 识别前提
  2. 识别结论
  3. 评估推理质量
- **输出**：`argument_analysis`
- **论证结构**：

| 部分 | 描述 | 评估要点 |
|------|------|----------|
| 前提 | 支撑结论的基础 | 是否真实、相关 |
| 推理 | 从前提到结论的过程 | 是否有效、充分 |
| 结论 | 论证的最终主张 | 是否合理、有说服力 |

### Step 2: 偏见检测

- **输入**：`argument_analysis`
- **动作**：
  1. 系统性排查偏见
  2. 评估偏见影响
  3. 提供去偏见建议
- **输出**：`bias_detection`
- **常见认知偏见**：

| 偏见 | 描述 | 检测方法 |
|------|------|----------|
| 确认偏误 | 寻找支持性证据 | 是否忽略反面证据 |
| 锚定效应 | 过度依赖初始信息 | 是否受第一印象影响 |
| 可得性偏差 | 高估易获取信息 | 是否过度依赖生动案例 |
| 从众效应 | 随大流 | 是否因多数人相信就相信 |

### Step 3: 证据评估

- **输入**：`argument_analysis.premises`
- **动作**：
  1. 评估证据质量
  2. 识别缺失证据
  3. 确定还需要什么证据
- **输出**：`evidence_evaluation`

### Step 4: 替代视角

- **输入**：`argument_or_claim`
- **动作**：
  1. 寻找不同观点
  2. 评估每个视角
  3. 平衡各方论证
- **输出**：`alternative_perspectives`

### Step 5: 关键问题

- **输入**：`argument_analysis` + `bias_detection`
- **动作**：
  1. 设计批判性问题
  2. 明确提问目的
  3. 预期洞察
- **输出**：`critical_questions`
- **批判性问题库**：

| 问题类型 | 示例问题 |
|----------|----------|
| 来源 | 信息来源可靠吗？ |
| 证据 | 有什么证据支持？ |
| 推理 | 推理过程合理吗？ |
| 假设 | 隐含假设是什么？ |
| 替代 | 有没有其他解释？ |
| 影响 | 谁会受影响？ |

### Step 6: 推理框架

- **输入**：`argument_analysis`
- **动作**：
  1. 分析归纳推理
  2. 分析演绎推理
  3. 分析溯因推理
- **输出**：`reasoning_framework`

### Step 7: 结论评估

- **输入**：所有前序输出
- **动作**：
  1. 综合评估质量
  2. 确定置信水平
  3. 列出注意事项
- **输出**：`conclusion_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**预设立场
2. **不得**忽视反面证据
3. **必须**保持客观公正

### 软性约束（建议遵守）
1. 建议考虑多个视角
2. 建议区分事实与观点
3. 建议保持开放心态

### 人工

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
