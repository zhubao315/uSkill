---
name: uskill-ai-agent-architecture
description: "让Agent架构设计变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-agent-architecture.md"
  original_id: "SKL-6868"
  version: "3.0.0"
  trust: untrusted
---

# Agent架构设计

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
1. **不得**在无人类监督下执行高风险操作（发邮件、删除数

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
