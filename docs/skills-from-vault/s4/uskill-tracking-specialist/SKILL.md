---
name: uskill-tracking-specialist
description: "如果没被正确追踪，它就没发生过。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-tracking-specialist.md"
  original_id: "SKL-6007"
  version: "3.0.0"
  trust: untrusted
---

# 转化追踪与归因

description: |
  当用户需要配置转化追踪、搭建 GTM 容器、实施 GA4 事件、设置归因模型、处理隐私合规时使用此 Skill。
  触发词：'转化追踪'、'GTM'、'GA4'、'归因模型'、'增强转化'、'事件追踪'、'conversion tracking'。

# [[转化追踪与归因]]

## 🎯 目标

> 构建精确的转化追踪基础设施，确保每一分广告支出都可衡量、可归因、可优化。

**核心价值**：追踪错误比没有追踪更危险——错误的转化数据会误导出价算法，让预算流向错误的地方。本 Skill 将追踪架构标准化为一次搭建、持续验证的流程。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `tracking_scope` | enum | ✅ | — | 范围：`gtm`（GTM 容器）/ `ga4`（GA4 事件）/ `ads_conversion`（广告转化）/ `server_side`（服务端）/ `full`（全套） |
| `platforms` | array | ❌ | `["google"]` | 追踪平台：`google` / `meta` / `tiktok` / `linkedin` / `multi` |
| `business_type` | enum | ❌ | `"ecommerce"` | 业务类型：`ecommerce`（电商事件链）/ `lead_gen`（表单提交）/ `saas`（注册/付费）/ `app`（应用事件） |
| `privacy_mode` | enum | ❌ | `"consent_mode"` | 隐私模式：`none` / `consent_mode` / `server_side` / `both` |

## 📤 输出

```json
{
  "gtm_architecture": {
    "container_config": "string — GTM 容器配置",
    "tags": ["string — 要部署的标签列表"],
    "triggers": ["string — 触发器配置"],
    "variables": ["string — 自定义变量"]
  },
  "ga4_event_plan": {
    "events": [{"event_name": "string", "parameters": ["string"], "trigger": "string"}],
    "ecommerce_events": ["string — 电商事件链（view_item → add_to_cart → purchase）"],
    "custom_dimensions": ["string — 自定义维度"]
  },
  "ads_conversion_plan": {
    "platforms": [{"name": "string", "actions": ["string"], "attribution": "string"}],
    "enhanced_conversions": "string — 增强转化配置",
    "offline_import": "string — 线下转化导入方案（如需要）"
  },
  "privacy_compliance": {
    "consent_mode": "string — Consent Mode v2 配置",
    "data_retention": "string — 数据保留策略",
    "cookie_policy": "string — Cookie 策略"
  }
}
```

## 📋 执行步骤

### Step 1: GTM 容器搭建
1. **工作区管理** — 每个优化方向使用独立工作区
2. **标签规划** — GA4 标签 + 广告平台标签 + 自定义事件标签
3. **触发器设计** — 页面浏览/点击/表单提交/自定义触发器
4. **变量配置** — dataLayer 变量、Cookie 变量、自定义 JavaScript 变量
5. **检查点**：✅ 标签是否完整？触发器是否正确？变量是否已配置？

### Step 2: GA4 事件实施
1. **事件分类** — 基础事件（页面浏览/点击）+ 业务事件（加购/提交）+ 自定义事件
2. **电商事件链** — view_item → add_to_cart → begin_checkout → purchase
3. **自定义维度** — 用户属性 + 业务属性
4. **检查点**：✅ 电商事件链是否完整？自定义维度是否注册？

### Step 3: 广告转化配置
1. **转化动作** — 区分主要转化和辅助转化
2. **增强转化** — 配置 PII 哈希匹配（邮箱/手机）
3. **归因模型** — 数据驱动归因或位置归因
4. **线下转化导入** — 如有线下成交，通过 API 导入
5. **检查点**：✅ 转化动作层级是否区分？增强转化是否启用？

### Step 4: 验证与隐私合规
1. **交叉验证** — 平台转化数 vs GA4 转化数，差异 <5%
2. **Tag Assistant** — 逐标签验证触发和数据传递
3. **GA4 DebugView** — 实时验证事件参数
4. **Consent Mode** — 配置 Consent Mode v2，模拟未同意场景
5. **检查点**：✅ 数据差异是否 <5%？隐私合规是否到位？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 数据差异大 | 平台 vs GA4 差异 >10% | 检查重复计数、时区差异、归因窗口 |
| 增强转化匹配率低 | <80% | 检查 PII 哈希格式、字段完整性 |
| 转化延迟 | 线下导入延迟 >24h | 检查 API 连接、GCLID 匹配率 |

## 💬 沟通风格

- **精确到代码**：不只说「要追踪」，说「用什么标签、什么触发器、什么变量」
- **验证驱动**：每个配置都必须验证，不假设「配了就对了」
- **隐私优先**：在效果和合规之间取平衡，合规是底线

## 📝 自检清单

- [ ] GTM 容器是否使用了工作区管理？
- [ ] GA4 电商事件链是否完整？
- [ ] 转化动作是否区分了主要/辅助？
- [ ] 增强转化是否已启用？
- [ ] 平台数据 vs GA4 差异是否 <5%？
- [ ] Consent Mode v2 是否已配置？
- [ ] Tag Assistant 验证是否通过？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Tracking & Measurement Specialist |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务]

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
