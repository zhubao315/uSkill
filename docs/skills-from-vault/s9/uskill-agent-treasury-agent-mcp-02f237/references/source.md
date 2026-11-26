
# 💰 Treasury Agent MCP 接入与回测系统

> **Q3 目标**：MCP 接入券商 API + 调仓策略回测 + 风控闭环验证
> **时间跨度**：2026-07-01 → 2026-09-30
> **关联**：[[∑ 投资条件反射规则]] · [[循环工程-财务智能体红队对抗配置]] · [[2026-Q3-OKR-草稿]]

---

## 一、系统架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Treasury Agent System                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Layer 1: Data Acquisition                 │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ MCP      │  │ 券商 API │  │ 手动录入 │              │   │
│  │  │ Protocol │  │ (模拟)   │  │ (降级)   │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                 Layer 2: Risk Control Engine              │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ CB-1     │  │ CB-2     │  │ CB-3     │              │   │
│  │  │ 集中度   │  │ 现金地板 │  │ 个股止损 │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ R4       │  │ R5       │  │ R6       │              │   │
│  │  │ 回撤控制 │  │ 波动率   │  │ 相关性   │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                 Layer 3: Backtest Engine                  │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ 策略回测 │  │ 历史数据 │  │ 绩效评估 │              │   │
│  │  │ Engine   │  │ Handler  │  │ Metrics  │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                 Layer 4: Reporting & Alerts               │   │
│  │  日报 │ 周报 │ 月报 │ OVP 季报 │ IM 推送 │ 邮件       │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 二、Phase 1：MCP API 原型（7/1 → 8/15）

### 目标
模拟券商 API 跑通，自动对账误差 <1%。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T1.1 | MCP 券商 API 接口定义 | `treasury_mcp_schema.yaml` | 7/15 | — |
| T1.2 | 模拟数据生成器 | `treasury_mock_data.py` | 7/25 | T1.1 |
| T1.3 | 持仓同步模块 | `treasury_sync.py` | 8/1 | T1.2 |
| T1.4 | 对账引擎 | `treasury_reconcile.py` | 8/10 | T1.3 |
| T1.5 | 端到端测试 | 测试报告 | 8/15 | T1.4 |

### MCP 接口定义

```yaml
# Treasury MCP Server - Tool Definitions
tools:
  - name: "treasury_sync_positions"
    description: "同步持仓数据"
    input:
      source: "string"          # mock | manual | broker_api
      date: "string"            # YYYY-MM-DD
    output:
      positions: "array"        # 持仓列表
      total_value: "number"     # 总市值
      cash_balance: "number"    # 现金余额

  - name: "treasury_reconcile"
    description: "对账：比较本地记录与券商数据"
    input:
      local_records: "array"    # 本地持仓
      broker_data: "array"      # 券商数据
    output:
      match_rate: "number"      # 匹配率
      discrepancies: "array"    # 差异项

  - name: "treasury_calculate_risk"
    description: "计算风控指标"
    input:
      positions: "array"
      total_value: "number"
    output:
      cb1_tech_concentration: "number"  # 科技集中度
      cb2_cash_floor: "number"          # 现金占比
      cb3_stock_loss: "array"           # 个股止损状态
      risk_level: "string"              # green|yellow|red
```

### 对账误差标准

```
对账误差 = |本地记录市值 - 券商数据市值| / 券商数据市值 × 100%

目标：<1%
触发条件：
  - 误差 <0.1%：正常
  - 0.1% ≤ 误差 <1%：告警
  - 误差 ≥1%：冻结交易 + 人工介入
```

---

## 三、Phase 2：回测系统（8/16 → 8/31）

### 目标
调仓策略回测系统上线，首份回测报告产出。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T2.1 | 历史数据接口 | `treasury_history.py` | 8/20 | — |
| T2.2 | 回测引擎核心 | `treasury_backtest.py` | 8/25 | T2.1 |
| T2.3 | 绩效指标计算 | `treasury_metrics.py` | 8/28 | T2.2 |
| T2.4 | 首份回测报告 | `回测报告-2026-08.md` | 8/31 | T2.3 |

### 回测策略定义

```yaml
# backtest_strategies.yaml
strategies:
  - name: "equal_weight_rebalance"
    description: "等权重再平衡"
    rules:
      - type: "rebalance"
        frequency: "monthly"
        target_weights: "equal"  # 各品种等权重
      - type: "stop_loss"
        threshold: -0.15
        action: "liquidate"

  - name: "risk_parity"
    description: "风险平价"
    rules:
      - type: "rebalance"
        frequency: "monthly"
        target_risk: "equal"  # 各品种风险贡献相等
      - type: "volatility_target"
        target_vol: 0.15
        action: "adjust_position"

  - name: "momentum_trend"
    description: "动量趋势"
    rules:
      - type: "signal"
        indicator: "MA20"
        entry: "price > MA20"
        exit: "price < MA20"
      - type: "stop_loss"
        threshold: -0.10
        action: "liquidate"
```

### 绩效指标体系

| 指标 | 公式 | 目标 |
|------|------|------|
| 年化收益率 | `(final/initial)^(252/days) - 1` | ≥ 基准 |
| 最大回撤 | `max(peak - trough) / peak` | ≤ 15% |
| 夏普比率 | `(return - risk_free) / volatility` | ≥ 1.0 |
| 胜率 | `winning_days / total_days` | ≥ 55% |
| 盈亏比 | `avg_win / avg_loss` | ≥ 1.5 |

---

## 四、Phase 3：风控闭环（9/1 → 9/15）

### 目标
风控 Agent 上线验证，硬性熔断 + 软性预警双保险生效。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T3.1 | 风控规则引擎更新 | `treasury_risk_engine.py` | 9/5 | Phase 1 |
| T3.2 | 软性预警系统 | `treasury_alert.py` | 9/10 | T3.1 |
| T3.3 | 红队对抗测试 | 测试报告 | 9/12 | T3.2 |
| T3.4 | 风控闭环验证 | 验证报告 | 9/15 | T3.3 |

### 风控规则升级（v1 → v2）

```yaml
# risk_rules_v2.yaml
circuit_breakers:
  - id: "CB-1"
    name: "科技集中度熔断"
    threshold: 0.50
    severity: "hard"           # 硬性：必须执行
    cooldown_days: 5
    action: "reduce_to_target"
    target: 0.45

  - id: "CB-2"
    name: "现金地板熔断"
    threshold: 0.05
    severity: "hard"
    action: "freeze_buy"
   解除条件: "连续3日≥10%"

  - id: "CB-3"
    name: "个股止损熔断"
    threshold: -0.15
    severity: "hard"
    action: "liquidate"
   禁买期: 30  # 交易日

soft_alerts:
  - id: "SA-1"
    name: "行业轮动预警"
    condition: "单行业占比>30%"
    severity: "warning"
    action: "notify_only"

  - id: "SA-2"
    name: "波动率飙升预警"
    condition: "20日波动率>历史80分位"
    severity: "warning"
    action: "reduce_position_10%"

  - id: "SA-3"
    name: "相关性集中预警"
    condition: "Top3持仓相关性>0.8"
    severity: "warning"
    action: "diversify_suggestion"
```

### 红队对抗测试矩阵

| 测试场景 | 输入 | 期望输出 | 验证点 |
|----------|------|---------|--------|
| 科技集中度超标 | 科技占比 65% | CB-1 触发，生成减仓建议 | 减仓比例正确 |
| 现金地板击穿 | 现金占比 3% | CB-2 触发，冻结买入 | 冻结生效 |
| 个股暴跌 | 单只浮亏 -18% | CB-3 触发，清仓指令 | 清仓执行 |
| 极端行情 | 单日 -5% | 多规则同时触发 | 优先级排序正确 |
| 数据延迟 | API 超时 | 降级到手动录入 | 降级生效 |

---

## 五、Phase 4：OVP 投资季报（9/16 → 9/30）

### 目标
首份 OVP 投资季报产出，自主调仓胜率首次测量。

### OVP 季报模板

```markdown
# Treasury Agent OVP 季报 — Q3 2026

## 核心指标
| 指标 | 目标 | 实际 | 状态 |
|------|:----:|:----:|:----:|
| 对账误差 | <1% | XX% | 🟢/🔴 |
| 回测胜率 | 首次测量 | XX% | 🟢 |
| 风控触发次数 | — | XX 次 | — |
| 调仓执行率 | 100% | XX% | 🟢/🔴 |

## 持仓结构变化
## 风控事件回顾
## 回测结果分析
## Q4 改进计划
```

---

## 六、文件产出物清单

| 文件 | 路径 | 说明 |
|------|------|------|
| MCP Schema | `04-Investor/45-投资工具/treasury_mcp_schema.yaml` | 接口定义 |
| 模拟数据 | `04-Investor/45-投资工具/treasury_mock_data.py` | 测试数据生成 |
| 同步模块 | `04-Investor/45-投资工具/treasury_sync.py` | 持仓同步 |
| 对账引擎 | `04-Investor/45-投资工具/treasury_reconcile.py` | 对账逻辑 |
| 回测引擎 | `04-Investor/45-投资工具/treasury_backtest.py` | 策略回测 |
| 风控引擎 | `04-Investor/45-投资工具/treasury_risk_engine.py` | 规则引擎 |
| 预警系统 | `04-Investor/45-投资工具/treasury_alert.py` | 软性预警 |
| 路线图 | `02-BUILD/22-uSkill/智能体任务/uSkill-Treasury-Agent-MCP接入与回测系统-v1.md` | 本文件 |


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

*版本：v1.0 · 2026-07-02 创建 · Q3 里程碑：8/15 API 原型 → 8/31 回测系统 → 9/15 风控上线 → 9/30 季报*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [投资决策类型] for [投资者风格], with [风险偏好], leaning toward [分析框架/数据源]."

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
| ""这次不一样"" | "每次泡沫都说这次不一样，这次也一样" |
| ""先满仓再说"" | "满仓=零容错，一个回调就是灾难" |
| ""跌了就补仓"" | "越补越套是亏损扩大的主因" |
| ""长期持有就行"" | "长期持有不等于不做仓位管理" |
| ""这次消息是利好"" | "消息面驱动的交易成功率低于掷硬币" |

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

## 🔄 IF/THEN 决策分支

- IF 市场处于恐慌状态（VIX > 30）→ THEN 启动逆向投资检查清单，评估是否为买入机会
- IF 持仓集中度 > 40%（单只股票）→ THEN 触发分散化建议，降低单一风险
- IF 浮亏 > 20% → THEN 启动止损审查，判断是基本面变化还是市场波动
- ELSE（市场平稳 + 持仓合理）→ THEN 输出维持建议 + 定投计划



## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析结果 |
| confidence | number | 置信度 |

## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常分析 | 完整持仓+市场数据 | 投资建议+风险提示 | 逻辑清晰 + 风险可控 |
| 2 | 恐慌市场 | VIX=35 + 持仓下跌 | 逆向投资检查清单 | 不追涨杀跌 |
| 3 | 集中持仓 | 单只占比 50% | 分散化方案 | 渐进式调整 |
| 4 | 深度浮亏 | 浮亏 25% | 止损审查报告 | 区分基本面 vs 波动 |
| 5 | 数据不全 | 缺少持仓明细 | 数据补全清单 | 不编造持仓 |

