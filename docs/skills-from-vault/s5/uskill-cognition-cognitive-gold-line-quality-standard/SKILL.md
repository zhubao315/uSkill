---
name: uskill-cognition-cognitive-gold-line-quality-standard
description: "让cognitive gold line quality standard变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-gold-line-quality-standard.md"
  original_id: "SKL-5108"
  version: "3.0.0"
  trust: untrusted
---

# cognitive gold line quality standard

---
# Apply Gold Line Quality Standard

## 🎯 目标

> Assess work quality in domains where standards are hard to quantify but genuine quality distinctions exist — where "难以量化但确有境界之分" (hard to quantify but there ARE real quality levels).

The "Gold Line" (金线), coined by author 冯唐 (Feng Tang), holds that in fields like literature, philosophy, design, and code, there exists an invisible but real threshold that separates adequate work from excellent work. Like a gold thread running through all great work, this standard is:
- **Real**: It genuinely exists regardless of whether people acknowledge it
- **Subtle**: Hard to articulate precisely, yet recognizable to experienced practitioners
- **Independent of popularity**: Sales, stars, or social proof do not determine whether the line is crossed
- **Domain-specific**: The gold line manifests differently in each field but the principle is universal

This skill provides a structured framework for identifying and applying this quality standard — while guarding against the arrogance that often accompanies such claims.

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| work | string | ✅ | The work to assess (text, code, design, presentation, etc.) |
| domain | string | ✅ | The field: `literature`, `code`, `design`, `presentation`, `philosophy`, `research`, `other` |
| benchmark | string | ❌ | Reference standard or exemplar to compare against |
| humility_check | boolean | ❌ | Whether to run the arrogance guardrail (default: true) |


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位质量标准专家，擅长为认知输出建立可量化的质量评估框架。请根据以下输入执行操作：
输入：[需制定质量标准的认知输出类型或工作场景]
要求：[指定质量维度、评分粒度、适用场景]
输出格式：[Gold Line 质量标准文档，含维度定义、评分量规、检查清单和基准示例]
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改

## 📤 输出

```json
{
  "gold_line_crossed": true | false | "borderline",
  "confidence": 0.0-1.0,
  "domain": "code",
  "criteria_scores": {
    "craftsmanship": 0.85,
    "originality": 0.70,
    "depth": 0.90,
    "clarity": 0.80,
    "coherence": 0.75
  },
  "gold_line_markers": ["List of specific qualities that signal crossing the line"],
  "gaps": ["Specific areas where the work falls short"],
  "arrogance_guardrail": "Warning message if applicable",
  "summary": "Brief natural-language assessment"
}
```

## 📋 执行步骤

### Step 1: Calibrate Domain Understanding

Before assessing any work, understand what "gold line" means in the target domain.

1. **Identify the domain's core craft dimensions** — what separates competent from excellent
2. **Recall exemplars** — works that are widely recognized (by practitioners, not just popular audiences) as crossing the gold line
3. **Note the domain's unique blind spots** — where popular opinion diverges from expert quality

#### Domain Calibration Reference

| Domain | Core Craft Dimensions | Gold Line Markers | Common Illusions |
|--------|----------------------|-------------------|------------------|
| **Literature** | Language precision, emotional resonance, structural integrity, originality of vision | Sentences that stay with you; structure that feels inevitable; language that surprises yet feels right | Bestseller ≠ literary quality; "difficult" ≠ deep |
| **Code** | Correctness, readability, architectural elegance, edge-case handling, composability | Code that reads like prose; abstractions that reveal the problem's true shape; tests that illuminate intent | Lines of code ≠ productivity; "works" ≠ well-crafted |
| **Design** | Visual hierarchy, affordance clarity, aesthetic coherence, restraint, emotional tone | Design that feels inevitable; UI that disappears; choices that serve function AND beauty | "Pretty" ≠ good design; trendy ≠ timeless |
| **Presentation** | Narrative arc, signal-to-noise ratio, audience calibration, visual-text harmony | Talk that teaches something unexpected; slides that amplify rather than duplicate speech | "Engaging" ≠ informative; "polished" ≠ substantive |
| **Philosophy** | Argument rigor, conceptual clarity, origina

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
