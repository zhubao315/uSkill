
description: |
  当用户需要改善人际关系、学习沟通技巧、处理冲突、建立深度连接时使用此 Skill。
  触发词包括：'人际关系'、'沟通'、'亲密关系'、'冲突'、'边界'、
  '非暴力沟通'、'关系改善'。当用户讨论家庭、朋友、同事关系时，
  即使未直接说"人际关系"，也应使用此 Skill。
  不适用于严重关系问题（建议专业咨询）。遇到日常关系改善需求时优先使用。

---

# uSkill-305: 人际关系

## 🎯 目标

> 基于心理学原理，提升沟通技巧，建立和维护健康的人际关系。

**核心价值**：人际关系是幸福感的最重要预测因素。好的关系需要刻意经营。

**适用场景**：
- 亲密关系维护
- 家庭关系改善
- 职场关系建设
- 友谊深化
- 冲突解决

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `relationship_type` | `enum` | ✅ | — | `romantic` / `family` / `friendship` / `work` |
| `current_challenges` | `array` | ❌ | `[]` | 当前挑战 |
| `relationship_context` | `string` | ❌ | — | 关系背景描述 |
| `improvement_goal` | `string` | ❌ | — | 改善目标 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话关系建议",
  "relationship_id": "IR-YYYY-MMDD-NNN",

  "relationship_assessment": {
    "current_state": "distant|neutral|connected|intimate",
    "strengths": ["string"],
    "areas_for_growth": ["string"],
    "communication_patterns": "string"
  },

  "communication_framework": {
    "non_violent_communication": {
      "observations": "string",
      "feelings": "string",
      "needs": "string",
      "requests": "string"
    },
    "active_listening": {
      "techniques": ["string"],
      "common_mistakes": ["string"]
    },
    "assertive_communication": {
      "i_statements": ["string"],
      "boundary_setting": ["string"]
    }
  },

  "relationship_building": {
    "emotional_intimacy": {
      "practices": ["string"],
      "exercises": ["string"]
    },
    "quality_time": {
      "activities": ["string"],
      "frequency": "string"
    },
    "appreciation_expression": {
      "methods": ["string"],
      "frequency": "string"
    }
  },

  "conflict_resolution": {
    "prevention": ["string"],
    "in_the_moment": ["string"],
    "repair_conversation": {
      "steps": ["string"],
      "template": "string"
    }
  },

  "boundary_setting": {
    "types": ["string"],
    "communication_scripts": ["string"],
    "enforcement_strategies": ["string"]
  },

  "growth_plan": {
    "daily_practices": ["string"],
    "weekly_exercises": ["string"],
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

### Step 1: 关系评估

- **输入**：`relationship_type` + `relationship_context`
- **动作**：
  1. 评估当前关系状态
  2. 识别优势和成长领域
  3. 分析沟通模式
- **输出**：`relationship_assessment`
- **关系状态指标**：

| 状态 | 特征 | 改善重点 |
|------|------|----------|
| 疏远 | 缺乏连接 | 建立连接 |
| 中性 | 平淡但稳定 | 增加深度 |
| 连接 | 有情感连接 | 维护和深化 |
| 亲密 | 深度连接 | 保持和成长 |

### Step 2: 沟通框架

- **输入**：`relationship_assessment`
- **动作**：
  1. 应用非暴力沟通
  2. 练习积极倾听
  3. 学习自信沟通
- **输出**：`communication_framework`
- **非暴力沟通四要素**：

| 要素 | 内容 | 示例 |
|------|------|------|
| 观察 | 描述事实 | "你昨晚没回家" |
| 感受 | 表达感受 | "我感到担心" |
| 需要 | 说明需要 | "因为我需要安全感" |
| 请求 | 提出请求 | "你能提前告诉我吗？" |

### Step 3: 关系建设

- **输入**：`relationship_type` + `improvement_goal`
- **动作**：
  1. 设计情感亲密练习
  2. 安排高质量时间
  3. 设计表达欣赏的方式
- **输出**：`relationship_building`

### Step 4: 冲突解决

- **输入**：`current_challenges`
- **动作**：
  1. 设计冲突预防策略
  2. 提供即时应对技巧
  3. 设计修复对话模板
- **输出**：`conflict_resolution`

### Step 5: 边界设定

- **输入**：`relationship_type`
- **动作**：
  1. 识别需要设定的边界
  2. 提供沟通话术
  3. 制定执行策略
- **输出**：`boundary_setting`

### Step 6: 成长计划

- **输入**：所有前序输出
- **动作**：
  1. 设计日常练习
  2. 安排每周练习
  3. 设定里程碑
- **输出**：`growth_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视关系中的虐待
2. **不得**强迫改变对方
3. **必须**尊重个体差异

### 软性约束（建议遵守）
1. 建议从小改变开始
2. 建议保持耐心
3. 建议寻求专业帮助（必要时）

### 人工兜底点
- 当存在虐待关系时，**必须**建议专业帮助
- 当关系问题严重时，**必须**建议 couples therapy

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IR_WARNING_STAGNANT` | 关系停滞 | 建议增加互动 | 🟡 |
| `IR_WARNING_CONFLICT` | 频繁冲突 | 建议学习冲突解决 | 🟡 |
| `IR_ERROR_ABUSE` | 存在虐待 | 建议专业帮助 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 关系已评估
- [ ] 沟通框架已提供
- [ ] 关系建设计划已制定
- [ ] 成长计划已设计

### OVP 验证信号
- 关系满意度 ≥ 80%
- 冲突频率降低 ≥ 30%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "亲密关系改善",
    "prompt": "我和伴侣最近经常吵架",
    "context": "relationship_type=romantic, current_challenges=[频繁争吵]",
    "assertions": [
      "relationship_assessment.current_state 已评估",
      "communication_framework.non_violent_communication 已提供",
      "conflict_resolution.repair_conversation.template 已设计"
    ],
    "expected_behavior": "提供改善亲密关系的建议",
    "critic_attack": "是否考虑了双方的责任？"
  },
  {
    "id": "test-002",
    "name": "职场关系",
    "prompt": "如何与难相处的同事合作",
    "context": "relationship_type=work, current_challenges=[合作困难]",
    "assertions": [
      "communication_framework.assertive_communication 已提供",
      "boundary_setting.types 已列出",
      "conflict_resolution.in_the_moment 已提供"
    ],
    "expected_behavior": "改善职场人际关系",
    "critic_attack": "是否考虑了职场权力动态？"
  },
  {
    "id": "test-003",
    "name": "家庭关系",
    "prompt": "如何与父母建立更好的关系",
    "context": "relationship_type=family, improvement_goal=增进理解",
    "assertions": [
      "relationship_building.emotional_intimacy.practices 已列出",
      "growth_plan.daily_practices 包含 表达欣赏",
      "communication_framework.active_listening.techniques 已提供"
    ],
    "expected_behavior": "改善家庭关系",
    "critic_attack": "是否考虑了代际差异？"
  }
]
```

---

## 🔗 关联文档

- [[冲突管理]] — 冲突解决
- [[压力管理]] — 压力应对
- [[团队激励]] — 团队关系
- [[教练式辅导]] — 引导他人
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：NVC + 积极倾听 + 边界设定 + Self-Play |

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


**相关概念**：[[社会关系与健康]] · [[多元思维模型在人际关系与信任纽带建立中的应用]]

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
