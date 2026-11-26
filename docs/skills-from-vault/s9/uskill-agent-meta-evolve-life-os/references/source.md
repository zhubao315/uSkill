
> ⚠️ 本文件为 v1.0 历史版本。v2.0（含 Self-Play + OVP）已迁移至 [[人生操作系统进化-Schema-v2]]。
> 新建 Skill 请使用 [[uSkill-Schema-模板]]。

# Life OS Autonomous Evolution

## 🎯 目标
> 定义人生操作系统的三循环自主进化机制（日循环/周循环/季循环），将系统从被动工具升级为主动进化的智能伙伴。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `cycle_type` | enum | ✅ | `daily` / `weekly` / `quarterly` |
| `daily_review` | object | ❌ | `{tasks_completed: [], energy_level: "int", insights: ["string"], date: "string"}` — 日循环输入 |
| `weekly_data` | object | ❌ | `{daily_reviews: ["object"], okr_progress: "object"}` — 周循环输入 |
| `quarterly_data` | object | ❌ | `{weekly_reviews: ["object"], historical_patterns: "object", environment_changes: ["string"]}` — 季循环输入 |

## 📤 输出

### 日循环输出
```json
{
  "cycle": "daily",
  "deviations": [{"planned": "string", "actual": "string", "gap": "string"}],
  "optimization_hint": "string — 注入明日计划的优化建议",
  "history_updated": "boolean"
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
    "energy": "string — 能量曲线与任务完成相关性"
  },
  "adjustments": {
    "task_volume": "string — 任务数量调整建议",
    "schedule": "string — 时间安排优化建议",
    "habits": ["string — 习惯微调建议"]
  },
  "weekly_report": "string — 周回顾文档"
}
```

### 季循环输出
```json
{
  "cycle": "quarterly",
  "data_aggregation": {
    "period_days": "int",
    "key_trends": ["string"],
    "anomalies": ["string"]
  },
  "analysis": {
    "success_patterns": ["string"],
    "failure_root_causes": ["string"],
    "environment_changes": ["string"],
    "system_modules_audit": [{"module": "string", "usage": "high | low | unused", "action": "keep | optimize | remove"}]
  },
  "upgrade_plan": {
    "new_modules": ["string"],
    "remove_modules": ["string"],
    "parameter_adjustments": [{"param": "string", "old_value": "string", "new_value": "string", "reason": "string"}],
    "version": "string"
  },
  "evolution_report": "string — 季度进化报告",
  "next_quarter_goals": ["string"]
}
```

## 📋 执行步骤

### 日循环（每日晚间）
1. **数据采集** — 读取今日复盘数据（完成率、能量水平、洞察）
2. **即时分析** — 对比计划 vs 实际，标记偏差项
3. **次日优化** — 将洞察注入明日计划生成逻辑，更新 history.json

### 周循环（每周日）
1. **周数据聚合** — 汇总 7 天完成率、能量曲线、洞察清单
2. **模式识别** — 分析成功模式（哪些天表现好？共同特征？）、失败模式（哪些天差？阻碍因素？）、能量模式（能量曲线与任务完成相关性）
3. **流程调整** — 根据模式调整任务数量、优化时间安排、微调习惯

### 季循环（每季度第一周）
1. **数据收集**（第 1-2 周）— 聚合过去 90 天所有数据，统计指标趋势，标记异常事件
2. **分析反思**（第 3 周）— AI 提取成功模式、失败根因分析、环境变化评估、系统模块审计
3. **系统升级**（第 4 周）— 生成升级建议（新增/删除/调参），用户审批后实施，更新版本号

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 日循环执行率连续 < 50% | 触发紧急优化：简化任务清单、降低目标 |
| 周数据缺失天数 > 2 | 标记 `WARNING_INCOMPLETE_WEEK` + 基于可用数据分析 |
| 季度升级建议过于激进 | 分批实施，优先采纳影响最大的 3 项 |
| 模式识别准确度 < 60% | 扩大分析窗口 + 增加数据维度 |

## ✅ 自检清单

- [ ] 日循环执行率 ≥ 85%
- [ ] 周循环执行率 ≥ 80%
- [ ] 季度进化必须完成
- [ ] 模式识别建议采纳率 ≥ 60%
- [ ] 系统自动化程度逐季提升
- [ ] 决策质量逐季改善
- [ ] 所有系统变更需用户审批


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

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-26-人生操作系统 转化 |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [学习任务] for [知识背景], with [学习目标], leaning toward [学习方法/输出形式]."

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
| ""以后再整理笔记"" | "以后不会来，现在就做" |
| ""读完就行了"" | "没有输出的阅读是自我感动" |
| ""这个太简单不用记"" | "简单的知识最容易忘" |
| ""收藏=学会"" | "收藏夹是知识的坟墓" |
| ""看完再总结"" | "看完就忘，边读边记才是正道" |

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


**相关概念**：[[个人效率系统工作流]]


**相关概念**：[[三大Agent-Skills框架方法论对比]] · [[Agent-Skills标准化爆发深度分析]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

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
