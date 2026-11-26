---
name: uskill-cognition-cognitive-strategic-learning-plan
description: "让cognitive strategic learning plan变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-strategic-learning-plan.md"
  original_id: "SKL-6828"
  version: "3.0.0"
  trust: untrusted
---

# cognitive strategic learning plan

# AI-Driven Strategic Learning Plan

## 🎯 目标
> 建立以战略目标为导向、AI 全面赋能的 4A 闭环学习系统，高效获取、深度内化并应用新知识，将新领域入门到产出时间缩短 50%，实现知识复利。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `learning_goal` | string | ✅ | SMART 学习目标，如"3 个月内掌握 Rust 并独立完成一个 CLI 工具" |
| `current_level` | enum | ✅ | `beginner` / `intermediate` / `advanced` — 当前知识水平 |
| `time_budget_hours_weekly` | int | ✅ | 每周可投入学习时间（小时） |
| `duration_weeks` | int | ❌ | 学习周期（周），默认 4 |
| `preferred_format` | enum | ❌ | `reading` / `video` / `hands_on` / `mixed`，默认 `mixed` |
| `output_type` | enum | ❌ | `blog` / `side_project` / `presentation` / `sop` — 知识内化产出形式，默认 `blog` |
| `context` | object | ❌ | `{related_okr: "string", existing_skills: ["string"], motivation: "string"}` — 学习背景 |

## 📤 输出

```json
{
  "learning_plan": {
    "smart_goal": "string — 结构化 SMART 目标",
    "alignment_with_okr": "string — 与个人 OKR 的关联说明",
    "weekly_schedule": [
      {
        "week": "int",
        "theme": "string",
        "topics": ["string"],
        "theory_hours": "number",
        "practice_hours": "number",
        "milestone": "string",
        "deliverable": "string"
      }
    ],
    "theory_practice_ratio": "string — 如 '6:4'"
  },
  "resource_collection": {
    "essential_books": [
      {"title": "string", "author": "string", "reason": "string", "priority": "must_read | recommended"}
    ],
    "papers_reports": [
      {"title": "string", "source": "string", "reason": "string"}
    ],
    "courses": [
      {"name": "string", "platform": "string", "duration": "string", "reason": "string"}
    ],
    "open_source_projects": [
      {"name": "string", "url": "string", "difficulty": "easy | medium | hard", "reason": "string"}
    ],
    "minimal_knowledge_set": "string — 最小知识集合摘要"
  },
  "active_learning": {
    "socratic_questions": [
      {"topic": "string", "questions": ["string — 启发性问题"]}
    ],
    "concept_map": "string — Mermaid 概念关系图",
    "misconceptions_to_watch": ["string — 常见误区"]
  },
  "assimilation_project": {
    "project_name": "string",
    "description": "string",
    "core_features": ["string"],
    "tech_stack": ["string"],
    "difficulty": "easy | medium | hard",
    "estimated_hours": "int",
    "learning_outcomes": ["string"]
  },
  "knowledge_output": {
    "type": "blog | side_project | presentation | sop",
    "outline": ["string — 文章/分享大纲"],
    "target_audience": "string",
    "key_insights_to_convey": ["string"]
  },
  "assessment": {
    "quiz": {
      "multiple_choice": [{"question": "string", "options": ["string"], "answer": "string", "explanation": "string"}],
      "short_answer": [{"question": "string", "reference_answer": "string"}],
      "scenario": [{"scenario": "string", "expected_approach": "string"}]
    },
    "pass_threshold_pct": 90,
    "weakness_analysis_template": "string"
  },
  "retrospective": {
    "sprint_review_questions": ["string"],
    "adjustment_actions": ["string"],
    "next_sprint_suggestions": ["string"]
  }
}
```

## 📋 执行步骤

### Phase 1: 对齐目标 (Align)
1. **明确学习意图** — 分析 `learning_goal` 与 `context.related_okr` 的关联，确保学习是战略投资而非随机探索，输出 SMART 目标结构化文档
2. **AI 辅助课程设计** — 根据 SMART 目标和 `current_level`，生成个性化学习大纲，包含每周主题、理论/实践比例、关键里程碑

### Phase 2: 获取知识 (Acquire)
3. **AI 辅助资源策展** — 为每个学习模块推荐"最小知识集合"：2 本圣经级书籍、3 篇核心论文、1-2 门在线课程、2-3 个开源项目
4. **苏格拉底式深度学习** — 对每个核心概念生成 5 个启发性问题，通过追问和诘难深化理解，而非被动接收
5. **概念图谱构建** — 生成 Mermaid 格式的概念关系图，标注知识节点间的依赖和联系

### Phase 3: 内化与应用 (Assimilate & Apply)
6. **结构化笔记沉淀** — 将新知识重构为原子化笔记，建立双向链接，链入 Obsidian 知识网络
7. **实践项目驱动** — 根据学习内容构思 1 个微型 Side Project，将理论转化为可交付的代码/产品
8. **费曼学习法输出** — 按 `output_type` 生成知识产出大纲（技术博客/项目文档/内部分享/SOP），确保能向他人清晰解释所学

### Phase 4: 评估与迭代 (Assess & Adjust)
9. **AI 生成自测卷** — 生成包含选择题、简答题、场景应用题的自测卷，含详细答案和解析
10. **复盘与调整** — 分析学习效率、障碍和成功经验，输出 Sprint 回顾报告和下一阶段调整建议

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `learning_goal` 过于模糊（如"学 AI"） | 返回 `ERROR_GOAL_TOO_VAGUE` + SMART 改写建议 |
| `time_budget_hours_weekly` < 3 | 返回 `WARNING_INSUFFICIENT_TIME` + 精简版学习计划（仅核心 20%） |
| `current_level` 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
