---
name: uskill-investment-valuation-analysis
description: "让估值分析变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-valuation-analysis.md"
  original_id: "SKL-5501"
  version: "3.0.0"
  trust: untrusted
---

# 估值分析

description: |
  当用户需要对公司或资产进行估值分析、选择估值方法、评估投资价值时使用此 Skill。
  触发词包括：'估值'、'DCF'、'PE'、'PB'、'PS'、'估值分析'、'公司估值'、
  '股票估值'。当用户讨论投资分析、股票研究、并购估值时，
  即使未直接说"估值分析"，也应使用此 Skill。
  不适用于技术分析（使用其他 Skill）。遇到基本面估值需求时优先使用。

---

# uSkill-501: 估值分析

## 🎯 目标

> 应用多种估值方法，对公司或资产进行全面估值，识别低估或高估机会。

**核心价值**：估值是投资决策的基础。正确的估值能帮助识别安全边际。

**适用场景**：
- 股票投资分析
- 并购估值
- 创业公司估值
- 房地产估值
- 资产评估

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `target` | `string` | ✅ | — | 待估值公司/资产 |
| `valuation_methods` | `array` | ❌ | `all` | 指定估值方法 |
| `data_sources` | `object` | ❌ | — | 财务数据来源 |
| `time_horizon` | `number` | ❌ | `5` | 预测时间范围（年） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话估值结论",
  "valuation_id": "VA-YYYY-MMDD-NNN",

  "company_overview": {
    "name": "string",
    "industry": "string",
    "competitive_position": "string",
    "key_metrics": {
      "revenue": "number",
      "growth_rate": "number",
      "profit_margin": "number",
      "market_cap": "number"
    }
  },

  "dcf_valuation": {
    "assumptions": {
      "growth_rate": "number",
      "discount_rate": "number",
      "terminal_growth_rate": "number",
      "projection_years": "number"
    },
    "free_cash_flow_projections": [
      {
        "year": "number",
        "fcf": "number",
        "pv": "number"
      }
    ],
    "terminal_value": "number",
    "enterprise_value": "number",
    "equity_value": "number",
    "per_share_value": "number",
    "sensitivity_analysis": {
      "optimistic": "number",
      "base": "number",
      "pessimistic": "number"
    }
  },

  "relative_valuation": {
    "comparable_companies": [
      {
        "name": "string",
        "pe_ratio": "number",
        "pb_ratio": "number",
        "ps_ratio": "number",
        "ev_ebitda": "number"
      }
    ],
    "peer_average": {
      "pe_ratio": "number",
      "pb_ratio": "number",
      "ps_ratio": "number",
      "ev_ebitda": "number"
    },
    "implied_valuation": {
      "pe_based": "number",
      "pb_based": "number",
      "ps_based": "number"
    }
  },

  "asset_valuation": {
    "book_value": "number",
    "tangible_assets": "number",
    "intangible_assets": "number",
    "net_asset_value": "number"
  },

  "valuation_summary": {
    "methods_used": ["string"],
    "value_range": {
      "low": "number",
      "high": "number",
      "midpoint": "number"
    },
    "current_price": "number",
    "margin_of_safety": "number",
    "recommendation": "undervalued|fairly_valued|overvalued"
  },

  "key_assumptions": [
    {
      "assumption": "string",
      "impact": "high|medium|low",
      "sensitivity": "string"
    }
  ],

  "risks_and_caveats": ["string"],

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 公司概况分析

- **输入**：`target`
- **动作**：
  1. 收集公司基本信息
  2. 分析竞争地位
  3. 评估关键财务指标
- **输出**：`company_overview`

### Step 2: DCF 估值

- **输入**：`company_overview` + `data_sources`
- **动作**：
  1. 预测自由现金流
  2. 确定折现率
  3. 计算终值和企业价值
- **输出**：`dcf_valuation`
- **DCF 关键假设**：

| 参数 | 说明 | 典型范围 |
|------|------|----------|
| 增长率 | 未来 FCF 增长 | 2-15% |
| 折现率 | WACC | 8-12% |
| 终值增长率 | 永续增长 | 2-3% |

### Step 3: 相对估值

- **输入**：`company_overview`
- **动作**：
  1. 选择可比公司
  2. 计算估值倍数
  3. 应用倍数估值
- **输出**：`relative_valuation`
- **常用估值倍数**：

| 倍数 | 公式 | 适用场景 |
|------|------|----------|
| PE | 市值/净利润 | 盈利稳定公司 |
| PB | 市值/净资产 | 资产密集型 |
| PS | 市值/营收 | 成长型公司 |
| EV/EBITDA | 企业价值/EBITDA | 资本结构差异大 |

### Step 4: 资产估值

- **输入**：`company_overview` + `data_sources`
- **动作**：
  1. 评估账面价值
  2. 评估有形资产
  3. 评估无形资产
- **输出**：`asset_valuation`

### Step 5: 综合估值

- **输入**：所有前序输出
- **动作**：
  1. 综合多种方法
  2. 确定价值区间
  3. 计算安全边际
- **输出**：`valuation_summary`
- **安全边际计算**：
  ```
  安全边际 = (内在价值 - 市场价格) / 内在价值
  ```

### Step 6: 敏感性分析

- **输入**：`dcf_valuation`
- **动作**：
  1. 测试关键假设变化
  2. 识别价值驱动因素
  3. 评估估值稳健性
- **输出**：`dcf_valuation.sensitivity_analysis`

---

## ⚠️

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
