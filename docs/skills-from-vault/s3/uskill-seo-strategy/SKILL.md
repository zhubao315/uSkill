---
name: uskill-seo-strategy
description: "搜索引擎不欠你流量，但你可以赢得它的信任。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-seo-strategy.md"
  original_id: "SKL-5708"
  version: "3.0.0"
  trust: untrusted
---

# SEO优化策略

description: |
  当用户需要优化网站/博客搜索排名、进行关键词研究、提升自然搜索流量时使用此 Skill。
  触发词：'SEO'、'搜索引擎优化'、'关键词排名'、'搜索流量'、'SEO优化'。

# [[SEO优化策略]]

## 🎯 目标

> 建立从关键词研究、内容优化到技术 SEO 的完整优化体系，持续提升自然搜索流量。

**核心价值**：SEO 是成本最低、效果最持久的流量来源，本 Skill 将每个环节标准化为可执行的动作清单。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `site_url` | string | ✅ | — | 待优化网站/博客 URL |
| `target_keywords` | array | ❌ | — | 目标关键词列表（如有） |
| `niche` | string | ❌ | — | 所属领域 |
| `audit_type` | enum | ❌ | `"full"` | 审计类型：`full`（全量）/ `content`（仅内容）/ `technical`（仅技术） |
| `language` | string | ❌ | `"zh"` | 内容语言：`zh` / `en` / `bilingual` |

## 📤 输出

```json
{
  "keyword_research": [{"keyword": "string", "volume": "int", "difficulty": "int", "intent": "string"}],
  "content_plan": [{"topic": "string", "target_kw": "string", "type": "string", "word_count": "int"}],
  "technical_audit": {"issues": ["string"], "fixes": ["string"], "priority": "string"},
  "on_page_checklist": ["string — 每篇内容的 SEO 优化清单"],
  "backlink_strategy": "string — 外链建设计划"
}
```

## 📋 执行步骤

### Step 1: 关键词研究
1. **种子词扩展** — 用 Google/百度搜索下拉词、相关搜索扩展关键词
2. **搜索意图分类** — 信息型（怎么/是什么）、导航型（品牌名）、交易型（购买/价格）
3. **竞争度评估** — 搜索量 / 竞争度 = 机会值，优先选高搜索低竞争的词
4. **检查点**：✅ 关键词是否有搜索量？竞争度是否可接受？

### Step 2: 内容优化
1. **标题优化** — 标题含核心关键词，长度 50-60 字符
2. **Meta Description** — 含关键词，150 字符以内，有 CTA
3. **正文布局** — H1 含关键词，前 100 字出现关键词，自然分布
4. **内链建设** — 每篇文章链接 2-3 篇相关文章
5. **检查点**：✅ 标题/Meta/正文是否都包含关键词？内链是否到位？

### Step 3: 技术 SEO
1. **页面速度** — Core Web Vitals 达标（LCP <2.5s, FID <100ms, CLS <0.1）
2. **移动适配** — 响应式设计，移动端体验良好
3. **结构化数据** — 添加 Article/BreadcrumbList/FAQ 等 Schema
4. **XML Sitemap** — 提交到搜索引擎，确保所有重要页面被收录
5. **检查点**：✅ 页面速度是否达标？是否移动端友好？

### Step 4: 外链建设
1. **内容营销** — 高质量内容自然吸引外链
2. **客座博客** — 在行业网站发布客座文章获取链接
3. **资源页链接** — 找到行业资源汇总页，申请收录
4. **检查点**：✅ 外链来源是否权威？锚文本是否多样化？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 排名下降 | 核心词掉出前 20 | 检查是否被惩罚、更新内容、增加外链 |
| 收录率低 | <70% | 检查 sitemap、提升内容质量、增加内链 |
| 流量瓶颈 | 连续 3 月无增长 | 扩展新关键词、优化现有内容、增加内容量 |

## 💬 沟通风格

- **数据驱动**：每个建议附带搜索量/竞争度数据
- **实操导向**：不说"要提升用户体验"，说"把 LCP 从 3.2s 降到 2.1s"
- **长期主义**：SEO 是马拉松，不追求短期排名跳跃

## 📝 自检清单

- [ ] 关键词是否基于搜索量和竞争度选择？
- [ ] 标题是否包含核心关键词？
- [ ] Meta Description 是否有 CTA？
- [ ] 正文前 100 字是否出现关键词？
- [ ] Core Web Vitals 是否达标？
- [ ] 是否提交了 XML Sitemap？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents SEO Specialist + Baidu SEO Specialist |


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

### ⚠️ Ask fir

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
