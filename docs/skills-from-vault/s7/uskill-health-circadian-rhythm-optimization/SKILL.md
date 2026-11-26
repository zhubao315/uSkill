---
name: uskill-health-circadian-rhythm-optimization
description: "让生物节律优化变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-circadian-rhythm-optimization.md"
  original_id: "SKL-6820"
  version: "3.0.0"
  trust: untrusted
---

# 生物节律优化

description: |
  当用户需要调节昼夜节律、管理精力分配、调整时差、应对季节性情绪波动时使用此 Skill。
  触发词包括：'生物钟'、'昼夜节律'、'倒时差'、'精力管理'、'倒班工作'、
  '季节性情绪'、'时差调整'、'节律紊乱'、'晨型夜型'。当用户讨论作息调整、
  精力低谷、跨时区旅行时，即使未直接说"生物节律优化"，也应使用此 Skill。
  不适用于临床睡眠障碍治疗。遇到节律管理需求时优先使用。

---

# uSkill-307: 生物节律优化

## 🎯 目标

> 基于昼夜节律科学，帮助用户调节生物钟、优化精力分配、应对时差和季节性变化，实现生理节律与生活节奏的最佳匹配。

**核心价值**：生物节律是精力的底层操作系统，优化节律能系统性提升认知表现和身体健康。

**适用场景**：
- 倒班工作节律适应
- 跨时差旅行调整
- 精力低谷期管理
- 季节性情绪波动应对
- 晨型/夜型节律重塑

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `concern_type` | `enum` | ✅ | — | 核心问题：jet_lag/shift_work/energy_dip/sadian/rhythm_reset |
| `current_schedule` | `object` | ❌ | — | 当前作息时间（起床、入睡、工作时段） |
| `chronotype` | `enum` | ❌ | `"unknown"` | 时间类型：morning/evening/intermediate/unknown |
| `travel_details` | `object` | ❌ | — | 时差调整时必填：出发地、目的地、时差小时数 |
| `work_constraint` | `object` | ❌ | — | 工作时间硬约束（如轮班表） |
| `light_exposure` | `object` | ❌ | — | 当前光照环境（室内时长、户外时长） |
| `supplements` | `array` | ❌ | `[]` | 正在使用的补充剂（褪黑素、维生素D等） |

**输入约束**：
- `concern_type` = jet_lag 时 `travel_details` 必填
- `travel_details.time_diff` 范围为 -12 到 +12 小时
- `current_schedule` 时间格式为 HH:MM
- 输入数据来源：用户描述 + 可选穿戴设备数据

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话节律优化摘要",
  "plan_id": "BIO-YYYY-MMDD-NNN",

  "rhythm_assessment": {
    "chronotype_detected": "morning|evening|intermediate",
    "current_alignment_score": "number — 0-100",
    "misalignment_areas": ["string"],
    "root_causes": ["string"]
  },

  "circadian_protocol": {
    "light_protocol": {
      "morning_light": {
        "timing": "string",
        "duration": "string",
        "intensity": "string",
        "method": "string"
      },
      "evening_dimming": {
        "timing": "string",
        "blue_light_filter": "boolean",
        "dark_room_protocol": "string"
      }
    },
    "meal_timing": {
      "first_meal": "string",
      "last_meal": "string",
      "fasting_window": "string",
      "caffeine_cutoff": "string"
    },
    "exercise_timing": {
      "optimal_window": "string",
      "avoid_window": "string",
      "intensity_by_time": "string"
    },
    "sleep_window": {
      "target_bedtime": "string",
      "target_wake_time": "string",
      "consistency_rule": "string"
    }
  },

  "jet_lag_protocol": {
    "pre_adjustment_days": "number",
    "hourly_schedule": [
      {
        "day": "number",
        "time": "string",
        "action": "string",
        "rationale": "string"
      }
    ],
    "melatonin_guide": {
      "timing": "string",
      "dosage": "string",
      "duration": "string"
    },
    "arrival_strategy": "string"
  },

  "energy_management": {
    "peak_hours": ["string"],
    "trough_hours": ["string"],
    "strategic_napping": {
      "recommended": "boolean",
      "timing": "string",
      "duration": "string"
    },
    "energy_boosters": ["string"],
    "energy_drains": ["string"]
  },

  "seasonal_support": {
    "light_therapy": {
      "recommended": "boolean",
      "timing": "string",
      "duration": "string",
      "lux_requirement": "string"
    },
    "outdoor_exposure_target": "string",
    "vitamin_d_consideration": "string",
    "mood_tracking_suggestion": "string"
  },

  "monitoring_plan": {
    "daily_metrics": ["string"],
    "weekly_review": ["string"],
    "adjustment_triggers": ["string"],
    "red_flags": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

### 异常输出

```json
{
  "status": "failed",
  "error_code": "BIO_ERROR_XXX",
  "error_message": "string — 错误描述",
  "suggestion": "string — 修复建议"
}
```

---

## 📋 执行步骤

### Step 1: 节律状态评估

- **输入**：全部输入参数
- **动作**：
  1. 分析当前作息与理想节律的偏差
  2. 识别 chronotype（若未知则通过问题推断）
  3. 评估 misalignment 严重程度
- **输出**：`rhythm_assessment`
- **分支条件**：
  - IF `chronotype` = unknown → 通过 3 个诊断问题推断：最佳起床时间、精力高峰时段、周末自然醒时间
  - IF `current_schedule` 未提供 → 要求用户提供典型一日作息
  - IF `misalignment_areas` > 3 个 → 标记为高优先级
  - ELSE → 直接评估

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
