---
name: uskill-education-instructional-design
description: "让教学设计变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-education-instructional-design.md"
  original_id: "SKL-6826"
  version: "3.0.0"
  trust: untrusted
---

# 教学设计

description: |
  当用户需要设计课程、开发教学内容、制定学习目标、设计评估方法时使用此 Skill。
  触发词包括：'教学设计'、'课程设计'、'学习目标'、'教学大纲'、'课程开发'、
  '教学方法'。当用户讨论培训、教育、知识传授时，
  即使未直接说"教学设计"，也应使用此 Skill。
  不适用于简单的知识分享（使用其他 Skill）。遇到系统化教学设计时优先使用。

---

# uSkill-701: 教学设计

## 🎯 目标

> 基于 ADDIE 模型和 Bloom 分类法，设计有效的教学活动和评估方法。

**核心价值**：好的教学设计能大幅提升学习效果，让知识传递更高效。

**适用场景**：
- 在线课程设计
- 企业培训设计
- 工作坊设计
- 教材编写
- 知识库设计

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `topic` | `string` | ✅ | — | 教学主题 |
| `target_audience` | `string` | ✅ | — | 目标学员 |
| `learning_objectives` | `array` | ❌ | `[]` | 学习目标 |
| `duration` | `string` | ❌ | `1hour` | 教学时长 |
| `format` | `enum` | ❌ | `online` | `online` / `offline` / `hybrid` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话教学设计建议",
  "instructional_id": "ID-YYYY-MMDD-NNN",

  "needs_analysis": {
    "learner_profile": {
      "prior_knowledge": "low|medium|high",
      "learning_style": "visual|auditory|kinesthetic|reading",
      "motivation": "intrinsic|extrinsic",
      "constraints": ["string"]
    },
    "learning_gaps": ["string"],
    "success_criteria": ["string"]
  },

  "learning_objectives": [
    {
      "objective": "string",
      "bloom_level": "remember|understand|apply|analyze|evaluate|create",
      "assessment_method": "string",
      "success_criteria": "string"
    }
  ],

  "curriculum_design": {
    "structure": {
      "modules": [
        {
          "name": "string",
          "duration": "string",
          "objectives": ["string"],
          "activities": ["string"],
          "materials": ["string"]
        }
      ],
      "total_duration": "string"
    },
    "pedagogical_approach": "string",
    "engagement_strategies": ["string"]
  },

  "assessment_design": {
    "formative": [
      {
        "method": "string",
        "purpose": "string",
        "timing": "string"
      }
    ],
    "summative": [
      {
        "method": "string",
        "alignment": "string",
        "rubric": "string"
      }
    ],
    "feedback_mechanism": "string"
  },

  "materials_and_resources": [
    {
      "type": "string",
      "description": "string",
      "purpose": "string"
    }
  ],

  "implementation_plan": {
    "preparation": ["string"],
    "delivery_tips": ["string"],
    "contingency_plans": ["string"]
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

### Step 1: 需求分析

- **输入**：`topic` + `target_audience`
- **动作**：
  1. 分析学员画像
  2. 识别学习差距
  3. 确定成功标准
- **输出**：`needs_analysis`

### Step 2: 学习目标制定

- **输入**：`needs_analysis` + `learning_objectives`
- **动作**：
  1. 应用 Bloom 分类法
  2. 制定可衡量的目标
  3. 对齐评估方法
- **输出**：`learning_objectives`
- **Bloom 分类法**：

| 层级 | 动词 | 评估方法 |
|------|------|----------|
| 记忆 | 列举、识别、背诵 | 选择题、填空题 |
| 理解 | 解释、总结、举例 | 简答题、概念图 |
| 应用 | 使用、计算、演示 | 案例分析、实操 |
| 分析 | 比较、区分、组织 | 论文、报告 |
| 评估 | 判断、评价、辩护 | 辩论、评审 |
| 创造 | 设计、构建、发明 | 项目、作品 |

### Step 3: 课程设计

- **输入**：`learning_objectives`
- **动作**：
  1. 设计课程结构
  2. 安排教学活动
  3. 选择教学方法
- **输出**：`curriculum_design`
- **教学方法选择**：

| 方法 | 适用场景 | 优点 |
|------|----------|------|
| 讲授 | 知识传递 | 高效 |
| 讨论 | 观点交流 | 深入 |
| 案例 | 应用实践 | 真实 |
| 项目 | 综合能力 | 实践 |
| 翻转课堂 | 自主学习 | 灵活 |

### Step 4: 评估设计

- **输入**：`learning_objectives`
- **动作**：
  1. 设计形成性评估
  2. 设计总结性评估
  3. 制定评分标准
- **输出**：`assessment_design`
- **评估类型**：

| 类型 | 目的 | 时机 |
|------|------|------|
| 形成性 | 监控学习进度 | 学习过程中 |
| 总结性 | 评估学习成果 | 学习结束后 |

### Step 5: 材料和资源

- **输入**：`curriculum_design`
- **动作**：
  1. 列出所需材料
  2. 推荐学习资源
  3. 设计辅助工具
- **输出**：`materials_and_resources`

### Step 6: 实施计划

- **输入**：所有前序输出
- **动作**：
  1. 制定准备清单
  2. 提供交付建议
  3. 准备应急预案
- **输出**：`implementation_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽略学习目标的可衡量性
2. **不得**使用单一评估方法
3. **必须**考虑学员多样性

### 软性约束（建议遵守）
1. 建议每 15-20 分钟变换活动
2. 建议提供多种学习路径
3. 建议收集学员反馈

### 人工兜底点
- 当学员基础差异大时，**必须**建议分层教学
- 当涉及敏感话题时，**必须**建议谨慎处理

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|------

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
