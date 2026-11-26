
description: |
  当用户需要解决团队冲突、处理人际矛盾、进行艰难对话、调解分歧时使用此 Skill。
  触发词包括：'冲突'、'矛盾'、'争执'、'调解'、'艰难对话'、'分歧'、
  '团队冲突'、'人际冲突'。当用户讨论团队管理、人际关系、谈判时，
  即使未直接说"冲突管理"，也应使用此 Skill。
  不适用于简单的意见分歧（直接沟通即可）。遇到需要调解的冲突时优先使用。

---

# uSkill-403: 冲突管理

## 🎯 目标

> 以协作型方式解决冲突，维护关系的同时解决问题，将冲突转化为成长机会。

**核心价值**：冲突不是坏事，处理不当才是。好的冲突管理能增强团队凝聚力。

**适用场景**：
- 团队成员间冲突
- 跨部门协作冲突
- 上下级冲突
- 客户关系冲突
- 合作伙伴关系冲突

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `conflict_description` | `string` | ✅ | — | 冲突情况描述 |
| `parties_involved` | `array` | ✅ | — | 冲突各方 |
| `conflict_type` | `enum` | ❌ | `unknown` | `task` / `relationship` / `value` / `structural` |
| `relationship_importance` | `enum` | ❌ | `high` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话冲突管理建议",
  "conflict_id": "CR-YYYY-MMDD-NNN",

  "conflict_analysis": {
    "type": "task|relationship|value|structural",
    "root_causes": ["string"],
    "escalation_level": "latent|manifest|severe",
    "emotional_intensity": "low|medium|high",
    "stakeholder_positions": [
      {
        "party": "string",
        "position": "string",
        "interests": ["string"],
        "needs": ["string"],
        "emotional_state": "string"
      }
    ]
  },

  "resolution_approach": {
    "recommended_approach": "collaborative|compromising|accommodating|avoiding|competing",
    "rationale": "string",
    "prerequisites": ["string"]
  },

  "mediation_plan": {
    "pre_mediation": ["string"],
    "opening": "string",
    "exploration_phase": ["string"],
    "problem_solving_phase": ["string"],
    "agreement_phase": ["string"]
  },

  "communication_framework": {
    "non_violent_communication": {
      "observations": "string",
      "feelings": "string",
      "needs": "string",
      "requests": "string"
    },
    "active_listening_techniques": ["string"],
    "de_escalation_strategies": ["string"]
  },

  "agreement_template": {
    "shared_understanding": "string",
    "action_items": [
      {
        "party": "string",
        "action": "string",
        "deadline": "string",
        "follow_up": "string"
      }
    ],
    "prevention_measures": ["string"]
  },

  "follow_up_plan": {
    "check_in_schedule": "string",
    "success_metrics": ["string"],
    "escalation_path": "string"
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

### Step 1: 冲突分析

- **输入**：`conflict_description` + `parties_involved`
- **动作**：
  1. 识别冲突类型
  2. 分析根本原因
  3. 评估升级程度
- **输出**：`conflict_analysis`
- **冲突类型**：

| 类型 | 特征 | 解决方向 |
|------|------|----------|
| 任务冲突 | 对工作内容/方法的分歧 | 明确目标和标准 |
| 关系冲突 | 人际间的不和 | 改善沟通和理解 |
| 价值冲突 | 价值观/信念的差异 | 寻找共同点 |
| 结构冲突 | 资源/权力的不平衡 | 调整结构或资源 |

### Step 2: 解决方案选择

- **输入**：`conflict_analysis`
- **动作**：
  1. 评估各种解决方案
  2. 选择最适合的方案
  3. 准备前提条件
- **输出**：`resolution_approach`
- **冲突解决策略**：

| 策略 | 适用情境 | 优点 | 缺点 |
|------|----------|------|------|
| 协作 | 双方利益都重要 | 双赢 | 耗时 |
| 妥协 | 需要快速解决 | 公平 | 双方都不满意 |
| 迁就 | 关系比结果重要 | 维护关系 | 可能被利用 |
| 回避 | 问题不重要 | 节省精力 | 问题可能恶化 |
| 竞争 | 紧急情况 | 快速 | 损害关系 |

### Step 3: 调解计划

- **输入**：`resolution_approach`
- **动作**：
  1. 制定调解流程
  2. 准备开场白
  3. 设计探索和解决问题阶段
- **输出**：`mediation_plan`
- **调解流程**：

| 阶段 | 目的 | 技巧 |
|------|------|------|
| 调解前 | 准备和单独沟通 | 了解各方立场 |
| 开场 | 建立安全氛围 | 设定规则 |
| 探索 | 理解各方需求 | 积极倾听 |
| 解决 | 生成解决方案 | 头脑风暴 |
| 达成 | 形成协议 | 明确细节 |

### Step 4: 沟通框架

- **输入**：`conflict_analysis`
- **动作**：
  1. 应用非暴力沟通
  2. 使用积极倾听技巧
  3. 使用降级策略
- **输出**：`communication_framework`
- **非暴力沟通（NVC）**：

| 步骤 | 内容 | 示例 |
|------|------|------|
| 观察 | 描述事实，不评判 | "我看到报告迟交了3天" |
| 感受 | 表达感受 | "我感到担心" |
| 需要 | 说明需要 | "因为我需要按时完成项目" |
| 请求 | 提出具体请求 | "你能告诉我原因并给出新时间吗？" |

### Step 5: 协议制定

- **输入**：所有前序输出
- **动作**：
  1. 总结共同理解
  2. 制定行动计划
  3. 设计预防措施
- **输出**：`agreement_template`

### Step 6: 跟进计划

- **输入**：`agreement_template`
- **动作**：
  1. 制定跟进时间表
  2. 设定成功指标
  3. 准备升级路径
- **输出**：`follow_up_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**偏袒任何一方（作为调解者时）
2. **不得**忽视情绪因素
3. **必须**确保各方都有发言机会

### 软性约束（建议遵守）
1. 建议先单独了解各方立场
2. 建议在中立场所进行调解
3. 建议书面记录协议

### 人工兜底点
- 当涉及骚扰或歧视时，**必须**建议正式投诉流程
- 当冲突升级到威胁程度时，**必须**建议安保介入

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `CR_WARNING_ESCALATION` | 冲突升级 | 建议暂停冷却 | 🟡 |
| `CR_WARNING_HOSTILITY` | 敌对情绪高 | 建议分开沟通 | 🟡 |
| `CR_ERROR_THREAT` | 威胁行为 | 建议安保介入 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 冲突类型已识别
- [ ] 根本原因已分析
- [ ] 解决方案已选择
- [ ] 协议已制定

### OVP 验证信号
- 冲突解决满意度 ≥ 85%
- 关系维护成功率 ≥ 80%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "任务冲突",
    "prompt": "两个团队成员对项目方向有不同意见，争执不下",
    "context": "conflict_type=task, parties=[成员A, 成员B]",
    "assertions": [
      "conflict_analysis.type = task",
      "resolution_approach.recommended_approach = collaborative",
      "mediation_plan 已制定"
    ],
    "expected_behavior": "以协作方式解决任务冲突",
    "critic_attack": "是否正确识别了冲突类型？"
  },
  {
    "id": "test-002",
    "name": "关系冲突",
    "prompt": "两个同事关系很差，经常互相指责",
    "context": "conflict_type=relationship, emotional_intensity=high",
    "assertions": [
      "conflict_analysis.type = relationship",
      "communication_framework.de_escalation_strategies 已生成",
      "agreement_template.prevention_measures 已列出"
    ],
    "expected_behavior": "处理关系冲突，改善沟通",
    "critic_attack": "是否充分考虑了情绪因素？"
  },
  {
    "id": "test-003",
    "name": "跨部门冲突",
    "prompt": "产品和技术部门对需求优先级有严重分歧",
    "context": "conflict_type=structural, parties=[产品部, 技术部]",
    "assertions": [
      "conflict_analysis.type = structural",
      "resolution_approach 包含 结构性解决方案",
      "agreement_template.action_items 包含 流程改进"
    ],
    "expected_behavior": "解决结构性冲突，改善协作流程",
    "critic_attack": "是否考虑了权力不平衡的因素？"
  }
]
```

---

## 🔗 关联文档

- [[决策领导力]] — 决策能力
- [[团队激励]] — 团队管理
- [[非暴力沟通]] — 沟通技巧
- [[心理安全建设]] — 心理安全
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：冲突分析 + 解决策略 + 调解流程 + Self-Play |

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


**相关概念**：[[心理安全]] · [[积极倾听]] · [[社会意识]]

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
