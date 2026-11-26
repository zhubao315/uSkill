---
name: uskill-ai-engineering-technical-database-selection
description: "让technical database selection变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-database-selection.md"
  original_id: "SKL-5126"
  version: "3.0.0"
  trust: untrusted
---

# technical database selection

# Database Selection Decision

> **角色**: 数据架构师 | **核心工具**: AI大模型, 性能基准测试, 数据模型分析 | **效率目标**: 系统化数据库选型，避免选型失误导致的技术债务

## 🎯 目标

基于**数据特征、访问模式和业务需求**，构建科学的数据库选型决策框架，在关系型、文档型、键值、列族、图、时序等多种数据库中做出最优选择。

**适用场景**:
1. **新项目选型** — 为新系统选择主数据库
2. **多数据库架构** — 为不同场景选择互补的数据库组合
3. **数据库迁移** — 评估是否需要从现有数据库迁移到更合适的方案

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `data_characteristics` | object | ✅ | 数据特征：`{structure, volume, velocity, variety, lifecycle}` |
| `access_patterns` | array | ✅ | 主要访问模式：读写比、查询复杂度、热点分布 |
| `consistency_requirement` | enum | ✅ | `strong` / `eventual` / `mixed` |
| `scale_requirement` | object | ✅ | 规模需求：`{data_size, qps, concurrent_connections}` |
| `team_expertise` | array | ❌ | 团队熟悉的技术栈 |
| `budget` | enum | ❌ | `open_source_only` / `moderate` / `enterprise`，默认 `moderate` |
| `compliance` | array | ❌ | 合规要求（数据本地化、加密、审计等） |

## 📤 输出

```json
{
  "primary_recommendation": {
    "database": "string — 推荐数据库名称",
    "category": "enum — RDBMS / document / key-value / column-family / graph / time-series / search",
    "rationale": "string — 选择理由",
    "pros": ["string"],
    "cons": ["string"]
  },
  "alternative_options": [
    {
      "database": "string",
      "category": "string",
      "rationale": "string",
      "trade_offs": "string — 与首选方案的权衡"
    }
  ],
  "polyglot_persistence": {
    "needed": "boolean — 是否需要多数据库组合",
    "components": [
      {"database": "string", "purpose": "string", "data_ownership": "string"}
    ]
  },
  "architecture_guidance": {
    "data_model": "string — 数据模型建议",
    "sharding_strategy": "string — 分片策略",
    "replication_strategy": "string — 复制策略",
    "caching_layer": "string — 缓存层建议",
    "backup_strategy": "string — 备份策略"
  },
  "migration_path": {
    "complexity": "enum — low / medium / high",
    "estimated_duration": "string",
    "key_steps": ["string"]
  },
  "tco_estimate": {
    "monthly_cost": "string — 月度成本估算",
    "cost_breakdown": "string — 成本构成"
  }
}
```

## 📋 执行步骤

### 阶段一：需求分析与数据特征画像

1. **数据结构分析** — 判断数据特征：
   - 高度结构化（表格/关系明确） → 关系型
   - 半结构化（JSON/XML/灵活Schema） → 文档型
   - 时序数据（带时间戳的指标/日志） → 时序数据库
   - 关系网络（社交关系/知识图谱） → 图数据库
   - 简单键值对（缓存/会话/配置） → 键值存储
2. **访问模式分析** — 明确读写比、查询模式、聚合需求
3. **规模与性能需求** — 量化数据量、QPS、延迟要求
4. **一致性需求** — 确定强一致性/最终一致性的边界

### 阶段二：数据库类型匹配

5. **关系型 (MySQL/PostgreSQL/TiDB)**:
   - ✅ 适用：复杂查询、事务一致性、成熟生态
   - ❌ 不适用：极高写入吞吐、灵活Schema、超大规模
6. **文档型 (MongoDB/CouchDB)**:
   - ✅ 适用：灵活Schema、快速迭代、内容管理
   - ❌ 不适用：复杂跨文档事务、强关系查询
7. **列族 (Cassandra/HBase)**:
   - ✅ 适用：超大规模写入、时序数据、宽表查询
   - ❌ 不适用：复杂事务、随机读取密集
8. **键值 (Redis/DynamoDB)**:
   - ✅ 适用：缓存、会话、排行榜、简单查询
   - ❌ 不适用：复杂查询、大数据量持久存储
9. **图 (Neo4j/JanusGraph)**:
   - ✅ 适用：关系查询、路径分析、推荐系统
   - ❌ 不适用：简单CRUD、大规模聚合
10. **时序 (InfluxDB/TimescaleDB/TDengine)**:
    - ✅ 适用：IoT数据、监控指标、日志分析
    - ❌ 不适用：复杂关系、事务操作
11. **搜索 (Elasticsearch/MeiliSearch)**:
    - ✅ 适用：全文搜索、日志分析、聚合分析
    - ❌ 不适用：主数据存储、强一致性

### 阶段三：候选方案评估

12. **生成候选列表** — 匹配2-3个候选数据库
13. **维度打分** — 从以下维度评估：
    - 功能匹配度（30%）
    - 性能/可扩展性（25%）
    - 运维复杂度（15%）
    - 社区/生态成熟度（15%）
    - 成本（15%）
14. **多数据库组合评估** — 判断是否需要polyglot persistence

### 阶段四：架构指导与迁移规划

15. **数据模型设计** — 根据选定数据库设计最优数据模型
16. **分片与复制策略** — 设计水平扩展和高可用方案
17. **迁移路径规划** — 如果涉及迁移，制定详细的迁移计划
18. **TCO估算** — 计算包含许可、运维、人力的总拥有成本

## ✅ 检查清单

- [ ] 数据特征和访问模式是否已充分分析
- [ ] 是否评估了至少2个候选方案
- [ ] 是否考虑了3-5年的数据增长预期
- [ ] 团队是否具备所选数据库的运维能力
- [ ] 是否考虑了备份恢复和灾难恢复方案
- [ ] 是否评估了云托管 vs 自建的利弊
- [ ] 多数据库方案的数据一致性是否已明确
- [ ] 是否有性能基准测试数据支撑

## ⚠️ 常见陷阱

| 陷阱 | 说明 | 规避方法 |
|------|------|---------|
| 锤子找钉子 | 熟悉MySQL就什么都用MySQL | 以需求驱动选型，而非技术偏好 |
| 过度设计 | 小项目就上分布式数据库 | 从简开始，按需演进 |
| 忽视运维成本 | 选了牛逼的数据库但没人会运维 | 团队能力是重要选型依据 |
| CAP理论忽视 | 不理解一致性/可用性/分区容错的权衡 | 明确业务对一致性和可用性的要求 |
| 盲目追新 | 跟风选择最新最热的数据库 | 优先选择经过生产验证的方案 |

## 🔗 关联

- **相关技能**: 微服务拆分决策, 缓存架构设计, 消息队列选型
- **推荐工具**: db-benchmark.com, Jepsen测试报告
- **经典著作**: 《Designing Data-Intensive Applications》— Martin Kleppmann


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
