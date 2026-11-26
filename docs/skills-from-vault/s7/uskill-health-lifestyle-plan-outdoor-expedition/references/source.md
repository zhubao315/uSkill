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
    "water": { "liters_per_day": "float", "purification_method": "string", "refill_points": ["string"] },
    "fuel": { "canisters": "int", "cooking_style": "string" },
    "redundancy_pct": "float — 建议 ≥20%"
  },
  "team_coordination": {
    "roles": [
      { "member": "string", "role": "leader|navigator|medic|logistics|sweep", "responsibilities": "string" }
    ],
    "comms_protocol": {
      "radio_channel": "string",
      "check_in_times": ["string"],
      "emergency_signal": "string",
      "satellite_device": "string — 如 Garmin inReach 号码"
    },
    "psychological_notes": "string — 针对团队心理素质的分工考量"
  },
  "emergency_card": {
    "contacts": [
      { "name": "string", "phone": "string", "role": "local_rescue|base_contact|hospital|team_leader" }
    ],
    "comms_protocol": "string — 通讯协议",
    "medical_procedures": [
      { "condition": "string — 如高反/失温/骨折", "procedure": "string — 现场处置流程" }
    ],
    "weather_contingencies": [
      { "condition": "string — 如雷暴/大雪/大雾", "action": "string — 应对措施" }
    ],
    "lost_protocol": "string — 迷路时的 STOP 原则（Stop, Think, Observe, Plan）"
  },
  "gpx_files": {
    "primary_route": "string — GPX 文件路径或内容",
    "backup_route": "string — 备用路线 GPX",
    "bailout_routes": ["string — 下撤路线 GPX"]
  },
  "expedition_plan_doc": "string — 完整《户外探险计划书》Markdown 内容",
  "go_no_go_decision": {
    "decision": "go | postpone | cancel",
    "rationale": "string",
    "decision_time": "datetime — 出发前12小时"
  }
}
```

## 📋 执行步骤

### Step 1: 目标定义与可行性分析

1. **动作**
   - 明确探险目标：清晰定义核心目标（登顶某峰 / 完成穿越 / 探索未知区域），目标应清晰且唯一
   - 定义活动风格：明确是轻量化快速穿越（FKT）、重装徒步还是休闲露营
   - 客观评估团队能力：逐一体能、技能和经验水平，识别每位成员的能力短板
   - 使用 **AI提示词-可行性分析**，让AI扮演"户外运动顾问"，基于目标、季节和团队概况进行初步的可行性与风险等级评估

2. **战略考量**
   - **没有金刚钻，不揽瓷器活**。确保目标与团队能力相匹配，是所有计划的起点和安全的第一道防线。不要让团队中最弱的人成为短板，而要以此为基准设计路线。

3. **质量检查点**
   - [ ] 探险目标是否清晰且唯一？
   - [ ] 活动风格是否已明确界定？
   - [ ] 团队成员的能力短板是否已逐一识别？
   - [ ] AI可行性评估是否已完成并获得评级？

---

### Step 2: 情报收集与AI辅助研判

1. **动作**
   - **地图与轨迹收集**：从两步路/六只脚等平台下载相关区域的等高线地图和多条（≥3条）他人 GPX 轨迹
   - **天气模型收集**：收集目标区域未来72小时的多种天气模型预报（ECMWF、GFS），进行交叉比对
   - **文本情报收集**：收集近期山友游记、社交媒体帖子，了解最新路况、水源状况和风险点
   - 使用 **AI提示词-GPX轨迹分析**，让AI扮演"GIS分析师"，对多条GPX轨迹进行叠加分析，识别常规路线、岔路口和水源/营地点
   - 将天气数据输入AI，让其解读并预测关键风险（特定时间的降雨概率、风寒效应、雷暴时段等）

2. **战略考量**
   - **信息优势是安全的核心**。将多源、异构的信息进行交叉验证和深度分析，形成超越单一信息源的立体判断。单条GPX可能有误，多条交叉才能确认主路线。

3. **质量检查点**
   - [ ] 是否已掌握≥3条不同的GPX轨迹作为参考？
   - [ ] 是否已收集至少两种天气模型的预报数据？
   - [ ] 对天气变化的风险（失温、雷暴、暴风雪）是否有清晰预判？
   - [ ] 是否已获取近期（≤30天）的路线实况信息？

---

### Step 3: 路线设计与多层预案

1. **动作**
   - **设计主路线（Plan A）**：在地图上精确绘制主路线，标记关键节点（垭口、水源、营地、决策点），预估每日里程、爬升/下降和所需时间
   - **设计备用路线（Plan B）**：当主路线受阻（道路损毁、天气封路）时的替代路线
   - **设计紧急下撤路线（Plan C）**：在路线上设置≥3个**"决策点（Decision Point）"**及对应的**"下撤路线（Bailout Route）"**，明确触发条件（如"下午2点前未到XX垭口，则启动下撤"）
   - 使用 **AI提示词-路线审查**，让AI扮演"国际登山向导"，以最苛刻标准审查完整路线计划（A/B/C），找出≥5个潜在风险点和疏漏
   - 导出所有路线为 GPX 文件

2. **战略考量**
   - **专业与业余的区别在于有无预案**。完善的多层预案是在不确定环境中保持掌控力的关键。每个决策点都要有明确的触发条件，避免在压力下做出非理性决策。

3. **质量检查点**
   - [ ] 计划中是否明确标记了≥3个"决策点"及其具体触发条件？
   - [ ] 所有备用和下撤路线是否同样经过了可行性分析？
   - [ ] AI向导审查是否已完成，风险点是否已逐条回应？
   - [ ] GPX 文件是否已导出且能在设备上正常显示？

---

### Step 4: 资源与团队协同

1. **动作**
   - **精细化装备清单**：根据路线、天气和活动风格，制定精确到个人的装备和公共装备清单，进行轻量化和功能性双重检查
   - **物资规划**：精确计算食物（热量）、水和燃料的需求量，留出≥20%冗余。食物需考虑高海拔/极端环境下的实际消耗
   - **团队分工**：明确领队、协作、导航、后勤、收队等角色职责，考虑成员性格和心理素质进行匹配
   - **通讯协议**：建立清晰的通讯协议——手台频道、定时联络时间、紧急信号、卫星通讯设备确认
   - 使用 **AI提示词-应急预案生成**，让AI扮演"荒野急救与生存专家"，生成简洁的应急预案卡

2. **战略考量**
   - 考虑成员的心理素质进行分工，将合适的人放在合适的位置。通讯协议是团队的"神经系统"——断联即失联，必须有冗余方案。

3. **质量检查点**
   - [ ] 装备清单是否经过轻量化和功能性双重检查？
   - [ ] 食物/水/燃料冗余是否≥20%？
   - [ ] 团队中每个人是否都清楚自己的职责和应急通讯方法？
   - [ ] 应急预案卡是否已生成并分发给所有人？

---

### Step 5: 发布计划与行前检查

1. **动作**
   - **生成计划书**：使用 **AI提示词-计划书生成**，将所有信息汇总生成一份简洁、清晰的《户外探险计划书》，分发给所有队员和留守联系人
   - **轨迹与地图导入**：将GPX轨迹和离线地图导入所有队员的GPS设备或手机中，确认均能正常加载和显示
   - **行前会议（Briefing）**：召集全体队员，详细讲解计划、预案和注意事项，确保信息完全对齐
   - **最终Go/No-Go决策**：出发前12小时，基于最新天气预报和人员状态，做出最终的"执行/推迟/取消"决策并记录理由

2. **战略考量**
   - **最后的决策是最重要的决策**。永远不要因为"来都来了"而无视行前检查发现的重大风险。Go/No-Go 决策必须记录，这是对团队和自己负责。

3. **质量检查点**
   - [ ] 留守联系人是否已收到完整的计划书？
   - [ ] 所有队员的GPS设备是否都能正常加载和显示轨迹？
   - [ ] 行前会议是否已召开，所有人是否信息对齐？
   - [ ] Go/No-Go 决策是否已做出并记录？

## 🤖 AI提示词库

### 提示词-01：可行性分析
```
你是一位经验丰富的户外领队。我计划在[月份]和[人数]名队员（平均体能[水平]）去[地点]进行一次为期[天数]的[活动类型，如重装徒步]。请为我进行一次初步的可行性分析，指出：
1. 该季节在该地区的主要风险（如天气、地质、野生动物）。
2. 对团队成员的最低体能和技能要求。
3. 给出"推荐"、"谨慎推荐"或"不推荐"的初步评级及理由。
```

### 提示词-02：GPX轨迹分析
```
你是一位GIS地理信息系统分析师。我将提供2-3条他人走过的GPX轨迹文件（以WKT或GeoJSON格式描述）。请你分析这些轨迹，并告诉我：
1. 它们重合度最高的"主路线"是哪一段？
2. 轨迹出现分叉的关键节点在哪里？
3. 综合所有轨迹，标注出可能的稳定水源地和适合扎营的平坦区域。
轨迹数据如下：[...]
```

### 提示词-03：路线审查
```
你是一位持有IFMGA认证的国际高山向导。我制定了一份登山/徒步计划，请你以最苛刻的标准对其进行审查，并指出至少5个潜在的风险点或计划疏漏。审查需覆盖：路线设计的合理性、时间安排的裕度、风险评估的全面性、以及应急预案的可行性。计划如下：[...]
```

### 提示词-04：应急预案生成
```
你是一位荒野急救与生存专家。针对我即将进行的"[活动类型]"活动，地点在"[地区类型，如高海拔山区]"，请为我生成一份简洁的应急预案卡。内容需包括：
1. 常见的3种医疗紧急情况（如高反、失温）的现场处置流程；
2. 3种极端天气（如雷暴、大雪）的应对措施；
3. 迷路时的"STOP"原则（Stop, Think, Observe, Plan）。
```

### 提示词-05：计划书生成
```
你是一位专业的户外探险文档撰写专家。请根据以下信息，生成一份简洁、清晰、专业的《户外探险计划书》。计划书需包含：目标概述、团队信息、详细路线（含每日行程）、风险评估、装备清单、应急预案、通讯协议。格式要求结构清晰，适合打印携带。信息如下：[...]
```

## ⚠️ 常见陷阱

| 陷阱 | 描述 | 应对 |
|------|------|------|
| **"来都来了"心理** | 行前检查发现重大风险，但因已投入时间精力而强行出发 | 坚守 Go/No-Go 决策记录制度，取消不丢人，出事才丢人 |
| **单一信息源依赖** | 仅凭一条 GPX 轨迹或一篇游记规划路线 | 必须≥3条轨迹交叉验证，游记需选近期且≥2篇 |
| **低估高海拔消耗** | 按平原体能计算行程，未考虑高海拔体能下降30-50% | 海拔每升高1000米，预期行进速度降低15-20% |
| **冗余不足** | 水和食物按精确量准备，无缓冲 | 永远留≥20%冗余，宁可多背不可少带 |
| **下撤路线未验证** | 标记了下撤路线但从未实际走过或研究过 | 下撤路线必须与主路线同等重视，做好GPX和可行性分析 |
| **通讯设备未测试** | 手台/卫星设备出发前未测试 | 行前会议必须现场测试所有通讯设备 |
| **天气窗口忽视** | 只看天气预报不看趋势，错过最佳窗口 | 收集≥2种天气模型，关注趋势而非单点数据 |
| **团队能力高估** | 以领队能力为基准设计路线 | 以团队中最弱者为基准，留出安全裕度 |
| **决策点模糊** | "差不多就下撤"而非明确时间和位置 | 每个决策点必须有精确的时间/位置/条件触发阈值 |

## 📚 关联资产

| 类型 | 名称 | 用途 |
|------|------|------|
| **核心技能** | 🤖 人工智能专家技能 | 数据分析、轨迹研判、天气解读 |
| **核心技能** | 🏗️ 架构师技能 | 冗余思维、多层预案设计 |
| **核心技能** | 🧠 心理学专家技能 | 团队心理评估、压力下决策 |
| **关联SOP** | SOP-18（AI驱动的个人OKR与数据复盘） | 分析体能数据、复盘活动表现 |
| **关联SOP** | SOP-15（AI赋能的摄影后期） | 活动记录与分享 |
| **硬件工具** | Garmin inReach | 卫星通讯与SOS求救 |
| **硬件工具** | GPS手表 / 智能手机 | 轨迹导航与离线地图 |
| **硬件工具** | 手持对讲机 | 团队短距通讯 |
| **软件平台** | 两步路、六只脚 | GPX轨迹下载与分享 |
| **软件平台** | Strava | 体能数据分析 |
| **软件平台** | Windy.com | 多模型天气预报 |
| **软件平台** | Google Earth / 卫星地图 | 地形研判与路线预览 |


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-019 转化 |
| 2026-05-09 | 1.0.1 | 全面升级：补充战略考量与质量检查点、增加常见陷阱、扩充提示词库至5个、完善输出JSON schema、补充关联资产 |

---
**相关笔记**：[[压力管理]] [[冥想进阶]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定制。

---

## 🚫 Anti-Rationalization Table `[v3新增]`

> 来源：addyosmani/agent-skills 的核心创新

| Agent 常见借口 | 反驳 |
|--------------|------|
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
- 检查常见错误

### ⚠️ Ask first（先问再做）
- 用户意图不明确时
- 操作不可逆时
- 涉及外部系统时

### 🚫 Never do（绝对禁止）
- 不跳过验证步骤
- 不在用户未确认时执行高风险操作
- 不伪装成功（失败就上报）

---

## 🔒 Gated Workflow `[v3新增]`

> 来源：addyosmani 的门禁 + claude-skills 的 Agent Harness

```
DISCUSS → PLAN → EXECUTE → VERIFY → CLOSE
   ↓         ↓        ↓          ↓        ↓
 Context   方案     执行      证据     Done/
 Read     确认     任务      检查    Escalate
```

### Phase 1: DISCUSS
- [ ] 输出 Context Read 一行判断
- [ ] 确认用户意图
- [ ] 确认约束条件

### Phase 2: PLAN
- [ ] 制定执行方案
- [ ] 确认资源可用
- [ ] 人工审批计划

### Phase 3: EXECUTE
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功
