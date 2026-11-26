---
name: uskill-sales-proposal
description: "提案不是功能清单，是帮客户赢得他自己的战役。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-sales-proposal.md"
  original_id: "SKL-6103"
  version: "3.0.0"
  trust: untrusted
---

# 销售方案与提案

description: |
  当用户需要撰写销售提案、RFP 响应、方案演示、竞标材料时使用此 Skill。
  触发词：'销售提案'、'RFP'、'方案'、'竞标'、'提案撰写'、'proposal'、'pitch deck'。

# [[销售方案与提案]]

## 🎯 目标

> 撰写以客户价值为核心的销售提案，而非以产品功能为核心的功能清单。

**核心价值**：客户买的不是你的产品，是他自己的问题被解决后的状态。本 Skill 确保每个提案都从客户视角出发。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `deal_context` | string | ✅ | — | 商机背景 |
| `proposal_type` | enum | ❌ | `"rfp_response"` | 类型：`rfp_response`（RFP 响应）/ `unsolicited`（主动提案）/ `renewal`（续约）/ `expansion`（扩展） |
| `format` | enum | ❌ | `"document"` | 格式：`document`（文档）/ `deck`（PPT）/ `demo`（演示） |
| `page_limit` | int | ❌ | `20` | 页数限制 |

## 📤 输出

```json
{
  "proposal_structure": {
    "executive_summary": "string — 执行摘要（1页）",
    "problem_statement": "string — 客户问题定义",
    "solution_overview": "string — 方案概述",
    "value_proposition": "string — 价值主张（含 ROI）",
    "implementation_plan": "string — 实施计划",
    "pricing": "string — 定价方案",
    "proof_points": ["string — 成功案例/数据证明"]
  },
  "differentiation": {
    "vs_competitors": "string — 差异化定位",
    "unique_advantages": ["string — 独特优势"]
  }
}
```

## 📋 执行步骤

### Step 1: 客户问题定义
1. **问题复述** — 用客户自己的话描述他的问题
2. **业务影响** — 量化问题的成本（时间/金钱/风险）
3. **成功标准** — 客户期望的解决方案是什么样的
4. **检查点**：✅ 问题是否用客户的语言描述？是否量化了影响？

### Step 2: 方案设计
1. **价值先行** — 开篇先说「你能得到什么」，而非「我们有什么」
2. **ROI 计算** — 量化方案带来的收益和节省
3. **实施路径** — 分阶段实施计划，降低客户风险感
4. **检查点**：✅ 方案是否以价值开篇？ROI 是否可量化？

### Step 3: 差异化与证明
1. **竞品对比** — 不贬低竞品，突出自身独特优势
2. **成功案例** — 同行业/同规模的成功案例
3. **数据证明** — 用数字而非形容词说服
4. **检查点**：✅ 差异化是否明确？是否有案例支撑？

### Step 4: 提案打磨
1. **一页摘要** — 高管只看第一页，确保核心信息完整
2. **视觉设计** — 图表 > 文字，一页一个核心信息
3. **语言精炼** — 删除所有不影响决策的文字
4. **检查点**：✅ 一页摘要是否完整？语言是否精炼？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| RFP 限制多 | 答案空间有限 | 聚焦最有差异化的 3 个点 |
| 竞争激烈 | 多家竞标 | 加入独特的成功案例和 ROI 计算 |
| 客户预算有限 | 低于预期 | 提供分阶段方案或精简版 |

## 💬 沟通风格

- **客户视角**：不说「我们提供」，说「你将获得」
- **数据说服**：每个价值主张附带数字
- **简洁有力**：能删的字都删，能用图表的不用文字

## 📝 自检清单

- [ ] 开篇是否以客户问题而非产品功能开始？
- [ ] 是否量化了 ROI？
- [ ] 差异化定位是否明确？
- [ ] 是否有成功案例支撑？
- [ ] 一页摘要是否包含核心信息？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Proposal Strategist |


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
 Read     确认

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
