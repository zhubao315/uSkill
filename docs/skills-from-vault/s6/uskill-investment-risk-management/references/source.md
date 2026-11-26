
description: |
  当用户需要管理投资风险、设计对冲策略、进行仓位管理、评估尾部风险时使用此 Skill。
  触发词包括：'风险管理'、'对冲'、'仓位管理'、'止损'、'尾部风险'、
  '风险控制'。当用户讨论投资组合、资产配置、风险控制时，
  即使未直接说"风险管理"，也应使用此 Skill。
  不适用于无风险资产（使用其他 Skill）。遇到投资风险管理时优先使用。

---

# uSkill-504: 风险管理

## 🎯 目标

> 识别、评估和管理投资风险，设计对冲策略，优化风险调整后收益。

**核心价值**：风险管理不是消除风险，而是确保承担的风险有相应的回报。

**适用场景**：
- 投资组合风险管理
- 个股风险控制
- 资产配置优化
- 尾部风险对冲
- 仓位管理

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `portfolio` | `object` | ✅ | — | 投资组合描述 |
| `risk_tolerance` | `enum` | ❌ | `moderate` | `conservative` / `moderate` / `aggressive` |
| `time_horizon` | `enum` | ❌ | `medium` | `short` / `medium` / `long` |
| `risk_focus` | `array` | ❌ | `all` | 关注的风险类型 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话风险管理建议",
  "risk_id": "RM-YYYY-MMDD-NNN",

  "risk_assessment": {
    "portfolio_risks": [
      {
        "risk_type": "market|credit|liquidity|concentration|currency",
        "description": "string",
        "probability": "low|medium|high",
        "impact": "low|medium|high",
        "current_exposure": "string"
      }
    ],
    "overall_risk_level": "low|medium|high",
    "risk_score": "number — 0-100"
  },

  "position_management": {
    "current_positions": [
      {
        "asset": "string",
        "weight": "number",
        "risk_contribution": "number",
        "rebalance_suggestion": "string"
      }
    ],
    "optimal_allocation": {
      "equities": "number",
      "fixed_income": "number",
      "alternatives": "number",
      "cash": "number"
    },
    "rebalance_frequency": "string"
  },

  "hedging_strategies": [
    {
      "strategy": "string",
      "instruments": ["string"],
      "cost": "number",
      "effectiveness": "high|medium|low",
      "implementation": "string"
    }
  ],

  "stop_loss_framework": {
    "individual_positions": {
      "method": "percentage|trailing|technical",
      "parameters": "string"
    },
    "portfolio_level": {
      "drawdown_limit": "number",
      "recovery_criteria": "string"
    }
  },

  "tail_risk_protection": {
    "scenarios": [
      {
        "scenario": "string",
        "probability": "number",
        "impact": "string",
        "protection_method": "string"
      }
    ],
    "insurance_strategies": ["string"]
  },

  "monitoring_system": {
    "daily_metrics": ["string"],
    "weekly_reviews": ["string"],
    "alert_thresholds": {
      "volatility": "number",
      "drawdown": "number",
      "correlation": "number"
    }
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

### Step 1: 风险评估

- **输入**：`portfolio`
- **动作**：
  1. 识别投资组合风险
  2. 评估每种风险的概率和影响
  3. 计算总体风险水平
- **输出**：`risk_assessment`
- **投资风险类型**：

| 风险类型 | 描述 | 来源 |
|----------|------|------|
| 市场风险 | 市场整体下跌 | 宏观经济 |
| 信用风险 | 违约风险 | 发行方 |
| 流动性风险 | 无法及时变现 | 市场深度 |
| 集中度风险 | 过度集中 | 组合结构 |
| 汇率风险 | 汇率波动 | 外币资产 |

### Step 2: 仓位管理

- **输入**：`risk_assessment` + `risk_tolerance`
- **动作**：
  1. 分析当前仓位
  2. 计算风险贡献
  3. 设计最优配置
- **输出**：`position_management`
- **资产配置指南**：

| 风险偏好 | 股票 | 债券 | 另类 | 现金 |
|----------|:----:|:----:|:----:|:----:|
| 保守型 | 30% | 50% | 10% | 10% |
| 稳健型 | 50% | 30% | 15% | 5% |
| 激进型 | 70% | 15% | 10% | 5% |

### Step 3: 对冲策略

- **输入**：`risk_assessment`
- **动作**：
  1. 设计对冲策略
  2. 选择对冲工具
  3. 评估成本和效果
- **输出**：`hedging_strategies`
- **常见对冲工具**：

| 工具 | 用途 | 成本 |
|------|------|------|
| 期权 | 保护下跌 | 期权费 |
| 期货 | 系统性对冲 | 保证金 |
| 反向ETF | 做空市场 | 管理费 |
| 分散化 | 降低集中度 | 机会成本 |

### Step 4: 止损框架

- **输入**：`risk_tolerance` + `time_horizon`
- **动作**：
  1. 设计个股止损规则
  2. 设计组合止损规则
  3. 设计恢复标准
- **输出**：`stop_loss_framework`

### Step 5: 尾部风险保护

- **输入**：`risk_assessment`
- **动作**：
  1. 识别极端场景
  2. 评估潜在影响
  3. 设计保护策略
- **输出**：`tail_risk_protection`

### Step 6: 监控系统

- **输入**：所有前序输出
- **动作**：
  1. 设计监控指标
  2. 设定警报阈值
  3. 制定回顾计划
- **输出**：`monitoring_system`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视尾部风险
2. **不得**过度杠杆
3. **必须**保持流动性

### 软性约束（建议遵守）
1. 建议定期再平衡
2. 建议保持纪律
3. 建议记录所有交易

### 人工兜底点
- 当市场剧烈波动时，**必须**建议冷静
- 当风险超出容忍时，**必须**建议减仓

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `RM_WARNING_HIGH_VOL` | 波动率上升 | 建议降低仓位 | 🟡 |
| `RM_WARNING_DRAWDOWN` | 回撤接近限制 | 建议止损 | 🟡 |
| `RM_ERROR_LIQUIDITY` | 流动性危机 | 建议持有现金 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 风险已评估
- [ ] 仓位管理已设计
- [ ] 对冲策略已制定
- [ ] 监控系统已建立

### OVP 验证信号
- 最大回撤 < 设定阈值
- 夏普比率 ≥ 1.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "股票组合风险管理",
    "prompt": "管理一个100万的股票投资组合",
    "context": "portfolio={stocks: 100万}, risk_tolerance=moderate",
    "assertions": [
      "risk_assessment.portfolio_risks 至少 3 种风险",
      "position_management.optimal_allocation 已设计",
      "stop_loss_framework 已制定"
    ],
    "expected_behavior": "全面管理股票组合风险",
    "critic_attack": "是否考虑了市场系统性风险？"
  },
  {
    "id": "test-002",
    "name": "极端市场保护",
    "prompt": "如何保护投资组合免受极端下跌",
    "context": "risk_focus=[tail_risk]",
    "assertions": [
      "tail_risk_protection.scenarios 至少 2 个极端场景",
      "hedging_strategies 包含 期权保护",
      "monitoring_system.alert_thresholds 已设定"
    ],
    "expected_behavior": "设计尾部风险保护策略",
    "critic_attack": "对冲成本是否过高？"
  },
  {
    "id": "test-003",
    "name": "资产配置优化",
    "prompt": "优化我的资产配置以降低风险",
    "context": "risk_tolerance=conservative, time_horizon=long",
    "assertions": [
      "position_management.current_positions 包含 分析",
      "position_management.optimal_allocation 符合保守型",
      "hedging_strategies 包含 分散化"
    ],
    "expected_behavior": "优化资产配置降低风险",
    "critic_attack": "是否考虑了税收影响？"
  }
]
```

---

## 🔗 关联文档

- [[估值分析]] — 估值方法
- [[决策推理-Schema]] — 决策框架
- [[uSkill-日程优化-v1]] — 概率决策
- [[杠铃策略实施协议]] — 杠铃策略
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：风险评估 + 仓位管理 + 对冲策略 + Self-Play |

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
