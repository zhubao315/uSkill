---
name: uskill-meta-life-os-evolve
description: "让人生操作系统进化-Schema-v2变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-meta-life-os-evolve.md"
  original_id: "SKL-6894"
  version: "3.0.0"
  trust: untrusted
---

# 人生操作系统进化-Schema-v2

description: |
  当用户需要定义、执行或评估人生操作系统的自主进化循环时使用此 Skill。
  触发词包括：'人生操作系统'、'自主进化'、'进化循环'、'系统升级'、
  'Life OS'、'进化报告'、'季度复盘'。当用户讨论系统版本更新、
  循环机制设计、进化健康度评估时，即使未直接说"人生操作系统"，
  也应使用此 Skill。不适用于单次任务执行（使用对应领域 Skill）。
  遇到系统级进化需求时优先使用。

---

# uSkill-005: 人生操作系统自主进化

## 🎯 目标

> 定义人生操作系统的三循环自主进化机制（日/周/季），将系统从被动工具升级为主动进化的智能伙伴。2.0 版本集成 Self-Play 自博弈验证与 OVP 数据驱动。

**核心价值**：让系统能够自动识别模式、发现问题、提出升级建议，并通过 Self-Play 验证升级的有效性。

**适用场景**：
- 每日复盘后触发日循环优化
- 每周日触发周循环模式识别
- 每季度第一周触发系统级评估与升级

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `cycle_type` | `enum` | ✅ | — | `daily` / `weekly` / `quarterly` |
| `daily_review` | `object` | ❌ | — | `{tasks_completed: [], energy_level: int, insights: [], date: string}` |
| `weekly_data` | `object` | ❌ | — | `{daily_reviews: [], okr_progress: object}` |
| `quarterly_data` | `object` | ❌ | — | `{weekly_reviews: [], historical_patterns: object, environment_changes: []}` |

**输入约束**：
- `daily_review.energy_level` 范围 1-5
- `weekly_data.daily_reviews` 至少包含 3 天数据
- `quarterly_data` 必须包含 `historical_patterns`

---

## 📤 输出

### 日循环输出
```json
{
  "cycle": "daily",
  "deviations": [
    {
      "planned": "string",
      "actual": "string",
      "gap": "string",
      "severity": "low|medium|high"
    }
  ],
  "optimization_hint": "string — 注入明日计划的优化建议",
  "pattern_signal": "string — 检测到的模式信号",
  "history_updated": true,
  "ovp_check": {
    "daily_completion_rate": "number",
    "deviation_count": "int",
    "within_threshold": true
  }
}
```

### 周循环输出
```json
{
  "cycle": "weekly",
  "completion_rate_pct": "number",
  "patterns": {
    "success": ["string — 成功模式"],
    "failure": ["string — 失败模式"],
    "energy": "string — 能量曲线与任务完成相关性",
    "new_discovery": "string — 本周新发现的模式"
  },
  "adjustments": {
    "task_volume": "string — 任务数量调整建议",
    "schedule": "string — 时间安排优化建议",
    "habits": ["string — 习惯微调建议"]
  },
  "self_play_result": {
    "test_count": "int",
    "pass_count": "int",
    "critic_findings": ["string — Critic 发现的问题"],
    "improvement_applied": "string — 应用的改进"
  },
  "weekly_report": "string — 周回顾文档"
}
```

### 季循环输出
```json
{
  "cycle": "quarterly",
  "data_aggregation": {
    "period_days": 90,
    "key_trends": ["string"],
    "anomalies": ["string"],
    "data_completeness_pct": "number"
  },
  "analysis": {
    "success_patterns": ["string"],
    "failure_root_causes": ["string"],
    "environment_changes": ["string"],
    "system_modules_audit": [
      {
        "module": "string",
        "usage": "high|low|unused",
        "action": "keep|optimize|remove",
        "confidence": "number"
      }
    ]
  },
  "upgrade_plan": {
    "new_modules": ["string"],
    "remove_modules": ["string"],
    "parameter_adjustments": [
      {
        "param": "string",
        "old_value": "string",
        "new_value": "string",
        "reason": "string"
      }
    ],
    "version": "string"
  },
  "self_play_validation": {
    "scenarios_tested": "int",
    "pass_rate_pct": "number",
    "critical_findings": ["string"],
    "validated_by": "Generator + Critic + Validator"
  },
  "evolution_report": "string — 季度进化报告",
  "next_quarter_goals": ["string"]
}
```

---

## 📋 执行步骤

### 日循环（每日晚间复盘后触发）

**Step 1: 数据采集**
- **输入**：当日日记、任务完成记录、能量状态
- **动作**：读取 `notes/01-Projects/每日复盘/` + Health Connect 数据
- **输出**：`daily_review` 对象
- **检查点**：✅ 验证数据完整性（energy_level 必填）

**Step 2: 偏差分析**
- **输入**：`daily_review`
- **动作**：对比计划 vs 实际，标记偏差项，计算偏差严重度
- **输出**：`deviations` 数组
- **分支条件**：
  - IF 偏差率 > 50% → 标记 `WARNING_HIGH_DEVIATION` + 简化次日计划
  - IF 能量 < 2 → 标记 `WARNING_LOW_ENERGY` + 推荐恢复活动
  - ELSE → 正常流程
- **检查点**：✅ 验证偏差项均有 severity 标记

**Step 3: 模式信号提取**
- **输入**：`deviations` + 历史 `history.json`
- **动作**：检测重复偏差模式（连续 3 天同一类偏差）
- **输出**：`pattern_signal`
- **检查点**：✅ 验证 pattern_signal 非空

**Step 4: 次日优化注入**
- **输入**：`deviations` + `pattern_signal`
- **动作**：生成次日优化建议，更新 `history.json`
- **输出**：`optimization_hint`
- **检查点**：✅ 验证 history.json 已更新

**Step 5: OVP 校验**
- **输入**：当日执行数据
- **动作*

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
