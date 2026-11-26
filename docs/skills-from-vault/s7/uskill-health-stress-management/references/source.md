
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
      "stress_assessment.stress_type = acute",
      "coping_strategies.immediate 包含 深呼吸",
      "建议 包含 准备策略"
    ],
    "expected_behavior": "针对急性压力提供即时应对",
    "critic_attack": "是否提供了足够的即时帮助？"
  },
  {
    "id": "test-003",
    "name": "慢性压力",
    "prompt": "我长期处于压力状态，感觉很疲惫",
    "context": "stress_level=8, type=chronic",
    "assertions": [
      "stress_assessment.stress_type = chronic",
      "support_system.professional_help = true",
      "monitoring_plan.red_flags 已列出"
    ],
    "expected_behavior": "识别慢性压力，建议专业帮助",
    "critic_attack": "是否正确评估了严重程度？"
  }
]
```

---

## 🔗 关联文档

- [[元认知-Schema]] — 元认知觉察
- [[情绪管理方法]] — 情绪调节
- [[心流状态激活]] — 正向体验
- [[2026-06 睡眠优化执行手册]] — 睡眠与压力
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：压力评估 + 应对策略 + 减压计划 + Self-Play |

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


**相关概念**：[[控制情绪的方法]] · [[正念]] · [[情绪书写与心理疗愈]]

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
