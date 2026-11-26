---
name: uskill-health-nutrition-planning
description: "让营养规划变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-nutrition-planning.md"
  original_id: "SKL-6822"
  version: "3.0.0"
  trust: untrusted
---

# 营养规划

description: |
  当用户需要制定饮食计划、优化营养摄入、管理体重、调整饮食习惯时使用此 Skill。
  触发词包括：'营养'、'饮食'、'减肥'、'增肌'、'卡路里'、'蛋白质'、
  '营养规划'、'饮食计划'。当用户讨论健康、运动、体重管理时，
  即使未直接说"营养规划"，也应使用此 Skill。
  不适用于特殊饮食需求（如糖尿病、过敏，需咨询医生）。遇到营养规划需求时优先使用。

---

# uSkill-303: 营养规划

## 🎯 目标

> 基于营养科学，制定个性化的饮食计划，优化营养摄入，支持健康目标。

**核心价值**：营养是健康的基石。正确的饮食能提升精力、改善体态、预防疾病。

**适用场景**：
- 体重管理（减脂/增肌）
- 运动营养
- 日常健康饮食
- 精力优化
- 睡眠改善

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `health_goal` | `enum` | ✅ | — | `weight_loss` / `muscle_gain` / `maintenance` / `performance` |
| `body_metrics` | `object` | ❌ | — | `{weight, height, age, gender, body_fat}` |
| `activity_level` | `enum` | ❌ | `moderate` | `sedentary` / `light` / `moderate` / `active` / `very_active` |
| `dietary_restrictions` | `array` | ❌ | `[]` | 饮食限制 |
| `preferences` | `object` | ❌ | — | 饮食偏好 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话营养建议",
  "nutrition_id": "NT-YYYY-MMDD-NNN",

  "calorie_needs": {
    "basal_metabolic_rate": "number",
    "total_daily_energy_expenditure": "number",
    "target_calories": "number",
    "calorie_adjustment": "number",
    "reasoning": "string"
  },

  "macronutrient_plan": {
    "protein": {
      "grams": "number",
      "percentage": "number",
      "timing": ["string"],
      "sources": ["string"]
    },
    "carbohydrates": {
      "grams": "number",
      "percentage": "number",
      "timing": ["string"],
      "sources": ["string"]
    },
    "fats": {
      "grams": "number",
      "percentage": "number",
      "timing": ["string"],
      "sources": ["string"]
    }
  },

  "micronutrient_focus": [
    {
      "nutrient": "string",
      "importance": "string",
      "recommended_amount": "string",
      "food_sources": ["string"]
    }
  ],

  "meal_plan": [
    {
      "meal": "breakfast|lunch|dinner|snack",
      "time": "string",
      "calories": "number",
      "macronutrients": {
        "protein": "number",
        "carbs": "number",
        "fats": "number"
      },
      "suggested_foods": ["string"],
      "portion_guidance": "string"
    }
  ],

  "hydration_plan": {
    "daily_water_intake": "string",
    "timing": ["string"],
    "electrolyte_considerations": "string"
  },

  "supplement_recommendations": [
    {
      "supplement": "string",
      "dosage": "string",
      "timing": "string",
      "reasoning": "string"
    }
  ],

  "monitoring_plan": {
    "daily_checks": ["string"],
    "weekly_reviews": ["string"],
    "adjustment_triggers": ["string"]
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

### Step 1: 能量需求计算

- **输入**：`body_metrics` + `activity_level` + `health_goal`
- **动作**：
  1. 计算基础代谢率
  2. 计算总能量消耗
  3. 确定目标热量
- **输出**：`calorie_needs`
- **BMR 计算公式（Mifflin-St Jeor）**：
  - 男性：BMR = 10 × 体重(kg) + 6.25 × 身高(cm) - 5 × 年龄 - 5
  - 女性：BMR = 10 × 体重(kg) + 6.25 × 身高(cm) - 5 × 年龄 - 161

### Step 2: 宏量营养素分配

- **输入**：`calorie_needs` + `health_goal`
- **动作**：
  1. 计算蛋白质需求
  2. 计算碳水化合物需求
  3. 计算脂肪需求
- **输出**：`macronutrient_plan`
- **宏量营养素分配指南**：

| 目标 | 蛋白质 | 碳水 | 脂肪 |
|------|:------:|:----:|:----:|
| 减脂 | 30-35% | 35-40% | 25-30% |
| 增肌 | 25-30% | 45-55% | 20-25% |
| 维持 | 20-25% | 45-55% | 25-30% |
| 运动表现 | 20-25% | 55-65% | 20-25% |

### Step 3: 微量营养素关注

- **输入**：`health_goal` + `dietary_restrictions`
- **动作**：
  1. 识别关键微量营养素
  2. 推荐食物来源
  3. 评估补充剂需求
- **输出**：`micronutrient_focus`

### Step 4: 餐食计划

- **输入**：`calorie_needs` + `macronutrient_plan`
- **动作**：
  1. 分配餐次
  2. 设计每餐内容
  3. 安排进食时间
- **输出**：`meal_plan`

### Step 5: 水分计划

- **输入**：`body_metrics` + `activity_level`
- **动作**：
  1. 计算水分需求
  2. 安排饮水时间
  3. 考虑电解质
- **输出**：`hydration_plan`

### Step 6: 补充剂建议

- **输入**：`micronutrient_focus` + `dietary_restrictions`
- **动作**：
  1. 评估补充剂需求
  2. 推荐补充剂类型
  3. 确定剂量和时间
- **输出**：`supplement_recommendations`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议极端饮食
2. **不得**忽视个体差异
3. **必须**建议咨询医生（特殊健康状况）

###

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
