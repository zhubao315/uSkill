---
name: uskill-efficiency-meeting-efficiency
description: "让会议效率变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-meeting-efficiency.md"
  original_id: "SKL-5206"
  version: "3.0.0"
  trust: untrusted
---

# 会议效率

description: |
  当用户需要优化会议全流程（会前准备→会中记录→会后跟进）时使用此 Skill。
  触发词包括：'会议'、'会议效率'、'会议记录'、'会议纪要'、'议程'、'跟进'、'行动项'。
  当用户抱怨"会议太多"、"会议没结果"、"开了会跟没开一样"时，
  即使未直接说"会议效率"，也应使用此 Skill。
  不适用于一对一沟通或非正式交流。遇到结构化会议优化时优先使用。

---

# uSkill-206: 会议效率

## 🎯 目标

> 优化会议全生命周期（会前→会中→会后），减少无效会议，提升决策质量和执行效率。

**核心价值**：让每次会议都有明确目的、高效执行、可追踪的结果。

**适用场景**：
- 周会/月会等定期会议
- 项目启动/评审会议
- 跨部门协调会议
- 头脑风暴/决策会议
- 站会/同步会议

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `meeting_type` | `enum` | ✅ | — | `standup` / `weekly` / `project_review` / `brainstorm` / `decision` / `sync` |
| `topic` | `string` | ✅ | — | 会议主题 |
| `participants` | `array` | ✅ | — | 参会人员列表 |
| `duration_minutes` | `number` | ❌ | `30` | 会议时长（分钟） |
| `context` | `object` | ❌ | — | `{background, previous_decisions, blockers}` |

**输入约束**：
- `participants` 必须包含所有必要决策者
- `duration_minutes` 应与会议类型匹配
- `topic` 应明确到可产生具体结论

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结会议效率方案",
  "meeting_id": "MT-YYYY-MMDD-NNN",

  "pre_meeting": {
    "objective": "string",
    "agenda": [
      {
        "item": "string",
        "time_allocation": "string",
        "owner": "string",
        "decision_needed": "boolean"
      }
    ],
    "pre_reading": ["string"],
    "expected_outcomes": ["string"],
    "invitation_notes": "string"
  },

  "during_meeting": {
    "structure": {
      "opening": "string",
      "main_discussion": "string",
      "decision_points": "string",
      "closing": "string"
    },
    "recording_template": {
      "decisions": ["string"],
      "action_items": [
        {
          "action": "string",
          "owner": "string",
          "deadline": "string"
        }
      ],
      "parking_lot": ["string"],
      "risks": ["string"]
    },
    "time_management": {
      "total_minutes": "number",
      "allocations": "object"
    }
  },

  "post_meeting": {
    "minutes_template": "string",
    "follow_up_actions": [
      {
        "action": "string",
        "owner": "string",
        "deadline": "string",
        "status": "pending"
      }
    ],
    "next_meeting_agenda": ["string"],
    "communication_plan": "string"
  },

  "metrics": {
    "estimated_time_saved": "string",
    "decision_clarity_score": "number",
    "follow_up_completion_rate": "string"
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

### Step 1: 会议需求分析

- **输入**：`meeting_type`, `topic`, `participants`
- **动作**：
  1. 判断会议是否必要（能否用邮件/文档替代）
  2. 确定会议类型和最佳时长
  3. 识别关键决策者和利益相关者
- **输出**：会议必要性评估 + 基础框架
- **分支条件**：
  - IF 纯信息同步 → 建议异步文档替代，取消会议
  - IF 需要多人讨论决策 → 进入完整流程
  - IF 参会人 > 8 → 建议缩小范围或分组讨论
  - ELSE → 标准会议流程
- **检查点**：✅ 应验证会议确实需要实时同步进行

### Step 2: 会前准备

- **输入**：会议需求分析结果
- **动作**：
  1. 设计结构化议程
  2. 分配时间预算
  3. 准备会前材料
  4. 发送会议邀请和预期
- **输出**：`pre_meeting`
- **分支条件**：
  - IF 决策型会议 → 议程必须包含决策点和选项对比
  - IF 头脑风暴 → 预留发散和收敛时间，准备引导问题
  - IF 有外部参会者 → 增加背景材料和术语说明
  - ELSE → 标准议程模板
- **检查点**：✅ 应验证议程覆盖所有必要话题且时间分配合理

### Step 3: 会中引导与记录

- **输入**：`pre_meeting`
- **动作**：
  1. 按议程引导讨论
  2. 实时记录决议和行动项
  3. 管理时间进度
  4. 处理偏离议题的情况
- **输出**：`during_meeting`
- **分支条件**：
  - IF 讨论偏离 → 记入 parking lot，回到主线
  - IF 出现僵局 → 使用决策框架（如投票、分组讨论）
  - IF 时间不够 → 优先处理高优先级议题，其余移至下次
  - ELSE → 按议程正常推进
- **检查点**：✅ 应验证所有决议有明确结论，所有行动项有责任人

### Step 4: 会后跟进

- **输入**：`during_meeting`
- **动作**：
  1. 生成会议纪要
  2. 分发行动项
  3. 设置跟进机制
  4. 更新项目文档
- **输出**：`post_meeting`
- **分支条件**：
  - IF 行动项 > 5 → 优先级排序，避免 overload
  - IF 涉及跨部门 → 增加同步通知相关方
  - IF 有风险项 → 立即上报，不等下次会议
  - ELSE → 标准跟进流程
- **检查点**：✅ 应验证行动项已通知到责任人且有明确截止日期

### Step 5: 会议效果评估

- **输入**：`post_meeting` + 实际执行情况
- **动作**：
  1. 追踪行动项完成率
  2. 评估会议时长合理性
  3. 收集参会者反馈
  4. 优化未来会议
- **输出**：`metrics`
- **检查点**：✅ 应验证评估指标可量化且有改进方向

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**召开无明确议程的会议
2. **不得**会议纪要超过 24 小时未分发
3. **必须**为每个行动项指定责任人和截止日期
4. **必须**在会议结束前确认所有决议

### 软性约束（建议遵守）
1. 会议时长尽量 ≤ 60 分钟
2. 参会人数尽量 ≤ 8 人
3. 每周同一类型会议不超过 1 次
4. 预留 10% 时间缓冲

### 人工兜底点


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
