
description: |
  当用户需要进入深度专注状态、消除干扰、安排专注时间块、提升认知产出质量时使用此 Skill。
  触发词包括：'深度工作'、'专注'、'心流'、'不分心'、'高效工作'、
  '时间块'、'消除干扰'、'认知产出'。当用户讨论工作效率、时间管理、
  项目推进时，即使未直接说"深度工作"，也应使用此 Skill。
  不适用于协作型工作（使用会议纪要 Skill）。遇到需要深度专注的任务时优先使用。

---

⚙️ AI-Co 运行配置块
触发场景: 用户说'深度工作'、'专注'、'心流'、'高效工作'、'时间块'
复用率预估: 高
一键调用: |
  任务分析→时间块设计→环境配置→干扰管理→心流触发
输入Schema: |
  task: string — 需要深度工作的任务（必填）
  duration_minutes: number — 专注时长，默认90
  time_of_day: enum(morning/afternoon/evening/auto) — 默认 auto
  interruption_level: enum(low/medium/high) — 默认 high
输出Schema: |
  status: string
  work_block_design: {duration, phases, optimal_time, energy_alignment}
  environment_setup: {physical, digital, social, mental}
  interruption_management: {prevention, handling, recovery}
  flow_state_triggers: [{trigger, importance, implementation}]
  monitoring_metrics: {quantitative, qualitative, targets}
  post_work_review: {what_worked, what_to_improve}
AI可执行度: 100%

# uSkill-201: 深度工作

## 🎯 目标

> 建立深度工作习惯，在无干扰状态下专注于高认知需求任务，最大化认知产出。

**核心价值**：在注意力稀缺的时代，深度工作是最稀缺、最有价值的能力。

**适用场景**：
- 编程和软件开发
- 写作和创作
- 学习和研究
- 战略规划
- 复杂问题解决

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task` | `string` | ✅ | — | 需要深度工作的任务 |
| `duration_minutes` | `number` | ❌ | `90` | 专注时长（分钟） |
| `time_of_day` | `enum` | ❌ | `auto` | `morning` / `afternoon` / `evening` / `auto` |
| `interruption_level` | `enum` | ❌ | `high` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话深度工作建议",
  "deep_work_id": "DW-YYYY-MMDD-NNN",

  "work_block_design": {
    "duration": "number — 分钟",
    "phases": [
      {
        "phase": "warmup|focus|break|review",
        "duration": "number — 分钟",
        "activity": "string"
      }
    ],
    "optimal_time": "string",
    "energy_alignment": "string"
  },

  "environment_setup": {
    "physical": ["string"],
    "digital": ["string"],
    "social": ["string"],
    "mental": ["string"]
  },

  "interruption_management": {
    "prevention": ["string"],
    "handling": ["string"],
    "recovery": "string"
  },

  "flow_state_triggers": [
    {
      "trigger": "string",
      "importance": "high|medium|low",
      "implementation": "string"
    }
  ],

  "monitoring_metrics": {
    "quantitative": ["string"],
    "qualitative": ["string"],
    "targets": {
      "focus_duration": "number — 分钟",
      "interruption_count": "number",
      "flow_state_achieved": "boolean"
    }
  },

  "post_work_review": {
    "what_worked": ["string"],
    "what_to_improve": ["string"],
    "adjustments_for_next": ["string"]
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

### Step 1: 任务分析与规划

- **输入**：`task` + `duration_minutes`
- **动作**：
  1. 分析任务的认知需求
  2. 设计专注时间块
  3. 对齐精力水平
- **输出**：`work_block_design`
- **时间块设计原则**：

| 阶段 | 时长 | 目的 |
|------|------|------|
| 热身 | 5-10 分钟 | 进入状态 |
| 深度专注 | 60-90 分钟 | 核心工作 |
| 短休息 | 5-10 分钟 | 恢复精力 |
| 回顾 | 5-10 分钟 | 总结产出 |

### Step 2: 环境准备

- **输入**：`work_block_design`
- **动作**：
  1. 设置物理环境
  2. 配置数字环境
  3. 管理社交环境
- **输出**：`environment_setup`
- **环境清单**：

| 类型 | 准备项 |
|------|--------|
| 物理 | 整洁桌面、舒适椅子、适当光线 |
| 数字 | 关闭通知、使用专注模式、准备工具 |
| 社交 | 告知他人、设置"请勿打扰" |
| 心理 | 明确目标、排除杂念 |

### Step 3: 干扰管理

- **输入**：`interruption_level`
- **动作**：
  1. 预防干扰
  2. 处理不可避免的干扰
  3. 设计恢复策略
- **输出**：`interruption_management`

### Step 4: 心流触发

- **输入**：`task` + `work_block_design`
- **动作**：
  1. 识别心流触发条件
  2. 设计挑战-技能平衡
  3. 设定明确目标
- **输出**：`flow_state_triggers`
- **心流触发器**：

| 触发器 | 描述 |
|--------|------|
| 明确目标 | 知道要做什么 |
| 即时反馈 | 知道做得怎么样 |
| 挑战-技能平衡 | 任务难度适中 |
| 深度专注 | 无干扰状态 |
| 控制感 | 感觉能掌控任务 |

### Step 5: 监控与回顾

- **输入**：实际执行数据
- **动作**：
  1. 监控关键指标
  2. 进行事后回顾
  3. 生成改进建议
- **输出**：`monitoring_metrics` + `post_work_review`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**安排超过 4 小时的连续深度工作
2. **不得**忽视休息和恢复
3. **必须**考虑个人精力模式

### 软性约束（建议遵守）
1. 建议每天安排 2-3 个深度工作块
2. 建议在精力高峰期安排最难的任务
3. 建议每周回顾深度工作效果

### 人工兜底点
- 当连续 3 天无法完成深度工作计划时，**必须**调整策略
- 当出现倦怠迹象时，**必须**建议休息

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `DW_WARNING Interruptions` | 干扰次数 > 3 | 建议调整环境 | 🟡 |
| `DW_WARNING_NO_FLOW` | 未进入心流状态 | 建议调整任务难度 | 🟡 |
| `DW_ERROR_EXHAUSTION` | 精力耗尽 | 建议立即休息 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 时间块设计合理
- [ ] 环境准备完整
- [ ] 干扰管理策略可行
- [ ] 心流触发条件明确

### OVP 验证信号
- 深度工作时间 ≥ 3 小时/天
- 心流状态达成率 ≥ 60%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "编程深度工作",
    "prompt": "我需要2小时专注编程完成一个复杂功能",
    "context": "task=编程, duration=120, interruption_level=high",
    "assertions": [
      "work_block_design.phases 包含 热身、专注、休息",
      "environment_setup 包含 数字干扰消除",
      "interruption_management.prevention 已生成"
    ],
    "expected_behavior": "设计适合编程的深度工作块",
    "critic_attack": "是否考虑了编程的特殊性？"
  },
  {
    "id": "test-002",
    "name": "写作深度工作",
    "prompt": "我要写一篇3000字的文章，需要深度思考",
    "context": "task=写作, duration=90, interruption_level=medium",
    "assertions": [
      "work_block_design.optimal_time 建议早晨",
      "flow_state_triggers 包含 明确目标",
      "monitoring_metrics.quantitative 包含 字数"
    ],
    "expected_behavior": "设计适合写作的深度工作块",
    "critic_attack": "是否过度关注字数而忽视质量？"
  },
  {
    "id": "test-003",
    "name": "学习深度工作",
    "prompt": "我要学习一个新技术概念，需要深入理解",
    "context": "task=学习, duration=60, interruption_level=low",
    "assertions": [
      "work_block_design.duration = 60",
      "flow_state_triggers 包含 挑战-技能平衡",
      "post_work_review 已设计"
    ],
    "expected_behavior": "设计适合学习的深度工作块",
    "critic_attack": "是否为学习留出了足够的回顾时间？"
  }
]
```

---

## 🔗 关联文档

- [[心流状态激活]] — 心流触发方法
- [[柳比歇夫时间统计]] — 时间统计方法
- [[时间块规划]] — 时间块安排
- [[uSkill-日程优化-v1]] — 日程优化
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：时间块设计 + 环境准备 + 心流触发 + Self-Play |

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


**相关概念**：[[注意力的有限性]] · [[正念与注意力]] · [[选择性注意]]


**相关概念**：[[三大Agent-Skills框架方法论对比]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

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
