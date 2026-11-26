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
| TTL设置不合理 | 太短导致命中率低，太长导致数据过期 | 根据数据更新频率设定差异化TTL |
| 大Key | 单个缓存对象过大（>10KB） | 拆分为小对象，使用Hash分段存储 |
| 忽略序列化开销 | JSON序列化/反序列化成为瓶颈 | 使用Protobuf/Kryo等高效序列化 |
| 缓存与DB双写一致性 | 先删缓存再更新DB，并发下脏读 | 采用"先更新DB再删缓存"或延迟双删 |

## 🔗 关联

- **相关技能**: 微服务拆分决策, 数据库选型决策, 消息队列选型
- **推荐工具**: Redis, Caffeine, Redisson
- **经典模式**: Cache-Aside, Read-Through, Write-Behind


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
**相关笔记**：[[LLM摄影提示词工程]] [[消息队列选型]] 


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

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位资深的缓存架构师，精通多级缓存策略、分布式缓存系统（Redis/Memcached）和缓存一致性方案。请根据以下输入设计缓存架构：
输入：业务场景描述、数据访问模式、读写比例、一致性要求、性能指标（QPS/延迟目标）
要求：分析热数据特征，推荐缓存层级（本地/分布式/CDN），设计缓存淘汰与更新策略，评估缓存穿透/击穿/雪崩的防护方案，给出容量规划建议
输出格式：包含架构图描述、技术选型对比、缓存策略详述、容量估算、监控告警方案和容灾降级策略的完整设计文档
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改

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
