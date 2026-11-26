---
name: uskill-entrepreneurship-product-validation
description: "让产品验证变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-entrepreneurship-product-validation.md"
  original_id: "SKL-6811"
  version: "3.0.0"
  trust: untrusted
---

# 产品验证

description: |
  当用户需要验证产品假设、进行客户开发、测试PMF、设计MVP时使用此 Skill。
  触发词包括：'产品验证'、'MVP'、'客户开发'、'PMF'、'假设验证'、
  '最小可行产品'。当用户讨论创业、产品开发、市场验证时，
  即使未直接说"产品验证"，也应使用此 Skill。
  不适用于成熟产品的优化（使用其他 Skill）。遇到产品验证需求时优先使用。

---

# uSkill-802: 产品验证

## 🎯 目标

> 应用精益创业方法，系统化验证产品假设，找到产品市场契合点（PMF）。

**核心价值**：避免在错误的产品上浪费资源，快速学习和迭代。

**适用场景**：
- 创业产品验证
- 新功能验证
- 市场需求验证
- 商业模式验证
- PMF 测试

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `product_idea` | `string` | ✅ | — | 产品想法描述 |
| `target_market` | `string` | ✅ | — | 目标市场 |
| `assumptions` | `array` | ❌ | `[]` | 待验证假设 |
| `resources` | `object` | ❌ | — | 可用资源 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话验证建议",
  "validation_id": "PV-YYYY-MMDD-NNN",

  "assumption_mapping": [
    {
      "assumption": "string",
      "type": "value|growth|usability|viability",
      "risk_level": "high|medium|low",
      "testable": true,
      "priority": "number"
    }
  ],

  "mvp_design": {
    "type": "landing_page|wizard_of_oz|concierge|piecemeal|prototype",
    "features": ["string"],
    "scope": "string",
    "timeline": "string",
    "budget": "string"
  },

  "customer_discovery": {
    "interview_guide": {
      "target_users": "string",
      "interview_questions": ["string"],
      "red_flags": ["string"]
    },
    "validation_experiments": [
      {
        "experiment": "string",
        "method": "string",
        "success_criteria": "string",
        "timeline": "string"
      }
    ]
  },

  "pmf_metrics": {
    "primary_metric": "string",
    "secondary_metrics": ["string"],
    "pmf_thresholds": {
      "score_4_5": "number — 认为非常失望的比例",
      "retention": "number — 月留存率",
      "nps": "number — 净推荐值"
    }
  },

  "iteration_plan": {
    "build_measure_learn_cycles": [
      {
        "cycle": "number",
        "hypothesis": "string",
        "experiment": "string",
        "success_criteria": "string"
      }
    ],
    "pivot_or_persevere_criteria": "string"
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

### Step 1: 假设识别

- **输入**：`product_idea` + `assumptions`
- **动作**：
  1. 识别关键假设
  2. 分类假设类型
  3. 评估风险等级
- **输出**：`assumption_mapping`
- **假设类型**：

| 类型 | 描述 | 示例 |
|------|------|------|
| 价值假设 | 客户是否需要 | 用户愿意付费 |
| 增长假设 | 如何获客 | 口碑传播 |
| 可用性假设 | 产品是否好用 | 用户能完成任务 |
| 可行性假设 | 业务是否可行 | 能盈利 |

### Step 2: MVP 设计

- **输入**：`assumption_mapping`
- **动作**：
  1. 选择 MVP 类型
  2. 定义核心功能
  3. 设计开发计划
- **输出**：`mvp_design`
- **MVP 类型选择**：

| 类型 | 描述 | 适用场景 |
|------|------|----------|
| 落地页 | 单页网站测试需求 | 早期验证 |
| 乌兹别克 | 人工模拟产品 | 验证价值 |
| 走廊测试 | 手动服务少量用户 | 验证可用性 |
| 原型 | 可交互原型 | 验证设计 |

### Step 3: 客户开发

- **输入**：`assumption_mapping` + `target_market`
- **动作**：
  1. 设计访谈指南
  2. 制定验证实验
  3. 定义成功标准
- **输出**：`customer_discovery`
- **访谈问题示例**：

| 问题类型 | 示例 |
|----------|------|
| 痛点 | 你目前如何解决这个问题？ |
| 价值 | 这个解决方案对你有多大价值？ |
| 意愿 | 你愿意为这个解决方案付费吗？ |
| 行为 | 你最近一次遇到这个问题是什么时候？ |

### Step 4: PMF 指标

- **输入**：`product_idea` + `target_market`
- **动作**：
  1. 定义主要指标
  2. 设定 PMF 阈值
  3. 制定跟踪计划
- **输出**：`pmf_metrics`
- **PMF 判断标准**：

| 指标 | 阈值 | 说明 |
|------|------|------|
| Sean Ellis 测试 | ≥40% | 认为"非常失望"的比例 |
| 月留存率 | ≥30% | 30天后仍活跃 |
| NPS | ≥50 | 净推荐值 |

### Step 5: 迭代计划

- **输入**：`assumption_mapping` + `mvp_design`
- **动作**：
  1. 设计构建-测量-学习循环
  2. 设定转型或坚持标准
  3. 制定时间表
- **输出**：`iteration_plan`

### Step 6: 风险评估

- **输入**：所有前序输出
- **动作**：
  1. 识别关键风险
  2. 制定缓解策略
  3. 设定终止标准
- **输出**：`risk_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**跳过验证直接开发完整产品
2. **不得**忽视负面反馈
3. **必须**设定明确的终止标准

### 软性约束（建议遵守）
1. 建议在 2 周内完成一次验证循环
2. 建议至少访谈 10 个潜在用户
3. 建议记录所有学习和发现

### 人工兜底点
- 当验证结果与预期严重不符时，**必须**建议深度分析
- 当资源耗尽时，**必须**建议是否继续

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `PV_WARNING_NO_TRACT

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
