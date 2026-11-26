---
name: uskill-education-learning-assessment
description: "让学习评估变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-education-learning-assessment.md"
  original_id: "SKL-6854"
  version: "3.0.0"
  trust: untrusted
---

# 学习评估

description: |
  当用户需要设计评估方法、衡量学习效果、提供有效反馈、改进教学时使用此 Skill。
  触发词包括：'学习评估'、'评估方法'、'学习效果'、'反馈'、'考核'、
  '学习测试'。当用户讨论教育、培训、知识管理时，
  即使未直接说"学习评估"，也应使用此 Skill。
  不适用于简单的考试出题（使用其他 Skill）。遇到系统化评估设计时优先使用。

---

# uSkill-702: 学习评估

## 🎯 目标

> 设计有效的学习评估方法，衡量学习效果，提供改进建议。

**核心价值**：没有评估就没有改进。好的评估能驱动持续学习。

**适用场景**：
- 课程效果评估
- 员工培训评估
- 个人学习效果衡量
- 教学质量改进
- 知识掌握度测试

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `learning_objectives` | `array` | ✅ | — | 学习目标 |
| `assessment_type` | `enum` | ❌ | `formative` | `formative` / `summative` / `diagnostic` |
| `learner_context` | `string` | ❌ | — | 学习者背景 |
| `constraints` | `object` | ❌ | — | 时间、资源限制 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话评估建议",
  "assessment_id": "LA-YYYY-MMDD-NNN",

  "assessment_design": {
    "type": "formative|summative|diagnostic",
    "methods": [
      {
        "method": "string",
        "purpose": "string",
        "alignment": "string",
        "pros": ["string"],
        "cons": ["string"]
      }
    ],
    "rubric": {
      "criteria": ["string"],
      "levels": ["string"],
      "scoring_guide": "string"
    }
  },

  "assessment_tools": [
    {
      "tool": "string",
      "description": "string",
      "best_for": "string",
      "implementation": "string"
    }
  ],

  "feedback_framework": {
    "timeliness": "string",
    "specificity": "string",
    "constructiveness": "string",
    "feedback_templates": ["string"]
  },

  "data_collection": {
    "metrics": ["string"],
    "collection_methods": ["string"],
    "frequency": "string",
    "responsible_parties": ["string"]
  },

  "analysis_and_reporting": {
    "analysis_methods": ["string"],
    "reporting_format": "string",
    "stakeholder_communication": ["string"]
  },

  "improvement_cycle": {
    "data_to_insights": "string",
    "insights_to_actions": "string",
    "actions_to_results": "string"
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

### Step 1: 评估设计

- **输入**：`learning_objectives` + `assessment_type`
- **动作**：
  1. 选择评估方法
  2. 设计评分标准
  3. 对齐学习目标
- **输出**：`assessment_design`
- **评估方法选择**：

| 方法 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| 测试 | 知识掌握 | 客观、可量化 | 无法评估应用 |
| 项目 | 综合能力 | 真实、全面 | 耗时 |
| 观察 | 技能操作 | 直接、真实 | 主观 |
| 反思 | 元认知 | 深度、个性化 | 难以标准化 |

### Step 2: 评估工具

- **输入**：`assessment_design`
- **动作**：
  1. 选择评估工具
  2. 设计实施流程
  3. 准备资源
- **输出**：`assessment_tools`

### Step 3: 反馈框架

- **输入**：`assessment_design`
- **动作**：
  1. 设计反馈原则
  2. 创建反馈模板
  3. 培训反馈者
- **输出**：`feedback_framework`
- **有效反馈原则**：

| 原则 | 描述 |
|------|------|
| 及时性 | 尽快提供反馈 |
| 具体性 | 指出具体行为 |
| 建设性 | 提供改进方向 |
| 平衡性 | 肯定优点和改进点 |

### Step 4: 数据收集

- **输入**：`assessment_tools`
- **动作**：
  1. 定义关键指标
  2. 设计收集方法
  3. 安排收集频率
- **输出**：`data_collection`

### Step 5: 分析和报告

- **输入**：`data_collection`
- **动作**：
  1. 选择分析方法
  2. 设计报告格式
  3. 规划沟通方式
- **输出**：`analysis_and_reporting`

### Step 6: 改进循环

- **输入**：所有前序输出
- **动作**：
  1. 设计数据到洞察的转化
  2. 设计洞察到行动的转化
  3. 设计行动到结果的验证
- **输出**：`improvement_cycle`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**仅使用单一评估方法
2. **不得**忽视评估公平性
3. **必须**与学习目标对齐

### 软性约束（建议遵守）
1. 建议结合定量和定性评估
2. 建议提供多次评估机会
3. 建议让学习者参与评估设计

### 人工兜底点
- 当涉及重要决策时，**必须**建议多角度评估
- 当评估结果异常时，**必须**建议深入分析

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `LA_WARNING_MISALIGNMENT` | 评估与目标不对齐 | 建议调整 | 🟡 |
| `LA_WARNING_BIAS` | 评估可能存在偏见 | 建议校准 | 🟡 |
| `LA_ERROR_NO_DATA` | 无法收集数据 | 建议更换方法 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 评估方法已选择
- [ ] 评分标准已设计
- [ ] 反馈框架已制定
- [ ] 改进循环已设计

### OVP 验证信号
- 评估有效性评分 ≥ 85/100
- 学习效果提升 ≥ 20%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "课程效果评估",
    "prompt": "评估一个在线Python课程的学习效果",
    "context": "learning_objectives=[掌握Python基础], assessment_type=summative",
    "assertions": [
      "assessment_design.m

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
