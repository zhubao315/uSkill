# Flyreading Meeting Methodology (飞阅会)

> A highly efficient meeting format pioneered by ByteDance, combining real-time video conferencing with collaborative cloud documents. The core idea: **read first, discuss second** — replace oral status updates with silent reading, then focus discussion only on questions and decisions.

## 🎯 目标

1. **Eliminate meeting inefficiency** — no more round-robin verbal updates or one-person presentations.
2. **Maximize preparation quality** — all context lives in a shared document before the meeting starts.
3. **Enable structured, time-boxed discussion** — silent reading compresses information transfer; focused Q&A drives decisions.
4. **Produce actionable outcomes** — every meeting ends with documented decisions, owners, and deadlines.
5. **Create institutional memory** — the meeting document becomes the single source of truth for what was discussed and decided.

## 📥 输入

| Parameter | Type | Required | Description |
|---|---|---|---|
| `meeting_topic` | string | ✅ | Overall meeting title or theme |
| `topics` | list[string] | ✅ | List of agenda items / discussion topics |
| `topic_estimates` | list[int] | ✅ | Estimated minutes per topic (parallel array to `topics`) |
| `participants` | list[string] | ✅ | Participant names or handles |
| `document_platform` | string | ❌ | `"feishu"` / `"lark"` / `"google_docs"` / `"notion"` / `"confluence"` (default: `"feishu"`) |
| `meeting_duration` | int | ❌ | Total meeting length in minutes (default: `30`) |
| `silent_reading_time` | int | ❌ | Minutes allocated for silent reading (default: `5`) |
| `team_size` | int | ❌ | Number of participants (affects reading time heuristic) |
| `document_template` | string | ❌ | URL or ID of a reusable meeting document template |
| `shared_links` | list[string] | ❌ | Related reference links to embed in the agenda |


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位会议速读专家，擅长快速提炼会议纪要、识别决策点和行动项。请根据以下输入执行操作：
输入：[粘贴会议录音转写文本或会议记录]
要求：[提取关键决策、行动项、责任人和时间节点]
输出格式：[结构化会议纪要，包含决策摘要、待办事项清单和后续跟踪项]
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改

## 📤 输出

```json
{
  "meeting_doc_url": "string — link to the finalized meeting document",
  "decisions": [
    {
      "topic": "string",
      "decision": "string",
      "rationale": "string (optional)"
    }
  ],
  "action_items": [
    {
      "task": "string",
      "owner": "string",
      "deadline": "YYYY-MM-DD",
      "status": "pending"
    }
  ],
  "comments_resolved": "integer — number of inline comments addressed",
  "comments_pending": "integer — number of comments still open",
  "follow_up_meeting": "boolean — whether a follow-up was scheduled",
  "doc_shared_with": "list[string] — people/groups the doc was shared with"
}
```

## 📋 执行步骤

### Phase 1: 准备文档，整理议题和流程 (Preparation — T-10 min)

1. **Create or open the meeting document.** Use a meeting template if available. Set the document title to the meeting topic with the date.

2. **Populate the agenda.** Add each topic as a top-level heading. Under each heading, include:
   - Brief context / background (2–3 sentences max)
   - Related links, data, or prior decisions
   - Estimated time for discussion
   - `@mention` the person responsible for presenting or owning that topic

3. **Adjust document permissions.** Set the document to be viewable/editable by all participants. Ensure "shared screen mode" or "presentation mode" is available if using the platform's screen-sharing doc feature.

4. **Send the document link to all participants** at least 10 minutes before the meeting, along with the time for silent reading.

> 💡 **Platform note (non-Feishu):** In Google Docs, use "Comment" + "Suggesting" mode. In Notion, use inline comments. In Confluence, use page comments. The key is that every participant can annotate before discussion begins.

### Phase 2: 默读文档，评论疑问和建议 (Silent Reading — 5 min)

5. **Initiate the video call.** The host starts the meeting and shares the meeting document on screen.

6. **Announce the silent reading period.** Clearly state: *"We'll spend the next [N] minutes reading the document. Please post your questions and suggestions as comments on the relevant sections."*

7. **Participants read independently.** Each person opens "free browse mode" (自由浏览模式) and reads at their own pace, navigating to sections most relevant to them.

8. **Annotate during reading.** Participants place comments, questions, or suggestions directly at the relevant location in the document — not in chat, not verbally.

9. **Use built-in tools:**
   - **Timer/Countdown** — set a visible countdown in the doc so everyone knows when silent reading ends.
   - **Progress tracking** (e.g., Feishu's 信息收集) — poll participants to confirm they've finished reading.

> 💡 **Time heuristic:** 5 min for documents under 2,000 words or ≤8 participants. Scale up by 1–2 min for longer docs or larger groups.

### Phase 3: "穿屏"互动，依序讨论并记录 (Screen-Through Discussion — 20 min)

10. **Begin sequential topic discussion.** The host moves through the document topic by topic, in agenda order.

11. **Address comments first.** For each topic, review the inline comments placed during silent reading. These represent the highest-priority questions from prepared readers.

12. **"Screen-through" interaction (穿屏):** Participants can directly click on the shared screen's document and edit content in real time — correcting facts, adding data, or co-writing conclusions. This turns the shared screen into a collaborative whiteboard.

13. **Toggle browsing modes as needed:**
    - **Follow mode (跟随模式)** — participants sync their view with the host's cursor to stay on the current discussion point.
    - **Free browse mode (自由浏览模式)** — participants temporarily break away to review specific sections, then rejoin the host's view.

14. **Record discussion points in real time.** The host (or a designated note-taker) captures key points, disagreements, and emerging decisions directly in the document under the relevant topic heading.

> 💡 **Platform note (non-Feishu):** Without native "screen-through," participants can open the same doc in their own browser and edit simultaneously. The host should verbally confirm which section is under discussion.

### Phase 4: 明确结论，分配待办负责人 (Conclusion & Action Items — 5 min)

15. **Summarize conclusions for each topic.** At the end of each topic section (or in a dedicated "Conclusions" section), write a concise summary of what was decided.

16. **Define action items.** For each next step, record:
    - **What** needs to be done (specific, measurable)
    - **Who** is responsible (`@mention` the owner)
    - **When** it's due (set a concrete date)
    - **Where** progress will be tracked (usually in this same document)

17. **Confirm ownership.** Ask each action item owner to verbally acknowledge their tasks before ending the meeting.

18. **Close the meeting.** Thank participants and confirm the post-meeting document polish window.

### Phase 5: 完善文档，分享给相关同事 (Post-Meeting Follow-Up — within 30 min)

19. **Polish the document.** The host refines meeting notes, ensures all conclusions and action items are clearly written, and fixes any formatting or incomplete entries.

20. **Share the document** with the broader team or stakeholders who did not attend, so they can review key takeaways and understand their tasks.

21. **Enable ongoing tracking.** Ask action item owners to update their progress directly in the document. This creates a living record that prevents decisions from being forgotten.

22. **Set a review checkpoint.** If action items span multiple days/weeks, schedule a brief follow-up flyreading meeting to review progress.

## ⚠️ 异常处理

| Scenario | Detection | Response |
|---|---|---|
| **Participant no-show** | Missing from video call after 2 min | Start without them; assign a buddy to catch them up via doc comments after the meeting |
| **Document not ready** | Agenda is empty or incomplete at meeting time | Delay start by 5 min; host fills critical gaps live; flag incomplete topics for next meeting |
| **Time overrun** | Topic discussion exceeds estimate by >50% | Host intervenes: "We're 2 min over on this topic. Let's capture the remaining discussion as comments and move on." |
| **Low engagement (no comments)** | 0 comments placed during silent reading | Host prompts: "If you have no questions, please place a ✅ reaction on each section to confirm you've read it." Extend reading by 2 min if needed |
| **Platform instability (lag/disconnect)** | Shared screen freezes or edits don't sync | Switch to "everyone opens the doc in their own browser" mode. Continue discussion verbally with one person editing the master doc |
| **Scope creep (off-topic discussion)** | Discussion drifts from the current agenda item | Host captures the tangent as a new item in the document: "Added to parking lot for future discussion." Redirect to the current topic |
| **Disagreement / conflict** | Two participants have opposing views, discussion stalls | Time-box: 2 min for each side to state their position in the doc. Then take a quick poll or escalate to a decision-maker |
| **Large group (>15 participants)** | Meeting has too many voices for 20-min discussion | Split into sub-groups with parallel docs for different topic clusters; reconvene for final 5-min conclusions |

## 🔧 平台适配 (Platform Adaptations)

| Feature | Feishu/Lark | Google Docs | Notion | Confluence |
|---|---|---|---|---|
| Silent reading comments | ✅ Native inline comments | ✅ Comments + Suggesting mode | ✅ Inline comments | ✅ Page/in-line comments |
| Screen-through editing | ✅ Native (穿屏) | ⚠️ Simulated (multi-cursor) | ⚠️ Simulated | ⚠️ Simulated |
| Follow/Free browse modes | ✅ Native | ❌ Manual (use @mention section links) | ❌ Manual | ❌ Manual |
| Timer/Countdown | ✅ Native widget | ❌ Use external timer | ❌ Use external timer | ❌ Use external timer |
| Document sharing to groups | ✅ Native | ✅ Share with groups | ✅ Share with workspace | ✅ Share with spaces |
| Action items with reminders | ✅ Native tasks | ⚠️ Use checkboxes + Calendar | ⚠️ Use databases + reminders | ⚠️ Use task lists |
| Reading progress tracking | ✅ Native (信息收集) | ❌ Manual poll | ❌ Manual poll | ❌ Manual poll |

## ✅ 飞阅会质量自检清单 (Meeting Quality Self-Check)

Use this checklist before, during, and after each flyreading meeting:

### Before the meeting
- [ ] All agenda topics have context, links, and assigned owners
- [ ] Document permissions are set for all participants
- [ ] Document link was shared at least 10 minutes before the meeting
- [ ] Estimated reading time has been calculated and communicated

### During the meeting
- [ ] Silent reading period was announced and timed
- [ ] At least 80% of participants placed comments during reading
- [ ] Discussion followed the agenda sequence (no major detours)
- [ ] All inline comments were addressed or acknowledged
- [ ] Conclusions were recorded in real time in the document

### After the meeting
- [ ] Document was polished and shared within 30 minutes of meeting end
- [ ] Every action item has an owner and a deadline
- [ ] Non-attendees have been notified and can 00-META the document
- [ ] Progress tracking mechanism is in place (doc comments, status updates)
- [ ] Follow-up meeting was scheduled if needed

## 📚 参考

- [飞阅会官方介绍 — 多人会议效率低？独家秘笈飞阅会助你提效](https://www.feishu.cn/hc/zh-CN/articles/360042128094) (Feishu Help Center)
- [飞书会议倒计时功能](https://www.feishu.cn/hc/zh-CN/articles/083603023089)
- [飞书信息收集功能](https://www.feishu.cn/hc/zh-CN/articles/490019170235)
- [飞书会议记录模板](https://www.feishu.cn/space/api/obj_template/create_obj_from_ow/?type=2&token=[REDACTED_TOKEN]&create_source=2)
- Source: `[VAULT_ROOT]/01-BRAIN/...`


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
---
**相关笔记**：[[住宿订单优化]] [[uSkill-agent-优先级排序-agent-实施手册]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定制。

---

## 🚫 Anti-Rationalization Table `[v3新增]`

> 来源：addyosmani/agent-skills 的核心创新

| Agent 常见借口 | 反驳 |
|--------------|------|
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
- 检查常见错误

### ⚠️ Ask first（先问再做）
- 用户意图不明确时
- 操作不可逆时
- 涉及外部系统时

### 🚫 Never do（绝对禁止）
- 不跳过验证步骤
- 不在用户未确认时执行高风险操作
- 不伪装成功（失败就上报）

---

## 🔒 Gated Workflow `[v3新增]`

> 来源：addyosmani 的门禁 + claude-skills 的 Agent Harness

```
DISCUSS → PLAN → EXECUTE → VERIFY → CLOSE
   ↓         ↓        ↓          ↓        ↓
 Context   方案     执行      证据     Done/
 Read     确认     任务      检查    Escalate
```

### Phase 1: DISCUSS
- [ ] 输出 Context Read 一行判断
- [ ] 确认用户意图
- [ ] 确认约束条件

### Phase 2: PLAN
- [ ] 制定执行方案
- [ ] 确认资源可用
- [ ] 人工审批计划

### Phase 3: EXECUTE
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功


**相关概念**：[[积极倾听]]

---



## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功
