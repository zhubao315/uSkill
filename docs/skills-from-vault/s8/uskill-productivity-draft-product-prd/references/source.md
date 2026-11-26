# Draft Product Requirements Document

## 🎯 目标
> AI 赋能的产品价值发现与需求管理全流程——从市场洞察到高质量 PRD 输出，将创意到可执行 PRD 的周期缩短 70%，覆盖 4D 流程：Discover → Design → Deliver → Data-driven Iterate。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `idea_or_problem` | string | ✅ | 产品创意或待解决问题的描述 |
| `target_market` | string | ❌ | 目标市场/行业描述 |
| `user_interviews` | string | ❌ | 用户访谈记录或反馈文本 |
| `existing_product` | string | ❌ | 已有产品描述（用于功能迭代场景） |
| `team_context` | object | ❌ | `{ team_size, tech_stack, sprint_weeks }` |
| `prd_scope` | enum | ❌ | `full`（完整 PRD） / `feature`（单功能 PRD），默认 `full` |

## 📤 输出

```json
{
  "market_insight": {
    "tam_sam_som": { "tam": "string", "sam": "string", "som": "string" },
    "competitors": [
      {"name": "string", "strengths": "string", "weaknesses": "string"}
    ],
    "top_trends": ["string"],
    "opportunity_gaps": ["string"]
  },
  "user_personas": [
    {
      "name": "string",
      "demographics": "string",
      "pain_points": ["string"],
      "scenarios": ["string"],
      "behavior_tags": ["string"]
    }
  ],
  "product_backlog": [
    {
      "feature": "string",
      "rice_score": "number",
      "priority": "P0 | P1 | P2",
      "rationale": "string"
    }
  ],
  "prd": {
    "title": "string",
    "background": "string",
    "objectives": ["string"],
    "user_stories": [
      {
        "story": "string — As a ... I want ... so that ...",
        "acceptance_criteria": ["string"],
        "priority": "string"
      }
    ],
    "non_functional_requirements": {
      "performance": "string",
      "scalability": "string",
      "security": "string"
    },
    "success_metrics": [
      {"metric": "string", "target": "string", "measurement": "string"}
    ],
    "timeline": "string"
  }
}
```

## 📋 执行步骤

1. **Discover — 市场与用户洞察** — AI 扮演市场分析师生成 TAM/SAM/SOM 和竞品分析；从用户访谈中提炼用户画像、痛点和使用场景
2. **Design — 方案设计与优先级决策** — 头脑风暴多种解决方案，技术可行性前置评估，用 RICE 框架量化排序形成产品待办清单
3. **Deliver — PRD 撰写与需求对齐** — 将高优先级功能转化为用户故事和验收标准，汇总为结构化 PRD
4. **Data — 成功指标与迭代循环** — 定义量化成功指标，建立数据追踪和反馈渠道，形成"假设-验证-学习"闭环

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `idea_or_problem` 过于模糊 | 返回澄清问题清单，要求补充目标用户、痛点和价值主张 |
| 无用户访谈数据 | 使用 AI 生成假设性用户画像，标记 `HYPOTHETICAL` 待验证 |
| 功能列表 > 20 项 | 自动分批，先输出 P0 级功能的 PRD，P1/P2 后续迭代 |
| 技术可行性存疑 | 标记 `NEEDS_TECH_SPIKE`，建议先做技术预研再定 PRD |

## ✅ 自检清单

- [ ] 输出包含 `market_insight`、`user_personas`、`product_backlog`、`prd` 四大模块
- [ ] 每个用户故事有明确的、可测试的验收标准
- [ ] 竞品分析 ≥ 2 个竞争对手
- [ ] RICE 评分排序逻辑自洽
- [ ] 成功指标可量化、可追踪
- [ ] PRD 已涵盖非功能性需求


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-05 转化 |

---
**相关笔记**：`Go 语言开发` [[时间块规划]] 


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


**相关概念**：[[需求分析]]

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
