---
name: uskill-cognitive-decision-reasoning
description: "让决策推理-Schema变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognitive-decision-reasoning.md"
  original_id: "SKL-6846"
  version: "3.0.0"
  trust: untrusted
---

# 决策推理-Schema

description: |
  当用户需要进行重大决策推理、量化决策信念、检测认知偏差、构建反方论证时使用此 Skill。
  触发词包括：'决策分析'、'贝叶斯'、'认知偏差'、'反方论证'、'决策推理'、
  '先验后验'、'决策日志'、'风险评估'、'决策复盘'。当用户讨论投资决策、
  技术选型、项目优先级、职业选择等需要理性量化支撑的场景时，即使未直接说
  "决策推理"，也应使用此 Skill。不适用于简单日常决策（直接执行即可）。
  遇到重大决策时优先使用，而非凭直觉判断。

---

# uSkill-006: 决策推理

## 🎯 目标

> 将重大决策从直觉判断升级为结构化推理，集成贝叶斯量化、认知偏差检测、反方论证、逻辑校验四维能力，建立「先验→证据→反方→后验→决策→回测」的完整决策闭环。

**核心价值**：让每一次重大决策都有迹可循、可回测、可迭代，沉淀为长期复利的认知资产。

**适用场景**：
- 投资决策（标的筛选、仓位管理、止盈止损）
- 技术选型（架构方案、工具选择、云平台迁移）
- 项目优先级（OKR 设定、资源分配、砍需求）
- 职业选择（跳槽、创业、合作）
- 系统设计（架构决策、方案评审）

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `decision_question` | `string` | ✅ | — | 待决策问题（一句话清晰陈述） |
| `decision_type` | `enum` | ✅ | — | `strategic` / `tactical` / `operational` |
| `prior_belief` | `object` | ✅ | — | `{hypothesis: string, probability: float, basis: string, confidence: float}` |
| `evidence_list` | `array` | ✅ | — | `[{description, strength, reliability, direction}]` |
| `context` | `object` | ❌ | — | `{deadline, stakeholders, risk_tolerance}` |
| `skip_devil_advocate` | `boolean` | ❌ | `false` | 是否跳过反方论证（仅限操作级决策） |

**输入约束**：
- `prior_belief.probability` 范围 0-1
- `prior_belief.basis` 必须为非空（不允许凭空设定先验）
- `evidence_list` 至少包含 1 条证据
- `decision_type = strategic` 时**必须**执行反方论证

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话决策结论",
  "decision_id": "DR-YYYY-NNN",
  "decision_question": "string",
  "decision_type": "strategic|tactical|operational",

  "bayesian_analysis": {
    "prior": {
      "hypothesis": "string",
      "probability": "number",
      "basis": "string",
      "confidence": "number"
    },
    "evidence": [
      {
        "description": "string",
        "strength": "number",
        "reliability": "number",
        "direction": "supportive|contradictory|neutral",
        "bayes_factor": "number"
      }
    ],
    "posterior": {
      "probability": "number",
      "change": "number",
      "robustness": "fragile|stable|robust"
    },
    "sensitivity": {
      "key_variable": "string",
      "flip_threshold": "number",
      "conclusion_stable": true
    }
  },

  "cognitive_bias_check": {
    "confirmation_bias": {"detected": false, "evidence": "string"},
    "anchoring_bias": {"detected": false, "evidence": "string"},
    "overconfidence_bias": {"detected": false, "evidence": "string"},
    "availability_bias": {"detected": false, "evidence": "string"},
    "sunk_cost_bias": {"detected": false, "evidence": "string"},
    "loss_aversion_bias": {"detected": false, "evidence": "string"},
    "survivorship_bias": {"detected": false, "evidence": "string"},
    "overall_risk": "low|medium|high"
  },

  "devil_advocate": {
    "counter_arguments": [
      {
        "title": "string",
        "evidence": "string",
        "severity": "high|medium|low",
        "rebuttal_needed": true
      }
    ],
    "weakness_points": ["string"],
    "revised_confidence": "number"
  },

  "logical_validation": {
    "premises_valid": true,
    "inference_valid": true,
    "fallacies_detected": ["string"],
    "argument_structure": "deductive|inductive|abductive"
  },

  "decision_output": {
    "recommendation": "string",
    "action": "string",
    "stop_loss_condition": "string",
    "key_evidence_needed": ["string"],
    "confidence_level": "number",
    "caveats": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

### 异常输出

```json
{
  "status": "failed",
  "error_code": "DR_ERROR_001",
  "error_message": "先验依据不足，无法进行贝叶斯分析",
  "suggestion": "请提供先验信念的历史数据或专家判断依据",
  "partial_result": {
    "bias_check": "已完成",
    "devil_advocate": "未执行"
  }
}
```

---

## 📋 执行步骤

### Step 1: 问题定义与假设空间构建

- **输入**：`decision_question` + `decision_type`
- **动作**：
  1. 将模糊决策问题拆解为可量化的假设
  2. 确保假设互斥且穷尽（MECE 原则）
  3. 确定决策边界（什么在范围内、什么不在）
- **输出**：结构化假设空间
- **分支条件**：
  - IF 假设不互斥 → 重新定义假设空间
  - IF 假设不穷尽 → 补充"其他"假设
  - IF 问题过于模糊 → 要求用户澄清
- **检查点**：✅ 验证假设满足 ME

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
