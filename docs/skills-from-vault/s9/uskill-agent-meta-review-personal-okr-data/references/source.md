# Personal OKR & Data Review

## 🎯 目标
> AI 赋能的月度复盘流程，聚合个人全维度数据（运动/学习/工作/财务），对齐四大战略支柱，生成可执行的优化行动计划。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `review_period` | string | ✅ | 复盘周期，如 `2026-04` |
| `health_data` | object | ❌ | `{sleep_hours: [], hrv: [], resting_hr: [], run_km: []}` |
| `learning_data` | object | ❌ | `{notes_created: 0, books_read: 0, reading_hours: 0}` |
| `work_data` | object | ❌ | `{deep_work_hours: [], tasks_completed: 0, screen_time_hours: []}` |
| `finance_data` | object | ❌ | `{investment_return_pct: 0, savings: 0}` |
| `okr_targets` | object | ✅ | 四大支柱的月度目标值 |

## 📤 输出

```json
{
  "review_report": {
    "period": "string",
    "overall_score": "number — 0-100",
    "pillars": [
      {
        "name": "string — 身心赋能 | 智慧学习 | 效率倍增 | 沟通精进",
        "score": "number — 0-100",
        "key_metrics": [{"metric": "string", "actual": "number", "target": "number", "achievement_pct": "number"}],
        "trend": "improving | stable | declining"
      }
    ],
    "key_insights": ["string — 核心洞察"],
    "correlations": [{"variables": ["string", "string"], "relationship": "string", "strength": "strong | moderate | weak"}]
  },
  "root_cause_analysis": [
    {
      "issue": "string",
      "symptom": "string",
      "root_cause": "string",
      "evidence": "string"
    }
  ],
  "action_plan": [
    {
      "experiment": "string",
      "hypothesis": "string",
      "daily_actions": ["string"],
      "success_metric": "string",
      "duration_days": "int",
      "evaluation_criteria": "string"
    }
  ],
  "dashboard_update": {
    "core_kpis": [{"name": "string", "current": "number", "target": "number"}],
    "next_month_focus": ["string"]
  }
}
```

## 📋 执行步骤

1. **数据聚合与清洗** — 从各数据源收集上一周期数据（运动/学习/工作/财务），合并 CSV 并处理缺失值和异常值，确保四大支柱核心数据完整
2. **战略对齐分析** — 计算每个支柱的核心量化指标，与 OKR 目标对比计算达成率，生成趋势图和可视化仪表盘
3. **AI 洞察与根因分析** — 用 AI 做关联分析（如"睡眠质量 vs 深度工作时长"），对未达标指标进行根本原因分析（运用行为心理学理论），提炼 2-3 条核心洞察
4. **生成行动计划** — 针对每条洞察设计小规模"改进实验"，遵循 SMART 原则，设定量化成功指标和评估标准，产出 3-5 个具体行动项
5. **更新仪表盘与目标** — 汇总为月度复盘报告，更新个人效能仪表盘，根据连续趋势动态调整长期目标

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 数据源缺失过多（>50%） | 返回 `WARNING_INSUFFICIENT_DATA` + 建议数据收集改进方案 |
| 所有指标均达标 | 正常输出 + 建议提升目标难度 |
| 连续 3 月同指标未达标 | 标记 `STRATEGIC_DEVIATION` + 建议重新评估目标合理性 |
| AI 关联分析无显著发现 | 扩大数据时间窗口 + 尝试不同分析维度 |

## ✅ 自检清单

- [ ] 四大支柱均有核心指标数据
- [ ] 每个未达标指标有至少 1 个根因假设
- [ ] AI 发现至少 1 个非显而易见的数据关联
- [ ] 行动计划遵循 SMART 原则
- [ ] 每个"实验"有明确的成功/失败判断标准
- [ ] 复盘报告已归档


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-18 转化 |

---
**相关笔记**：[[成长心态]] [[个人数据 OKR 复盘]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

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
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

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


**相关概念**：[[战略 OKR 管理]]

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
