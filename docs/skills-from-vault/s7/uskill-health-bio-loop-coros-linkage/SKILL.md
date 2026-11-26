---
name: uskill-health-bio-loop-coros-linkage
description: "Bio-Loop-Coros 联动配置"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-bio-loop-coros-linkage.md"
  original_id: ""
  version: ""
  trust: untrusted
---

# Bio-Loop-Coros 联动配置

# Bio-Loop-Coros 联动配置

> **D-B2-03 交付物** | v6.0-Graph P2 织网阶段
> **定位：** 打通 Bio-Loop Agent 与 Coros Pace 4 的双向数据流
> **验收标准：** 双向同步延迟 < 5min；成功率 ≥ 98%；断连自动重试 + 告警
> **OVP：** 硬件数据与 Obsidian 记录偏差 < 5%

---

## 一、架构总览

```
Coros Pace 4 (硬件)
    ↓ Health Connect / Coros API
Bio-Loop Agent (Loop 3)
    ├── 读取: HRV / 训练数据 / 睡眠 / 恢复指标
    ├── 写入: 训练计划调整 / 恢复周指令
    ├── 注入: bioloop-injection-{date}.md → Daily Loop
    └── 告警: HRV 跌破阈值 → Safety Claw
```

---

## 二、API 认证配置

### 2.1 Coros API 接入方式

| 方式 | 说明 | 状态 |
|------|------|:----:|
| **Health Connect** (Android) | 系统级健康数据聚合 | ✅ 已接入 |
| **Coros API** (REST) | 直接 API 调用 | ✅ 已落地（官方 `coros-mcp` 全量同步，2026-10-06）|
| **手动导出** (CSV) | 手动同步备份 | ✅ 已有 |

### 2.2 认证配置

```yaml
# Coros API 配置
coros_api:
  base_url: "https://api.coros.com"
  auth_method: "oauth2"
  client_id: "${COROS_CLIENT_ID}"
  client_secret: "${COROS_CLIENT_SECRET}"
  token_url: "https://api.coros.com/oauth/token"
  scopes:
    - "activity.read"
    - "profile.read"
    - "health.read"
  
# Health Connect 配置
health_connect:
  package: "com.google.android.apps.healthdata"
  permissions:
    - "android.permission.health.READ_HEART_RATE"
    - "android.permission.health.READ_SLEEP_SESSION"
    - "android.permission.health.READ_EXERCISE"
    - "android.permission.health.READ_SPEED"
    - "android.permission.health.READ_DISTANCE"
```

### 2.3 数据字段映射

| Coros 字段 | Health Connect 字段 | Bio-Loop 字段 | 频率 |
|-----------|-------------------|-------------|:----:|
| `heartRate` | `HeartRatePoint` | `hrv_3d_avg` | 每日 |
| `pace` | `SpeedPoint` | `today_pace` | 每次跑步 |
| `distance` | `DistancePoint` | `today_km` / `monthly_km` | 每次跑步 |
| `elevation` | `ElevationPoint` | `cumulative_elevation` | 每次跑步 |
| `sleep` | `SleepSession` | `sleep_duration` / `sleep_quality` | 每日 |
| `trainingLoad` | `—` | `training负荷` | 每次跑步 |
| `vo2max` | `—` | `vo2max` | 每周 |

### 2.4 官方 coros-mcp 字段映射（2026-10-06 全量落地）

> 官方 `coros-mcp` 已可一次拉全历史（活动/每日/睡眠），无需 Health Connect。缓存：`~/.config/coros-mcp/cache.db`；导出：`.runtime/coros/`。详版见 [[uCore-数据接入方案]] §十。

| COROS 缓存表·字段 | → Bio-Loop / state | 频率 |
|---|---|---|
| `activities.distance_meters` / `duration_seconds` / `avg_hr` / `training_load` / `avg_power` / `elevation_gain` | `today_km` / `last_run` / `load.weekly_km` | 每次运动 |
| `daily.avg_sleep_hrv` / `baseline` / `interval_list` | `hrv.d3_avg` / `baseline` / 分区 | 每日 |
| `daily.rhr` | `rhr.latest` / `avg_84d` | 每日 |
| `daily.training_load` / `training_load_ratio` / `tired_rate` / `ati` / `cti` | `load.*` | 每日 |
| `daily.vo2max` / `lthr` / `ltsp` / `stamina_level(_7d)` | 表现指标 | 每日 |
| `sleep.total_duration_minutes` / `phases.{deep,light,rem,awake}` / `avg_hr` | `sleep.*` | 每日 |

> 覆盖：活动 **4,471**（2023-01→）· 每日 **1,381**（2022-12→）· 睡眠 **1,358**（2023-01→）。

---

## 三、数据同步策略

### 3.1 同步频率

| 数据类型 | 同步频率 | 触发方式 | 超时 |
|---------|:-------:|---------|:----:|
| **HRV** | 每日 07:00 | cron | 30s |
| **训练数据** | 跑步结束后 | 事件触发 | 60s |
| **睡眠** | 每日 08:00 | cron | 30s |
| **月度汇总** | 每日 22:00 | cron | 60s |

### 3.2 同步流程

```
1. 触发同步（cron / 事件）
2. 调用 Health Connect / Coros API
3. 解析响应 JSON
4. 写入 bioloop-injection-{date}.md
5. 更新 running_loop_status.json
6. 检查 HRV 阈值
7. 若跌破阈值 → 触发 Safety Claw
```

### 3.3 数据转换规则

```python
# HRV 计算：3 日滚动均值
def calc_hrv_3d_avg(hrv_values: list[float]) -> float:
    """取最近 3 天的 HRV 均值"""
    return sum(hrv_values[-3:]) / len(hrv_values[-3:])

# 月度跑量计算
def calc_monthly_km(daily_km: list[float]) -> float:
    """当月累计跑量"""
    return sum(daily_km)

# 训练负荷评估
def assess_training_load(load: float) -> str:
    if load < 100: return "低"
    elif load < 200: return "中等"
    elif load < 300: return "高"
    else: return "极高（需恢复）"
```

---

## 四、异常重试与告警

### 4.1 重试策略

| 异常类型 | 重试次数 | 重试间隔 | 降级策略 |
|---------|:-------:|:-------:|---------|
| API 超时 | 3 | 10s / 30s / 60s | 使用上次缓存数据 |
| 认证失败 | 1 | — | 告警 + 人工介入 |
| 数据格式错误 | 1 | — | 跳过本次同步 |
| 网络断连 | 5 | 60s 递增 | 本地缓存 + 下次重试 |
| Health Connect 不可用 | 3 | 300s | 降级为手动导入 |

### 4.2 告警规则

| 告警级别 | 触发条件 | 通知方式 | 处理 |
|:-------:

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
