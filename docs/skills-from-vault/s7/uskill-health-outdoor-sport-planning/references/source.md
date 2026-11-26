
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
  - IF `temperature` < 5°C 或 > 35°C → 追加温控装备
  - IF `budget` < 基础装备总价 → 标注缺失项并建议租赁
  - ELSE → 标准清单输出
- **检查点**：✅ 验证所有必带装备已列入，重量在体能承受范围内

### Step 4: 安全评估

- **输入**：`route_plan` + `equipment_list` + `group_size`
- **动作**：
  1. 识别路线风险点（地形、气候、野生动物）
  2. 评估综合风险等级
  3. 制定应急撤离方案
  4. 确认通讯保障
- **输出**：`safety_assessment`
- **分支条件**：
  - IF 风险等级 = extreme → 强制要求专业向导 + 双人结组
  - IF `group_size` > 1 → 增加人员管理方案和集合点
  - IF 无手机信号覆盖 → 启用卫星通讯方案
  - ELSE → 标准安全方案
- **检查点**：✅ 验证每个风险有对应缓解措施，应急方案可执行

### Step 5: 天气应对与时间线

- **输入**：`weather_response` + `route_plan` + `safety_assessment`
- **动作**：
  1. 设定天气触发点（推迟/折返/避险条件）
  2. 编排详细时间线
  3. 制定备用方案
- **输出**：`weather_response` + `timeline`
- **分支条件**：
  - IF 预报有极端天气 → 标记为 HIGH PRIORITY 并建议改期
  - IF 日落前无法完成路线 → 缩减路线或提前出发
  - IF 降水概率 > 60% → 追加避雨装备和备选室内活动
  - ELSE → 标准时间线
- **检查点**：✅ 验证返回时间 ≤ 日落前 1 小时，触发条件明确可判断

### Step 6: 方案整合与输出

- **输入**：全部前序输出
- **动作**：
  1. 整合为完整 JSON 输出
  2. 生成可读摘要
  3. 执行 Self-Play 校验
- **输出**：最终 `plan_id` 标记的完整方案
- **检查点**：✅ 验证所有模块数据一致，无遗漏字段

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**推荐超出用户体能等级的路线（beginner 禁止 extreme 路线）
2. **不得**在极端天气预警下建议出行（台风、暴雨红色预警、暴风雪）
3. **必须**包含应急撤离方案
4. **必须**标注紧急联系方式和最近医疗机构

### 软性约束（建议遵守）
1. 建议携带急救包（即使短途）
2. 建议告知至少一位亲友行程计划
3. 建议购买户外运动保险

### 人工兜底点
- 当路线涉及悬崖、深水区时，**必须**要求专业装备和经验确认
- 当用户有心血管疾病史时，**必须**建议医疗评估后再行动
- 当 `group_size` > 15 时，**必须**建议聘请专业领队

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `OUT_ERROR_WEATHER` | 天气 API 不可用或数据过期 | 使用缓存数据并标注 WARNING，建议用户出行前再确认 | 🟡 |
| `OUT_ERROR_ROUTE` | 目的地无法匹配或路线不通 | 要求用户提供详细坐标或替代目的地 | 🟡 |
| `OUT_ERROR_BUDGET` | 预算不足以覆盖基础装备 | 输出最低装备清单并建议租赁渠道 | 🟡 |
| `OUT_ERROR_FITNESS` | 体能与路线严重不匹配 | 强制降级路线或建议体能训练后再执行 | 🔴 |
| `OUT_ERROR_GROUP` | 群组中有未成年或老人 | 追加特殊安全措施并建议降低路线难度 | 🔴 |

### 降级策略
- 当天气数据不可用时，自动降级为"标准天气假设"方案并标注 WARNING
- 当路线数据不完整时，输出部分路线 + 用户手动补充提示
- 当装备数据缺失时，输出通用装备清单

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] `plan_id` 格式为 OUT-YYYY-MMDD-NNN

### 内容校验
- [ ] 路线距离与时间估算匹配（步行 ~4-5km/h，骑行 ~15-20km/h）
- [ ] 装备清单覆盖所有天气相关需求
- [ ] 安全评估包含至少 2 个风险点
- [ ] 应急方案包含最近医院和联系方式
- [ ] 时间线包含返回截止时间

### 合规校验
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确触发
- [ ] 敏感位置信息已脱敏

### OVP 验证信号
- 路线完成率 ≥ 90%
- 安全事件为零
- 装备覆盖率 100%

---

## 🔄 迭代触发条件

### Self-Play 触发
- **频率**：weekly
- **触发条件**：
  - 新增运动类型支持时
  - 天气数据源变更时
  - 用户反馈路线偏差 > 20% 时

### 版本升级触发
- 当新增运动类型（如攀岩、皮划艇）时，升级 minor 版本
- 当安全模型重大重构时，升级 major 版本

### 废弃触发
- 当路线数据源停止更新超过 6 个月时，标记为 deprecated

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "单日徒步规划",
    "prompt": "我想周末去香山徒步，2个人，中级水平，天气预报说多云",
    "context": "activity_type=hike, group_size=2, fitness_level=intermediate",
    "assertions": [
      "route_plan.total_distance_km > 0",
      "route_plan.difficulty 为 moderate",
      "safety_assessment.risk_level 已评估",
      "equipment_list.essential 包含登山鞋",
      "timeline.return_deadline 在日落前"
    ],
    "expected_behavior": "生成完整的单日徒步方案",
    "critic_attack": "是否考虑了香山的实际路况和游客密度？"
  },
  {
    "id": "test-002",
    "name": "新手骑行路线",
    "prompt": "我刚入门骑行，想在城市周边骑50公里，预算2000元买装备",
    "context": "activity_type=bike, fitness_level=beginner, budget=2000",
    "assertions": [
      "route_plan.difficulty 为 easy",
      "equipment_list.estimated_cost <= 2000",
      "equipment_list.essential 包含头盔",
      "safety_assessment.identified_risks 包含交通安全"
    ],
    "expected_behavior": "推荐适合新手的平坦路线并控制预算内装备",
    "critic_attack": "是否提醒了新手骑行的安全要点？"
  },
  {
    "id": "test-003",
    "name": "暴雨天气应对",
    "prompt": "计划明天露营但预报说有暴雨，怎么办",
    "context": "activity_type=camp, weather_forecast={precipitation: 'heavy'}",
    "assertions": [
      "weather_response.trigger_points.postpone_conditions 包含暴雨",
      "weather_response.contingency_plan 已提供",
      "status 建议推迟或提供替代方案"
    ],
    "expected_behavior": "明确建议推迟并提供备选方案",
    "critic_attack": "是否过于保守？小雨是否仍可露营？"
  },
  {
    "id": "test-004",
    "name": "多日穿越规划",
    "prompt": "我计划走鳌太线，4天3晚，高级水平",
    "context": "activity_type=multi_day, duration=multi_day, fitness_level=advanced",
    "assertions": [
      "route_plan.waypoints 包含营地",
      "route_plan.waypoints 包含水源点",
      "equipment_list.essential 包含帐篷",
      "safety_assessment.risk_level 为 high 或 extreme",
      "safety_assessment.emergency_plan.evacuation_route 已提供"
    ],
    "expected_behavior": "生成详细的多日穿越方案含营地规划",
    "critic_attack": "鳌太线风险极高，是否充分警告？"
  },
  {
    "id": "test-005",
    "name": "极端高温越野跑",
    "prompt": "下周要参加一个50公里越野跑，预报气温38度",
    "context": "activity_type=trail_run, weather_forecast={temperature: 38}",
    "assertions": [
      "weather_response.trigger_points 包含高温条件",
      "equipment_list.weather_specific 包含防晒和降温装备",
      "safety_assessment.identified_risks 包含中暑",
      "timeline 包含补水提醒节点"
    ],
    "expected_behavior": "针对极端高温生成专项安全方案",
    "critic_attack": "是否建议考虑取消或缩短赛程？"
  },
  {
    "id": "test-006",
    "name": "带儿童露营",
    "prompt": "带两个小孩（6岁和10岁）去露营，新手",
    "context": "activity_type=camp, group_size=3, fitness_level=beginner, special_needs=[children]",
    "assertions": [
      "route_plan.difficulty 为 easy",
      "safety_assessment.identified_risks 包含儿童安全",
      "equipment_list.essential 包含儿童专用装备",
      "timeline 包含儿童休息间隔"
    ],
    "expected_behavior": "针对家庭露营生成安全方案",
    "critic_attack": "是否考虑了儿童的特殊需求？"
  }
]
```

---

## 🔗 关联文档

- [[压力管理]] — 运动压力与恢复平衡
- [[营养规划]] — 户外运动营养补给
- [[2026-06 睡眠优化执行手册]] — 运动后睡眠恢复
- [[心率区间训练]] — 运动强度监控
- [[马拉松训练体系]] — 长距离耐力训练
- [[数据驱动 Biohacking 闭环]] — 运动数据追踪

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：路线规划 + 装备选型 + 安全评估 + 天气应对 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


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


**相关概念**：[[户外运动风险管理]] · [[户外探险规划]]

---



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
