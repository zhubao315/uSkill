# Wait for the Pitch Decision / 等待击球法则

## Goal

Most people should do nothing most of the time. Truly life-changing decisions number only a few in a lifetime. This skill trains you to classify decisions, define clear "strike zone" criteria, and concentrate resources when the right opportunity arrives — minimizing decision fatigue and maximizing compounding returns.

## Core Insight

> "The big money is not in the buying and selling, but in the waiting." — Charlie Munger

Decision fatigue erodes judgment. Compounding favors concentration. Good opportunities are rare — but when they appear, acting decisively yields outsized returns.

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `decision` | string | Yes | The decision or opportunity currently under consideration |
| `domain` | string | No | Life domain: `investment`, `career`, `relationship`, `business`, `health`, `other` |
| `current_knowledge_level` | string | No | Your current understanding/preparedness: `low`, `medium`, `high` |
| `time_pressure` | string | No | Perceived urgency: `none`, `low`, `medium`, `high` |
| `criteria_met` | object | No | Key-value pairs of your strike zone criteria and whether each is met |

## Output

```json
{
  "decision_class": "routine | important | life-changing",
  "strike_zone_hit": true,
  "criteria_assessment": {
    "met": ["criterion_1", "criterion_2"],
    "not_met": ["criterion_3"],
    "unknown": ["criterion_4"]
  },
  "recommendation": "act_now | prepare_and_wait | dismiss",
  "confidence": 0.0,
  "preparation_actions": ["action_1", "action_2"],
  "rationale": "Explanation of the recommendation"
}
```

## Execution Steps

### Step 1: Classify the Decision

Categorize the decision into one of three tiers:

- **Routine** — Low consequence, reversible, frequent (daily meals, minor purchases). Decide quickly or automate.
- **Important** — Moderate consequence, partially reversible (job changes, large purchases). Apply standard analysis.
- **Life-changing** — High consequence, largely irreversible, rare (career pivot, marriage, major investment). Enter the strike zone protocol.

### Step 2: Define Strike Zone Criteria

For important and life-changing decisions, list all criteria that must be met before acting. Only act when **ALL** criteria are satisfied.

Example strike zone for a career change:
- [ ] Compensation ≥ current + 30%
- [ ] Role aligns with 10-year vision
- [ ] Company has strong fundamentals
- [ ] Team culture fits personal values
- [ ] No better alternative exists in 6-month horizon

### Step 3: Fill Waiting Time with Preparation

While waiting for criteria to be met:
- **Learn**: Deepen domain knowledge, study comparable cases
- **Build**: Develop skills, relationships, and resources needed for when the moment arrives
- **Monitor**: Track whether conditions are moving toward or away from your strike zone
- **Refine**: Adjust criteria based on new information

### Step 4: Concentrate When Criteria Are Met

When ALL strike zone criteria are hit:
- Act decisively and with full conviction
- Allocate disproportionate resources — this is the moment the preparation was for
- Avoid half-measures; the rarity of the opportunity justifies bold action
- Document the decision for future retrospective

## Exception Handling

| Situation | Action |
|---|---|
| Time pressure is genuine (not perceived) | Verify with a pre-mortem: "What if I don't act now?" If irreversible loss is certain, act |
| Too many criteria never met | Re-evaluate criteria — they may be too restrictive; adjust or accept the opportunity is not for you |
| Emotional pressure to act | Apply the "24-hour rule" — sleep on it. If still feels urgent after cooling down, re-evaluate |
| Criteria met but anxiety persists | Normal. Anxiety ≠ bad decision. Review your criteria objectively; if all are met, execute |

## Self-Check

After applying this skill, verify:

- [ ] Did I correctly classify the decision tier?
- [ ] Did I resist acting on incomplete strike zone criteria?
- [ ] Did I use waiting time productively (learning, building, monitoring)?
- [ ] When criteria were met, did I act with conviction and concentration?
- [ ] Did I document the decision and rationale for retrospective review?

## Examples

### Investment Decision
**Input**: "Should I invest in Company X right now?"
**Analysis**: 3 of 5 strike zone criteria met (valuation is right, but industry trend unclear and management change pending).
**Output**: `recommendation: prepare_and_wait` — Continue research, set alerts for management announcements, wait for all criteria.

### Career Decision
**Input**: "Should I accept this job offer?"
**Analysis**: Compensation meets threshold, role aligns with vision, but company culture is unknown.
**Output**: `recommendation: prepare_and_wait` — Schedule informational interviews with current employees, request a team lunch, set 2-week deadline.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-05-09 | Initial creation from 经验晶体 '等待击球法则' |


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
**相关笔记**：[[多尺度思考]] [[金线质量标准]] 


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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

## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位时机决策专家，擅长分析在社交、商业或沟通场景中"是否开口"的最优时机。请根据以下输入执行操作：
输入：[当前场景描述，含在场人物、对话氛围、自身目标]
要求：[分析维度，如对方信号、环境线索、风险收益]
输出格式：[等待或开口的决策建议，含时机信号清单、开口话术和风险预案]
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改


## 🎯 技能概述

> 本技能提供 认知与学习 领域的标准化操作流程，帮助用户高效完成相关任务。

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

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |

