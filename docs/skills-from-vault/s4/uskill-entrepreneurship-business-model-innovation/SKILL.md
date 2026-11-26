---
name: uskill-entrepreneurship-business-model-innovation
description: "让商业模式创新变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-entrepreneurship-business-model-innovation.md"
  original_id: "SKL-6813"
  version: "3.0.0"
  trust: untrusted
---

# 商业模式创新

description: |
  当用户需要创新商业模式、重新设计盈利方式、颠覆传统行业、寻找蓝海市场时使用此 Skill。
  触发词包括：'商业模式创新'、'盈利模式'、'颠覆式创新'、'蓝海战略'、
  '重新设计商业模式'。当用户讨论创业、战略转型、行业变革时，
  即使未直接说"商业模式创新"，也应使用此 Skill。
  不适用于现有模式优化（使用商业画布）。遇到颠覆性创新需求时优先使用。

---

# uSkill-803: 商业模式创新

## 🎯 目标

> 使用商业模式创新工具，发现新的价值创造和价值获取方式。

**核心价值**：商业模式创新比产品创新更能改变行业格局。

**适用场景**：
- 行业颠覆
- 新市场创造
- 盈利模式重构
- 平台经济设计
- 生态系统构建

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_model` | `string` | ✅ | — | 当前商业模式描述 |
| `innovation_goal` | `enum` | ❌ | `disrupt` | `disrupt` / `expand` / `optimize` / `create` |
| `industry_context` | `string` | ❌ | — | 行业背景 |
| `constraints` | `array` | ❌ | `[]` | 限制条件 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话创新建议",
  "innovation_id": "BI-YYYY-MMDD-NNN",

  "current_model_analysis": {
    "strengths": ["string"],
    "weaknesses": ["string"],
    "opportunities": ["string"],
    "threats": ["string"]
  },

  "innovation_frameworks": {
    "blue_ocean_strategy": {
      "eliminate": ["string"],
      "reduce": ["string"],
      "raise": ["string"],
      "create": ["string"]
    },
    "business_model_patterns": [
      {
        "pattern": "string",
        "description": "string",
        "applicability": "high|medium|low"
      }
    ]
  },

  "innovation_ideas": [
    {
      "idea": "string",
      "description": "string",
      "value_proposition": "string",
      "revenue_model": "string",
      "key_resources": ["string"],
      "feasibility": "high|medium|low",
      "impact": "high|medium|low"
    }
  ],

  "implementation_roadmap": {
    "phase_1": {
      "name": "验证期",
      "duration": "string",
      "key_activities": ["string"],
      "success_criteria": "string"
    },
    "phase_2": {
      "name": "构建期",
      "duration": "string",
      "key_activities": ["string"],
      "success_criteria": "string"
    },
    "phase_3": {
      "name": "扩展期",
      "duration": "string",
      "key_activities": ["string"],
      "success_criteria": "string"
    }
  },

  "risk_assessment": {
    "key_risks": ["string"],
    "mitigation_strategies": ["string"],
    "kill_criteria": "string"
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

### Step 1: 当前模式分析

- **输入**：`current_model`
- **动作**：
  1. 分析当前模式的优势
  2. 识别弱点和机会
  3. 评估威胁
- **输出**：`current_model_analysis`

### Step 2: 创新框架应用

- **输入**：`current_model_analysis` + `innovation_goal`
- **动作**：
  1. 应用蓝海战略 ERRC 矩阵
  2. 应用商业模式模式库
  3. 生成创新想法
- **输出**：`innovation_frameworks`
- **商业模式创新模式**：

| 模式 | 描述 | 示例 |
|------|------|------|
| 平台模式 | 连接双方或多边市场 | 淘宝、Uber |
| 订阅模式 | 定期收费 | Netflix、Spotify |
| 免费增值 | 基础免费，高级付费 | Dropbox、LinkedIn |
| 共享经济 | 共享闲置资源 | Airbnb、滴滴 |
| 数据变现 | 利用数据创造价值 | Google、Facebook |

### Step 3: 创新想法生成

- **输入**：`innovation_frameworks`
- **动作**：
  1. 生成多个创新想法
  2. 评估每个想法
  3. 选择最有潜力的想法
- **输出**：`innovation_ideas`

### Step 4: 实施路线图

- **输入**：`innovation_ideas`
- **动作**：
  1. 设计验证期
  2. 设计构建期
  3. 设计扩展期
- **输出**：`implementation_roadmap`

### Step 5: 风险评估

- **输入**：`innovation_ideas`
- **动作**：
  1. 识别关键风险
  2. 制定缓解策略
  3. 设定终止标准
- **输出**：`risk_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视市场需求
2. **不得**过度理想化
3. **必须**考虑可执行性

### 软性约束（建议遵守）
1. 建议从小规模验证开始
2. 建议保持迭代心态
3. 建议关注现金流

### 人工兜底点
- 当涉及重大投资时，**必须**建议专业评估
- 当创新颠覆性强时，**必须**建议深度验证

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `BI_WARNING_UNFEASIBLE` | 方案不可行 | 建议调整 | 🟡 |
| `BI_WARNING_INCREMENTAL` | 创新不够颠覆 | 建议更大胆 | 🟡 |
| `BI_ERROR_NO_VALUE` | 无价值创造 | 建议重新思考 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 当前模式已分析
- [ ] 创新框架已应用
- [ ] 创新想法已生成
- [ ] 实施路线图已设计

### OVP 验证信号
- 创新想法数量 ≥ 3
- 可行性评分 ≥ 75/100

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "传统行业颠覆",
    "prompt": "如何颠覆传统出租车行业",
    "context": "current_model=传统出租车, innovation_goal=disrupt",
    "ass

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
