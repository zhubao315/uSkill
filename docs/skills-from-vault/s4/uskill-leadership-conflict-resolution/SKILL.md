---
name: uskill-leadership-conflict-resolution
description: "让冲突管理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-leadership-conflict-resolution.md"
  original_id: "SKL-5403"
  version: "3.0.0"
  trust: untrusted
---

# 冲突管理

description: |
  当用户需要解决团队冲突、处理人际矛盾、进行艰难对话、调解分歧时使用此 Skill。
  触发词包括：'冲突'、'矛盾'、'争执'、'调解'、'艰难对话'、'分歧'、
  '团队冲突'、'人际冲突'。当用户讨论团队管理、人际关系、谈判时，
  即使未直接说"冲突管理"，也应使用此 Skill。
  不适用于简单的意见分歧（直接沟通即可）。遇到需要调解的冲突时优先使用。

---

# uSkill-403: 冲突管理

## 🎯 目标

> 以协作型方式解决冲突，维护关系的同时解决问题，将冲突转化为成长机会。

**核心价值**：冲突不是坏事，处理不当才是。好的冲突管理能增强团队凝聚力。

**适用场景**：
- 团队成员间冲突
- 跨部门协作冲突
- 上下级冲突
- 客户关系冲突
- 合作伙伴关系冲突

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `conflict_description` | `string` | ✅ | — | 冲突情况描述 |
| `parties_involved` | `array` | ✅ | — | 冲突各方 |
| `conflict_type` | `enum` | ❌ | `unknown` | `task` / `relationship` / `value` / `structural` |
| `relationship_importance` | `enum` | ❌ | `high` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话冲突管理建议",
  "conflict_id": "CR-YYYY-MMDD-NNN",

  "conflict_analysis": {
    "type": "task|relationship|value|structural",
    "root_causes": ["string"],
    "escalation_level": "latent|manifest|severe",
    "emotional_intensity": "low|medium|high",
    "stakeholder_positions": [
      {
        "party": "string",
        "position": "string",
        "interests": ["string"],
        "needs": ["string"],
        "emotional_state": "string"
      }
    ]
  },

  "resolution_approach": {
    "recommended_approach": "collaborative|compromising|accommodating|avoiding|competing",
    "rationale": "string",
    "prerequisites": ["string"]
  },

  "mediation_plan": {
    "pre_mediation": ["string"],
    "opening": "string",
    "exploration_phase": ["string"],
    "problem_solving_phase": ["string"],
    "agreement_phase": ["string"]
  },

  "communication_framework": {
    "non_violent_communication": {
      "observations": "string",
      "feelings": "string",
      "needs": "string",
      "requests": "string"
    },
    "active_listening_techniques": ["string"],
    "de_escalation_strategies": ["string"]
  },

  "agreement_template": {
    "shared_understanding": "string",
    "action_items": [
      {
        "party": "string",
        "action": "string",
        "deadline": "string",
        "follow_up": "string"
      }
    ],
    "prevention_measures": ["string"]
  },

  "follow_up_plan": {
    "check_in_schedule": "string",
    "success_metrics": ["string"],
    "escalation_path": "string"
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

### Step 1: 冲突分析

- **输入**：`conflict_description` + `parties_involved`
- **动作**：
  1. 识别冲突类型
  2. 分析根本原因
  3. 评估升级程度
- **输出**：`conflict_analysis`
- **冲突类型**：

| 类型 | 特征 | 解决方向 |
|------|------|----------|
| 任务冲突 | 对工作内容/方法的分歧 | 明确目标和标准 |
| 关系冲突 | 人际间的不和 | 改善沟通和理解 |
| 价值冲突 | 价值观/信念的差异 | 寻找共同点 |
| 结构冲突 | 资源/权力的不平衡 | 调整结构或资源 |

### Step 2: 解决方案选择

- **输入**：`conflict_analysis`
- **动作**：
  1. 评估各种解决方案
  2. 选择最适合的方案
  3. 准备前提条件
- **输出**：`resolution_approach`
- **冲突解决策略**：

| 策略 | 适用情境 | 优点 | 缺点 |
|------|----------|------|------|
| 协作 | 双方利益都重要 | 双赢 | 耗时 |
| 妥协 | 需要快速解决 | 公平 | 双方都不满意 |
| 迁就 | 关系比结果重要 | 维护关系 | 可能被利用 |
| 回避 | 问题不重要 | 节省精力 | 问题可能恶化 |
| 竞争 | 紧急情况 | 快速 | 损害关系 |

### Step 3: 调解计划

- **输入**：`resolution_approach`
- **动作**：
  1. 制定调解流程
  2. 准备开场白
  3. 设计探索和解决问题阶段
- **输出**：`mediation_plan`
- **调解流程**：

| 阶段 | 目的 | 技巧 |
|------|------|------|
| 调解前 | 准备和单独沟通 | 了解各方立场 |
| 开场 | 建立安全氛围 | 设定规则 |
| 探索 | 理解各方需求 | 积极倾听 |
| 解决 | 生成解决方案 | 头脑风暴 |
| 达成 | 形成协议 | 明确细节 |

### Step 4: 沟通框架

- **输入**：`conflict_analysis`
- **动作**：
  1. 应用非暴力沟通
  2. 使用积极倾听技巧
  3. 使用降级策略
- **输出**：`communication_framework`
- **非暴力沟通（NVC）**：

| 步骤 | 内容 | 示例 |
|------|------|------|
| 观察 | 描述事实，不评判 | "我看到报告迟交了3天" |
| 感受 | 表达感受 | "我感到担心" |
| 需要 | 说明需要 | "因为我需要按时完成项目" |
| 请求 | 提出具体请求 | "你能告诉我原因并给出新时间吗？" |

### Step 5: 协议制定

- **输入**：所有前序输出
- **动作**：
  1. 总结共同理解
  2. 制定行动计划
  3. 设计预防措施
- **输出**：`agreement_template`

### Step 6: 跟进计划

- **输入**：`agreement_template`
- **动作**：
  1. 制定跟进时间表
  2. 设定成功指标
  3. 准备升级路径
- **输出**：`follow_up_plan`

---


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
