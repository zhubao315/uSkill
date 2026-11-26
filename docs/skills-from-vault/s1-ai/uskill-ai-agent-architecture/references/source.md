
description: |
  当用户需要设计 Agent 系统架构（规划、记忆、工具使用、多 Agent 协作）时使用此 Skill。
  触发词包括：'Agent架构'、'智能体设计'、'Agent系统'、'多Agent'、'Agent协作'、'规划模块'。
  当用户需要"构建 AI Agent"、"设计自主系统"、"多智能体协作"时，
  即使未直接说"Agent架构"，也应使用此 Skill。
  不适用于简单的 LLM API 调用。遇到复杂 Agent 系统设计时优先使用。

---

# uSkill-902: Agent架构设计

## 🎯 目标

> 设计可扩展、可靠的 Agent 系统架构，涵盖规划、记忆、工具使用和多 Agent 协作。

**核心价值**：从单次 LLM 调用到自主执行系统，让 AI 能处理复杂、多步骤任务。

**适用场景**：
- 自动化工作流 Agent
- 多步骤任务执行系统
- 人机协作系统
- 多 Agent 协作平台
- 自主决策系统

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `agent_type` | `enum` | ✅ | — | `single` / `multi` / `hierarchical` / `swarm` |
| `task_domain` | `string` | ✅ | — | Agent 要处理的任务领域 |
| `capabilities` | `array` | ✅ | — | 需要的能力列表 |
| `constraints` | `object` | ❌ | — | `{latency, cost, safety, scalability}` |
| `existing_system` | `object` | ❌ | — | 已有系统信息 |

**输入约束**：
- `capabilities` 必须明确列出工具和接口需求
- `constraints.safety` 必须定义权限边界
- `agent_type=multi` 时必须定义通信协议

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结架构方案",
  "agent_id": "AG-YYYY-MMDD-NNN",

  "architecture": {
    "topology": "string",
    "components": [
      {
        "name": "string",
        "type": "string",
        "responsibility": "string",
        "interfaces": ["string"]
      }
    ],
    "data_flow": "string",
    "communication_protocol": "string"
  },

  "planning": {
    "decomposition_strategy": "string",
    "plan_representation": "string",
    "replanning_trigger": "string",
    "failure_recovery": "string"
  },

  "memory": {
    "short_term": {
      "type": "string",
      "capacity": "string",
      "eviction_policy": "string"
    },
    "long_term": {
      "type": "string",
      "storage": "string",
      "retrieval": "string"
    },
    "shared_memory": "string"
  },

  "tool_use": {
    "registry": [
      {
        "name": "string",
        "purpose": "string",
        "input_schema": "object",
        "safety_level": "low|medium|high"
      }
    ],
    "execution_sandbox": "string",
    "error_handling": "string"
  },

  "multi_agent": {
    "coordination_pattern": "string",
    "conflict_resolution": "string",
    "load_balancing": "string",
    "deadlock_prevention": "string"
  },

  "safety": {
    "permission_model": "string",
    "audit_logging": "string",
    "human_in_the_loop": "string",
    "emergency_stop": "string"
  },

  "evaluation": {
    "metrics": ["string"],
    "benchmarks": ["string"],
    "monitoring": "string"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 需求分析与拓扑选型

- **输入**：`agent_type`, `task_domain`, `capabilities`
- **动作**：
  1. 分析任务复杂度和领域特征
  2. 评估单 Agent vs 多 Agent 的适用性
  3. 选择合适的系统拓扑
- **输出**：`architecture.topology`
- **分支条件**：
  - IF 任务可独立完成 → 单 Agent 架构
  - IF 任务需要分工协作 → 多 Agent 架构
  - IF 任务有层级关系 → 层级式架构
  - IF 需要高度并行 → 蜂群架构
  - ELSE → 从单 Agent 开始，按需扩展
- **检查点**：✅ 应验证拓扑选择与任务规模匹配

### Step 2: 核心模块设计

- **输入**：选定的拓扑
- **动作**：
  1. 设计规划模块（任务分解与执行）
  2. 设计记忆模块（短期/长期/共享）
  3. 设计工具使用模块
- **输出**：`planning`, `memory`, `tool_use`
- **分支条件**：
  - IF 任务步骤 > 5 → 增加中间验证点
  - IF 需要跨会话记忆 → 增加强持久化
  - IF 工具有副作用 → 增加沙箱和审批
  - IF 数据量大 → 增加流式处理
- **检查点**：✅ 应验证模块间接口清晰无歧义

### Step 3: 多 Agent 协作设计

- **输入**：`agent_type`, 核心模块设计
- **动作**：
  1. 定义 Agent 间通信协议
  2. 设计协调模式
  3. 实现冲突解决和死锁预防
- **输出**：`multi_agent`
- **分支条件**：
  - IF Agent 间有共享资源 → 增加锁机制
  - IF 任务有依赖关系 → 设计 DAG 调度
  - IF 需要动态扩缩容 → 增加负载均衡
  - IF 有竞争决策 → 设计投票或仲裁机制
- **检查点**：✅ 应验证无死锁风险且通信可靠

### Step 4: 安全与监控设计

- **输入**：所有前序设计
- **动作**：
  1. 设计权限模型
  2. 实现审计日志
  3. 设计人机协作点
  4. 实现紧急停止机制
- **输出**：`safety`, `evaluation`
- **分支条件**：
  - IF 涉及外部 API → 增加速率限制和重试
  - IF 处理敏感数据 → 增加脱敏和访问控制
  - IF 需要实时监控 → 增加 metrics 和告警
  - ELSE → 标准安全措施
- **检查点**：✅ 应验证安全措施覆盖所有高风险点

### Step 5: 评估与迭代规划

- **输入**：完整架构设计
- **动作**：
  1. 定义评估指标
  2. 设计基准测试
  3. 规划迭代路径
- **输出**：`evaluation`
- **检查点**：✅ 应验证评估指标可量化且可追踪

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在无人类监督下执行高风险操作（发邮件、删除数据、支付）
2. **不得**绕过工具沙箱直接执行系统命令
3. **必须**为每个 Agent 操作记录审计日志
4. **必须**实现紧急停止机制

### 软性约束（建议遵守）
1. 单个 Agent 的工具数 ≤ 20
2. Agent 间通信延迟 < 100ms
3. 记忆检索延迟 < 500ms
4. 定期进行架构健康度评估

### 人工兜底点
- 当 Agent 决策涉及法律、财务、人事时，**必须**等待人类确认
- 当系统出现未预期的行为时，**必须**暂停并人工审查
- 当 Agent 间出现无法解决的冲突时，**必须**升级到人类仲裁

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `AG_ERROR_PLANNING_FAILED` | 任务无法分解 | 回退到人工分解 | 🔴 |
| `AG_ERROR_TOOL_FAILURE` | 工具调用失败 | 重试或使用备选工具 | 🟡 |
| `AG_WARNING_MEMORY_FULL` | 短期记忆满 | 清理或转移至长期记忆 | 🟡 |
| `AG_ERROR_DEADLOCK` | Agent 间死锁 | 超时释放 + 重新调度 | 🔴 |
| `AG_WARNING_SAFETY_BREACH` | 安全边界触发 | 立即暂停 + 人类介入 | 🔴 |

### 降级策略
- 当多 Agent 协作失败时，回退到单 Agent 串行执行
- 当工具不可用时，输出手动操作指南
- 当规划失败时，提供简化版任务分解

---

## ✅ 校验验收规则

### 格式校验
- [ ] 架构图组件完整
- [ ] 接口定义明确
- [ ] 数据流无歧义

### 内容校验
- [ ] 规划模块可分解复杂任务
- [ ] 记忆模块支持长短期切换
- [ ] 工具使用有安全边界
- [ ] 多 Agent 无死锁风险

### 合规校验
- [ ] 安全措施已实现
- [ ] 审计日志已设计
- [ ] 人工兜底点已标注

### OVP 验证信号
- Agent 任务完成率 ≥ 85%
- 工具调用成功率 ≥ 95%
- 平均响应时间 ≤ 5s

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "单 Agent 工作流",
    "prompt": "设计一个自动处理客户邮件的 Agent",
    "context": "agent_type=single, capabilities=['邮件读取', '意图分类', '自动回复']",
    "assertions": [
      "architecture.components 包含规划、记忆、工具模块",
      "tool_use.registry 覆盖所有能力",
      "safety 包含人工兜底机制"
    ],
    "expected_behavior": "设计单 Agent 邮件处理系统",
    "critic_attack": "是否考虑了邮件的复杂性和边界情况？"
  },
  {
    "id": "test-002",
    "name": "多 Agent 协作",
    "prompt": "设计一个代码审查系统，包含作者、审查者、集成者三个角色",
    "context": "agent_type=multi, capabilities=['代码分析', '规范检查', '自动测试']",
    "assertions": [
      "multi_agent.coordination_pattern 明确",
      "conflict_resolution 有具体机制",
      "deadlock_prevention 已设计"
    ],
    "expected_behavior": "设计三角色代码审查 Agent 系统",
    "critic_attack": "角色分工是否清晰？是否存在职责重叠？"
  },
  {
    "id": "test-003",
    "name": "层级式架构",
    "prompt": "设计一个项目管理 Agent，管理层分配任务给执行层",
    "context": "agent_type=hierarchical, capabilities=['任务分解', '进度跟踪', '资源分配']",
    "assertions": [
      "architecture 包含管理层和执行层",
      "planning.decomposition_strategy 明确",
      "shared_memory 支持层级间信息共享"
    ],
    "expected_behavior": "设计层级式项目管理 Agent",
    "critic_attack": "层级间通信是否高效？是否存在信息丢失？"
  },
  {
    "id": "test-004",
    "name": "安全边界设计",
    "prompt": "Agent 需要调用外部 API，如何确保安全？",
    "context": "agent_type=single, constraints={safety: 'high'}",
    "assertions": [
      "tool_use.execution_sandbox 已设计",
      "safety.permission_model 包含 API 权限控制",
      "audit_logging 覆盖所有 API 调用"
    ],
    "expected_behavior": "设计安全的外部 API 调用方案",
    "critic_attack": "是否考虑了 API 密钥管理？是否限制了调用频率？"
  },
  {
    "id": "test-005",
    "name": "记忆系统设计",
    "prompt": "Agent 需要记住过去 30 天的用户交互",
    "context": "agent_type=single, capabilities=['用户交互', '偏好学习']",
    "assertions": [
      "memory.short_term 和 long_term 都有定义",
      "retrieval 策略支持 30 天范围",
      "eviction_policy 合理"
    ],
    "expected_behavior": "设计支持长期记忆的 Agent 系统",
    "critic_attack": "记忆容量是否足够？检索效率如何？"
  },
  {
    "id": "test-006",
    "name": "蜂群架构",
    "prompt": "需要 100 个 Agent 并行处理数据",
    "context": "agent_type=swarm, capabilities=['数据处理', '结果聚合']",
    "assertions": [
      "multi_agent.load_balancing 已设计",
      "通信协议支持高并发",
      "结果聚合机制明确"
    ],
    "expected_behavior": "设计高并发的蜂群 Agent 架构",
    "critic_attack": "是否考虑了资源限制？聚合结果是否一致？"
  },
  {
    "id": "test-007",
    "name": "人机协作设计",
    "prompt": "Agent 需要在关键决策点等待人类确认",
    "context": "agent_type=single, constraints={safety: 'high'}",
    "assertions": [
      "safety.human_in_the_loop 明确触发条件",
      "planning.replanning_trigger 包含人类反馈",
      "emergency_stop 可用"
    ],
    "expected_behavior": "设计人机协作的 Agent 系统",
    "critic_attack": "人类确认的延迟是否影响系统效率？"
  },
  {
    "id": "test-008",
    "name": "故障恢复设计",
    "prompt": "Agent 执行到一半失败了怎么办？",
    "context": "agent_type=single",
    "assertions": [
      "planning.failure_recovery 有具体策略",
      "memory 支持断点恢复",
      "有重试和回退机制"
    ],
    "expected_behavior": "设计健壮的故障恢复机制",
    "critic_attack": "恢复是否保证数据一致性？"
  },
  {
    "id": "test-009",
    "name": "性能优化",
    "prompt": "Agent 响应太慢，怎么优化？",
    "context": "agent_type=single, constraints={latency: 'low'}",
    "assertions": [
      "evaluation.metrics 包含延迟指标",
      "优化方案包含缓存和预计算",
      "有性能基准和监控"
    ],
    "expected_behavior": "设计性能优化方案",
    "critic_attack": "优化是否引入了新的瓶颈？"
  },
  {
    "id": "test-010",
    "name": "可观测性设计",
    "prompt": "怎么监控 Agent 的运行状态？",
    "context": "agent_type=multi",
    "assertions": [
      "evaluation.monitoring 包含 metrics 和 logs",
      "审计日志覆盖关键操作",
      "有告警和仪表盘方案"
    ],
    "expected_behavior": "设计完整的可观测性方案",
    "critic_attack": "监控是否覆盖了所有关键路径？"
  }
]
```

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🔗 关联文档

- [[人生操作系统进化-Schema-v2]] — 系统架构参考
- [[生态系统思维]] — 系统设计方法论
- [[Prompt工程进阶]] — Agent 中的 Prompt 设计
- [[RAG优化]] — Agent 记忆检索
- [[自动化工作流]] — Agent 应用场景

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：规划/记忆/工具/多Agent协作 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [任务类型] for [用户水平], with [约束条件], leaning toward [方法/工具]."

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
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


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
