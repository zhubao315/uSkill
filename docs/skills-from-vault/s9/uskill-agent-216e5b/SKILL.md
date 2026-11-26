---
name: uskill-agent-216e5b
description: "让循环工程-审计-调度数据契约变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-循环工程-审计-调度数据契约.md"
  original_id: "SKL-7062"
  version: "v1.2"
  trust: untrusted
---

# 循环工程-审计-调度数据契约-v1.2

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
| `comparison_with_prev.broken_links` | string | `{{trend_broken_delta

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
