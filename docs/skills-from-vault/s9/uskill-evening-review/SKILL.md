---
name: uskill-evening-review
description: "让晚间复盘报告 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-evening-review.md"
  original_id: "SKL-6887"
  version: "3.0.0"
  trust: untrusted
---

# 晚间复盘报告 Agent — 实施手册

description: |
  当用户需要每日晚间复盘当日执行情况时使用此 Skill。
  触发词包括：'晚间复盘'、'今日复盘'、'每日回顾'、'日终总结'、'执行复盘'。
  当用户说"今天干了什么"、"帮我复盘一下"，即使未直接说"晚间复盘"，也应使用此 Skill。
  不适用于项目级复盘（用季度/年度复盘）。用于日常个人执行力的追踪与优化。

---

# 🌙 uSkill-304: 晚间复盘报告

## 🎯 目标

> 每日22:00自动复盘当日执行情况，对比计划vs实际，识别未完成项，生成洞察和明日建议。

**核心价值**：用数据驱动的每日复盘，持续优化个人执行力，避免"忙了一天不知道忙了什么"。

**适用场景**：
- 每日22:00定时复盘
- 工作日结束时的执行回顾
- 投资操作日的决策复盘
- 跑步/训练日的运动复盘
- 项目关键节点的进度检查

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `today_plan` | `array` | ✅ | — | 今日计划任务列表（含优先级和预计时长） |
| `actual_execution` | `array` | ❌ | — | 实际执行记录（含完成状态和实际时长） |
| `investment_data` | `object` | ❌ | — | 投资操作数据（如有） |
| `training_data` | `object` | ❌ | — | 训练数据（如有） |
| `mood_score` | `number` | ❌ | — | 今日心情评分（1-10） |
| `energy_level` | `enum` | ❌ | `normal` | `high` / `normal` / `low` / `exhausted` |

**输入约束**：
- `today_plan` 每项应有：task_name, priority(P0/P1/P2), estimated_minutes
- `actual_execution` 每项应有：task_name, status(completed/partial/skipped), actual_minutes
- 如未提供 actual_execution，将基于日记和行为数据推断

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话复盘结论",
  "date": "YYYY-MM-DD",
  "completion_rate": {
    "overall": "number (0-100%)",
    "p0_tasks": "number",
    "p1_tasks": "number",
    "p2_tasks": "number"
  },
  "plan_vs_actual": [
    {
      "task": "string",
      "priority": "P0|P1|P2",
      "estimated_min": "number",
      "actual_min": "number",
      "status": "completed|partial|skipped",
      "deviation_reason": "string"
    }
  ],
  "insights": [
    {
      "type": "positive|negative|neutral",
      "content": "string",
      "actionable": "boolean"
    }
  ],
  "tomorrow_recommendations": [
    {
      "priority": "P0|P1|P2",
      "action": "string",
      "reason": "string",
      "estimated_min": "number"
    }
  ],
  "habit_tracking": {
    "morning_routine": "boolean",
    "exercise": "boolean",
    "reading": "boolean",
    "meditation": "boolean"
  }
}
```

---

## 🔄 执行流程

```
1. [数据采集] → 接收输入数据
   → 判断条件：actual_execution 是否提供？
     → 是：使用实际数据
     → 否：从日记/行为数据推断执行情况

2. [完成率计算] → 对比计划vs实际
   → 按优先级分组计算完成率
   → overall = completed_count / total_count * 100%
   → 判断条件：P0 任务完成率 < 80%？
     → 是：🔴 P0未完成预警
     → 否：overall < 60%？
       → 是：🟡 整体完成率偏低
       → 否：🟢 执行力良好

3. [偏差分析] → 识别未完成项及原因
   → 逐项分析偏差原因：
     → 时间不足（估算偏差）
     → 优先级变更（临时插入任务）
     → 能量不足（疲劳/情绪影响）
     → 外部阻塞（等待他人/依赖未就绪）
     → 主动放弃（重新评估后放弃）
   → 产出：偏差原因分布

4. [洞察提取] → 从数据中提取模式
   → 正向洞察：哪些做得好？为什么好？
   → 负向洞察：哪些模式反复出现？根因是什么？
   → 中性洞察：有什么新发现？
   → 判断条件：是否有重复出现的负向模式？
     → 是：标注为「系统性问题」，建议专项解决
     → 否：标注为「偶发偏差」

5. [明日建议] → 基于复盘生成明日计划建议
   → 未完成 P0 任务 → 明日优先处理
   → 重复负向模式 → 明日针对性调整
   → 能量管理建议 → 基于 energy_level 和 mood_score
   → 判断条件：energy_level == exhausted？
     → 是：建议明日减负+早睡
     → 否：按正常节奏规划

6. [习惯追踪] → 检查日常习惯完成情况
   → 晨间流程、运动、阅读、冥想
   → 记录连续打卡天数

7. [输出报告] → 生成结构化复盘报告
```

---

## 📝 Prompt 模板

### 标准复盘 Prompt

```
你是晚间复盘Agent。请复盘今日执行情况。

【今日计划】
{today_plan}

【实际执行】
{actual_execution}

【复盘维度】
1. 完成率：按P0/P1/P2分别计算
2. 偏差分析：未完成项的原因分类
3. 洞察提取：正向/负向/中性模式识别
4. 明日建议：基于复盘的具体行动建议
5. 习惯追踪：晨间流程/运动/阅读/冥想

【输出要求】
- 完成率必须有具体数字
- 偏差原因必须具体到根因
- 明日建议必须可执行（有具体时间和行动）
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| today_plan 缺失 | 输出警告，基于日记推断 | 仅输出习惯追踪+心情记录 |
| actual_execution 缺失 | 基于日记/行为数据推断 | 完成率标注"推断值" |
| 所有任务完成 | 输出「🟢 完美执行日」 | 仅生成正向洞察 |
| 连续3天完成率<50% | 触发「执行力危机」预警 | 建议任务量减半+专注P0 |

---

## ✅ 质量自检

- [ ] 完成率计算准确（completed/total）
- [ ] P0 任务有单独完成率
- [ ] 偏差原因具体到根因（非泛泛而谈）
- [ ] 洞察有具体证据支撑
- [ ] 明日建议有具体时间/行动
- [ ] 习惯追踪覆盖4项核心习惯

---

## 💡 使用示例

### 示例 1：正常执行日

**输入**：
```json
{
  "today_plan": [
    {"task": "完成OKR复盘", "priority": "P0", "estimated_min": 60},
    {"task": "跑步13km", "priority": "P1", "estimated_min": 70},
    {"task": "阅读30页", "priority": "P2", "estimated_min": 30}
  ],
  "actual_execution": [
    {"task": "完成OKR复盘", "status": "completed", "actual_min": 55},
    {"task": "跑步13km", "status": "completed", "actual_min": 70},
    {"task": "阅读3

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
