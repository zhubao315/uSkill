
# Twin MCP 输入契约

> **用途**：定义 Knowledge Twin Agent 的 4 类输入源结构、字段 schema、蒸馏频率与优先级规则
> **关联**：[[uSkill-agent-每日领域共生循环系统]] · [[uSkill-agent-循环工程统一调度入口]] · [[2026年度目标 AI-Co Evolution]]
> **Q3 里程碑**：7/15 MVP 跑通，每日蒸馏 ≥1 条经验自动写入 Twin

---

## 架构总览

```
┌──────────────────────────────────────────────────────────────┐
│                    Knowledge Twin 蒸馏引擎                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ 📅 Daily  │  │ 🤖 uSkill │  │ 💰 投资  │  │ 💬 对话  │   │
│  │  Notes   │  │  Cards   │  │  复盘    │  │  流水    │   │
│  │ (日频)   │  │ (周频)   │  │ (周频)   │  │ (事件)   │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │              │              │              │          │
│       └──────────────┴──────┬───────┴──────────────┘          │
│                             │                                 │
│                    ┌────────┴────────┐                        │
│                    │  蒸馏 + 向量化   │                        │
│                    │  (本地 LLM)     │                        │
│                    └────────┬────────┘                        │
│                             │                                 │
│                    ┌────────┴────────┐                        │
│                    │  Twin 向量库    │                        │
│                    │  (知识图谱)     │                        │
│                    └─────────────────┘                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 源 1：Daily Notes（日记）

### 路径

```
08-CALENDAR/81-Daily-Notes/2026/YYYY-MM-DD.md
```

### 文件规模

- **总量**：~130 篇（2026-01-04 至 2026-06-26）
- **平均行数**：100-250 行/篇
- **增量**：日均 1 篇（非每日都有）

### Frontmatter Schema

```yaml
---
title: "YYYY-MM-DD"          # 必填，日期格式
created: YYYY-MM-DD          # 必填
updated: YYYY-MM-DD          # 必填
tags:                         # 必填
  - "维度/成长"               # 固定标签
  - "类型/日记"               # 固定标签
  - "来源/个人经历"           # 固定标签
---
```

### 内部结构（固定区块）

```markdown
# YYYY-MM-DD 领域共生日志与复盘    # 或 "每日日志"

## 📥 晨间计划 (08:00 AM)          # Block A：晨间计划
### 📌 建议任务一（🏗️ 架构师）      # 3 个任务 + 可选审计任务
### 📌 建议任务二（💰 投资人）
### 📌 建议任务三（📚 终身学习者）
## 📋 晨间计划状态                  # 表格：任务/身份/状态/完成时间/产出文件

## 📰 午间资讯 (12:00 PM)          # Block B：午间资讯
### 🔥 今日必读                     # 3-4 条高价值资讯
### 📊 数据速览                     # 市场指标表格

## 📝 生活记录                      # Block C：生活记录（可选）
## 全天对话流水备份                 # Block D：对话原始语料（占位）

## 🌙 晚间复盘总结                  # Block E：晚间复盘
### 完成率                         # 计划 vs 实际
### 今日洞察                       # 1-3 条核心洞察
### 明日建议                       # 1-3 条明日行动

## 🔄 循环工程执行记录              # Block F：循环状态表
```

### 蒸馏规则

| 区块 | 蒸馏频率 | 提取目标 | 优先级 |
|------|:--------:|---------|:------:|
| 晨间计划 | 日频 | 任务决策逻辑、Area→Project 映射 | P1 |
| 午间资讯 | 日频 | 市场判断、行业趋势信号 | P2 |
| 生活记录 | 日频 | 个人状态、精力模式、关系动态 | P2 |
| 对话流水 | 事件触发 | 原始思考、决策过程、情感信号 | P0 |
| 晚间复盘 | 日频 | 洞察、反思、方法论提炼 | P0 |
| 循环状态 | 日频 | 系统健康信号 | P3 |

### 提取字段

```yaml
daily_note:
  date: "YYYY-MM-DD"
  morning_tasks:
    - identity: "架构师|投资人|学习者|艺术家"
      task: "string"
      status: "done|pending|partial"
      output: "string"              # 产出文件链接
  market_snapshot:
    shanghai_index: float
    growth_index: float
    gold_price: "string"
    sentiment: "bullish|bearish|neutral"
  life_log:
    sleep_quality: "good|fair|poor"
    energy_level: "high|medium|low"
    relationships: "string"          # 关键关系动态
  evening_insights:
    - insight: "string"
      domain: "架构|投资|学习|生活"
      confidence: 0.0-1.0
  next_day_suggestions:
    - suggestion: "string"
      priority: "P0|P1|P2"
```

---

## 源 2：uSkill 技能卡

### 路径

```
02-BUILD/22-uSkill/
├── 智能体任务/           # 60 篇 Agent 实施手册
├── 投资/                 # 13 篇投资技能
├── 健康与生活/
├── 元技能/
├── 思维与认知/
├── 效率与工具/
├── 创意与表达/
└── ...（共 ~333 篇）
```

### 文件规模

- **总量**：333 篇（uSkill 目标 300 已超额）
- **重点子目录**：`智能体任务/`（60 篇）、`投资/`（13 篇）
- **平均行数**：30-80 行/篇

### Frontmatter Schema

```yaml
---
title: "uSkill-XXXX-v1"           # 必填，命名格式：uSkill-{技能名}-v{版本}
created: YYYY-MM-DD               # 必填
updated: YYYY-MM-DD               # 可选
tags:                             # 必填
  - "维度/技能"                   # 或 维度/管理 等
  - "类型/方法"                   # 或 类型/框架 等
---
```

### 内部结构（两种模板）

#### 模板 A：Agent 实施手册（智能体任务/）

```markdown
# 🤖 uSkill-XXXX Agent

> 一句话描述

## 执行 Prompt

```
{Agent 的完整 prompt 模板，含输入变量占位符}
```

---
**相关笔记**：[[笔记名]] [[笔记名]]
```

#### 模板 B：技能卡（投资/ 等）

```markdown
# 技能名称

> 一句话描述

## 核心规则
1. ...
2. ...

## 实操步骤
1. ...
2. ...

---
**相关笔记**：[[相关笔记]]
```

### 蒸馏规则

| 子目录 | 蒸馏频率 | 提取目标 | 优先级 |
|--------|:--------:|---------|:------:|
| 智能体任务/ | 周频（变更时触发） | Agent 能力边界、Prompt 模式、输入输出契约 | P0 |
| 投资/ | 周频 | 投资决策规则、风控逻辑、量化策略 | P1 |
| 健康与生活/ | 双周频 | 生活习惯模型、身心管理方法 | P2 |
| 其他 | 月频 | 通用方法论、思维模型 | P3 |

### 提取字段

```yaml
uskill_card:
  name: "string"                  # 技能名称
  version: "v1|v2|..."           # 版本号
  category: "agent|skill|sop"    # 类型
  domain: "架构|投资|健康|生活|思维|效率"  # 领域
  prompt_template: "string"      # Prompt 模板（agent 类型）
  input_variables:
    - name: "string"
      type: "string|number|array"
      description: "string"
  output_format: "string"        # 输出格式描述
  trigger_words:
    - "string"                   # 触发词列表
  dependencies:
    - "string"                   # 依赖的其他 uSkill
  last_used: "YYYY-MM-DD"       # 最近使用时间
  use_count: number              # 累计使用次数
```

---

## 源 3：投资复盘

### 路径

```
04-Investor/46-投资记录/
├── YYYY-MM-DD-投资组合综合分析报告.md
├── YYYY-MM-DD-持仓深度分析报告.md
├── YYYY-MM-DD-黄金投资策略复盘.md
├── 交易复盘模板.md
├── 投资日记.md
└── ...（共 43 个文件）
```

### 文件规模

- **总量**：43 个文件
- **结构化报告**：~10 篇（2026-06-24 集中产出）
- **模板/框架**：~5 篇
- **流水/记录**：~28 篇

### Frontmatter Schema

```yaml
---
title: "投资组合综合分析报告 — YYYY-MM-DD"   # 必填
created: YYYY-MM-DD                           # 必填
updated: YYYY-MM-DD                           # 可选
tags:
  - "维度/投资"                               # 固定标签
  - "类型/参考"                               # 或 类型/洞察
  - "来源/个人经历"                           # 固定标签
---
```

### 内部结构（综合分析报告模板）

```markdown
# 💰 投资组合综合分析 — YYYY-MM-DD

> **分析日期**：YYYY-MM-DD | **分析版本**：vX.X
> **关联**：[[uSkill-投资组合监控-v2]] · [[风控规则手册]]

---

## 市场环境总结               # Block A：宏观环境
## 组合表现评估               # Block B：组合 PnL
| 指标 | 数值 | 状态 |

## R1-R5 风控状态            # Block C：风控规则触发
| 规则 | 阈值 | 当前值 | 状态 |

## 贵金属专项分析             # Block D：贵金属
## 科技端分析                 # Block E：科技
## 组合优化建议               # Block F：调仓建议
## 明日操作清单               # Block G：可执行动作
```

### 蒸馏规则

| 文件类型 | 蒸馏频率 | 提取目标 | 优先级 |
|----------|:--------:|---------|:------:|
| 综合分析报告 | 事件触发（产出时） | 组合结构、PnL、风控触发 | P0 |
| 持仓深度分析 | 事件触发 | 单品种决策逻辑、仓位变化 | P0 |
| 策略复盘 | 事件触发 | 策略有效性、失效条件 | P1 |
| 交易复盘模板 | 月频 | 决策框架更新 | P2 |

### 提取字段

```yaml
investment_review:
  date: "YYYY-MM-DD"
  portfolio:
    total_value: number           # 总市值
    daily_pnl: number            # 当日盈亏
    daily_return_pct: float      # 当日收益率
    cumulative_pnl: number       # 累计盈亏
    position_pct: float          # 仓位比例
  holdings:
    - name: "string"             # 持仓名称
      ticker: "string"           # 代码
      weight_pct: float          # 占比
      daily_return_pct: float    # 当日涨跌
      cumulative_return_pct: float  # 累计收益
      thesis: "string"           # 持仓逻辑
  risk_rules:
    - rule_id: "R1-R5"
      threshold: "string"
      current_value: "string"
      status: "green|yellow|red"
  market_signals:
    - signal: "string"
      source: "string"
      confidence: 0.0-1.0
  action_items:
    - action: "string"
      priority: "P0|P1|P2"
      deadline: "string"
  key_insight: "string"           # 一句话核心洞察
```

---

## 源 4：对话流水

### 存储位置

对话流水有两种存储形式：

| 位置 | 说明 | 格式 |
|------|------|------|
| Daily Note 内嵌 | `## 全天对话流水备份` 区块 | 非结构化文本 |
| Session Memory | `[PRIVATE_PATH]` | checkpoint.md + tasks/ |

### Daily Note 内嵌对话流水

```markdown
## 全天对话流水备份

*在此处追加全天对话原文，作为晚上提炼的原始语料*

**对话1：{主题}（HH:MM）**
- 用户输入：{原文}
- Agent 输出：{摘要}
- 关键决策：{决策点}

**对话2：{主题}（HH:MM）**
...
```

### Session Memory 结构

```
memory/sessions/{session_id}/
├── checkpoint.md          # 结构化会话状态（11 个区块）
├── notes.md               # 自由笔记
└── tasks/{task_id}/
    └── progress.md        # 任务进度
```

### 蒸馏规则

| 来源 | 蒸馏频率 | 提取目标 | 优先级 |
|------|:--------:|---------|:------:|
| 对话流水（Daily Note） | 日频（晚间复盘时） | 决策过程、思考路径、情感信号 | P0 |
| Session Checkpoint | 事件触发（checkpoint 写入时） | 任务进展、学习记录、错误模式 | P1 |

### 提取字段

```yaml
dialogue_log:
  date: "YYYY-MM-DD"
  session_id: "string"
  conversations:
    - topic: "string"
      time: "HH:MM"
      user_intent: "string"          # 用户意图
      agent_action: "string"         # Agent 执行动作
      decision_point: "string"       # 关键决策
      outcome: "string"              # 结果
      emotion_signal: "string"       # 情感信号（如有）
      learnings:
        - "string"                   # 提炼的学习点
  fleeting_notes:
    - note: "string"
      domain: "架构|投资|学习|生活"
      source: "conversation|observation|reflection"
```

---

## 蒸馏频率矩阵

| 源 | 频率 | 触发条件 | 预估条数/周 |
|----|:----:|---------|:-----------:|
| 📅 Daily Notes | 日频 | 每日 20:00 晚间复盘时 | 5-7 条 |
| 🤖 uSkill 技能卡 | 周频 | 文件变更时 / 每周一扫描 | 2-5 条 |
| 💰 投资复盘 | 事件触发 | 新报告产出时 | 1-3 条 |
| 💬 对话流水 | 日频 + 事件 | 晚间复盘 + checkpoint 写入 | 5-10 条 |

**预期产出**：每日 ≥1 条经验写入 Twin，每周 ≥15 条结构化蒸馏记录。

---

## 数据流路径

```
每日 08:00    晨间计划 → 写入 Daily Note Block A
     ↓
每日 12:00    午间资讯 → 写入 Daily Note Block B
     ↓
全天          对话流水 → 追加至 Daily Note Block D
     ↓
每周一        uSkill 扫描 → 检测变更文件 → 触发蒸馏
     ↓
事件触发      投资复盘 → 写入 04-Investor/46-投资记录/
     ↓
每日 20:00    晚间复盘 → 蒸馏 Daily Note 全部 Block → Twin
     ↓
              Session Checkpoint → 蒸馏至 tasks/progress.md
```

---

## 关联

- [[uSkill-agent-每日领域共生循环系统]] — Daily Loop 三段式架构
- [[uSkill-agent-循环工程统一调度入口]] — 7 循环统一调度
- [[uSkill-agent-知识孪生体深度蒸馏双链织入]] — Twin 蒸馏核心算法
- [[2026-Q3-冲刺清单]] — Q3 冲刺里程碑
- [[2026年度目标 AI-Co Evolution]] — 年度战略上下文


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

*Twin MCP 输入契约 v1 | Q3 里程碑：7/15 MVP 跑通 | 每日蒸馏 ≥1 条经验*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [投资决策类型] for [投资者风格], with [风险偏好], leaning toward [分析框架/数据源]."

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
| ""这次不一样"" | "每次泡沫都说这次不一样，这次也一样" |
| ""先满仓再说"" | "满仓=零容错，一个回调就是灾难" |
| ""跌了就补仓"" | "越补越套是亏损扩大的主因" |
| ""长期持有就行"" | "长期持有不等于不做仓位管理" |
| ""这次消息是利好"" | "消息面驱动的交易成功率低于掷硬币" |

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


**相关概念**：[[信息管理系统]]

---


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
