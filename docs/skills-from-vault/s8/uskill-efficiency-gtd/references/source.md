
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
|------|------|
| 1 | 清空所有收件箱 |
| 2 | 回顾下一步行动清单 |
| 3 | 回顾项目清单 |
| 4 | 回顾等待清单 |
| 5 | 回顾将来也许清单 |
| 6 | 检查日历（未来 7 天） |

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**将模糊目标直接放入下一步行动
2. **不得**跳过每周回顾
3. **必须**为每个项目定义明确的完成标准

### 软性约束（建议遵守）
1. 建议每天清空收件箱
2. 建议每周进行一次完整回顾
3. 建议限制下一步行动清单在 50 项以内

### 人工兜底点
- 当任务积压过多时，**必须**建议优先级排序
- 当无法定义下一步时，**必须**建议分解任务

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `GT_WARNING_INBOX_FULL` | 收件箱 > 50 项 | 建议立即清理 | 🟡 |
| `GT_WARNING_NO_NEXT_ACTION` | 项目无下一步 | 建议定义下一步 | 🟡 |
| `GT_ERROR_OVERWHELMED` | 任务过多无法处理 | 建议优先级排序 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 收件箱已清空
- [ ] 所有可行动项有下一步
- [ ] 项目有明确定义
- [ ] 回顾清单已生成

### OVP 验证信号
- 收件箱清零率 ≥ 90%
- 下一步行动明确率 ≥ 95%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "收件箱清理",
    "prompt": "我有30封邮件、10个会议纪要、5个想法需要处理",
    "context": "action_type=collect",
    "assertions": [
      "collection.total_items = 45",
      "processing_decisions 每项都有决策",
      "organization.next_actions 已生成"
    ],
    "expected_behavior": "收集并处理所有项目",
    "critic_attack": "是否正确分类了所有项目？"
  },
  {
    "id": "test-002",
    "name": "项目分解",
    "prompt": "我需要完成年度报告，这是一个大项目",
    "context": "action_type=organize",
    "assertions": [
      "organization.projects 包含 年度报告",
      "project.next_actions 至少 3 个具体步骤",
      "每步有明确的完成标准"
    ],
    "expected_behavior": "将大项目分解为可执行的下一步",
    "critic_attack": "分解是否足够细致？"
  },
  {
    "id": "test-003",
    "name": "每周回顾",
    "prompt": "这周任务很多，我需要进行每周回顾",
    "context": "action_type=review",
    "assertions": [
      "review_checklist.weekly_review 包含 完整步骤",
      "metrics 包含 当前状态统计",
      "建议已生成"
    ],
    "expected_behavior": "执行完整的每周回顾",
    "critic_attack": "回顾是否足够深入？"
  }
]
```

---

## 🔗 关联文档

- [[时间块规划]] — 时间块安排
- [[uSkill-日程优化-v1]] — 日程优化
- [[uSkill-系统熵增检测-v1]] — 晨间计划
- [[uSkill-productivity-晚间复盘报告]] — 晚间复盘
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：收集-处理-组织-回顾 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


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


**相关概念**：[[艾宾浩斯遗忘曲线]] · [[生产力系统]]


**相关概念**：[[三大Agent-Skills框架方法论对比]]

---


## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志

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
