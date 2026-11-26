# Poverty Trap Diagnosis Framework

## 🎯 目标

Diagnose systemic resource-constraint traps in any domain using the 4-mechanism framework from Banerjee & Duflo's poverty research. This skill transforms the book's empirical findings into a reusable analytical method applicable to organizational, community, product, or policy contexts where scarcity creates self-reinforcing feedback loops.

**Core thesis:** Poverty traps are not monolithic — they decompose into four distinct mechanisms (Information, Risk, Bandwidth, Institutional), each requiring a different intervention strategy. Effective diagnosis must identify which mechanisms dominate in a given context before prescribing solutions.

## 📥 输入

| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `target_population` | string | ✅ | The group or system under analysis (e.g., "rural smallholder farmers", "early-stage startup founders", "first-gen college students") |
| `resource_constraint` | string | ✅ | The primary scarce resource (e.g., financial capital, health 00-META, education quality, market 00-META) |
| `context_description` | string | ✅ | Situational context including geography, institutional environment, and relevant systemic factors |
| `available_data` | object | ❌ | Optional empirical data: surveys, behavioral observations, outcome metrics, cost structures |
| `comparison_baseline` | string | ❌ | A non-constrained comparison group or theoretical baseline for gap analysis |
| `intervention_budget` | string | ❌ | Resource envelope for potential interventions (affects feasibility filtering) |
| `time_horizon` | string | ❌ | Short-term (0-6mo), medium-term (6-24mo), or long-term (2yr+) orientation |

## 📤 输出

```json
{
  "diagnosis_id": "string",
  "trap_profile": {
    "information_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "info_access_gaps": ["string"],
      "quality_info_cost_assessment": "string",
      "low_cost_delivery_strategies": ["string"]
    },
    "risk_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "systemic_risk_amplifiers": ["string"],
      "conservative_cascade_indicators": ["string"],
      "risk_transfer_mechanisms": ["string"]
    },
    "bandwidth_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "cognitive_load_sources": ["string"],
      "decision_fatigue_indicators": ["string"],
      "simplification_opportunities": ["string"]
    },
    "institutional_trap": {
      "severity": "none | low | medium | high | critical",
      "evidence": ["string"],
      "friction_costs": ["string"],
      "nudge_designs": ["string"],
      "behavioral_interventions": ["string"]
    }
  },
  "dominant_trap_ranking": ["string"],
  "intervention_roadmap": [
    {
      "mechanism": "string",
      "intervention": "string",
      "expected_roi": "string",
      "implementation_difficulty": "low | medium | high",
      "priority": 1
    }
  ],
  "self_check_results": [
    {
      "check": "string",
      "passed": true,
      "notes": "string"
    }
  ]
}
```

## 📋 执行步骤

### Step 1: 情境映射 (Context Mapping)
Map the target population and resource constraint into the diagnostic space. Identify the baseline conditions: What does "non-constrained" look like for this population? Establish measurable indicators for each trap mechanism. Document the institutional landscape — who are the gatekeepers, intermediaries, and service providers?

**Deliverable:** A context map with population characteristics, constraint definitions, and baseline gap estimates.

### Step 2: 信息陷阱诊断 (Information Trap Diagnosis)
Analyze information 00-META asymmetries:
- **Access gaps:** What critical information does the target population lack? Where do they currently get information, and what is the quality gap?
- **Cost of quality info:** Calculate the effective cost (time, money, cognitive effort) of accessing accurate, actionable information. Compare to the cost of misinformation or no information.
- **Delivery strategy design:** Propose low-cost, high-uptake information delivery mechanisms. Consider channel preferences, trust anchors, timing, and format. Reference: vaccine uptake increased from 5% to 40% when combined with instant grain rewards — information alone is insufficient without friction reduction.

**Key question:** Is the primary barrier that people *don't know*, or that knowing is *too expensive*?

### Step 3: 风险陷阱诊断 (Risk Trap Diagnosis)
Map the risk landscape and response constraints:
- **Systemic risk amplifiers:** Identify risks that are both high-probability and high-consequence for the target population (health shocks, market volatility, climate events, policy uncertainty). Note: the poor face *disproportionately higher* base rates of adverse events.
- **Conservative decision cascades:** Trace how risk exposure leads to risk-averse behavior that perpetuates the constraint. Example: lack of crop insurance → only planting subsistence crops → never entering cash-crop markets → remaining income-constrained.
- **Risk-transfer mechanisms:** Identify existing informal risk-sharing (family networks, community pools) and formal mechanisms (insurance, hedging). Assess gaps and propose viable risk-transfer designs. Reference: Grameen Bank's 98% repayment rate shows group liability can function as a risk-transfer mechanism; Andhra Pradesh crisis shows when microfinance *adds* risk instead of reducing it.

**Key question:** Are people making "irrational" choices, or are they rationally managing risks that outsiders don't see?

### Step 4: 带宽陷阱诊断 (Bandwidth Trap Diagnosis)
Assess cognitive resource depletion from scarcity:
- **Cognitive load sources:** Enumerate the recurring decisions and survival pressures that consume mental bandwidth. Quantify where possible (e.g., number of distinct financial decisions per week, time spent on water collection).
- **Decision fatigue indicators:** Look for patterns of defaulting to status quo, inconsistent choices over time, low uptake of beneficial programs even when free, and procrastination on high-value actions.
- **Simplification opportunities:** Design interventions that reduce decision burden — defaults, auto-enrollment, bundled services, simplified choice architectures. Reference: goal-based savings accounts showed 81% improvement over casual savings because they eliminated the "when and how much to save" decision.

**Key question:** Is the bottleneck knowledge, or is it the *capacity to act on knowledge* given everything else competing for attention?

### Step 5: 制度陷阱诊断 (Institutional Trap Diagnosis)
Analyze institutional design failures:
- **Friction costs:** Measure the transaction costs of engaging with relevant institutions — forms, travel time, waiting periods, documentation requirements, eligibility verification. Calculate the effective "tax" these impose on the target population.
- **Nudge design:** Propose choice architecture changes that make beneficial behavior the default. Consider: opt-out vs opt-in, simplification, reminder systems, social proof, commitment devices. Evidence: removing even small friction (e.g., requiring people to walk to a clinic) can reduce uptake by 50%+.
- **Behavioral intervention design:** Design interventions that work *with* cognitive biases rather than against them. Consider present bias, loss aversion, social norms, and mental accounting. Reference: $1 in water purification investment saves $3 in medical costs — but adoption requires institutional design that makes purification the default, not the exception.

**Key question:** Are institutions designed for the people they serve, or for the administrators who run them?

### Step 6: 综合诊断与干预路线图 (Synthesis & Intervention Roadmap)
Integrate findings across all four mechanisms:
1. **Rank traps by severity** — which mechanisms create the strongest self-reinforcing loops?
2. **Identify interaction effects** — e.g., information gaps + bandwidth depletion compound each other; institutional friction amplifies risk exposure.
3. **Design sequenced interventions** — address the highest-leverage trap first, but sequence to avoid creating new traps (e.g., microfinance 00-META without financial literacy → over-indebtedness).
4. **Estimate ROI** for each proposed intervention using available evidence and analogies.
5. **Run the self-check** (see below) before finalizing.

**Deliverable:** A prioritized intervention roadmap with expected impact, difficulty, and sequencing rationale.

## ⚠️ 异常处理

| 异常场景 | 识别信号 | 处置策略 |
|----------|----------|----------|
| 数据不足，无法区分陷阱严重性 | 每个机制的 evidence 数组为空或仅有推测 | 标记为 "insufficient_data"，输出最低置信度诊断，建议补充数据收集步骤（快速 ethnographic survey, key informant interviews, behavioral observation） |
| 多个陷阱严重性相同，无法排序 | 四个机制 severity 评级完全一致 | 进行交互效应分析：哪个陷阱的改善对其他三个有最大正外部性？优先该机制。如仍无法区分，默认优先 Bandwidth Trap（认知带宽是其他干预生效的前提） |
| 目标群体异质性过高 | 存在显著亚群体差异（收入分层、地理分散、文化差异） | 按关键变量拆分为 2-3 个亚群体，分别诊断后合并报告。标注哪些结论适用于全群体 vs 仅特定亚群体 |
| 发现"反向陷阱"：干预本身创造新陷阱 | 微金融案例：Grameen 成功 vs Andhra Pradesh 危机 | 在干预路线图中添加 "trap_risk" 字段，标注每个干预的潜在负面第二效应，设计防护机制（如贷款上限、强制冷却期） |
| 机构环境高度对抗或不合作 | 利益相关者阻挠数据收集或干预实施 | 切换至"隐蔽诊断"模式：使用公开数据、间接指标、代理变量。降低干预方案对机构配合的依赖度，优先设计自下而上的干预 |
| 文化规范与行为干预冲突 | nudge 设计与本地价值观、宗教、社会结构矛盾 | 深度文化适配：与社区领袖共建干预设计，使用本地叙事框架，避免"外部专家强加"的框架。增加参与式设计阶段 |
| 时间尺度不匹配 | 短期干预需求 vs 长期结构性问题 | 分层输出：(1) 即时缓解措施 (< 1mo), (2) 中期行为改变 (1-6mo), (3) 长期制度重构 (> 6mo)。明确哪些是"创可贴"vs 真正的系统性改变 |

## ✅ 自检清单

- [ ] 四个陷阱机制均已分析，无遗漏
- [ ] 每个机制的 severity 评级有至少 1 条具体 evidence 支撑
- [ ] Information Trap: 信息获取成本已量化或定性估算，而非仅描述"缺乏信息"
- [ ] Risk Trap: 已区分"真实风险"与"感知风险"，干预方案不假设风险可被消除
- [ ] Bandwidth Trap: 已识别具体的认知负荷来源，而非笼统描述"决策疲劳"
- [ ] Institutional Trap: 摩擦成本已用目标群体的视角（而非机构视角）评估
- [ ] 干预路线图包含 sequencing（先后顺序），而非仅并列方案
- [ ] 每个干预方案标注了潜在负面第二效应（trap_risk）
- [ ] 比较基准已明确定义（与谁/什么比？）
- [ ] 诊断结论可被非专业人士理解（避免经济学术语黑箱化）
- [ ] 引用了至少 2 条来自源文献或类似情境的经验证据
- [ ] 输出 JSON schema 完整，所有必需字段已填充

## 📚 参考

### 源文献
- Banerjee, A. V., & Duflo, E. (2011). *Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty*. PublicAffairs. — 本书的核心框架来源，基于 15 年随机对照实验的贫困陷阱诊断方法。
- Banerjee, A. V., & Duflo, E. (2019). *Good Economics for Hard Times*. PublicAffairs. — 扩展框架至更广泛的制度与行为经济学问题。

### 关键证据索引
| 证据 | 来源 | 对应陷阱 |
|------|------|----------|
| 疫苗接种率 5%→40%（即时粮食奖励） | Banerjee & Duflo, RCT data | Information + Bandwidth |
| 目标储蓄账户提升 81% | Field et al., savings RCT | Bandwidth |
| $1 水净化 → $3 医疗成本节约 | WHO / WASH studies | Institutional |
| Grameen 98% 还款率 vs 安得拉邦危机 | Microfinance literature | Risk |
| 移除小摩擦致接种率降 50%+ | Health 00-META studies | Institutional |

### 关联技能
- `cognitive-decision-fatigue-mapping` — Bandwidth Trap 诊断的细化工具
- `cognitive-nudge-design` — Institutional Trap 干预设计的专项技能
- `cognitive-ri[REDACTED_TOKEN]` — Risk Trap 深度分析的配套技能
- `cognitive-information-asymmetry-diagnosis` — Information Trap 的独立诊断工具
- `behavioral-economics-intervention-design` — 跨机制行为干预设计
- `policy-friction-cost-analysis` — Institutional Trap 中摩擦成本量化工具

### 延伸阅读
- Mullainathan, S., & Shafir, E. (2013). *Scarcity: Why Having Too Little Means So Much*. — Bandwidth Trap 的认知科学基础。
- Kahneman, D. (2011). *Thinking, Fast and Slow*. — 行为干预设计的理论框架。
- Thaler, R. H., & Sunstein, C. R. (2008). *Nudge*. — Institutional Trap 干预设计的经典参考。


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
---
**相关笔记**：[[uSkill-cognition-知识缺口识别]] [[第二大脑知识管理]] 


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


**相关概念**：[[个人理财]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位贫困陷阱诊断专家，擅长识别导致个人或组织陷入低水平循环的认知与行为模式。请根据以下输入执行操作：
输入：[当前困境表现、行为模式描述、资源约束条件]
要求：[诊断维度、干预可行性评估、时间窗口]
输出格式：[贫困陷阱诊断报告，含陷阱类型识别、因果链分析、关键支点定位和脱困策略]
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改

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
