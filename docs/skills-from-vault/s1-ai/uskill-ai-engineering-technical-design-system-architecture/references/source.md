# System Design Analysis

## 🎯 目标
> 将业务需求转化为 AI-Native、云原生的系统架构设计，输出完整的架构文档，包括 C4 模型、ADR 和 LLMOps 治理框架。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `business_requirements` | string | ✅ | BRD/PRD 或业务需求描述 |
| `system_type` | enum | ❌ | `Type-A`(传统) / `Type-B`(部分AI) / `Type-C`(全栈AI-Native)，默认自动判断 |
| `budget_monthly` | number | ❌ | 月度预算上限（元），用于成本约束 |
| `team_skill_level` | enum | ❌ | `junior` / `mid` / `senior`，默认 `mid` |

## 📤 输出

```json
{
  "system_type": "Type-A | Type-B | Type-C",
  "requirements_report": {
    "business_flows": "string — Mermaid 流程图",
    "ai_decision_points": [{"name": "string", "latency_ms": "int", "accuracy_pct": "number", "data_dep": "string"}],
    "moscow": {"must": ["string"], "should": ["string"], "could": ["string"]},
    "non_functional": {"qps": "int", "inference_latency_p95_ms": "int", "monthly_token_k": "number", "monthly_cost_yuan": "number"}
  },
  "architecture_options": [
    {
      "name": "string",
      "tech_stack": "string",
      "dev_weeks": "int",
      "latency_p95_ms": "int",
      "monthly_cost_yuan": "number",
      "model_control": "low | mid | high",
      "risk": ["string"],
      "recommended": "boolean"
    }
  ],
  "c4_models": {
    "context_diagram": "string — PlantUML",
    "container_diagram": "string — PlantUML",
    "component_diagram": "string — PlantUML"
  },
  "adr_list": [{"title": "string", "decision": "string", "rationale": "string", "tradeoffs": "string"}],
  "llmops_strategy": {
    "model_selection": "string",
    "token_budget_yuan": "number",
    "degradation_chain": ["string"],
    "circuit_breaker": "string",
    "caching_strategy": "string"
  },
  "observability": {
    "metrics": ["string"],
    "alert_rules": ["string"],
    "cost_tracking": "string"
  },
  "risks": [{"name": "string", "level": "high | mid | low", "mitigations": ["string"], "owner": "string"}],
  "implementation_roadmap": [{"phase": "string", "duration_weeks": "int", "deliverables": ["string"]}]
}
```

## 📋 执行步骤

1. **场景预诊断** — 分析 `business_requirements`，判断系统复杂度（Type-A/B/C），确定后续流程深度
2. **需求分析** — 提取核心业务流程（Mermaid），识别 AI 决策点地图，MoSCoW 分类，量化非功能需求（QPS/延迟/Token/成本）
3. **架构方案生成** — 生成 2-3 个备选方案（轻量级/中量级/重量级），从技术成熟度、开发周期、推理延迟、Token 成本、模型可控性、团队技能 6 维对比，输出成本对比表和选型矩阵
4. **详细设计** — 生成 C4 三层模型（Context/Container/Component），为 AI 组件设计数据模型（AIRequest/AIResponse/ModelVersion），设计 RAG Pipeline、Prompt Manager、Model Selector、Output Validator
5. **部署与可观测性** — 设计 K8s 部署方案（Deployment/StatefulSet/HPA），定义 AI 特有监控指标（Token 消耗、推理延迟、幻觉率、成本），设计降级/熔断/缓存策略
6. **风险评估** — 识别 AI 特有风险（幻觉/隐私/投毒/漂移/Lock-in/成本失控）、云安全风险、运维风险，为每个高风险设计 ≥2 个缓解方案
7. **文档汇总** — 汇总为完整架构文档（执行摘要→需求→选型→设计→部署→成本→风险→路线图），以"挑剔的 CTO"视角终审

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `business_requirements` 过于模糊 | 返回 `ERROR_VAGUE_INPUT` + 需澄清的问题清单 |
| 预算无法支撑任何方案 | 返回 `WARNING_BUDGET_INSUFFICIENT` + 最低成本方案及缺口 |
| 团队技能不足以实施首选方案 | 降低方案复杂度 + 附加培训计划 |
| AI 决策点无法量化准确率要求 | 标记为 `UNVALIDATED` + 建议 A/B 测试验证 |

## ✅ 自检清单

- [ ] 输出包含 `system_type` 分类
- [ ] 至少识别 2 个核心 AI 决策点
- [ ] 提供 2-3 个架构方案及多维对比
- [ ] C4 模型包含 Context + Container + Component 三层
- [ ] LLMOps 策略包含降级链和熔断机制
- [ ] 风险清单 ≥ 7 项，每项有 ≥ 2 个缓解方案
- [ ] 成本预测包含 LLM Token 费用


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-01 转化 |

---
**相关笔记**：[[AI时代工程团队管理-宣讲文案]] [[全栈功能开发]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [学习任务] for [知识背景], with [学习目标], leaning toward [学习方法/输出形式]."

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
| ""以后再整理笔记"" | "以后不会来，现在就做" |
| ""读完就行了"" | "没有输出的阅读是自我感动" |
| ""这个太简单不用记"" | "简单的知识最容易忘" |
| ""收藏=学会"" | "收藏夹是知识的坟墓" |
| ""看完再总结"" | "看完就忘，边读边记才是正道" |

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
