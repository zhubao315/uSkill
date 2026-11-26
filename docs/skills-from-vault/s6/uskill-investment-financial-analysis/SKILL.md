---
name: uskill-investment-financial-analysis
description: "让财报解读变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-financial-analysis.md"
  original_id: "SKL-5502"
  version: "3.0.0"
  trust: untrusted
---

# 财报解读

description: |
  当用户需要解读财务报表、分析公司财务健康、识别财务风险、评估投资价值时使用此 Skill。
  触发词包括：'财报'、'财务分析'、'资产负债表'、'利润表'、'现金流量表'、
  '财务比率'、'财务健康'。当用户讨论投资分析、股票研究、公司评估时，
  即使未直接说"财报解读"，也应使用此 Skill。
  不适用于技术分析（使用其他 Skill）。遇到基本面财务分析时优先使用。

---

# uSkill-502: 财报解读

## 🎯 目标

> 系统化解读三大财务报表，识别关键财务指标，发现潜在风险和机会。

**核心价值**：财务报表是公司的"体检报告"。读懂财报是投资的基本功。

**适用场景**：
- 股票投资分析
- 公司财务健康评估
- 并购尽职调查
- 信用风险评估
- 竞争对手分析

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `company_name` | `string` | ✅ | — | 公司名称 |
| `financial_statements` | `object` | ❌ | — | 财务报表数据 |
| `analysis_focus` | `enum` | ❌ | `full` | `profitability` / `liquidity` / `solvency` / `efficiency` / `full` |
| `comparison_period` | `enum` | ❌ | `yoy` | `yoy` / `qoq` / `trend` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话财务分析结论",
  "financial_id": "FA-YYYY-MMDD-NNN",

  "income_statement_analysis": {
    "revenue": {
      "amount": "number",
      "growth_rate": "number",
      "quality": "string"
    },
    "profitability": {
      "gross_margin": "number",
      "operating_margin": "number",
      "net_margin": "number",
      "trend": "improving|stable|declining"
    },
    "red_flags": ["string"]
  },

  "balance_sheet_analysis": {
    "assets": {
      "total_assets": "number",
      "asset_quality": "string",
      "goodwill_ratio": "number"
    },
    "liabilities": {
      "total_liabilities": "number",
      "debt_level": "low|medium|high",
      "debt_structure": "string"
    },
    "equity": {
      "shareholders_equity": "number",
      "retained_earnings": "number",
      "equity_quality": "string"
    }
  },

  "cash_flow_analysis": {
    "operating_cash_flow": "number",
    "investing_cash_flow": "number",
    "financing_cash_flow": "number",
    "free_cash_flow": "number",
    "cash_flow_quality": "string"
  },

  "financial_ratios": {
    "profitability": {
      "roe": "number",
      "roa": "number",
      "roic": "number"
    },
    "liquidity": {
      "current_ratio": "number",
      "quick_ratio": "number"
    },
    "solvency": {
      "debt_to_equity": "number",
      "interest_coverage": "number"
    },
    "efficiency": {
      "asset_turnover": "number",
      "inventory_turnover": "number",
      "receivable_turnover": "number"
    }
  },

  "quality_of_earnings": {
    "accrual_ratio": "number",
    "cash_conversion": "number",
    "recurring_revenue": "number",
    "earnings_quality": "high|medium|low"
  },

  "risk_assessment": {
    "financial_health_score": "number",
    "key_risks": ["string"],
    "warning_signs": ["string"],
    "strengths": ["string"]
  },

  "peer_comparison": {
    "industry_average": {
      "roe": "number",
      "debt_to_equity": "number",
      "margin": "number"
    },
    "relative_position": "above|at|below"
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

### Step 1: 利润表分析

- **输入**：`financial_statements.income_statement`
- **动作**：
  1. 分析收入增长
  2. 评估盈利能力
  3. 识别异常项目
- **输出**：`income_statement_analysis`
- **关键指标**：

| 指标 | 公式 | 说明 |
|------|------|------|
| 毛利率 | (收入-成本)/收入 | 产品盈利能力 |
| 营业利润率 | 营业利润/收入 | 经营效率 |
| 净利率 | 净利润/收入 | 整体盈利 |

### Step 2: 资产负债表分析

- **输入**：`financial_statements.balance_sheet`
- **动作**：
  1. 评估资产质量
  2. 分析负债结构
  3. 评估权益质量
- **输出**：`balance_sheet_analysis`

### Step 3: 现金流量表分析

- **输入**：`financial_statements.cash_flow`
- **动作**：
  1. 分析经营现金流
  2. 评估投资活动
  3. 分析融资活动
- **输出**：`cash_flow_analysis`
- **现金流质量指标**：

| 指标 | 健康标准 | 风险信号 |
|------|----------|----------|
| 经营现金流/净利润 | > 1 | < 0.8 |
| 自由现金流 | 正且增长 | 持续为负 |
| 资本支出/折旧 | 合理比例 | 过高或过低 |

### Step 4: 财务比率计算

- **输入**：所有财务数据
- **动作**：
  1. 计算盈利能力比率
  2. 计算流动性比率
  3. 计算偿债能力比率
  4. 计算效率比率
- **输出**：`financial_ratios`

### Step 5: 盈利质量评估

- **输入**：`income_statement_analysis` + `cash_flow_analysis`
- **动作**：
  1. 计算应计比率
  2. 评估现金转换率
  3. 识别经常性收入
- **输出**：`quality_of_earnings`

### Step 6: 风险评估

- **输入**：所有前序输出


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
