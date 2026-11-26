
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
- 当邮件链超过 10 轮时，**必须**建议转为会议或电话沟通

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `EM_ERROR_AMBIGUOUS` | 无法确定 4D 分类 | 提供分类建议并请求确认 | 🟡 |
| `EM_WARNING_HIGH_VOLUME` | 待处理邮件 > 50 封 | 建议分批处理，优先处理 P1 | 🟡 |
| `EM_ERROR_SENSITIVE` | 涉及敏感信息 | 标记为需人工处理 | 🔴 |
| `EM_WARNING_CIRCULAR` | 邮件链循环讨论 | 建议电话或会议终止循环 | 🟡 |
| `EM_ERROR_DELEGATION_FAILED` | 委托无响应 | 自动提醒并建议备选委托人 | 🟡 |

### 降级策略
- 当邮件量过大无法逐封处理时，生成批量处理方案（快速扫描→批量归档）
- 当无法生成高质量回复时，提供回复框架和关键点

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 每封邮件有明确的 4D 分类

### 内容校验
- [ ] 优先级排序合理
- [ ] 回复草稿语气恰当
- [ ] 委托有明确责任人
- [ ] 延迟有提醒机制

### 合规校验
- [ ] 敏感邮件已标记
- [ ] 未自动回复需要人工判断的邮件
- [ ] 归档规则不遗漏重要信息

### OVP 验证信号
- 邮件处理时间减少 ≥ 40%
- 收件箱清零率 ≥ 90%
- P1 邮件响应时间 ≤ 4 小时

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "批量邮件分类",
    "prompt": "我有 30 封未读邮件，帮我快速分类处理",
    "context": "action_type=process, emails 包含各种类型",
    "assertions": [
      "triage.classification 四类都有数值",
      "priority_queue 按优先级排序",
      "estimated_processing_time 合理"
    ],
    "expected_behavior": "快速将 30 封邮件分为 4D 类别并排序",
    "critic_attack": "分类是否准确？是否存在误分类？"
  },
  {
    "id": "test-002",
    "name": "紧急邮件处理",
    "prompt": "老板发邮件说客户投诉了，需要今天回复",
    "context": "action_type=draft, priority_framework=eisenhower",
    "assertions": [
      "triage.priority_queue[0].priority = 'P1'",
      "drafts 包含正式回复草稿",
      "响应时间建议 ≤ 4 小时"
    ],
    "expected_behavior": "识别紧急邮件，生成高质量回复草稿",
    "critic_attack": "回复是否足够专业？是否解决了客户问题？"
  },
  {
    "id": "test-003",
    "name": "委托邮件处理",
    "prompt": "这封邮件应该由法务部处理，我不确定怎么回复",
    "context": "action_type=process",
    "assertions": [
      "delegation 包含委托建议",
      "delegate_to 指向法务部",
      "follow_up_date 已设置"
    ],
    "expected_behavior": "正确识别委托场景，提供委托建议和跟踪",
    "critic_attack": "委托理由是否充分？是否需要抄送？"
  },
  {
    "id": "test-004",
    "name": "邮件模板生成",
    "prompt": "帮我写一封拒绝合作邀请的邮件",
    "context": "action_type=draft",
    "assertions": [
      "drafts.body 使用三明治结构",
      "语气专业且礼貌",
      "包含替代方案或未来合作可能"
    ],
    "expected_behavior": "生成礼貌专业的拒绝邮件模板",
    "critic_attack": "是否保持了关系？是否过于生硬？"
  },
  {
    "id": "test-005",
    "name": "邮件归档设计",
    "prompt": "我的收件箱有 500 封邮件，需要整理归档",
    "context": "action_type=organize",
    "assertions": [
      "archive_plan.folders 结构清晰",
      "auto_archive_criteria 可执行",
      "不遗漏重要邮件"
    ],
    "expected_behavior": "设计合理的邮件归档体系",
    "critic_attack": "归档规则是否过于复杂？是否便于查找？"
  },
  {
    "id": "test-006",
    "name": "订阅邮件清理",
    "prompt": "我订阅了太多 newsletter，每天收件箱都是噪音",
    "context": "action_type=process",
    "assertions": [
      "triage.classification.delete 比例高",
      "提供了退订建议",
      "保留有价值的订阅"
    ],
    "expected_behavior": "识别低价值订阅，提供清理方案",
    "critic_attack": "是否误删了有价值的订阅？"
  },
  {
    "id": "test-007",
    "name": "跨时区邮件协调",
    "prompt": "我需要给纽约和伦敦的同事发邮件，考虑时差",
    "context": "action_type=draft, context={working_hours: 'UTC+8 9-18'}",
    "assertions": [
      "考虑了接收方的工作时间",
      "回复建议考虑时差",
      "紧急程度评估准确"
    ],
    "expected_behavior": "生成考虑时差的邮件处理建议",
    "critic_attack": "时差计算是否正确？"
  },
  {
    "id": "test-008",
    "name": "长邮件链处理",
    "prompt": "这个邮件链已经来回 12 轮了，还没结论",
    "context": "action_type=process",
    "assertions": [
      "建议转为会议或电话",
      "总结了当前分歧点",
      "提供了终止循环的方案"
    ],
    "expected_behavior": "识别邮件链循环，建议替代沟通方式",
    "critic_attack": "是否遗漏了重要的历史信息？"
  },
  {
    "id": "test-009",
    "name": "敏感邮件识别",
    "prompt": "收到一封涉及公司裁员计划的邮件",
    "context": "action_type=process",
    "assertions": [
      "标记为 sensitive",
      "不生成自动回复",
      "建议人工处理"
    ],
    "expected_behavior": "识别敏感邮件，触发人工兜底",
    "critic_attack": "敏感度判断是否准确？"
  },
  {
    "id": "test-010",
    "name": "邮件回复效率",
    "prompt": "这些邮件内容都差不多，能不能批量回复？",
    "context": "action_type=draft, emails 包含相似邮件",
    "assertions": [
      "识别可批量回复的邮件",
      "提供个性化模板",
      "保留人工审核环节"
    ],
    "expected_behavior": "识别批量回复机会，生成可个性化的模板",
    "critic_attack": "批量回复是否缺乏个性化？"
  }
]
```

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🔗 关联文档

- [[数字断舍离]] — 信息简化方法论
- [[SOP-23-效率分析]] — 效率诊断工具
- [[自动化工作流]] — 流程自动化
- [[GTD执行]] — 任务管理框架
- [[深度工作四步法——专注力炼金术]] — 专注时间保护

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：4D分类→优先级→草拟→委托→归档 + Self-Play |

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


**相关概念**：[[信息管理系统]]

---



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


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
