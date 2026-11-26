
description: |
  当用户需要在不确定性中做决策、平衡多方利益、快速果断决策、承担决策责任时使用此 Skill。
  触发词包括：'领导力决策'、'管理决策'、'战略决策'、'团队决策'、
  '快速决策'、'果断决策'。当用户讨论团队管理、组织决策、战略选择时，
  即使未直接说"决策领导力"，也应使用此 Skill。
  不适用于个人决策（使用决策推理 Skill）。遇到团队或组织决策时优先使用。

---

# uSkill-401: 决策领导力

## 🎯 目标

> 帮助领导者在不确定性中做出高质量决策，平衡速度与质量，承担决策责任。

**核心价值**：领导力的核心是决策力。好的领导者能在信息不完整时做出正确判断。

**适用场景**：
- 战略方向选择
- 资源分配决策
- 人事任免决策
- 危机应对决策
- 创新项目决策

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `decision_context` | `string` | ✅ | — | 决策背景描述 |
| `stakeholders` | `array` | ✅ | — | 利益相关者列表 |
| `time_pressure` | `enum` | ❌ | `medium` | `low` / `medium` / `high` / `critical` |
| `information_completeness` | `number` | ❌ | `0.7` | 信息完整度 0-1 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话决策建议",
  "leadership_id": "LD-YYYY-MMDD-NNN",

  "decision_framework": {
    "framework_used": "string",
    "rationale": "string"
  },

  "stakeholder_analysis": [
    {
      "stakeholder": "string",
      "interest": "high|medium|low",
      "influence": "high|medium|low",
      "position": "support|neutral|oppose",
      "engagement_strategy": "string"
    }
  ],

  "options_analysis": [
    {
      "option": "string",
      "pros": ["string"],
      "cons": ["string"],
      "risks": ["string"],
      "resource_requirements": "string",
      "alignment_with_values": "high|medium|low"
    }
  ],

  "decision_output": {
    "recommended_option": "string",
    "decision_rationale": "string",
    "confidence_level": "number",
    "conditions_for_reversal": ["string"]
  },

  "implementation_plan": {
    "immediate_actions": ["string"],
    "communication_plan": ["string"],
    "monitoring_metrics": ["string"],
    "check_in_schedule": "string"
  },

  "risk_mitigation": {
    "identified_risks": ["string"],
    "mitigation_strategies": ["string"],
    "contingency_plans": ["string"]
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

### Step 1: 决策框架选择

- **输入**：`decision_context` + `time_pressure`
- **动作**：
  1. 评估决策类型
  2. 选择合适的决策框架
  3. 确定决策标准
- **输出**：`decision_framework`
- **决策框架选择**：

| 情境 | 框架 | 适用条件 |
|------|------|----------|
| 时间充裕 | 贝叶斯决策 | 信息可量化 |
| 时间紧迫 | 直觉+验证 | 需要快速决策 |
| 利益冲突 | 协作决策 | 多方参与 |
| 高风险 | 预验尸法 | 需要识别风险 |

### Step 2: 利益相关者分析

- **输入**：`stakeholders`
- **动作**：
  1. 识别所有利益相关者
  2. 评估其利益和影响力
  3. 制定参与策略
- **输出**：`stakeholder_analysis`
- **利益相关者矩阵**：

| | 高影响力 | 低影响力 |
|---|:---:|:---:|
| **高利益** | 密切合作 | 保持知情 |
| **低利益** | 满足需求 | 监控即可 |

### Step 3: 选项分析

- **输入**：`decision_framework`
- **动作**：
  1. 生成至少 3 个选项
  2. 评估每个选项的优劣
  3. 评估风险和资源需求
- **输出**：`options_analysis`

### Step 4: 决策输出

- **输入**：`options_analysis` + `stakeholder_analysis`
- **动作**：
  1. 综合评估
  2. 做出推荐
  3. 明确决策依据
- **输出**：`decision_output`

### Step 5: 实施计划

- **输入**：`decision_output`
- **动作**：
  1. 制定立即行动清单
  2. 制定沟通计划
  3. 设定监控指标
- **输出**：`implementation_plan`

### Step 6: 风险缓解

- **输入**：`options_analysis`
- **动作**：
  1. 识别潜在风险
  2. 制定缓解策略
  3. 准备应急计划
- **输出**：`risk_mitigation`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在信息严重不足时强行决策
2. **不得**忽视主要利益相关者
3. **必须**明确决策依据和可逆条件

### 软性约束（建议遵守）
1. 建议在决策前征求至少 2 个不同意见
2. 建议设定决策回顾时间点
3. 建议记录决策过程以便复盘

### 人工兜底点
- 当涉及重大战略决策时，**必须**建议董事会或顾问参与
- 当决策可能导致重大损失时，**必须**建议压力测试

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `LD_WARNING_LOW_INFO` | 信息完整度 < 50% | 建议收集更多信息 | 🟡 |
| `LD_WARNING_CONFLICT` | 利益相关者严重冲突 | 建议协调或升级 | 🟡 |
| `LD_ERROR_CRITICAL` | 关键决策 + 高风险 | 建议外部咨询 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 决策框架已选择
- [ ] 利益相关者已分析
- [ ] 选项已生成并评估
- [ ] 实施计划已制定

### OVP 验证信号
- 决策质量评分 ≥ 80/100
- 利益相关者满意度 ≥ 75%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "战略方向选择",
    "prompt": "我们是应该进入新市场还是深耕现有市场？",
    "context": "stakeholders=[股东、员工、客户], time_pressure=medium",
    "assertions": [
      "decision_framework 已选择",
      "stakeholder_analysis 包含 所有利益相关者",
      "options_analysis 至少 2 个选项"
    ],
    "expected_behavior": "提供结构化的战略决策分析",
    "critic_attack": "是否考虑了所有利益相关者？"
  },
  {
    "id": "test-002",
    "name": "危机决策",
    "prompt": "竞争对手突然降价20%，我们需要在24小时内做出反应",
    "context": "stakeholders=[管理层、销售团队], time_pressure=critical",
    "assertions": [
      "decision_framework.framework_used = 快速决策框架",
      "implementation_plan.immediate_actions 已列出",
      "risk_mitigation 已生成"
    ],
    "expected_behavior": "在时间压力下提供快速决策建议",
    "critic_attack": "是否在速度和质量之间平衡？"
  },
  {
    "id": "test-003",
    "name": "人事决策",
    "prompt": "我需要决定是否提拔一个业绩好但团队关系差的员工",
    "context": "stakeholders=[该员工、团队、HR], time_pressure=low",
    "assertions": [
      "stakeholder_analysis 包含 所有相关方",
      "options_analysis 包含 多种方案",
      "decision_output.conditions_for_reversal 已列出"
    ],
    "expected_behavior": "平衡业绩和团队关系的决策分析",
    "critic_attack": "是否充分考虑了团队影响？"
  }
]
```

---

## 🔗 关联文档

- [[决策推理-Schema]] — 决策推理框架
- [[团队激励]] — 团队管理
- [[冲突管理]] — 冲突解决
- 战略思维 — 战略规划
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：决策框架 + 利益相关者分析 + 实施计划 + Self-Play |

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


**相关概念**：[[决策模型]] · [[70%信息即可决策]]

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
