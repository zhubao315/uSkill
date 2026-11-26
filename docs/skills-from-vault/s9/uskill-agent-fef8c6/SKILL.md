---
name: uskill-agent-fef8c6
description: "让uSkill-全局审计专项循环变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-全局审计专项循环.md"
  original_id: "SKL-7204"
  version: "3.0.0"
  trust: untrusted
---

# uSkill-全局审计专项循环

# uSkill-全局审计专项循环

> **系统状态：** 🟢 正常 | **运行版本：** v2.0 / 全域合流版
> **全库基线：** 8,724 篇 | **最新执行：** 2026-06-30 三层全量冷审计通过 ✅ | 综合健康度 93.0 (A)
> **控制核心：** 意图优先于代码 (Intent over Code) | 彻底消除库内热熵

---

## 🎯 目标

本系统作为 **uLife OS 循环工程的第 7 循环（全局审计层）**，通过"结构 → 内容 → 体系"的三层刚性递进式冷审计，将原本高频调用产生的信息热熵强制冷凝，使知识库维持在低熵、高机器可读性状态。

### 🧭 三层审计架构与网格化调度

```
┌────────────────────────────────────────────────────────────────────────┐
│  Layer 3: 知识体系审计（每月 1 日 02:00）                                 │
│  "全局拓扑完整性" ─── 核心概念覆盖度 · 领域平衡系数 · 盲区缺口 · MOC 刚性路由 │
├────────────────────────────────────────────────────────────────────────┤
│  Layer 2: 内容质量审计（每周日 02:00）                                    │
│  "原子笔记高保真" ─── 深度判定 (D1-D3) · 时效性 · 知识三分类 (K1-K3) · 孤立度 │
├────────────────────────────────────────────────────────────────────────┤
│  Layer 1: 结构健康审计（每日 02:00）                                      │
│  "物理管道低熵化" ─── 伪 Wikilink 剥离 · 孤岛硬收容 · 脏标签死锁 · FM 补全  │
└────────────────────────────────────────────────────────────────────────┘
```

#### 📡 统一 Cron 触发网格

- **Layer 1 (每日 02:00)**：窗口 15min。依赖中枢：`[LOOP-DAILY]`。
- **Layer 2 (每周日 02:00)**：窗口 30min。依赖中枢：`[uSkill-技能推理器孤岛审计]`。
- **Layer 3 (每月 1 日 02:00)**：窗口 60min。依赖中枢：`[uSkill-知识孪生体深度蒸馏双链织入]`。

---

## 📥 输入

| 参数 | 含义 | 来源 |
|------|------|------|
| `raw_markdown` | 全库原始 Markdown 文本 | 文件系统遍历 |
| `audit_exceptions.json` | 豁免白名单 | `00-META/审计/` |
| `concept_list` | 核心概念清单 | 核心概念库 / 上月缓存 |
| `dataview_index` | 双向链接索引 | Dataview |
| `updated_days` / `incoming_links` | 单篇元数据 | frontmatter / 图谱 |
| `trend.json`（上期） | 历史基线 | `00-META/审计/` |

---

## 📤 输出

统一冷审计物理报告链条（增量流式写入 `00-META/审计/trend.json`）：

```
日报 (Daily)  --> 00-META/审计/YYYY-MM-DD-深夜审计报告.md
周报 (Weekly) --> 00-META/审计/YYYY-MM-DD-内容质量周报.md
月报 (Monthly)--> 00-META/审计/YYYY-MM-DD-知识体系月报.md
                                      │ (增量流式写入)
                                      ▼
                       📁 00-META/审计/trend.json
```

#### ⚙️ `trend.json` 刚性基线数据（2026-06-25 真实全量更新）

```json
{
  "date": "2026-06-25T03:00",
  "schema_version": "1.4",
  "note": "L1+L2+L3 三层全量执行，完成 144 篇 YAML 补全及 26 篇硬核过滤豁免",
  "layer1": {
    "total_notes": 10158,
    "broken_links": 161,
    "broken_link_rate": 1.58,
    "orphan_count": 1507,
    "orphan_rate": 14.8,
    "asset_entropy": 1.58,
    "tag_compliance": 100.0,
    "wild_tag_count": 0,
    "search_kw_coverage": 20.0,
    "moc_coverage": 100.0,
    "fm_completeness": 99.7,
    "concept_coverage": 100.0
  },
  "layer2": {
    "scanned_notes": 4200,
    "shallow_rate": 5.2,
    "deep_rate": 50.0,
    "stale_rate": 3.1,
    "actionable_rate": 49.8,
    "well_connected_rate": 91.1
  },
  "layer3": {
    "concept_coverage": 100.0,
    "domain_balance": "near_threshold",
    "dominant_domain": "维度/学习",
    "dominant_domain_pct": 39.4,
    "knowledge_gaps": 0,
    "gap_list": [],
    "moc_coverage_avg": 85.7,
    "moc_effective": 7
  }
}
```

---

## 🔄 执行流程

### Layer 1：结构健康审计（每日低熵管道）

**物理层 5 大刚性检查项**：
1. **死链精准过滤**：提取物理 `wikilink`，过滤代码块示例、别名重载及引用块。首次执行断链 1,694 条（4.6%），归口 `07-SOURCES` 概念收容仓。
2. **孤岛自适应控制**：判定无出入链笔记，豁免 `08-CALENDAR`、24-项目支持及 7 天内新创闪念。
3. **脏标签零容忍**：审查非标标签，阻断并提示归类，合规率锁 100%。
4. **Frontmatter (FM) 语义标记**：强制检查 `search_keywords` 与 `context_triggers`。基线 20%，长期攻坚指标。
5. **MOC 拓扑挂载**：核准核心概念节点向 89 个 MOC 目录的物理映射。

每天 02:15 生成 `00-META/审计/YYYY-MM-DD-深夜审计报告.md`，增量写入 `trend.json`。

### Layer 2：内容质量审计（每周内容解构）

**扫描靶向**：`01-BRAIN/`、`02-BUILD/22-uSkill/`、`02-BUILD/23-uWise/`、`03-Architect/`、`04-Investor/`。提示词见 [[uSkill-agent-全局审计专项循环#📝 Prompt 模板]]。

### Layer 3：知识体系审计（每月全局拓扑）

**体系级检查维度**：
- **概念覆盖度**：核心概念无实体 → 触发骨架预留。
- **领域平衡性**：单项占比 > 40% 触发死锁预警。
- **知识缺口**：被引 ≥5 次无实体的悬空链接 → 最高优先级 Backlog。
- **MOC 路由覆盖率**：核心 MOC 对子领域高频笔记覆盖率 ≥ 80%。

### 决策分支（IF / THEN）

- IF `broken_link_rate` ≥ 10% → THEN 触发审计熔断，纳入 P0，立即死链收容。
- IF `dominant_domain_pct` > 40% → THEN 立即触发结构性偏科预警，强制重分类骨架笔记。
- IF `dominant_domain_pct` 在 35%–40% → THEN 橙色预警，生成重分类建议但不自动执行。
- IF `incoming_links` == 0 → THEN 标记为 I3 孤立岛，纳入待重构 Backlog。
- IF 某笔记 `updated_days` 缺失 → THEN 时效维度判定为 FX，

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
