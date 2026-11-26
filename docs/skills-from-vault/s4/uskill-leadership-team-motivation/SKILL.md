---
name: uskill-leadership-team-motivation
description: "让团队激励变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-leadership-team-motivation.md"
  original_id: "SKL-5402"
  version: "3.0.0"
  trust: untrusted
---

# 团队激励

description: |
  当用户需要激励团队、建立心理安全感、激发内在动机、提升团队敬业度时使用此 Skill。
  触发词包括：'团队激励'、'员工激励'、'敬业度'、'内在动机'、'心理安全'、
  '团队士气'、'激励策略'。当用户讨论团队管理、员工发展、组织文化时，
  即使未直接说"团队激励"，也应使用此 Skill。
  不适用于个人自我激励（使用其他 Skill）。遇到团队激励需求时优先使用。

---

# uSkill-402: 团队激励

## 🎯 目标

> 基于自我决定理论，建立激发内在动机的团队环境，提升团队敬业度和绩效。

**核心价值**：真正的激励来自内在，而非外在奖惩。领导者的核心任务是创造激发内在动机的环境。

**适用场景**：
- 团队士气低落
- 员工敬业度下降
- 新团队组建
- 变革期激励
- 高绩效团队建设

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `team_context` | `string` | ✅ | — | 团队情况描述 |
| `current_challenges` | `array` | ❌ | `[]` | 当前挑战 |
| `team_size` | `number` | ❌ | `10` | 团队规模 |
| `industry` | `string` | ❌ | `tech` | 行业类型 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话团队激励建议",
  "motivation_id": "TM-YYYY-MMDD-NNN",

  "team_assessment": {
    "current_state": "disengaged|neutral|engaged|high_performing",
    "key_challenges": ["string"],
    "motivation_level": "low|medium|high",
    "psychological_safety": "low|medium|high"
  },

  "intrinsic_motivation_analysis": {
    "autonomy": {
      "current_level": "low|medium|high",
      "improvement_areas": ["string"]
    },
    "mastery": {
      "current_level": "low|medium|high",
      "improvement_areas": ["string"]
    },
    "purpose": {
      "current_level": "low|medium|high",
      "improvement_areas": ["string"]
    }
  },

  "motivation_strategies": {
    "immediate_actions": [
      {
        "action": "string",
        "target": "autonomy|mastery|purpose",
        "implementation": "string",
        "expected_impact": "string"
      }
    ],
    "medium_term_initiatives": ["string"],
    "long_term_culture_changes": ["string"]
  },

  "psychological_safety_plan": {
    "assessment_method": "string",
    "improvement_strategies": ["string"],
    "metrics": ["string"]
  },

  "recognition_framework": {
    "types_of_recognition": ["string"],
    "frequency": "string",
    "personalization": "string"
  },

  "monitoring_plan": {
    "engagement_metrics": ["string"],
    "review_frequency": "string",
    "feedback_mechanisms": ["string"]
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

### Step 1: 团队状态评估

- **输入**：`team_context` + `current_challenges`
- **动作**：
  1. 评估当前团队状态
  2. 识别关键挑战
  3. 测量激励水平
- **输出**：`team_assessment`
- **团队状态指标**：

| 状态 | 特征 | 干预重点 |
|------|------|----------|
| 脱离 | 缺乏动力、消极 | 基础需求满足 |
| 中性 | 完成任务但无热情 | 激发内在动机 |
| 投入 | 主动积极、有热情 | 保持和深化 |
| 高绩效 | 超越期望、创新 | 挑战和成长 |

### Step 2: 内在动机分析

- **输入**：`team_assessment`
- **动作**：
  1. 评估自主性需求
  2. 评估胜任感需求
  3. 评估归属感需求
- **输出**：`intrinsic_motivation_analysis`
- **自我决定理论（SDT）**：

| 需求 | 描述 | 满足方式 |
|------|------|----------|
| 自主性 | 控制自己工作的能力 | 授权、选择权 |
| 胜任感 | 感觉自己有能力 | 挑战、反馈 |
| 归属感 | 与他人连接 | 团队活动、认可 |

### Step 3: 激励策略生成

- **输入**：`intrinsic_motivation_analysis`
- **动作**：
  1. 生成即时行动
  2. 制定中期计划
  3. 规划长期文化
- **输出**：`motivation_strategies`

### Step 4: 心理安全建设

- **输入**：`team_assessment`
- **动作**：
  1. 评估心理安全水平
  2. 制定提升策略
  3. 设定监控指标
- **输出**：`psychological_safety_plan`
- **心理安全建设策略**：

| 策略 | 描述 |
|------|------|
| 承认错误 | 领导者先承认自己的错误 |
| 欢迎提问 | 鼓励团队成员提问 |
| 包容失败 | 将失败视为学习机会 |
| 尊重差异 | 尊重不同观点和背景 |

### Step 5: 认可框架

- **输入**：`intrinsic_motivation_analysis`
- **动作**：
  1. 设计认可类型
  2. 确定频率
  3. 个性化方案
- **输出**：`recognition_framework`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**仅依赖外在激励（奖金、惩罚）
2. **不得**忽视个体差异
3. **必须**建立长期文化而非短期刺激

### 软性约束（建议遵守）
1. 建议定期进行员工满意度调查
2. 建议一对一沟通了解个体需求
3. 建议将激励融入日常工作

### 人工兜底点
- 当团队出现严重士气问题时，**必须**进行深度诊断
- 当核心员工有离职风险时，**必须**立即干预

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `TM_WARNING_LOW_SAFETY` | 心理安全水平低 | 建议优先建设安全 | 🟡 |
| `TM_WARNING_BURNOUT` | 团队倦怠迹象 | 建议减负和恢复 | 🟡 |
| `TM_ERROR_CRISIS` | 团队危机状态 | 建议立即干预 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 团队状态已评估
- [ ] 内在动机已分析
- [ ] 激励策略已生成
- [ ] 心理安全计划已制定

### OVP 验证信号
- 团队敬业度 ≥ 80%
- 员工满意度 ≥

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
