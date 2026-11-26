
description: |
  当用户需要辅导他人成长、进行教练式对话、帮助他人达成目标、提升他人能力时使用此 Skill。
  触发词包括：'教练'、'辅导'、'coach'、'GROW模型'、'提问技术'、
  '成长辅导'、'职业辅导'。当用户讨论团队发展、人才培养、领导力时，
  即使未直接说"教练式辅导"，也应使用此 Skill。
  不适用于直接指导（告诉答案）。遇到需要引导他人自己找到答案时优先使用。

---

# uSkill-404: 教练式辅导

## 🎯 目标

> 使用 GROW 模型和教练式提问，帮助他人明确目标、探索方案、制定行动计划。

**核心价值**：教练不给答案，而是帮助他人自己找到答案。这比直接指导更持久有效。

**适用场景**：
- 员工发展辅导
- 职业规划辅导
- 绩效改进辅导
- 领导力发展
- 个人成长辅导

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `coachee_context` | `string` | ✅ | — | 被辅导者情况 |
| `coaching_goal` | `string` | ✅ | — | 辅导目标 |
| `session_type` | `enum` | ❌ | `development` | `development` / `performance` / `career` / `personal` |
| `relationship` | `enum` | ❌ | `manager` | `manager` / `peer` / `external` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话辅导建议",
  "coaching_id": "CO-YYYY-MMDD-NNN",

  "coachee_assessment": {
    "current_situation": "string",
    "readiness_level": "low|medium|high",
    "learning_style": "string",
    "potential_blockers": ["string"]
  },

  "grow_session_plan": {
    "goal": {
      "desired_outcome": "string",
      "specific_goals": ["string"],
      "success_criteria": "string",
      "timeframe": "string"
    },
    "reality": {
      "current_state": "string",
      "obstacles": ["string"],
      "resources_available": ["string"],
      "previous_attempts": ["string"]
    },
    "options": {
      "possible_actions": ["string"],
      "pros_and_cons": {
        "action1": {"pros": ["string"], "cons": ["string"]},
        "action2": {"pros": ["string"], "cons": ["string"]}
      },
      "best_option": "string"
    },
    "will": {
      "commitment_level": "low|medium|high",
      "first_step": "string",
      "timeline": "string",
      "support_needed": ["string"],
      "accountability": "string"
    }
  },

  "coaching_questions": {
    "goal_setting": ["string"],
    "reality_check": ["string"],
    "option_exploration": ["string"],
    "commitment": ["string"]
  },

  "coaching_techniques": [
    {
      "technique": "string",
      "description": "string",
      "when_to_use": "string"
    }
  ],

  "session_structure": {
    "opening": "string",
    "main_body": "string",
    "closing": "string",
    "duration": "string"
  },

  "follow_up_plan": {
    "check_in_schedule": "string",
    "progress_metrics": ["string"],
    "adjustment_triggers": ["string"]
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

### Step 1: 被辅导者评估

- **输入**：`coachee_context`
- **动作**：
  1. 了解当前情况
  2. 评估准备度
  3. 识别潜在障碍
- **输出**：`coachee_assessment`

### Step 2: GROW 模型应用

- **输入**：`coaching_goal` + `coachee_assessment`
- **动作**：
  1. 明确目标（Goal）
  2. 探索现实（Reality）
  3. 探索选项（Options）
  4. 确定意愿（Will）
- **输出**：`grow_session_plan`
- **GROW 模型详解**：

| 阶段 | 核心问题 | 目的 |
|------|----------|------|
| Goal | 你想要什么？ | 明确目标 |
| Reality | 现在的情况是什么？ | 了解现状 |
| Options | 你有哪些选择？ | 探索方案 |
| Will | 你打算怎么做？ | 承诺行动 |

### Step 3: 教练式提问设计

- **输入**：`grow_session_plan`
- **动作**：
  1. 设计目标设定问题
  2. 设计现实探索问题
  3. 设计选项探索问题
  4. 设计承诺确认问题
- **输出**：`coaching_questions`
- **教练式提问原则**：

| 原则 | 描述 | 示例 |
|------|------|------|
| 开放式 | 避免是/否问题 | "你怎么看？" |
| 聚焦式 | 针对具体话题 | "关于X，你..." |
| 前进式 | 关注未来 | "接下来你会...?" |
| 力量式 | 发掘资源 | "你有哪些优势？" |

### Step 4: 教练技巧应用

- **输入**：`coachee_assessment` + `grow_session_plan`
- **动作**：
  1. 选择适合的技巧
  2. 应用到对话中
  3. 调整教练风格
- **输出**：`coaching_techniques`
- **教练技巧库**：

| 技巧 | 描述 | 适用场景 |
|------|------|----------|
| 积极倾听 | 全神贯注听对方说 | 全程 |
| 反映情感 | 反映对方的情绪 | 情绪高涨时 |
| 沉默 | 给对方思考空间 | 深度思考时 |
| 澄清 | 确保理解正确 | 信息模糊时 |
| 总结 | 总结关键点 | 阶段转换时 |
| 挑战 | 质疑假设 | 思维受限时 |

### Step 5: 会话结构设计

- **输入**：`grow_session_plan`
- **动作**：
  1. 设计开场
  2. 安排主体
  3. 设计结尾
- **输出**：`session_structure`

### Step 6: 跟进计划

- **输入**：`grow_session_plan`
- **动作**：
  1. 制定跟进时间表
  2. 设定进度指标
  3. 识别调整触发点
- **输出**：`follow_up_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**直接给出答案（除非被问到）
2. **不得**评判或批评
3. **必须**保持中立和支持性

### 软性约束（建议遵守）
1. 建议 70% 时间用于提问，30% 用于陈述
2. 建议每次辅导有明确的产出
3. 建议定期评估辅导效果

### 人工兜底点
- 当被辅导者出现严重心理问题时，**必须**建议专业帮助
- 当涉及敏感话题时，**必须**谨慎处理

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `CO_WARNING_DEFENSIVE` | 被辅导者防御 | 建立信任 | 🟡 |
| `CO_WARNING_STUCK` | 对话陷入僵局 | 换个角度提问 | 🟡 |
| `CO_ERROR_CRISIS` | 心理危机 | 建议专业帮助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] GROW 模型已应用
- [ ] 教练式问题已设计
- [ ] 行动计划已制定
- [ ] 跟进计划已制定

### OVP 验证信号
- 辅导满意度 ≥ 85%
- 被辅导者目标达成率 ≥ 70%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "职业发展辅导",
    "prompt": "辅导一个想转管理岗的高级工程师",
    "context": "session_type=career, coachee_context=高级工程师5年经验",
    "assertions": [
      "grow_session_plan.goal 包含 具体目标",
      "grow_session_plan.options 包含 多种选择",
      "coaching_questions 包含 职业规划问题"
    ],
    "expected_behavior": "使用GROW模型辅导职业发展",
    "critic_attack": "是否充分探索了被辅导者的真实意愿？"
  },
  {
    "id": "test-002",
    "name": "绩效改进辅导",
    "prompt": "辅导一个绩效下滑的员工",
    "context": "session_type=performance, coachee_context=绩效下滑",
    "assertions": [
      "grow_session_plan.reality.obstacles 已识别",
      "grow_session_plan.will.first_step 已明确",
      "coaching_techniques 包含 挑战技巧"
    ],
    "expected_behavior": "以教练方式帮助改进绩效",
    "critic_attack": "是否在支持和挑战之间平衡？"
  },
  {
    "id": "test-003",
    "name": "领导力辅导",
    "prompt": "辅导一个新晋经理提升领导力",
    "context": "session_type=development, coachee_context=新晋经理",
    "assertions": [
      "grow_session_plan.goal.specific_goals 至少 2 个",
      "coaching_questions 包含 自我认知问题",
      "follow_up_plan.check_in_schedule 已制定"
    ],
    "expected_behavior": "帮助新经理发展领导力",
    "critic_attack": "是否考虑了新经理的特殊挑战？"
  }
]
```

---

## 🔗 关联文档

- [[团队激励]] — 团队管理
- [[冲突管理]] — 冲突解决
- [[决策领导力]] — 决策能力
- [[非暴力沟通]] — 沟通技巧
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：GROW模型 + 教练技巧 + 会话设计 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务] for [业务阶段], with [资源约束], leaning toward [策略框架/执行路径]."

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
| ""先做再说"" | "方向错了，执行力越强死得越快" |
| ""用户说想要这个"" | "用户说的是解决方案，不是需求本身" |
| ""竞品都在做"" | "竞品犯错不意味着你也应该犯" |
| ""这个市场很大"" | "大市场≠你能切到的市场" |

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


**相关概念**：[[管理者是园丁而非监工]] · [[心理安全]] · [[仆人式领导]]

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
