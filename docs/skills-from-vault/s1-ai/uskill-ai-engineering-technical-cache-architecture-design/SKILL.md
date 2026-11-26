---
name: uskill-ai-engineering-technical-cache-architecture-design
description: "让technical cache architecture design变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-cache-architecture-design.md"
  original_id: "SKL-5127"
  version: "3.0.0"
  trust: untrusted
---

# technical cache architecture design

# Cache Architecture Design

> **角色**: 后端架构师 | **核心工具**: AI大模型, Redis, 本地缓存库 | **效率目标**: 系统化多级缓存设计，平衡性能与一致性

## 🎯 目标

构建**多级缓存架构**，在L1本地缓存、L2分布式缓存和L3持久化存储之间实现最优平衡，解决缓存穿透、雪崩、击穿等经典问题，保证数据最终一致性。

**适用场景**:
1. **高并发读优化** — 热点数据读取QPS极高，数据库无法承受
2. **响应延迟优化** — API响应时间要求从100ms降至10ms以内
3. **多级缓存体系建设** — 从零设计或优化现有缓存架构

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `system_profile` | object | ✅ | 系统概况：`{qps, read_write_ratio, latency_target, data_size}` |
| `data_access_patterns` | array | ✅ | 数据访问模式列表：`{data_type, hotness, update_frequency, consistency_need}` |
| `current_architecture` | string | ❌ | 当前架构描述（如有） |
| `infrastructure` | object | ❌ | 基础设施：`{redis_cluster, memory_budget, network_bandwidth}` |
| `consistency_tolerance` | enum | ❌ | `strong` / `eventual_with_bound` / `eventual`，默认 `eventual_with_bound` |

## 📤 输出

```json
{
  "cache_topology": {
    "levels": [
      {
        "level": "int",
        "name": "string — L1/L2/L3",
        "technology": "string — Caffeine/Redis/MySQL",
        "capacity": "string",
        "ttl_range": "string",
        "data_scope": "string — 该层缓存的数据范围"
      }
    ],
    "data_flow": "string — 数据流向描述"
  },
  "strategy_per_data_type": [
    {
      "data_type": "string",
      "cache_pattern": "enum — cache-aside / read-through / write-through / write-behind",
      "ttl": "string",
      "invalidation_strategy": "string",
      "consistency_model": "string"
    }
  ],
  "problem_solutions": {
    "cache_penetration": {"solution": "string", "implementation": "string"},
    "cache_breakdown": {"solution": "string", "implementation": "string"},
    "cache_avalanche": {"solution": "string", "implementation": "string"},
    "hot_key": {"solution": "string", "implementation": "string"}
  },
  "consistency_guarantee": {
    "strategy": "string — 一致性策略",
    "delayed_double_delete": "boolean — 是否使用延迟双删",
    "message_queue_invalidation": "boolean — 是否使用MQ异步失效",
    "version_vector": "boolean — 是否使用版本向量"
  },
  "monitoring": {
    "key_metrics": ["string — 需要监控的关键指标"],
    "alert_rules": [
      {"metric": "string", "threshold": "string", "action": "string"}
    ]
  },
  "code_templates": {
    "cache_aside_pattern": "string — Cache-Aside伪代码",
    "bloom_filter_setup": "string — 布隆过滤器配置"
  }
}
```

## 📋 执行步骤

### 阶段一：需求分析与缓存适用性评估

1. **性能瓶颈识别** — 分析当前系统的性能瓶颈是否真的是IO/数据库
2. **数据访问模式分析** — 识别热点数据、读写比、数据更新频率
3. **缓存适用性判断** — 不是所有数据都适合缓存：
   - ✅ 适合：读多写少、可容忍短暂不一致、数据访问有热点
   - ❌ 不适合：写多读少、强一致性要求、数据无热点
4. **确定缓存目标** — 命中率目标（>95%）、延迟目标（<5ms）、一致性目标

### 阶段二：多级缓存架构设计

5. **L1本地缓存设计**:
   - 技术选型：Caffeine(Guava) / Ehcache
   - 适用场景：极高频读取、数据量小、可容忍短暂不一致
   - 配置要点：容量上限、过期策略、刷新机制
6. **L2分布式缓存设计**:
   - 技术选型：Redis Cluster / Redis Sentinel
   - 数据结构选择：String/Hash/List/Set/ZSet按场景选择
   - 内存优化：压缩、序列化方式、大Key拆分
7. **L3数据库层设计**:
   - 查询优化：索引优化、读写分离
   - 作为缓存的兜底层
8. **数据流向设计** — 定义读写请求在各层之间的流转路径

### 阶段三：缓存模式与策略选择

9. **Cache-Aside (旁路缓存)**:
   - 读：先查缓存 → 命中返回 → 未命中查DB → 写入缓存
   - 写：先更新DB → 再删除缓存（而非更新缓存）
10. **Read-Through / Write-Through**:
    - 缓存层封装DB操作，应用只与缓存交互
    - 适合：缓存数据结构与DB一致
11. **Write-Behind (异步写回)**:
    - 写操作先写缓存，异步批量写入DB
    - 适合：写入量大、可容忍少量数据丢失
12. **选择依据** — 根据数据类型和一致性需求选择不同模式

### 阶段四：经典问题解决方案

13. **缓存穿透** — 查询不存在的数据导致请求直达DB：
    - 方案：布隆过滤器 + 空值缓存（TTL 2-5分钟）
14. **缓存击穿** — 热点Key过期瞬间大量请求穿透：
    - 方案：互斥锁重建 + 逻辑过期（不设物理TTL）
15. **缓存雪崩** — 大量Key同时过期：
    - 方案：TTL加随机偏移 + 多级缓存 + 限流降级
16. **热Key问题** — 单个Key访问量过大：
    - 方案：本地缓存 + Redis Key分片（key_1, key_2...）

### 阶段五：一致性保证与监控

17. **延迟双删** — 更新DB后删缓存，延迟N毫秒再删一次
18. **消息队列异步失效** — DB变更发送消息，消费端异步删除缓存
19. **版本号机制** — 携带版本号，低版本的写入不覆盖高版本
20. **监控体系建设** — 命中率、延迟、内存使用、连接数、慢查询

## ✅ 检查清单

- [ ] 是否分析了数据访问模式并确认缓存适用性
- [ ] 缓存层级和每层职责是否清晰
- [ ] 每种数据类型的缓存策略是否已确定
- [ ] 缓存穿透/击穿/雪崩方案是否已准备
- [ ] 一致性策略是否满足业务需求
- [ ] 缓存Key命名规范是否已制定
- [ ] 监控告警是否已配置
- [ ] 缓存容量规划是否考虑了数据增长

## ⚠️ 常见陷阱

| 陷阱 | 说明 | 规避方法 |
|------|------|---------|
| 缓存所有数据 | 不加区分地缓存一切 | 只缓存热点数据，写多读少的数据不缓存 |
| 更新缓存而非删除 | 写DB同时更新缓存，并发下数据不一致 | 写操作只删除缓存，让读操作重建 |
| TTL设置不合理 | 太短导致命中率低，太长导致数据过期 | 根据数据更新频率设定差异化T

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
