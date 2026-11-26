
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
- 当会议出现重大分歧且无法在会内解决时，**必须**安排专题讨论
- 当行动项连续 2 次跟进未完成时，**必须**升级处理
- 当会议效率持续下降时，**必须**重新评估会议必要性

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `MT_ERROR_NO_AGENDA` | 会议无议程 | 建议推迟并补充议程 | 🔴 |
| `MT_ERROR_OVER_TIME` | 会议超时 50% | 立即收敛，剩余议题移至 parking lot | 🟡 |
| `MT_WARNING_LOW_ATTENDANCE` | 关键决策者缺席 | 延期或改为书面决策 | 🟡 |
| `MT_WARNING_NO_OUTCOME` | 会议无明确决议 | 安排跟进会议或指定决策人 | 🟡 |
| `MT_ERROR_CONFLICT` | 参会者间严重冲突 | 暂停会议，安排一对一沟通 | 🔴 |

### 降级策略
- 当无法召集全体参会时，采用异步文档协作 + 简短确认会
- 当会议频繁超时，拆分为多个短会或改为书面决策

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 行动项有责任人和截止日期

### 内容校验
- [ ] 议程覆盖所有必要话题
- [ ] 时间分配合理
- [ ] 决议明确无歧义
- [ ] 会后纪要完整

### 合规校验
- [ ] 未遗漏关键决策者
- [ ] 敏感信息处理得当
- [ ] 跟进机制已建立

### OVP 验证信号
- 会议时间压缩率 ≥ 25%
- 会后行动项执行率 ≥ 85%
- 参会者满意度 ≥ 4.0/5.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "周会优化",
    "prompt": "我们每周一开 2 小时周会，感觉效率很低，一半时间在闲聊",
    "context": "meeting_type=weekly, participants=['PM', 'Dev×3', 'QA', 'Designer']",
    "assertions": [
      "pre_meeting.agenda 有明确时间分配",
      "during_meeting.time_management.total_minutes ≤ 60",
      "post_meeting.follow_up_actions 每项有 owner 和 deadline"
    ],
    "expected_behavior": "将 2 小时周会优化为 1 小时高效会议，含结构化议程和跟进机制",
    "critic_attack": "是否考虑了团队文化？压缩时间是否现实？"
  },
  {
    "id": "test-002",
    "name": "决策会议设计",
    "prompt": "我们需要决定用 React 还是 Vue 重写前端",
    "context": "meeting_type=decision, participants=['CTO', 'Tech Lead', '3 Senior Devs']",
    "assertions": [
      "pre_meeting.agenda 包含决策标准",
      "during_meeting.recording_template.decisions 包含明确结论",
      "pre_meeting.pre_reading 包含技术对比文档"
    ],
    "expected_behavior": "设计结构化决策会议，包含评估标准、方案对比、投票机制",
    "critic_attack": "是否考虑了技术选型的风险评估？"
  },
  {
    "id": "test-003",
    "name": "无效会议识别",
    "prompt": "这个会只是通知大家一个消息，要不要开？",
    "context": "meeting_type=sync, topic='通知项目延期' , participants=['10人']",
    "assertions": [
      "analysis 建议异步通知替代",
      "如果仍需会议，时长 ≤ 15 分钟",
      "提供了邮件/文档替代方案"
    ],
    "expected_behavior": "识别纯通知类会议，建议异步替代方案",
    "critic_attack": "是否充分考虑了团队沟通氛围的影响？"
  },
  {
    "id": "test-004",
    "name": "站会效率提升",
    "prompt": "我们的站会经常变成讨论会，经常超时",
    "context": "meeting_type=standup, participants=['Scrum Master', 'Dev×5', 'QA']",
    "assertions": [
      "during_meeting.structure 明确区分同步和讨论",
      "parking_lot 机制已设计",
      "时间管理严格 ≤ 15 分钟"
    ],
    "expected_behavior": "恢复站会本质，严格时间盒，讨论问题移至专题会",
    "critic_attack": "是否处理了团队习惯改变的阻力？"
  },
  {
    "id": "test-005",
    "name": "跨部门协调会",
    "prompt": "产品、研发、设计三方对需求理解不一致，需要对齐",
    "context": "meeting_type=project_review, participants=['Product×2', 'Dev Lead', 'Design Lead', 'QA Lead']",
    "assertions": [
      "pre_meeting 包含各方立场预收集",
      "during_meeting 结构包含分歧解决环节",
      "post_meeting 包含共识文档模板"
    ],
    "expected_behavior": "设计促进理解的会议结构，确保各方声音被听到",
    "critic_attack": "是否考虑了权力不对等导致的沉默？"
  },
  {
    "id": "test-006",
    "name": "远程会议优化",
    "prompt": "我们是远程团队，视频会议经常有人不说话",
    "context": "meeting_type=weekly, participants=['远程×6']",
    "assertions": [
      "during_meeting 包含远程参与引导策略",
      "recording_template 包含发言人记录",
      "pre_meeting 包含技术准备检查"
    ],
    "expected_behavior": "针对远程场景设计参与度提升方案",
    "critic_attack": "是否考虑了时区差异？"
  },
  {
    "id": "test-007",
    "name": "复盘会议设计",
    "prompt": "项目出了严重事故，需要开复盘会",
    "context": "meeting_type=project_review, topic='生产事故复盘', participants=['Tech Lead', 'Dev×3', 'Ops']",
    "assertions": [
      "pre_meeting 包含事实收集和时间线",
      "during_meeting 结构强调无责复盘原则",
      "post_meeting 包含根因分析和改进措施"
    ],
    "expected_behavior": "设计无责复盘会议，聚焦改进而非追责",
    "critic_attack": "是否确保了心理安全感？"
  },
  {
    "id": "test-008",
    "name": "会议频率审计",
    "prompt": "我一周有 20 个会，根本没时间写代码",
    "context": "meeting_type=sync",
    "assertions": [
      "analysis 提供会议必要性评估框架",
      "建议合并或取消可替代的会议",
      "提供时间保护策略"
    ],
    "expected_behavior": "审计会议负担，提供减负方案",
    "critic_attack": "建议是否考虑了组织政治因素？"
  },
  {
    "id": "test-009",
    "name": "头脑风暴引导",
    "prompt": "我们需要想出新产品的 10 个创意",
    "context": "meeting_type=brainstorm, participants=['Product', 'Design', 'Marketing', 'Dev']",
    "assertions": [
      "pre_meeting 包含发散和收敛阶段设计",
      "during_meeting 包含创意引导工具",
      "recording_template 包含投票排序机制"
    ],
    "expected_behavior": "设计高效的头脑风暴流程，确保创意产出",
    "critic_attack": "是否避免了群体思维？是否给了内向者空间？"
  },
  {
    "id": "test-010",
    "name": "会议纪要标准化",
    "prompt": "每次会后都忘记记了什么，下次开会又从头讨论",
    "context": "meeting_type=weekly",
    "assertions": [
      "post_meeting.minutes_template 包含决议和行动项",
      "post_meeting.next_meeting_agenda 自动继承 parking lot",
      "跟踪机制确保行动项闭环"
    ],
    "expected_behavior": "建立会议连续性机制，确保决议可追溯",
    "critic_attack": "纪要模板是否过于复杂导致无人填写？"
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

- [[AI回忆录撰写服务-PRD与实现方案]] — 产品需求文档
- [[文档质量评审]] — 文档评审标准
- [[OKR 战略目标管理]] — 目标对齐
- [[GTD执行]] — 任务管理
- [[深度工作四步法——专注力炼金术]] — 专注时间保护

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：会前→会中→会后全流程 + Self-Play |

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


**相关概念**：[[积极倾听]] · [[社会意识]] · [[心理安全]]

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
