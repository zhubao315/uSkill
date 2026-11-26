---
name: uskill-thinking-innovation
description: "让创新思维变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-thinking-innovation.md"
  original_id: "SKL-6853"
  version: "3.0.0"
  trust: untrusted
---

# 创新思维

description: |
  当用户需要产生创新想法、突破思维定式、进行创造性思考、解决复杂问题时使用此 Skill。
  触发词包括：'创新'、'创意'、'brainstorming'、'头脑风暴'、'SCAMPER'、
  '六顶思考帽'、'水平思考'。当用户讨论创新、设计思维、问题解决时，
  即使未直接说"创新思维"，也应使用此 Skill。
  不适用于执行已确定的方案（使用其他 Skill）。遇到创新需求时优先使用。

---

# uSkill-109: 创新思维

## 🎯 目标

> 应用系统化创新方法，产生高质量的创新想法。

**核心价值**：创新不是天赋，而是可以学习的方法。

**适用场景**：
- 产品创新
- 流程改进
- 问题解决
- 商业模式创新
- 战略创新

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `challenge` | `string` | ✅ | — | 需要创新的挑战 |
| `constraint` | `array` | ❌ | `[]` | 限制条件 |
| `method` | `enum` | ❌ | `auto` | `scamper` / `six_hats` / `lateral` / `auto` |
| `diversity_level` | `enum` | ❌ | `medium` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话创新建议",
  "innovation_id": "IN-YYYY-MMDD-NNN",

  "challenge_analysis": {
    "core_problem": "string",
    "assumptions_to_challenge": ["string"],
    "perspectives": ["string"],
    "success_criteria": "string"
  },

  "innovation_method": {
    "primary_method": "scamper|six_hats|lateral|design_thinking",
    "application": "string",
    "techniques_used": ["string"]
  },

  "ideas_generated": [
    {
      "idea": "string",
      "description": "string",
      "novelty": "low|medium|high",
      "feasibility": "low|medium|high",
      "potential_impact": "low|medium|high",
      "implementation_sketch": "string"
    }
  ],

  "idea_evaluation": {
    "criteria": ["string"],
    "scoring_matrix": [
      {
        "idea": "string",
        "scores": {
          "novelty": "number",
          "feasibility": "number",
          "impact": "number"
        },
        "total_score": "number"
      }
    ],
    "top_ideas": ["string"]
  },

  "implementation_roadmap": {
    "phase_1_explore": {
      "duration": "string",
      "activities": ["string"],
      "deliverables": ["string"]
    },
    "phase_2_prototype": {
      "duration": "string",
      "activities": ["string"],
      "deliverables": ["string"]
    },
    "phase_3_test": {
      "duration": "string",
      "activities": ["string"],
      "deliverables": ["string"]
    }
  },

  "creativity_exercises": [
    {
      "exercise": "string",
      "purpose": "string",
      "time_required": "string"
    }
  ],

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 挑战分析

- **输入**：`challenge` + `constraint`
- **动作**：
  1. 明确核心问题
  2. 识别需要挑战的假设
  3. 确定成功标准
- **输出**：`challenge_analysis`

### Step 2: 创新方法选择

- **输入**：`challenge_analysis` + `method`
- **动作**：
  1. 选择最适合的方法
  2. 应用方法技巧
  3. 生成多样化想法
- **输出**：`innovation_method`
- **创新方法库**：

| 方法 | 描述 | 适用场景 |
|------|------|----------|
| SCAMPER | 替代、合并、调整、修改、另用、消除、重排 | 产品改进 |
| 六顶思考帽 | 白(事实)、红(情感)、黑(风险)、黄(利益)、绿(创意)、蓝(控制) | 全面思考 |
| 水平思考 | 打破常规思维路径 | 突破性创新 |
| 设计思维 | 同情、定义、构思、原型、测试 | 用户中心设计 |

### Step 3: 想法生成

- **输入**：`innovation_method`
- **动作**：
  1. 应用创新技巧
  2. 产生多样化想法
  3. 鼓励疯狂想法
- **输出**：`ideas_generated`
- **SCAMPER 技巧**：

| 字母 | 技巧 | 问题示例 |
|:----:|------|----------|
| S | 替代 | 什么可以被替代？ |
| C | 合并 | 什么可以合并？ |
| A | 调整 | 什么可以调整？ |
| M | 修改 | 什么可以放大/缩小？ |
| P | 另用 | 有什么其他用途？ |
| E | 消除 | 什么可以删除？ |
| R | 重排 | 什么可以重新排列？ |

### Step 4: 想法评估

- **输入**：`ideas_generated`
- **动作**：
  1. 定义评估标准
  2. 评分每个想法
  3. 选择最佳想法
- **输出**：`idea_evaluation`

### Step 5: 实施路线图

- **输入**：`idea_evaluation.top_ideas`
- **动作**：
  1. 设计探索阶段
  2. 设计原型阶段
  3. 设计测试阶段
- **输出**：`implementation_roadmap`

### Step 6: 创造力练习

- **输入**：`challenge_analysis`
- **动作**：
  1. 设计日常练习
  2. 安排团队练习
  3. 提供灵感来源
- **输出**：`creativity_exercises`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在想法生成阶段评判
2. **不得**忽视可行性
3. **必须**考虑约束条件

### 软性约束（建议遵守）
1. 建议先追求数量再追求质量
2. 建议鼓励"疯狂"想法
3. 建议结合多种方法

### 人工兜底点
- 当创新涉及重大风险时，**必须**建议小规模测试
- 当团队创新受阻时，**必须**建议外部刺激

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IN_WARNING_BLOCKED` | 思维受阻 | 换个方法 | 🟡 |
| `IN_WARNING_SAME_IDEAS` | 想法雷同 | 增加多样性 | 🟡 |


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
