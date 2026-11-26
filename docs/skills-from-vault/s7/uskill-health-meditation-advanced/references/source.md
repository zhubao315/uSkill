
description: |
  当用户需要深入冥想练习、学习正念技巧、进行慈悲冥想、提升专注力时使用此 Skill。
  触发词包括：'冥想'、'正念'、'专注'、'慈悲冥想'、'身体扫描'、
  '冥想进阶'、'禅修'。当用户讨论压力管理、专注力提升、情绪调节时，
  即使未直接说"冥想进阶"，也应使用此 Skill。
  不适用于冥想初学者（使用基础冥想指南）。遇到进阶冥想需求时优先使用。

---

# uSkill-304: 冥想进阶

## 🎯 目标

> 提供系统化的冥想进阶路径，从基础正念到高级冥想技巧，提升心理素质。

**核心价值**：冥想是训练心智的"健身房"。持续练习能显著提升专注力和情绪调节能力。

**适用场景**：
- 专注力提升
- 压力管理
- 情绪调节
- 睡眠改善
- 自我认知深化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_level` | `enum` | ❌ | `beginner` | `beginner` / `intermediate` / `advanced` |
| `practice_goal` | `enum` | ❌ | `focus` | `focus` / `stress` / `emotion` / `sleep` / `self_awareness` |
| `available_time` | `number` | ❌ | `10` | 每日可用时间（分钟） |
| `experience` | `object` | ❌ | — | 冥想经验描述 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话冥想建议",
  "meditation_id": "MD-YYYY-MMDD-NNN",

  "level_assessment": {
    "current_level": "beginner|intermediate|advanced",
    "strengths": ["string"],
    "areas_for_growth": ["string"],
    "recommended_focus": "string"
  },

  "practice_path": {
    "current_phase": {
      "name": "string",
      "duration": "string",
      "techniques": ["string"],
      "daily_practice": "string"
    },
    "next_phases": [
      {
        "name": "string",
        "prerequisites": ["string"],
        "techniques": ["string"]
      }
    ]
  },

  "technique_library": [
    {
      "technique": "string",
      "level": "beginner|intermediate|advanced",
      "description": "string",
      "duration": "string",
      "benefits": ["string"],
      "instructions": ["string"]
    }
  ],

  "weekly_schedule": {
    "monday": "string",
    "tuesday": "string",
    "wednesday": "string",
    "thursday": "string",
    "friday": "string",
    "saturday": "string",
    "sunday": "string",
    "total_weekly_minutes": "number"
  },

  "progress_tracking": {
    "daily_metrics": ["string"],
    "weekly_reviews": ["string"],
    "milestones": [
      {
        "milestone": "string",
        "target_date": "string",
        "success_criteria": "string"
      }
    ]
  },

  "common_challenges": [
    {
      "challenge": "string",
      "cause": "string",
      "solution": "string"
    }
  ],

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 水平评估

- **输入**：`current_level` + `experience`
- **动作**：
  1. 评估当前冥想水平
  2. 识别优势和成长领域
  3. 确定练习重点
- **输出**：`level_assessment`
- **冥想水平标准**：

| 水平 | 特征 | 能稳定练习 |
|------|------|:----------:|
| 初学者 | 刚开始，容易分心 | 5-10 分钟 |
| 中级 | 能稳定练习，开始深入 | 15-30 分钟 |
| 高级 | 能进行深度冥想 | 30+ 分钟 |

### Step 2: 练习路径设计

- **输入**：`level_assessment` + `practice_goal`
- **动作**：
  1. 设计当前阶段
  2. 规划进阶路径
  3. 设定里程碑
- **输出**：`practice_path`
- **冥想进阶路径**：

| 阶段 | 时长 | 技巧 |
|------|------|------|
| 基础 | 1-3 个月 | 呼吸观察、身体扫描 |
| 中级 | 3-6 个月 | 慈悲冥想、开放觉知 |
| 高级 | 6+ 个月 | 非二元觉知、三摩地 |

### Step 3: 技巧库构建

- **输入**：`practice_path`
- **动作**：
  1. 选择适合的技巧
  2. 提供详细指导
  3. 标注注意事项
- **输出**：`technique_library`
- **冥想技巧库**：

| 技巧 | 水平 | 时长 | 主要益处 |
|------|:----:|:----:|----------|
| 呼吸观察 | 初级 | 5-10 分钟 | 专注力、平静 |
| 身体扫描 | 初级 | 10-20 分钟 | 放松、身体觉知 |
| 慈悲冥想 | 中级 | 15-30 分钟 | 同理心、情绪调节 |
| 开放觉知 | 中级 | 15-30 分钟 | 觉察力、灵活性 |
| 非二元觉知 | 高级 | 30+ 分钟 | 自我认知、智慧 |

### Step 4: 每周计划

- **输入**：`practice_path` + `available_time`
- **动作**：
  1. 安排每日练习
  2. 平衡不同技巧
  3. 安排休息日
- **输出**：`weekly_schedule`

### Step 5: 进度跟踪

- **输入**：`practice_path`
- **动作**：
  1. 设定日常指标
  2. 设计周度回顾
  3. 设定里程碑
- **输出**：`progress_tracking`

### Step 6: 常见挑战

- **输入**：`level_assessment`
- **动作**：
  1. 识别常见障碍
  2. 分析原因
  3. 提供解决方案
- **输出**：`common_challenges`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议超过能力范围的练习
2. **不得**忽视身心反应
3. **必须**建议循序渐进

### 软性约束（建议遵守）
1. 建议固定练习时间
2. 建议记录练习日记
3. 建议寻找练习伙伴

### 人工兜底点
- 当出现严重身心反应时，**必须**建议暂停
- 当有心理疾病史时，**必须**建议咨询专业人士

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `MD_WARNING_DISTRACTION` | 频繁分心 | 正常，温和带回 | 🟡 |
| `MD_WARNING_DISCOMFORT` | 身体不适 | 调整姿势 | 🟡 |
| `MD_ERROR_CRISIS` | 严重身心反应 | 暂停并寻求帮助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 水平已评估
- [ ] 练习路径已设计
- [ ] 技巧库已构建
- [ ] 每周计划已制定

### OVP 验证信号
- 冥想练习频率 ≥ 5 次/周
- 正念评分提升 ≥ 20%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "初学者入门",
    "prompt": "我想开始冥想，但不知道怎么入门",
    "context": "current_level=beginner, available_time=10",
    "assertions": [
      "level_assessment.current_level = beginner",
      "practice_path.current_phase.duration = 1-3个月",
      "technique_library 包含 呼吸观察"
    ],
    "expected_behavior": "为初学者设计入门路径",
    "critic_attack": "是否足够简单易行？"
  },
  {
    "id": "test-002",
    "name": "中级进阶",
    "prompt": "我已经练习呼吸观察3个月，想进一步提升",
    "context": "current_level=intermediate, practice_goal=focus",
    "assertions": [
      "level_assessment.areas_for_growth 已识别",
      "practice_path.next_phases 包含 开放觉知",
      "weekly_schedule.total_weekly_minutes >= 100"
    ],
    "expected_behavior": "为中级练习者设计进阶路径",
    "critic_attack": "是否考虑了个人差异？"
  },
  {
    "id": "test-003",
    "name": "压力缓解",
    "prompt": "我想用冥想来缓解工作压力",
    "context": "practice_goal=stress, available_time=15",
    "assertions": [
      "technique_library 包含 身体扫描和慈悲冥想",
      "weekly_schedule 安排了 减压练习",
      "common_challenges 包含 压力相关挑战"
    ],
    "expected_behavior": "针对压力缓解设计冥想计划",
    "critic_attack": "是否结合了其他减压方法？"
  }
]
```

---

## 🔗 关联文档

- [[元认知-Schema]] — 元认知觉察
- [[压力管理]] — 压力应对
- [[2026-06 睡眠优化执行手册]] — 睡眠改善
- [[心流状态激活]] — 专注力提升
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：水平评估 + 进阶路径 + 技巧库 + Self-Play |

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
