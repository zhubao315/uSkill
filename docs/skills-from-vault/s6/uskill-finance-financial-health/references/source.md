
description: |
  当用户需要管理个人财务、制定预算、偿还债务、建立储蓄习惯时使用此 Skill。
  触发词包括：'财务健康'、'预算'、'储蓄'、'债务'、'理财'、
  '个人财务'。当用户讨论金钱管理、财务规划时，
  即使未直接说"财务健康"，也应使用此 Skill。
  不适用于复杂投资策略（使用投资 Skill）。遇到个人财务管理时优先使用。

---

# uSkill-901: 财务健康

## 🎯 目标

> 帮助用户建立健康的财务习惯，实现财务稳定和增长。

**核心价值**：财务健康是人生其他方面的基础。好的财务管理能减少压力、增加自由。

**适用场景**：
- 预算制定
- 债务管理
- 储蓄规划
- 应急基金建立
- 财务目标设定

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `financial_situation` | `object` | ✅ | — | 财务状况描述 |
| `financial_goals` | `array` | ✅ | — | 财务目标 |
| `income_stability` | `enum` | ❌ | `stable` | `stable` / `variable` / `uncertain` |
| `risk_tolerance` | `enum` | ❌ | `moderate` | `conservative` / `moderate` / `aggressive` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话财务建议",
  "financial_id": "FH-YYYY-MMDD-NNN",

  "financial_assessment": {
    "current_state": {
      "total_income": "number",
      "total_expenses": "number",
      "net_cash_flow": "number",
      "total_debt": "number",
      "total_savings": "number",
      "net_worth": "number"
    },
    "health_score": "number — 0-100",
    "key_metrics": {
      "savings_rate": "number",
      "debt_to_income": "number",
      "emergency_fund_months": "number",
      "expense_ratio": "number"
    },
    "strengths": ["string"],
    "areas_for_improvement": ["string"]
  },

  "budget_plan": {
    "framework": "50_30_20|zero_based|envelope",
    "allocation": {
      "needs": {
        "percentage": "number",
        "categories": ["string"],
        "amount": "number"
      },
      "wants": {
        "percentage": "number",
        "categories": ["string"],
        "amount": "number"
      },
      "savings": {
        "percentage": "number",
        "categories": ["string"],
        "amount": "number"
      }
    },
    "monthly_budget": [
      {
        "category": "string",
        "budgeted": "number",
        "actual": "number",
        "variance": "number"
      }
    ]
  },

  "debt_management": {
    "total_debt": "number",
    "debt_breakdown": [
      {
        "type": "string",
        "amount": "number",
        "interest_rate": "number",
        "minimum_payment": "number",
        "payoff_strategy": "avalanche|snowball"
      }
    ],
    "payoff_timeline": "string",
    "total_interest_saved": "number"
  },

  "savings_plan": {
    "emergency_fund": {
      "target_amount": "number",
      "current_amount": "number",
      "monthly_contribution": "number",
      "timeline_to_target": "string"
    },
    "short_term_savings": [
      {
        "goal": "string",
        "target_amount": "number",
        "monthly_contribution": "number",
        "timeline": "string"
      }
    ],
    "long_term_savings": {
      "retirement": "string",
      "investment_strategy": "string"
    }
  },

  "action_plan": {
    "immediate_actions": ["string"],
    "this_month": ["string"],
    "this_quarter": ["string"],
    "this_year": ["string"]
  },

  "monitoring_system": {
    "daily_tracking": ["string"],
    "weekly_reviews": ["string"],
    "monthly_checkpoints": ["string"],
    "annual_reviews": ["string"]
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

### Step 1: 财务评估

- **输入**：`financial_situation`
- **动作**：
  1. 计算收支情况
  2. 评估资产负债
  3. 计算关键指标
- **输出**：`financial_assessment`
- **财务健康指标**：

| 指标 | 健康标准 | 说明 |
|------|----------|------|
| 储蓄率 | ≥20% | 收入储蓄比例 |
| 债务收入比 | <36% | 月供/月收入 |
| 应急基金 | 3-6个月 | 应对突发情况 |
| 流动性比率 | >1 | 流动资产/月支出 |

### Step 2: 预算制定

- **输入**：`financial_assessment`
- **动作**：
  1. 选择预算框架
  2. 分配预算比例
  3. 设计月度预算
- **输出**：`budget_plan`
- **50/30/20 预算法则**：

| 类别 | 比例 | 内容 |
|------|:----:|------|
| 需求 | 50% | 住房、食物、交通 |
| 欲望 | 30% | 娱乐、外出、购物 |
| 储蓄 | 20% | 应急、投资、还债 |

### Step 3: 债务管理

- **输入**：`financial_situation.debts`
- **动作**：
  1. 分析债务结构
  2. 选择还款策略
  3. 制定还款计划
- **输出**：`debt_management`
- **债务还款策略**：

| 策略 | 描述 | 优点 |
|------|------|------|
| 雪崩法 | 先还高利率 | 节省利息 |
| 雪球法 | 先还小额 | 心理激励 |

### Step 4: 储蓄规划

- **输入**：`financial_goals`
- **动作**：
  1. 设计应急基金
  2. 规划短期储蓄
  3. 规划长期储蓄
- **输出**：`savings_plan`

### Step 5: 行动计划

- **输入**：所有前序输出
- **动作**：
  1. 制定立即行动
  2. 制定月度计划
  3. 制定年度计划
- **输出**：`action_plan`

### Step 6: 监控系统

- **输入**：`budget_plan`
- **动作**：
  1. 设计日常跟踪
  2. 安排周度回顾
  3. 设定月度检查点
- **输出**：`monitoring_system`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议超出能力的投资
2. **不得**忽视应急基金
3. **必须**考虑个人情况

### 软性约束（建议遵守）
1. 建议从记账开始
2. 建议自动化储蓄
3. 建议定期回顾调整

### 人工兜底点
- 当债务严重时，**必须**建议专业咨询
- 当财务状况复杂时，**必须**建议财务规划师

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `FH_WARNING_LOW_SAVINGS` | 储蓄率低 | 建议增加储蓄 | 🟡 |
| `FH_WARNING_HIGH_DEBT` | 债务过高 | 建议还债优先 | 🟡 |
| `FH_ERROR_CRISIS` | 财务危机 | 建议专业帮助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 财务评估完成
- [ ] 预算已制定
- [ ] 债务管理计划已制定
- [ ] 储蓄计划已制定

### OVP 验证信号
- 财务健康评分 ≥ 80/100
- 储蓄率 ≥ 20%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "月光族理财",
    "prompt": "我是月光族，如何开始理财",
    "context": "financial_situation={income:10000, expenses:10000, savings:0}",
    "assertions": [
      "financial_assessment.health_score < 50",
      "budget_plan.framework 已选择",
      "action_plan.immediate_actions 至少 3 个"
    ],
    "expected_behavior": "帮助月光族开始理财",
    "critic_attack": "建议是否足够简单易行？"
  },
  {
    "id": "test-002",
    "name": "债务管理",
    "prompt": "我有信用卡债务，如何偿还",
    "context": "financial_situation={debts:[{type:信用卡, amount:50000, rate:18%}]}",
    "assertions": [
      "debt_management.debt_breakdown 已分析",
      "debt_management.payoff_strategy 已选择",
      "debt_management.payoff_timeline 已计算"
    ],
    "expected_behavior": "制定债务偿还计划",
    "critic_attack": "是否考虑了最低还款额？"
  },
  {
    "id": "test-003",
    "name": "应急基金",
    "prompt": "如何建立应急基金",
    "context": "financial_goals=[建立应急基金]",
    "assertions": [
      "savings_plan.emergency_fund.target_amount 已计算",
      "savings_plan.emergency_fund.monthly_contribution 已设定",
      "savings_plan.emergency_fund.timeline_to_target 已给出"
    ],
    "expected_behavior": "设计应急基金计划",
    "critic_attack": "目标金额是否合理？"
  }
]
```

---

## 🔗 关联文档

- [[估值分析]] — 投资分析
- [[提示词-营销-GEO合规风险管理]] — 风险控制
- [[现金流四象限分析]] — 现金流管理
- [[uSkill-投资组合监控-v1]] — 投资监控
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：财务评估 + 预算 + 债务管理 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [投资决策类型] for [投资者风格], with [风险偏好], leaning toward [分析框架/数据源]."

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
| ""这次不一样"" | "每次泡沫都说这次不一样，这次也一样" |
| ""先满仓再说"" | "满仓=零容错，一个回调就是灾难" |
| ""跌了就补仓"" | "越补越套是亏损扩大的主因" |
| ""长期持有就行"" | "长期持有不等于不做仓位管理" |
| ""这次消息是利好"" | "消息面驱动的交易成功率低于掷硬币" |

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
