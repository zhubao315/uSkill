# P4 Agentic Finance - Adversarial Investment Research System

## 🎯 目标
> 对抗性投研数字孪生系统：基于本地4090集群部署MoA架构，4个Agent（激进派/保守派/裁判官/风控官）对抗辩论，100次虚拟辩论产出"幸存者策略"，目标年化收益18%+，最大回撤<15%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `investment_target` | object | ✅ | `{ticker: "string", market: "A-share" | "crypto", name: "string"}` — 投资标的 |
| `analysis_type` | enum | ✅ | `quick_scan`（快速扫描）/ `full_debate`（完整辩论）/ `risk_check`（风控审查） |
| `hardware_config` | object | ❌ | `{gpu_count: "number", gpu_model: "string", vram_gb: "number"}` — 硬件配置，默认4090集群 |
| `model_config` | object | ❌ | `{aggressive: "string", conservative: "string", referee: "string", risk_officer: "string"}` — 各Agent模型 |
| `market_data` | object | ❌ | `{prices: [], fundamentals: {}, news: []}` — 行情/基本面/新闻数据 |
| `portfolio_context` | object | ❌ | `{current_positions: [], total_capital: "number", max_drawdown: "number"}` — 当前持仓上下文 |
| `custom_constraints` | object | ❌ | `{max_single_position: "number", stop_loss: "number", holding_period: "string"}` — 自定义约束 |

## 📤 输出

```json
{
  "agentic_finance_report": {
    "debate_summary": {
      "target": "string — 标的名称/代码",
      "debate_rounds": "number — 辩论轮次",
      "convergence": "boolean — 是否收敛",
      "total_duration_ms": "number — 总耗时"
    },
    "agent_a_aggressive": {
      "stance": "buy | sell | hold",
      "confidence": "number (0-100)",
      "technical_signals": {
        "rsi": "number",
        "macd": "string",
        "bollinger": "string",
        "volume_anomaly": "boolean"
      },
      "argument": "string — 核心论证",
      "target_price": "number",
      "stop_loss": "number"
    },
    "agent_b_conservative": {
      "stance": "buy | sell | hold",
      "confidence": "number (0-100)",
      "valuation_metrics": {
        "pe_percentile": "number",
        "pb_percentile": "number",
        "roe": "number",
        "moat_score": "string"
      },
      "argument": "string — 核心论证",
      "safety_margin": "string — 安全边际分析"
    },
    "agent_c_referee": {
      "final_verdict": "buy | sell | hold | wait",
      "overall_confidence": "number (0-100)",
      "reasoning": "string — 综合判断逻辑",
      "counterfactual": {
        "if_a_wrong": "string — 如果激进派错了，原因可能是...",
        "if_b_wrong": "string — 如果保守派错了，原因可能是..."
      },
      "recommended_position_pct": "number (0-100)",
      "recommended_holding_days": "number"
    },
    "agent_d_risk_officer": {
      "veto": "boolean — 是否一票否决",
      "risk_level": "low | medium | high | critical",
      "black_swan_flags": ["string — 黑天鹅风险信号"],
      "drawdown_status": {
        "current_drawdown_pct": "number",
        "max_allowed_pct": "number",
        "breach": "boolean"
      },
      "action": "approve | veto | reduce_position",
      "alert_message": "string | null"
    },
    "final_decision": {
      "recommendation": "buy | sell | hold | wait | veto",
      "position_size_pct": "number",
      "entry_price_range": {"low": "number", "high": "number"},
      "stop_loss": "number",
      "take_profit": "number",
      "holding_period": "string",
      "confidence_score": "number (0-100)",
      "human_override_needed": "boolean"
    },
    "backtest_context": {
      "similar_scenarios_count": "number",
      "historical_win_rate": "number",
      "avg_return": "number",
      "max_drawdown_in_similar": "number"
    }
  }
}
```

## 📋 执行步骤

### Step 1: 环境准备与数据接入 (Setup & Data Pipeline)
1. **硬件确认** — 验证4090集群状态，确保GPU可用显存充足
   - 检查项：NVIDIA驱动版本、CUDA版本、vLLM/Ollama服务状态
2. **模型加载** — 加载4个Agent对应模型
   - Agent A（激进派）: Qwen2-7B — 快速决策，动量捕捉
   - Agent B（保守派）: Llama3-8B — 稳健分析，价值评估
   - Agent C（裁判官）: ChatGLM4-9B — 综合判断，Reflection机制
   - Agent D（风控官）: Qwen2-72B（量化版）— 深度风控分析
3. **数据获取** — 接入实时/历史行情数据
   - A股：Tushare / AKShare
   - 加密货币：Binance API
   - 新闻：雪球、东方财富、Twitter API
   - 质量检查：数据完整性>99%，延迟<1s

### Step 2: Agent对抗辩论 (Multi-Agent Debate)
1. **辩论启动** — 将标的信息和市场数据广播给4个Agent
2. **第一轮：独立分析**
   - Agent A 分析技术面（RSI/MACD/布林带/成交量突变/资金流向）
   - Agent B 分析基本面（PE/PB估值分位数/现金流/ROE/护城河/宏观周期）
   - 各自输出：买卖建议 + 论证 + 目标价 + 止损位
3. **第二轮：交叉质询**
   - Agent A 反驳 Agent B 的保守论点
   - Agent B 反驳 Agent A 的激进论点
   - 各自更新置信度
4. **第三轮：裁判官综合**
   - Agent C 接收A/B完整论证
   - 执行Reflection："如果A错了，可能是因为...；如果B错了，可能是因为..."
   - 给出置信度评分(0-100)和最终建议
5. **风控审查** — Agent D 独立审查
   - 扫描黑天鹅事件（地缘政治/监管政策/突发新闻）
   - 检查账户回撤（单日>5% 或 连续3日>10% 则触发否决）
   - 检查市场异常（波动率骤升/流动性枯竭）
   - 拥有绝对否决权，可直接切断交易

### Step 3: 策略生成与回测验证 (Strategy Generation & Backtesting)
1. **幸存者策略生成** — 基于辩论结果生成可执行策略
   - 入场规则、出场规则、止损止盈、仓位控制
2. **历史回测** — 用历史数据验证策略
   - 测试场景：牛市(2019-2020)、熊市(2021-2022)、震荡市(2023)、黑天鹅(2020.3/2022.2)
   - 核心指标：胜率>60%、盈亏比>2:1、最大回撤<15%、年化收益>18%
3. **策略优化** — 基于回测结果调整Agent权重和风控阈值

### Step 4: 人类决策与执行 (Human Decision & Execution)
1. **决策报告呈现** — 向人类决策者展示完整辩论报告
   - 4个Agent的立场、论证、置信度一目了然
2. **人类审核** — 人类可覆盖/修改AI建议
   - 记录人类修改率，分析人类决策质量
3. **执行建议** — 如通过风控审查，生成具体执行指令
   - 标的、方向、仓位、价格区间、止损止盈
   - 质量检查：Agent角色鲜明？辩论逻辑清晰？输出可解释？风控100%生效？

## 🤖 AI提示词库

### 提示词-P4-R01: 技术架构设计
```
你是一位资深量化系统架构师，专注于AI驱动的投资决策系统。我需要你设计一个基于4090集群的对抗性投研系统。

【项目背景】
- 硬件: 4090集群 (2-4张卡)
- 目标: 年化18%+, 利润30-40万
- 模式: 4个Agent对抗辩论 + 人类决策

【任务】
请生成《技术架构设计文档》，包含：
1. 硬件配置方案（GPU分配策略、显存优化、推理性能预估）
2. 模型选型矩阵（4个Agent各推荐模型+理由+对比）
3. MoA架构设计（辩论流程、上下文管理、超时控制、容错重试）
4. 数据管道（实时数据源、特征工程、存储方案、黑天鹅监控）
5. 风险控制架构（独立风控层、熔断机制、一票否决权、告警系统）
```

### 提示词-P4-P01: Agent开发计划
```
你是一位AI Agent系统专家，需要为4个不同角色的Agent制定详细的开发计划。

【角色定义】
- Agent A (激进派): 动量策略，追求高收益
- Agent B (保守派): 价值投资，控制风险
- Agent C (裁判官): Reflection机制，综合决策
- Agent D (风控官): 一票否决，黑天鹅监控

【任务】
请生成《Agent开发实施计划》，每个Agent包含：Prompt设计要点、工具接口、输出格式定义、测试用例设计。另含MoA协调器的辩论流程编排和人类接口设计。
```

### 提示词-P4-V01: Agent编码
```
你是一位全栈AI工程师，正在{BRANCH_NAME}分支上实现{AGENT_NAME}。

【上下文】
- 项目: P4 Agentic Finance
- 硬件: 4090集群 + vLLM推理
- 模型: {MODEL_NAME}

【任务】
请生成完整代码，包括：Prompt模板（角色定义/分析维度/输出约束）、工具接口（数据获取/计算/格式化）、Agent核心类（__init__/analyze/format_output/validate）、测试代码、配置文件。

【约束条件】
- Python 3.10+, 类型注解, JSON输出, 响应<2秒, 完整异常捕获
```

### 提示词-P4-I01: 回测分析
```
你是一位量化回测专家，需要分析100次虚拟辩论的结果，生成幸存者策略。

【回测数据】
- 辩论次数: 100次 | 回测周期: 2018-2024 | 初始资金: 100万 | 标的: 50只A股

【任务】
请生成《回测分析报告》，包含：整体表现分析（收益分布/最大回撤/年化收益/基准对比）、Agent表现分析（各Agent贡献度/成功率/置信度有效性/否决准确性）、策略优化建议（Prompt优化/权重调整/风控阈值）、幸存者策略（入场/出场/止损止盈/仓位）、实盘建议。
```

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| GPU显存不足 | 降级模型量化（INT8/FP16）或减少并发Agent数 |
| 模型推理延迟>5s | 切换到更小模型或启用KV Cache优化 |
| Agent输出不一致无法收敛 | 设置置信度阈值，裁判官强制决策，必要时人类干预 |
| 数据源不可用 | 多数据源备份 + 本地缓存 + 静默模式 |
| Agent D触发否决 | 立即停止交易，发送告警，等待人类确认 |
| 策略回测胜率<50% | 标记 `WARNING_LOW_WIN_RATE` + 建议重新设计Agent Prompt |
| 黑天鹅事件触发 | 强制空仓 + 切断交易API + 发送紧急告警 |
| 4090集群不稳定 | 主备切换 → 降级单卡 → 本地Ollama备份 |

## ✅ 自检清单

- [ ] 环境：4090集群可用，vLLM/Ollama服务正常，4个Agent模型已加载
- [ ] 数据：行情数据完整性>99%，延迟<1s，黑天鹅监控已启动
- [ ] 辩论：Agent角色鲜明（激进/保守/裁判/风控），辩论逻辑清晰
- [ ] 输出：每个Agent输出可解释，置信度评分合理
- [ ] 风控：Agent D独立运行，一票否决机制正常，熔断逻辑已测试
- [ ] 回测：胜率>60%，最大回撤<15%，年化收益>18%，盈亏比>2:1
- [ ] 实盘：小额验证通过（5-10万），人类可干预，执行记录完整
- [ ] 商业：AI决策内参模板标准化，客户转化漏斗清晰


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-27 转化 |

---
**相关笔记**：[[SOP-09-投资人-投资机会分析]] [[会议效率]] 


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


**相关概念**：[[P4 Agentic 金融]]

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
