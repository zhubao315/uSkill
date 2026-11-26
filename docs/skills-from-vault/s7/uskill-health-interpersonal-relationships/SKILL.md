---
name: uskill-health-interpersonal-relationships
description: "让人际关系变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-interpersonal-relationships.md"
  original_id: "SKL-6825"
  version: "3.0.0"
  trust: untrusted
---

# 人际关系

description: |
  当用户需要改善人际关系、学习沟通技巧、处理冲突、建立深度连接时使用此 Skill。
  触发词包括：'人际关系'、'沟通'、'亲密关系'、'冲突'、'边界'、
  '非暴力沟通'、'关系改善'。当用户讨论家庭、朋友、同事关系时，
  即使未直接说"人际关系"，也应使用此 Skill。
  不适用于严重关系问题（建议专业咨询）。遇到日常关系改善需求时优先使用。

---

# uSkill-305: 人际关系

## 🎯 目标

> 基于心理学原理，提升沟通技巧，建立和维护健康的人际关系。

**核心价值**：人际关系是幸福感的最重要预测因素。好的关系需要刻意经营。

**适用场景**：
- 亲密关系维护
- 家庭关系改善
- 职场关系建设
- 友谊深化
- 冲突解决

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `relationship_type` | `enum` | ✅ | — | `romantic` / `family` / `friendship` / `work` |
| `current_challenges` | `array` | ❌ | `[]` | 当前挑战 |
| `relationship_context` | `string` | ❌ | — | 关系背景描述 |
| `improvement_goal` | `string` | ❌ | — | 改善目标 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话关系建议",
  "relationship_id": "IR-YYYY-MMDD-NNN",

  "relationship_assessment": {
    "current_state": "distant|neutral|connected|intimate",
    "strengths": ["string"],
    "areas_for_growth": ["string"],
    "communication_patterns": "string"
  },

  "communication_framework": {
    "non_violent_communication": {
      "observations": "string",
      "feelings": "string",
      "needs": "string",
      "requests": "string"
    },
    "active_listening": {
      "techniques": ["string"],
      "common_mistakes": ["string"]
    },
    "assertive_communication": {
      "i_statements": ["string"],
      "boundary_setting": ["string"]
    }
  },

  "relationship_building": {
    "emotional_intimacy": {
      "practices": ["string"],
      "exercises": ["string"]
    },
    "quality_time": {
      "activities": ["string"],
      "frequency": "string"
    },
    "appreciation_expression": {
      "methods": ["string"],
      "frequency": "string"
    }
  },

  "conflict_resolution": {
    "prevention": ["string"],
    "in_the_moment": ["string"],
    "repair_conversation": {
      "steps": ["string"],
      "template": "string"
    }
  },

  "boundary_setting": {
    "types": ["string"],
    "communication_scripts": ["string"],
    "enforcement_strategies": ["string"]
  },

  "growth_plan": {
    "daily_practices": ["string"],
    "weekly_exercises": ["string"],
    "milestones": [
      {
        "milestone": "string",
        "timeline": "string",
        "success_criteria": "string"
      }
    ]
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

### Step 1: 关系评估

- **输入**：`relationship_type` + `relationship_context`
- **动作**：
  1. 评估当前关系状态
  2. 识别优势和成长领域
  3. 分析沟通模式
- **输出**：`relationship_assessment`
- **关系状态指标**：

| 状态 | 特征 | 改善重点 |
|------|------|----------|
| 疏远 | 缺乏连接 | 建立连接 |
| 中性 | 平淡但稳定 | 增加深度 |
| 连接 | 有情感连接 | 维护和深化 |
| 亲密 | 深度连接 | 保持和成长 |

### Step 2: 沟通框架

- **输入**：`relationship_assessment`
- **动作**：
  1. 应用非暴力沟通
  2. 练习积极倾听
  3. 学习自信沟通
- **输出**：`communication_framework`
- **非暴力沟通四要素**：

| 要素 | 内容 | 示例 |
|------|------|------|
| 观察 | 描述事实 | "你昨晚没回家" |
| 感受 | 表达感受 | "我感到担心" |
| 需要 | 说明需要 | "因为我需要安全感" |
| 请求 | 提出请求 | "你能提前告诉我吗？" |

### Step 3: 关系建设

- **输入**：`relationship_type` + `improvement_goal`
- **动作**：
  1. 设计情感亲密练习
  2. 安排高质量时间
  3. 设计表达欣赏的方式
- **输出**：`relationship_building`

### Step 4: 冲突解决

- **输入**：`current_challenges`
- **动作**：
  1. 设计冲突预防策略
  2. 提供即时应对技巧
  3. 设计修复对话模板
- **输出**：`conflict_resolution`

### Step 5: 边界设定

- **输入**：`relationship_type`
- **动作**：
  1. 识别需要设定的边界
  2. 提供沟通话术
  3. 制定执行策略
- **输出**：`boundary_setting`

### Step 6: 成长计划

- **输入**：所有前序输出
- **动作**：
  1. 设计日常练习
  2. 安排每周练习
  3. 设定里程碑
- **输出**：`growth_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视关系中的虐待
2. **不得**强迫改变对方
3. **必须**尊重个体差异

### 软性约束（建议遵守）
1. 建议从小改变开始
2. 建议保持耐心
3. 建议寻求专业帮助（必要时）

### 人工兜底点
- 当存在虐待关系时，**必须**建议专业帮助
- 当关系问题严重时，**必须**建议 couples therapy

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IR_WARNING_STAGNANT` | 关系停滞 | 建议增加互动 | 🟡 |
| `IR_WARNING_CONFLICT` | 频繁冲突 | 建议学习冲突解决 | 🟡 |
| `IR_ERROR_ABUSE` | 存在虐待 | 建议专业帮助 | 🔴 |

---

## ✅ 校验验

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
