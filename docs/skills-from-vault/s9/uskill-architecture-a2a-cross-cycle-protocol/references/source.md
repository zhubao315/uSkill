
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
| **5→3** Twin→Bio | `data_published` | `twin_recovery_suggestions.md` | 每日 | — |
| **5→4** Twin→Social | `data_published` | `twin_relationship_alerts.json` | 每周 | — |
| **6→0** Audit→Daily | `data_published` | `trend.json` | 每日 | — |
| **6→2** Audit→SkillAudit | `data_published` | `trend.json` (L2 部分) | 每周 | — |
| **3→0** Bio→Daily | `alert_triggered` | HRV 跌破基线 | 实时 | <5min |
| **1→0** Treasury→Scheduler | `command_issued` | 冻结投资决策 | 实时 | <10min |
| **6→0** Audit→Daily | `alert_triggered` | 关键问题 P0 | 每日 | <1h |

### 3.3 各循环输入/输出 Schema

#### Loop 0: Daily Loop

```json
{
  "input": {
    "audit_snapshot": { "$ref": "#/definitions/AuditSnapshot" },
    "hrv": { "type": "number", "description": "3日HRV均值" },
    "pending": { "type": "array", "items": { "type": "string" } },
    "twin_injection": { "$ref": "#/definitions/TwinInjection" },
    "treasury_injection": { "$ref": "#/definitions/TreasuryInjection" },
    "bioloop_injection": { "$ref": "#/definitions/BioloopInjection" }
  },
  "output": {
    "morning_plan": { "$ref": "#/definitions/MorningPlan" },
    "invest_brief": { "$ref": "#/definitions/InvestBrief" },
    "fitness_brief": { "$ref": "#/definitions/FitnessBrief" },
    "read_brief": { "$ref": "#/definitions/ReadBrief" },
    "evening_review": { "$ref": "#/definitions/EveningReview" }
  }
}
```

#### Loop 1: Treasury

```json
{
  "input": {
    "twin_insights": { "$ref": "#/definitions/TwinInsightCache" },
    "audit_health": { "$ref": "#/definitions/AuditSnapshot" },
    "market_data": { "type": "object", "description": "外部市场数据" }
  },
  "output": {
    "p0_queue": { "$ref": "#/definitions/P0Queue" },
    "risk_status": { "$ref": "#/definitions/RiskStatus" },
    "treasury_injection": { "$ref": "#/definitions/TreasuryInjection" }
  }
}
```

#### Loop 3: Bio-Loop

```json
{
  "input": {
    "coros_data": { "$ref": "#/definitions/CorosData" },
    "hrv_baseline": { "type": "number", "default": 75 },
    "twin_recovery": { "$ref": "#/definitions/TwinRecoverySuggestions" }
  },
  "output": {
    "bioloop_injection": { "$ref": "#/definitions/BioloopInjection" },
    "recovery_alert": { "$ref": "#/definitions/RecoveryAlert" },
    "safety_claw_trigger": { "type": "boolean" }
  }
}
```

#### Loop 5: Knowledge Twin

```json
{
  "input": {
    "daily_raw": { "type": "string", "description": "Daily Note 原文" },
    "twin_graph": { "type": "object", "description": "现有词条图谱" }
  },
  "output": {
    "twin_injection": { "$ref": "#/definitions/TwinInjection" },
    "twin_insight_cache": { "$ref": "#/definitions/TwinInsightCache" },
    "twin_recovery_suggestions": { "$ref": "#/definitions/TwinRecoverySuggestions" },
    "twin_relationship_alerts": { "$ref": "#/definitions/TwinRelationshipAlerts" }
  }
}
```

---

## 四、关键数据结构定义

### 4.1 TwinInjection（Twin→Daily Loop）

```json
{
  "date": "2026-07-23",
  "experience_crystals": [
    {
      "title": "反确认偏差",
      "preview": "在投资决策中主动寻找反面证据...",
      "fidelity_score": 85,
      "dimension": "投资",
      "related_notes": ["[[确认偏差]]", "[[投资心理]]"]
    }
  ],
  "dimension_distribution": {
    "投资": 2, "认知": 1, "健康": 1
  }
}
```

### 4.2 TreasuryInjection（Treasury→Daily Loop）

```json
{
  "date": "2026-07-23",
  "risk_overall": "yellow",
  "hard_triggers": 0,
  "soft_warnings": 2,
  "total_value": 2813600,
  "cash_ratio": 0.10,
  "tech_concentration": 0.659,
  "twin_investment_insights": [
    {
      "title": "半导体估值逻辑",
      "preview": "PE > 80 时需谨慎...",
      "source": "twin_insight_cache.json"
    }
  ]
}
```

### 4.3 BioloopInjection（Bio→Daily Loop）

```json
{
  "date": "2026-07-23",
  "today_running": "15.15km, 配速05'40\"",
  "hrv_3d_avg": 74.1,
  "hrv_baseline": 75,
  "hrv_status": "normal",
  "monthly_mileage": 169.2,
  "monthly_target": 200,
  "recovery_advice": "保持当前训练强度，注意睡眠"
}
```

### 4.4 AuditSnapshot（Audit→所有循环）

```json
{
  "date": "2026-07-23",
  "health_score": { "L1": 97, "L2": 85, "L3": 80, "composite": 97, "grade": "A++" },
  "broken_link_rate": 0.19,
  "orphan_rate": 0.6,
  "tag_compliance": 100,
  "fm_complete_rate": 99.8,
  "critical_issues": [],
  "action_queue": { "P0": [], "P1": [], "P2": [] }
}
```

### 4.5 P0Queue（Treasury→Scheduler）

```json
{
  "date": "2026-07-23",
  "items": [
    {
      "id": "P0-001",
      "rule_id": "R-CONCENTRATION",
      "name": "行业集中度超限",
      "current_value": 0.659,
      "threshold": 0.30,
      "priority": "P0"
    }
  ]
}
```

---

## 五、Schema 冲突检测

### 5.1 冲突类型

| 冲突类型 | 说明 | 检测方法 | 严重度 |
|---------|------|---------|:------:|
| **字段缺失** | 消费者期望的字段在消息中不存在 | JSON Schema 校验 | 🔴 P0 |
| **类型不匹配** | 字段类型与 Schema 定义不一致 | JSON Schema 校验 | 🔴 P0 |
| **新增字段（破坏性）** | 生产者新增了消费者未处理的 required 字段 | Schema diff | 🟡 P1 |
| **新增字段（非破坏性）** | 生产者新增了 optional 字段 | Schema diff | 🟢 P2 |
| **语义变更** | 字段含义变化但 Schema 不变 | 人工审查 | 🔴 P0 |

### 5.2 冲突检测脚本

```bash
# 位置：09-REFERENCE/93-脚本/a2a_schema_check.py
# 用法：
python3 a2a_schema_check.py --validate  # 校验所有已发布消息
python3 a2a_schema_check.py --diff     # 对比 Schema 版本差异
python3 a2a_schema_check.py --check-consumers  # 检查消费者兼容性
```

### 5.3 兼容性规则

| 变更类型 | 消费者影响 | 是否兼容 | 处理 |
|---------|-----------|:-------:|------|
| 新增 optional 字段 | 无 | ✅ | 无需处理 |
| 新增 required 字段 | 消费者可能缺失 | ❌ | 消费者必须更新 |
| 删除 optional 字段 | 消费者可能依赖 | ❌ | 需通知消费者 |
| 删除 required 字段 | 无 | ✅ | 消费者可忽略 |
| 修改字段类型 | 消费者解析失败 | ❌ | 需要版本升级 |

---

## 六、示例 Trace：完整跨循环通信

### 6.1 场景：Bio-Loop HRV 跌破阈值 → Daily Loop 认知降载

```
时间线：

T+0min  [Loop 3 Bio-Loop] Coros API 数据同步
        → 读取 HRV: 3日均值 = 67.5 (基线 75, 跌破 10%)
        → 触发 Safety Claw: HRV < baseline * 0.90
        → 生成 Event:
          {
            "event_type": "alert_triggered",
            "source_loop": 3,
            "target_loops": [0],
            "payload": {
              "alert_type": "hrv_damping",
              "severity": "P0",
              "context": {"hrv_3d_avg": 67.5, "baseline": 75, "drop_pct": 0.10}
            }
          }

T+1min  [Loop 3 Bio-Loop] 写入 bioloop-injection-20260723.md
        → 包含 recovery_advice: "强制切换恢复周"

T+2min  [Loop 0 Daily Loop] 读取 bioloop-injection 文件
        → 生成 Event:
          {
            "event_type": "data_consumed",
            "source_loop": 0,
            "payload": {
              "event_ref": "<上一个 event_id>",
              "consumer_loop": 0
            }
          }

T+3min  [Loop 0 Daily Loop] 触发认知降载
        → 晨间计划任务量从 5 个降至 3 个
        → 架构师身份任务暂停（高计算负载）
        → 输出: cognitive_damping_active = true

T+5min  [Loop 6 Audit] 记录异常
        → 写入 trend.json: bioloop_hrv_status = "warning"
```

### 6.2 场景：Twin 蒸馏产出 → Treasury 投资助手 → Daily Loop

```
T+0min  [Loop 5 Twin] Daily Note 蒸馏完成
        → 产出经验晶体: "反确认偏差-投资决策"
        → dimension = "投资"
        → 写入 twin-injection-20260723.md (Daily Loop 消费)
        → 写入 twin_insight_cache.json (Treasury 消费)

T+5min  [Loop 1 Treasury] 读取 twin_insight_cache.json
        → 新增洞察: "PE > 80 时需谨慎"
        → 注入风险评估: tech_concentration = 65.9% → 🔴

T+10min [Loop 0 Daily Loop] 读取 twin-injection + treasury-injection
        → 晨间计划参考: "今日关注半导体估值风险"
        → 投资人身份任务: "审计持仓集中度"
```

---

## 七、超时与重试策略

| 消息类型 | 超时 | 重试次数 | 重试间隔 | 降级策略 |
|---------|:----:|:-------:|:-------:|---------|
| `data_published` | — | 0 | — | 跳过当日，等待下次 |
| `alert_triggered` (P0) | 10min | 3 | 1min | 升级至 Operator |
| `alert_triggered` (P1) | 1h | 2 | 5min | 记录日志，下次执行 |
| `command_issued` | 10min | 3 | 1min | 冻结自动执行 |
| `status_updated` | 5min | 1 | 1min | 使用旧状态 |

---

## 八、验证记录

### 8.1 三子图互联验证

| 子图对 | 验证场景 | 消息类型 | 结果 | 状态 |
|--------|---------|---------|------|:----:|
| **5→0** Twin→Daily | Twin 发布经验晶体 → Daily 读取 | data_published | injection 文件正确生成 + 读取 | ✅ |
| **1→0** Treasury→Daily | Treasury 发布风险状态 → Daily 晨间计划参考 | data_published | treasury-injection 正确生成 | ✅ |
| **3→0** Bio→Daily | HRV 跌破阈值 → Daily 认知降载 | alert_triggered | bioloop-injection 正确生成 | ✅ |
| **6→0** Audit→Daily | 审计快照 → Daily 晨间初始化 | data_published | trend.json 正确消费 | ✅ |
| **5→1** Twin→Treasury | Twin 投资洞察 → Treasury 风险评估 | data_published | twin_insight_cache 正确生成 | ✅ |
| **1→Scheduler** Treasury→调度 | P0 队列非空 → 冻结投资 | command_issued | treasury-p0-queue 正确触发 | ✅ |

**验证覆盖：** 6/6 核心跨循环场景全部通过 ✅

---

## 九、与现有架构兼容性

| 现有机制 | A2A 协议映射 | 兼容性 |
|---------|-------------|:------:|
| `.runtime-context/*.md` 文件 | `data_published` 事件的 payload 文件 | ✅ 100% |
| `twin_bridge.py` | 5→0/5→1/5→3/5→4 的 bridge 脚本 | ✅ 无需修改 |
| `treasury_loop.py` | 1→0/1→Scheduler 的 bridge 脚本 | ✅ 无需修改 |
| `bioloop_loop.py` | 3→0 的 bridge 脚本 | ✅ 无需修改 |
| `trend.json` | 6→所有的审计数据交换 | ✅ 无需修改 |
| Scheduler 路由规则 | `command_issued` + `alert_triggered` 事件 | ✅ 映射完成 |

---

## 十、关联文档

| 文档 | 关系 |
|------|------|
| [[uSkill-agent-循环工程统一调度入口]] | 7 循环中央调度 |
| [[uSkill-agent-每日领域共生循环系统]] §9 | Daily Loop DAG + Event Log |
| [[图工程（Graph Engineering）]] | Send API + 边类型定义 |
| [[2026年度目标 AI Co-Evolution-自主进化的人生操作系统]] §9.7 | 数据契约层 |
| [[L2-循环工程]] | 7 循环配置映射 |

---

*关联项目：[[uLife]] · [[uSkill]] · [[图工程]] | D-A2-01 交付物 | v6.0-Graph P2*
*版本：v1.0.0 | 更新：2026-07-23 | 变更：A2A 跨循环通信协议首版*
