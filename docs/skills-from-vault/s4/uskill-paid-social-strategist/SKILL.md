---
name: uskill-paid-social-strategist
description: "社交媒体广告的本质是在对的时间把对的内容推给对的人。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-paid-social-strategist.md"
  original_id: "SKL-6003"
  version: "3.0.0"
  trust: untrusted
---

# 社交媒体广告投放

description: |
  当用户需要在 Meta/抖音/小红书/TikTok 等平台投放付费广告、设计受众策略、优化转化成本时使用此 Skill。
  触发词：'社交媒体广告'、'Meta广告'、'Facebook广告'、'抖音广告'、'信息流广告'、'paid social'。

# 社交媒体广告投放

## 🎯 目标

> 构建以转化目标为核心的社交媒体广告体系，从受众、素材到投放全链路优化。

**核心价值**：社交媒体广告与搜索广告的根本区别是「用户没在找你」。本 Skill 将策略从「搜索意图」转向「兴趣激发」。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `platforms` | array | ✅ | — | 平台：`meta` / `douyin` / `xiaohongshu` / `tiktok` / `wechat` / `weibo` |
| `monthly_budget` | int | ✅ | — | 月度预算 |
| `objective` | enum | ❌ | `"conversion"` | 目标：`awareness`（曝光）/ `traffic`（引流）/ `engagement`（互动）/ `conversion`（转化）/ `app`（应用安装） |
| `product_service` | string | ✅ | — | 推广产品/服务 |
| `target_audience` | string | ❌ | — | 目标受众描述 |
| `creative_format` | enum | ❌ | `"video"` | 素材格式：`image` / `video` / `carousel` / `collection` |

## 📤 输出

```json
{
  "campaign_structure": {
    "levels": "string — 投放层级结构",
    "budget_split": "string — 预算分配逻辑",
    "bidding": "string — 出价策略"
  },
  "audience_plan": {
    "core_audiences": ["string — 核心受众定位"],
    "lookalike": "string — 相似受众方案",
    "retargeting": "string — 再营销受众",
    "exclusions": ["string — 排除受众"]
  },
  "creative_brief": {
    "hook_options": ["string — 开头钩子"],
    "body": "string — 内容主体",
    "cta": "string — 行动号召",
    "format_specs": "string — 素材规格"
  },
  "optimization_plan": {
    "daily_actions": ["string — 每日优化动作"],
    "scaling_trigger": "string — 放量条件",
    "kill_criteria": "string — 停止条件"
  }
}
```

## 📋 执行步骤

### Step 1: 受众策略
1. **冷受众** — 基于兴趣/行为/人口属性定位核心受众
2. **相似受众** — 用已转化用户创建 1%-10% Lookalike
3. **再营销** — 访问过网站/加购未付款/互动过内容的用户
4. **排除** — 已转化用户、员工、低质量流量
5. **检查点**：✅ 受众规模是否在 10-500 万之间？冷/热受众是否分层？

### Step 2: 素材设计
1. **平台适配** — 不同平台的内容消费习惯不同（Meta 偏图文、抖音偏短视频）
2. **钩子设计** — 前 3 秒决定用户是否继续看
3. **信息简洁** — 一条广告只传达一个核心信息
4. **CTA 明确** — 告诉用户下一步做什么
5. **检查点**：✅ 素材是否适配平台？前 3 秒是否有钩子？

### Step 3: 投放与出价
1. **出价策略** — 转化量充足用最低成本，不足用出价上限
2. **预算分配** — 70% 稳定计划 + 20% 测试计划 + 10% 再营销
3. **频次控制** — 同一用户看到同一广告 ≤3 次/周
4. **检查点**：✅ 出价策略是否匹配数据量级？频次是否控制？

### Step 4: 优化与放量
1. **每日监控** — CTR/CPA/ROAS 三个核心指标
2. **素材轮换** — 每 2-3 周更新素材，防止疲劳
3. **放量条件** — CPA 稳定低于目标 3 天以上才放量
4. **停止条件** — CPA 连续 3 天超目标 150% 则暂停
5. **检查点**：✅ 监控是否到位？放量/停止条件是否明确？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| CTR 低 | <1% | 优化素材钩子、调整受众定位 |
| CPA 飙升 | >目标 200% | 暂停计划、检查素材疲劳、调整出价 |
| 频次过高 | >4 次/周 | 扩大受众范围或更换素材 |

## 💬 沟通风格

- **受众思维**：先说「谁会看到」，再说「看到什么」
- **平台意识**：不同平台用不同语言，不一套素材打天下
- **数据纪律**：放量有门槛，停止有标准

## 📝 自检清单

- [ ] 受众规模是否在合理范围？
- [ ] 素材是否适配目标平台？
- [ ] 频次是否控制在 ≤3 次/周？
- [ ] 冷/热/再营销受众是否分层？
- [ ] 放量/停止条件是否明确？
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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Paid Social Strategist |


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
| ""用户说想要这个"" | "用户

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
