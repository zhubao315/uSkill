
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
- **检查点**：✅ 验证 chronotype 推断逻辑一致，alignment_score 计算正确

### Step 2: 光照与环境方案

- **输入**：`rhythm_assessment` + `light_exposure`
- **动作**：
  1. 设计晨间光照方案（时间、时长、强度）
  2. 设计晚间避光方案
  3. 评估当前光照环境不足之处
- **输出**：`circadian_protocol.light_protocol`
- **分支条件**：
  - IF chronotype = evening 且需调整为 earlier → 渐进式提前（每 2 天提前 15 分钟）
  - IF 室外光照不足 → 建议使用 10000 lux 光照灯
  - IF 居住高纬度地区冬季 → 追加光疗方案
  - ELSE → 标准光照方案
- **检查点**：✅ 验证光照时间在安全范围内，无过曝风险

### Step 3: 进餐与运动时机

- **输入**：`circadian_protocol.light_protocol` + `work_constraint`
- **动作**：
  1. 设定进食窗口（与节律同步）
  2. 安排运动最佳时段
  3. 设定咖啡因截止时间
- **输出**：`circadian_protocol.meal_timing` + `circadian_protocol.exercise_timing`
- **分支条件**：
  - IF `work_constraint` 含夜班 → 进食窗口反转（夜间进食、白天禁食）
  - IF 用户有晨练习惯 → 运动安排在光照后 1-2 小时
  - IF 用户晚餐较晚 → 建议就寝前 3 小时完成进食
  - ELSE → 标准时间窗
- **检查点**：✅ 验证进食窗口 ≥12 小时，咖啡因截止在就寝前 8 小时

### Step 4: 时差调整方案（条件执行）

- **输入**：`travel_details` + `rhythm_assessment`
- **动作**：
  1. 计算时差调整天数（每小时时差 ≈ 1 天恢复）
  2. 生成逐日光照/褪黑素时间表
  3. 设定到达后首日策略
- **输出**：`jet_lag_protocol`
- **分支条件**：
  - IF `concern_type` ≠ jet_lag → 跳过此步骤，输出 null
  - IF 时差 ≤ 3 小时 → 简化方案（仅光照调整）
  - IF 时差 > 6 小时 → 完整方案含提前调整期 + 褪黑素指导
  - IF 向东飞行 > 向西飞行 → 需更激进的提前策略
  - ELSE → 标准时差方案
- **检查点**：✅ 验证逐日时间表无冲突，褪黑素剂量在安全范围

### Step 5: 精力管理与季节支持

- **输入**：`circadian_protocol` + `rhythm_assessment`
- **动作**：
  1. 识别用户精力高峰和低谷时段
  2. 设定战略性小睡方案
  3. 评估季节性因素影响
- **输出**：`energy_management` + `seasonal_support`
- **分支条件**：
  - IF `concern_type` = energy_dip → 重点优化精力分配
  - IF `concern_type` = sadian → 启动季节性情绪管理方案
  - IF 当前月份为 11-2 月（北半球冬季） → 追加光疗建议
  - ELSE → 标准精力管理
- **检查点**：✅ 验证小睡时长 ≤ 25 分钟且在 14:00 前

### Step 6: 监控计划与方案整合

- **输入**：全部前序输出
- **动作**：
  1. 设定每日/每周监控指标
  2. 定义调整触发条件
  3. 整合为完整 JSON 输出
- **输出**：`monitoring_plan` + 最终方案
- **检查点**：✅ 验证所有模块数据一致，监控指标可量化

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议处方药物（褪黑素仅建议 OTC 剂量 ≤ 3mg）
2. **不得**忽视持续 2 周以上的严重情绪低落（建议就医）
3. **必须**标注光照疗法的禁忌症（如双相情感障碍）
4. **必须**建议轮班工作者咨询职业健康医生

### 软性约束（建议遵守）
1. 建议使用穿戴设备追踪睡眠和活动数据
2. 建议调整期保持至少 7 天的作息一致性
3. 建议记录精力日记以验证方案效果

### 人工兜底点
- 当用户报告持续情绪低落或自杀念头时，**必须**立即建议专业心理援助
- 当轮班工作涉及夜间驾驶时，**必须**强调安全风险
- 当时差调整涉及重要商务活动时，**必须**建议提前 7 天开始调整

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `BIO_ERROR_CHRONOTYPE` | chronotype 推断矛盾 | 要求用户补充诊断信息，使用保守中间方案 | 🟡 |
| `BIO_ERROR_SCHEDULE` | current_schedule 格式错误 | 请求修正并提供标准格式示例 | 🟡 |
| `BIO_WARNING_MOOD` | 用户报告情绪低落 > 2 周 | 建议就医并提供心理援助热线 | 🔴 |
| `BIO_ERROR_TRAVEL` | travel_details 信息不完整 | 要求补充出发地、目的地、日期 | 🟡 |
| `BIO_WARNING_SUPPLEMENT` | 用户正在使用影响节律的药物 | 提醒咨询医生，标注可能冲突 | 🟡 |

### 降级策略
- 当 chronotype 未知时，使用 intermediate 假设并标注需验证
- 当 weather/light 数据缺失时，使用标准光照方案
- 当 jet_lag 方案过于复杂时，简化为核心光照+褪黑素方案

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] `plan_id` 格式为 BIO-YYYY-MMDD-NNN
- [ ] 时间字段格式为 HH:MM

### 内容校验
- [ ] 光照方案时间在安全范围内（非睡眠时段）
- [ ] 褪黑素剂量 ≤ 3mg
- [ ] 小睡时长 ≤ 25 分钟
- [ ] 进食窗口 ≥ 12 小时
- [ ] 咖啡因截止在就寝前 ≥ 8 小时

### 合规校验
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确触发
- [ ] 未建议处方药物

### OVP 验证信号
- 精力评分 ≥ 85/100
- 节律稳定性偏差 ≤ 15%
- 用户主观满意度提升

---

## 🔄 迭代触发条件

### Self-Play 触发
- **频率**：weekly
- **触发条件**：
  - 新增 chronotype 诊断维度时
  - 时差调整模型更新时
  - 用户反馈精力评分变化 < 5% 时

### 版本升级触发
- 当新增季节性情绪管理模块时，升级 minor 版本
- 当精力管理模型重大更新时，升级 major 版本

### 废弃触发
- 当节律科学出现颠覆性新发现，需完全重构方案时，标记为 deprecated

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
    "name": "跨时差旅行调整",
    "prompt": "下周一从北京飞纽约，时差13小时，怎么提前调整？",
    "context": "concern_type=jet_lag, travel_details={from:'Beijing', to:'NewYork', time_diff:13}",
    "assertions": [
      "jet_lag_protocol.pre_adjustment_days >= 5",
      "jet_lag_protocol.hourly_schedule 包含逐日计划",
      "jet_lag_protocol.melatonin_guide 已提供",
      "circadian_protocol.light_protocol 已调整"
    ],
    "expected_behavior": "生成完整的提前调整时间表",
    "critic_attack": "是否区分了向东和向西飞行的差异？"
  },
  {
    "id": "test-002",
    "name": "夜班工作者节律",
    "prompt": "我上夜班（22:00-06:00），白天睡觉但总是睡不好",
    "context": "concern_type=shift_work, current_schedule={work:'22:00-06:00', sleep:'08:00-15:00'}",
    "assertions": [
      "circadian_protocol.light_protocol 包含夜班光照方案",
      "circadian_protocol.meal_timing 反转为夜间进食",
      "energy_management.trough_hours 已识别",
      "monitoring_plan 包含调整触发条件"
    ],
    "expected_behavior": "为夜班工作者设计完整的节律倒转方案",
    "critic_attack": "是否建议了轮班制度的职业健康咨询？"
  },
  {
    "id": "test-003",
    "name": "冬季情绪低落",
    "prompt": "每年冬天11月到2月就情绪很低落，不想出门",
    "context": "concern_type=sadian, current_schedule={outdoor_hours: 0.5}",
    "assertions": [
      "seasonal_support.light_therapy.recommended 为 true",
      "seasonal_support.light_therapy.lux_requirement 包含 10000 lux",
      "circadian_protocol.light_protocol 包含晨间光照",
      "monitoring_plan.red_flags 包含情绪恶化信号"
    ],
    "expected_behavior": "生成季节性情绪管理方案含光疗建议",
    "critic_attack": "是否提醒了双相情感障碍的禁忌？"
  },
  {
    "id": "test-004",
    "name": "晨型人重塑为夜型",
    "prompt": "我是早起鸟但新工作要求晚上开会到10点，怎么调整",
    "context": "concern_type=rhythm_reset, chronotype=morning, work_constraint={late_meetings: true}",
    "assertions": [
      "circadian_protocol.sleep_window.target_bedtime >= 23:00",
      "circadian_protocol.light_protocol.evening_dimming 已延迟",
      "energy_management.peak_hours 已重新映射",
      "jet_lag_protocol 为 null（非时差场景）"
    ],
    "expected_behavior": "渐进式节律后移方案",
    "critic_attack": "晨型人强行转夜型是否健康？"
  },
  {
    "id": "test-005",
    "name": "精力低谷期管理",
    "prompt": "每天下午2-4点特别困，效率很低怎么办",
    "context": "concern_type=energy_dip, current_schedule={work_start:'09:00', work_end:'18:00'}",
    "assertions": [
      "energy_management.trough_hours 包含 14:00-16:00",
      "energy_management.strategic_napping.recommended 为 true",
      "energy_management.strategic_napping.duration <= 25分钟",
      "circadian_protocol.meal_timing.lunch 不晚于 13:00"
    ],
    "expected_behavior": "识别精力低谷原因并提供小睡+饮食方案",
    "critic_attack": "是否排除了贫血等病理因素？"
  },
  {
    "id": "test-006",
    "name": "未知 chronotype 诊断",
    "prompt": "我不知道自己是早起鸟还是夜猫子，帮我判断",
    "context": "concern_type=rhythm_reset, chronotype=unknown",
    "assertions": [
      "rhythm_assessment.chronotype_detected 已推断",
      "推断基于至少 3 个维度",
      "方案中标注了 chronotype 推断置信度"
    ],
    "expected_behavior": "通过诊断问题推断 chronotype 并生成方案",
    "critic_attack": "推断方法是否科学可靠？"
  }
]
```

---

## 🔗 关联文档

- [[2026-06 睡眠优化执行手册]] — 睡眠与节律的协同优化
- [[压力管理]] — 压力对节律的影响
- [[冥想进阶]] — 冥想对节律的辅助调节
- [[深度工作四步法——专注力炼金术]] — 精力高峰与深度工作的匹配
- [[晨间例行系统]] — 晨间光照与节律建立
- [[数据驱动 Biohacking 闭环]] — 穿戴设备数据驱动节律追踪

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：节律评估 + 光照方案 + 时差调整 + 精力管理 + Self-Play |

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
