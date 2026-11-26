---
name: uskill-entrepreneurship-business-model-canvas
description: "让商业画布变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-entrepreneurship-business-model-canvas.md"
  original_id: "SKL-6814"
  version: "3.0.0"
  trust: untrusted
---

# 商业画布

description: |
  当用户需要设计商业模式、分析商业要素、评估商业可行性、进行商业创新时使用此 Skill。
  触发词包括：'商业画布'、'商业模式'、'商业设计'、'价值主张'、'盈利模式'、
  '商业模式设计'。当用户讨论创业、产品、战略时，
  即使未直接说"商业画布"，也应使用此 Skill。
  不适用于已有成熟商业模式的优化（使用其他 Skill）。遇到商业模式设计时优先使用。

---

# uSkill-801: 商业画布

## 🎯 目标

> 使用 Business Model Canvas 9 要素框架，系统化设计和分析商业模式。

**核心价值**：商业画布是理解和设计商业模式的强大工具，一页纸看清商业全貌。

**适用场景**：
- 创业项目规划
- 新业务设计
- 商业模式创新
- 竞争对手分析
- 投资评估

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `business_idea` | `string` | ✅ | — | 商业想法描述 |
| `industry` | `string` | ❌ | — | 行业类型 |
| `stage` | `enum` | ❌ | `idea` | `idea` / `startup` / `growth` / `mature` |
| `existing_canvas` | `object` | ❌ | — | 现有商业模式（用于优化） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话商业模式总结",
  "canvas_id": "BM-YYYY-MMDD-NNN",

  "business_model_canvas": {
    "customer_segments": {
      "primary": "string",
      "secondary": ["string"],
      "personas": ["string"]
    },
    "value_propositions": {
      "core_value": "string",
      "pain_points_addressed": ["string"],
      "gains_created": ["string"],
      "differentiation": "string"
    },
    "channels": {
      "acquisition": ["string"],
      "delivery": ["string"],
      "support": ["string"]
    },
    "customer_relationships": {
      "type": "personal_assistance|self_service|automated|communities|co_creation",
      "retention_strategy": "string",
      "loyalty_programs": ["string"]
    },
    "revenue_streams": {
      "primary": "string",
      "pricing_model": "string",
      "recurring_revenue": "boolean",
      "revenue_mix": ["string"]
    },
    "key_resources": {
      "physical": ["string"],
      "intellectual": ["string"],
      "human": ["string"],
      "financial": ["string"]
    },
    "key_activities": {
      "production": ["string"],
      "platform": ["string"],
      "network": ["string"]
    },
    "key_partnerships": {
      "suppliers": ["string"],
      "strategic_alliances": ["string"],
      "joint_ventures": ["string"],
      "buyer_supplier": ["string"]
    },
    "cost_structure": {
      "fixed_costs": ["string"],
      "variable_costs": ["string"],
      "cost_drivers": ["string"]
    }
  },

  "feasibility_analysis": {
    "market_size": "string",
    "competition": "string",
    "entry_barriers": "string",
    "key_risks": ["string"],
    "mitigation_strategies": ["string"]
  },

  "financial_projections": {
    "revenue_model": "string",
    "break_even_estimate": "string",
    "funding_requirements": "string",
    "key_assumptions": ["string"]
  },

  "improvement_suggestions": [
    {
      "element": "string",
      "current_state": "string",
      "suggestion": "string",
      "impact": "high|medium|low"
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

### Step 1: 客户细分

- **输入**：`business_idea`
- **动作**：
  1. 识别主要客户群体
  2. 创建客户画像
  3. 分析客户需求
- **输出**：`business_model_canvas.customer_segments`

### Step 2: 价值主张

- **输入**：`customer_segments`
- **动作**：
  1. 定义核心价值
  2. 识别痛点解决方案
  3. 分析差异化
- **输出**：`business_model_canvas.value_propositions`
- **价值主张画布**：

| 客户侧 | 产品侧 |
|---------|---------|
| 客户任务 | 产品/服务 |
| 痛点 | 痛点缓解 |
| 期望收益 | 收益创造 |

### Step 3: 渠道通路

- **输入**：`customer_segments`
- **动作**：
  1. 设计获客渠道
  2. 设计交付渠道
  3. 设计支持渠道
- **输出**：`business_model_canvas.channels`

### Step 4: 客户关系

- **输入**：`customer_segments`
- **动作**：
  1. 确定关系类型
  2. 设计留存策略
  3. 设计忠诚度计划
- **输出**：`business_model_canvas.customer_relationships`

### Step 5: 收入来源

- **输入**：`value_propositions`
- **动作**：
  1. 识别收入来源
  2. 设计定价模型
  3. 评估经常性收入
- **输出**：`business_model_canvas.revenue_streams`

### Step 6: 核心资源

- **输入**：`value_propositions` + `channels`
- **动作**：
  1. 识别关键资源
  2. 评估资源需求
  3. 规划资源获取
- **输出**：`business_model_canvas.key_resources`

### Step 7: 关键业务

- **输入**：`value_propositions`
- **动作**：
  1. 识别关键活动
  2. 优化业务流程
  3. 评估外包需求
- **输出**：`business_model_canvas.key_activities`

#

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
