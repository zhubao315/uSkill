---
name: uskill-productivity-review-document-checklist
description: "让productivity review document checklist变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-review-document-checklist.md"
  original_id: "SKL-5059"
  version: "3.0.0"
  trust: untrusted
---

# productivity review document checklist

# Review Document Quality Checklist

## 🎯 目标
> 基于 Why-Who-How-What 四维框架，系统化审查文档质量，确保文档目标明确、读者导向、结构清晰、内容精炼。适用于任何类型文档的快速质量评估与改进指导。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `document_text` | string | ✅ | 待审查的文档原文（纯文本或 Markdown） |
| `document_type` | enum | ❌ | `report` / `proposal` / `tutorial` / `spec` / `email`，默认 `report` |
| `audience` | string | ❌ | 目标读者描述（如"产品经理""技术团队""高管"） |
| `strictness` | enum | ❌ | `lenient`（宽松） / `normal`（标准） / `strict`（严格），默认 `normal` |

## 📤 输出

```json
{
  "score": {
    "overall": 0-100,
    "why": 0-100,
    "who": 0-100,
    "how": 0-100,
    "what": 0-100
  },
  "checklist_results": [
    {
      "dimension": "why | who | how | what",
      "item": "string — 检查项名称",
      "status": "pass | fail | warning | skip",
      "detail": "string — 具体说明",
      "location": "string — 引用文档中的相关段落或行号"
    }
  ],
  "issues": [
    {
      "severity": "critical | major | minor | suggestion",
      "dimension": "why | who | how | what",
      "description": "string — 问题描述",
      "location": "string — 位置引用",
      "fix": "string — 修复建议"
    }
  ],
  "strengths": ["string — 文档亮点"],
  "recommendations": [
    {
      "priority": "high | medium | low",
      "action": "string — 可操作的改进动作",
      "dimension": "why | who | how | what"
    }
  ]
}
```

## 📋 执行步骤

### Step 1: Why — 目标审查（权重 30%）

> 检查文档是否回答了"为什么要写这份文档"。

- **核心问题定义**: 文档是否清晰阐述要解决的核心问题或要传达的核心结论？
- **关键观点明确**: 主要论点/立场是否在前 20% 的篇幅内出现？
- **可执行建议**: 文档是否包含明确的行动建议或决策依据？（`report`/`proposal` 类必查）

评分规则: 核心问题缺失 → 该维度 ≤ 30；观点不明确 → 该维度 ≤ 60；建议缺失 → 扣 15 分。

### Step 2: Who — 读者审查（权重 25%）

> 检查文档是否以目标读者为中心。

- **读者画像**: 是否明确定义或暗示了目标读者？（若输入含 `audience` 参数则对比检查）
- **背景上下文**: 是否为读者提供了理解所需的背景信息？避免知识诅咒。
- **角色关切**: 是否覆盖了不同角色（决策者/执行者/审核者）的核心关切点？
- **术语适配**: 行话和缩写是否对目标读者合适？首次出现的术语是否有解释？

评分规则: 未识别读者 → 该维度 ≤ 25；背景信息不足 → 扣 20 分；术语未解释 → 每个扣 5 分。

### Step 3: How — 结构审查（权重 25%）

> 检查文档结构是否符合金字塔原理，便于快速获取信息。

- **金字塔原理**: 是否采用"结论先行、分层论述"的结构？
- **结论前置**: 核心结论/摘要是否在文档开头 1-2 段出现？
- **目录/导航**: 文档是否有清晰的目录或小标题体系？（> 2000 字必查）
- **逻辑链路**: 各章节之间的逻辑关系是否清晰（因果/并列/递进）？
- **篇幅均衡**: 各章节篇幅是否与重要性成正比？

评分规则: 无结构可言 → 该维度 ≤ 20；结论未前置 → 扣 25 分；缺少目录 → 扣 10 分。

### Step 4: What — 内容审查（权重 20%）

> 检查文档内容的表达质量，分五个子维度逐项评估。

| 子维度 | 检查要点 |
|--------|----------|
| **突出重点** | 关键数据/结论是否用粗体/图表/高亮突出？每段是否有中心句？ |
| **精简内容** | 是否存在冗余段落、重复表述、可删除的填充词？信息密度是否足够？ |
| **清晰表达** | 句子是否简短明确？是否存在歧义、指代不清、过度被动语态？ |
| **格式一致性** | 标题层级、列表样式、日期格式、数字格式是否全文统一？ |
| **迭代优化** | 是否有修订痕迹或待办标记？是否有"待完善""TODO"等未完成标记？ |

评分规则: 每个子维度 20 分，满分 100 → 加权后乘以 20% 计入总分。

### Step 5: 评分汇总

```
总分 = why_score × 0.30 + who_score × 0.25 + how_score × 0.25 + what_score × 0.20
```

- `strictness = strict` 时: 任何维度 < 40 → 总分上限 60
- `strictness = lenient` 时: 总分 × 1.1（上限 100），minor issues 不计入
- 评级: ≥ 85 优秀 / ≥ 70 良好 / ≥ 50 及格 / < 50 需重写

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `document_text` 为空 | 返回 `ERROR_EMPTY_INPUT`，终止执行 |
| 文档 < 100 字 | 返回 `WARNING_TOO_SHORT`，跳过 Step 3 结构审查 |
| 文档 > 50000 字 | 采样审查：首尾各 5000 字 + 中间随机 3 段 × 3000 字 |
| 非中英文文档 | 返回 `WARNING_UNSUPPORTED_LANGUAGE`，以英文分析框架尽力审查 |
| 文档含大量代码块 | 代码块不计入结构/内容审查字数，仅审查注释和文档说明部分 |

## ✅ 自检清单

- [ ] 四维审查（Why / Who / How / What）全部完成，无遗漏
- [ ] 评分权重与公式逻辑自洽：总分 = 各维度加权和
- [ ] 每个 issue 包含 `location` 字段，引用具体段落或行号
- [ ] 每个 recommendation 包含可操作的具体动作，非泛泛而谈
- [ ] 输出 JSON 结构符合上方 schema 定义
- [ ] `checklist_results` 覆盖所有维度的所有检查项
- [ ] `strictness` 参数对评分和过滤逻辑有实际影响


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



> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
