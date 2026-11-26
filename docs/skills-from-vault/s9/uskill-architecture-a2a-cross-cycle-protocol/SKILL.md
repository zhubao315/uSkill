---
name: uskill-architecture-a2a-cross-cycle-protocol
description: "A2A 跨循环通信协议 v1"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-architecture-a2a-cross-cycle-protocol.md"
  original_id: ""
  version: ""
  trust: untrusted
---

# A2A 跨循环通信协议 v1

# A2A 跨循环通信协议 v1

> **D-A2-01 交付物** | v6.0-Graph P2 织网阶段
> **定位：** 定义 7 个子图之间的数据交换契约（Event Log 格式 / State Schema / 调用时序）
> **验收标准：** 覆盖 7 子图两两通信场景；至少 3 个子图互联验证；Schema 冲突检测生效
> **OVP：** 协议文档通过 Operator 评审

---

## 一、协议总览

### 1.1 设计原则

| 原则 | 说明 |
|------|------|
| **文件即消息** | 当前架构为文件 I/O，协议将文件格式标准化为消息契约 |
| **追加即发布** | 写入 `.runtime-context/` 的文件即为"发布"，下游读取即为"订阅" |
| **Schema 强校验** | 每个跨循环消息必须符合预定义 JSON Schema |
| **向后兼容** | 新增字段可用 `x-optional` 标记，不破坏已有消费者 |
| **幂等消费** | 消费者重复读取同一消息不产生副作用 |

### 1.2 架构映射

```
Loop 0 (Daily)  ←→  Loop 1 (Treasury)  ←→  Loop 5 (Twin)
      ↕                    ↕                      ↕
Loop 3 (Bio)    ←→  Loop 4 (Social)   ←→  Loop 6 (Audit)
      ↕                    ↕                      ↕
             Loop 2 (Skill Audit) ←→ 所有循环
```

---

## 二、通用 Event 格式

### 2.1 Event Schema（跨循环消息统一格式）

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["event_id", "event_type", "source_loop", "timestamp", "payload"],
  "properties": {
    "event_id": {
      "type": "string",
      "format": "uuid",
      "description": "全局唯一事件标识"
    },
    "event_type": {
      "type": "string",
      "enum": [
        "data_published",
        "data_consumed",
        "alert_triggered",
        "status_updated",
        "command_issued",
        "command_acknowledged"
      ],
      "description": "事件类型"
    },
    "source_loop": {
      "type": "integer",
      "enum": [0, 1, 2, 3, 4, 5, 6],
      "description": "来源循环编号"
    },
    "target_loops": {
      "type": "array",
      "items": { "type": "integer", "enum": [0, 1, 2, 3, 4, 5, 6] },
      "description": "目标循环编号（空数组=广播）"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 事件时间"
    },
    "payload": {
      "type": "object",
      "description": "事件负载（由 event_type 决定 schema）"
    },
    "schema_version": {
      "type": "string",
      "default": "1.0",
      "description": "Schema 版本号"
    },
    "priority": {
      "type": "string",
      "enum": ["P0", "P1", "P2"],
      "default": "P2",
      "description": "事件优先级"
    },
    "ttl_seconds": {
      "type": "integer",
      "default": 3600,
      "description": "消息存活时间（秒）"
    }
  }
}
```

### 2.2 Event Type 定义

| event_type | 含义 | payload 结构 | 典型场景 |
|-----------|------|-------------|---------|
| `data_published` | 生产者发布数据 | `{data_key, data_schema, data_content}` | Twin 发布蒸馏结果 |
| `data_consumed` | 消费者确认读取 | `{event_ref, consumer_loop}` | Daily Loop 读取 injection 文件 |
| `alert_triggered` | 告警触发 | `{alert_type, severity, context}` | Bio-Loop HRV 跌破阈值 |
| `status_updated` | 状态更新 | `{status_key, old_value, new_value}` | Treasury 风险等级变更 |
| `command_issued` | 发出指令 | `{command, params, deadline}` | Scheduler 冻结投资决策 |
| `command_acknowledged` | 指令确认 | `{command_ref, ack_status}` | Treasury 确认冻结 |

---

## 三、7 循环通信接口表

### 3.1 循环角色定义

| Loop | 名称 | 角色 | 生产数据 | 消费数据 |
|:----:|------|------|---------|---------|
| 0 | Daily Loop | 编排+执行 | 晨间计划/午间简报/晚间复盘 | Audit/Twin/Treasury/Bio injection |
| 1 | Treasury | 投资风控 | P0 队列/风险状态/持仓 | Twin 投资洞察/Audit 健康度 |
| 2 | Skill Audit | 技能治理 | 孤岛清单/复用率 | Audit trend.json |
| 3 | Bio-Loop | 身心健康 | HRV/训练/恢复 | Twin 恢复建议/Audit 快照 |
| 4 | Social | 关系网络 | 衰减预警/LQS | Twin 关系提醒 |
| 5 | Knowledge Twin | 知识蒸馏 | 经验晶体/洞察 | Daily Note/Raw 输入 |
| 6 | Global Audit | 审计验证 | trend.json/审计报告 | 所有循环状态 |

### 3.2 循环间通信接口矩阵

| 源 → 目标 | 消息类型 | 数据格式 | 频率 | 超时 |
|-----------|---------|---------|:----:|:----:|
| **5→0** Twin→Daily | `data_published` | `twin-injection-{date}.md` | 每日 | — |
| **1→0** Treasury→Daily | `data_published` | `treasury-injection-{date}.md` | 每日 | — |
| **3→0** Bio→Daily | `data_published` | `bioloop-injection-{date}.md` | 每日 | — |
| **1→0** Treasury→Daily | `alert_triggered` | `treasury-p0-queue.json` | 实时 | <10min |
| **5→1** Twin→Twin→Treasury | `data_published` | `twin_insight_cache.json` | 每日 | — |
| **5→3** Twin→Bio | `data_published` | `twin_recovery_suggestions.md` 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
