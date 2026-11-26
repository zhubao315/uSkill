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
| 所有方案IRR低于阈值 | 明确建议 `pass` + 说明机会成本 |

## ✅ 自检清单

- [ ] 筛选阶段：至少识别3个核心机会点和3个核心风险点
- [ ] 尽调阶段：技术/产品/团队/法务四维度均有评估结论
- [ ] 估值阶段：DCF + 可比公司法双重验证，敏感性分析覆盖关键变量
- [ ] 风险矩阵：≥5项风险，每项有 ≥2 个缓解方案
- [ ] IC Memo：包含明确的"投/不投/重新谈判"建议
- [ ] 红队演练：至少3个攻击点经数据或逻辑支撑
- [ ] 成本预测：包含隐性成本（时间/机会成本/管理投入）


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
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-02 转化 |

---
**相关笔记**：[[DIKW 知识金字塔]] [[SKILLS-CATALOG]] 


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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


**相关概念**：[[投资机会解析]]

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
