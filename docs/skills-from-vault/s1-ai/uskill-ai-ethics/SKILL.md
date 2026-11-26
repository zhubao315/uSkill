---
name: uskill-ai-ethics
description: "让AI伦理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-ethics.md"
  original_id: "SKL-6863"
  version: "3.0.0"
  trust: untrusted
---

# AI伦理

description: |
  当用户需要评估和改进 AI 系统的伦理合规性（偏见、公平性、可解释性、透明度）时使用此 Skill。
  触发词包括：'AI伦理'、'偏见检测'、'公平性'、'可解释性'、'透明度'、'算法审计'。
  当用户提到"AI 有偏见"、"不公平"、"不知道为什么这样输出"、"需要解释"时，
  即使未直接说"AI伦理"，也应使用此 Skill。
  不适用于性能优化。遇到 AI 安全和伦理合规时优先使用。

---

# uSkill-904: AI伦理

## 🎯 目标

> 评估和改进 AI 系统的伦理合规性，包括偏见检测、公平性评估、可解释性和透明度。

**核心价值**：确保 AI 系统公正、透明、可信赖，符合社会伦理和法规要求。

**适用场景**：
- AI 模型上线前审计
- 算法公平性评估
- 决策可解释性改进
- 合规性检查（GDPR、AI Act）
- AI 伦理培训

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `system_type` | `enum` | ✅ | — | `classification` / `generation` / `recommendation` / `decision` |
| `domain` | `string` | ✅ | — | 应用领域（如招聘、贷款、医疗） |
| `sensitive_attributes` | `array` | ❌ | `[]` | 需要检查的敏感属性 |
| `current_issues` | `array` | ❌ | `[]` | 已知的伦理问题 |
| `regulatory_requirements` | `array` | ❌ | `[]` | 需要遵守的法规 |

**输入约束**：
- `domain` 影响偏见检测的重点维度
- `sensitive_attributes` 应覆盖所有相关敏感属性
- `regulatory_requirements` 应明确具体的合规要求

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结 AI 伦理评估结果",
  "ethics_id": "AE-YYYY-MMDD-NNN",

  "bias_assessment": {
    "dimensions_checked": ["string"],
    "bias_metrics": [
      {
        "attribute": "string",
        "metric": "string",
        "value": "number",
        "threshold": "number",
        "status": "pass|fail|warning"
      }
    ],
    "root_cause_analysis": "string",
    "mitigation_strategies": ["string"]
  },

  "fairness_evaluation": {
    "fairness_definition": "string",
    "metrics": [
      {
        "name": "string",
        "value": "number",
        "target": "number",
        "explanation": "string"
      }
    ],
    "group_analysis": "string",
    "trade_offs": ["string"]
  },

  "explainability": {
    "method": "string",
    "features": [
      {
        "feature": "string",
        "importance": "number",
        "explanation": "string"
      }
    ],
    "decision_path": "string",
    "user_friendly_summary": "string"
  },

  "transparency": {
    "documentation": ["string"],
    "disclosure_items": ["string"],
    "limitation_disclosure": "string",
    "data_provenance": "string"
  },

  "compliance": {
    "regulations": [
      {
        "name": "string",
        "status": "compliant|non_compliant|partial",
        "gaps": ["string"],
        "remediation": ["string"]
      }
    ]
  },

  "recommendations": {
    "immediate": ["string"],
    "short_term": ["string"],
    "long_term": ["string"]
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

### Step 1: 系统画像与风险评估

- **输入**：`system_type`, `domain`, `sensitive_attributes`
- **动作**：
  1. 分析系统类型和应用领域
  2. 识别潜在的伦理风险维度
  3. 评估风险等级
- **输出**：风险评估报告
- **分支条件**：
  - IF 领域是高风险（招聘、贷款、医疗）→ 全面审计
  - IF 领域是中风险（推荐、搜索）→ 重点审计
  - IF 领域是低风险（内容生成）→ 基础审计
  - IF 有已知问题 → 针对性深度审计
  - ELSE → 标准审计流程
- **检查点**：✅ 应验证风险维度覆盖完整

### Step 2: 偏见检测与分析

- **输入**：风险评估结果
- **动作**：
  1. 选择偏见检测指标
  2. 执行统计测试
  3. 分析偏见来源
- **输出**：`bias_assessment`
- **分支条件**：
  - IF 检测到显著偏见 → 进行根因分析
  - IF 偏见不显著但接近阈值 → 标记为预警
  - IF 偏见来源是数据 → 建议数据增强或重采样
  - IF 偏见来源是模型 → 建议去偏见技术
  - ELSE → 记录为通过
- **检查点**：✅ 应验证检测覆盖所有敏感属性

### Step 3: 公平性评估

- **输入**：`bias_assessment`
- **动作**：
  1. 选择公平性定义和指标
  2. 执行公平性测试
  3. 分析群体差异
- **输出**：`fairness_evaluation`
- **分支条件**：
  - IF 使用群体公平性 → 检查统计平等、机会平等
  - IF 使用个体公平性 → 检查相似个体相似对待
  - IF 存在公平性权衡 → 明确权衡并记录
  - IF 无法满足所有公平性标准 → 选择最适合的
  - ELSE → 使用默认公平性标准
- **检查点**：✅ 应验证公平性指标选择与领域匹配

### Step 4: 可解释性设计

- **输入**：`fairness_evaluation`
- **动作**：
  1. 选择可解释性方法
  2. 生成特征重要性分析
  3. 设计用户友好的解释
- **输出**：`explainability`
- **分支条件**：
  - IF 是黑盒模型 → 使用 LIME/SHAP 等事后解释
  - IF 是白盒模型 → 使用内在可解释性
  - IF 面向普通用户 → 使用自然语言解释
  - IF 面向技术人员 → 使用特征重要性图
  - ELSE → 选择通用可解释性方法
- **检查点**：✅ 应验证解释准确反映了模型决策过程

### Step 5: 透明度与合规报告

- **输入**：所有前序评估结果
- **动作**：
  1. 生成透明度文档
  2. 评估法规合规性
  3. 制定改进建议
- **输出**：`transparency`, `compliance`, `recommendations`
- **检查点**：✅ 应验证报告完整且可操作

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在高风险应用中跳过偏见检测
2. **不得**隐瞒已知的

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
