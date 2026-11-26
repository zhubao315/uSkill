---
name: uskill-leadership-coaching
description: "让教练式辅导变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-leadership-coaching.md"
  original_id: "SKL-5404"
  version: "3.0.0"
  trust: untrusted
---

# 教练式辅导

description: |
  当用户需要辅导他人成长、进行教练式对话、帮助他人达成目标、提升他人能力时使用此 Skill。
  触发词包括：'教练'、'辅导'、'coach'、'GROW模型'、'提问技术'、
  '成长辅导'、'职业辅导'。当用户讨论团队发展、人才培养、领导力时，
  即使未直接说"教练式辅导"，也应使用此 Skill。
  不适用于直接指导（告诉答案）。遇到需要引导他人自己找到答案时优先使用。

---

# uSkill-404: 教练式辅导

## 🎯 目标

> 使用 GROW 模型和教练式提问，帮助他人明确目标、探索方案、制定行动计划。

**核心价值**：教练不给答案，而是帮助他人自己找到答案。这比直接指导更持久有效。

**适用场景**：
- 员工发展辅导
- 职业规划辅导
- 绩效改进辅导
- 领导力发展
- 个人成长辅导

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `coachee_context` | `string` | ✅ | — | 被辅导者情况 |
| `coaching_goal` | `string` | ✅ | — | 辅导目标 |
| `session_type` | `enum` | ❌ | `development` | `development` / `performance` / `career` / `personal` |
| `relationship` | `enum` | ❌ | `manager` | `manager` / `peer` / `external` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话辅导建议",
  "coaching_id": "CO-YYYY-MMDD-NNN",

  "coachee_assessment": {
    "current_situation": "string",
    "readiness_level": "low|medium|high",
    "learning_style": "string",
    "potential_blockers": ["string"]
  },

  "grow_session_plan": {
    "goal": {
      "desired_outcome": "string",
      "specific_goals": ["string"],
      "success_criteria": "string",
      "timeframe": "string"
    },
    "reality": {
      "current_state": "string",
      "obstacles": ["string"],
      "resources_available": ["string"],
      "previous_attempts": ["string"]
    },
    "options": {
      "possible_actions": ["string"],
      "pros_and_cons": {
        "action1": {"pros": ["string"], "cons": ["string"]},
        "action2": {"pros": ["string"], "cons": ["string"]}
      },
      "best_option": "string"
    },
    "will": {
      "commitment_level": "low|medium|high",
      "first_step": "string",
      "timeline": "string",
      "support_needed": ["string"],
      "accountability": "string"
    }
  },

  "coaching_questions": {
    "goal_setting": ["string"],
    "reality_check": ["string"],
    "option_exploration": ["string"],
    "commitment": ["string"]
  },

  "coaching_techniques": [
    {
      "technique": "string",
      "description": "string",
      "when_to_use": "string"
    }
  ],

  "session_structure": {
    "opening": "string",
    "main_body": "string",
    "closing": "string",
    "duration": "string"
  },

  "follow_up_plan": {
    "check_in_schedule": "string",
    "progress_metrics": ["string"],
    "adjustment_triggers": ["string"]
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

### Step 1: 被辅导者评估

- **输入**：`coachee_context`
- **动作**：
  1. 了解当前情况
  2. 评估准备度
  3. 识别潜在障碍
- **输出**：`coachee_assessment`

### Step 2: GROW 模型应用

- **输入**：`coaching_goal` + `coachee_assessment`
- **动作**：
  1. 明确目标（Goal）
  2. 探索现实（Reality）
  3. 探索选项（Options）
  4. 确定意愿（Will）
- **输出**：`grow_session_plan`
- **GROW 模型详解**：

| 阶段 | 核心问题 | 目的 |
|------|----------|------|
| Goal | 你想要什么？ | 明确目标 |
| Reality | 现在的情况是什么？ | 了解现状 |
| Options | 你有哪些选择？ | 探索方案 |
| Will | 你打算怎么做？ | 承诺行动 |

### Step 3: 教练式提问设计

- **输入**：`grow_session_plan`
- **动作**：
  1. 设计目标设定问题
  2. 设计现实探索问题
  3. 设计选项探索问题
  4. 设计承诺确认问题
- **输出**：`coaching_questions`
- **教练式提问原则**：

| 原则 | 描述 | 示例 |
|------|------|------|
| 开放式 | 避免是/否问题 | "你怎么看？" |
| 聚焦式 | 针对具体话题 | "关于X，你..." |
| 前进式 | 关注未来 | "接下来你会...?" |
| 力量式 | 发掘资源 | "你有哪些优势？" |

### Step 4: 教练技巧应用

- **输入**：`coachee_assessment` + `grow_session_plan`
- **动作**：
  1. 选择适合的技巧
  2. 应用到对话中
  3. 调整教练风格
- **输出**：`coaching_techniques`
- **教练技巧库**：

| 技巧 | 描述 | 适用场景 |
|------|------|----------|
| 积极倾听 | 全神贯注听对方说 | 全程 |
| 反映情感 | 反映对方的情绪 | 情绪高涨时 |
| 沉默 | 给对方思考空间 | 深度思考时 |
| 澄清 | 确保理解正确 | 信息模糊时 |
| 总结 | 总结关键点 | 阶段转换时 |
| 挑战 | 质疑假设 | 思维受限时 |

### Step 5: 会话结构设计

- **输入**：`grow_session_plan`
- **动作**：
  1. 设计开场
  2. 安排主体
  3. 设计结尾
- **输出**：`session_structure`

### Step 6: 跟进计划

- **输入**：`grow_session_plan`
- **动作**：
  1. 制定跟进时间表
  2. 设定进度指标
  3. 识别调整触发点
- **输出**：`follow_up_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**直接给出答案（除非被问到）
2

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
