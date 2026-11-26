---
name: uskill-investment-risk-management
description: "让风险管理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-risk-management.md"
  original_id: "SKL-5504"
  version: "3.0.0"
  trust: untrusted
---

# 风险管理

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
3. **必须**保

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
