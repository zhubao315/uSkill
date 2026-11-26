
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
```json
{
  "morning_plan": { "tasks": [{ "id": "string", "dimension": "string", "action": "string", "steps": ["string"], "deliverable": "string" }] },
  "daily_inspirations": { "inspirations": [{ "source": "string", "insight": "string", "action": "string" }] },
  "invest_brief": { "market": "string", "action": "string", "risk": "enum(low|medium|high)" },
  "fitness_brief": { "training": "string", "recovery": "enum(normal|caution|rest)", "adjust": "string" },
  "read_brief": { "article": "string", "insight": "string", "action": "string" },
  "evening_review": { "completed": "integer", "insights": ["string"], "tomorrow_focus": "string" }
}
```

---

### Loop 1: Treasury（财务红队对抗）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 10 * * 1` (每周一) / event(P0 queue) |
| **频率** | 每周 |
| **模式** | Orchestrator（Fable 5 规划 + Sonnet 5 并行研究） |
| **超时** | 1800s (30min) |

**Input Params:**
```json
{
  "mode": { "enum": ["full_analysis", "quick_check", "emergency_scan"] },
  "focus_areas": { "type": "array", "items": { "enum": ["positions", "risk", "backtest", "rebalance"] } }
}
```

**Input Context:**
```json
{
  "twin_insights": { "$ref": "#/definitions/TwinInsightCache" },
  "audit_health": { "$ref": "#/definitions/AuditSnapshot" },
  "market_data": { "type": "object" }
}
```

**Output:**
```json
{
  "p0_queue": { "$ref": "#/definitions/P0Queue" },
  "risk_status": { "overall": "enum(green|yellow|red)", "hard_triggers": "integer", "soft_warnings": "integer" },
  "treasury_injection": { "$ref": "#/definitions/TreasuryInjection" },
  "backtest_result": { "win_rate": "number", "sharpe": "number", "max_drawdown": "number" }
}
```

---

### Loop 2: Skill Audit（技能推理器孤岛审计）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 2 1 * *` (每月1日) / manual |
| **频率** | 每月 |
| **模式** | Orchestrator（Fable 5 审计标准 + Sonnet 5 批量扫描） |
| **超时** | 3600s (60min) |

**Input Params:**
```json
{
  "scope": { "enum": ["full", "incremental", "targeted"], "default": "incremental" },
  "target_domains": { "type": "array", "items": { "integer": "enum(1-9)" } }
}
```

**Input Context:**
```json
{
  "audit_trend": { "$ref": "#/definitions/TrendJson" },
  "skill_graph": { "type": "object", "description": "当前 Skill 图谱数据" }
}
```

**Output:**
```json
{
  "isolated_skills": [{ "id": "string", "name": "string", "reason": "string", "days_inactive": "integer" }],
  "reuse_rate": { "overall": "number", "per_domain": { "type": "object" } },
  "recommendations": [{ "action": "enum(integrate|deprecate|merge)", "skill_id": "string", "reason": "string" }]
}
```

---

### Loop 3: Bio-Loop（身心循环智能体自适应负荷重排）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 7 * * *` (每日) / event(HRV alert) |
| **频率** | 每日 |
| **模式** | Advisor（Sonnet 5 趋势监控 + Fable 5 熔断决策） |
| **超时** | 300s (5min) |

**Input Params:**
```json
{
  "sync_only": { "type": "boolean", "default": false },
  "force_recovery": { "type": "boolean", "default": false }
}
```

**Input Context:**
```json
{
  "coros_data": { "hrv_3d_avg": "number", "today_km": "number", "resting_hr": "integer" },
  "hrv_baseline": { "type": "number", "default": 75 },
  "twin_recovery": { "$ref": "#/definitions/TwinRecoverySuggestions" }
}
```

**Output:**
```json
{
  "bioloop_injection": { "$ref": "#/definitions/BioloopInjection" },
  "safety_claw_trigger": { "type": "boolean" },
  "recovery_alert": { "triggered": "boolean", "reason": "string", "action": "string" },
  "training_adjustment": { "volume_change_pct": "number", "intensity_change": "enum(up|down|maintain)" }
}
```

---

### Loop 4: Social（关系网络连接器衰减预警）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 9 * * 1` (每周一) / manual |
| **频率** | 每周 |
| **模式** | Advisor（Sonnet 5 NLP 分析 + Fable 5 阈值判定） |
| **超时** | 600s (10min) |

**Input Params:**
```json
{
  "scan_depth": { "enum": ["core_only", "extended"], "default": "core_only" },
  "decay_threshold_days": { "type": "integer", "default": 90 }
}
```

**Input Context:**
```json
{
  "core_circle": { "type": "array", "items": { "name": "string", "last_interaction": "date", "lqs_baseline": "number" } },
  "interaction_logs": { "type": "array", "description": "近90天通讯日志" }
}
```

**Output:**
```json
{
  "decay_alerts": [{ "name": "string", "days_no_contact": "integer", "lqs_current": "number", "severity": "enum(low|medium|high)" }],
  "preservation_actions": [{ "name": "string", "action": "string", "deadline": "date" }],
  "twin_relationship_alerts": { "$ref": "#/definitions/TwinRelationshipAlerts" }
}
```

---

### Loop 5: Knowledge Twin（知识孪生体深度蒸馏）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 22 * * *` (每日) / event(new daily note) |
| **频率** | 每日 |
| **模式** | Orchestrator（Fable 5 优先级排程 + Sonnet 5 批量 CoT 提取） |
| **超时** | 600s (10min) |

**Input Params:**
```json
{
  "target_date": { "type": "string", "format": "date", "description": "蒸馏目标日期" },
  "quality_mode": { "enum": ["standard", "deep", "quick"], "default": "standard" },
  "fidelity_threshold": { "type": "number", "default": 0.7 }
}
```

**Input Context:**
```json
{
  "daily_raw": { "type": "string", "description": "Daily Note 原文" },
  "twin_graph": { "type": "object", "description": "现有词条图谱" }
}
```

**Output:**
```json
{
  "evergreen_notes": [{ "id": "uuid", "title": "string", "fidelity_score": "number", "dual_links": ["string"] }],
  "twin_injection": { "$ref": "#/definitions/TwinInjection" },
  "twin_insight_cache": { "$ref": "#/definitions/TwinInsightCache" },
  "distill_metrics": { "entries_created": "integer", "avg_fidelity": "number", "dual_link_rate": "number" }
}
```

---

### Loop 6: Global Audit（全局审计专项循环）

| 字段 | 值 |
|------|-----|
| **触发** | cron `0 2 * * *` (每日) / cron `0 2 * * 0` (L2 每周日) / cron `0 2 1 * *` (L3 每月) |
| **频率** | L1 每日 / L2 每周 / L3 每月 |
| **模式** | Orchestrator（Fable 5 异常判定 + Sonnet 5 逐层扫描） |
| **超时** | L1: 900s / L2: 1800s / L3: 3600s |

**Input Params:**
```json
{
  "layer": { "enum": ["L1", "L2", "L3"], "default": "L1" },
  "force_full": { "type": "boolean", "default": false }
}
```

**Input Context:**
```json
{
  "raw_markdown": { "type": "string", "description": "全库原始 Markdown" },
  "audit_exceptions": { "type": "object", "description": "豁免白名单" },
  "trend_previous": { "$ref": "#/definitions/TrendJson" },
  "concept_list": { "type": "array", "items": { "type": "string" } }
}
```

**Output:**
```json
{
  "health_score": { "L1": "integer", "L2": "integer", "L3": "integer", "composite": "integer", "grade": "string" },
  "critical_issues": [{ "severity": "enum(P0|P1|P2)", "description": "string", "affected_files": ["string"] }],
  "action_queue": { "P0": ["string"], "P1": ["string"], "P2": ["string"] },
  "trend_update": { "$ref": "#/definitions/TrendJson" }
}
```

---

## 三、可配置参数表

| Loop | 参数 | 默认值 | 范围 | 说明 |
|:----:|------|--------|------|------|
| 0 | `time_slot` | auto | morning/midday/system3/evening | 时段选择 |
| 0 | `task_count` | 5 | 3-7 | 每日任务数 |
| 0 | `identity_weights` | auto | 0.0-1.0 | 身份维度权重 |
| 1 | `mode` | full_analysis | full/quick/emergency | 分析深度 |
| 1 | `backtest_days` | 30 | 7-365 | 回测天数 |
| 1 | `risk_threshold` | 0.3 | 0.1-0.5 | 风险阈值 |
| 2 | `scope` | incremental | full/incremental/targeted | 审计范围 |
| 2 | `min_reuse_rate` | 0.3 | 0.1-0.5 | 最低复用率 |
| 3 | `hrv_baseline` | 75 | 50-100 | HRV 基线 |
| 3 | `recovery_drop_pct` | 0.10 | 0.05-0.20 | 恢复触发阈值 |
| 4 | `decay_threshold_days` | 90 | 30-180 | 衰减阈值天数 |
| 4 | `core_circle_size` | 10 | 5-15 | 核心圈人数 |
| 5 | `fidelity_threshold` | 0.7 | 0.5-0.9 | 保真度阈值 |
| 5 | `quality_mode` | standard | standard/deep/quick | 蒸馏质量 |
| 5 | `max_entries_per_day` | 3 | 1-10 | 每日最大词条 |
| 6 | `layer` | L1 | L1/L2/L3 | 审计层级 |
| 6 | `max_broken_link_rate` | 0.05 | 0.01-0.10 | 断链率阈值 |

---

## 四、触发条件矩阵

| Loop | cron 表达式 | event 触发 | 手动触发 | barrier 触发 |
|:----:|------------|-----------|---------|-------------|
| 0 | `0 8,12,18,20 * * *` | — | `/daily` | — |
| 1 | `0 10 * * 1` | P0 queue 非空 | `/treasury` | — |
| 2 | `0 2 1 * *` | — | `/skill-audit` | A2+B2 完成后 |
| 3 | `0 7 * * *` | HRV 跑破阈值 | `/bio` | — |
| 4 | `0 9 * * 1` | — | `/social` | — |
| 5 | `0 22 * * *` | 新 Daily Note 写入 | `/twin` | — |
| 6 | `0 2 * * *` | — | `/audit` | 所有循环完成后 |

---

## 五、重试策略

| Loop | L1 重试 | L2 修补 | L3 上报 | 写入冲突重试 |
|:----:|:------:|:------:|:------:|:----------:|
| 0 | 1次/5min | 换时段执行 | 人工补做 | 3次/1s |
| 1 | 1次/5min | 降级为 quick 模式 | 人工决策 | 3次/1s |
| 2 | 1次/10min | 降级为 incremental | 跳过本月 | 3次/1s |
| 3 | 1次/1min | 强制恢复周 | 人工干预 | 3次/1s |
| 4 | 1次/5min | 降级为 core_only | 人工决策 | 3次/1s |
| 5 | 1次/5min | 降级为 quick 模式 | 跳过当日 | 3次/1s |
| 6 | L1: 1次/5min | L2: 等下周 | L3: 用缓存 | 3次/1s |

---

## 六、兼容性测试矩阵

### 6.1 旧参数→新接口映射

| 旧参数格式 | 新接口字段 | 兼容方式 |
|-----------|-----------|---------|
| `input_data` (string) | `params` + `context` | 自动解析 |
| `context` (string) | `context` (object) | JSON.parse |
| 直接调用 SKILL.md | `loop_id` + `trigger_type=manual` | 路由映射 |

### 6.2 兼容性测试结果

| Loop | 旧格式 | 新接口 | 自动转换 | 状态 |
|:----:|-------|-------|:-------:|:----:|
| 0 | SKILL.md 直接调用 | LoopRequest(loop_id=0) | ✅ | ✅ |
| 1 | `input_data` string | LoopRequest(loop_id=1, params) | ✅ | ✅ |
| 2 | SKILL.md 直接调用 | LoopRequest(loop_id=2) | ✅ | ✅ |
| 3 | Coros API 直接调用 | LoopRequest(loop_id=3, context) | ✅ | ✅ |
| 4 | SKILL.md 直接调用 | LoopRequest(loop_id=4) | ✅ | ✅ |
| 5 | `daily_raw` string | LoopRequest(loop_id=5, context) | ✅ | ✅ |
| 6 | 三层管道直接调用 | LoopRequest(loop_id=6, params.layer) | ✅ | ✅ |

**接口兼容性：** 7/7 = **100%** ≥ 95% ✅

---

## 七、Schema 校验脚本

```bash
# 位置：09-REFERENCE/93-脚本/schema_validate.py
# 用法：
python3 schema_validate.py --loop 0 --validate input.json   # 校验 Loop 0 输入
python3 schema_validate.py --loop all --validate-all         # 全量校验
python3 schema_validate.py --diff v1 v2                      # Schema 版本对比
```

---

## 八、关联文档

| 文档 | 关系 |
|------|------|
| [[A2A跨循环通信协议-v1]] | D-A2-01，消息格式定义 |
| [[uSkill-agent-循环工程统一调度入口]] | 7 循环调度中枢 |
| [[L2-循环工程]] | 循环配置映射 |
| [[图工程（Graph Engineering）]] | Send API + 边类型 |

---

*关联项目：[[uLife]] · [[uSkill]] | D-A2-02 交付物 | v6.0-Graph P2*
*版本：v1.0.0 | 更新：2026-07-23 | 变更：7 循环统一 Schema 接口化首版*
