---
name: uskill-investment-industry-analysis
description: "让行业分析变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-industry-analysis.md"
  original_id: "SKL-5503"
  version: "3.0.0"
  trust: untrusted
---

# 行业分析

description: |
  当用户需要分析行业结构、评估竞争格局、识别行业趋势、进行行业比较时使用此 Skill。
  触发词包括：'行业分析'、'竞争格局'、'波特五力'、'行业趋势'、'市场分析'、
  '行业研究'。当用户讨论投资、战略、市场研究时，
  即使未直接说"行业分析"，也应使用此 Skill。
  不适用于公司层面分析（使用财报解读）。遇到行业层面分析时优先使用。

---

# uSkill-503: 行业分析

## 🎯 目标

> 使用波特五力、价值链、生命周期等框架，全面分析行业结构和竞争动态。

**核心价值**：行业结构决定竞争规则。理解行业是投资和战略的基础。

**适用场景**：
- 投资行业选择
- 竞争战略制定
- 市场进入决策
- 并购目标筛选
- 行业趋势研判

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `industry_name` | `string` | ✅ | — | 行业名称 |
| `analysis_framework` | `array` | ❌ | `all` | 分析框架 |
| `geographic_scope` | `string` | ❌ | `global` | 地理范围 |
| `time_horizon` | `number` | ❌ | `5` | 预测时间范围（年） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话行业分析结论",
  "industry_id": "IA-YYYY-MMDD-NNN",

  "industry_overview": {
    "definition": "string",
    "market_size": "string",
    "growth_rate": "number",
    "key_drivers": ["string"],
    "industry_lifecycle_stage": "introduction|growth|maturity|decline"
  },

  "porter_five_forces": {
    "threat_of_new_entrants": {
      "level": "low|medium|high",
      "barriers": ["string"],
      "factors": ["string"]
    },
    "threat_of_substitutes": {
      "level": "low|medium|high",
      "substitutes": ["string"],
      "switching_costs": "string"
    },
    "bargaining_power_of_buyers": {
      "level": "low|medium|high",
      "factors": ["string"]
    },
    "bargaining_power_of_suppliers": {
      "level": "low|medium|high",
      "factors": ["string"]
    },
    "competitive_rivalry": {
      "level": "low|medium|high",
      "competitors": ["string"],
      "competition_factors": ["string"]
    },
    "overall_attractiveness": "low|medium|high"
  },

  "value_chain_analysis": {
    "primary_activities": [
      {
        "activity": "string",
        "importance": "high|medium|low",
        "key_players": ["string"]
      }
    ],
    "support_activities": ["string"],
    "value_creation_opportunities": ["string"]
  },

  "competitive_landscape": {
    "market_structure": "perfect_competition|monopolistic|oligopoly|monopoly",
    "key_players": [
      {
        "name": "string",
        "market_share": "number",
        "competitive_advantage": "string",
        "strategy": "string"
      }
    ],
    "competitive_dynamics": "string"
  },

  "trend_analysis": {
    "technological_trends": ["string"],
    "regulatory_trends": ["string"],
    "consumer_trends": ["string"],
    "economic_trends": ["string"],
    "impact_assessment": "string"
  },

  "opportunities_and_threats": {
    "opportunities": [
      {
        "opportunity": "string",
        "probability": "high|medium|low",
        "impact": "high|medium|low"
      }
    ],
    "threats": [
      {
        "threat": "string",
        "probability": "high|medium|low",
        "impact": "high|medium|low"
      }
    ]
  },

  "investment_implications": {
    "best_segments": ["string"],
    "avoid_segments": ["string"],
    "key_success_factors": ["string"],
    "risks": ["string"]
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

### Step 1: 行业概况

- **输入**：`industry_name`
- **动作**：
  1. 定义行业边界
  2. 评估市场规模
  3. 识别增长驱动因素
- **输出**：`industry_overview`
- **行业生命周期**：

| 阶段 | 特征 | 投资策略 |
|------|------|----------|
| 导入期 | 高增长、高风险 | 选择性投资 |
| 成长期 | 快速增长、竞争加剧 | 龙头公司 |
| 成熟期 | 增长放缓、利润稳定 | 价值投资 |
| 衰退期 | 增长停滞、利润下降 | 避免或做空 |

### Step 2: 波特五力分析

- **输入**：`industry_name`
- **动作**：
  1. 评估新进入者威胁
  2. 评估替代品威胁
  3. 评估买方议价能力
  4. 评估供应商议价能力
  5. 评估竞争强度
- **输出**：`porter_five_forces`
- **进入壁垒类型**：

| 壁垒 | 描述 | 示例 |
|------|------|------|
| 规模经济 | 大规模生产成本优势 | 制造业 |
| 资本需求 | 需要大量投资 | 芯片制造 |
| 转换成本 | 客户转换成本高 | 企业软件 |
| 品牌忠诚 | 客户品牌偏好 | 消费品 |
| 政策壁垒 | 政府法规限制 | 金融、医疗 |

### Step 3: 价值链分析

- **输入**：`industry_name`
- **动作**：
  1. 识别主要活动
  2. 识别支持活动
  3. 发现价值创造机会
- **输出**：`value_chain_analysis`

### Step 4: 竞争格局

- **输入**：`industry_name`
- **动作**：
  1. 评估市场结构
  2. 分析主要竞争者
  3. 评估竞争动态

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
