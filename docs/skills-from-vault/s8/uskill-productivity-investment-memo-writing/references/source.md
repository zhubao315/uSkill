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
   - AI提效：将晦涩技术术语转化为商业优势描述
3. **市场/订单验证** — 收集客户意向书或中标公告
   - 具体到中标份额、预计发数、单星重量等硬数据
   - AI提效：利用Deep Research查找组网计划和宏观数据

### Step 3: 财务与数据核查 (Financial DD)
1. **历史财务清洗** — 获取近3年审计报告，录入结构化格式
   - 重点计算研发费用占比、毛利率变化趋势
2. **BOM成本分析** — 拆解单品BOM（物料清单）
   - 细化到各核心部件单价
   - AI提效：辅助判断成本下降逻辑的合理性
3. **收入预测建模** — 建立悲观/中性/乐观三张预测表
   - 收入 = 预计量 × 单价
   - 预测依据必须基于客户组网计划，而非拍脑袋

### Step 4: 建模与估值 (Modeling)
1. **估值锚定** — 选取可比公司
   - 一级市场：看竞品最近一轮融资估值
   - 二级市场：看类似标的PE/PS倍数
2. **IRR测算** — 设定退出年份，计算内部收益率
   - 假设IPO时PE倍数 × 预测净利润 = 退出市值
   - 计算从当前轮次到退出的IRR

### Step 5: 综合撰写与风控 (Synthesis)
1. **风险压力测试** — 列出关键风险点（技术/政策/资金链）
   - AI提效：让AI扮演"苛刻投委"进行红队攻击
2. **核心观点提炼** — "3+3"结构
   - 3大宏观逻辑：为什么选赛道？
   - 3大微观亮点：为什么选这家公司？
3. **撰写完整IM报告** — 汇总所有章节，输出标准化IM文档

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `company_info` 不完整 | 返回 `ERROR_INSUFFICIENT_INFO` + 至少需要公司名+行业+阶段 |
| `financial_data` 缺失但 `report_type=ic_memo` | 返回 `WARNING_NO_FINANCIALS` + 仅输出定性分析框架 |
| 财务数据异常（收入突变>10x） | 标记 `FLAG_FINANCIAL_ANOMALY` + 要求人工核实 |
| `comparable_companies` 为空 | 自动搜索同行业可比公司，标注 `AUTO_PEERS_SELECTED` |
| `deal_terms` 缺失但需要IRR测算 | 跳过IRR计算，输出估值区间供人工填充 |
| 预测假设相互冲突 | 返回假设矛盾点 + 要求用户选择立场 |
| 产品对标数据不完整 | 标记缺失字段，用"N/A"填充，降低对比表完整度评分 |

## ✅ 自检清单

- [ ] 基础扫描：工商/团队/融资三维度信息完整
- [ ] 业务尽调：产品对标表至少含3家竞品，包含行业标杆
- [ ] 业务尽调：技术优势描述已转化为商业语言
- [ ] 财务核查：近3年核心财务指标（研发占比/毛利率）已计算
- [ ] 财务核查：BOM成本拆解至少到二级部件
- [ ] 财务预测：悲观/中性/乐观三情景预测已完成
- [ ] 估值建模：DCF + 可比公司法双重验证
- [ ] IRR测算：退出路径和假设已明确
- [ ] 风险分析：≥5项风险，每项有缓解方案
- [ ] 红队演练：至少3个尖锐挑战问题
- [ ] 核心观点：包含"3+3"结构（3宏观+3微观）
- [ ] 最终建议：包含明确的"投/不投/重新谈判"建议


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-25 转化 |

---
**相关笔记**：[[uSkill-agent-优先级排序-agent-实施手册]] [[会议飞读法]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

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
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

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
