---
name: uskill-productivity-investment-memo-writing
description: "让productivity investment memo writing变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-investment-memo-writing.md"
  original_id: "SKL-6917"
  version: "3.0.0"
  trust: untrusted
---

# productivity investment memo writing

# Investment Memo (IM) Report Writing

## 🎯 目标
> AI增强的投资经理IM报告撰写：5步流水线从基础扫描到综合风控，1天内完成标准IM报告，论证深度提升50%，覆盖立项报告、投决报告、LP汇报三种场景。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `company_info` | object | ✅ | `{name: "string", industry: "string", stage: "string", website: "string"}` — 目标公司基础信息 |
| `report_type` | enum | ✅ | `initiation`（立项报告）/ `ic_memo`（投决报告）/ `lp_report`（LP汇报） |
| `financial_data` | object | ❌ | `{audit_reports: [], bom_data: [], revenue_history: [], years: []}` — 审计报告/BOM/收入历史 |
| `team_resumes` | array | ❌ | 创始人及核心团队简历文本 |
| `product_docs` | array | ❌ | 产品参数文档、技术白皮书等 |
| `market_research` | object | ❌ | `{market_size: {}, policies: [], customer_plans: []}` — 市场/政策/客户组网计划 |
| `deal_terms` | object | ❌ | `{amount: "number", valuation: "number", exit_year: "number", exit_pe: "number"}` — 交易条款 |
| `comparable_companies` | array | ❌ | 可比公司列表 `[{name: "string", valuation: "number", pe: "number", ps: "number"}]` |

## 📤 输出

```json
{
  "im_report": {
    "executive_summary": {
      "industry_logic": "string — 行业逻辑（为什么选赛道）",
      "sub_strategy": "string — 细分策略",
      "core_advantages": ["string — 3大微观亮点"],
      "product_value": "string — 产品价值主张",
      "deal_summary": "string — 交易/退出/风险摘要",
      "recommendation": "invest | pass | renegotiate"
    },
    "company_basics": {
      "registration_info": "string",
      "founder_profile": [{"name": "string", "key_labels": ["string"], "commercial_value": "string"}],
      "equity_structure": "string",
      "history": "string",
      "funding_history": [{"round": "string", "date": "string", "amount": "number", "valuation": "number", "investors": ["string"]}],
      "valuation_curve": "string — 估值增长趋势描述"
    },
    "business_analysis": {
      "product_comparison": [
        {"company": "string", "specifications": {}, "cost_per_unit": "number", "highlights": ["string"]}
      ],
      "business_model": "string",
      "competitive_moat": ["string — 技术/成本/客户壁垒"],
      "tech_to_business_translation": "string — 技术商业化描述"
    },
    "financial_analysis": {
      "historical": {
        "revenue_trend": "string",
        "gross_margin_trend": "string",
        "rd_expense_ratio": "number",
        "key_ratios": {}
      },
      "bom_analysis": {
        "components": [{"name": "string", "cost": "number", "pct": "number"}],
        "cost_reduction_path": "string"
      },
      "forecast": {
        "scenarios": {
          "pessimistic": {"revenue": "number", "profit": "number"},
          "neutral": {"revenue": "number", "profit": "number"},
          "optimistic": {"revenue": "number", "profit": "number"}
        },
        "assumptions": ["string"],
        "forecast_basis": "string — 预测依据（客户组网计划等）"
      }
    },
    "valuation_and_return": {
      "comparable_multiples": {"pe": "number", "ps": "number", "ev_ebitda": "number"},
      "dcf_value_range": {"low": "number", "mid": "number", "high": "number"},
      "irr": "number",
      "exit_path": "string",
      "exit_assumptions": "string"
    },
    "deal_structure": {
      "investment_amount": "number",
      "equity_pct": "number",
      "valuation_cap": "number",
      "special_terms": ["string — 回购/清算等条款"]
    },
    "risk_analysis": [
      {"risk": "string", "category": "policy | technology | market | financial", "probability": "high | mid | low", "impact": "high | mid | low", "mitigation": "string"}
    ],
    "red_team_challenges": ["string — 投委尖锐挑战问题"],
    "conclusion": "string — 最终投资建议"
  },
  "report_markdown": "string — 完整IM报告Markdown文本"
}
```

## 📋 执行步骤

### Step 1: 基础扫描 (Basic Scan)
1. **工商数据收集** — 从企查查/天眼查导出企业征信报告
   - Checklist：成立时间、注册资本、股权穿透图（至自然人/国资）、对外投资架构
2. **团队画像提取** — 收集创始人及核心技术人员简历
   - 重点标注"体制内级别"（所长/主任设计师）、"过往项目"、"技术奖项"
   - AI提效：从简历堆中快速提取含金量标签
3. **历史融资梳理** — 梳理历次融资的时间、金额、估值、投资方
   - 绘制估值增长曲线，可视化展示资本追捧程度

### Step 2: 业务尽调 (Business DD)
1. **产品对标** — 制作参数对比表
   - 核心产品：运载能力/推力/成本等关键参数
   - 对标对象：必须包含"行业标杆"和"国内竞品"
2. **技术/成本拆解** — 寻找"人无我有"或"人有我优"的差异化优势
   - AI提效：将晦涩技术术语转化为商业优势

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
