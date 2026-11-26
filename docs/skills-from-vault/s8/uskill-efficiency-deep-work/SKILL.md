---
name: uskill-efficiency-deep-work
description: "让深度工作变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-deep-work.md"
  original_id: "SKL-6913"
  version: "3.0.0"
  trust: untrusted
---

# 深度工作

description: |
  当用户需要进入深度专注状态、消除干扰、安排专注时间块、提升认知产出质量时使用此 Skill。
  触发词包括：'深度工作'、'专注'、'心流'、'不分心'、'高效工作'、
  '时间块'、'消除干扰'、'认知产出'。当用户讨论工作效率、时间管理、
  项目推进时，即使未直接说"深度工作"，也应使用此 Skill。
  不适用于协作型工作（使用会议纪要 Skill）。遇到需要深度专注的任务时优先使用。

---

⚙️ AI-Co 运行配置块
触发场景: 用户说'深度工作'、'专注'、'心流'、'高效工作'、'时间块'
复用率预估: 高
一键调用: |
  任务分析→时间块设计→环境配置→干扰管理→心流触发
输入Schema: |
  task: string — 需要深度工作的任务（必填）
  duration_minutes: number — 专注时长，默认90
  time_of_day: enum(morning/afternoon/evening/auto) — 默认 auto
  interruption_level: enum(low/medium/high) — 默认 high
输出Schema: |
  status: string
  work_block_design: {duration, phases, optimal_time, energy_alignment}
  environment_setup: {physical, digital, social, mental}
  interruption_management: {prevention, handling, recovery}
  flow_state_triggers: [{trigger, importance, implementation}]
  monitoring_metrics: {quantitative, qualitative, targets}
  post_work_review: {what_worked, what_to_improve}
AI可执行度: 100%

# uSkill-201: 深度工作

## 🎯 目标

> 建立深度工作习惯，在无干扰状态下专注于高认知需求任务，最大化认知产出。

**核心价值**：在注意力稀缺的时代，深度工作是最稀缺、最有价值的能力。

**适用场景**：
- 编程和软件开发
- 写作和创作
- 学习和研究
- 战略规划
- 复杂问题解决

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task` | `string` | ✅ | — | 需要深度工作的任务 |
| `duration_minutes` | `number` | ❌ | `90` | 专注时长（分钟） |
| `time_of_day` | `enum` | ❌ | `auto` | `morning` / `afternoon` / `evening` / `auto` |
| `interruption_level` | `enum` | ❌ | `high` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话深度工作建议",
  "deep_work_id": "DW-YYYY-MMDD-NNN",

  "work_block_design": {
    "duration": "number — 分钟",
    "phases": [
      {
        "phase": "warmup|focus|break|review",
        "duration": "number — 分钟",
        "activity": "string"
      }
    ],
    "optimal_time": "string",
    "energy_alignment": "string"
  },

  "environment_setup": {
    "physical": ["string"],
    "digital": ["string"],
    "social": ["string"],
    "mental": ["string"]
  },

  "interruption_management": {
    "prevention": ["string"],
    "handling": ["string"],
    "recovery": "string"
  },

  "flow_state_triggers": [
    {
      "trigger": "string",
      "importance": "high|medium|low",
      "implementation": "string"
    }
  ],

  "monitoring_metrics": {
    "quantitative": ["string"],
    "qualitative": ["string"],
    "targets": {
      "focus_duration": "number — 分钟",
      "interruption_count": "number",
      "flow_state_achieved": "boolean"
    }
  },

  "post_work_review": {
    "what_worked": ["string"],
    "what_to_improve": ["string"],
    "adjustments_for_next": ["string"]
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

### Step 1: 任务分析与规划

- **输入**：`task` + `duration_minutes`
- **动作**：
  1. 分析任务的认知需求
  2. 设计专注时间块
  3. 对齐精力水平
- **输出**：`work_block_design`
- **时间块设计原则**：

| 阶段 | 时长 | 目的 |
|------|------|------|
| 热身 | 5-10 分钟 | 进入状态 |
| 深度专注 | 60-90 分钟 | 核心工作 |
| 短休息 | 5-10 分钟 | 恢复精力 |
| 回顾 | 5-10 分钟 | 总结产出 |

### Step 2: 环境准备

- **输入**：`work_block_design`
- **动作**：
  1. 设置物理环境
  2. 配置数字环境
  3. 管理社交环境
- **输出**：`environment_setup`
- **环境清单**：

| 类型 | 准备项 |
|------|--------|
| 物理 | 整洁桌面、舒适椅子、适当光线 |
| 数字 | 关闭通知、使用专注模式、准备工具 |
| 社交 | 告知他人、设置"请勿打扰" |
| 心理 | 明确目标、排除杂念 |

### Step 3: 干扰管理

- **输入**：`interruption_level`
- **动作**：
  1. 预防干扰
  2. 处理不可避免的干扰
  3. 设计恢复策略
- **输出**：`interruption_management`

### Step 4: 心流触发

- **输入**：`task` + `work_block_design`
- **动作**：
  1. 识别心流触发条件
  2. 设计挑战-技能平衡
  3. 设定明确目标
- **输出**：`flow_state_triggers`
- **心流触发器**：

| 触发器 | 描述 |
|--------|------|
| 明确目标 | 知道要做什么 |
| 即时反馈 | 知道做得怎么样 |
| 挑战-技能平衡 | 任务难度适中 |
| 深度专注 | 无干扰状态 |
| 控制感 | 感觉能掌控任务 |

### Step 5: 监控与回顾

- **输入**：实际执行数据
- **动作**：
  1. 监控关键指标
  2. 进行事后回顾
  3. 生成改进建议
- **输出**：`monitoring_metrics` + `post_work_review`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**安排超过 4 小时的连续深度工作
2. **不得**忽视休息和恢复
3. **必须**考虑个人精力模式

### 软性约束（建议遵守）
1. 建议每天安排 2-3 个深度工作块
2. 建议在精力高峰期安排最难的任务
3. 建议每周回顾深度工作效果

##

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
