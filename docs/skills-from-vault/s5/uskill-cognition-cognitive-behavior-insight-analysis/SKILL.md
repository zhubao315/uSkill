---
name: uskill-cognition-cognitive-behavior-insight-analysis
description: "让cognitive behavior insight analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-behavior-insight-analysis.md"
  original_id: "SKL-6852"
  version: "3.0.0"
  trust: untrusted
---

# cognitive behavior insight analysis

# AI-Powered Behavior Insight Analysis (AI赋能的人性洞察与行为分析)

## 🎯 目标

> 在非临床场景下，通过AI增强的五步循环流程，对个人、团队或用户群体的行为与心理模式进行系统化分析，产出数据驱动的洞察报告与可执行行动建议。

**适用场景：**
- **用户行为洞察** — 分析产品数据与访谈，找出用户流失的深层心理原因
- **团队协作诊断** — 通过访谈和观察，诊断沟通不畅或士气低落的系统性原因
- **个人决策复盘** — 复盘重大决策中的认知偏差（如确认偏误、损失厌恶）

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `analysis_goal` | string | ✅ | 核心分析问题，须具体、可回答 |
| `scenario` | enum | ✅ | 分析场景：`product` / `team` / `personal` |
| `qualitative_data` | string | ✅ | 定性数据：访谈文稿、会议记录、日记等（已匿名化） |
| `quantitative_data` | string | ❌ | 定量数据：行为日志、使用时长、互动数据等（CSV格式） |
| `psychology_framework` | enum | ❌ | 指定心理学框架：`fogg_bmap` / `maslow` / `dual_process` / `tuckman` / `cognitive_distortion`，默认自动匹配 |
| `output_style` | enum | ❌ | 报告风格：`concise` / `detailed`，默认 `concise` |

## 📤 输出

```json
{
  "insight_report": {
    "core_question": "string — 分析目标",
    "data_patterns": {
      "top_themes": ["string — 高频主题/痛点/期望"],
      "sentiment": "string — 整体情感倾向：positive/neutral/negative",
      "counterintuitive_findings": ["string — 反直觉发现"]
    },
    "psychology_interpretation": {
      "framework_used": "string — 使用的心理学框架",
      "behavior_mechanism": "string — 行为背后的心理机制解释",
      "hypotheses": ["string — 待验证假设"]
    },
    "actionable_recommendations": [
      {
        "action": "string — 具体做什么",
        "rationale": "string — 为什么做",
        "expected_outcome": "string — 预期效果",
        "validation_metric": "string — 验证指标",
        "validation_method": "string — 验证方法"
      }
    ]
  }
}
```

## 📋 执行步骤

### 第一步：目标定义与数据源确定

1. **明确分析目标** — 将 `analysis_goal` 转化为一个具体、可回答的核心问题。产品场景示例："核心用户最主要的行为动机是什么？"；团队场景示例："远程协作中的主要沟通瓶颈在哪里？"；个人场景示例："投资决策中最容易受到哪些认知偏误影响？"
2. **确定数据来源** — 根据目标确认需要的定性数据（访谈文稿、问卷、会议记录、日记）和定量数据（行为日志、使用时长、互动数据）。确保至少有两种数据来源。

### 第二步：多维数据收集与整理

3. **数据匿名化处理** — 对所有 `qualitative_data` 和 `quantitative_data` 进行严格的匿名化处理，移除所有个人身份信息。
4. **AI辅助整理** — 对访谈录音等非结构化数据进行转录和初步摘要，整理为便于分析的文本格式。确保数据已整理为 `.txt` 或 `.csv` 格式。

### 第三步：AI辅助模式识别

5. **定性数据分析** — 使用以下提示词对访谈文稿进行主题建模与情感分析：

```
你是一位资深的用户体验研究员。我将提供 {{number}} 份访谈的匿名文稿。请你：
1. 使用主题建模，识别出被提及次数最多的 Top 5 痛点和 Top 5 期望
2. 对整体文稿进行情感分析，判断主流情绪是积极、中立还是消极
3. 引用原文，总结出 2-3 个最有趣或最反直觉的观点
文稿如下：{{qualitative_data}}
```

6. **定量数据分析** — 对行为数据进行探索性分析（EDA），包括用户分群（Clustering）、行为序列分析，寻找异常模式或群体特征。

### 第四步：心理学框架解读

7. **选择解读框架** — 根据 `scenario` 和 `psychology_framework` 选择理论框架：
   - `product` → 福格行为模型 B=MAP、马斯洛需求层次、用户心智模型
   - `team` → 塔克曼团队发展阶段、Lencioni 团队协作五大障碍
   - `personal` → 卡尼曼双系统理论、CBT 认知扭曲模型

8. **深度解读** — 使用以下提示词将数据模式与心理学框架结合：

```
你是一位 {{psychology_school}} 专家。我发现了一个行为模式："{{data_pattern}}"。请你运用 {{psychology_theory}} 来解释这个模式背后可能的心理机制，并提出 2-3 个待验证的假设。
```

9. **人工提炼与升华** — 基于AI的初步解读，结合专业知识，提炼出超越数据表面、触及深层动机的洞察。AI提供素材，人来赋予智慧。

### 第五步：行动建议与验证方案

10. **生成行动建议** — 使用以下提示词将洞察转化为可执行建议：

```
你是一位经验丰富的产品总监/组织发展顾问。基于以下核心洞察："{{core_insight}}"，请为我头脑风暴出 3-5 个具体的、可执行的行动建议。每个建议需说明"做什么"、"为什么做"以及"预期的效果"。
```

11. **设计验证方案** — 为每个关键建议设计可衡量的验证指标和验证方法（如A/B测试、前后对比），确保可在一定周期内判断有效性。
12. **汇总报告** — 整合以上所有步骤的输出，生成结构化的《人性洞察与行为分析报告》。

## ⚠️ 异常处理

| 异常场景 | 处理方案 |
|----------|---------|
| 输入数据未匿名化 | 拒绝执行，返回 `ERROR_PRIVACY_VIOLATION`，要求匿名化后重新提交 |
| 定性数据过少（< 3 条） | 返回警告 `WARN_INSUFFICIENT_DATA`，建议补充数据或降低分析深度 |
| AI识别主题与预期严重偏离 | 提示人工复核原始数据，检查数据质量或分析目标是否清晰 |
| 定量数据缺失 | 仅基于定性数据执行，在报告中标注 `QUALITATIVE_ONLY` 限制说明 |
| 心理学框架不适用场景 | 自动推荐最匹配的框架，返回 `WARN_FRAMEWORK_MISMATCH` 并说明原因 |
| 生成建议过于笼统 | 要求AI基于具体场景细化，增加"谁做、何时做、做到什么程度"约束 |

## ✅ 自检清单

- [ ] 分析目标是否是一个具体、可回答的问题（非模糊表述）
- [ ] 输入数据已完全匿名化，无个人身份信息泄露
- [ ] 报告包含至少 2 种数据来源的交叉分析
- [ ] 心理学框架选择与分析场景匹配
- [ ] 洞察解读超越数据表面，触及行为背后的动机或原因
- [ ] 每个行动建议包含"做什么"、"为什么"、"预期效果"三项
- [ ] 验证方案可衡量、有明确周期和判断标准
- [ ] 输出 JSON 结构符合定义的 schema


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
- [

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
