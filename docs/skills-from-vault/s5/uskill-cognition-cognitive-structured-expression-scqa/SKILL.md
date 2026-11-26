---
name: uskill-cognition-cognitive-structured-expression-scqa
description: "让cognitive structured expression scqa变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-structured-expression-scqa.md"
  original_id: "SKL-6855"
  version: "3.0.0"
  trust: untrusted
---

# cognitive structured expression scqa

# Structured Expression with SCQA Framework

## 🎯 目标
> 运用麦肯锡 SCQA（Situation-Complication-Question-Answer）结构化表达框架，将任何观点、提案或故事组织为引人入胜、逻辑清晰的叙事结构。无论是汇报、写作、演讲还是日常沟通，都能快速构建有说服力的表达。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `core_message` | string | ✅ | 你要表达的核心观点或解决方案 |
| `context` | string | ✅ | 背景情境描述（行业、项目、受众等） |
| `expression_type` | enum | ✅ | `presentation` / `writing` / `proposal` / `pitch` / `report` |
| `audience` | string | ❌ | 目标受众（如"高管团队"、"技术同事"、"客户"），默认"通用" |
| `tone` | string | ❌ | 语气风格：`formal` / `conversational` / `urgent`，默认 formal |
| `length` | string | ❌ | 输出篇幅：`brief`（1段） / `standard`（3-5段） / `extended`（完整文章），默认 standard |
| `additional_materials` | string | ❌ | 补充素材、数据、案例等，用于丰富内容 |

## 📤 输出

```json
{
  "scqa_structure": {
    "situation": {
      "content": "string — 情景描述：大家都熟悉且认同的事实背景",
      "hooks": ["string — 引发共鸣的关键细节"]
    },
    "complication": {
      "content": "string — 冲突/挑战：与期望不符的现实问题",
      "pain_points": ["string — 核心痛点列表"]
    },
    "question": {
      "content": "string — 核心疑问：站在受众角度提出的关键问题",
      "sub_questions": ["string — 支撑性子问题"]
    },
    "answer": {
      "content": "string — 解决方案：你的核心观点和行动建议",
      "key_actions": ["string — 关键行动项"]
    }
  },
  "full_expression": "string — 完整的结构化表达文本",
  "variations": {
    "headline_version": "string — 一句话精华版",
    "elevator_pitch": "string — 30秒电梯演讲版",
    "expanded_version": "string — 完整展开版（根据 length 参数）"
  },
  "delivery_tips": {
    "opening_hook": "string — 开场吸引注意力的建议",
    "transition_phrases": ["string — S→C→Q→A 各段之间的过渡语"],
    "closing_impact": "string — 收尾增强影响力的建议"
  }
}
```

## 📋 执行步骤

### Step 1: 明确核心信息与受众
1. **锁定核心观点** — 明确你最终要传达的 Answer 是什么。SCQA 的核心是"答案先行"的金字塔原理思维
2. **分析受众** — 了解受众的背景知识、关注点和决策标准。不同受众需要不同的 S/C/Q 切入角度
3. **确定篇幅与形式** — 根据场景选择 brief / standard / extended

### Step 2: 构建 SCQA 四层结构
4. **Situation（情景）** — 用受众普遍认同、感到熟悉或容易理解的事实作为开场，建立共鸣和代入感
   - 技巧：引用行业共识、共同经历、已知数据
   - 示例："贵公司在过去三年实现了年均30%的营收增长..."
5. **Complication（冲突）** — 引出与现状不符的挑战、威胁或变化，制造张力
   - 技巧：聚焦"但是"——然而市场正在变化、竞争加剧、新法规出台...
   - 示例："然而，随着AI技术的快速渗透，传统业务模式正面临根本性挑战..."
6. **Question（疑问）** — 从受众视角，将冲突转化为他们最关心的问题
   - 技巧：用"那么"过渡，问题要精准命中受众焦虑
   - 示例："那么，如何在AI时代保持竞争优势？"
7. **Answer（回答）** — 清晰、有力地给出你的解决方案，这是全文的高潮和重点
   - 技巧：简洁有力，配合具体行动建议和预期效果
   - 示例："我们建议从三个维度构建AI能力壁垒..."

### Step 3: 多版本生成与优化
8. **生成完整表达** — 将 SCQA 四段组合为流畅的完整文本，注意段落间的过渡语
9. **生成变体版本** — 输出一句话精华版、30秒电梯版和完整展开版
10. **润色与优化** — 根据受众和语气调整措辞，确保逻辑连贯、说服力强

### Step 4: 交付技巧指导
11. **提供表达建议** — 给出开场、过渡、收尾的具体技巧
12. **检查 SCQA 完整性** — 确保四个层次都清晰且相互呼应

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `core_message` 不清晰 | 返回引导性问题清单，帮助提炼核心观点 |
| 情景（S）缺乏受众共鸣 | 建议替换为受众更熟悉的背景事实 |
| 冲突（C）力度不够 | 建议加入具体数据或案例增强紧迫感 |
| 问题（Q）与受众脱节 | 根据受众画像重新设计问题角度 |
| 答案（A）过于空泛 | 要求补充具体行动步骤和可量化目标 |
| SCQA 逻辑链断裂 | 逐段检查因果关系，补充过渡语 |

## ✅ 自检清单

- [ ] Situation 是否选用了受众普遍认同的背景事实？
- [ ] Complication 是否制造了足够的张力和紧迫感？
- [ ] Question 是否从受众角度出发，精准命中其核心关切？
- [ ] Answer 是否清晰有力，包含具体可执行的行动建议？
- [ ] S→C→Q→A 四段之间是否有自然流畅的逻辑过渡？
- [ ] 全文是否形成了"共鸣→焦虑→好奇→信服"的情绪曲线？
- [ ] 是否提供了多种版本（精华版/电梯版/完整版）？
- [ ] 核心观点是否在 Answer 中突出呈现，而非埋没在细节中？


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
| 2026-05-08 | 1.0.0 | 初始版本，从 Framework_SCQA 转化 |

---
**相关笔记**：[[学习金字塔输出驱动]] [[uSkill-cognition-贝叶斯决策框架

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
