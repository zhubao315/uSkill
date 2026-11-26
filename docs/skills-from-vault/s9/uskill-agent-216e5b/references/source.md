
# 循环工程-审计-调度数据契约

> **用途**：定义 `trend.json` (审计层) 与 `循环工程统一调度入口` (调度层) 之间的数据字段映射与 Schema 契约
> **数据源**：`00-META/审计/trend.json` (schema v1.9)
> **消费方**：`[[uSkill-agent-循环工程统一调度入口]]` · `[[uSkill-agent-每日领域共生循环系统]]` · Home 看板

---

## 数据流架构

```
00-META/审计/trend.json (schema v1.6)
    │
    ├──→ 调度入口模板变量 (00:15 审计完成 → 08:00 晨间初始化)
    │       {{audit_snapshot}} → Daily Loop 晨间计划
    │
    ├──→ Home 健康度看板 (异步刷新)
    │       综合健康度 | 断链率 | 深度率 | 领域均衡
    │
    └──→ 专项循环 (按需拉取)
            Layer 2 → 技能推理器
            Layer 3 → 知识孪生体
```

---

## 字段映射契约

### Layer 1：结构健康

| `trend.json` 字段 | 类型 | 调度入口变量 | Home 看板映射 | 说明 |
|---|---|---|---|---|
| `layer1.total_notes` | int | `{{total_notes}}` | 全库资产 | 去重后笔记总数 |
| `layer1.broken_links_total` | int | `{{broken_links_total}}` | 断链数 | 断链绝对数 |
| `layer1.broken_link_fix_rate` | float | — | — | 断链修复率 % |
| `layer1.orphan_count` | int | — | — | 孤岛绝对数 |
| `layer1.orphan_rate` | float | `{{orphan_rate}}` | 孤岛率 | 孤岛占比 % |
| `layer1.tag_compliance` | float | `{{tag_compliance}}` | 标签合规 | % |
| `layer1.fm_complete_rate` | float | `{{fm_completeness}}` | FM 完整率 | % |
| `layer1.fm_issue_count` | int | `{{fm_issues}}` | FM 缺陷数 | 含 YAML 错误/缺字段 |
| `layer1.moc_count` | int | — | — | MOC 总数 |
| `layer1.skill_reuse_rate` | float | `{{skill_reuse_rate}}` | uSkill 复用率 | % |
| `layer1.zero_byte_files` | int | — | — | 零字节文件数 |
| `layer1.sync_conflict_md` | int | `{{sync_conflict_md}}` | ⚠️ 冲突文件 | sync-conflict .md 文件数 |
| `layer1.sync_conflict_index` | int | `{{sync_conflict_index}}` | ⚠️ 冲突索引 | twin_index 等二进制冲突数 |
| `layer1.large_files_over_50k` | int | — | ⚠️ 关注 | 大文件数 |
| `layer1.short_files_500b` | int | `{{short_file_count}}` | 短文件数 | <500B 笔记数 |

### Layer 2：内容质量

| `trend.json` 字段 | 类型 | 调度入口变量 | Home 看板映射 | 说明 |
|---|---|---|---|---|
| `layer2.scanned_notes` | int | — | — | 抽样量 |
| `layer2.depth.D3_rate` | float | `{{deep_rate}}` | 深度率 D3 | % |
| `layer2.depth.D1_rate` | float | `{{shallow_rate}}` | 浅层率 D1 | % |
| `layer2.freshness.F1_rate` | float | `{{stale_rate}}` | 过时率 F1 | % |
| `layer2.actionability.A1_rate` | float | `{{actionable_rate}}` | 可操作率 A1 | % |
| `layer2.encoding.K3_rate` | float | `{{metacognition_rate}}` | 元认知率 K3 | % |
| `layer2.connectivity.I1_rate` | float | `{{well_connected_rate}}` | 高关联率 I1 | % |
| `layer2.connectivity.I3_isolated` | int | — | 孤立笔记数 | 引用为 0 |

### Layer 3：知识体系

| `trend.json` 字段 | 类型 | 调度入口变量 | Home 看板映射 | 说明 |
|---|---|---|---|---|
| `layer3.concept_coverage` | float | `{{concept_coverage}}` | 概念覆盖率 | % |
| `layer3.concept_total` | int | — | — | 核心概念总数 |
| `layer3.dominant_domain` | string | `{{dominant_domain}}` | 主导领域 | 如"维度/学习" |
| `layer3.dominant_domain_pct` | float | `{{dominant_domain_pct}}` | 主导领域占比 | % |
| `layer3.domain_balance` | string | — | 均衡状态 | healthy / near_threshold / critical |
| `layer3.knowledge_gaps` | int | — | 知识缺口数 | |
| `layer3.moc_coverage_avg` | float | `{{moc_coverage_avg}}` | MOC 覆盖率 | % |
| `layer3.moc_effective` | int | — | — | 有效核心 MOC 数 |

### 健康度

| `trend.json` 字段 | 类型 | 调度入口变量 | Home 看板映射 | 说明 |
|---|---|---|---|---|
| `health_score.L1` | int | — | 结构分 | 0-100 |
| `health_score.L2` | int | — | 内容分 | 0-100 |
| `health_score.L3` | int | — | 体系分 | 0-100 |
| `health_score.composite` | float | `{{health_score}}` | 综合健康度 | 0-100 |
| `health_score.grade` | string | `{{health_grade}}` | 等级 | A / B+ / B / C |

### 关键问题与行动队列（v1.1 新增）

| `trend.json` 字段 | 类型 | 调度入口变量 | 说明 |
|---|---|---|---|
| `critical_issues[]` | string[] | `{{critical_issues}}` | P0 级关键问题列表，非空时自动提升为调度任务 |
| `action_queue.P0[]` | string[] | `{{action_queue_p0}}` | 紧急行动项，必须当日处理 |
| `action_queue.P1[]` | string[] | `{{action_queue_p1}}` | 重要行动项，本周内处理 |
| `action_queue.P2[]` | string[] | `{{action_queue_p2}}` | 常规行动项，持续推进 |

### 跨周期趋势对比（v1.1 新增）

| `trend.json` 字段 | 类型 | 调度入口变量 | 说明 |
|---|---|---|---|
| `comparison_with_prev.total_notes_change` | string | `{{trend_notes_delta}}` | 笔记数变化（如 "+82"） |
| `comparison_with_prev.broken_links` | string | `{{trend_broken_delta}}` | 断链变化（如 "0→3(+3回升)"） |
| `comparison_with_prev.sync_conflict` | string | `{{trend_sync_delta}}` | 冲突变化（如 "0→18(+18爆发)"） |
| `comparison_with_prev.domain_learning_change` | string | `{{trend_learning_delta}}` | 学习域占比变化 |
| `comparison_with_prev.health_change` | string | `{{trend_health_delta}}` | 综合健康度变化 |

---

## 调度入口模板注入点

### 1. 全局总调度官提示词注入点

```markdown
# 动态输入状态锚点
* 全局共享状态快照:
  总笔记: {{total_notes}} | 健康度: {{health_score}} ({{health_grade}})
  uSkill 复用率: {{skill_reuse_rate}}% | MOC 覆盖率: {{moc_coverage_avg}}%
* 深夜审计最新指标:
  笔记总数: {{total_notes}} | 断链: {{broken_links_total}}条
  领域失衡度: {{dominant_domain}} 占比 {{dominant_domain_pct}}%
  sync-conflict: {{sync_conflict_md}}篇(.md) + {{sync_conflict_index}}个(索引)
  FM缺陷: {{fm_issues}}篇 | 短文件: {{short_file_count}}篇
* 跨周期趋势 (较上期):
  断链: {{trend_broken_delta}} | 冲突: {{trend_sync_delta}}
  健康度: {{trend_health_delta}} | 学习域: {{trend_learning_delta}}
* 端侧生物生理算力: {{current_biometrics_HRV}}
* 待处理人工签字队列: {{sign_queue}}
* 关键问题 (非空时自动提升P0): {{critical_issues}}
* 行动队列:
  P0(当日): {{action_queue_p0}}
  P1(本周): {{action_queue_p1}}
  P2(持续): {{action_queue_p2}}
```

### 2. 监控仪表板注入点

```
┌──────────────────────────────────────────────────────────┐
│  L1 结构健康  │ 断链: {{broken_links_total}}条           │
│               │ 孤岛率: {{orphan_rate}}%                  │
│               │ 标签合规: {{tag_compliance}}%             │
│               │ FM完整: {{fm_completeness}}% (缺陷{{fm_issues}}篇) │
│               │ sync-conflict: {{sync_conflict_md}}篇 🔴  │
│               │ 短文件(<500B): {{short_file_count}}篇     │
│  L2 内容质量  │ D3深度: {{deep_rate}}%                   │
│               │ A1可操作: {{actionable_rate}}%            │
│               │ K3元认知: {{metacognition_rate}}%         │
│  L3 知识体系  │ 概念覆盖: {{concept_coverage}}%           │
│               │ MOC覆盖: {{moc_coverage_avg}}%           │
│               │ 主导领域: {{dominant_domain}} {{dominant_domain_pct}}% │
│  综合健康度   │ {{health_score}} {{health_grade}}         │
│  趋势         │ {{trend_health_delta}}                    │
│  关键问题     │ {{critical_issues}}                       │
└──────────────────────────────────────────────────────────┘
```
┌──────────────────────────────────────────────────────────┐
│  L1 结构健康  │ 断链率: {{broken_link_rate}}%            │
│               │ 孤岛率: {{orphan_rate}}%                  │
│               │ 标签合规: {{tag_compliance}}%             │
│  L2 内容质量  │ 深度率: {{deep_rate}}%                   │
│               │ 可操作率: {{actionable_rate}}%            │
│               │ 元认知率: {{metacognition_rate}}%         │
│  L3 知识体系  │ 概念覆盖: {{concept_coverage}}%           │
│               │ MOC 覆盖: {{moc_coverage_avg}}%           │
│               │ 主导领域: {{dominant_domain_pct}}%        │
│  综合健康度   │ {{health_score}} {{health_grade}}         │
└──────────────────────────────────────────────────────────┘
```

### 3. 晨间计划审计快照注入点

```markdown
## 全局审计快照 (02:00 冷审计馈入)
* 系统健康度: {{health_score}} {{health_grade}}
* 断链: {{broken_links_total}}条 | 孤岛率: {{orphan_rate}}%
* 领域失衡度: {{dominant_domain_pct}}% ({{dominant_domain}})
* D3深度率: {{deep_rate}}% | A1可操作率: {{actionable_rate}}%
* sync-conflict: {{sync_conflict_md}}篇(.md) + {{sync_conflict_index}}个(索引)
* FM缺陷: {{fm_issues}}篇 | 短文件: {{short_file_count}}篇
* 趋势: {{trend_health_delta}} | {{trend_broken_delta}} | {{trend_sync_delta}}
## 关键问题 (自动提升P0)
{{critical_issues}}
## 行动队列
P0(当日): {{action_queue_p0}}
```

---

## JSON 契约校验 Schema

调度层解析 `trend.json` 时，应提取以下精简块作为晨间初始化参数：

```json
{
  "audit_snapshot_v1": {
    "generated_at": "YYYY-MM-DDTHH:MM",
    "layer1": {
      "total_notes": 9761,
      "broken_links_total": 3,
      "orphan_rate": 4.8,
      "tag_compliance": 93.3,
      "fm_complete_rate": 99.4,
      "fm_issue_count": 55,
      "skill_reuse_rate": 83.7,
      "sync_conflict_md": 18,
      "sync_conflict_index": 3873,
      "short_files_500b": 1483
    },
    "layer2": {
      "deep_rate": 79.6,
      "actionable_rate": 32.2,
      "metacognition_rate": 55.7
    },
    "layer3": {
      "concept_coverage": 100.0,
      "dominant_domain": "维度/学习",
      "dominant_domain_pct": 38.5,
      "domain_balance": "stable",
      "moc_coverage_avg": 89.4,
      "knowledge_gaps": 7
    },
    "health": {
      "score": 93.0,
      "grade": "A"
    },
    "critical_issues": [
      "sync-conflict .md文件18篇需清理",
      "twin_index sync-conflict 3,873个二进制index文件",
      "01-BRAIN断链回升+3"
    ],
    "action_queue": {
      "P0": ["清理18篇sync-conflict.md", "清理3,873个twin_index冲突文件", "修复3个01-BRAIN断链"],
      "P1": ["audit/intentional_stale标签治理", "01-BRAIN短文件充实"],
      "P2": ["uWise孤岛治理", "C8-哲学与宗教评估"]
    },
    "comparison_with_prev": {
      "date": "2026-07-01",
      "total_notes_change": "+82",
      "broken_links": "0→3(+3回升)",
      "sync_conflict": "0→18(+18爆发)",
      "domain_learning_change": "38.7%→38.5%(-0.2%)",
      "health_change": "91.0(A-)→93.0(A+2)"
    }
  }
}
```

---

## Twin-Loop Bridge 数据契约（S1 新增）

| 文件路径 | 格式 | 生产者 | 消费者 | 字段 |
|---------|------|--------|--------|------|
| `.runtime-context/twin-injection-YYYYMMDD.md` | Markdown | `twin_bridge.py` | Daily Loop | 经验快照 + 维度分布 |
| `treasury_data/twin_insight_cache.json` | JSON | `twin_bridge.py` | Treasury 循环 | `{date, insights[{path, title, preview, score}]}` |
| `twin_recovery_suggestions.md` | Markdown | `twin_bridge.py` | Bio-Loop | 健康洞察 + 恢复建议 |
| `twin_relationship_alerts.json` | JSON | `twin_bridge.py` | Social Capital | `{date, alerts[{path, title, preview}]}` |
| `00-META/循环工程审计快照.json` | JSON | `twin_bridge.py` | 审计层 | `{twin_distill_entries, twin_last_distill, twin_bridge_status}` |

## Treasury-Loop Bridge 数据契约（S2 新增）

| 文件路径 | 格式 | 生产者 | 消费者 | 字段 |
|---------|------|--------|--------|------|
| `.runtime-context/treasury-p0-queue.json` | JSON | `treasury_loop.py` | P0 队列 | `{date, items[{id, rule_id, name, current_value, threshold, priority}]}` |
| `.runtime-context/treasury-injection-YYYYMMDD.md` | Markdown | `treasury_loop.py` | Daily Loop | 风控状态 + 持仓概览 + Twin 投资洞察 |
| `treasury_data/investment_loop_status.json` | JSON | `treasury_loop.py` | 投资循环 | `{date, risk_overall, freeze, next_action, rules}` |
| `00-META/循环工程审计快照.json` | JSON | `treasury_loop.py` | 审计层 | `{treasury_overall_status, treasury_hard_triggers, treasury_cash_ratio}` |

## Bio-Loop Bridge 数据契约（S7 新增）

| 文件路径 | 格式 | 生产者 | 消费者 | 字段 |
|---------|------|--------|--------|------|
| `.runtime-context/bioloop-injection-YYYYMMDD.md` | Markdown | `bioloop_loop.py` | Daily Loop | 今日训练 + HRV 状态 + 月度跑量 |
| `running_loop_status.json` | JSON | `bioloop_loop.py` | Bio-Loop | `{date, today_running, hrv_trend, monthly_mileage}` |
| `recovery_week_alert.md` | Markdown | `bioloop_loop.py` | Operator | 恢复周触发通知 |
| `00-META/循环工程审计快照.json` | JSON | `bioloop_loop.py` | 审计层 | `{bioloop_avg_hrv, bioloop_hrv_status, bioloop_monthly_km}` |

---

## 版本兼容规则

| 契约版本 | `trend.json` schema | 调度入口版本 | 说明 |
|---------|:-------------------:|:-----------:|------|
| v1 | v1.6 | v1.2 | 基础字段映射（已过时） |
| v1.1 | v1.9+ | v1.3+ | 新增 sync_conflict/critical_issues/action_queue/trend_delta（当前版） |
| v2 (规划) | v2.0 | v2.0+ | 跨周期对比字段增强 |

- **前向兼容**：调度层仅读取映射表中定义的字段，忽略 `trend.json` 新增字段
- **缺省值**：若某字段在 `trend.json` 中不存在，调度层使用 `—` 或 `null` 填充
- **强制字段**：`total_notes` / `broken_links_total` / `health_score` 为 P0 级，缺失则标记 `⚠️ 数据源异常`
- **告警字段**：`critical_issues` / `action_queue` / `comparison_with_prev` 非空时，调度层必须自动提升为任务优先级

---

## 关联

- [[uSkill-agent-循环工程统一调度入口]] — 消费方：调度中枢 v1.2
- [[uSkill-agent-每日领域共生循环系统]] — 消费方：晨间计划 v1.2
- [[uSkill-agent-全局审计专项循环]] — 生产方：审计层 v1.4
- `00-META/审计/trend.json` — 物理数据源


![[SKILL]]

---

*契约版本：v1.2 | 数据源 schema：v1.9 | 消费方：调度入口 v1.3+ | 更新：2026-07-10*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

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
| ""字段名差不多就行"" | "差一个下划线就差一个世界，数据契约必须精确匹配" |
| ""版本号以后再统一"" | "版本混乱 = 数据混乱，Schema 契约必须一次性对齐" |
| ""先跑通再说，契约后面补"" | "没有契约的数据流 = 定时炸弹，早晚爆炸" |

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


**相关概念**：[[循环工程]]

---


## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据


## 🎯 技能概述

> 本技能提供 通用 领域的标准化操作流程，帮助用户高效完成相关任务。

**核心价值**：将复杂操作标准化为可重复执行的步骤，降低出错率，提升效率。

**适用场景**：
1. 日常操作执行
2. 新手快速上手
3. 质量一致性保证

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
