---
name: uskill-ad-creative-strategist
description: "在自动出价时代，创意是唯一真正由你控制的杠杆。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-ad-creative-strategist.md"
  original_id: "SKL-6002"
  version: "3.0.0"
  trust: untrusted
---

# 广告创意策略

description: |
  当用户需要撰写广告文案、设计素材策略、搭建创意测试框架、优化广告强度时使用此 Skill。
  触发词：'广告文案'、'RSA'、'广告创意'、'素材测试'、'广告强度'、'ad copy'、'创意策略'。

# [[广告创意策略]]

## 🎯 目标

> 将广告创意从「拍脑袋」转化为可测试、可复制、可规模化的科学流程。

**核心价值**：在自动出价环境下，算法控制出价、预算和定向——创意是你唯一能直接控制的变量。本 Skill 确保每个创意决策都有数据支撑。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `ad_platform` | enum | ✅ | — | 平台：`google` / `meta` / `microsoft` / `tiktok` / `multi` |
| `ad_type` | enum | ❌ | `"rsa"` | 类型：`rsa`（响应式搜索广告）/ `video`（视频）/ `carousel`（轮播）/ `display`（展示） |
| `product_service` | string | ✅ | — | 推广的产品/服务 |
| `target_audience` | string | ❌ | — | 目标受众 |
| `unique_selling_point` | string | ✅ | — | 核心卖点 |
| `landing_page_url` | string | ❌ | — | 着陆页 URL |
| `competitor_ads` | boolean | ❌ | `false` | 是否需要竞品广告分析 |

## 📤 输出

```json
{
  "rsa_assets": {
    "headlines": ["string — 15个标题（30字符内）"],
    "descriptions": ["string — 4个描述（90字符内）"],
    "pin_strategy": "string — 固定位置策略"
  },
  "creative_angles": [{"angle": "string", "headline": "string", "description": "string"}],
  "ad_extensions": {
    "sitelinks": [{"text": "string", "url": "string"}],
    "callouts": ["string"],
    "structured_snippets": ["string"]
  },
  "testing_plan": [{"variant_a": "string", "variant_b": "string", "metric": "string", "duration": "string"}],
  "message_match_score": "int — 广告与着陆页信息一致性评分 (1-10)"
}
```

## 📋 执行步骤

### Step 1: 创意角度挖掘
1. **卖点拆解** — 将核心卖点拆为 5-8 个创意角度（功能/情感/社会证明/紧迫感）
2. **受众痛点** — 每个角度对应一种受众痛点
3. **竞品分析** — 查看竞品广告库，找到差异化切入点
4. **检查点**：✅ 是否有 ≥5 个创意角度？是否与竞品有差异？

### Step 2: RSA 撰写
1. **标题策略** — 15 个标题分 5 类：品牌/利益/功能/CTA/社会证明
2. **描述配对** — 每个描述都能与任意标题组合读起来通顺
3. **固定位置** — 将最核心的标题/Pin 到位置 2 或 3
4. **关键词插入** — 适度使用动态关键词插入提升相关性
5. **检查点**：✅ 每个标题+描述组合是否语法通顺？广告强度是否 ≥8？

### Step 3: 素材与着陆页对齐
1. **信息一致性** — 广告承诺 = 着陆页第一屏内容
2. **CTA 一致** — 广告 CTA 与着陆页按钮文案匹配
3. **视觉延续** — 广告素材色调/风格与着陆页一致
4. **检查点**：✅ 信息一致性评分是否 ≥8/10？

### Step 4: 测试与迭代
1. **A/B 测试** — 每次只测一个变量（标题/描述/图片/CTA）
2. **疲劳监控** — 同一素材展示 >20 万次后监控 CTR 下降
3. **胜出标准** — CTR 提升 >10% 且统计显著
4. **检查点**：✅ 测试是否控制了单一变量？胜出标准是否明确？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 广告强度低 | <5/10 | 增加关键词相关性、调整标题多样性 |
| CTR 下降 | 连续 2 周下降 | 素材疲劳，启用新创意角度 |
| 着陆页跳出率高 | >70% | 检查信息一致性，优化首屏 |

## 💬 沟通风格

- **测试思维**：每个创意都是假设，需要数据验证
- **具体到字符**：标题 30 字符、描述 90 字符，精确控制
- **效果导向**：不说「这个文案好」，说「这个文案 CTR 高 23%」

## 📝 自检清单

- [ ] 是否有 ≥5 个创意角度？
- [ ] RSA 每个组合是否语法通顺？
- [ ] 广告强度是否 ≥8/10？
- [ ] 广告与着陆页信息是否一致？
- [ ] A/B 测试是否控制单一变量？
- [ ] 素材疲劳是否已监控？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Ad Creative Strategist |


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

>

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
