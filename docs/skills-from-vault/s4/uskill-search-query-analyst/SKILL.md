---
name: uskill-search-query-analyst
description: "搜索词报告是最诚实的用户意图数据——它告诉你用户真正在搜什么。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-search-query-analyst.md"
  original_id: "SKL-6004"
  version: "3.0.0"
  trust: untrusted
---

# 搜索词分析与关键词策略

description: |
  当用户需要分析搜索词报告、构建关键词策略、管理否定关键词、优化质量得分时使用此 Skill。
  触发词：'搜索词'、'关键词'、'否定关键词'、'质量得分'、'匹配类型'、'搜索词报告'。

# 搜索词分析与关键词策略

## 🎯 目标

> 基于搜索词报告数据持续优化关键词策略，确保每一分广告费都花在高意图流量上。

**核心价值**：搜索词报告是 PPC 中最被低估的数据源——它直接展示用户的真实搜索行为。本 Skill 将搜索词分析标准化为每周必做的优化动作。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `search_terms_data` | string | ✅ | — | 搜索词报告（CSV/截图/手动输入） |
| `campaign_goals` | enum | ❌ | `"conversion"` | 目标：`conversion` / `traffic` / `brand` |
| `match_type_strategy` | enum | ❌ | `"tiered"` | 匹配类型策略：`broad`（广泛）/ `phrase`（短语）/ `exact`（精确）/ `tiered`（分层） |
| `language` | string | ❌ | `"zh"` | 搜索语言 |

## 📤 输出

```json
{
  "search_term_analysis": {
    "high_intent": [{"term": "string", "volume": "string", "action": "string"}],
    "low_intent": [{"term": "string", "reason": "string", "action": "string"}],
    "irrelevant": ["string — 需否定的搜索词"]
  },
  "negative_keywords": {
    "account_level": ["string — 账户级否定词"],
    "campaign_level": {"campaign_name": ["string"]},
    "strategy": "string — 否定词管理策略"
  },
  "match_type_plan": [{"keyword": "string", "recommended_match": "string", "reason": "string"}],
  "quality_score_audit": {
    "low_score_keywords": [{"keyword": "string", "score": "int", "breakdown": "string"}],
    "improvement_actions": ["string"]
  }
}
```

## 📋 执行步骤

### Step 1: 搜索词扫描
1. **数据获取** — 导出最近 30 天搜索词报告
2. **意图分类** — 将每个搜索词分为高意图/低意图/不相关
3. **覆盖率检查** — 搜索词是否都被现有关键词覆盖
4. **检查点**：✅ 搜索词报告是否完整？意图分类是否准确？

### Step 2: 否定关键词管理
1. **即时否定** — 明确不相关的搜索词立即加入否定列表
2. **模式否定** — 使用否定短语否定一类搜索词（如「免费」「下载」）
3. **账户级 vs 计划级** — 通用否定词放账户级，计划特定放计划级
4. **检查点**：✅ 不相关搜索词是否已否定？否定词层级是否正确？

### Step 3: 匹配类型优化
1. **精确匹配** — 高转化搜索词升级为精确匹配
2. **短语匹配** — 中等意图词保持短语匹配
3. **广泛匹配** — 配合智能出价测试新流量
4. **检查点**：✅ 匹配类型是否按意图分层？高转化词是否已锁定？

### Step 4: 质量得分优化
1. **质量得分审计** — 检查每个关键词的质量得分分项（相关性/着陆页体验/预期 CTR）
2. **低分修复** — 针对性优化低分项
3. **检查点**：✅ 低分关键词是否有优化方案？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 不相关流量占比高 | >20% | 紧急添加否定词、收紧匹配类型 |
| 质量得分骤降 | 平均 <5 | 检查着陆页、更新广告文案 |
| 搜索词无覆盖 | 新搜索词无匹配关键词 | 添加新关键词或用广泛匹配捕获 |

## 💬 沟通风格

- **周度节奏**：搜索词分析是每周必做的纪律性工作
- **意图导向**：每个搜索词都回答「这个用户的意图是什么」
- **否定优先**：先排除错误的，再优化正确的

## 📝 自检清单

- [ ] 是否每周分析搜索词报告？
- [ ] 不相关搜索词是否已否定？
- [ ] 否定词是否区分了账户级和计划级？
- [ ] 高转化词是否已升级为精确匹配？
- [ ] 质量得分低的关键词是否有优化方案？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Search Query Analyst |


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

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
