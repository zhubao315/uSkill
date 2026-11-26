---
name: uskill-growth-mindset
description: "让成长心态变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-growth-mindset.md"
  original_id: "SKL-6896"
  version: "3.0.0"
  trust: untrusted
---

# 成长心态

description: |
  当用户需要建立成长心态、克服固定心态、从失败中学习、提升韧性时使用此 Skill。
  触发词包括：'成长心态'、'固定心态'、'韧性'、'失败学习'、'自我成长'。
  当用户讨论个人发展、学习、挑战时，
  即使未直接说"成长心态"，也应使用此 Skill。
  不适用于严重心理问题（建议专业帮助）。遇到心态调整需求时优先使用。

---

# uSkill-1001: 成长心态

## 🎯 目标

> 帮助用户从固定心态转变为成长心态，提升学习能力和韧性。

**核心价值**：心态决定行为。成长心态是持续进步的基础。

**适用场景**：
- 克服失败恐惧
- 接受新挑战
- 从批评中学习
- 提升学习效果
- 职业发展

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_situation` | `string` | ✅ | — | 当前情况描述 |
| `mindset_indicators` | `object` | ❌ | — | 心态指标 |
| `growth_goals` | `array` | ❌ | `[]` | 成长目标 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话成长建议",
  "growth_id": "GM-YYYY-MMDD-NNN",

  "mindset_assessment": {
    "current_mindset": "fixed|growth|mixed",
    "indicators": {
      "challenge_response": "avoids|embraces",
      "failure_response": "gives_up|persists",
      "criticism_response": "defensive|learns",
      "success_response": "threatened|inspired"
    },
    "areas_for_growth": ["string"]
  },

  "mindset_shift_strategies": {
    "awareness_building": {
      "triggers": ["string"],
      "reframing_techniques": ["string"],
      "self_talk_adjustments": ["string"]
    },
    "behavioral_experiments": [
      {
        "experiment": "string",
        "purpose": "string",
        "success_criteria": "string"
      }
    ],
    "environment_design": {
      "support_systems": ["string"],
      "challenge_sources": ["string"],
      "learning_resources": ["string"]
    }
  },

  "failure_recovery_framework": {
    "immediate_response": ["string"],
    "analysis_process": ["string"],
    "learning_extraction": ["string"],
    "forward_planning": ["string"]
  },

  "growth_practices": {
    "daily": ["string"],
    "weekly": ["string"],
    "monthly": ["string"]
  },

  "progress_tracking": {
    "metrics": ["string"],
    "milestones": [
      {
        "milestone": "string",
        "timeline": "string",
        "success_criteria": "string"
      }
    ]
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

### Step 1: 心态评估

- **输入**：`current_situation` + `mindset_indicators`
- **动作**：
  1. 评估当前心态类型
  2. 识别关键指标
  3. 确定成长领域
- **输出**：`mindset_assessment`
- **固定心态 vs 成长心态**：

| 维度 | 固定心态 | 成长心态 |
|------|----------|----------|
| 挑战 | 回避 | 拥抱 |
| 失败 | 放弃 | 坚持 |
| 批评 | 防御 | 学习 |
| 成功 | 威胁 | 启发 |
| 努力 | 无用 | 必要 |

### Step 2: 心态转变策略

- **输入**：`mindset_assessment`
- **动作**：
  1. 建立觉察
  2. 设计行为实验
  3. 设计支持环境
- **输出**：`mindset_shift_strategies`
- **心态转变技术**：

| 技术 | 描述 | 应用 |
|------|------|------|
| 觉察触发 | 识别固定心态时刻 | 日常观察 |
| 重构思维 | 用成长视角重新解读 | 自我对话 |
| 行为实验 | 尝试新的行为模式 | 刻意练习 |
| 环境设计 | 创造支持成长的环境 | 周围人和支持 |

### Step 3: 失败恢复框架

- **输入**：`mindset_assessment`
- **动作**：
  1. 设计即时应对
  2. 设计分析流程
  3. 设计学习提取
- **输出**：`failure_recovery_framework`

### Step 4: 成长实践

- **输入**：`mindset_shift_strategies`
- **动作**：
  1. 设计日常练习
  2. 安排每周练习
  3. 规划每月回顾
- **输出**：`growth_practices`

### Step 5: 进度跟踪

- **输入**：`growth_goals`
- **动作**：
  1. 定义跟踪指标
  2. 设定里程碑
  3. 制定回顾计划
- **输出**：`progress_tracking`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**强迫用户接受成长心态
2. **不得**忽视真实困难
3. **必须**尊重个体差异

### 软性约束（建议遵守）
1. 建议从小改变开始
2. 建议保持耐心
3. 建议寻找支持伙伴

### 人工兜底点
- 当存在严重心理问题时，**必须**建议专业帮助
- 当改变困难时，**必须**建议寻求支持

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `GM_WARNING_RESISTANCE` | 强烈抵抗 | 建议放慢速度 | 🟡 |
| `GM_WARNING_SETBACK` | 倒退 | 正常化，继续前进 | 🟡 |
| `GM_ERROR_CRISIS` | 严重心理问题 | 建议专业帮助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 心态已评估
- [ ] 转变策略已设计
- [ ] 失败恢复框架已制定
- [ ] 成长实践已安排

### OVP 验证信号
- 挑战接受率提升 ≥ 30%
- 失败后恢复时间缩短 ≥ 25%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "职业挑战",
    "prompt": "我害怕接受新项目，怕失败",
    "context": "current_situation=职业挑战, mindset_indicators={challenge_response:avoids}",
    "assertions": [
      "mindset_assessment.current_mindset = fixed

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
