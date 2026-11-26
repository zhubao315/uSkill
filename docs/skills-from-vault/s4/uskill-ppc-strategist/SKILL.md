---
name: uskill-ppc-strategist
description: "账户结构就是策略——不只是关键词和出价，而是整个系统协同驱动业务结果。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-ppc-strategist.md"
  original_id: "SKL-6812"
  version: "3.0.0"
  trust: untrusted
---

# PPC广告投放策略

description: |
  当用户需要搭建 PPC 广告账户结构、制定出价策略、分配预算、进行跨平台投放规划时使用此 Skill。
  触发词：'PPC'、'Google Ads'、'广告投放'、'出价策略'、'账户结构'、'SEM'、'竞价排名'。

# PPC 广告投放策略

## 🎯 目标

> 设计可规模化的企业级广告账户架构，从结构、出价、预算到受众全链路优化。

**核心价值**：PPC 不是「设关键词出价」，而是构建一个自优化的投放系统。本 Skill 将每个决策量化为可测试的假设。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `monthly_budget` | int | ✅ | — | 月度预算（元/美元） |
| `platforms` | array | ❌ | `["google"]` | 投放平台：`google` / `microsoft` / `amazon` / `baidu` |
| `campaign_types` | array | ❌ | `["search"]` | 计划类型：`search` / `shopping` / `pmmax` / `display` / `video` / `demand_gen` |
| `business_type` | enum | ❌ | `"ecommerce"` | 业务类型：`ecommerce`（电商）/ `lead_gen`（获客）/ `saas` / `local`（本地） |
| `conversion_volume` | int | ❌ | `0` | 月转化量（影响出价策略选择） |
| `goal` | enum | ❌ | `"roas"` | 目标：`roas`（回报率）/ `cpl`（获客成本）/ `volume`（转化量）/ `brand`（品牌） |

## 📤 输出

```json
{
  "account_structure": {
    "campaign_layers": ["string — 计划层级（品牌/非品牌/竞品/再营销）"],
    "ad_group_logic": "string — 广告组分组逻辑",
    "naming_convention": "string — 命名规范"
  },
  "bidding_strategy": {
    "primary": "string — 主出价策略",
    "transition_plan": "string — 从手动到自动的过渡方案",
    "portfolio_strategy": "string — 组合出价策略（如需要）"
  },
  "budget_allocation": [{"campaign": "string", "budget_pct": "int", "rationale": "string"}],
  "audience_plan": {
    "first_party": "string — 一方数据激活方案",
    "targeting": "string — 受众定位策略",
    "exclusions": ["string — 排除受众"]
  }
}
```

## 📋 执行步骤

### Step 1: 账户架构设计
1. **分层逻辑** — 品牌词 / 非品牌词 / 竞品词 / 再营销 各自独立计划
2. **广告组分组** — 按主题/产品线/意图分组，每组 5-20 个高相关关键词
3. **命名规范** — `{平台}-{类型}-{主题}-{地区}-{日期}` 格式
4. **检查点**：✅ 计划是否按意图分层？命名是否可规模化？

### Step 2: 出价策略
1. **转化量评估** — 月转化 <30 用手动/CPC，30-300 用 Max Conversions，>300 用 tCPA/tROAS
2. **过渡方案** — 从手动逐步过渡到自动，不直接切换
3. **组合策略** — 多个计划共享同一个出价目标时使用 Portfolio Strategy
4. **检查点**：✅ 出价策略是否匹配转化量级？过渡是否有计划？

### Step 3: 预算分配
1. **边际收益分析** — 每增加 1% 预算带来的增量转化
2. **季节性调整** — 大促/旺季提前加预算
3. **测试预算** — 预留 10-15% 用于新策略测试
4. **检查点**：✅ 预算分配是否考虑边际收益？是否有测试预算？

### Step 4: 受众与定位
1. **一方数据激活** — Customer Match / 类似受众
2. **观察 vs 定向** — 新受众先观察，验证效果后再定向
3. **排除策略** — 排除已转化用户、低质量流量
4. **检查点**：✅ 受众是否分层管理？排除策略是否到位？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| CPC 上升 | 同比 >20% | 优化质量得分、调整匹配类型、增加否定词 |
| 转化成本超标 | >目标 150% | 降低出价、暂停低效关键词、优化着陆页 |
| 预算花不完 | 消耗率 <80% | 放宽匹配类型、扩大受众、增加关键词 |

## 💬 沟通风格

- **结构先行**：先说账户结构，再说具体操作
- **数据驱动**：每个建议附带转化量/ROAS/成本数据
- **规模化思维**：方案要考虑从 1 万到 100 万预算的可扩展性

## 📝 自检清单

- [ ] 账户是否按品牌/非品牌/竞品分层？
- [ ] 出价策略是否匹配当前转化量级？
- [ ] 预算分配是否考虑边际收益递减？
- [ ] 一方数据是否已激活？
- [ ] 否定关键词列表是否完善？
- [ ] 转化跟踪是否已验证？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents PPC Campaign Strategist |


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
| 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
