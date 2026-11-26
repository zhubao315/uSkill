---
name: uskill-health-sleep-optimization
description: "让睡眠优化变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-sleep-optimization.md"
  original_id: "SKL-6823"
  version: "3.0.0"
  trust: untrusted
---

# 睡眠优化

description: |
  当用户需要改善睡眠质量、优化睡眠环境、建立健康睡眠习惯、解决睡眠问题时使用此 Skill。
  触发词包括：'睡眠'、'失眠'、'睡眠质量'、'睡眠习惯'、'入睡困难'、
  '睡眠环境'、'昼夜节律'、'睡眠卫生'。当用户讨论疲劳、精力不足、
  作息紊乱时，即使未直接说"睡眠优化"，也应使用此 Skill。
  不适用于严重睡眠障碍（建议就医）。遇到睡眠改善需求时优先使用。

---

# uSkill-301: 睡眠优化

## 🎯 目标

> 基于睡眠科学，建立健康的睡眠习惯，优化睡眠环境，提升睡眠质量和精力恢复。

**核心价值**：睡眠是精力恢复的基础，优化睡眠是提升整体效率的关键。

**适用场景**：
- 入睡困难
- 睡眠质量差
- 作息不规律
- 精力不足
- 倒时差

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_sleep_issues` | `array` | ✅ | — | 当前睡眠问题 |
| `sleep_schedule` | `object` | ❌ | — | 当前作息时间 |
| `environment` | `object` | ❌ | — | 睡眠环境描述 |
| `lifestyle` | `object` | ❌ | — | 生活习惯信息 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话睡眠优化建议",
  "sleep_id": "SL-YYYY-MMDD-NNN",

  "sleep_assessment": {
    "issues_identified": ["string"],
    "severity": "mild|moderate|severe",
    "potential_causes": ["string"]
  },

  "sleep_hygiene_recommendations": {
    "schedule": {
      "bedtime": "string",
      "wake_time": "string",
      "consistency": "string"
    },
    "environment": {
      "temperature": "string",
      "lighting": "string",
      "noise": "string",
      "mattress_pillow": "string"
    },
    "pre_sleep_routine": ["string"],
    "avoid": ["string"]
  },

  "circadian_rhythm_optimization": {
    "light_exposure": ["string"],
    "meal_timing": ["string"],
    "exercise_timing": "string",
    "caffeine_cutoff": "string"
  },

  "sleep_quality_metrics": {
    "target_sleep_duration": "string",
    "target_sleep_latency": "string",
    "target_sleep_efficiency": "string",
    "tracking_method": "string"
  },

  "monitoring_plan": {
    "daily_checks": ["string"],
    "weekly_reviews": ["string"],
    "red_flags": ["string"]
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

### Step 1: 睡眠问题评估

- **输入**：`current_sleep_issues`
- **动作**：
  1. 识别具体睡眠问题
  2. 评估严重程度
  3. 分析潜在原因
- **输出**：`sleep_assessment`
- **常见睡眠问题**：

| 问题 | 特征 | 可能原因 |
|------|------|----------|
| 入睡困难 | 超过 30 分钟无法入睡 | 焦虑、咖啡因、屏幕光 |
| 睡眠中断 | 夜间频繁醒来 | 压力、环境噪音、年龄 |
| 早醒 | 比预定时间早醒 | 抑郁、时差、年龄 |
| 睡眠质量差 | 睡够时间但仍疲劳 | 睡眠呼吸暂停、压力 |

### Step 2: 睡眠卫生建议

- **输入**：`sleep_assessment`
- **动作**：
  1. 制定规律作息时间
  2. 优化睡眠环境
  3. 建立睡前程序
- **输出**：`sleep_hygiene_recommendations`
- **睡眠卫生清单**：

| 类别 | 建议 |
|------|------|
| 作息 | 固定就寝和起床时间 |
| 环境 | 凉爽、黑暗、安静 |
| 睡前 | 避免屏幕、放松活动 |
| 避免 | 咖啡因、酒精、大餐 |

### Step 3: 昼夜节律优化

- **输入**：`sleep_hygiene_recommendations`
- **动作**：
  1. 优化光线暴露
  2. 调整进餐时间
  3. 安排运动时间
- **输出**：`circadian_rhythm_optimization`
- **昼夜节律原则**：

| 时段 | 建议 |
|------|------|
| 早晨 | 接触阳光 15-30 分钟 |
| 下午 | 避免咖啡因 |
| 傍晚 | 适度运动 |
| 睡前 | 避免强光 |

### Step 4: 监控计划

- **输入**：所有前序输出
- **动作**：
  1. 设定监控指标
  2. 制定回顾计划
  3. 识别危险信号
- **输出**：`sleep_quality_metrics` + `monitoring_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议使用安眠药（需医生处方）
2. **不得**忽视严重睡眠障碍
3. **必须**建议就医当出现危险信号时

### 软性约束（建议遵守）
1. 建议记录睡眠日记
2. 建议持续追踪至少 2 周
3. 建议考虑个人差异

### 人工兜底点
- 当出现睡眠呼吸暂停症状时，**必须**建议就医
- 当睡眠问题持续 4 周以上时，**必须**建议专业评估

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `SL_WARNING_PERSISTENT` | 问题持续 2 周 | 建议加强干预 | 🟡 |
| `SL_WARNING_SEVERE` | 严重失眠 | 建议就医 | 🔴 |
| `SL_ERROR_SLEEP_APNEA` | 疑似睡眠呼吸暂停 | 建议立即就医 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 睡眠问题已识别
- [ ] 卫生建议已生成
- [ ] 昼夜节律已优化
- [ ] 监控计划已制定

### OVP 验证信号
- 睡眠质量评分 ≥ 80/100
- 入睡时间 < 20 分钟

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "入睡困难",
    "prompt": "我每天晚上躺在床上要1个多小时才能睡着",
    "context": "issues=[入睡困难]",
    "assertions": [
      "sleep_assessment.issues_identified 包含 入睡困难",
      "sleep_hygiene_recommendations 包含 睡前程序",
      "circadian_rhythm_optimization.light_exposure 已建议"
    ],
    "expected_behavior": "针对入睡困难提供建议",
    "critic_attack": "是否考虑了焦虑等因素？"
  },
  {
    "id": "test-002",
    "name": "作息不规律",
    "prompt": "我每天睡觉和起床时间都不一样",
    "context": "

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
