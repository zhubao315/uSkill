---
name: uskill-health-lifestyle-running-training-plan
description: "让lifestyle running training plan变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-lifestyle-running-training-plan.md"
  original_id: "SKL-5106"
  version: "3.0.0"
  trust: untrusted
---

# lifestyle running training plan

# Running Training Plan Management

> **角色**: 健身跑者 (Fitness Runner) | **核心工具**: AI大模型, Strava/Garmin, uPrompt | **效率目标**: 自动化训练分析，将计划调整时间缩短90%

## 🎯 目标

以**长期主义**为核心，构建数据驱动、AI赋能的动态训练与恢复管理系统，科学提升运动表现、预防伤病，并实现身心状态的持续优化。

**适用场景**:
1. **首马备赛** — 报名全程马拉松，需要制定科学的16周备赛计划
2. **伤后恢复** — 从伤病中恢复，需要循序渐进的复健跑计划
3. **平台期突破** — 配速瓶颈，需要通过间歇跑和力量训练组合提升最大摄氧量

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `race_goal` | string | ✅ | 赛事目标，如"北京马拉松PB 3:30:00"或"全年无伤跑2000km" |
| `current_fitness` | object | ✅ | 当前体能数据：`{best_pace_min_km, weekly_km, max_hr, resting_hr, hrv}` |
| `race_date` | string | ❌ | 目标赛事日期（YYYY-MM-DD），用于倒推训练周期 |
| `training_phase` | enum | ❌ | `base` / `build` / `peak` / `taper`，默认自动判断 |
| `injury_history` | string | ❌ | 伤病史描述，用于风险规避 |
| `available_days_weekly` | int | ❌ | 每周可用训练天数，默认 5 |
| `equipment_data` | string | ❌ | 运动平台数据导出（Strava/Garmin CSV），用于AI分析 |

## 📤 输出

### 核心交付物

1. **《年度/季度训练计划》** — 包含明确的周期划分（基础期、强化期、巅峰期、恢复期）和赛事目标
2. **《周度训练与营养方案》** — 每日训练内容、强度、时长及对应的营养和恢复建议
3. **《周度/月度训练复盘与洞察报告》** — 基于数据分析，评估进展，识别风险，提出调整建议

### 输出结构

```json
{
  "macro_plan": {
    "total_weeks": "int — 总训练周数",
    "phases": [
      {
        "name": "string — base / build / peak / taper",
        "weeks": "int — 该阶段周数",
        "weekly_km_range": "string — 周跑量范围",
        "focus": "string — 训练重点"
      }
    ],
    "target_weekly_km_peak": "number — 巅峰期周跑量"
  },
  "micro_plan": {
    "week_number": "int — 当前第几周",
    "daily_sessions": [
      {
        "day": "string — 周一至周日",
        "type": "string — easy / interval / tempo / long / rest / strength",
        "description": "string — 具体训练内容",
        "intensity": "string — 心率区间或配速",
        "duration_min": "int — 预计时长",
        "notes": "string — 补充说明"
      }
    ]
  },
  "nutrition_recovery": {
    "daily_calories": "number — 建议每日热量",
    "macros": {"carbs_pct": "number", "protein_pct": "number", "fat_pct": "number"},
    "recovery_tips": ["string — 恢复建议"],
    "sleep_target_hours": "number"
  },
  "data_insights": {
    "training_load_trend": "string — 训练负荷趋势",
    "recovery_status": "string — 恢复状态评估",
    "injury_risk": "low | medium | high",
    "key_correlations": ["string — 数据关联洞察"],
    "recommendations": ["string — 基于数据的建议"]
  },
  "weekly_review_template": "string — 周度复盘模板"
}
```

## 📋 执行步骤

### 阶段一：规划 (Plan) — 设定智慧目标与科学路径

1. **确立核心目标** — 基于跑步哲学（积极生活、内在修行、长期主义、力美融合），设定年度核心目标（如"完成一次全马PB"、"全年健康无伤跑2000公里"）
2. **评估当前状态** — 从运动平台（Strava/Garmin）导出近3个月跑步数据（心率、配速、跑量、HRV、睡眠分数）
3. **AI生成宏观计划** — 使用提示词-01，让AI扮演"顶级跑步教练"，根据年度目标和当前状态生成包含宏观周期（Macrocycle）和中观周期（Mesocycle）的年度训练框架
4. **AI生成微观计划** — 在每个中观周期开始前，使用提示词-02，生成未来4周详细的微观周期（Microcycle）训练计划

**质量检查点**:
- [ ] 训练计划是否包含有氧、无氧、力量、恢复等多种元素的平衡
- [ ] 训练负荷增长是否遵循循序渐进原则（每周跑量增幅≤10%）

### 阶段二：执行 (Do) — 纪律与数据的每日实践

1. **每日训练** — 严格按照周计划执行跑步、力量训练和拉伸
2. **数据自动记录** — 通过智能手表自动记录训练数据（心率、配速、步频、功率等）
3. **营养与恢复** — 遵循计划进行营养补充和睡眠管理

**核心原则**: 一致性高于强度。长期主义的成功在于日复一日的坚持，而非一两次"超常发挥"。

**质量检查点**:
- [ ] 每日训练完成率是否达到90%以上
- [ ] 训练中主观感受（RPE）是否与数据（心率）匹配

### 阶段三：检查 (Check) — AI赋能的深度数据洞察

1. **数据汇总** — 每周将运动平台数据导出为CSV文件
2. **AI数据分析** — 使用提示词-03，让AI扮演"运动数据科学家"，分析周度数据，识别训练负荷（Training Load）、恢复状态（HRV）、睡眠质量与运动表现之间的关联
3. **伤病风险预警** — 关注异常信号（静息心率持续升高、HRV持续下降），作为过度训练或伤病风险预警
4. **撰写复盘报告** — 结合数据分析和主观感受，撰写周度训练复盘

**质量检查点**:
- [ ] 是否识别出上周训练的关键成功点和待改进点
- [ ] AI分析是否揭示了至少一个之前未曾注意到的数据关联

### 阶段四：调整 (Act) — 动态优化与持续迭代

1. **形成调整策略** — 基于复盘洞察，决定下一周期调整方向（增加强度、增加恢复、调整营养）
2. **AI方案优化** — 使用提示词-04，让AI扮演"运动康复师/营养师"，生成具体行动方案（如"增加2组核心力量训练"、"长距离跑后补充20克蛋白质"）
3. **更新计划** — 将调整方案更新到下一周训练计划，启动新一轮PDCA循环

**核心原则**: 训练计划是活的，不是死的。通过快速"检查-调整"循环，让身体始终处于最佳"适应-成长"区间。

**质量检查点**:
- [ ] 调整方案是否直接回应了"检查"阶段发现的问题
- [ ] 下一周期的计划是否已完成更新

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `current_fitness` 数据不完整 | 返回 `WARNING_INCOMPLETE_DATA` + 最低要求数据清单 |
| `race_date` 与当前日期间隔不足 | 根据剩余周数自动压缩训练周期 + 降低目标预期 |
| 数据分析发现过度训练风险 | 返回 `ALERT_OVERTRAINING` + 立即减量方案（降30%跑量） |
| 伤病史涉及关键部位 | 自动调整训练类型规避 + 建议专业运动医学评估 |
| HRV持续低于个人基线 | 标记恢复不足 + 增加休息日 + 睡眠优化建议 |
| 静息心率持续升高 | 降量20%-30% + 增加睡眠时长 + 检查营养摄入 |
| 训练主观感受与数据严重不匹配 | 暂停高强度训练 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
