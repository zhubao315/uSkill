---
name: uskill-cognition-cognitive-analyze-investment-opportunity
description: "让cognitive analyze investment opportunity变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-analyze-investment-opportunity.md"
  original_id: "SKL-6829"
  version: "3.0.0"
  trust: untrusted
---

# cognitive analyze investment opportunity

# Investment Opportunity Analysis

## 🎯 目标
> AI增强的投资机会全流程分析：从广域扫描、深度尽调、估值建模到投决输出，2小时内完成高质量初筛，2天内完成深度分析报告。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `target_info` | string | ✅ | 目标公司信息（BP/公开资料/名称） |
| `analysis_stage` | enum | ✅ | `screening` / `due_diligence` / `valuation` / `ic_memo` |
| `investment_criteria` | object | ❌ | `{sector: "string", stage: "string", min_irr_pct: "number", max_pe: "number"}` — 投资筛选标准 |
| `financial_data` | object | ❌ | `{revenue_series: [], profit_series: [], cashflow_series: [], years: []}` — 三年财务数据 |
| `budget_range` | object | ❌ | `{min: "number", max: "number", currency: "CNY|USD"}` — 投资金额区间 |
| `risk_tolerance` | enum | ❌ | `conservative` / `moderate` / `aggressive`，默认 `moderate` |

## 📤 输出

```json
{
  "stage": "screening | due_diligence | valuation | ic_memo",
  "screening_report": {
    "sector_attractiveness": "string — 赛道吸引力评分与分析",
    "business_model_score": "number (1-10)",
    "top3_opportunities": ["string — 最大机会点"],
    "top3_risks": ["string — 最大风险点"],
    "verdict": "proceed | reject | needs_more_info"
  },
  "due_diligence_report": {
    "tech_dd": {
      "architecture_maturity": "low | mid | high",
      "tech_moat": ["string"],
      "tech_debt_level": "low | mid | high",
      "scalability_score": "number (1-10)"
    },
    "product_dd": {
      "market_position": "string",
      "user_experience_score": "number (1-10)",
      "product_roadmap_clarity": "low | mid | high"
    },
    "team_dd": {
      "founder_assessment": "string",
      "team_strengths": ["string"],
      "team_weaknesses": ["string"],
      "psychological_profile": "string"
    },
    "legal_financial_dd": {
      "ip_portfolio": "string",
      "contract_risks": ["string"],
      "financial_health_grade": "A | B | C | D"
    },
    "top3_fatal_risks": ["string"],
    "verdict": "proceed | reject | conditional"
  },
  "valuation_model": {
    "dcf_value_range": {"low": "number", "mid": "number", "high": "number"},
    "comparable_multiples": {"pe": "number", "ps": "number", "ev_ebitda": "number"},
    "sensitivity_analysis": [{"scenario": "string", "value": "number", "probability": "number"}],
    "recommended_valuation": "number",
    "key_assumptions": ["string"]
  },
  "risk_matrix": [
    {"risk": "string", "probability": "high | mid | low", "impact": "high | mid | low", "mitigation": "string"}
  ],
  "ic_memo": {
    "executive_summary": "string",
    "investment_thesis": "string",
    "deal_terms": {"amount": "number", "equity_pct": "number", "valuation_cap": "number"},
    "recommendation": "invest | pass | renegotiate",
    "red_team_challenges": ["string — 魔鬼代言人攻击点"]
  }
}
```

## 📋 执行步骤

### Stage 1: AI驱动广域扫描与初筛
1. **设定筛选标准** — 根据 `investment_criteria` 定义行业赛道、成长阶段、财务阈值
2. **AI宏观分析** — 让AI扮演"行业分析师"，生成目标赛道一页纸速览（市场规模/产业链/Top3趋势/3年预测）
3. **AI初筛报告** — 让AI扮演"精明VC"，300字内指出商业模式最性感的点、最脆弱的环节、Top3待验证问题
4. **输出筛选结论** — 评分并给出 `proceed / reject / needs_more_info` 判断

### Stage 2: 跨学科深度尽调
5. **技术尽调** — 评估技术架构成熟度、核心算法壁垒、技术债水平、可扩展性
6. **产品尽调** — 分析市场定位、用户体验、产品路线图清晰度
7. **团队尽调** — 创始人心理特质评估、团队优劣势分析
8. **法务财务尽调** — IP组合审查、合同风险识别、财务健康度打分
9. **AI尽调清单生成** — 让AI扮演"M&A尽调顾问"，生成商业/技术/产品/财务/法务/人事六维问题清单

### Stage 3: 定量估值与定性判断
10. **DCF估值** — 构建折现现金流模型，输出低/中/高情景估值
11. **可比公司法** — 计算PE/PS/EV-EBITDA倍数，对标同业
12. **敏感性分析** — 对关键假设做压力测试，输出概率加权估值
13. **AI财务诊断** — 让AI扮演"苛刻财务分析师"，重点检查收入真实性、现金流匹配度、表外风险
14. **管理层定性判断** — 结合心理画像评估创始人韧性与动机

### Stage 4: 红队演练与风险对冲
15. **魔鬼代言人** — 让AI扮演"对冲基金做空者"，提出3-5个最致命攻击点并预测催化剂事件
16. **风险矩阵构建** — 概率×影响二维评估，为每个高风险设计 ≥2 个缓解方案
17. **仓位与止损设计** — 根据风险收益比确定投资条款

### Stage 5: IC Memo输出与投后闭环
18. **撰写IC Memo** — 汇总执行摘要、投资逻辑、交易条款、明确建议
19. **决策记录** — 记录"投"或"不投"的完整决策链路
20. **投后追踪设定** — 定义关键监控指标和警报阈值

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `target_info` 过于模糊 | 返回 `ERROR_INSUFFICIENT_INFO` + 需补充清单（至少需公司名+赛道+阶段） |
| `financial_data` 缺失但 stage=valuation | 返回 `WARNING_NO_FINANCIALS` + 仅输出定性估值框架 |
| 财务数据异常（收入>10x利润突变） | 标记 `FLAG_FINANCIAL_ANOMALY` + 要求人工核实 |
| 估值模型假设冲突 | 返回假设矛盾点 + 要求用户选择立场 |
|

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
