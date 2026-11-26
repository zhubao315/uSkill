---
name: uskill-run-training-dispatch
description: "让跑步训练调度 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-run-training-dispatch.md"
  original_id: "SKL-6903"
  version: "3.0.0"
  trust: untrusted
---

# 跑步训练调度 Agent — 实施手册

description: |
  当用户需要基于训练计划生成每日跑步方案时使用此 Skill。
  触发词包括：'跑步计划'、'今日跑什么'、'训练安排'、'跑步方案'。
  当用户说"今天怎么跑"、"帮我安排跑步"，即使未直接说"训练调度"，也应使用此 Skill。
  不适用于伤病康复期（需医生指导）。用于健康跑者的日常训练安排。

---

# 🏃 uSkill-307: 跑步训练调度

## 🎯 目标

> 基于训练计划和身体状态，生成个性化每日跑步方案，平衡训练效果与伤病风险。

**核心价值**：让每一次跑步都有明确目的，避免"随便跑跑"的低效训练。

**适用场景**：
- 每日晨跑前的训练安排
- 周末长距离跑的方案制定
- 比赛前的减量调整
- 身体状态不佳时的方案修改

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `training_plan` | `object` | ✅ | — | 当前训练计划（周期、目标、周跑量） |
| `body_status` | `object` | ✅ | — | 身体状态（睡眠、疲劳度、HRV、伤痛） |
| `weather` | `object` | ❌ | — | 天气数据（温度、湿度、风力、AQI） |
| `recent_runs` | `array` | ❌ | — | 近期跑步数据（配速、心率、距离） |
| `race_target` | `object` | ❌ | — | 目标赛事（如有） |

**输入约束**：
- `body_status` 至少包含 sleep_quality(1-10) 和 fatigue_level(1-10)
- `recent_runs` 建议提供最近3-7天数据

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话训练建议",
  "training_type": "interval|tempo|easy|long|rest|cross",
  "plan": {
    "warmup": {"duration_min": "number", "description": "string"},
    "main": {"distance_km": "number", "target_pace": "string", "target_hr": "string", "description": "string"},
    "cooldown": {"duration_min": "number", "description": "string"}
  },
  "alerts": [
    {"level": "red|yellow|green", "message": "string"}
  ],
  "adjustments": ["string"]
}
```

---

## 🔄 执行流程

```
1. [状态评估] → 综合评估身体状态
   → 判断条件：sleep_quality < 5 或 fatigue_level > 8？
     → 是：强制休息或轻松跑
     → 否：进入步骤2

2. [训练匹配] → 根据训练计划确定今日类型
   → 规则：根据周期化训练安排（基础期/强化期/巅峰期/竞赛期）
   → 规则：连续高强度不超过2天
   → 判断条件：昨日训练类型？
     → 高强度(LS/间歇) → 今日轻松跑或休息
     → 轻松跑 → 今日可安排中高强度

3. [天气适配] → 根据天气调整方案
   → 温度>32°C → 减量20%+增加补水
   → 湿度>80% → 降低配速目标30s/km
   → AQI>150 → 室内交叉训练
   → 大风(>5级) → 调整路线或改为室内

4. [方案生成] → 输出结构化训练方案
   → 热身：10-15min慢跑+动态拉伸
   → 主课：配速区间+心率区间+距离
   → 放松：10min慢跑+静态拉伸

5. [预警检查] → 伤病风险评估
   → 连续3天高强度 → 🔴 过训预警
   → HRV下降>15% → 🟡 恢复不足
   → 有伤痛报告 → 🔴 停训建议
```

---

## 📝 Prompt 模板

### 标准调度 Prompt

```
你是跑步训练调度Agent。请生成今日跑步方案。

【训练计划】{training_plan}
【身体状态】{body_status}
【天气】{weather}
【近期跑步】{recent_runs}

【调度规则】
1. 根据训练周期确定今日训练类型
2. 根据身体状态调整强度
3. 根据天气调整方案
4. 连续高强度不超过2天

【输出格式】
按标准 JSON 输出，包含训练类型、详细方案、预警、调整建议。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 身体状态极差 | 强制休息建议 | 仅输出休息+恢复建议 |
| 天气极端 | 改为室内交叉训练 | 提供替代方案 |
| 训练计划缺失 | 基于近期数据推断 | 输出通用轻松跑方案 |
| 有伤痛报告 | 建议就医+停训 | 不提供训练方案 |

---

## ✅ 质量自检

- [ ] 训练类型匹配训练周期
- [ ] 强度匹配身体状态
- [ ] 天气因素已考虑
- [ ] 热身+主课+放松完整
- [ ] 配速/心率区间合理
- [ ] 预警有具体依据

---

## 💡 使用示例

### 示例 1：正常训练日

**输入**：
```json
{
  "training_plan": {"week": 8, "phase": "强化期", "target_weekly_km": 60},
  "body_status": {"sleep_quality": 8, "fatigue_level": 4, "hrv": 65},
  "weather": {"temp": 22, "humidity": 55, "aqi": 45},
  "recent_runs": [{"date": "2026-06-28", "type": "easy", "km": 10}]
}
```

**输出**：
```json
{
  "training_type": "tempo",
  "plan": {
    "warmup": {"duration_min": 15, "description": "慢跑+动态拉伸"},
    "main": {"distance_km": 10, "target_pace": "5'00\"/km", "target_hr": "155-165bpm", "description": "节奏跑：2km热身+6km目标配速+2km放松"},
    "cooldown": {"duration_min": 10, "description": "慢跑+静态拉伸"}
  }
}
```

### 示例 2：疲劳累积预警

**输入**：
```json
{
  "body_status": {"sleep_quality": 5, "fatigue_level": 9, "hrv": 45},
  "recent_runs": [{"date": "2026-06-28", "type": "tempo", "km": 12}, {"date": "2026-06-27", "type": "interval", "km": 10}]
}
```

**输出**：
```json
{
  "training_type": "rest",
  "alerts": [{"level": "red", "message": "疲劳度9/10，连续2天高强度，建议强制休息"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 输入要点 | 期望输出 | 边界条件 |
|---|------|----------|----------|----------|
| 1 | 正常训练 | 良好状态+天气好 | tempo/interval方案 | 正常输入 |
| 2 | 疲劳累积 | 疲劳9+连续高强度 | 强制休息 | 过训风险 |
| 3 | 极端天气 | 温度35°C+湿度90% | 室内替代方案 | 天气触发 |
| 4 | 伤病状态 | 有伤痛报告 | 停训+就医 | 伤病红线 |
| 5 | 赛前减量 | 赛前3天 | 轻松跑+调整 | 赛事触发 |

---

## 📊 版本记录

| 版本 | 日期 | 变更内容 | 验证结果 |
|------|------|----------|----------|
| v1.0 | 2026-06-17 | 初始 Prompt wrapper 版本 | — |
| v2.0 | 2026-06-29 | 升级为 Gen3 Schema：补齐 9 模块 | 待验证 |


#### ⚠️ 边界约束

> 此区块定义

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
