---
name: uskill-programmatic-buyer
description: "程序化不是黑盒——理解拍卖机制才能控制成本。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-programmatic-buyer.md"
  original_id: "SKL-6006"
  version: "3.0.0"
  trust: untrusted
---

# 程序化广告投放

description: |
  当用户需要进行[[程序化广告投放]]、管理 DSP、优化展示广告效果、进行品牌安全防护时使用此 Skill。
  触发词：'程序化广告'、'DSP'、'RTB'、'展示广告'、'programmatic'、'品牌安全'。

# 程序化广告投放

## 🎯 目标

> 在开放的程序化生态中控制成本、确保品牌安全、最大化可见曝光。

**核心价值**：程序化广告的水很深——虚假流量、品牌安全、可见性问题随时在消耗预算。本 Skill 将每个环节的风控前置。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `campaign_goal` | enum | ✅ | — | 目标：`awareness`（曝光）/ `consideration`（考虑）/ `conversion`（转化）/ `retargeting`（再营销） |
| `monthly_budget` | int | ✅ | — | 月度预算 |
| `dsp` | enum | ❌ | `"dv360"` | DSP：`dv360` / `the_trade_desk` / `amazon_dsp` / `others` |
| `inventory_type` | enum | ❌ | `"open"` | 库存类型：`open`（公开竞价）/ `preferred`（优先交易）/ `private`（私有市场）/ `programmatic_guaranteed`（程序化保证） |
| `brand_safety_level` | enum | ❌ | `"strict"` | 品牌安全：`strict` / `moderate` / `relaxed` |

## 📤 输出

```json
{
  "campaign_config": {
    "targeting": "string — 定向策略",
    "bidding": "string — 竞价策略",
    "frequency_cap": "string — 频次上限",
    "brand_safety": "string — 品牌安全配置"
  },
  "inventory_strategy": {
    "preferred_publishers": ["string — 优先投放媒体"],
    "blocklist": ["string — 黑名单"],
    "viewability_target": "int — 可见性目标 (%)"
  },
  "anti_fraud_config": {
    "viewability_filter": "string — 可见性过滤规则",
    "bot_detection": "string — 反机器人检测",
    "ads_txt": "boolean — 是否要求 ads.txt 验证"
  },
  "optimization_plan": ["string — 优化动作"]
}
```

## 📋 执行步骤

### Step 1: 定向与出价
1. **受众定向** — 人群/兴趣/上下文/再营销分层
2. **上下文定向** — 投放页面内容匹配（关键词/话题/类别）
3. **出价策略** — 品牌曝光用 CPM，效果用 CPC/CPA
4. **检查点**：✅ 定向是否精准？出价策略是否匹配 KPI？

### Step 2: 品牌安全
1. **白名单** — 优先投放高质量媒体
2. **黑名单** — 排除低质量/争议性内容
3. **第三方验证** — 接入 IAS/DoubleVerify/MOAT 验证
4. **检查点**：✅ 品牌安全配置是否到位？是否有第三方验证？

### Step 3: 反欺诈与可见性
1. **ads.txt 验证** — 只投放 ads.txt 授权的媒体
2. **可见性过滤** — 只计入可见曝光（50% 像素 + 1 秒）
3. **机器人过滤** — 过滤非人类流量
4. **检查点**：✅ 反欺诈是否启用？可见性目标是否设定？

### Step 4: 优化与报告
1. **媒体优化** — 按媒体维度分析效果，调整投放比例
2. **创意轮换** — 防止素材疲劳
3. **频次控制** — 同一用户 ≤3 次/天
4. **检查点**：✅ 媒体效果是否分析？频次是否控制？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 虚假流量 | 机器人占比 >10% | 启用更严格的反欺诈过滤 |
| 可见率低 | <50% | 调整媒体组合，增加优质媒体占比 |
| 品牌安全事件 | 出现在争议内容旁 | 立即暂停并更新黑名单 |

## 💬 沟通风格

- **风控优先**：先说品牌安全和反欺诈，再说效果优化
- **透明化**：程序化不是黑盒，每个决定都要可解释
- **数据验证**：不只看平台报告数据，用第三方验证

## 📝 自检清单

- [ ] 品牌安全白名单/黑名单是否配置？
- [ ] ads.txt 验证是否启用？
- [ ] 可见性过滤是否设置？
- [ ] 频次上限是否合理？
- [ ] 第三方验证是否接入？
- [ ] 媒体效果是否定期分析？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Programmatic Buyer |


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


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
