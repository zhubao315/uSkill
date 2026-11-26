---
name: uskill-ai-engineering-technical-microservice-decomposition
description: "让technical microservice decomposition变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-microservice-decomposition.md"
  original_id: "SKL-6858"
  version: "3.0.0"
  trust: untrusted
---

# technical microservice decomposition

- 维度/学习
- 类型/方法
aliases:
- 微服务
# Microservice Decomposition Decision

> **角色**: 系统架构师 | **核心工具**: AI大模型, 架构分析工具, DDD建模 | **效率目标**: 结构化微服务拆分决策，降低架构演进风险

## 🎯 目标

构建从**单体到微服务**的系统化拆分决策框架，基于领域驱动设计(DDD)识别业务边界，通过量化评估确定拆分优先级，确保架构演进有序可控。

**适用场景**:
1. **单体应用拆分** — 现有单体系统面临扩展瓶颈，需要逐步拆分为微服务
2. **新系统架构设计** — 从零设计微服务架构，确定服务边界
3. **现有微服务重构** — 已有微服务架构但边界不合理，需要重新划分

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `system_description` | string | ✅ | 当前系统描述（功能模块、技术栈、团队规模） |
| `pain_points` | array | ✅ | 当前架构痛点列表 |
| `business_domains` | array | ✅ | 核心业务领域描述 |
| `team_structure` | object | ✅ | 团队结构：`{team_count, team_sizes, team_skills}` |
| `deployment_env` | enum | ❌ | `kubernetes` / `ecs` / `bare_metal`，默认 `kubernetes` |
| `traffic_pattern` | object | ❌ | 流量特征：`{peak_qps, avg_qps, growth_rate}` |
| `data_constraints` | object | ❌ | 数据约束：`{data_volume, consistency_requirement, compliance}` |

## 📤 输出

```json
{
  "domain_analysis": {
    "bounded_contexts": [
      {
        "name": "string — 限界上下文名称",
        "core_domain": "boolean — 是否核心域",
        "capabilities": ["string — 包含的业务能力"],
        "entities": ["string — 核心实体"],
        "events": ["string — 领域事件"]
      }
    ],
    "context_map": [
      {"from": "string", "to": "string", "relationship": "string — 上下游/共享内核/防腐层"}
    ]
  },
  "service_proposal": [
    {
      "service_name": "string",
      "responsibility": "string — 职责描述",
      "bounded_context": "string — 对应限界上下文",
      "split_priority": "enum — P0 / P1 / P2",
      "split_rationale": "string — 拆分理由",
      "dependencies": ["string — 依赖的其他服务"],
      "data_ownership": "string — 拥有的数据",
      "estimated_effort": "string — 预估工作量"
    }
  ],
  "migration_roadmap": {
    "phase_1": {"services": ["string"], "duration": "string", "goal": "string"},
    "phase_2": {"services": ["string"], "duration": "string", "goal": "string"},
    "phase_3": {"services": ["string"], "duration": "string", "goal": "string"}
  },
  "risk_assessment": {
    "technical_risks": [{"risk": "string", "mitigation": "string"}],
    "organizational_risks": [{"risk": "string", "mitigation": "string"}],
    "anti_patterns_to_avoid": ["string"]
  },
  "infrastructure_requirements": {
    "service_mesh": "boolean",
    "api_gateway": "boolean",
    "config_center": "boolean",
    "distributed_tracing": "boolean",
    "circuit_breaker": "boolean"
  }
}
```

## 📋 执行步骤

### 阶段一：现状评估与拆分必要性判断

1. **架构痛点诊断** — 分析当前架构的核心问题：
   - 部署耦合：改一行代码需要部署整个系统？
   - 扩展瓶颈：无法对高负载模块独立扩容？
   - 团队瓶颈：多团队频繁代码冲突？
   - 技术栈僵化：无法为特定场景选择最优技术？
2. **拆分必要性评分** — 评估是否真正需要微服务（警惕"简历驱动开发"）
3. **确定拆分约束** — 明确团队规模、时间窗口、基础设施成熟度

### 阶段二：领域建模与边界识别

4. **事件风暴 (Event Storming)** — 组织跨职能工作坊，梳理业务领域事件
5. **识别限界上下文** — 基于DDD方法划分业务边界：
   - **核心域**: 企业核心竞争力所在，投入最多资源
   - **支撑域**: 为核心域提供支撑，可自建或外购
   - **通用域**: 通用能力（用户、权限、通知），可直接购买
6. **绘制上下文映射** — 定义限界上下文之间的关系和交互模式
7. **验证边界合理性** — 检查：每个上下文是否可以独立演进？数据归属是否清晰？

### 阶段三：服务拆分方案设计

8. **确定拆分策略**:
   - **绞杀者模式 (Strangler Fig)**: 逐步将功能从单体迁移到新服务
   - **分支 by 抽取 (Branch by Abstraction)**: 先抽象接口，再替换实现
   - **并行运行 (Parallel Run)**: 新旧系统并行，逐步切换流量
9. **服务粒度评估** — 使用量化标准：
   - 单个服务代码量 < 5万行
   - 团队1个披萨团队（5-8人）可以完全拥有
   - 服务可以独立部署、独立扩缩
10. **定义服务契约** — 确定API规范、事件格式、数据所有权

### 阶段四：迁移路线图制定

11. **拆分优先级排序** — 按以下维度评分：
    - 业务价值/痛点缓解度
    - 技术可行性/风险
    - 团队能力/学习曲线
12. **制定分阶段路线图** — 每个阶段明确服务列表、时间估算、里程碑
13. **基础设施规划** — 确定所需的基础设施组件（服务网格、配置中心、链路追踪等）
14. **风险评估与缓解** — 识别技术风险和组织风险，制定缓解措施

## ✅ 检查清单

- [ ] 是否进行了领域建模（事件风暴/领域分析）
- [ ] 每个服务的数据所有权是否明确
- [ ] 服务间通信方式是否确定（同步REST/gRPC vs 异步消息）
- [ ] 是否考虑了分布式事务处理方案
- [ ] 是否规划了服务发现、配置管理、监控告警
- [ ] 团队是否具备运维微服务的能力
- [ ] 迁移方案是否支持灰度发布和回滚
- [ ] 是否评估了不拆分的方案

## ⚠️ 常见陷阱

| 陷阱 | 说明 | 规避方法 |
|------|------|---------|
| 过早拆分 | 业务不成熟就拆微服务，增加复杂度 | 优先优化单体，实在不行再拆 |
| 分布式单体 | 拆了服务但仍然紧密耦合 | 严格遵守异步通信和独立部署 |
| 数据库共享 | 多个服务共享同一数据库 | 每个服务拥有独立数据存储 |
| 粒度过细 | 服务拆得太细，运维成本爆炸 | 遵循"两个披萨团队"原则 |
| 忽略组织架构 | 技术架构与组织架构不匹配 | 康威定律：架构应映射组织结构 |
| 缺少可观测性 | 分布式系统排障困难 | 必须先建设日志/指标/追踪三大支柱 |

## 🔗 关联

- **相关技能**: 数据库选型决策, 缓存架构设计, 消息队列选型, CI-CD流水线设计
- **推荐工具**: 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
