---
name: uskill-efficiency-email-processing
description: "让邮件处理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-email-processing.md"
  original_id: "SKL-5207"
  version: "3.0.0"
  trust: untrusted
---

# 邮件处理

description: |
  当用户需要高效处理邮件、应用 4D 原则（Delete/Do/Delegate/Defer）、管理邮件优先级时使用此 Skill。
  触发词包括：'邮件'、'邮件处理'、'收件箱'、'邮件管理'、'4D原则'、'邮件模板'、'邮件回复'。
  当用户抱怨"邮件太多处理不完"、"不知道先回哪个"、"邮件写不好"时，
  即使未直接说"邮件处理"，也应使用此 Skill。
  不适用于即时通讯工具的消息管理。遇到邮件全生命周期管理时优先使用。

---

# uSkill-207: 邮件处理

## 🎯 目标

> 应用 4D 原则高效处理邮件，建立邮件优先级体系，提供模板化回复方案。

**核心价值**：将邮件从信息负担转变为高效沟通工具，减少处理时间，提升回复质量。

**适用场景**：
- 每日邮件批量处理
- 重要邮件优先级排序
- 模板化回复设计
- 邮件归档与整理
- 跨时区邮件协调

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `emails` | `array` | ✅ | — | 待处理邮件列表 |
| `action_type` | `enum` | ❌ | `process` | `process` / `draft` / `organize` / `review` |
| `priority_framework` | `enum` | ❌ | `eisenhower` | `eisenhower` / `urgent_important` / `custom` |
| `context` | `object` | ❌ | — | `{role, responsibilities, working_hours}` |

**输入约束**：
- `emails` 每项应包含 subject, sender, body_snippet, timestamp
- `action_type=draft` 时必须提供回复意图
- 优先级框架应与用户工作风格匹配

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结邮件处理状态",
  "email_id": "EM-YYYY-MMDD-NNN",

  "triage": {
    "total_emails": "number",
    "classification": {
      "delete": "number",
      "do": "number",
      "delegate": "number",
      "defer": "number"
    },
    "priority_queue": [
      {
        "email_id": "string",
        "subject": "string",
        "sender": "string",
        "d4_action": "delete|do|delegate|defer",
        "priority": "P1|P2|P3|P4",
        "estimated_time": "string",
        "deadline": "string"
      }
    ]
  },

  "drafts": [
    {
      "email_id": "string",
      "to": "string",
      "subject": "string",
      "body": "string",
      "tone": "formal|casual|urgent",
      "notes": "string"
    }
  ],

  "delegation": [
    {
      "email_id": "string",
      "delegate_to": "string",
      "reason": "string",
      "follow_up_date": "string"
    }
  ],

  "deferral": [
    {
      "email_id": "string",
      "defer_to": "string",
      "reason": "string",
      "reminder_set": "boolean"
    }
  ],

  "archive_plan": {
    "folders": ["string"],
    "rules": ["string"],
    "auto_archive_criteria": "string"
  },

  "metrics": {
    "estimated_processing_time": "string",
    "inbox_zero_eta": "string",
    "response_rate": "string"
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

### Step 1: 邮件收集与分类

- **输入**：`emails`
- **动作**：
  1. 收集所有待处理邮件
  2. 快速扫描判断可删除项
  3. 应用 4D 原则分类
- **输出**：`triage`
- **分支条件**：
  - IF 邮件来自订阅/通知 → 评估是否可退订或自动归档
  - IF 邮件可 2 分钟内回复 → 直接标记为 do 并执行
  - IF 邮件需要他人处理 → 标记为 delegate
  - IF 邮件需要等待外部信息 → 标记为 defer 并设置提醒
  - ELSE → 进入优先级排序
- **检查点**：✅ 应验证每封邮件有明确的 4D 分类

### Step 2: 优先级排序

- **输入**：`triage`
- **动作**：
  1. 按 Eisenhower 矩阵排序
  2. 考虑截止日期和发件人重要性
  3. 生成优先级队列
- **输出**：`triage.priority_queue`
- **分支条件**：
  - IF 来自上级/客户且紧急 → P1 立即处理
  - IF 影响项目进度 → P2 当日内处理
  - IF 信息性/可选 → P3 批量处理
  - IF 低价值/可忽略 → P4 归档或删除
- **检查点**：✅ 应验证优先级与实际情况匹配

### Step 3: 邮件草拟

- **输入**：`triage.priority_queue` (do 类)
- **动作**：
  1. 分析邮件意图和所需回复类型
  2. 选择合适的语气和格式
  3. 生成邮件草稿
- **输出**：`drafts`
- **分支条件**：
  - IF 正式商务邮件 → 使用专业模板，正式语气
  - IF 内部协作邮件 → 简洁直接，可使用要点格式
  - IF 紧急情况 → 突出关键信息，明确行动项
  - IF 需要拒绝 → 使用"三明治"法（肯定→拒绝→替代方案）
- **检查点**：✅ 应验证草稿语气恰当、信息完整

### Step 4: 委托与延迟处理

- **输入**：`triage`
- **动作**：
  1. 为 delegate 类邮件选择委托对象
  2. 为 defer 类邮件设置提醒
  3. 跟踪委托状态
- **输出**：`delegation`, `deferral`
- **分支条件**：
  - IF 委托对象不明确 → 建议合适的委托人
  - IF 延迟超过 7 天 → 评估是否需要升级处理
  - IF 委托无响应 → 设置自动提醒
  - ELSE → 正常跟踪
- **检查点**：✅ 应验证委托有明确责任人，延迟有提醒

### Step 5: 归档与清理

- **输入**：处理完成的邮件
- **动作**：
  1. 设计文件夹结构
  2. 创建自动归档规则
  3. 清理收件箱
- **输出**：`archive_plan`
- **检查点**：✅ 应验证归档规则可维护且不遗漏重要邮件

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在未确认的情况下删除重要邮件
2. **不得**将需要人工判断的邮件自动回复
3. **必须**为每封 P1 邮件在 4 小时内响应
4. **必须**保留所有涉及承诺和协议的邮件记录

### 软性约束（建议遵守）
1. 每日固定 2-3 个时段处理邮件
2. 避免在收件箱中回复（先处理再回复）
3. 长邮件考虑电话或会议替代
4. 定期清理超过 30 天的非重要邮件

### 人工兜底点
- 当邮件涉及法律、财务、人事敏感信息时，**必须**人工审核后发送
- 当收到威胁或不当邮件时，**必须**转交相关部门处理
- 当邮件链

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
