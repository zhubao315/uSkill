---
name: uskill-health-outdoor-sport-planning
description: "让户外运动规划变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-outdoor-sport-planning.md"
  original_id: "SKL-6815"
  version: "3.0.0"
  trust: untrusted
---

# 户外运动规划

description: |
  当用户需要规划户外运动路线、选择装备、评估安全风险、制定天气应对方案时使用此 Skill。
  触发词包括：'户外规划'、'徒步路线'、'骑行路线'、'露营准备'、'越野跑计划'、
  '装备清单'、'安全评估'、'天气应对'。当用户讨论出行计划、户外活动准备时，
  即使未直接说"户外运动规划"，也应使用此 Skill。
  不适用于室内运动、专业竞技赛事组织。遇到户外活动规划需求时优先使用。

---

# uSkill-306: 户外运动规划

## 🎯 目标

> 为户外运动活动提供科学的路线规划、装备选型、安全评估和天气应对方案，确保运动体验安全且高质量。

**核心价值**：将分散的户外信息整合为可执行的系统方案，降低风险、提升体验。

**适用场景**：
- 徒步旅行规划
- 骑行路线设计
- 露营活动准备
- 越野跑赛前策划
- 多日穿越行程编排

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `activity_type` | `enum` | ✅ | — | 运动类型：hike/bike/camp/trail_run/multi_day |
| `destination` | `string` | ✅ | — | 目的地或区域名称 |
| `duration` | `string` | ✅ | — | 活动时长：half_day/full_day/overnight/multi_day |
| `fitness_level` | `enum` | ❌ | `"intermediate"` | 体能等级：beginner/intermediate/advanced/expert |
| `group_size` | `number` | ❌ | `1` | 参与人数 |
| `weather_forecast` | `object` | ❌ | — | 天气预报数据（温度、降水、风力） |
| `budget` | `number` | ❌ | — | 装备预算（元） |
| `special_needs` | `array` | ❌ | `[]` | 特殊需求（如携带儿童、宠物、摄影器材） |

**输入约束**：
- `activity_type` 必须为预定义枚举值之一
- `group_size` 必须 ≥1 且 ≤30
- `fitness_level` 影响路线难度推荐上限
- 输入数据来源：用户描述 + 天气 API + 地图数据

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话户外运动规划摘要",
  "plan_id": "OUT-YYYY-MMDD-NNN",

  "route_plan": {
    "name": "string",
    "total_distance_km": "number",
    "elevation_gain_m": "number",
    "difficulty": "easy|moderate|hard|extreme",
    "estimated_time_hours": "number",
    "waypoints": [
      {
        "name": "string",
        "type": "start|rest|water|camp|end",
        "coordinates": "string",
        "notes": "string"
      }
    ],
    "alternative_routes": ["string"]
  },

  "equipment_list": {
    "essential": [
      {
        "item": "string",
        "quantity": "number",
        "reason": "string"
      }
    ],
    "recommended": ["string"],
    "weather_specific": ["string"],
    "estimated_cost": "number"
  },

  "safety_assessment": {
    "risk_level": "low|medium|high|extreme",
    "identified_risks": [
      {
        "risk": "string",
        "probability": "low|medium|high",
        "mitigation": "string"
      }
    ],
    "emergency_plan": {
      "nearest_hospital": "string",
      "emergency_contacts": ["string"],
      "evacuation_route": "string",
      "first_aid_kit": ["string"]
    },
    "communication_plan": "string"
  },

  "weather_response": {
    "current_conditions": "string",
    "forecast_48h": "string",
    "trigger_points": {
      "postpone_conditions": ["string"],
      "turn_back_conditions": ["string"],
      "shelter_seek_conditions": ["string"]
    },
    "contingency_plan": "string"
  },

  "timeline": {
    "departure": "string",
    "checkpoints": ["string"],
    "return_deadline": "string",
    "dark_hours_plan": "string"
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
  "error_code": "OUT_ERROR_XXX",
  "error_message": "string — 错误描述",
  "suggestion": "string — 修复建议"
}
```

---

## 📋 执行步骤

### Step 1: 环境与需求解析

- **输入**：全部输入参数
- **动作**：
  1. 解析运动类型和目的地信息
  2. 获取天气预报数据
  3. 评估用户体能等级与活动难度匹配度
- **输出**：`environment_profile`
- **分支条件**：
  - IF `weather_forecast` 未提供 → 调用天气 API 获取当前预报
  - IF `destination` 无法匹配已知地点 → 要求用户提供经纬度或详细描述
  - ELSE → 使用提供的天气和地点数据
- **检查点**：✅ 验证天气数据新鲜度 ≤24h，地点信息可定位

### Step 2: 路线规划

- **输入**：`environment_profile` + `activity_type` + `fitness_level`
- **动作**：
  1. 匹配推荐路线库
  2. 计算距离、爬升、预计时间
  3. 标注关键路点（水源、休息点、营地）
  4. 生成备选路线
- **输出**：`route_plan`
- **分支条件**：
  - IF `fitness_level` = beginner 且路线难度 > moderate → 降级为简化路线
  - IF `group_size` > 10 → 增加后勤保障路点
  - IF `duration` = multi_day → 插入营地和补给点
  - ELSE → 标准路线输出
- **检查点**：✅ 验证路线可通性、路点间距合理性（≤3h 步行）

### Step 3: 装备选型

- **输入**：`route_plan` + `weather_response` + `budget`
- **动作**：
  1. 按运动类型匹配基础装备清单
  2. 根据天气条件追加专项装备
  3. 预算内优先级排序
  4. 生成装备数量和替代方案
- **输出**：`equipment_list`
- **分支条件**：
  - IF `weather_response` 含降水预报 → 追加防水装备
  - IF `tempe

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
