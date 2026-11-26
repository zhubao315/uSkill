
description: |
  当用户需要建立成长心态、克服固定心态、从失败中学习、提升韧性时使用此 Skill。
  触发词包括：'成长心态'、'固定心态'、'韧性'、'失败学习'、'自我成长'。
  当用户讨论个人发展、学习、挑战时，
  即使未直接说"成长心态"，也应使用此 Skill。
  不适用于严重心理问题（建议专业帮助）。遇到心态调整需求时优先使用。

---

# uSkill-1001: 成长心态

## 🎯 目标

> 帮助用户从固定心态转变为成长心态，提升学习能力和韧性。

**核心价值**：心态决定行为。成长心态是持续进步的基础。

**适用场景**：
- 克服失败恐惧
- 接受新挑战
- 从批评中学习
- 提升学习效果
- 职业发展

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_situation` | `string` | ✅ | — | 当前情况描述 |
| `mindset_indicators` | `object` | ❌ | — | 心态指标 |
| `growth_goals` | `array` | ❌ | `[]` | 成长目标 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话成长建议",
  "growth_id": "GM-YYYY-MMDD-NNN",

  "mindset_assessment": {
    "current_mindset": "fixed|growth|mixed",
    "indicators": {
      "challenge_response": "avoids|embraces",
      "failure_response": "gives_up|persists",
      "criticism_response": "defensive|learns",
      "success_response": "threatened|inspired"
    },
    "areas_for_growth": ["string"]
  },

  "mindset_shift_strategies": {
    "awareness_building": {
      "triggers": ["string"],
      "reframing_techniques": ["string"],
      "self_talk_adjustments": ["string"]
    },
    "behavioral_experiments": [
      {
        "experiment": "string",
        "purpose": "string",
        "success_criteria": "string"
      }
    ],
    "environment_design": {
      "support_systems": ["string"],
      "challenge_sources": ["string"],
      "learning_resources": ["string"]
    }
  },

  "failure_recovery_framework": {
    "immediate_response": ["string"],
    "analysis_process": ["string"],
    "learning_extraction": ["string"],
    "forward_planning": ["string"]
  },

  "growth_practices": {
    "daily": ["string"],
    "weekly": ["string"],
    "monthly": ["string"]
  },

  "progress_tracking": {
    "metrics": ["string"],
    "milestones": [
      {
        "milestone": "string",
        "timeline": "string",
        "success_criteria": "string"
      }
    ]
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

### Step 1: 心态评估

- **输入**：`current_situation` + `mindset_indicators`
- **动作**：
  1. 评估当前心态类型
  2. 识别关键指标
  3. 确定成长领域
- **输出**：`mindset_assessment`
- **固定心态 vs 成长心态**：

| 维度 | 固定心态 | 成长心态 |
|------|----------|----------|
| 挑战 | 回避 | 拥抱 |
| 失败 | 放弃 | 坚持 |
| 批评 | 防御 | 学习 |
| 成功 | 威胁 | 启发 |
| 努力 | 无用 | 必要 |

### Step 2: 心态转变策略

- **输入**：`mindset_assessment`
- **动作**：
  1. 建立觉察
  2. 设计行为实验
  3. 设计支持环境
- **输出**：`mindset_shift_strategies`
- **心态转变技术**：

| 技术 | 描述 | 应用 |
|------|------|------|
| 觉察触发 | 识别固定心态时刻 | 日常观察 |
| 重构思维 | 用成长视角重新解读 | 自我对话 |
| 行为实验 | 尝试新的行为模式 | 刻意练习 |
| 环境设计 | 创造支持成长的环境 | 周围人和支持 |

### Step 3: 失败恢复框架

- **输入**：`mindset_assessment`
- **动作**：
  1. 设计即时应对
  2. 设计分析流程
  3. 设计学习提取
- **输出**：`failure_recovery_framework`

### Step 4: 成长实践

- **输入**：`mindset_shift_strategies`
- **动作**：
  1. 设计日常练习
  2. 安排每周练习
  3. 规划每月回顾
- **输出**：`growth_practices`

### Step 5: 进度跟踪

- **输入**：`growth_goals`
- **动作**：
  1. 定义跟踪指标
  2. 设定里程碑
  3. 制定回顾计划
- **输出**：`progress_tracking`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**强迫用户接受成长心态
2. **不得**忽视真实困难
3. **必须**尊重个体差异

### 软性约束（建议遵守）
1. 建议从小改变开始
2. 建议保持耐心
3. 建议寻找支持伙伴

### 人工兜底点
- 当存在严重心理问题时，**必须**建议专业帮助
- 当改变困难时，**必须**建议寻求支持

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `GM_WARNING_RESISTANCE` | 强烈抵抗 | 建议放慢速度 | 🟡 |
| `GM_WARNING_SETBACK` | 倒退 | 正常化，继续前进 | 🟡 |
| `GM_ERROR_CRISIS` | 严重心理问题 | 建议专业帮助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 心态已评估
- [ ] 转变策略已设计
- [ ] 失败恢复框架已制定
- [ ] 成长实践已安排

### OVP 验证信号
- 挑战接受率提升 ≥ 30%
- 失败后恢复时间缩短 ≥ 25%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "职业挑战",
    "prompt": "我害怕接受新项目，怕失败",
    "context": "current_situation=职业挑战, mindset_indicators={challenge_response:avoids}",
    "assertions": [
      "mindset_assessment.current_mindset = fixed",
      "mindset_shift_strategies.awareness_building.triggers 已列出",
      "failure_recovery_framework 已设计"
    ],
    "expected_behavior": "帮助克服挑战恐惧",
    "critic_attack": "是否真正理解了恐惧的根源？"
  },
  {
    "id": "test-002",
    "name": "从失败中学习",
    "prompt": "项目失败了，我感到很沮丧",
    "context": "current_situation=项目失败",
    "assertions": [
      "failure_recovery_framework.immediate_response 已提供",
      "failure_recovery_framework.learning_extraction 已设计",
      "growth_practices 包含 复盘练习"
    ],
    "expected_behavior": "帮助从失败中恢复和学习",
    "critic_attack": "是否给予了足够的情感支持？"
  },
  {
    "id": "test-003",
    "name": "接受批评",
    "prompt": "我很难接受他人的批评",
    "context": "mindset_indicators={criticism_response:defensive}",
    "assertions": [
      "mindset_shift_strategies.self_talk_adjustments 已提供",
      "behavioral_experiments 包含 接受批评实验",
      "growth_practices.daily 包含 反思练习"
    ],
    "expected_behavior": "帮助从批评中学习",
    "critic_attack": "是否区分了建设性和破坏性批评？"
  }
]
```

---

## 🔗 关联文档

- [[元认知-Schema]] — 元认知觉察
- [[uSkill-cognition-控制二分法]] — 控制与影响
- [[每日觉醒反思]] — 反思实践
- [[痛苦反思成长循环]] — 成长循环
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：心态评估 + 转变策略 + 失败恢复 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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
