---
name: uskill-agent-meta-strategic-okr-management
description: "让meta strategic okr management变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-strategic-okr-management.md"
  original_id: "SKL-5024"
  version: "3.0.0"
  trust: untrusted
---

# meta strategic okr management

# Strategic OKR Goal Management

> AI赋能的个人战略目标管理系统——基于OKR框架的季度规划、周度检视与复盘闭环。

## 🎯 目标

> 建立一套基于OKR（Objectives and Key Results）框架、由AI全面赋能的个人目标设定、追踪与复盘系统，确保个人精力聚焦于最高价值事务。本技能是个人战略的"总指挥室"与"导航仪"，将年度愿景转化为可衡量的季度行动，驱动个人能力的指数级成长。

**核心适用场景**：
1. **季度目标设定** — 结合年度愿景，设定3个具有挑战性且可衡量的OKR
2. **周度进度检视** — 每周五客观评估KR进展，识别障碍
3. **战略方向调整** — 当季度目标不再契合当前需求时进行校准

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `annual_vision` | string | ✅ | 年度愿景描述，包含四大战略支柱方向 |
| `strategic_focus` | string | ✅ | 本季度战略重心（如"提升AI产品的商业化能力"） |
| `existing_okrs` | object[] | ❌ | 上季度OKR及完成情况（用于延续性分析） |
| `data_review` | object | ❌ | 来自SOP-18的个人数据分析结果 |
| `knowledge_assets` | string[] | ❌ | 相关知识资产链接（来自SOP-21第二大脑） |

**数据来源约定**：
- 年度愿景：`🎯 我的2025成果导航` 文档
- 数据支撑：SOP-18（AI驱动的个人数据复盘）
- 经验沉淀：SOP-21（第二大脑知识管理系统）
- 效率基线：SOP-23（效率分析）

## 📤 输出

```json
{
  "quarterly_okr_document": {
    "quarter": "Q2-2026",
    "objectives": [
      {
        "id": "O-1",
        "description": "定性的、鼓舞人心的目标描述",
        "aligned_pillars": ["智慧学习", "效率倍增"],
        "key_results": [
          {
            "id": "KR-1.1",
            "description": "可量化的关键结果描述",
            "target_value": "目标值",
            "current_value": "当前值",
            "progress_pct": 0,
            "confidence_score": 8
          }
        ]
      }
    ]
  },
  "weekly_checkin": {
    "week": "W19",
    "date": "2026-05-09",
    "kr_progress": [
      {
        "kr_id": "KR-1.1",
        "progress_pct": 35,
        "confidence_score": 7,
        "blockers": ["障碍描述"],
        "ai_suggestions": ["建议1", "建议2"]
      }
    ]
  },
  "quarterly_review": {
    "quarter": "Q1-2026",
    "objective_scores": [
      {
        "o_id": "O-1",
        "achievement_level": "定性评估",
        "kr_scores": [
          { "kr_id": "KR-1.1", "final_score": 0.75 }
        ]
      }
    ],
    "highlights": ["成就与亮点"],
    "lowlights": ["失败与不足"],
    "root_causes": ["根本原因分析"],
    "lessons_learned": ["核心经验沉淀"]
  }
}
```

## 📋 执行步骤

### Phase 1: 设定 (Set) — 定义高价值、挑战性的季度OKR

1. **对齐年度愿景**
   - 回顾年度愿景文档和四大战略支柱（智慧学习、效率倍增、身心赋能、沟通精进）
   - 明确本季度的战略重心

2. **AI辅助目标头脑风暴**
   - 使用提示词模板进行目标（Objectives）头脑风暴：
     > 你是一位顶级的个人战略顾问，深刻理解我的年度四大战略支柱。基于我的年度愿景"[粘贴愿景]"和本季度战略重心"[战略重心]"，请为我头脑风暴3-5个鼓舞人心的、定性的季度目标（Objectives）。
   - AI扮演"战略顾问"角色，输出3-5个候选目标

3. **选择与精炼目标 (O)**
   - 运用战略眼光，从中选择2-3个最具"非对称回报"价值的目标
   - 确保每个O与至少一个战略支柱直接对齐
   - O应为定性的、有方向的，而非量化指标

4. **拆解关键结果 (KR)**
   - 针对每个O，使用提示词模板拆解KR：
     > 你是一位OKR设定专家。我的季度目标(O)是："[粘贴Objective]"。请你引导我，通过提问的方式，帮助我设定3-5个衡量这个O是否达成的关键结果（KR）。请确保每个KR都符合SMART原则，特别是可量化和结果导向。
   - 每个O下设定3-5个KR
   - KR必须是定量的、结果导向的，而非过程性任务

5. **质量检查**
   - [ ] 每个O是否与至少一个战略支柱直接对齐？
   - [ ] 每个KR是否可量化、结果导向（非任务列表）？
   - [ ] KR的理想期末完成度是否在70%-80%？（100%说明不够挑战）

### Phase 2: 对齐与执行 (Align & Execute)

6. **任务分解**
   - 将每个KR分解为具体的周度和日度任务
   - 录入任务管理工具（Todoist/Trello/Notion）

7. **资源对齐**
   - 评估完成OKR所需资源（时间、金钱、外部协助）
   - 进行资源规划与分配

8. **日常执行**
   - 聚焦完成每日/每周任务
   - 确保行动与目标持续对齐

9. **质量检查**
   - [ ] 本周Top 3任务是否直接或间接推动某个KR的进展？

### Phase 3: 检视与跟进 (Check-in & Track)

10. **每周五进行周度检视**
    - 更新KR进度（0-100%）
    - 更新信心指数（1-10分）
    - 记录阻碍KR进展的主要问题（Blocker）

11. **数据驱动评估**
    - 结合SOP-18的个人数据分析结果
    - 为KR进展提供客观数据支撑

12. **AI辅助偏差分析**
    - 使用提示词模板进行障碍分析：
      > 你是一位敏锐的效能教练。我正在进行周度OKR检视。我的一个关键结果（KR）是"[KR描述]"，目标是[目标值]，目前进度是[当前值]。我的信心指数是[1-10分]，因为我遇到了障碍："[障碍描述]"。请帮我分析这个障碍的可能原因，并提出2-3个具体的、可操作的建议来帮助我移除它。

13. **质量检查**
    - [ ] 每个KR的进度是否有客观数据支撑？
    - [ ] 信心指数低于5的KR是否已识别障碍并有初步应对想法？

### Phase 4: 复盘与重置 (Reflect & Reset)

14. **季度末KR最终打分**
    - 为每个KR打出最终分数（0.7-0.8为理想区间）
    - 根据KR完成情况定性评估O的达成程度

15. **AI引导深度反思**
    - 使用提示词模板进行复盘引导：
      > 你是一位经验丰富的复盘引导师。我的一个季度OKR刚刚结束，目标（O）是"[O描述]"，关键结果（KR）的最终得分如下：[列出KR及最终得分]。请你通过一系列深刻的问题，引导我进行一次全面的季度复盘。问题请覆盖"成就与亮点"、"失败与不足"、"根本原因分析"和"核心经验沉淀"四个方面。

16. **经验沉淀与庆祝**
    - 庆祝本季度取得的成就
    - 将关键经验教训沉淀到SOP-21第二大脑系统

17. **启动新周期**
    - 将本次复盘洞察作为下一季度OKR设定的重要输入
    - 启动新一轮"设定"流程

18. **质量检查**
    - [ ] 是否为每个未完成的KR找到根本原因？
    - [ ] 是否总结出至少1-2条指导下季度工作的核心经验？

## ⚠️ 异常处理

| 异常场景 | 处理方式 |
|----------|----------|
| OKR设定过多（>3个O或每个O下>5个KR） |

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
