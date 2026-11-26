---
name: uskill-discovery-negotiation
description: "好的销售不是说服，是发现对方真正需要什么。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-discovery-negotiation.md"
  original_id: "SKL-6102"
  version: "3.0.0"
  trust: untrusted
---

# 客户发现与谈判

description: |
  当用户需要进行客户发现访谈、需求挖掘、方案谈判、赢率评估时使用此 Skill。
  触发词：'客户发现'、'需求挖掘'、'SPIN'、'谈判'、'商机评估'、'discovery call'。

# [[客户发现与谈判]]

## 🎯 目标

> 用结构化提问发现客户真实需求，用数据驱动谈判达成双赢。

**核心价值**：80% 的丢单发生在发现阶段——不是产品不好，是没搞清楚客户到底要什么。本 Skill 将发现和谈判标准化为可复制的方法论。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `deal_context` | string | ✅ | — | 商机背景（客户/行业/阶段） |
| `meeting_type` | enum | ❌ | `"discovery"` | 类型：`discovery`（发现）/ `demo`（演示）/ `negotiation`（谈判）/ `close`（成交） |
| `methodology` | enum | ❌ | `"spin"` | 方法论：`spin` / `gap_selling` / `sandler` / `meddpicc` |
| `competitor` | string | ❌ | — | 竞争对手（如有） |

## 📤 输出

```json
{
  "discovery_framework": {
    "situation_questions": ["string — 现状类问题"],
    "problem_questions": ["string — 痛点类问题"],
    "implication_questions": ["string — 影响类问题"],
    "need_payoff_questions": ["string — 价值类问题"]
  },
  "qualification_score": {
    "score": "int — 商机评分 (0-100)",
    "breakdown": {"pain": "int", "budget": "int", "authority": "int", "timeline": "int"},
    "recommendation": "string — 推进建议"
  },
  "negotiation_plan": {
    "our_position": "string — 我方立场",
    "their_position": "string — 预判对方立场",
    "tradeable_items": ["string — 可交换的筹码"],
    "walk_away_point": "string — 底线"
  }
}
```

## 📋 执行步骤

### Step 1: 发现阶段
1. **SPIN 提问** — Situation → Problem → Implication → Need-payoff
2. **痛点量化** — 将痛点转化为具体的业务影响（时间/金钱/风险）
3. **决策链** — 搞清楚谁是决策者、影响者、使用者、反对者
4. **检查点**：✅ 痛点是否已量化？决策链是否清晰？

### Step 2: 资格评估
1. **MEDDPICC** — Metrics/Economic Buyer/Decision Criteria/Decision Process/Paper Process/Identify Pain/Champion/Competition
2. **评分** — 对每个维度打分，计算总分
3. **推进/放弃决策** — 分数 <60 的商机考虑放弃或重新培育
4. **检查点**：✅ 评分是否有数据支撑？是否避免了主观判断？

### Step 3: 谈判策略
1. **价值锚定** — 先谈价值再谈价格
2. **让价策略** — 每次让价必须换取对等条件
3. **BATNA** — 明确最佳替代方案，不打无准备之仗
4. **检查点**：✅ 是否有明确的谈判底线？让价是否有交换条件？

### Step 4: 成交推进
1. **紧迫感** — 合理制造时间压力（非虚假）
2. **风险逆转** — 降低客户决策风险（试用/退款/分阶段）
3. **下一步** — 每次沟通结束明确下一步动作和时间
4. **检查点**：✅ 是否有成交信号？下一步是否明确？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 客户犹豫 | 长时间无进展 | 重新评估痛点是否真实，考虑放弃 |
| 竞争激烈 | 多家竞标 | 聚焦差异化优势，避免价格战 |
| 决策链复杂 | 多人决策 | 找到 Champion，逐个击破 |

## 💬 沟通风格

- **提问优先**：说的比听的多 = 失败的发现
- **价值导向**：先谈客户能得到什么，再谈你要收多少
- **不卑不亢**：有底线的灵活，不是一味让步

## 📝 自检清单

- [ ] 是否用了 SPIN/Gap Selling 结构化提问？
- [ ] 痛点是否量化为业务影响？
- [ ] 决策链是否清晰？
- [ ] 谈判底线是否明确？
- [ ] 每次沟通是否明确了下一步？

---


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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Discovery Coach + Deal Strategist + Sales Coach |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务] for [业务阶段], with [资源约束], leaning toward [策略框架/执行路径]."

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
| ""先做再说"" | "方向错了，执行力越强死得越快" |
| ""用户说想要这个"" | "用户说的是解决方案，不是需求本身" |
| ""竞品都在做"" | "竞品犯错不意味着你也应该犯" |
| ""这个市场很大"" | "大市场≠你能切到的市场" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
- 检查常见错误

### 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
