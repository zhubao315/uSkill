
# Dynatrace Agent Builder + 自治SRE深度研究

> 数据源：Dynatrace 官方新闻稿(2026-07-27) / The New Stack / Help Net Security / AI Agent Store
> 研究日期：2026-07-28

---

## 1. 发布概述

Dynatrace 于 2026-07-27 宣布 Dynatrace Intelligence 的重大升级，核心是从"洞察"到"自主执行"的跨越。这不仅仅是增量更新——这是 Dynatrace 将其可观测性平台定位为**企业级 Agent 控制平面**的战略宣言。

### 时间线

| 时间 | 里程碑 |
|------|--------|
| 2026-01 | Perform 2026：发布 Dynatrace Intelligence（融合确定性分析+agentic AI） |
| 2026-07-27 | Intelligence 重大升级：自治 SRE Agent + Agent Builder + 扩展集成 |
| 2026-08 | 自治 SRE Agent 和 Agent Builder 正式可用（预计） |

### 核心定位

> "Most observability platforms stop at data. With these advancements, we're helping organizations move from **understanding problems to resolving them automatically**." — Steve Tack, CPO

---

## 2. 五大核心组件

### 2.1 Autonomous SRE Agent
- **触发方式**：对新检测到的问题自动触发
- **工作流**：判断是否属于已有调查 → 如是，则丰富调查内容并更新问题引用
- **关键设计**：不是二选一（人类 vs 平台），而是"爬-走-跑"渐进信任

### 2.2 Cloud SRE Agent
- **多云协调**：在 AWS / Azure / GCP 之间协调修复活动
- **输出**：统一的可审计记录（single auditable record）
- **状态**：当前 SaaS 客户可立即使用（DPS 上）

### 2.3 Agent Builder 🌟（核心关注点）
- **无代码**：可视化拖拽式 Agent 创建
- **自定义**：针对客户特有的运维工作流
- **部署方式**：一键部署到 Dynatrace 平台
- **状态**：预计 2026-08 可用（当前不可用）

### 2.4 Enhanced Dynatrace Assist
- 自然语言调查能力
- Agent-ready 工作流（向更多用户开放）
- **状态**：当前可用

### 2.5 扩展集成生态
| 集成层 | 具体 |
|--------|------|
| 云平台 | AWS / Azure / GCP |
| ITSM | ServiceNow / Atlassian / PagerDuty |
| 开发者工具 | GitHub / CI/CD 工具链 |
| AI | 其他 AI 技术集成 |

---

## 3. 关键技术架构：确定性 vs 概率性

这是 Dynatrace 最核心的技术主张。

### 传统 AIOps 的问题
- 多数 AI 系统依赖概率输出（probabilistic outputs）
- IDC 副总裁 Stephen Elliot: "AI-generated insight → safe, governed execution 之间的差距是最大担忧"
- 概率性导致运维团队不信任自动执行

### Dynatrace 的答案
- **因果 AI 引擎（Causal AI Engine）**：基于确定性、实时的系统理解
- 每步执行扎根于环境特定上下文（environment-specific context）
- 执行过程：透明、可审计、受控（transparent, auditable, governed）

```
传统流：数据 → 洞察 → 人工分析 → 人工执行
Dynatrace：数据 → 洞察 → 确定性上下文 → 自动执行（人类监督）
```

---

## 4. 发布节奏：爬-走-跑模型

Steve Tack 强调的三个阶段：

| 阶段 | 信任基础 | 人类参与 | 状态 |
|:----:|---------|:--------:|:----:|
| 爬 | 确定性 AI 精确定位根因 | 人参与回路 | ✅ 当前 |
| 走 | 基于定位+预测的修复自动化 | 人参与回路 | ✅ 当前 |
| 跑 | 人仅在回路上（Human-on-the-loop） | 人监督 | 🚧 逐步推进 |

> "The measure of success isn't how productive your engineers are — it's the percentage of incidents that never need a human at all." — Steve Tack

---

## 5. 战略分析：可观测性 → Agent OS

### Dynatrace 的战略逻辑
Futurum Group 在 Perform 2026 分析中指出：

**核心论点：可观测性正在成为 Agent 的操作系统。**
- 从 "observability as feedback" → "observability as an active participant in delivery workflows"
- Dynatrace 正在从运维扩展到 DevOps/开发者层面（operate-to-code 闭环）
- 生产环境的真实数据反馈到软件变更和发布决策

### 竞品格局
- **Dynatrace 本次发布**：自治 SRE Agent + Builder + 集成，最早面向 enterprise 提供完整的 Agent 控制平面
- **ServiceNow**：ITSG + AI Agent（相同赛道）
- **Microsoft**：Azure AI Agent + Fabric（更偏向云原生）
- **Datadog**：Bits AI（自然语言查询，尚无自主执行 Agent）
- **Splunk（Cisco）**：AI Assistant，Agent 能力有限
- **New Relic**：AI 辅助分析，无 Agent Builder

### 关键问题
1. **一家厂商控制权问题**：企业愿意将操作权威（operational authority）集中在一个平台吗？
   - Dynatrace 对外定位是"互补而非替代"——强调与云提供商和 ITSM 的集成
   - Futurum 观点：这是"early advantage vs single vendor control"的张力
2. **Agent Builder 的实际能力**：无代码到何种程度？是否支持 MCP？是否支持外部 LLM 选择？
   - 目前公开信息太少——预计 8 月上线后才明朗
3. **信任与监管合规**：在金融/医疗等受监管行业，审计轨迹是否满足要求？

---

## 6. 与同领域的横向比较

| 维度 | Dynatrace | Datadog Bits AI | ServiceNow AI Agent | Huawei AgentSphere |
|:----:|:---------:|:---------------:|:-------------------:|:------------------:|
| 无代码 Builder | ✅ Agent Builder（8月） | ❌ | ❌ | ❌ |
| 自治 SRE Agent | ✅ Autonomous + Cloud SRE | ❌ 仅查询 | ❌ | ❌ |
| 确定性因果 AI | ✅ Causal AI Engine | ❌ 概率性 | ❌ | ❌ |
| 多云修复 | ✅ | ❌ | ❌ Only AWS | ❌ Only Huawei |
| ITSM 集成 | ServiceNow/Atlassian/PagerDuty | ❌ | 原生 | ❌ |
| 当前可用 | 部分功能 | ✅ | ✅ | ✅ 泰国首发 |

---

## 7. 对工程师的启示

### 对可观测性选型的意义
- 如果团队正在评估可观测性平台，Dynatrace 的自治 Agent 能力可能是决定性因素
- 但需注意：8 月之前看不见 Agent Builder 的实际体验——先不要仅凭评测做决策

### 对 Agent 工程范式的意义
- Dynatrace 采用的是**确定性优先**的 Agent 设计哲学——与纯 LLM-based Agent（如 AutoGPT 等）形成对比
- 关键洞察：**生产运维 Agent 不能容忍幻觉**——这就是为何 Dynatrace 坚持因果 AI 引擎
- 与我们的 RCARE 脚手架有相通之处：都强调可审计、可追溯、人类在回路

### 对"驾驭工程"维度（我们的系统3）
- 2027 年可能是"自治 SRE 元年"——但当前爬-走-跑模型意味着大多数企业仍处在"爬"阶段
- Dynatrace 是最早系统化提出 **Human-on-the-loop** 而非 Human-in-the-loop 的大型平台之一

---

## 8. 相关阅读

- [[RCARE：标准化人机对话脚手架]]（架构设计理念相通）
- [[系统3校准-Day5-涌现判定扩展]]（Agent 涌现行为与可控性的边界）

---

*数据采集时间：2026-07-28 14:30 CST | 信息来源：Dynatrace Official PR、The New Stack、Help Net Security、Futurum Group、AI Agent Store*
