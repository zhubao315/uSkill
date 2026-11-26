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
| **Philosophy** | Argument rigor, conceptual clarity, original insight, intellectual honesty | Ideas that reframe your thinking; arguments that survive adversarial reading | "Dense" ≠ profound; "counterintuitive" ≠ true |
| **Research** | Methodological rigor, novelty, reproducibility, significance of claims | Findings that open new questions; methods others can build on | "Published" ≠ correct; "cited" ≠ important |

### Step 2: Conduct the Multi-Layer Assessment

Evaluate the work across five universal quality layers. Each layer has specific indicators.

#### Layer 1 — Craftsmanship (技艺)
Does the maker demonstrate mastery of the medium's tools and conventions?

**Assess:**
- Are the basics done right? (grammar, syntax, alignment, consistency)
- Is there evidence of deliberate practice and refinement?
- Are conventions followed where appropriate and broken intentionally where needed?
- Does the work show "10,000 hours" of accumulated skill?

**Gold line signal**: Basics are invisible — they don't call attention to themselves. The craft serves the content.

#### Layer 2 — Originality (原创)
Does the work contribute something new — a perspective, technique, combination, or synthesis?

**Assess:**
- Does it surprise you with a novel approach, even in a familiar domain?
- Does it combine existing ideas in a way that produces new insight?
- Would removing the original element diminish the work significantly?
- Is the originality substantive (not just cosmetic novelty)?

**Gold line signal**: You think "why didn't I think of that?" — the idea feels obvious in hindsight but was not obvious before.

#### Layer 3 — Depth (深度)
Does the work engage with the full complexity of its subject?

**Assess:**
- Does it address counterarguments, edge cases, or complications?
- Does it go beyond surface-level treatment?
- Does the maker demonstrate understanding of the history and context?
- Is there evidence of wrestling with hard choices rather than defaulting to easy ones?

**Gold line signal**: The work rewards re-reading/re-examination; you notice new layers each time.

#### Layer 4 — Clarity (清晰)
Does the work communicate its intent effectively and efficiently?

**Assess:**
- Is the main point/purpose clear within the first encounter?
- Is every element in service of the whole?
- Could anything be removed without loss?
- Is the complexity appropriate — neither oversimplified nor unnecessarily ornate?

**Gold line signal**: The work feels inevitable — as if no other arrangement could serve as well.

#### Layer 5 — Coherence (整体性)
Does the work hold together as a unified whole?

**Assess:**
- Do the parts reinforce each other?
- Is there a consistent voice/tone/style throughout?
- Does the ending fulfill the promise of the beginning?
- Does the work have internal logic that guides every choice?

**Gold line signal**: The work feels like it came from a single, clear vision — even if it was created iteratively.

### Step 3: Score and Synthesize

1. **Score each layer** on a 0.0–1.0 scale
2. **Identify gold line markers** — specific elements that signal the work crosses (or approaches) the threshold
3. **Identify gaps** — specific elements where the work falls short
4. **Make the judgment call**:
   - **Crossed** (≥ 0.75 average, no layer below 0.5): The work passes the gold line
   - **Borderline** (0.60–0.74 average, or mixed signals): Close but with notable weaknesses
   - **Not crossed** (< 0.60 average, or fundamental issues): The work does not meet the standard

### Step 4: Run the Arrogance Guardrail

**This step is critical.** The gold line concept is inherently dangerous — claiming to know the standard implies you are qualified to judge. Always check:

1. **Am I the right judge?** — Do I have sufficient domain expertise to evaluate this work? If not, reduce confidence and add caveats.
2. **Am I confusing taste with quality?** — "I don't like this" ≠ "this is below the gold line." Be specific about craft-level issues, not preferences.
3. **Am I accounting for context?** — A junior developer's first project has a different gold line than a senior architect's. Constraints (time, resources, audience) matter.
4. **Am I being honest about my own position?** — As 冯唐's original statement was criticized for arrogance ("I know the gold line because I've reached it"), ensure your assessment doesn't carry unearned authority.
5. **Would I say this to the maker's face with the same confidence?** — If the assessment feels too harsh or too generous when imagined as direct feedback, recalibrate.

> ⚠️ **Red flag**: If your assessment implies "only people like me can see the gold line," you have crossed from assessment into arrogance. Step back.

### Step 5: Deliver the Assessment

Structure your output with:
1. The judgment (crossed / borderline / not crossed)
2. Confidence level (informed by your own domain expertise)
3. Specific criteria scores
4. Concrete evidence — quote or cite specific elements
5. Actionable gaps — what would elevate the work
6. The arrogance guardrail note (if applicable)

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| **Domain mismatch** — The work spans multiple domains | Assess in the primary domain; note secondary domain qualities separately |
| **Insufficient expertise** — You lack domain knowledge to judge | Set confidence to < 0.3, flag explicitly, suggest finding a domain expert |
| **Confusing popularity with quality** — Tempted to weight audience reception | Remind: "这条金线和销量没有直接正相关的关系，在某些时代，甚至负相关" (The gold line has no direct positive correlation with sales; in some eras, even a negative one) |
| **Cultural/era bias** — Standards shift across time and culture | Acknowledge the temporal context; assess within the work's intended context |
| **Assessor's own blind spots** — You may have preferences disguised as standards | Run the arrogance guardrail (Step 4) with extra rigor; seek second opinions |
| **Work is intentionally unconventional** — Breaks norms deliberately | Distinguish between "breaks rules from mastery" and "breaks rules from ignorance" — only the former can cross the gold line |

## 💡 示例

### Example 1: Code Review

**Input**: A Python data pipeline script, 200 lines

**Assessment Process**:
- **Craftsmanship (0.85)**: Clean naming, consistent style, proper error handling. Minor issue: some functions are slightly too long.
- **Originality (0.60)**: Standard pipeline pattern; one clever use of generators for memory efficiency.
- **Depth (0.75)**: Handles most edge cases; one gap in retry logic.
- **Clarity (0.90)**: Reads like prose; comments explain "why" not "what."
- **Coherence (0.80)**: Clear architecture; consistent abstractions.

**Result**: `gold_line_crossed: true` (avg: 0.78) — This code crosses the gold line. It demonstrates that the author has internalized Pythonic idioms and writes code that serves the reader, not just the machine.

### Example 2: Writing Assessment

**Input**: A blog post about distributed systems

**Assessment Process**:
- **Craftsmanship (0.70)**: Good grammar, but some paragraphs are dense. Pacing could improve.
- **Originality (0.85)**: Novel analogy connecting distributed consensus to social contracts.
- **Depth (0.90)**: Deep engagement with CAP theorem nuances; acknowledges trade-offs honestly.
- **Clarity (0.65)**: The core insight is buried in paragraph 3; needs a clearer thesis upfront.
- **Coherence (0.70)**: Strong middle section, but the conclusion feels tacked on.

**Result**: `gold_line_crossed: "borderline"` (avg: 0.76, but clarity below threshold) — The depth and originality approach the gold line, but structural issues prevent the work from fully crossing it. Recommendation: Lead with the social contract analogy; rewrite the conclusion to fulfill it.

### Example 3: Design Evaluation

**Input**: A mobile app onboarding flow (5 screens)

**Assessment Process**:
- **Craftsmanship (0.80)**: Consistent visual system; proper spacing and alignment.
- **Originality (0.50)**: Standard swipe-through pattern; nothing novel.
- **Depth (0.70)**: Considers edge cases (accessibility, slow networks); but assumes single-language users.
- **Clarity (0.90)**: Every screen has one clear action; no ambiguity.
- **Coherence (0.85)**: Smooth progression; visual language consistent throughout.

**Result**: `gold_line_crossed: true` (avg: 0.75) — The onboarding crosses the gold line through clarity and coherence. While not original, the execution demonstrates mastery: every choice serves the user's journey. The gold line doesn't require novelty — it requires that everything works at a high level together.

## 📚 参考

- **来源**: [[金线]] — 冯唐原信及网友讨论
- **作者**: [[冯唐]] (Feng Tang) — 70后作家，原文写给[[《1988：我想和这个世界谈谈》-韩寒]]的公开信
- **核心引用**: "文学的标准的确很难量化，但是文学的确有一条金线，一部作品达到了就是达到了，没达到就是没达到，对于门外人，若隐若现，对于明眼人，一清二楚，洞若观火。"
- **相关技能**: cognitive-first-principles-thinking, cognitive-metacognition-awareness
- **延伸阅读**: 班门弄斧 — 金线概念被网友用来讽刺"专家傲慢"的场景

## 🧠 元认知备注

The Gold Line concept is a double-edged sword:
- **Useful**: It affirms that quality is real even when hard to measure — combating pure relativism ("all opinions are equal") and popularity-driven assessment ("if it sells, it's good")
- **Dangerous**: It can become a weapon of gatekeeping and intellectual elitism — "I see the gold line and you don't" is often a claim of unearned authority

The healthiest application: Use the gold line as an **internal compass** for your own work (aspiration, not judgment), and as a **structured heuristic** for evaluating others' work (with humility, specificity, and the arrogance guardrail always active).

> "文章千古事，得失寸心知" — The matter of writing is for eternity; its gains and losses are known in the heart. 杜甫 (Du Fu)


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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
- 不在用户未确认时执行高风险操作
- 不伪装成功（失败就上报）

---

## 🔒 Gated Workflow `[v3新增]`

> 来源：addyosmani 的门禁 + claude-skills 的 Agent Harness

```
DISCUSS → PLAN → EXECUTE → VERIFY → CLOSE
   ↓         ↓        ↓          ↓        ↓
 Context   方案     执行      证据     Done/
 Read     确认     任务      检查    Escalate
```

### Phase 1: DISCUSS
- [ ] 输出 Context Read 一行判断
- [ ] 确认用户意图
- [ ] 确认约束条件

### Phase 2: PLAN
- [ ] 制定执行方案
- [ ] 确认资源可用
- [ ] 人工审批计划

### Phase 3: EXECUTE
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功


**相关概念**：[[金线质量标准]] · [[质量属性与架构权衡]]

---



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功
