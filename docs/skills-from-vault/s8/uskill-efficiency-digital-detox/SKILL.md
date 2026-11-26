---
name: uskill-efficiency-digital-detox
description: "让数字断舍离变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-digital-detox.md"
  original_id: "SKL-6920"
  version: "3.0.0"
  trust: untrusted
---

# 数字断舍离

description: |
  当用户需要清理数字文件、整理邮件、管理订阅、减少数字噪音时使用此 Skill。
  触发词包括：'数字断舍离'、'文件清理'、'邮件整理'、'订阅管理'、'数字极简'。
  当用户讨论效率、整理、减负时，
  即使未直接说"数字断舍离"，也应使用此 Skill。
  不适用于知识库管理（使用第二大脑 Skill）。遇到数字物品清理时优先使用。

---

# uSkill-204: 数字断舍离

## 🎯 目标

> 清理数字物品，减少信息噪音，提升数字生活效率。

**核心价值**：数字物品也会占据心智空间。清理数字物品能提升专注力。

**适用场景**：
- 文件清理
- 邮件整理
- 订阅管理
- 应用清理
- 通知优化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `cleanup_scope` | `enum` | ❌ | `all` | `files` / `email` / `subscriptions` / `apps` / `all` |
| `current_status` | `object` | ❌ | — | 当前数字物品状况 |
| `goals` | `array` | ❌ | `[]` | 清理目标 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话清理建议",
  "detox_id": "DD-YYYY-MMDD-NNN",

  "assessment": {
    "total_files": "number",
    "total_emails": "number",
    "active_subscriptions": "number",
    "installed_apps": "number",
    "notification_sources": "number",
    "digital_clutter_score": "number — 0-100"
  },

  "cleanup_plan": {
    "files": {
      "strategy": "string",
      "categories": [
        {
          "category": "string",
          "action": "delete|archive|organize",
          "criteria": "string",
          "estimated_savings": "string"
        }
      ]
    },
    "email": {
      "strategy": "string",
      "actions": ["string"],
      "automation_rules": ["string"]
    },
    "subscriptions": {
      "strategy": "string",
      "keep": ["string"],
      "cancel": ["string"],
      "downgrade": ["string"]
    },
    "apps": {
      "strategy": "string",
      "keep": ["string"],
      "uninstall": ["string"]
    }
  },

  "automation_setup": {
    "file_management": ["string"],
    "email_rules": ["string"],
    "notification_optimization": ["string"]
  },

  "maintenance_routine": {
    "daily": ["string"],
    "weekly": ["string"],
    "monthly": ["string"],
    "quarterly": ["string"]
  },

  "benefits_tracking": {
    "storage_saved": "string",
    "time_saved_weekly": "string",
    "stress_reduction": "string"
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

### Step 1: 数字物品评估

- **输入**：`current_status`
- **动作**：
  1. 统计各类数字物品数量
  2. 评估数字杂乱程度
  3. 识别高优先级清理领域
- **输出**：`assessment`

### Step 2: 文件清理

- **输入**：`assessment.total_files`
- **动作**：
  1. 设计清理策略
  2. 制定分类标准
  3. 执行清理
- **输出**：`cleanup_plan.files`
- **文件清理原则**：

| 原则 | 描述 |
|------|------|
| 一年规则 | 超过一年未使用的文件归档 |
| 重复文件 | 检测并删除重复文件 |
| 临时文件 | 清理临时和缓存文件 |
| 大文件 | 识别并处理大文件 |

### Step 3: 邮件整理

- **输入**：`assessment.total_emails`
- **动作**：
  1. 设计清理策略
  2. 创建过滤规则
  3. 设置自动归档
- **输出**：`cleanup_plan.email`

### Step 4: 订阅管理

- **输入**：`assessment.active_subscriptions`
- **动作**：
  1. 列出所有订阅
  2. 评估使用频率
  3. 决定保留/取消/降级
- **输出**：`cleanup_plan.subscriptions`

### Step 5: 应用清理

- **输入**：`assessment.installed_apps`
- **动作**：
  1. 列出所有应用
  2. 评估使用频率
  3. 卸载不需要的应用
- **输出**：`cleanup_plan.apps`

### Step 6: 自动化设置

- **输入**：`cleanup_plan`
- **动作**：
  1. 设置文件管理自动化
  2. 创建邮件规则
  3. 优化通知设置
- **输出**：`automation_setup`

### Step 7: 维护例程

- **输入**：所有前序输出
- **动作**：
  1. 设计日常维护
  2. 安排周度整理
  3. 规划月度回顾
- **输出**：`maintenance_routine`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**删除重要数据
2. **不得**忽视数据备份
3. **必须**考虑数据安全

### 软性约束（建议遵守）
1. 建议先备份再清理
2. 建议循序渐进
3. 建议建立新习惯

### 人工兜底点
- 当涉及重要数据时，**必须**建议专业帮助
- 当清理困难时，**必须**建议分阶段进行

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `DD_WARNING_LARGE_SCOPE` | 范围过大 | 建议缩小范围 | 🟡 |
| `DD_WARNING_DATA_RISK` | 数据风险 | 建议备份 | 🟡 |
| `DD_ERROR_IMPORTANT_DATA` | 重要数据 | 建议保留 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 评估已完成
- [ ] 清理计划已制定
- [ ] 自动化已设置
- [ ] 维护例程已设计

### OVP 验证信号
- 数字物品减少 ≥ 30%
- 检索时间减少 ≥ 20%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "文件清理",
    "prompt": "我的电脑文件太多，需要清理",
    "context": "cleanup_scope=files",
    "assertions": [
      "assessment.total_files 已统计",
      "cleanup_plan.f

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
