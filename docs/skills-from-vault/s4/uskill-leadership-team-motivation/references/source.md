
description: |
  当用户需要激励团队、建立心理安全感、激发内在动机、提升团队敬业度时使用此 Skill。
  触发词包括：'团队激励'、'员工激励'、'敬业度'、'内在动机'、'心理安全'、
  '团队士气'、'激励策略'。当用户讨论团队管理、员工发展、组织文化时，
  即使未直接说"团队激励"，也应使用此 Skill。
  不适用于个人自我激励（使用其他 Skill）。遇到团队激励需求时优先使用。

---

# uSkill-402: 团队激励

## 🎯 目标

> 基于自我决定理论，建立激发内在动机的团队环境，提升团队敬业度和绩效。

**核心价值**：真正的激励来自内在，而非外在奖惩。领导者的核心任务是创造激发内在动机的环境。

**适用场景**：
- 团队士气低落
- 员工敬业度下降
- 新团队组建
- 变革期激励
- 高绩效团队建设

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `team_context` | `string` | ✅ | — | 团队情况描述 |
| `current_challenges` | `array` | ❌ | `[]` | 当前挑战 |
| `team_size` | `number` | ❌ | `10` | 团队规模 |
| `industry` | `string` | ❌ | `tech` | 行业类型 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话团队激励建议",
  "motivation_id": "TM-YYYY-MMDD-NNN",

  "team_assessment": {
    "current_state": "disengaged|neutral|engaged|high_performing",
    "key_challenges": ["string"],
    "motivation_level": "low|medium|high",
    "psychological_safety": "low|medium|high"
  },

  "intrinsic_motivation_analysis": {
    "autonomy": {
      "current_level": "low|medium|high",
      "improvement_areas": ["string"]
    },
    "mastery": {
      "current_level": "low|medium|high",
      "improvement_areas": ["string"]
    },
    "purpose": {
      "current_level": "low|medium|high",
      "improvement_areas": ["string"]
    }
  },

  "motivation_strategies": {
    "immediate_actions": [
      {
        "action": "string",
        "target": "autonomy|mastery|purpose",
        "implementation": "string",
        "expected_impact": "string"
      }
    ],
    "medium_term_initiatives": ["string"],
    "long_term_culture_changes": ["string"]
  },

  "psychological_safety_plan": {
    "assessment_method": "string",
    "improvement_strategies": ["string"],
    "metrics": ["string"]
  },

  "recognition_framework": {
    "types_of_recognition": ["string"],
    "frequency": "string",
    "personalization": "string"
  },

  "monitoring_plan": {
    "engagement_metrics": ["string"],
    "review_frequency": "string",
    "feedback_mechanisms": ["string"]
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

### Step 1: 团队状态评估

- **输入**：`team_context` + `current_challenges`
- **动作**：
  1. 评估当前团队状态
  2. 识别关键挑战
  3. 测量激励水平
- **输出**：`team_assessment`
- **团队状态指标**：

| 状态 | 特征 | 干预重点 |
|------|------|----------|
| 脱离 | 缺乏动力、消极 | 基础需求满足 |
| 中性 | 完成任务但无热情 | 激发内在动机 |
| 投入 | 主动积极、有热情 | 保持和深化 |
| 高绩效 | 超越期望、创新 | 挑战和成长 |

### Step 2: 内在动机分析

- **输入**：`team_assessment`
- **动作**：
  1. 评估自主性需求
  2. 评估胜任感需求
  3. 评估归属感需求
- **输出**：`intrinsic_motivation_analysis`
- **自我决定理论（SDT）**：

| 需求 | 描述 | 满足方式 |
|------|------|----------|
| 自主性 | 控制自己工作的能力 | 授权、选择权 |
| 胜任感 | 感觉自己有能力 | 挑战、反馈 |
| 归属感 | 与他人连接 | 团队活动、认可 |

### Step 3: 激励策略生成

- **输入**：`intrinsic_motivation_analysis`
- **动作**：
  1. 生成即时行动
  2. 制定中期计划
  3. 规划长期文化
- **输出**：`motivation_strategies`

### Step 4: 心理安全建设

- **输入**：`team_assessment`
- **动作**：
  1. 评估心理安全水平
  2. 制定提升策略
  3. 设定监控指标
- **输出**：`psychological_safety_plan`
- **心理安全建设策略**：

| 策略 | 描述 |
|------|------|
| 承认错误 | 领导者先承认自己的错误 |
| 欢迎提问 | 鼓励团队成员提问 |
| 包容失败 | 将失败视为学习机会 |
| 尊重差异 | 尊重不同观点和背景 |

### Step 5: 认可框架

- **输入**：`intrinsic_motivation_analysis`
- **动作**：
  1. 设计认可类型
  2. 确定频率
  3. 个性化方案
- **输出**：`recognition_framework`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**仅依赖外在激励（奖金、惩罚）
2. **不得**忽视个体差异
3. **必须**建立长期文化而非短期刺激

### 软性约束（建议遵守）
1. 建议定期进行员工满意度调查
2. 建议一对一沟通了解个体需求
3. 建议将激励融入日常工作

### 人工兜底点
- 当团队出现严重士气问题时，**必须**进行深度诊断
- 当核心员工有离职风险时，**必须**立即干预

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `TM_WARNING_LOW_SAFETY` | 心理安全水平低 | 建议优先建设安全 | 🟡 |
| `TM_WARNING_BURNOUT` | 团队倦怠迹象 | 建议减负和恢复 | 🟡 |
| `TM_ERROR_CRISIS` | 团队危机状态 | 建议立即干预 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 团队状态已评估
- [ ] 内在动机已分析
- [ ] 激励策略已生成
- [ ] 心理安全计划已制定

### OVP 验证信号
- 团队敬业度 ≥ 80%
- 员工满意度 ≥ 4.0/5.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "团队士气低落",
    "prompt": "我们团队最近士气很低，大家都在抱怨",
    "context": "current_challenges=[士气低落, 抱怨多]",
    "assertions": [
      "team_assessment.current_state = disengaged",
      "intrinsic_motivation_analysis 包含 三个需求分析",
      "motivation_strategies.immediate_actions 已生成"
    ],
    "expected_behavior": "诊断士气问题，提供激励策略",
    "critic_attack": "是否正确诊断了根本原因？"
  },
  {
    "id": "test-002",
    "name": "新团队组建",
    "prompt": "我刚接手一个新团队，需要建立团队文化",
    "context": "team_size=15, industry=tech",
    "assertions": [
      "team_assessment 包含 初始状态评估",
      "psychological_safety_plan 已制定",
      "recognition_framework 已设计"
    ],
    "expected_behavior": "为新团队设计激励和文化建设方案",
    "critic_attack": "是否考虑了团队的多样性？"
  },
  {
    "id": "test-003",
    "name": "高绩效维持",
    "prompt": "我们团队绩效很好，但担心员工倦怠",
    "context": "current_challenges=[高绩效, 倦怠风险]",
    "assertions": [
      "team_assessment.current_state = high_performing",
      "motivation_strategies 包含 预防倦怠策略",
      "monitoring_plan 包含 倦怠预警指标"
    ],
    "expected_behavior": "在保持高绩效的同时预防倦怠",
    "critic_attack": "是否过度关注维持而忽视创新？"
  }
]
```

---

## 🔗 关联文档

- [[决策领导力]] — 决策能力
- [[冲突管理]] — 冲突解决
- [[心理安全建设]] — 心理安全
- [[教练式辅导]] — 辅导能力
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：SDT分析 + 心理安全 + 认可框架 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务] for [业务阶段], with [资源约束], leaning toward [策略框架/执行路径]."

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
| ""先做再说"" | "方向错了，执行力越强死得越快" |
| ""用户说想要这个"" | "用户说的是解决方案，不是需求本身" |
| ""竞品都在做"" | "竞品犯错不意味着你也应该犯" |
| ""这个市场很大"" | "大市场≠你能切到的市场" |

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


**相关概念**：[[管理者是园丁而非监工]] · [[心理安全]]

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
