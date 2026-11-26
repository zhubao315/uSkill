---
name: uskill-productivity-meeting-flyreading
description: "让productivity meeting flyreading变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-meeting-flyreading.md"
  original_id: "SKL-6918"
  version: "3.0.0"
  trust: untrusted
---

# productivity meeting flyreading

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

6. 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
