---
name: uskill-agent-meta-personal-okr-goal-management
description: "让meta personal okr goal management变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-personal-okr-goal-management.md"
  original_id: "SKL-5052"
  version: "3.0.0"
  trust: untrusted
---

# meta personal okr goal management

# Personal OKR Goal Management

## 🎯 目标
> AI赋能的个人战略目标管理系统：基于OKR框架，通过「设定→对齐执行→检视跟进→复盘重置」四步循环，将年度愿景转化为可衡量的季度行动，驱动个人能力指数级成长。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `phase` | enum | ✅ | 执行阶段：`set` / `align` / `checkin` / `reflect` |
| `annual_vision` | string | ✅ | 年度愿景描述，如 `"AI-Led Evolution"` |
| `strategic_pillars` | array | ✅ | 四大战略支柱：`["智慧学习", "效率倍增", "身心赋能", "沟通精进"]` |
| `quarter` | string | ✅ | 当前季度，如 `"2026-Q2"` |
| `existing_okrs` | array | ❌ | 已设定的OKR列表（checkin/reflect阶段必填） |
| `weekly_data` | object | ❌ | 周度进展数据 `{kr_progress: [], confidence: [], blockers: []}` |
| `focus_area` | string | ❌ | 本季度战略重心，如 `"提升AI产品的商业化能力"` |
| `review_week` | number | ❌ | 当前是季度第几周（checkin阶段用） |

## 📤 输出

```json
{
  "phase": "set | align | checkin | reflect",
  "quarter": "string",
  "objectives": [
    {
      "id": "O1",
      "description": "string — 定性的、鼓舞人心的季度目标",
      "aligned_pillar": "string — 对齐的战略支柱",
      "key_results": [
        {
          "id": "KR1.1",
          "description": "string — 可量化的关键结果",
          "target_value": "number",
          "current_value": "number",
          "unit": "string",
          "confidence": "number (1-10)",
          "progress_pct": "number (0-100)",
          "status": "on_track | at_risk | behind"
        }
      ],
      "overall_score": "number (0.0-1.0)"
    }
  ],
  "aligned_tasks": [
    {
      "kr_id": "string",
      "weekly_tasks": ["string"],
      "daily_actions": ["string"],
      "resources_needed": ["string"]
    }
  ],
  "checkin_report": {
    "week_number": "number",
    "kr_updates": [
      {
        "kr_id": "string",
        "progress_pct": "number",
        "confidence": "number (1-10)",
        "blockers": ["string"],
        "ai_suggestions": ["string"]
      }
    ],
    "top3_weekly_tasks_aligned": "boolean",
    "data_evidence": ["string"]
  },
  "reflect_report": {
    "final_scores": [
      {
        "kr_id": "string",
        "final_score": "number (0.0-1.0)",
        "achievement": "string"
      }
    ],
    "highlights": ["string"],
    "failures": ["string"],
    "root_causes": ["string"],
    "core_lessons": ["string"],
    "next_quarter_inputs": ["string"]
  },
  "quality_checks": {
    "pillar_alignment": "boolean",
    "kr_measurable": "boolean",
    "challenge_level": "string — ideal | too_easy | too_hard",
    "weekly_review_complete": "boolean"
  }
}
```

## 📋 执行步骤

### Step 1: 设定 (Set) — 定义高价值季度OKR
1. **对齐年度愿景** — 回顾年度成果导航和四大战略支柱，明确本季度战略重心
2. **AI头脑风暴目标** — 使用 **Prompt-01**，让AI扮演"战略顾问"，基于年度愿景生成3-5个鼓舞人心的季度目标（O）
   - O是定性的、有方向的，如："在AI投资领域建立初步的技术优势和盈利模型"
3. **选择与精炼O** — 运用投资人战略眼光，选择2-3个最具"非对称回报"价值的目标
4. **拆解关键结果** — 使用 **Prompt-02**，让AI扮演"OKR专家"，将每个O拆解为3-5个可量化的KR
   - 好的KR在期末完成度应在70%-80%，100%说明不够有挑战
   - KR必须是结果导向的定量指标，如："将投资AI策略回测年化收益率提升到25%"

### Step 2: 对齐与执行 (Align & Execute)
1. **任务分解** — 将每个KR分解为周度和日度任务，录入任务管理工具
2. **资源对齐** — 评估完成OKR所需的时间、金钱、外部协助并进行规划
3. **日常执行** — 聚焦每日/每周任务，确保行动与目标对齐
   - 验证：本周Top 3任务是否直接或间接推动某个KR？

### Step 3: 检视与跟进 (Check-in & Track)
1. **周度检视（每周五）** — 更新KR进度（0-100%）、信心指数（1-10分）、识别障碍（Blocker）
2. **数据驱动评估** — 结合个人数据分析结果，为KR进展提供客观数据支撑
3. **AI辅助分析** — 使用 **Prompt-03**，让AI扮演"效能教练"，分析进度偏差并提出移除障碍的建议

### Step 4: 复盘与重置 (Reflect & Reset)
1. **季度末复盘** — KR最终打分（0.7-0.8为理想），定性评估O达成程度
2. **深度反思** — 使用 **Prompt-04**，让AI扮演"复盘专家"，覆盖成就、失败、根本原因、经验沉淀
3. **庆祝与沉淀** — 庆祝成就，将经验教训沉淀到第二大脑知识系统
4. **启动新周期** — 将复盘洞察作为下一季度OKR设定的输入

## 🤖 AI Prompt 模板

### Prompt-01: 目标头脑风暴
```
你是一位顶级的个人战略顾问，深刻理解我的年度四大战略支柱（智慧学习、效率倍增、身心赋能、沟通精进）。基于我的年度愿景"[粘贴年度愿景]"和本季度的战略重心"[如：提升AI产品的商业化能力]"，请为我头脑风暴3-5个鼓舞人心的、定性的季度目标（Objectives）。
```

### Prompt-02: KR拆解
```
你是一位OKR设定专家。我的季度目标(O)是："[粘贴一个Objective]"。请你引导我，通过提问的方式，帮助我设定3-5个衡量这个O是否达成的关键结果（KR）。请确保每个KR都符合SMART原则，特别是可量化和结果导向。请逐一提出建议并等待我的确认。
```

### Prompt-03: 周度检视辅助
```
你是一位敏锐的效能教练。我正在进行周度OKR检视。我的一个关键结果（KR）是"[KR描述]"，目标是[目标值]，目前进度是[当前值]。我的信心指数是[1-10分]，因为我遇到了障碍："[障碍描述]"。请帮我分析这个障碍的可能原因，并提出2-3个具体的、可操作的建议来帮助我移除它。
```

### Prompt-04: 季度复盘引导
```
你是一位经验丰富的复盘引导师。我的一个季度OKR刚刚结束，目标（O）是"[O描述]"，关键结果（KR）的最终得分如下：[列出KR及

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
