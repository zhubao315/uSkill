---
name: uskill-investment-im-report-writing
description: "让investment im report writing变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-im-report-writing.md"
  original_id: "SKL-6879"
  version: "3.0.0"
  trust: untrusted
---

# investment im report writing

# IM报告撰写（投资备忘录）

> **角色**: 投资经理 | **核心工具**: AI大模型, 财务模型, 行业数据库 | **效率目标**: 标准化输出高质量投资备忘录

## 🎯 目标
系统化完成投资备忘录(IM)的10章结构化撰写，覆盖项目启动、IC汇报、LP报告三大场景，确保分析深度与格式一致性。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `company_name` | string | ✅ | 标的公司全称 |
| `sector` | string | ✅ | 所属行业/赛道 |
| `deal_stage` | enum | ✅ | `screening` / `due_diligence` / `ic_presentation` / `lp_report` |
| `data_room` | object | ✅ | 尽调数据包（财务报表、业务数据、合同等） |
| `model_assumptions` | object | ❌ | 财务预测假设（增长率、利润率等） |
| `deal_terms` | object | ❌ | 交易条款信息（估值、对价、结构等） |
| `report_format` | enum | ❌ | `full` / `summary` / `ic_deck`，默认 `full` |

## 📤 输出

```json
{
  "report": {
    "chapter_1_executive_summary": {
      "investment_thesis": "string — 核心投资逻辑",
      "key_metrics": { "revenue": "number", "growth_rate": "number", "valuation": "string" },
      "recommendation": "enum — invest / pass / conditional_invest"
    },
    "chapter_2_company_info": { "overview": "string", "history": "string", "shareholders": "object" },
    "chapter_3_business_analysis": { "model": "string", "competitive_advantage": "string", "market_position": "string" },
    "chapter_4_revenue_sustainability": { "revenue_breakdown": "object", "sustainability_score": "number", "drivers": ["string"] },
    "chapter_5_financial_analysis": { "historical": "object", "key_ratios": "object", "quality_flags": ["string"] },
    "chapter_6_financial_forecast": { "projections": "object", "scenarios": ["string"], "assumptions": "object" },
    "chapter_7_deal_structure": { "valuation": "string", "terms": "object", "legal_considerations": "string" },
    "chapter_8_investment_return": { "irr": "number", "moic": "number", "payback_period": "string" },
    "chapter_9_risk_analysis": { "risk_matrix": "array", "mitigation": "object", "residual_risk": "string" },
    "chapter_10_conclusion": { "final_recommendation": "string", "next_steps": ["string"], "conditions": ["string"] }
  },
  "metadata": { "generated_at": "datetime", "version": "string", "author": "string" }
}
```

## 📋 执行步骤

### 阶段一：基础扫描（Basic Scan）

1. **收集公开信息** — 通过天眼查、招股书、行业报告获取公司基础数据
2. **初步筛选判断** — 验证项目是否符合基金投资策略与额度门槛，输出Pass/Proceed

### 阶段二：业务尽调（Business DD）

3. **行业与市场分析** — 评估TAM/SAM/SOM，绘制竞争格局图谱
4. **商业模式拆解** — 识别核心收入来源、客户集中度、定价能力与护城河
5. **管理层访谈** — 使用AI提示词模板(Prompt-3)结构化整理访谈要点

### 阶段三：财务尽调（Financial DD）

6. **历史财务分析** — 审阅3-5年报表，识别收入确认、关联交易、表外负债等质量风险
7. **财务质量校验** — 使用AI提示词模板(Prompt-5)生成财务质量评分卡

### 阶段四：建模（Modeling）

8. **构建财务模型** — 搭建DCF/可比估值模型，设定Base/Bull/Bear三种情景
9. **投资回报测算** — 计算IRR、MOIC、回收期，与基金要求回报对比

### 阶段五：综合撰写（Synthesis）

10. **逐章撰写** — 按10章框架依次填充内容，每章使用对应AI提示词模板
11. **交叉验证** — 确保各章节数据一致、逻辑自洽，财务预测与业务分析吻合
12. **风险矩阵编制** — 汇总所有风险因素，评估影响程度与发生概率
13. **执行摘要提炼** — 最后撰写第1章，确保决策者3分钟内掌握核心结论
14. **格式与合规检查** — 检查排版、数据标注、免责声明、合规要素完整性

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `data_room` 数据不完整 | 标注缺失项，使用公开数据补充并标记`[待确认]` |
| 财务数据勾稽不平 | 触发`ERROR_FINANCIAL_MISMATCH`，要求补充审计调整表 |
| 估值假设争议大 | 提供多情景估值区间，标注敏感性分析结果 |
| 管理层信息不可得 | 降级处理，标注`[未访谈]`并在风险章节反映 |
| IC汇报时间不足 | 切换为`report_format: ic_deck`，输出精简版 |

## ✅ 自检清单

- [ ] 10章结构完整，无遗漏章节
- [ ] 执行摘要包含核心投资逻辑、关键财务指标、明确推荐结论
- [ ] 财务预测三种情景(Bull/Base/Bear)均有呈现
- [ ] 风险矩阵覆盖市场、运营、财务、法律四维度
- [ ] 所有数据标注来源，`[待确认]`项已列出清单
- [ ] IRR/MOIC计算与投资门槛对比结论明确
- [ ] 格式符合基金IC材料标准，无排版错误


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
