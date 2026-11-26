---
name: uskill-agent-meta-design-learning-plan
description: "让meta design learning plan变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-design-learning-plan.md"
  original_id: "SKL-5009"
  version: "3.0.0"
  trust: untrusted
---

# meta design learning plan

# Design Personalized Learning Plan

## 🎯 目标
> 以战略目标为导向，AI全面赋能的闭环学习系统——高效获取、深度内化、并最终应用新知识，将新领域的入门到产出时间缩短50%，实现知识复利。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `learning_goal` | string | ✅ | 学习目标描述，如"3个月内掌握Rust并完成一个CLI工具" |
| `current_level` | enum | ✅ | `beginner` / `intermediate` / `advanced` |
| `time_budget_hours_weekly` | int | ✅ | 每周可投入的学习时间（小时） |
| `duration_weeks` | int | ❌ | 学习周期（周），默认 4 |
| `learning_style` | enum | ❌ | `reading` / `video` / `hands-on` / `mixed`，默认 `mixed` |
| `output_format` | enum | ❌ | `blog` / `project` / `presentation` / `all`，默认 `all` |
| `related_okr` | string | ❌ | 关联的OKR或战略目标 |

## 📤 输出

```json
{
  "learning_plan": {
    "smart_goal": "string — SMART格式的学习目标",
    "total_weeks": "int — 总学习周数",
    "weekly_schedule": [
      {
        "week": "int",
        "theme": "string — 本周学习主题",
        "modules": ["string — 学习模块"],
        "practice_ratio": "number — 实践占比(0-1)",
        "milestone": "string — 本周里程碑",
        "hours_planned": "number — 计划学时"
      }
    ]
  },
  "resources": {
    "books": [{"title": "string", "author": "string", "priority": "must-read | recommended"}],
    "courses": [{"name": "string", "platform": "string", "url": "string"}],
    "papers": [{"title": "string", "relevance": "string"}],
    "projects": [{"name": "string", "difficulty": "easy | medium | hard", "description": "string"}]
  },
  "knowledge_base": {
    "personal-knowledge-vault_structure": "string — 建议的Obsidian目录结构",
    "key_concepts": ["string — 核心概念清单"],
    "link_map": "string — 知识关联图谱（Mermaid）"
  },
  "practice_projects": [
    {
      "name": "string",
      "description": "string",
      "tech_stack": ["string"],
      "expected_outcome": "string",
      "difficulty": "easy | medium | hard"
    }
  ],
  "assessment": {
    "quiz_template": "string — 自我测验模板",
    "target_score": "number — 目标正确率(%)",
    "review_schedule": ["string — 复习时间点"]
  }
}
```

## 📋 执行步骤

1. **对齐目标（Align）** — 将学习意图与长期战略目标/OKR对齐，转化为SMART目标（具体、可衡量、可实现、相关、有时限），生成结构化课程大纲
2. **获取知识（Acquire）** — 策展"最小知识集合"：必读书籍、核心论文、在线课程、开源项目，对复杂内容进行AI辅助摘要与解读，保持苏格拉底式追问深化理解
3. **内化与应用（Assimilate & Apply）** — 将新知识重构为原子化笔记并链入Obsidian知识网络，设计微型实践项目（Side Project），用费曼学习法输出（技术博客/内部分享）
4. **评估与迭代（Assess & Adjust）** — AI生成自我测验（选择题+简答+场景题），评估SMART目标完成度，复盘学习效率与障碍，调整下一阶段计划

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `learning_goal` 过于模糊 | 返回澄清问题清单：目标用户、预期输出、应用场景、衡量标准 |
| `time_budget_hours_weekly` < 3 | 返回 `WARNING_INSUFFICIENT_TIME` + 建议延长周期或精简目标 |
| 资源推荐无免费替代 | 标记付费资源 + 提供免费替代方案 |
| 测验正确率 < 60% | 建议返回"获取知识"阶段补充基础 + 调整学习路径 |
| 学习进度严重滞后 | 自动调整后续计划密度 + 建议砍低优先级模块 |

## ✅ 自检清单

- [ ] 学习目标符合SMART原则
- [ ] 周计划包含理论与实践的合理比例（建议6:4）
- [ ] 资源清单包含至少2本必读书籍和1个实践项目
- [ ] Obsidian笔记结构已规划，支持双向链接
- [ ] 至少设计1个可交付的实践产出（博客/代码/分享）
- [ ] 包含自我测验模板和复习时间表
- [ ] 学习计划与相关OKR/战略目标明确关联


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-09 转化 |

---
**相关笔记**：[[战略 OKR 管理]] [[uSkill-agent-长寿逃逸速度人生规划]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [学习任务] for [知识背景], with [学习目标], leaning toward [学习方法/输出形式]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

#

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
