---
name: uskill-cognition-cognitive-adversarial-investment-research
description: "让cognitive adversarial investment research变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-adversarial-investment-research.md"
  original_id: "SKL-5040"
  version: "3.0.0"
  trust: untrusted
---

# cognitive adversarial investment research

# Adversarial Investment Research System

## 🎯 目标
> 构建基于 MoA（Mixture of Agents）架构的对抗性投研系统，通过 4 个 Agent 角色辩论生成高胜率投资决策，结合独立风控实现"幸存者策略"输出。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `target_asset` | string | ✅ | 投资标的（股票代码/币种） |
| `market_data` | object | ✅ | 行情数据：K线、成交量、技术指标 |
| `fundamental_data` | object | ❌ | 基本面数据：PE/PB/ROE/现金流 |
| `news_context` | string | ❌ | 相关新闻与市场情绪摘要 |
| `portfolio_state` | object | ❌ | 当前持仓状态与资金余额 |
| `risk_params` | object | ❌ | 风控参数：最大回撤阈值、单票仓位上限，默认 `{max_drawdown_pct: 15, max_single_pct: 20}` |
| `debate_rounds` | int | ❌ | 辩论轮数，默认 `3` |

## 📤 输出

```json
{
  "debate_summary": {
    "agent_aggressive": {"signal": "buy|sell|hold", "confidence": 0-100, "reasoning": "string", "target_price": "number", "stop_loss": "number"},
    "agent_conservative": {"signal": "buy|sell|hold", "confidence": 0-100, "reasoning": "string", "safety_margin_pct": "number"},
    "agent_referee": {"final_signal": "buy|sell|hold", "confidence": 0-100, "position_pct": "0-100", "reflection": "string"},
    "agent_risk_officer": {"veto": "boolean", "risk_level": "low|mid|high|critical", "alert": "string|null", "black_swan_flags": ["string"]}
  },
  "action": {
    "decision": "buy|sell|hold|forced_cash",
    "position_pct": "number",
    "entry_price": "number",
    "stop_loss": "number",
    "take_profit": "number",
    "hold_days_range": "[min, max]"
  },
  "audit": {
    "debate_log": "string — 完整辩论记录",
    "consensus_score": "0-100 — A/B一致性",
    "risk_check_passed": "boolean"
  }
}
```

## 📋 执行步骤

1. **收集市场数据** — 获取 `target_asset` 的行情、基本面、新闻数据，清洗并计算技术指标（RSI/MACD/布林带）
2. **启动激进派分析** — Agent A 以动量策略视角分析：识别突破信号、资金流向、成交量突变，输出买入/卖出/持有建议与目标价位
3. **启动保守派分析** — Agent B 以价值投资视角分析：评估估值分位数、安全边际、宏观周期，输出持有/观望建议
4. **执行对抗辩论** — 将 A/B 完整论证输入辩论协调器，进行 `debate_rounds` 轮交叉质询，记录分歧点与论据
5. **裁判官综合决策** — Agent C 接收辩论记录，执行 Reflection 机制：假设 A 错误的原因 + 假设 B 错误的原因，输出置信度评分与仓位建议
6. **风控官独立审查** — Agent D 独立扫描黑天鹅指标（地缘政治、监管政策、异常波动），检查回撤阈值，行使一票否决权
7. **生成执行指令** — 综合裁判官建议与风控结果，输出最终决策（含入场价、止损、止盈、持仓周期）
8. **记录辩论日志** — 保存完整辩论过程、Agent 分歧点、置信度，用于后续回测与策略优化

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 市场数据缺失或延迟 | 使用本地缓存最近数据 + 标记 `DATA_STALE` 警告 |
| Agent 输出格式异常 | 重试 1 次后降级为保守策略（hold） |
| A/B 辩论无法收敛 | Agent C 强制裁决 + 降低仓位至 50% |
| 风控官触发否决 | 直接输出 `forced_cash`，忽略其他 Agent 建议 |
| 黑天鹅事件（波动率骤升/熔断） | 立即清仓 + 发送告警 + 记录事件 |
| 推理延迟 > 5s | 降级到轻量模型或单 Agent 决策 |

## ✅ 自检清单

- [ ] 输出包含 4 个 Agent 的独立分析结果
- [ ] 辩论轮数 ≥ 1，每轮有完整论据记录
- [ ] 裁判官 Reflection 包含双向假设分析
- [ ] 风控官输出包含黑天鹅标志检查
- [ ] 仓位建议在风控参数范围内
- [ ] 止损/止盈价位已计算且合理（止损 ≤ -8%）
- [ ] 辩论日志完整可追溯


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
**相关笔记**：[[行为洞察分析旧版]] [[AI 目标审计]] 


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
| "

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
