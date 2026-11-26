
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
    {"task": "阅读30页", "status": "partial", "actual_min": 15}
  ],
  "mood_score": 8,
  "energy_level": "high"
}
```

**输出**：
```json
{
  "completion_rate": {"overall": 83, "p0_tasks": 100, "p1_tasks": 100, "p2_tasks": 50},
  "insights": [{"type": "positive", "content": "P0/P1任务全部完成，执行力优秀", "actionable": false}],
  "tomorrow_recommendations": [{"priority": "P2", "action": "继续完成阅读任务，从第16页开始", "reason": "今日未完成", "estimated_min": 15}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 输入要点 | 期望输出 | 边界条件 |
|---|------|----------|----------|----------|
| 1 | 完美执行 | 全部完成 | 🟢 100%完成率 | 无偏差 |
| 2 | P0未完成 | P0任务skipped | 🔴 P0预警 | 关键任务 |
| 3 | 疲惫日 | energy=exhausted | 建议减负+早睡 | 能量极低 |
| 4 | 数据缺失 | 仅提供计划 | 推断+警告 | 部分输入 |
| 5 | 连续低效 | 连续3天<50% | 执行力危机预警 | 系统性问题 |

---

## 📊 版本记录

| 版本 | 日期 | 变更内容 | 验证结果 |
|------|------|----------|----------|
| v1.0 | 2026-06-17 | 初始 Prompt wrapper 版本 | — |
| v2.0 | 2026-06-29 | 升级为 Gen3 Schema：补齐 9 模块 | 待验证 |


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---
---

*Agent可读性标记：search_keywords=[晚间复盘；每日回顾；执行力追踪；计划vs实际]；context_triggers=[日终复盘；习惯养成；时间管理；个人效率]*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [训练类型] for [跑者水平], with [身体状态], leaning toward [训练计划/恢复策略]."

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
| ""今天状态不好不记录了"" | "跑完不记等于没跑，数据是训练的基础" |
| ""少跑一次没关系"" | "连续中断是放弃的前兆" |
| ""配速慢一点无所谓"" | "配速是训练强度的直接指标" |
| ""伤了再休息"" | "伤了再休息是被动休息，主动恢复才是正道" |
| ""不需要热身"" | "热身5分钟省的是5天伤病假" |

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


**相关概念**：[[情绪日记]]

---

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
