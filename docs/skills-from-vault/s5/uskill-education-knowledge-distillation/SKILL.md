---
name: uskill-education-knowledge-distillation
description: "让知识蒸馏变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-education-knowledge-distillation.md"
  original_id: "SKL-6841"
  version: "3.0.0"
  trust: untrusted
---

# 知识蒸馏

description: |
  当用户需要将复杂概念简化、进行知识传达、制作教学材料、解释专业概念时使用此 Skill。
  触发词包括：'知识蒸馏'、'简化'、'通俗易懂'、'教学'、'解释'、
  '复杂概念简化'。当用户讨论教学、知识分享、沟通时，
  即使未直接说"知识蒸馏"，也应使用此 Skill。
  不适用于深度技术文档（使用其他 Skill）。遇到知识简化需求时优先使用。

---

# uSkill-703: 知识蒸馏

## 🎯 目标

> 将复杂知识简化为易于理解的形式，同时保持准确性。

**核心价值**：能够简单解释复杂概念，才是真正理解的标志。

**适用场景**：
- 教学材料制作
- 技术文档简化
- 知识分享
- 跨部门沟通
- 客户教育

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `complex_knowledge` | `string` | ✅ | — | 复杂知识描述 |
| `target_audience` | `string` | ✅ | — | 目标受众 |
| `simplification_level` | `enum` | ❌ | `moderate` | `light` / `moderate` / `heavy` |
| `format` | `enum` | ❌ | `text` | `text` / `visual` / `interactive` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话简化建议",
  "distillation_id": "KD-YYYY-MMDD-NNN",

  "knowledge_analysis": {
    "core_concept": "string",
    "key_components": ["string"],
    "common_misconceptions": ["string"],
    "prerequisites": ["string"]
  },

  "simplification_strategy": {
    "analogy": {
      "analogy_description": "string",
      "mapping": {
        "source_domain": "string",
        "target_domain": "string",
        "correspondences": ["string"]
      },
      "limitations": ["string"]
    },
    "metaphor": "string",
    "story": "string",
    "visual_metaphor": "string"
  },

  "simplified_explanations": {
    "one_liner": "string",
    "elevator_pitch": "string",
    "detailed_explanation": "string",
    "visual_representation": "string"
  },

  "progressive_disclosure": {
    "level_1_basic": "string",
    "level_2_intermediate": "string",
    "level_3_advanced": "string",
    "level_4_expert": "string"
  },

  "common_questions": [
    {
      "question": "string",
      "answer": "string",
      "misconception_addressed": "string"
    }
  ],

  "validation": {
    "accuracy_check": "string",
    "clarity_check": "string",
    "engagement_check": "string"
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

### Step 1: 知识分析

- **输入**：`complex_knowledge`
- **动作**：
  1. 识别核心概念
  2. 分解关键组件
  3. 识别常见误解
- **输出**：`knowledge_analysis`

### Step 2: 简化策略

- **输入**：`knowledge_analysis` + `target_audience`
- **动作**：
  1. 选择类比
  2. 设计隐喻
  3. 创作故事
- **输出**：`simplification_strategy`
- **简化技术**：

| 技术 | 描述 | 适用场景 |
|------|------|----------|
| 类比 | 用熟悉事物解释新概念 | 概念引入 |
| 隐喻 | 用形象语言描述 | 抽象概念 |
| 故事 | 用叙事传达知识 | 情感连接 |
| 可视化 | 用图表展示 | 关系展示 |

### Step 3: 分层解释

- **输入**：`simplification_strategy`
- **动作**：
  1. 设计基础解释
  2. 设计进阶解释
  3. 设计专家解释
- **输出**：`simplified_explanations` + `progressive_disclosure`

### Step 4: 常见问题

- **输入**：`knowledge_analysis.common_misconceptions`
- **动作**：
  1. 预测常见问题
  2. 准备清晰答案
  3. 纠正常见误解
- **输出**：`common_questions`

### Step 5: 验证

- **输入**：所有前序输出
- **动作**：
  1. 检查准确性
  2. 检查清晰度
  3. 检查吸引力
- **输出**：`validation`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**牺牲准确性换取简单
2. **不得**过度简化导致误解
3. **必须**标注简化局限性

### 软性约束（建议遵守）
1. 建议使用多种简化技术
2. 建议测试简化效果
3. 建议提供深入学习路径

### 人工兜底点
- 当涉及专业领域时，**必须**建议专家审核
- 当简化可能导致误解时，**必须**标注警告

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `KD_WARNING_OVERSIMPLIFY` | 过度简化 | 建议增加细节 | 🟡 |
| `KD_WARNING_INACCURATE` | 简化不准确 | 建议修正 | 🟡 |
| `KD_ERROR_TOO_COMPLEX` | 无法简化 | 建议分步简化 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 核心概念已识别
- [ ] 类比已设计
- [ ] 分层解释已生成
- [ ] 常见问题已准备

### OVP 验证信号
- 简化准确率 ≥ 90%
- 受众理解率 ≥ 85%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "技术概念简化",
    "prompt": "用简单语言解释机器学习",
    "context": "target_audience=非技术人员",
    "assertions": [
      "knowledge_analysis.core_concept 已识别",
      "simplification_strategy.analogy 已设计",
      "simplified_explanations.one_liner 已生成"
    ],
    "expected_behavior": "将机器学习简化为通俗概念",
    "critic_attack": "简化是否保持了准确性？"
  },
  {
    "id": "test-002",
    "name": "商业概念简化",
    "prompt": "如何向客户解释我们的AI产品",
    "context": 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
