---
name: uskill-ai-engineering-architecture-design-system
description: "让architecture design system变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-architecture-design-system.md"
  original_id: "SKL-6865"
  version: "3.0.0"
  trust: untrusted
---

# architecture design system

# System Architecture Design

## 🎯 目标
> 设计 AI 原生、云原生、LLMOps 就绪的系统架构，将 AI 能力从"辅助功能"升级为"架构核心"，在 3.5 小时内完成架构初稿。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `business_context` | string | ✅ | 业务背景描述 / BRD / PRD |
| `requirements` | string | ✅ | 功能与非功能需求列表 |
| `constraints` | object | ❌ | 技术约束（预算、团队规模、合规要求） |
| `existing_system` | string | ❌ | 现有系统架构描述（重构场景） |
| `ai_decision_points` | list | ❌ | 已知的 AI 决策点清单 |

## 📤 输出

```json
{
  "scenario_type": "Type-A | Type-B | Type-C",
  "requirements_report": {
    "core_flows": "string — Mermaid 流程图",
    "ai_decision_map": [{"point": "string", "latency_ms": "int", "accuracy": "float", "data_dep": "string"}],
    "non_functional": {"qps": "int", "inference_p95_ms": "int", "token_budget_monthly": "int", "llm_cost_budget": "float"}
  },
  "architecture_options": [
    {
      "name": "string — 方案名称",
      "tech_stack": ["string"],
      "dev_weeks": "int",
      "inference_p95_ms": "int",
      "monthly_cost": "float",
      "risk": ["string"],
      "recommended": "boolean"
    }
  ],
  "c4_diagrams": {
    "context": "string — PlantUML 代码",
    "container": "string — PlantUML 代码",
    "component": "string — PlantUML 代码"
  },
  "adr_decisions": [{"id": "string", "context": "string", "decision": "string", "rationale": "string"}],
  "llmops_strategy": {
    "model_chain": ["string — 降级链"],
    "circuit_breaker": "string — 熔断策略",
    "cache_strategy": "string",
    "rate_limit": "string"
  },
  "observability": {
    "metrics": ["string — Prometheus 指标"],
    "alerts": [{"metric": "string", "threshold": "string", "action": "string"}],
    "tracing_spans": ["string"]
  },
  "risks": [{"risk": "string", "severity": "high|medium|low", "mitigations": ["string"], "owner": "string"}],
  "implementation_roadmap": [{"phase": "string", "duration": "string", "deliverables": ["string"]}]
}
```

## 📋 执行步骤

1. **场景预诊断** — 分析 `business_context`，判断系统类型（Type-A 传统 / Type-B 部分 AI / Type-C 全栈 AI-Native）
2. **需求深度分析** — 识别 AI 决策点（≥ 3 个），量化非功能需求（QPS / 推理延迟 / Token 消耗 / 成本预算），用 MoSCoW 法则划分优先级
3. **生成备选方案** — 输出 2-3 个架构方案（轻量级外部 API / 中量级开源模型 / 重量级自训练），附 12 个月成本对比表和选型矩阵
4. **C4 模型设计** — 生成 Context → Container → Component 三层 PlantUML 代码，AI 组件层包含 Prompt Manager / Model Selector / RAG Pipeline / Output Validator / Feedback Loop
5. **LLMOps 策略制定** — 设计模型降级链、熔断策略、缓存策略、速率限制、成本追踪方案
6. **可观测性设计** — 定义 AI 特有 Prometheus 指标（Token 消耗率 / 推理延迟 P95 / 幻觉率 / 成本 per request），配置告警阈值
7. **风险评估** — 识别 AI 特有风险（幻觉 / 隐私泄露 / 模型漂移 / Vendor Lock-in）和云安全风险，每个高风险 ≥ 2 个缓解方案
8. **架构决策记录** — 生成 ≥ 5 个核心 ADR，包含决策背景、选项对比、权衡分析
9. **文档汇总** — 按执行摘要 → 需求分析 → 架构选型 → 详细设计 → 部署方案 → 成本 ROI → 风险评估 → 路线图结构输出完整文档
10. **终审检查** — 以"挑剔的 CTO"视角检查前后逻辑一致性、技术债、成本模型现实性

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `business_context` 信息不足 | 返回所需信息清单，请求补充 |
| 需求存在矛盾 | 标注矛盾点，给出推荐解释方案 |
| AI 决策点 < 3 个 | 建议降级为 Type-A 传统架构 |
| Token 预算超出约束 | 自动切换到更经济的模型方案 |
| PlantUML 生成失败 | 降级为 Mermaid 或文字描述 |

## ✅ 自检清单

- [ ] 场景类型判断准确（Type-A/B/C）
- [ ] AI 决策点 ≥ 3 个，含延迟和准确率要求
- [ ] 非功能需求已量化（QPS / 推理延迟 / Token 预算 / 成本）
- [ ] 架构方案 ≥ 2 个，含 12 个月成本对比
- [ ] C4 图三层完整，AI 组件角色清晰
- [ ] ADR ≥ 5 个，含权衡分析
- [ ] 风险 ≥ 7 个，每个高风险有 ≥ 2 个缓解方案
- [ ] 降级链路完整，含完全失败 fallback
- [ ] 成本告警阈值已设置
- [ ] 文档覆盖全部 6 个交付物


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

| 日期 | 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
