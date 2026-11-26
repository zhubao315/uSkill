---
name: uskill-finance-financial-health
description: "让财务健康变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-finance-financial-health.md"
  original_id: "SKL-6882"
  version: "3.0.0"
  trust: untrusted
---

# 财务健康

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

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
