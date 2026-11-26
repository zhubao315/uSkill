
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
- **动作**：计算 daily_completion_rate，判断是否 within_threshold
- **输出**：`ovp_check`
- **检查点**：✅ 验证 OVP 指标已计算

---

### 周循环（每周日触发）

**Step 1: 周数据聚合**
- **输入**：7 天 `daily_review` 记录
- **动作**：汇总完成率、能量曲线、洞察清单
- **输出**：聚合数据
- **分支条件**：
  - IF 缺失天数 > 2 → 标记 `WARNING_INCOMPLETE_WEEK` + 基于可用数据分析
  - IF 缺失天数 > 4 → 标记 `ERROR_INSUFFICIENT_DATA` + 跳过本周
- **检查点**：✅ 验证至少 3 天数据

**Step 2: 模式识别**
- **输入**：聚合数据 + 历史周数据
- **动作**：识别成功模式、失败模式、能量模式
- **输出**：`patterns` 对象
- **检查点**：✅ 验证每个模式有具体描述

**Step 3: 流程调整建议**
- **输入**：`patterns`
- **动作**：生成任务数量、时间安排、习惯微调建议
- **输出**：`adjustments` 对象
- **检查点**：✅ 验证建议可执行（非空泛）

**Step 4: Self-Play 验证**
- **输入**：`patterns` + `adjustments`
- **动作**：
  - Generator 生成 3 个候选优化方案
  - Critic 用 `critic_rules` 攻击
  - 在 `evals.json` 上跑分
  - 胜出方案写入周报
- **输出**：`self_play_result`
- **检查点**：✅ 验证至少通过 1 个测试用例

**Step 5: 周报生成**
- **输入**：所有前序输出
- **动作**：生成结构化周报文档
- **输出**：`weekly_report` + 写入 `notes/01-Projects/周回顾/`
- **检查点**：✅ 验证周报文件已创建

---

### 季循环（每季度第一周触发）

**Step 1: 数据收集（第 1-2 周）**
- **输入**：90 天所有日/周循环数据
- **动作**：聚合统计、趋势分析、异常标记
- **输出**：`data_aggregation`
- **检查点**：✅ 验证 data_completeness_pct ≥ 70%

**Step 2: 系统审计（第 3 周）**
- **输入**：聚合数据 + 系统模块清单
- **动作**：逐模块评估使用频率、效果、成本
- **输出**：`system_modules_audit`
- **分支条件**：
  - IF 模块 usage = unused 连续 2 季 → 标记 `recommend_remove`
  - IF 模块 usage = low → 标记 `recommend_optimize`
  - IF 模块 usage = high → 标记 `keep`
- **检查点**：✅ 验证每个模块有 action 标记

**Step 3: 升级方案设计**
- **输入**：`system_modules_audit` + 环境变化评估
- **动作**：设计新增/删除/调参方案
- **输出**：`upgrade_plan`
- **检查点**：✅ 验证 version 符合语义化版本

**Step 4: Self-Play 全量验证**
- **输入**：`upgrade_plan`
- **动作**：
  - Generator 生成 5 个候选升级方案
  - Critic 用全部 `critic_rules` 攻击
  - 在 `evals.json` 全量测试
  - 胜出方案通过 Validator 在真实数据验证
- **输出**：`self_play_validation`
- **检查点**：✅ 验证 pass_rate_pct ≥ 80%

**Step 5: 用户审批 + 实施**
- **输入**：`upgrade_plan` + `self_play_validation`
- **动作**：呈现方案 → 用户审批 → 执行变更 → 更新版本号
- **输出**：`evolution_report` + `next_quarter_goals`
- **检查点**：✅ 验证用户已审批（人工兜底点）

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. 所有系统变更**必须**经用户审批（人工兜底点）
2. 日循环数据缺失 > 40% 时**必须**标记异常并简化分析
3. Self-Play 测试用例**不得**跳过 Critic 攻击阶段
4. 升级方案**不得**删除用户手动创建的模块（只删除 Agent 生成的）

### 软性约束（建议遵守）
1. 建议每次升级不超过 3 个模块变更
2. 建议版本号遵循语义化版本规范
3. 建议保留历史版本备份

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `WARNING_INCOMPLETE_WEEK` | 周数据缺失 > 2 天 | 基于可用数据分析 + 标记 | 🟡 |
| `ERROR_INSUFFICIENT_DATA` | 周数据缺失 > 4 天 | 跳过本周 + 标记 | 🔴 |
| `WARNING_HIGH_DEVIATION` | 日偏差率 > 50% | 简化次日计划 | 🟡 |
| `WARNING_LOW_ENERGY` | 能量 < 2 | 推荐恢复活动 | 🟡 |
| `ERROR_DATA_CORRUPTED` | JSON 解析失败 | 回滚到上一版本 + 告警 | 🔴 |
| `ERROR_UPGRADE_FAILED` | 版本升级失败 | 保留旧版本 + 标记 | 🔴 |

### 降级策略
- 当 Self-Play 不可用时，降级为单方案执行（无 Critic 验证）
- 当 OVP 校验不可用时，降级为手动记录模式

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 字段类型与 Schema 一致

### 内容校验
- [ ] deviations 每项有 severity 标记
- [ ] patterns 每项有具体描述（非空泛）
- [ ] adjustments 每项可执行

### 合规校验
- [ ] 硬性约束未违反
- [ ] 人工兜底点已正确触发（季度升级必须用户审批）
- [ ] Self-Play 测试用例已执行

### OVP 验证信号
- 日循环执行率 ≥ 85%
- 周循环执行率 ≥ 80%
- 模式识别建议采纳率 ≥ 60%
- 季度 Self-Play 通过率 ≥ 80%

---

## 🔄 迭代触发条件

### Self-Play 触发
- **频率**：weekly（周循环内置）
- **触发条件**：
  - 每次周循环自动触发
  - 季度升级方案必须触发

### 版本升级触发
- minor 版本：新增模块或调整参数
- major 版本：删除模块或改变循环机制

### 废弃触发
- 当模块连续 2 季度 unused 时，标记 deprecated

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags/ovp/self_play）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥3 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "日循环正常执行",
    "prompt": "执行今日人生操作系统日循环",
    "context": "今日完成 5/8 任务，能量 3/5，有 2 条洞察",
    "assertions": [
      "输出包含 deviations 数组",
      "deviations 每项有 severity",
      "output 包含 optimization_hint",
      "history.json 已更新"
    ],
    "expected_behavior": "分析偏差，提取模式，生成次日优化建议",
    "critic_attack": "optimization_hint 是否过于笼统？是否可执行？"
  },
  {
    "id": "test-002",
    "name": "日循环数据不足",
    "prompt": "执行日循环",
    "context": "仅有 1 条任务记录，无能量数据",
    "assertions": [
      "输出包含 WARNING 标记",
      "deviations 为空或标注数据不足",
      "optimization_hint 建议补充数据"
    ],
    "expected_behavior": "识别数据不足，标记警告，给出最小化分析",
    "critic_attack": "是否在数据不足时仍强行分析？"
  },
  {
    "id": "test-003",
    "name": "周循环模式识别",
    "prompt": "执行本周人生操作系统周循环",
    "context": "本周 7 天数据完整，完成率从 60% 提升到 85%",
    "assertions": [
      "输出包含 patterns.success",
      "识别到完成率提升趋势",
      "adjustments 建议具体可执行",
      "self_play_result 通过至少 1 个测试"
    ],
    "expected_behavior": "识别正向趋势，提取成功模式，建议保持",
    "critic_attack": "是否过度归因？是否有其他因素？"
  },
  {
    "id": "test-004",
    "name": "周循环数据缺失",
    "prompt": "执行周循环",
    "context": "仅有 2 天数据（缺失 5 天）",
    "assertions": [
      "输出标记 WARNING_INCOMPLETE_WEEK",
      "基于可用数据给出分析",
      "建议补充缺失数据"
    ],
    "expected_behavior": "标记数据不足，降级分析",
    "critic_attack": "降级分析是否仍有参考价值？"
  },
  {
    "id": "test-005",
    "name": "季度系统审计",
    "prompt": "执行本季度人生操作系统系统审计",
    "context": "过去 90 天数据完整，有 3 个模块连续 unused",
    "assertions": [
      "输出包含 system_modules_audit",
      "unused 模块标记 recommend_remove",
      "upgrade_plan 包含具体变更",
      "self_play_validation 通过率 ≥ 80%"
    ],
    "expected_behavior": "识别 unused 模块，建议删除，通过 Self-Play 验证",
    "critic_attack": "删除建议是否过于激进？是否有潜在价值？"
  }
]
```

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-12 | 1.0.0 | 初始版本，从 SOP-26 转化 |
| 2026-06-22 | 2.0.0 | 升级：集成 Self-Play + OVP 验证 + 驾驭工程约束 + Agent Mesh 协作 |

---

*关联：[[人生操作系统进化-Schema-v2]] · [[uSkill-Schema-模板]] · [[AI Co-Evolution 自主进化的人生操作系统]]*


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
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

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

---



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
