---
name: uskill-agent-meta-personal-data-okr-review
description: "让meta personal data okr review变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-personal-data-okr-review.md"
  original_id: "SKL-5030"
  version: "3.0.0"
  trust: untrusted
---

# meta personal data okr review

# Personal Data-Driven OKR Review

## 🎯 目标
> AI赋能的月度战略复盘：系统化聚合、分析个人全维度数据，与四大战略支柱对齐，生成可执行的优化行动计划，实现数据驱动的自我进化。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `review_period` | string | ✅ | 复盘周期，如 `"2026-04"` |
| `okr_targets` | object | ✅ | `{body: [], learning: [], productivity: [], finance: []}` — 四大支柱的OKR目标 |
| `data_sources` | object | ✅ | `{strava: [], garmin: [], toggl: [], obsidian: [], finance_app: [], ...}` — 各平台导出数据 |
| `focus_areas` | array | ❌ | 本次复盘重点关注的支柱，如 `["body", "productivity"]` |
| `review_depth` | enum | ❌ | `quick`（30分钟）/ `standard`（1小时）/ `deep`（2小时），默认 `standard` |
| `dashboard_state` | object | ❌ | `{last_month_scores: {}, trend_data: {}}` — 上月仪表盘状态 |

## 📤 输出

```json
{
  "pillar_scores": {
    "body": {
      "score": "number (0-100)",
      "trend": "up | flat | down",
      "key_metrics": [{"metric": "string", "value": "number", "target": "number", "achievement_pct": "number"}],
      "summary": "string"
    },
    "learning": { "/* same structure */": "" },
    "productivity": { "/* same structure */": "" },
    "finance": { "/* same structure */": "" }
  },
  "overall_score": "number (0-100)",
  "correlation_insights": [
    {"variables": ["string", "string"], "relationship": "positive | negative", "strength": "strong | moderate | weak", "insight": "string"}
  ],
  "root_cause_analysis": [
    {"unmet_goal": "string", "root_cause": "string", "evidence": "string", "framework": "string"}
  ],
  "core_insights": [
    {"insight": "string", "actionability": "high | medium | low", "priority": "number"}
  ],
  "action_plan": [
    {
      "experiment": "string — 改进实验名称",
      "hypothesis": "string — 实验假设",
      "daily_actions": ["string — 每日执行动作"],
      "success_metric": "string — 成功指标",
      "success_threshold": "string — 达标阈值",
      "duration": "string — 实验周期",
      "pillar": "body | learning | productivity | finance"
    }
  ],
  "dashboard_update": {
    "new_kpis": [{"metric": "string", "target": "number", "pillar": "string"}],
    "retired_kpis": ["string"],
    "adjusted_long_term_goals": [{"goal": "string", "old_target": "string", "new_target": "string", "reason": "string"}]
  },
  "monthly_report_md": "string — Markdown格式的完整月度复盘报告"
}
```

## 📋 执行步骤

### Step 1: 数据聚合与清洗
1. **收集四大支柱数据** — 从各平台导出上一周期数据
   - 身心赋能：Strava/Garmin跑步数据、智能手表睡眠/HRV数据
   - 智慧学习：Obsidian笔记增长数、阅读App读书时长/数量
   - 效率倍增：Toggl/RescueTime时间追踪、任务管理工具已完成任务数
   - 沟通精进：财务App投资收益、社交媒体互动数据
2. **数据清洗** — 合并CSV文件，处理缺失值和异常值
3. **完整性校验** — 确保四大支柱核心数据均已覆盖

### Step 2: 战略支柱对齐分析
1. **计算核心指标** — 针对每个支柱计算本周期量化指标
2. **与OKR对比** — 将指标与月度/季度OKR目标对比，计算达成率
3. **趋势分析** — 结合 `dashboard_state` 计算环比变化趋势
4. **可视化呈现** — 生成趋势图、瀑布图，更新仪表盘

### Step 3: AI辅助洞察与根本原因分析
1. **AI关联分析** — 让AI扮演"数据科学家"，将清洗后数据喂入，寻找隐藏关联
   - 示例：睡眠质量与次日深度工作时长的关系
   - 示例：跑量增加与投资决策冷静度的关系
2. **根本原因分析** — 对"未达标"指标，运用行为心理学进行根因分析
   - 示例：深度工作时长未达标 → AI发现下午效率低 → 可能是"决策疲劳"或"午后血糖波动"
3. **AI洞察提炼** — 让AI扮演"行为分析师"，提炼2-3条核心洞察

### Step 4: 生成洞察与行动计划
1. **总结核心洞察** — 提炼3-5条最核心、可行动的洞察
2. **设计改进"实验"** — 针对每条洞察设计小规模改进实验
3. **AI辅助生成计划** — 让AI扮演"个人效能教练"，转化为结构化行动计划
   - 遵循SMART原则
   - 为每个实验设定明确的成功/失败判断标准

### Step 5: 更新仪表盘与目标
1. **撰写复盘报告** — 汇总所有内容形成《月度个人OKR与数据复盘报告》
2. **更新仪表盘** — 将下月行动计划和关键指标更新到仪表盘
3. **调整长期目标** — 如连续多周期显示某目标不合理，进行战略性调整

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 某支柱数据完全缺失 | 返回 `WARNING_MISSING_PILLAR` + 该支柱标记为"数据不足"，不纳入评分 |
| 数据出现异常极值（如单日跑量100km） | 标记 `FLAG_OUTLIER` + 要求用户确认是否为录入错误 |
| `okr_targets` 未设定 | 返回 `ERROR_NO_OKR` + 要求至少设定每个支柱1个核心指标 |
| 所有支柱达标率>95% | 提示 `INFO_TARGETS_TOO_EASY` + 建议提高下月挑战度 |
| AI关联分析未发现显著关联 | 返回 `INFO_NO_CORRELATION` + 建议延长数据收集周期或增加数据维度 |
| `review_period` 跨度>2个月 | 提示 `WARNING_LONG_GAP` + 建议分段分析 |

## ✅ 自检清单

- [ ] 四大支柱的核心数据是否都已收集完毕？
- [ ] 数据是否存在明显的错误或遗漏？
- [ ] 每个战略支柱是否至少有1-2个核心指标进行追踪？
- [ ] 指标的达成情况是否一目了然？
- [ ] 是否对每个关键指标的波动都提出了至少一个根本原因假设？
- [ ] AI是否发现了至少一个未曾预料到的数据关联？
- [ ] 每个行动计划是否都遵循了SMART原则？
- [ ] 是否为每个"实验"都设定了明确的成功或失败判断标准？
- [ ] 复盘报告是否已归档，便于未来回顾？
- [ ] 下月核心指标和行动项是否已清晰展示在仪表盘上？


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
