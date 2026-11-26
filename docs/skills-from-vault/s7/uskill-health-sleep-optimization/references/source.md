
description: |
  当用户需要改善睡眠质量、优化睡眠环境、建立健康睡眠习惯、解决睡眠问题时使用此 Skill。
  触发词包括：'睡眠'、'失眠'、'睡眠质量'、'睡眠习惯'、'入睡困难'、
  '睡眠环境'、'昼夜节律'、'睡眠卫生'。当用户讨论疲劳、精力不足、
  作息紊乱时，即使未直接说"睡眠优化"，也应使用此 Skill。
  不适用于严重睡眠障碍（建议就医）。遇到睡眠改善需求时优先使用。

---

# uSkill-301: 睡眠优化

## 🎯 目标

> 基于睡眠科学，建立健康的睡眠习惯，优化睡眠环境，提升睡眠质量和精力恢复。

**核心价值**：睡眠是精力恢复的基础，优化睡眠是提升整体效率的关键。

**适用场景**：
- 入睡困难
- 睡眠质量差
- 作息不规律
- 精力不足
- 倒时差

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_sleep_issues` | `array` | ✅ | — | 当前睡眠问题 |
| `sleep_schedule` | `object` | ❌ | — | 当前作息时间 |
| `environment` | `object` | ❌ | — | 睡眠环境描述 |
| `lifestyle` | `object` | ❌ | — | 生活习惯信息 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话睡眠优化建议",
  "sleep_id": "SL-YYYY-MMDD-NNN",

  "sleep_assessment": {
    "issues_identified": ["string"],
    "severity": "mild|moderate|severe",
    "potential_causes": ["string"]
  },

  "sleep_hygiene_recommendations": {
    "schedule": {
      "bedtime": "string",
      "wake_time": "string",
      "consistency": "string"
    },
    "environment": {
      "temperature": "string",
      "lighting": "string",
      "noise": "string",
      "mattress_pillow": "string"
    },
    "pre_sleep_routine": ["string"],
    "avoid": ["string"]
  },

  "circadian_rhythm_optimization": {
    "light_exposure": ["string"],
    "meal_timing": ["string"],
    "exercise_timing": "string",
    "caffeine_cutoff": "string"
  },

  "sleep_quality_metrics": {
    "target_sleep_duration": "string",
    "target_sleep_latency": "string",
    "target_sleep_efficiency": "string",
    "tracking_method": "string"
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

### Step 1: 睡眠问题评估

- **输入**：`current_sleep_issues`
- **动作**：
  1. 识别具体睡眠问题
  2. 评估严重程度
  3. 分析潜在原因
- **输出**：`sleep_assessment`
- **常见睡眠问题**：

| 问题 | 特征 | 可能原因 |
|------|------|----------|
| 入睡困难 | 超过 30 分钟无法入睡 | 焦虑、咖啡因、屏幕光 |
| 睡眠中断 | 夜间频繁醒来 | 压力、环境噪音、年龄 |
| 早醒 | 比预定时间早醒 | 抑郁、时差、年龄 |
| 睡眠质量差 | 睡够时间但仍疲劳 | 睡眠呼吸暂停、压力 |

### Step 2: 睡眠卫生建议

- **输入**：`sleep_assessment`
- **动作**：
  1. 制定规律作息时间
  2. 优化睡眠环境
  3. 建立睡前程序
- **输出**：`sleep_hygiene_recommendations`
- **睡眠卫生清单**：

| 类别 | 建议 |
|------|------|
| 作息 | 固定就寝和起床时间 |
| 环境 | 凉爽、黑暗、安静 |
| 睡前 | 避免屏幕、放松活动 |
| 避免 | 咖啡因、酒精、大餐 |

### Step 3: 昼夜节律优化

- **输入**：`sleep_hygiene_recommendations`
- **动作**：
  1. 优化光线暴露
  2. 调整进餐时间
  3. 安排运动时间
- **输出**：`circadian_rhythm_optimization`
- **昼夜节律原则**：

| 时段 | 建议 |
|------|------|
| 早晨 | 接触阳光 15-30 分钟 |
| 下午 | 避免咖啡因 |
| 傍晚 | 适度运动 |
| 睡前 | 避免强光 |

### Step 4: 监控计划

- **输入**：所有前序输出
- **动作**：
  1. 设定监控指标
  2. 制定回顾计划
  3. 识别危险信号
- **输出**：`sleep_quality_metrics` + `monitoring_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议使用安眠药（需医生处方）
2. **不得**忽视严重睡眠障碍
3. **必须**建议就医当出现危险信号时

### 软性约束（建议遵守）
1. 建议记录睡眠日记
2. 建议持续追踪至少 2 周
3. 建议考虑个人差异

### 人工兜底点
- 当出现睡眠呼吸暂停症状时，**必须**建议就医
- 当睡眠问题持续 4 周以上时，**必须**建议专业评估

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `SL_WARNING_PERSISTENT` | 问题持续 2 周 | 建议加强干预 | 🟡 |
| `SL_WARNING_SEVERE` | 严重失眠 | 建议就医 | 🔴 |
| `SL_ERROR_SLEEP_APNEA` | 疑似睡眠呼吸暂停 | 建议立即就医 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 睡眠问题已识别
- [ ] 卫生建议已生成
- [ ] 昼夜节律已优化
- [ ] 监控计划已制定

### OVP 验证信号
- 睡眠质量评分 ≥ 80/100
- 入睡时间 < 20 分钟

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "入睡困难",
    "prompt": "我每天晚上躺在床上要1个多小时才能睡着",
    "context": "issues=[入睡困难]",
    "assertions": [
      "sleep_assessment.issues_identified 包含 入睡困难",
      "sleep_hygiene_recommendations 包含 睡前程序",
      "circadian_rhythm_optimization.light_exposure 已建议"
    ],
    "expected_behavior": "针对入睡困难提供建议",
    "critic_attack": "是否考虑了焦虑等因素？"
  },
  {
    "id": "test-002",
    "name": "作息不规律",
    "prompt": "我每天睡觉和起床时间都不一样",
    "context": "issues=[作息不规律]",
    "assertions": [
      "sleep_hygiene_recommendations.schedule 包含 固定时间",
      "circadian_rhythm_optimization 包含 一致性建议"
    ],
    "expected_behavior": "建立规律作息",
    "critic_attack": "是否考虑了工作性质的影响？"
  },
  {
    "id": "test-003",
    "name": "睡眠质量差",
    "prompt": "我睡够8小时但醒来还是很累",
    "context": "issues=[睡眠质量差]",
    "assertions": [
      "sleep_assessment.potential_causes 包含 可能原因",
      "sleep_quality_metrics 已设定目标",
      "建议 包含 环境优化"
    ],
    "expected_behavior": "分析睡眠质量差的原因",
    "critic_attack": "是否需要建议就医检查？"
  }
]
```

---

## 🔗 关联文档

- [[uSkill-日程优化-v1]] — 身体状态监控
- [[心率区间训练]] — 运动与睡眠
- [[数据驱动 Biohacking 闭环]] — 数据驱动优化
- [[营养规划]] — 营养与睡眠
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：睡眠评估 + 卫生建议 + 昼夜节律 + Self-Play |

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


**相关概念**：[[睡眠的生理修复机制]] · [[子午觉：顺应时辰的睡眠养生]] · [[运动恢复与休息]]

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
