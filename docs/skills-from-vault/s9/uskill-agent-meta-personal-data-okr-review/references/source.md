# Personal Data-Driven OKR Review

## 🎯 目标
> AI赋能的月度战略复盘：系统化聚合、分析个人全维度数据，与四大战略支柱对齐，生成可执行的优化行动计划，实现数据驱动的自我进化。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `review_period` | string | ✅ | 复盘周期，如 `"2026-04"` |
| `okr_targets` | object | ✅ | `{body: [], learning: [], productivity: [], finance: []}` — 四大支柱的OKR目标 |
| `data_sources` | object | ✅ | `{strava: [], garmin: [], toggl: [], obsidian: [], finance_app: [], ...}` — 各平台导出数据 |
| `focus_areas` | array | ❌ | 本次复盘重点关注的支柱，如 `["body", "productivity"]` |
| `review_depth` | enum | ❌ | `quick`（30分钟）/ `standard`（1小时）/ `deep`（2小时），默认 `standard` |
| `dashboard_state` | object | ❌ | `{last_month_scores: {}, trend_data: {}}` — 上月仪表盘状态 |

## 📤 输出

```json
{
  "pillar_scores": {
    "body": {
      "score": "number (0-100)",
      "trend": "up | flat | down",
      "key_metrics": [{"metric": "string", "value": "number", "target": "number", "achievement_pct": "number"}],
      "summary": "string"
    },
    "learning": { "/* same structure */": "" },
    "productivity": { "/* same structure */": "" },
    "finance": { "/* same structure */": "" }
  },
  "overall_score": "number (0-100)",
  "correlation_insights": [
    {"variables": ["string", "string"], "relationship": "positive | negative", "strength": "strong | moderate | weak", "insight": "string"}
  ],
  "root_cause_analysis": [
    {"unmet_goal": "string", "root_cause": "string", "evidence": "string", "framework": "string"}
  ],
  "core_insights": [
    {"insight": "string", "actionability": "high | medium | low", "priority": "number"}
  ],
  "action_plan": [
    {
      "experiment": "string — 改进实验名称",
      "hypothesis": "string — 实验假设",
      "daily_actions": ["string — 每日执行动作"],
      "success_metric": "string — 成功指标",
      "success_threshold": "string — 达标阈值",
      "duration": "string — 实验周期",
      "pillar": "body | learning | productivity | finance"
    }
  ],
  "dashboard_update": {
    "new_kpis": [{"metric": "string", "target": "number", "pillar": "string"}],
    "retired_kpis": ["string"],
    "adjusted_long_term_goals": [{"goal": "string", "old_target": "string", "new_target": "string", "reason": "string"}]
  },
  "monthly_report_md": "string — Markdown格式的完整月度复盘报告"
}
```

## 📋 执行步骤

### Step 1: 数据聚合与清洗
1. **收集四大支柱数据** — 从各平台导出上一周期数据
   - 身心赋能：Strava/Garmin跑步数据、智能手表睡眠/HRV数据
   - 智慧学习：Obsidian笔记增长数、阅读App读书时长/数量
   - 效率倍增：Toggl/RescueTime时间追踪、任务管理工具已完成任务数
   - 沟通精进：财务App投资收益、社交媒体互动数据
2. **数据清洗** — 合并CSV文件，处理缺失值和异常值
3. **完整性校验** — 确保四大支柱核心数据均已覆盖

### Step 2: 战略支柱对齐分析
1. **计算核心指标** — 针对每个支柱计算本周期量化指标
2. **与OKR对比** — 将指标与月度/季度OKR目标对比，计算达成率
3. **趋势分析** — 结合 `dashboard_state` 计算环比变化趋势
4. **可视化呈现** — 生成趋势图、瀑布图，更新仪表盘

### Step 3: AI辅助洞察与根本原因分析
1. **AI关联分析** — 让AI扮演"数据科学家"，将清洗后数据喂入，寻找隐藏关联
   - 示例：睡眠质量与次日深度工作时长的关系
   - 示例：跑量增加与投资决策冷静度的关系
2. **根本原因分析** — 对"未达标"指标，运用行为心理学进行根因分析
   - 示例：深度工作时长未达标 → AI发现下午效率低 → 可能是"决策疲劳"或"午后血糖波动"
3. **AI洞察提炼** — 让AI扮演"行为分析师"，提炼2-3条核心洞察

### Step 4: 生成洞察与行动计划
1. **总结核心洞察** — 提炼3-5条最核心、可行动的洞察
2. **设计改进"实验"** — 针对每条洞察设计小规模改进实验
3. **AI辅助生成计划** — 让AI扮演"个人效能教练"，转化为结构化行动计划
   - 遵循SMART原则
   - 为每个实验设定明确的成功/失败判断标准

### Step 5: 更新仪表盘与目标
1. **撰写复盘报告** — 汇总所有内容形成《月度个人OKR与数据复盘报告》
2. **更新仪表盘** — 将下月行动计划和关键指标更新到仪表盘
3. **调整长期目标** — 如连续多周期显示某目标不合理，进行战略性调整

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 某支柱数据完全缺失 | 返回 `WARNING_MISSING_PILLAR` + 该支柱标记为"数据不足"，不纳入评分 |
| 数据出现异常极值（如单日跑量100km） | 标记 `FLAG_OUTLIER` + 要求用户确认是否为录入错误 |
| `okr_targets` 未设定 | 返回 `ERROR_NO_OKR` + 要求至少设定每个支柱1个核心指标 |
| 所有支柱达标率>95% | 提示 `INFO_TARGETS_TOO_EASY` + 建议提高下月挑战度 |
| AI关联分析未发现显著关联 | 返回 `INFO_NO_CORRELATION` + 建议延长数据收集周期或增加数据维度 |
| `review_period` 跨度>2个月 | 提示 `WARNING_LONG_GAP` + 建议分段分析 |

## ✅ 自检清单

- [ ] 四大支柱的核心数据是否都已收集完毕？
- [ ] 数据是否存在明显的错误或遗漏？
- [ ] 每个战略支柱是否至少有1-2个核心指标进行追踪？
- [ ] 指标的达成情况是否一目了然？
- [ ] 是否对每个关键指标的波动都提出了至少一个根本原因假设？
- [ ] AI是否发现了至少一个未曾预料到的数据关联？
- [ ] 每个行动计划是否都遵循了SMART原则？
- [ ] 是否为每个"实验"都设定了明确的成功或失败判断标准？
- [ ] 复盘报告是否已归档，便于未来回顾？
- [ ] 下月核心指标和行动项是否已清晰展示在仪表盘上？


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
**相关笔记**：[[思维方法选择]] [[成长心态]] 


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


**相关概念**：[[战略 OKR 管理]] · [[个人效率系统工作流]]

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
