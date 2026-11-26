---
name: uskill-leadership-decision-making
description: "让决策领导力变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-leadership-decision-making.md"
  original_id: "SKL-5401"
  version: "3.0.0"
  trust: untrusted
---

# 决策领导力

description: |
  当用户需要在不确定性中做决策、平衡多方利益、快速果断决策、承担决策责任时使用此 Skill。
  触发词包括：'领导力决策'、'管理决策'、'战略决策'、'团队决策'、
  '快速决策'、'果断决策'。当用户讨论团队管理、组织决策、战略选择时，
  即使未直接说"决策领导力"，也应使用此 Skill。
  不适用于个人决策（使用决策推理 Skill）。遇到团队或组织决策时优先使用。

---

# uSkill-401: 决策领导力

## 🎯 目标

> 帮助领导者在不确定性中做出高质量决策，平衡速度与质量，承担决策责任。

**核心价值**：领导力的核心是决策力。好的领导者能在信息不完整时做出正确判断。

**适用场景**：
- 战略方向选择
- 资源分配决策
- 人事任免决策
- 危机应对决策
- 创新项目决策

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `decision_context` | `string` | ✅ | — | 决策背景描述 |
| `stakeholders` | `array` | ✅ | — | 利益相关者列表 |
| `time_pressure` | `enum` | ❌ | `medium` | `low` / `medium` / `high` / `critical` |
| `information_completeness` | `number` | ❌ | `0.7` | 信息完整度 0-1 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话决策建议",
  "leadership_id": "LD-YYYY-MMDD-NNN",

  "decision_framework": {
    "framework_used": "string",
    "rationale": "string"
  },

  "stakeholder_analysis": [
    {
      "stakeholder": "string",
      "interest": "high|medium|low",
      "influence": "high|medium|low",
      "position": "support|neutral|oppose",
      "engagement_strategy": "string"
    }
  ],

  "options_analysis": [
    {
      "option": "string",
      "pros": ["string"],
      "cons": ["string"],
      "risks": ["string"],
      "resource_requirements": "string",
      "alignment_with_values": "high|medium|low"
    }
  ],

  "decision_output": {
    "recommended_option": "string",
    "decision_rationale": "string",
    "confidence_level": "number",
    "conditions_for_reversal": ["string"]
  },

  "implementation_plan": {
    "immediate_actions": ["string"],
    "communication_plan": ["string"],
    "monitoring_metrics": ["string"],
    "check_in_schedule": "string"
  },

  "risk_mitigation": {
    "identified_risks": ["string"],
    "mitigation_strategies": ["string"],
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

### Step 1: 决策框架选择

- **输入**：`decision_context` + `time_pressure`
- **动作**：
  1. 评估决策类型
  2. 选择合适的决策框架
  3. 确定决策标准
- **输出**：`decision_framework`
- **决策框架选择**：

| 情境 | 框架 | 适用条件 |
|------|------|----------|
| 时间充裕 | 贝叶斯决策 | 信息可量化 |
| 时间紧迫 | 直觉+验证 | 需要快速决策 |
| 利益冲突 | 协作决策 | 多方参与 |
| 高风险 | 预验尸法 | 需要识别风险 |

### Step 2: 利益相关者分析

- **输入**：`stakeholders`
- **动作**：
  1. 识别所有利益相关者
  2. 评估其利益和影响力
  3. 制定参与策略
- **输出**：`stakeholder_analysis`
- **利益相关者矩阵**：

| | 高影响力 | 低影响力 |
|---|:---:|:---:|
| **高利益** | 密切合作 | 保持知情 |
| **低利益** | 满足需求 | 监控即可 |

### Step 3: 选项分析

- **输入**：`decision_framework`
- **动作**：
  1. 生成至少 3 个选项
  2. 评估每个选项的优劣
  3. 评估风险和资源需求
- **输出**：`options_analysis`

### Step 4: 决策输出

- **输入**：`options_analysis` + `stakeholder_analysis`
- **动作**：
  1. 综合评估
  2. 做出推荐
  3. 明确决策依据
- **输出**：`decision_output`

### Step 5: 实施计划

- **输入**：`decision_output`
- **动作**：
  1. 制定立即行动清单
  2. 制定沟通计划
  3. 设定监控指标
- **输出**：`implementation_plan`

### Step 6: 风险缓解

- **输入**：`options_analysis`
- **动作**：
  1. 识别潜在风险
  2. 制定缓解策略
  3. 准备应急计划
- **输出**：`risk_mitigation`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在信息严重不足时强行决策
2. **不得**忽视主要利益相关者
3. **必须**明确决策依据和可逆条件

### 软性约束（建议遵守）
1. 建议在决策前征求至少 2 个不同意见
2. 建议设定决策回顾时间点
3. 建议记录决策过程以便复盘

### 人工兜底点
- 当涉及重大战略决策时，**必须**建议董事会或顾问参与
- 当决策可能导致重大损失时，**必须**建议压力测试

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `LD_WARNING_LOW_INFO` | 信息完整度 < 50% | 建议收集更多信息 | 🟡 |
| `LD_WARNING_CONFLICT` | 利益相关者严重冲突 | 建议协调或升级 | 🟡 |
| `LD_ERROR_CRITICAL` | 关键决策 + 高风险 | 建议外部咨询 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 决策框架已选择
- [ ] 利益相关者已分析
- [ ] 选项已生成并评估
- [ ] 实施计划已制定

### OVP 验证信号
- 决策质量评分 ≥ 80/100
- 利益相关者满意度 ≥ 75%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "战略方向选择",
    "prompt": "我们是应该进入新市场还是深耕现有市场？",
    "context": "stakeholders=[股东、员工、客户], time_pressure=medium",
    "assertions": [
      "decision_framework 已选择",
 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
