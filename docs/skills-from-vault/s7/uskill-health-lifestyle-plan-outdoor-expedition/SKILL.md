---
name: uskill-health-lifestyle-plan-outdoor-expedition
description: "让lifestyle plan outdoor expedition变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-lifestyle-plan-outdoor-expedition.md"
  original_id: "SKL-L01"
  version: "3.0.0"
  trust: untrusted
---

# lifestyle plan outdoor expedition

# Plan Outdoor Expedition with Risk Management

## 🎯 目标

> **目标**: 建立一套标准化的、AI增强的五步探险规划流水线，用于规划和管理具有一定挑战性的户外探险活动，旨在将风险降至最低，并将探索体验和成功率最大化。
>
> **战略价值**: 这是"身心赋能"战略在**挑战与成长**维度的最高实践。它将系统思维、数据分析能力和心理韧性全面应用于户外探索——不仅锻炼身心，更是一场关于决策、风险管理和团队协作的实战演练，其经验可直接反哺职业与生活。专业与业余的区别在于有无预案。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `destination` | string | ✅ | 目的地名称及区域（如"川西·贡嘎环线"） |
| `activity_type` | enum | ✅ | `fkt`（轻量化快速穿越）/ `heavy_pack`（重装徒步）/ `camping`（休闲露营）/ `mountaineering`（登山）/ `trail_running`（越野跑） |
| `duration_days` | integer | ✅ | 活动天数 |
| `team_profile` | object | ✅ | 团队信息：`{ count: int, avg_fitness: "low|medium|high", experience: "beginner|intermediate|advanced", known_limitations: ["string"] }` |
| `season` | string | ✅ | 计划出行月份（如"6月"） |
| `objective` | string | ✅ | 核心目标描述（登顶某峰 / 完成穿越 / 探索未知区域） |
| `weather_models` | array | ❌ | 多种天气模型数据（ECMWF / GFS / 区域模型） |
| `existing_gpx_tracks` | array | ❌ | 已有的他人 GPX 轨迹（WKT / GeoJSON 格式） |
| `recent_trip_reports` | string | ❌ | 近期山友游记或社交媒体路况信息 |
| `constraints` | object | ❌ | 约束条件：`{ budget: int, transport: "string", special_limits: ["string"] }` |
| `stage` | enum | ✅ | `feasibility` / `intel` / `route_design` / `resources` / `publish` — 当前所处规划阶段 |

## 📤 输出

```json
{
  "stage": "feasibility | intel | route_design | resources | publish",
  "feasibility_report": {
    "rating": "recommended | cautious | not_recommended",
    "seasonal_risks": ["string — 如天气、地质、野生动物风险"],
    "team_strengths": ["string"],
    "team_weaknesses": ["string — 体能/技能短板"],
    "min_fitness_requirement": "string",
    "min_skills_required": ["string"],
    "rationale": "string — 评级理由"
  },
  "intel_report": {
    "gpx_analysis": {
      "main_route_consensus": "string — 多轨迹重合的主路线描述",
      "key_fork_points": [{ "name": "string", "lat": "float", "lng": "float", "note": "string" }],
      "water_sources": [{ "name": "string", "lat": "float", "lng": "float", "reliability": "seasonal|permanent|unknown" }],
      "camp_sites": [{ "name": "string", "lat": "float", "lng": "float", "capacity": "int" }]
    },
    "weather_forecast": {
      "72h_summary": "string",
      "critical_risks": ["string — 如失温、雷暴、暴风雪"],
      "wind_chill_factor": "string",
      "precipitation_probability": "string"
    },
    "trail_conditions": "string — 来自游记的最新路况"
  },
  "route_plan": {
    "plan_a": {
      "name": "string — 主路线名称",
      "waypoints": [
        {
          "name": "string",
          "lat": "float",
          "lng": "float",
          "elevation_m": "int",
          "type": "start|pass|water|camp|summit|decision_point|end",
          "note": "string"
        }
      ],
      "daily_schedule": [
        {
          "day": "int",
          "segment": "string — 如 '营地A → 垭口B'",
          "distance_km": "float",
          "elevation_gain_m": "int",
          "elevation_loss_m": "int",
          "estimated_hours": "float"
        }
      ],
      "total_distance_km": "float",
      "total_elevation_gain_m": "int"
    },
    "plan_b_backup": {
      "description": "string — 备用路线说明",
      "trigger_condition": "string — 何时启用",
      "route_summary": "string"
    },
    "plan_c_bailout": [
      {
        "decision_point": "string — 如'下午2点前未到XX垭口'",
        "trigger": "string — 具体触发条件",
        "bailout_route": "string — 下撤路线描述",
        "estimated_exit_hours": "float"
      }
    ],
    "ai_review_notes": ["string — AI向导审查发现的风险点"]
  },
  "gear_list": {
    "personal": [
      { "item": "string", "weight_g": "int", "essential": true, "category": "clothing|navigation|safety|sleep|cooking|hygiene" }
    ],
    "shared": [
      { "item": "string", "weight_g": "int", "essential": true, "assigned_to": "string" }
    ],
    "total_personal_weight_kg": "float",
    "total_shared_weight_kg": "float",
    "lightweight_check_passed": "boolean"
  },
  "supply_plan": {
    "food": { "cal_per_day": "int", "total_cal": "int", "menu_summary": "string" },
    "water": { "liters_per_day": "float", "purification_method": "string", "

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
