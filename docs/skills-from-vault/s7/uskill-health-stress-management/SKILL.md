---
name: uskill-health-stress-management
description: "让压力管理变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-stress-management.md"
  original_id: "SKL-6819"
  version: "3.0.0"
  trust: untrusted
---

# 压力管理

description: |
  当用户需要识别压力源、管理压力反应、建立应对策略、预防倦怠时使用此 Skill。
  触发词包括：'压力'、'焦虑'、'倦怠'、'压力管理'、'应对压力'、
  '压力源'、'压力反应'、'恢复'。当用户讨论疲劳、焦虑、工作压力、
  生活压力时，即使未直接说"压力管理"，也应使用此 Skill。
  不适用于严重心理问题（建议就医）。遇到压力管理需求时优先使用。

---

# uSkill-302: 压力管理

## 🎯 目标

> 识别压力源，管理压力反应，建立健康的应对策略，预防慢性压力和倦怠。

**核心价值**：适度压力是动力，过度压力是毒药。学会管理压力是可持续发展的关键。

**适用场景**：
- 工作压力管理
- 学业压力应对
- 人际关系压力
- 财务压力
- 生活变故应对

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `stress_description` | `string` | ✅ | — | 压力情况描述 |
| `stress_level` | `number` | ❌ | `5` | 压力水平 1-10 |
| `duration` | `enum` | ❌ | `acute` | `acute` / `chronic` |
| `physical_symptoms` | `array` | ❌ | `[]` | 身体症状 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话压力管理建议",
  "stress_id": "ST-YYYY-MMDD-NNN",

  "stress_assessment": {
    "stressors_identified": [
      {
        "source": "string",
        "type": "work|relationship|financial|health|other",
        "controllability": "high|medium|low",
        "severity": "low|medium|high"
      }
    ],
    "stress_level": "number",
    "stress_type": "acute|chronic",
    "physical_impact": ["string"],
    "emotional_impact": ["string"]
  },

  "coping_strategies": {
    "immediate": [
      {
        "technique": "string",
        "description": "string",
        "effectiveness": "high|medium|low",
        "time_required": "string"
      }
    ],
    "short_term": ["string"],
    "long_term": ["string"]
  },

  "stress_reduction_plan": {
    "daily_practices": ["string"],
    "weekly_practices": ["string"],
    "lifestyle_changes": ["string"]
  },

  "support_system": {
    "professional_help": "boolean",
    "social_support": ["string"],
    "resources": ["string"]
  },

  "monitoring_plan": {
    "daily_checks": ["string"],
    "weekly_reviews": ["string"],
    "red_flags": ["string"]
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

### Step 1: 压力评估

- **输入**：`stress_description` + `stress_level`
- **动作**：
  1. 识别具体压力源
  2. 评估压力水平
  3. 分析影响范围
- **输出**：`stress_assessment`
- **压力评估维度**：

| 维度 | 评估内容 |
|------|----------|
| 来源 | 工作/关系/财务/健康 |
| 可控性 | 可控/部分可控/不可控 |
| 持续时间 | 急性/慢性 |
| 影响程度 | 轻度/中度/重度 |

### Step 2: 应对策略生成

- **输入**：`stress_assessment`
- **动作**：
  1. 生成即时应对策略
  2. 制定短期改善计划
  3. 规划长期预防措施
- **输出**：`coping_strategies`
- **即时应对技术**：

| 技术 | 描述 | 时间 |
|------|------|------|
| 深呼吸 | 4-7-8 呼吸法 | 2 分钟 |
| 渐进式肌肉放松 | 从脚到头逐步放松 | 10 分钟 |
| 正念冥想 | 专注当下 | 5-10 分钟 |
| 身体活动 | 散步或运动 | 15-30 分钟 |

### Step 3: 压力减少计划

- **输入**：`coping_strategies`
- **动作**：
  1. 制定每日实践
  2. 制定每周实践
  3. 规划生活方式改变
- **输出**：`stress_reduction_plan`

### Step 4: 支持系统

- **输入**：`stress_assessment`
- **动作**：
  1. 评估是否需要专业帮助
  2. 识别社会支持资源
  3. 提供相关资源
- **输出**：`support_system`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议忽视严重压力症状
2. **不得**替代专业心理治疗
3. **必须**在必要时建议就医

### 软性约束（建议遵守）
1. 建议记录压力日记
2. 建议建立日常减压习惯
3. 建议定期评估压力水平

### 人工兜底点
- 当出现严重焦虑或抑郁症状时，**必须**建议就医
- 当压力导致身体症状时，**必须**建议专业评估

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `ST_WARNING_CHRONIC` | 慢性压力 | 建议加强干预 | 🟡 |
| `ST_WARNING_SEVERE` | 压力水平 > 8 | 建议专业帮助 | 🔴 |
| `ST_ERROR_CRISIS` | 危机状态 | 建议立即求助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 压力源已识别
- [ ] 应对策略已生成
- [ ] 减压计划已制定
- [ ] 支持系统已评估

### OVP 验证信号
- 压力管理有效性 ≥ 75%
- 应对策略采纳率 ≥ 70%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "工作压力",
    "prompt": "我工作压力很大，经常加班到很晚",
    "context": "stress_level=7, type=chronic",
    "assertions": [
      "stress_assessment.stressors_identified 包含 工作",
      "coping_strategies.immediate 包含 即时技术",
      "stress_reduction_plan 包含 工作边界建议"
    ],
    "expected_behavior": "识别工作压力，提供应对策略",
    "critic_attack": "是否考虑了工作性质的影响？"
  },
  {
    "id": "test-002",
    "name": "急性压力",
    "prompt": "明天有个重要演讲，我现在很紧张",
    "context": "stress_level=6, type=acute",
    "assertions": [
      "stress_as

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
