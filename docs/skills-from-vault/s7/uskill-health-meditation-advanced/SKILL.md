---
name: uskill-health-meditation-advanced
description: "让冥想进阶变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-meditation-advanced.md"
  original_id: "SKL-6824"
  version: "3.0.0"
  trust: untrusted
---

# 冥想进阶

description: |
  当用户需要深入冥想练习、学习正念技巧、进行慈悲冥想、提升专注力时使用此 Skill。
  触发词包括：'冥想'、'正念'、'专注'、'慈悲冥想'、'身体扫描'、
  '冥想进阶'、'禅修'。当用户讨论压力管理、专注力提升、情绪调节时，
  即使未直接说"冥想进阶"，也应使用此 Skill。
  不适用于冥想初学者（使用基础冥想指南）。遇到进阶冥想需求时优先使用。

---

# uSkill-304: 冥想进阶

## 🎯 目标

> 提供系统化的冥想进阶路径，从基础正念到高级冥想技巧，提升心理素质。

**核心价值**：冥想是训练心智的"健身房"。持续练习能显著提升专注力和情绪调节能力。

**适用场景**：
- 专注力提升
- 压力管理
- 情绪调节
- 睡眠改善
- 自我认知深化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_level` | `enum` | ❌ | `beginner` | `beginner` / `intermediate` / `advanced` |
| `practice_goal` | `enum` | ❌ | `focus` | `focus` / `stress` / `emotion` / `sleep` / `self_awareness` |
| `available_time` | `number` | ❌ | `10` | 每日可用时间（分钟） |
| `experience` | `object` | ❌ | — | 冥想经验描述 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话冥想建议",
  "meditation_id": "MD-YYYY-MMDD-NNN",

  "level_assessment": {
    "current_level": "beginner|intermediate|advanced",
    "strengths": ["string"],
    "areas_for_growth": ["string"],
    "recommended_focus": "string"
  },

  "practice_path": {
    "current_phase": {
      "name": "string",
      "duration": "string",
      "techniques": ["string"],
      "daily_practice": "string"
    },
    "next_phases": [
      {
        "name": "string",
        "prerequisites": ["string"],
        "techniques": ["string"]
      }
    ]
  },

  "technique_library": [
    {
      "technique": "string",
      "level": "beginner|intermediate|advanced",
      "description": "string",
      "duration": "string",
      "benefits": ["string"],
      "instructions": ["string"]
    }
  ],

  "weekly_schedule": {
    "monday": "string",
    "tuesday": "string",
    "wednesday": "string",
    "thursday": "string",
    "friday": "string",
    "saturday": "string",
    "sunday": "string",
    "total_weekly_minutes": "number"
  },

  "progress_tracking": {
    "daily_metrics": ["string"],
    "weekly_reviews": ["string"],
    "milestones": [
      {
        "milestone": "string",
        "target_date": "string",
        "success_criteria": "string"
      }
    ]
  },

  "common_challenges": [
    {
      "challenge": "string",
      "cause": "string",
      "solution": "string"
    }
  ],

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 水平评估

- **输入**：`current_level` + `experience`
- **动作**：
  1. 评估当前冥想水平
  2. 识别优势和成长领域
  3. 确定练习重点
- **输出**：`level_assessment`
- **冥想水平标准**：

| 水平 | 特征 | 能稳定练习 |
|------|------|:----------:|
| 初学者 | 刚开始，容易分心 | 5-10 分钟 |
| 中级 | 能稳定练习，开始深入 | 15-30 分钟 |
| 高级 | 能进行深度冥想 | 30+ 分钟 |

### Step 2: 练习路径设计

- **输入**：`level_assessment` + `practice_goal`
- **动作**：
  1. 设计当前阶段
  2. 规划进阶路径
  3. 设定里程碑
- **输出**：`practice_path`
- **冥想进阶路径**：

| 阶段 | 时长 | 技巧 |
|------|------|------|
| 基础 | 1-3 个月 | 呼吸观察、身体扫描 |
| 中级 | 3-6 个月 | 慈悲冥想、开放觉知 |
| 高级 | 6+ 个月 | 非二元觉知、三摩地 |

### Step 3: 技巧库构建

- **输入**：`practice_path`
- **动作**：
  1. 选择适合的技巧
  2. 提供详细指导
  3. 标注注意事项
- **输出**：`technique_library`
- **冥想技巧库**：

| 技巧 | 水平 | 时长 | 主要益处 |
|------|:----:|:----:|----------|
| 呼吸观察 | 初级 | 5-10 分钟 | 专注力、平静 |
| 身体扫描 | 初级 | 10-20 分钟 | 放松、身体觉知 |
| 慈悲冥想 | 中级 | 15-30 分钟 | 同理心、情绪调节 |
| 开放觉知 | 中级 | 15-30 分钟 | 觉察力、灵活性 |
| 非二元觉知 | 高级 | 30+ 分钟 | 自我认知、智慧 |

### Step 4: 每周计划

- **输入**：`practice_path` + `available_time`
- **动作**：
  1. 安排每日练习
  2. 平衡不同技巧
  3. 安排休息日
- **输出**：`weekly_schedule`

### Step 5: 进度跟踪

- **输入**：`practice_path`
- **动作**：
  1. 设定日常指标
  2. 设计周度回顾
  3. 设定里程碑
- **输出**：`progress_tracking`

### Step 6: 常见挑战

- **输入**：`level_assessment`
- **动作**：
  1. 识别常见障碍
  2. 分析原因
  3. 提供解决方案
- **输出**：`common_challenges`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议超过能力范围的练习
2. **不得**忽视身心反应
3. **必须**建议循序渐进

### 软性约束（建议遵守）
1. 建议固定练习时间
2. 建议记录练习日记
3. 建议寻找练习伙伴

### 人工兜底点
- 当出现严重身心反应时，**必须**建议暂停
- 当有心理疾病史时，**必须**建议咨询专业人士

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `MD_WARNING_DISTRACTION` | 频繁分心 | 正常，温和带回 | 🟡 |


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
