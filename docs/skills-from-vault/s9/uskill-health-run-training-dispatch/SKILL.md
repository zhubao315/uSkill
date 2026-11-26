---
name: uskill-health-run-training-dispatch
description: "让年度四阶段周期化计划自动落到每周训练块，并在 HRV 预警时自适应重排，而非僵化照搬课表。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-health-run-training-dispatch.md"
  original_id: "SKL-7121"
  version: "3.0.0"
  trust: untrusted
---

# 跑步训练调度

description: |
  当用户需要制定或重排跑步周训练计划时使用此 Skill。
  触发词包括：'跑步计划'、'本周训练'、'排一下跑步'、'训练调度'、'HRV预警重排'。
  即使用户只说'这周怎么跑'，只要意图是安排跑步训练，也应使用此 Skill。
  不适用于力量训练、比赛战术或营养方案（可转交对应 Skill）。

---

# 🏃 uSkill-7121: 跑步训练调度

## 🎯 目标

> 依据年度四阶段周期化框架（Q1 有氧基础 / Q2 极化 / Q3 速度耐力 / Q4 减量备赛），将目标自动落到每周训练块，并在 HRV 异常时自适应重排，保障「心率回归 + 速度突破」双目标稳步达成。

**适用场景**：周训练生成、赛前减量、HRV 熔断重排、阶段目标对齐、月跑量校准。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `phase` | `enum` | ✅ | Q1/Q2/Q3/Q4 当前阶段 |
| `weekly_target_km` | `number` | ✅ | 阶段月均跑量折算的周目标 |
| `hrv_baseline` | `number` | ✅ | 长期 HRV 稳态基线（如 75） |
| `hrv_recent_3d` | `array` | ❌ | 近 3 天 HRV 均值 |
| `last_week_actual` | `number` | ❌ | 上周实际跑量（用于校准） |

---

## 📤 输出

```json
{
  "week_plan": [
    {"day": "周二", "type": "easy|tempo|interval|long", "km": "number", "pace": "string", "hr_zone": "string"}
  ],
  "weekly_km": "number",
  "intensity_ratio": "80/20",
  "hrv_action": "normal|deload",
  "notes": ["string"]
}
```

---

## 🔄 执行流程

```
1. [阶段定位] → 读取 phase 决定结构与跑量
   → Q1：月均120-140km，强制慢跑06'00"-06'30"，HR<150
   → Q2：月均150-170km，80%轻松+20%强度(间歇/Tempo，HR165-175)
   → Q3：月均170-190km，节奏跑+长距离18-25km+间歇
   → Q4：减量备赛，跑量降30%
   → 判断条件：last_week_actual 偏离目标 >10%？
     → 是：本周目标向实际均值回拉，避免连续过载
     → 否：沿用阶段目标

2. [HRV 熔断检查] → 比对 hrv_recent_3d 与基线
   → 规则：均值 < 基线×0.90 且连续3天 → 触发熔断
   → 判断条件：触发熔断？
     → 是：周跑量降50%，所有强度课转轻松跑/休息，标注 deload
     → 否：进入正常排期

3. [结构生成] → 按 80/20 极化排布
   → 规则：≥80% 轻松跑（05'45"-06'00"，HR<150）
   → 规则：≤20% 强度课（间歇800-1200m 或 Tempo 20-30min）
   → 判断条件：本周已有 ≥2 次强度课？
     → 是：其余全部排轻松跑
     → 否：补 1 次间歇 + 1 次节奏跑

4. [长距与节奏] → 周末长距离 + 周中节奏
   → 长距离：18-25km @145-155bpm（Q3）
   → 判断条件：下周有比赛？
     → 是：赛前7天进入减量，长距离砍半
     → 否：正常执行

5. [输出计划] → 生成 week_plan + 比率 + HRV动作 + notes
```

---

## 📝 Prompt 模板

### 标准调度 Prompt

```
你是跑步训练调度 Agent。请生成本周训练计划。

【阶段】{phase}
【周目标跑量】{weekly_target_km} km
【HRV基线】{hrv_baseline}｜【近3天】{hrv_recent_3d}
【上周实际】{last_week_actual}

【调度规则】
1. 按阶段结构排布，守住 80/20 极化比例
2. HRV 均值<基线×0.90 且连续3天 → 周跑量降50%、强度课转轻松
3. 轻松跑 HR<150，强度课 HR165-175
4. 赛前7天减量

【输出格式】
按标准 JSON 输出 week_plan / weekly_km / intensity_ratio / hrv_action / notes。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| HRV 数据缺失 | 按上周实际保守排期 | 标注"未监测"，跑量取下限 |
| 阶段目标未知 | 默认 Q2 极化结构 | 提示用户确认阶段 |
| 连续两周过载 | 强制插入恢复周 | 周跑量降30% |
| 伤痛信号 | 全部转步行/休息 | 标注"伤停"，转交康复 Skill |

---

## ✅ 质量自检

- [ ] week_plan 含 ≥3 次训练且覆盖周末长距离
- [ ] intensity_ratio 符合 80/20
- [ ] HRV 熔断条件已判断并写入 hrv_action
- [ ] 轻松跑 HR 区 <150、强度课在 165-175
- [ ] weekly_km 落在阶段目标±10%

---

## 💡 使用示例

### 示例 1：Q2 正常周

**输入**：
```json
{
  "phase": "Q2",
  "weekly_target_km": 40,
  "hrv_baseline": 75,
  "hrv_recent_3d": [78, 76, 77],
  "last_week_actual": 38
}
```

**输出**：
```json
{
  "week_plan": [
    {"day": "周二", "type": "easy", "km": 10, "pace": "05'50\"", "hr_zone": "<150"},
    {"day": "周四", "type": "interval", "km": 8, "pace": "04'50\"", "hr_zone": "165-175"},
    {"day": "周六", "type": "tempo", "km": 12, "pace": "05'10\"", "hr_zone": "155-165"},
    {"day": "周日", "type": "long", "km": 15, "pace": "05'55\"", "hr_zone": "<150"}
  ],
  "weekly_km": 45,
  "intensity_ratio": "80/20",
  "hrv_action": "normal",
  "notes": ["强度课占比19%，结构健康"]
}
```

### 示例 2：HRV 熔断（边界）

**输入**：
```json
{
  "phase": "Q3",
  "weekly_target_km": 45,
  "hrv_baseline": 75,
  "hrv_recent_3d": [66, 64, 67]
}
```

**输出**：
```json
{
  "hrv_action": "deload",
  "weekly_km": 22,
  "notes": ["HRV均值65.7<67.5(基线×0.9)且连续3天，触发熔断，周跑量降50%"]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | Q2 正常周 | 80/20 计划 + 正常 HRV |
| 2 | HRV 熔断 | 跑量降50% + deload |
| 3 | 上周过载 | 回拉目标 + 恢复周 |
| 4 | 赛前7天 | 长距离砍半减量 |
| 5 | HRV 缺失 | 保守下限排期 |
| 6 | 伤痛信号 | 全转休息 + 转交 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. HRV 跌破基线 10% 必须熔断，不得硬扛
2. 不得给出超越用户历史最大跑量的骤增计划（周增量≤10%）
3. 伤痛信号下不得安排任何跑步负荷

**软性约束（建议遵守）**：
1. 优先沿用已验证的 80/20 极化结构
2. 季节/温度极端时下调强度课占比

**人工兜底点**：
- 当 HRV 异常但用户主观状态极佳时，提示而非强制
- 当疑似过度训练综合征时转交医疗/康复

#### ✅ 校验验收规则

**格式校验**：
- [ ] week_plan 结构完整
- [ ] intensity_ratio 字段存在

**内容校验**：
- [ 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
