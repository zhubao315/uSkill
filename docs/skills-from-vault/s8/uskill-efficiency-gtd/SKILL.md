---
name: uskill-efficiency-gtd
description: "让GTD执行变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-gtd.md"
  original_id: "SKL-6915"
  version: "3.0.0"
  trust: untrusted
---

# GTD执行

description: |
  当用户需要收集所有待办事项、处理和组织任务、定期回顾、确保所有任务有明确下一步时使用此 Skill。
  触发词包括：'GTD'、'任务管理'、'收件箱清零'、'待办事项'、'下一步行动'、
  '任务组织'、'每周回顾'、'任务收集'。当用户讨论任务管理、时间管理、
  工作效率时，即使未直接说"GTD"，也应使用此 Skill。
  不适用于简单的待办清单（直接记录即可）。遇到复杂任务管理时优先使用。

---

⚙️ AI-Co 运行配置块
触发场景: 用户说'收件箱清零'、'任务管理'、'GTD'、'待办事项处理'、'下一步行动'
复用率预估: 高
一键调用: |
  收集→处理→组织→回顾四步流程，应用2分钟规则
输入Schema: |
  input_items: array — 待收集的任务/想法列表（必填）
  action_type: enum(collect/process/organize/review) — 默认 collect
  context: object — {current_projects, roles, goals}
输出Schema: |
  status: string
  collection: {total_items, categories}
  processing_decisions: [{item, decision, next_action, context}]
  organization: {next_actions, projects, waiting_for, someday_maybe}
  review_checklist: {weekly_review, monthly_review, quarterly_review}
  metrics: {inbox_zero, next_actions_count, completion_rate}
AI可执行度: 100%

# uSkill-202: GTD执行

## 🎯 目标

> 应用 Getting Things Done 方法论，将所有承诺和想法从大脑中收集出来，建立可靠的组织和回顾系统。

**核心价值**：清空大脑负担，确保所有任务都有明确下一步，减少焦虑和遗忘。

**适用场景**：
- 个人任务管理
- 项目任务跟踪
- 团队任务协调
- 跨项目任务管理
- 日常工作组织

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `input_items` | `array` | ✅ | — | 待收集的任务/想法列表 |
| `action_type` | `enum` | ❌ | `collect` | `collect` / `process` / `organize` / `review` |
| `context` | `object` | ❌ | — | `{current_projects, roles, goals}` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话GTD状态总结",
  "gtd_id": "GT-YYYY-MMDD-NNN",

  "collection": {
    "total_items": "number",
    "categories": {
      "tasks": "number",
      "ideas": "number",
      "references": "number",
      "someday_maybe": "number"
    }
  },

  "processing_decisions": [
    {
      "item": "string",
      "decision": "do|delegate|defer|delete",
      "actionable": true,
      "next_action": "string",
      "context": "string",
      "time_estimate": "string",
      "energy_level": "high|medium|low",
      "priority": "high|medium|low"
    }
  ],

  "organization": {
    "next_actions": [
      {
        "action": "string",
        "context": "string",
        "project": "string",
        "due_date": "string",
        "priority": "string"
      }
    ],
    "projects": [
      {
        "name": "string",
        "outcome": "string",
        "next_actions": ["string"],
        "waiting_for": ["string"]
      }
    ],
    "waiting_for": [
      {
        "item": "string",
        "delegated_to": "string",
        "follow_up_date": "string"
      }
    ],
    "someday_maybe": ["string"],
    "reference": ["string"]
  },

  "review_checklist": {
    "weekly_review": ["string"],
    "monthly_review": ["string"],
    "quarterly_review": ["string"]
  },

  "metrics": {
    "inbox_zero": "boolean",
    "next_actions_count": "number",
    "projects_count": "number",
    "completion_rate": "number"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 收集（Capture）

- **输入**：`input_items`
- **动作**：
  1. 收集所有"未竟之事"
  2. 清空大脑中的所有承诺
  3. 统一放入收件箱
- **输出**：`collection`
- **收集范围**：

| 类别 | 示例 |
|------|------|
| 工作任务 | 邮件、会议、项目 |
| 个人事务 | 家庭、健康、财务 |
| 想法创意 | 灵感、计划、愿望 |
| 参考信息 | 文档、链接、笔记 |

### Step 2: 处理（Process）

- **输入**：`collection`
- **动作**：
  1. 逐条处理收件箱项目
  2. 应用 2 分钟规则
  3. 做出处理决策
- **输出**：`processing_decisions`
- **处理决策流程**：

```
项目 → 是否可行动？
  ├─ 否 → 删除 / 参考 / 将来也许
  └─ 是 → 是否可 2 分钟内完成？
        ├─ 是 → 立即做
        └─ 否 → 是否可委托？
              ├─ 是 → 委托
              └─ 否 → 延期 → 下一步行动是什么？
```

- **2 分钟规则**：如果一件事能在 2 分钟内完成，立即做

### Step 3: 组织（Organize）

- **输入**：`processing_decisions`
- **动作**：
  1. 将任务放入正确的清单
  2. 定义下一步行动
  3. 关联到项目
- **输出**：`organization`
- **组织清单**：

| 清单 | 内容 |
|------|------|
| 下一步行动 | 具体可执行的下一步 |
| 等待 | 已委托给他人的事项 |
| 项目 | 需要多个步骤才能完成的目标 |
| 将来也许 | 目前不行动但想保留的事项 |
| 参考 | 需要保存但不需行动的信息 |

### Step 4: 回顾（Review）

- **输入**：`organization`
- **动作**：
  1. 检查系统完整性
  2. 更新任务状态
  3. 确保所有任务有下一步
- **输出**：`review_checklist`
- **每周回顾清单**：

| 步骤 | 内容 |
|------|-

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
