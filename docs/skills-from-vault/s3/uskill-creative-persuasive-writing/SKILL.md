---
name: uskill-creative-persuasive-writing
description: "让说服力写作变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-persuasive-writing.md"
  original_id: "SKL-5610"
  version: "3.0.0"
  trust: untrusted
---

# 说服力写作

description: |
  当用户需要撰写提案、影响力建设、谈判准备、政策建议时使用此 Skill。
  触发词包括：'说服'、'提案'、'影响力'、'论证'、'修辞'、
  'Cialdini'、'谈判'。
  不适用于营销文案（使用文案写作）。当需要深度说服和论证时优先使用。

---

# uSkill-610: 说服力写作

## 🎯 目标

> 运用 Cialdini 六大影响力原则，构建严密的论证结构，创作有说服力的内容。

**核心价值**：说服不是操纵，而是帮助受众理解并接受正确的观点。

**适用场景**：
- 提案写作
- 影响力建设
- 谈判准备
- 政策建议
- 学术论文
- 商业计划

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `position` | `string` | ✅ | — | 需要论证的立场/观点 |
| `audience` | `string` | ✅ | — | 目标受众 |
| `context` | `string` | ✅ | — | 应用场景 |
| `evidence` | `array` | ❌ | `[]` | 已有证据/数据 |
| `style` | `enum` | ❌ | `logical` | `logical` / `emotional` / `balanced` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话说服策略建议",
  "persuasion_id": "PRSU-YYYY-MMDD-NNN",

  "influence_principles": {
    "reciprocity": "string",
    "commitment": "string",
    "social_proof": "string",
    "authority": "string",
    "liking": "string",
    "scarcity": "string"
  },

  "argument_structure": {
    "thesis": "string",
    "premises": ["string"],
    "evidence": ["string"],
    "counterarguments": ["string"],
    "rebuttals": ["string"],
    "conclusion": "string"
  },

  "rhetoric_techniques": [
    {
      "technique": "string",
      "description": "string",
      "application": "string"
    }
  ],

  "logical_framework": {
    "type": "string",
    "structure": "string",
    "flow": ["string"]
  },

  "psychological_hooks": {
    "emotional_appeals": ["string"],
    "cognitive_biases": ["string"],
    "framing_strategies": ["string"]
  },

  "delivery_recommendations": {
    "tone": "string",
    "pacing": "string",
    "emphasis": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 影响力原则分析

- **输入**：`position` + `audience` + `context`
- **动作**：
  1. 分析受众心理
  2. 选择适合的影响力原则
  3. 设计应用策略
- **输出**：`influence_principles`
- **Cialdini 六大原则**：

| 原则 | 原理 | 应用方法 |
|------|------|----------|
| 互惠 | 给予后获得 | 提供价值后再请求 |
| 承诺一致 | 言行一致 | 获取小承诺 |
| 社会认同 | 从众心理 | 展示他人选择 |
| 权威 | 信任专家 | 引用权威观点 |
| 喜好 | 喜欢则同意 | 建立好感 |
| 稀缺 | 害怕失去 | 强调稀缺性 |

**分支条件**：
- 若 `context=商业提案` → 优先使用权威和互惠
- 若 `context=政策建议` → 优先使用社会认同和权威
- 若 `context=谈判` → 优先使用承诺一致和稀缺
- 若 `context=学术论文` → 优先使用权威和逻辑论证
- 若受众为理性人群 → 优先使用逻辑论证
- 若受众为感性人群 → 优先使用情感诉求

### Step 2: 论证结构设计

- **输入**：`position` + `evidence`
- **动作**：
  1. 确定核心论点
  2. 构建论证结构
  3. 准备反驳回应
- **输出**：`argument_structure`
- **论证结构类型**：

| 类型 | 结构 | 适用场景 |
|------|------|----------|
| 演绎法 | 大前提-小前提-结论 | 逻辑严密的论证 |
| 归纳法 | 案例-规律-结论 | 经验性论证 |
| 溯因法 | 结果-原因-解释 | 解释性论证 |
| 辩证法 | 正-反-合 | 复杂问题讨论 |

**分支条件**：
- 若有大量数据支持 → 使用归纳法
- 若需要逻辑严密 → 使用演绎法
- 若需要解释现象 → 使用溯因法
- 若存在争议 → 使用辩证法

### Step 3: 修辞技巧应用

- **输入**：`argument_structure` + `style`
- **动作**：
  1. 选择修辞技巧
  2. 应用到论证中
  3. 增强说服力
- **输出**：`rhetoric_techniques`
- **修辞技巧库**：

| 技巧 | 描述 | 示例 |
|------|------|------|
| 隐喻 | 类比说明 | "时间就是金钱" |
| 排比 | 增强气势 | "我们需要...我们需要...我们需要..." |
| 反问 | 引发思考 | "难道我们不应该...吗？" |
| 对比 | 突出差异 | "过去...现在..." |
| 故事 | 情感共鸣 | "让我讲一个故事..." |
| 数据 | 理性支撑 | "数据显示..." |

**分支条件**：
- 若 `style=logical` → 优先使用数据和对比
- 若 `style=emotional` → 优先使用故事和隐喻
- 若 `style=balanced` → 综合使用各种技巧
- 若 `audience=专业人士` → 减少情感技巧
- 若 `audience=普通大众` → 增加情感技巧

### Step 4: 心理钩子设计

- **输入**：`position` + `audience`
- **动作**：
  1. 设计情感诉求
  2. 识别认知偏差
  3. 确定框架策略
- **输出**：`psychological_hooks`
- **认知偏差应用**：

| 偏差 | 原理 | 应用方法 |
|------|------|----------|
| 锚定效应 | 先入为主 | 提供参考点 |
| 损失厌恶 | 害怕失去 | 强调损失 |
| 确认偏差 | 符合预期 | 符合既有观点 |
| 从众效应 | 随大流 | 展示多数选择 |
| 光环效应 | 以偏概全 | 突出正面特质 |

**分支条件**：
- 若需要理性决策 → 减少认知偏差应用
- 若需要快速决策 → 适当应用认知偏差
- 若涉及伦理考量 → 谨慎使用心理技巧
- 若 `context=学术` → 避免使用认知偏差

### Step 5: 论证完善与交付

- **输入**：所有前序输出
- **动作**：
  1. 检查逻辑严密性
  2. 优化表达方式
  3. 确定交付策略
- **输出**：`delivery_recommendations`
- **交付策略**：

| 策略 | 目的 | 适用场景 |
|------|------|----------|
| 渐进式 | 逐步推进 | 复杂论证 |
| 冲击式 | 强烈开场 | 需要关注 |
| 故事式 | 情感共鸣 | 需要认同 |
| 数据式 | 理性说服 | 需要信任 |

**分支条件**：
- 若 `context=提案` → 使用渐进式
- 若 `context

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
