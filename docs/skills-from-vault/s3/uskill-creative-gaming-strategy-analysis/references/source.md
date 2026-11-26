# Gaming Strategy Analysis & Content Creation

## 🎯 目标
> 建立一套数据驱动的系统化流程，用于深度分析游戏版本与战局，并高效转化为个人竞技水平提升和高价值游戏内容创作。将单局复盘与策略提炼时间缩短 80%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `mode` | enum | ✅ | `competitive`（竞技提升）/ `content`（内容创作）/ `both`（双轨） |
| `version_patch_notes` | string | ❌ | 最新版本更新公告原文 |
| `match_data` | object | ❌ | `{hero_picks: ["string"], team_comps: ["string"], key_events: [{time: "string", event: "string"}], post_match_stats: {"string": "any"}, match_result: "win | loss"}` |
| `target_hero` | string | ❌ | 目标英雄名称（内容创作路径必填） |
| `content_platform` | enum | ❌ | `bilibili` / `zhihu` / `douyin`（内容创作路径选填） |
| `current_rank` | string | ❌ | 当前段位信息 |
| `known_issues` | ["string"] | ❌ | 已知个人短板（如"中期容易迷失节奏"） |

## 📤 输出

### 竞技提升路径 (`mode: competitive`)
```json
{
  "meta_analysis": {
    "tier_list": {"S": ["string"], "A": ["string"], "B": ["string"]},
    "meta_shifts": ["string — 版本 Meta 变化要点"],
    "underrated_picks": ["string — 被低估的潜力股英雄/战术"],
    "recommended_strategies": ["string — 新版本核心打法建议"]
  },
  "match_review": {
    "match_result": "win | loss",
    "winning_condition": "string — 胜负手分析",
    "bp_analysis": "string — Ban/Pick 阶段优劣势",
    "key_moments": [{ "time": "string", "decision": "string", "assessment": "correct | suboptimal", "alternative": "string" }],
    "economy_analysis": "string — 经济曲线与资源置换",
    "psychological_factors": ["string — 心理状态变化"],
    "top_3_improvements": [{ "issue": "string", "root_cause": "string", "practice_method": "string", "measurable_target": "string" }]
  },
  "training_plan": {
    "duration": "string — 如 '1 week'",
    "daily_tasks": [{ "day": "string", "tasks": ["string"], "duration_minutes": "int", "target_metric": "string" }],
    "weekly_goal": "string — 可衡量的周目标"
  }
}
```

### 内容创作路径 (`mode: content`)
```json
{
  "content_strategy": {
    "topic": "string — 具有稀缺性和深度的内容主题",
    "unique_insight": "string — 体现顶尖理解的独家知识点",
    "target_audience": "string",
    "hook": "string — 引人入胜的标题/开场"
  },
  "content_outline": {
    "sections": [{ "title": "string", "key_points": ["string"], "estimated_length": "string" }],
    "discussion_trigger": "string — 能引发评论区热烈讨论的结尾设计"
  },
  "draft": {
    "body": "string — 润色后的攻略文案或视频脚本",
    "tone": "professional-yet-engaging",
    "platform_adaptations": [{ "platform": "string", "adjustments": "string" }]
  }
}
```

## 📋 执行步骤

### 核心分析阶段

1. **版本与 Meta 分析** — 获取最新版本更新公告，让 AI 扮演"顶级战队数据分析师"，分析英雄、装备、地图机制调整，预测 T0/T1 英雄梯度和主流战术。运用价值投资思维寻找被低估的"潜力股"英雄或战术。
2. **对局复盘与数据分析** — 选取代表性对局录像，人工标记关键时间点（一级团、关键击杀、转折点团战），将关键事件、阵容、出装、数据面板输入 AI。让 AI 扮演"电竞复盘教练"，从经济曲线、决策逻辑、操作细节、资源置换角度深度复盘。识别数据背后的因果关系，分析心理状态变化。

### 竞技提升路径

3. **提炼个人提升点** — 基于复盘报告总结 Top 3 待改进项（必须足够具体，如"提高小地图关注频率"而非"提升意识"），让 AI 设计针对性练习方法。
4. **制定周度训练计划** — 将练习项目整合到一周计划，设定可衡量目标（如"本周完成50次特定连招练习，成功率达90%"），兼顾排位、巅峰赛和针对性练习的时间分配。

### 内容创作路径

5. **确定内容主题与框架** — 基于版本分析和复盘洞察确定稀缺性内容主题，让 AI 设计引人入胜的大纲或视频脚本框架。
6. **AI 辅助内容生成与发布** — 结合实战经验撰写初稿或录制素材，让 AI 扮演"游戏 KOL"润色文案使其更具网感和传播力，发布到知乎、B 站等平台。

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 版本更新公告缺失或不完整 | 基于高端局数据和社区讨论反推 Meta 变化 |
| 对局录像无法获取 | 使用赛后数据面板 + 个人回忆重建关键事件时间线 |
| 复盘分析过于笼统 | 要求 AI 聚焦具体时间点和决策，提供"如果重来"的替代方案 |
| 训练计划执行率 < 60% | 简化训练项目，降低单日负荷，增加趣味性 |
| 内容主题缺乏差异化 | 追问 AI "这个观点的独家之处在哪里"，挖掘更深层洞察 |
| 润色后失去专业性 | 设置红线术语清单，要求 AI 保留关键专业表达 |

## ✅ 自检清单

- [ ] Meta 预测与主流高端局表现初步吻合
- [ ] 复盘明确了本局"胜负手"
- [ ] AI 分析指出了自己未曾注意到的细节
- [ ] 待改进项足够具体且可执行
- [ ] 训练计划有可衡量的目标
- [ ] 内容主题体现了独特理解
- [ ] 最终内容既有深度又易于受众理解
- [ ] 内容具有"网感"和传播力


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-16-游戏王者-游戏攻略分析 转化 |

---
**相关笔记**：[[演讲节奏控制]] [[摄影后期处理]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [摄影场景] for [拍摄者水平], with [创作优先级], leaning toward [器材/环境约束]."

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
| ""直接给一组参数就行了"" | "不知道用户场景就给参数，是赌博不是指导" |
| ""ISO 高一点没关系"" | "后期降噪损失细节，能前期解决就别留后期" |
| ""先拍一张试试看"" | "曝光三角的价值在于拍前就知道结果" |
| ""这个场景太简单了"" | "越简单越容易犯低级错误" |
| ""用户没问安全快门"" | "安全快门是糊片第一道防线，必须主动检查" |

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


**相关概念**：[[游戏与发展]]

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
