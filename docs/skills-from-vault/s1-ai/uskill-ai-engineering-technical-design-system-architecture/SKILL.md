---
name: uskill-ai-engineering-technical-design-system-architecture
description: "让technical design system architecture变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-design-system-architecture.md"
  original_id: "SKL-6867"
  version: "3.0.0"
  trust: untrusted
---

# technical design system architecture

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

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
