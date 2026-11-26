---
name: uskill-architecture-cycle-engineering-schema
description: "循环工程-统一 Schema 接口化"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-architecture-cycle-engineering-schema.md"
  original_id: ""
  version: ""
  trust: untrusted
---

# 循环工程-统一 Schema 接口化

# 循环工程-统一 Schema 接口化

> **D-A2-02 交付物** | v6.0-Graph P2 织网阶段
> **定位：** 将 7 套专项循环的执行入口参数化为统一 Schema 接口
> **验收标准：** 7 循环 Schema 均通过 JSON Schema 校验；接口兼容性 ≥ 95%
> **OVP：** Schema 覆盖率 7/7；接口兼容性测试通过

---

## 一、统一接口架构

### 1.1 接口总览

```
┌─────────────────────────────────────────────────┐
│              LoopController (调度层)              │
│                                                   │
│  输入: LoopRequest  →  路由  →  输出: LoopResponse│
└──────────┬──────────────────────────┬────────────┘
           │                          │
    ┌──────┴──────┐           ┌──────┴──────┐
    │ Loop 0-6    │           │ Loop 0-6    │
    │ Input Schema│           │Output Schema│
    └─────────────┘           └─────────────┘
```

### 1.2 统一 LoopRequest 结构

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["loop_id", "trigger_type", "timestamp"],
  "properties": {
    "loop_id": {
      "type": "integer",
      "enum": [0, 1, 2, 3, 4, 5, 6],
      "description": "循环编号"
    },
    "trigger_type": {
      "type": "string",
      "enum": ["cron", "manual", "event", "barrier", "recovery"],
      "description": "触发类型"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "params": {
      "type": "object",
      "description": "循环特定参数（见各循环定义）"
    },
    "context": {
      "type": "object",
      "description": "上下文注入（来自上游循环）"
    },
    "constraints": {
      "type": "object",
      "properties": {
        "timeout_seconds": { "type": "integer", "default": 900 },
        "max_retries": { "type": "integer", "default": 3 },
        "retry_interval_seconds": { "type": "integer", "default": 300 }
      }
    }
  }
}
```

### 1.3 统一 LoopResponse 结构

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["loop_id", "status", "timestamp", "output"],
  "properties": {
    "loop_id": {
      "type": "integer",
      "enum": [0, 1, 2, 3, 4, 5, 6]
    },
    "status": {
      "type": "string",
      "enum": ["completed", "partial", "failed", "skipped", "timeout"]
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "output": {
      "type": "object",
      "description": "循环输出（见各循环定义）"
    },
    "artifacts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "path": { "type": "string" },
          "type": { "type": "string", "enum": ["file", "json", "event"] },
          "schema": { "type": "string" }
        }
      },
      "description": "产出物列表"
    },
    "metrics": {
      "type": "object",
      "properties": {
        "duration_ms": { "type": "integer" },
        "tokens_used": { "type": "integer" },
        "nodes_executed": { "type": "integer" },
        "nodes_failed": { "type": "integer" }
      }
    },
    "errors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": { "type": "string" },
          "message": { "type": "string" },
          "recoverable": { "type": "boolean" }
        }
      }
    }
  }
}
```

---

## 二、7 循环接口定义

### Loop 0: Daily Loop（每日领域共生）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 8,12,18,20 * * *` / manual |
| **频率** | 每日 |
| **模式** | Advisor（Sonnet 5 主循环 + Fable 5 纠偏） |
| **超时** | 900s (15min) |

**Input Params:**
```json
{
  "time_slot": { "enum": ["morning", "midday", "system3", "evening"] },
  "identity_override": { "type": "array", "items": { "enum": ["architect", "investor", "scholar", "artist", "creator", "runner"] } }
}
```

**Input Context:**
```json
{
  "audit_snapshot": { "$ref": "#/definitions/AuditSnapshot" },
  "hrv": { "type": "number" },
  "pending_tasks": { "type": "array", "items": { "type": "string" } },
  "twin_injection": { "$ref": "#/definitions/TwinInjection" },
  "treasury_injection": { "$ref": "#/definitions/TreasuryInjection" },
  "bioloop_injection": { "$ref": "#/definitions/BioloopInjection" }
}
```

**Output:**
```

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
