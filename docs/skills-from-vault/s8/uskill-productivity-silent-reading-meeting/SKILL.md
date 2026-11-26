---
name: uskill-productivity-silent-reading-meeting
description: "让productivity silent reading meeting变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-silent-reading-meeting.md"
  original_id: "SKL-6911"
  version: "3.0.0"
  trust: untrusted
---

# productivity silent reading meeting

# Efficient Silent Reading Meeting (Flying Reading Meeting)

## 🎯 目标
> 运用字节跳动「飞阅会」方法论，将传统低效会议改造为文档驱动的高效协作模式。通过"会前写文档 → 会中默读讨论 → 会后跟待办"的标准化流程，将会议效率提升 50% 以上，彻底告别"会而不议、议而不决、决而不行"的会议顽疾。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `meeting_topic` | string | ✅ | 会议主题 |
| `participants` | array | ✅ | 参会人员列表及角色（主持人、决策者、参与者） |
| `agenda_items` | array | ✅ | 议题列表，每项包含：标题、背景信息、期望结论、预估时长 |
| `meeting_duration` | int | ✅ | 会议总时长（分钟），推荐 30min |
| `decision_needed` | boolean | ❌ | 是否需要产出明确决策，默认 true |
| `meeting_doc_template` | string | ❌ | 会议文档模板链接，默认使用标准模板 |
| `collaboration_tool` | string | ❌ | 协作工具：`feishu` / `notion` / `google_docs` / `local_markdown`，默认 feishu |

## 📤 输出

```json
{
  "meeting_doc": {
    "title": "string — 会议文档标题",
    "doc_url": "string — 文档链接（在线协作时）",
    "content_markdown": "string — 完整会议文档 Markdown",
    "structure": {
      "agenda_section": "string — 议题列表与背景",
      "discussion_space": "string — 每个议题的讨论记录区",
      "decision_section": "string — 结论与决策记录区",
      "action_items": "string — 待办事项区"
    }
  },
  "meeting_plan": {
    "preparation_phase": {
      "time": "string — 如 '09:50-10:00'",
      "tasks": ["string — 准备阶段任务清单"],
      "responsible": "string — 负责人"
    },
    "silent_reading_phase": {
      "time": "string — 如 '10:00-10:05'",
      "duration_minutes": "int — 默读时长",
      "instructions": "string — 默读指引（评论疑问、标注建议）"
    },
    "discussion_phase": {
      "time": "string — 如 '10:05-10:25'",
      "agenda_order": ["string — 按序讨论的议题"],
      "discussion_rules": ["string — 讨论规则"]
    },
    "closing_phase": {
      "time": "string — 如 '10:25-10:30'",
      "tasks": ["string — 收尾任务（总结结论、分配待办）"]
    },
    "followup_phase": {
      "time": "string — 如 '10:30-11:00'",
      "tasks": ["string — 会后跟进任务"]
    }
  },
  "action_items": [
    {
      "task": "string — 待办内容",
      "owner": "string — 负责人",
      "due_date": "string — 截止日期",
      "priority": "string — high / medium / low"
    }
  ],
  "efficiency_metrics": {
    "estimated_time_saved": "string — 相比传统会议预估节省时间",
    "pre_read_ratio": "string — 文档提前阅读率",
    "decision_clarity_score": "string — 决策清晰度评分"
  }
}
```

## 📋 执行步骤

### Phase 0: 会前准备（会前 10 分钟）
1. **创建会议文档** — 按标准模板创建文档，包含：标题、参会人、日期、议题列表
2. **撰写议题内容** — 每个议题包含：背景信息、关键数据/链接、预估时长、期望结论
3. **预设讨论空间** — 为每个议题预留评论区和结论记录区
4. **@相关人员** — 在文档中 @ 对应议题的负责人，确保信息触达
5. **调整权限** — 设置文档编辑/评论权限

### Phase 1: 默读文档（5 分钟）
6. **主持人发起会议** — 开启视频会议，屏幕共享会议文档
7. **约定默读时间** — 根据文档长度约定默读时长（通常 3-5 分钟）
8. **自由阅读模式** — 参会者各自阅读，将疑问和建议以**评论**形式发布在文档对应位置
9. **使用倒计时** — 设置文档倒计时功能，时间到自动提醒

### Phase 2: 穿屏讨论（20 分钟）
10. **依序主持** — 主持人按议题顺序逐项推进讨论
11. **聚焦评论** — 优先讨论文档中参会者留下的评论和疑问
12. **实时记录** — 在文档中实时记录讨论要点和结论
13. **穿屏互动** — 参会者可直接修改共享文档内容（如同在白板上书写）
14. **控制节奏** — 超时议题标记"待续"，移入下次会议

### Phase 3: 明确结论与分配待办（5 分钟）
15. **总结会议结论** — 主持人在文档末尾汇总本次会议的关键决策
16. **记录待办事项** — 每项待办包含：具体内容、负责人、截止日期
17. **认领与确认** — 各负责人当面确认任务量和时间承诺
18. **散会** — 结论和待办明确后立即散会

### Phase 4: 会后跟进（会后 30 分钟内）
19. **完善文档** — 主持人补充和整理会议记录
20. **分享文档** — 将文档分享至会议群组，让未参会者也能了解要点
21. **进度同步** — 各负责人在文档中同步待办进展，形成闭环跟踪

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 参会者未提前阅读文档 | 主持人延长默读时间至 8 分钟，或标注"跳过预读议题" |
| 讨论严重超时 | 主持人中断讨论，标记为"待深度讨论"，安排专题会议 |
| 参会者无法实时编辑文档 | 降级为"口头讨论 + 主持人记录"模式 |
| 议题过多无法在时限内完成 | 按优先级排序，低优先级议题移入下次会议 |
| 会后文档未及时完善 | 设置 30 分钟提醒，主持人完成归档 |
| 待办事项无人认领 | 主持人指定负责人，被指定人 24h 内确认或拒绝 |

## ✅ 自检清单

- [ ] 会议文档是否在会前 10 分钟发送给所有参会者？
- [ ] 每个议题是否包含充分的背景信息和期望结论？
- [ ] 默读阶段是否有明确的时间控制？
- [ ] 讨论是否聚焦于文档中的评论和疑问，而非漫谈？
- [ ] 每个议题是否都记录了明确的结论？
- [ ] 待办事项是否都有明确的负责人和截止日期？
- [ ] 会议是否在时限内准时结束？
- [ ] 会后文档是否已完善并分享至相关群组？
- [ ] 相比传统会议，是否节省了 50% 以上的时间？


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
- [ ] 方案

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
