
description: |
  当用户需要分析论证、识别偏见、评估证据、进行独立思考时使用此 Skill。
  触发词包括：'批判性思维'、'论证分析'、'偏见'、'证据评估'、'独立思考'。
  当用户讨论决策、分析、辩论时，
  即使未直接说"批判性思维"，也应使用此 Skill。
  不适用于简单事实核查（使用信息污染检测）。遇到深度分析时优先使用。

---

# uSkill-110: 批判性思维

## 🎯 目标

> 帮助用户进行独立、客观、深入的思考，识别和避免思维陷阱。

**核心价值**：批判性思维是信息时代的生存技能。它帮助我们区分事实与观点、逻辑与情绪。

**适用场景**：
- 决策分析
- 论证评估
- 偏见识别
- 证据评估
- 信息筛选

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `argument_or_claim` | `string` | ✅ | — | 需要分析的论点或主张 |
| `context` | `string` | ❌ | — | 背景信息 |
| `analysis_depth` | `enum` | ❌ | `standard` | `shallow` / `standard` / `deep` |
| `focus_areas` | `array` | ❌ | `all` | 关注的分析领域 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话批判性分析结论",
  "critical_id": "CT-YYYY-MMDD-NNN",

  "argument_analysis": {
    "premises": [
      {
        "premise": "string",
        "type": "factual|value|assumption",
        "evidence": "string",
        "strength": "strong|moderate|weak"
      }
    ],
    "conclusion": "string",
    "inference_quality": "valid|invalid|uncertain",
    "logical_gaps": ["string"]
  },

  "bias_detection": {
    "detected_biases": [
      {
        "bias": "string",
        "description": "string",
        "evidence": "string",
        "impact": "low|medium|high"
      }
    ],
    "overall_bias_risk": "low|medium|high",
    "debiasing_suggestions": ["string"]
  },

  "evidence_evaluation": {
    "evidence_quality": {
      "relevance": "high|medium|low",
      "sufficiency": "sufficient|insufficient|mixed",
      "reliability": "high|medium|low",
      "currency": "current|somewhat_outdated|outdated"
    },
    "missing_evidence": ["string"],
    "additional_evidence_needed": ["string"]
  },

  "alternative_perspectives": [
    {
      "perspective": "string",
      "argument": "string",
      "strength": "string",
      "weakness": "string"
    }
  ],

  "critical_questions": [
    {
      "question": "string",
      "purpose": "string",
      "expected_insight": "string"
    }
  ],

  "reasoning_framework": {
    "inductive_reasoning": "string",
    "deductive_reasoning": "string",
    "abductive_reasoning": "string"
  },

  "conclusion_assessment": {
    "overall_quality": "strong|moderate|weak",
    "confidence_level": "number",
    "key_caveats": ["string"],
    "recommendation": "string"
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

### Step 1: 论证分析

- **输入**：`argument_or_claim`
- **动作**：
  1. 识别前提
  2. 识别结论
  3. 评估推理质量
- **输出**：`argument_analysis`
- **论证结构**：

| 部分 | 描述 | 评估要点 |
|------|------|----------|
| 前提 | 支撑结论的基础 | 是否真实、相关 |
| 推理 | 从前提到结论的过程 | 是否有效、充分 |
| 结论 | 论证的最终主张 | 是否合理、有说服力 |

### Step 2: 偏见检测

- **输入**：`argument_analysis`
- **动作**：
  1. 系统性排查偏见
  2. 评估偏见影响
  3. 提供去偏见建议
- **输出**：`bias_detection`
- **常见认知偏见**：

| 偏见 | 描述 | 检测方法 |
|------|------|----------|
| 确认偏误 | 寻找支持性证据 | 是否忽略反面证据 |
| 锚定效应 | 过度依赖初始信息 | 是否受第一印象影响 |
| 可得性偏差 | 高估易获取信息 | 是否过度依赖生动案例 |
| 从众效应 | 随大流 | 是否因多数人相信就相信 |

### Step 3: 证据评估

- **输入**：`argument_analysis.premises`
- **动作**：
  1. 评估证据质量
  2. 识别缺失证据
  3. 确定还需要什么证据
- **输出**：`evidence_evaluation`

### Step 4: 替代视角

- **输入**：`argument_or_claim`
- **动作**：
  1. 寻找不同观点
  2. 评估每个视角
  3. 平衡各方论证
- **输出**：`alternative_perspectives`

### Step 5: 关键问题

- **输入**：`argument_analysis` + `bias_detection`
- **动作**：
  1. 设计批判性问题
  2. 明确提问目的
  3. 预期洞察
- **输出**：`critical_questions`
- **批判性问题库**：

| 问题类型 | 示例问题 |
|----------|----------|
| 来源 | 信息来源可靠吗？ |
| 证据 | 有什么证据支持？ |
| 推理 | 推理过程合理吗？ |
| 假设 | 隐含假设是什么？ |
| 替代 | 有没有其他解释？ |
| 影响 | 谁会受影响？ |

### Step 6: 推理框架

- **输入**：`argument_analysis`
- **动作**：
  1. 分析归纳推理
  2. 分析演绎推理
  3. 分析溯因推理
- **输出**：`reasoning_framework`

### Step 7: 结论评估

- **输入**：所有前序输出
- **动作**：
  1. 综合评估质量
  2. 确定置信水平
  3. 列出注意事项
- **输出**：`conclusion_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**预设立场
2. **不得**忽视反面证据
3. **必须**保持客观公正

### 软性约束（建议遵守）
1. 建议考虑多个视角
2. 建议区分事实与观点
3. 建议保持开放心态

### 人工兜底点
- 当涉及重大决策时，**必须**建议多方验证
- 当信息不确定时，**必须**标注不确定性

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `CT_WARNING_BIAS` | 检测到偏见 | 标记并建议去偏见 | 🟡 |
| `CT_WARNING_WEAK_EVIDENCE` | 证据不足 | 建议补充证据 | 🟡 |
| `CT_ERROR_NO_ARGUMENT` | 无法识别论证 | 要求澄清 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 论证已分析
- [ ] 偏见已检测
- [ ] 证据已评估
- [ ] 替代视角已考虑

### OVP 验证信号
- 偏见识别率 ≥ 80%
- 论证分析准确率 ≥ 85%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "新闻报道分析",
    "prompt": "分析这篇新闻报道的可信度",
    "context": "argument_or_claim=新闻报道内容",
    "assertions": [
      "argument_analysis.premises 至少 2 个",
      "bias_detection.detected_biases 已列出",
      "evidence_evaluation.evidence_quality 已评估"
    ],
    "expected_behavior": "全面分析新闻报道的可信度",
    "critic_attack": "是否保持了客观性？"
  },
  {
    "id": "test-002",
    "name": "商业决策分析",
    "prompt": "评估这个商业提案的论证质量",
    "context": "argument_or_claim=商业提案",
    "assertions": [
      "argument_analysis.inference_quality 已评估",
      "alternative_perspectives 至少 2 个替代视角",
      "conclusion_assessment.recommendation 已给出"
    ],
    "expected_behavior": "评估商业提案的论证质量",
    "critic_attack": "是否考虑了所有风险？"
  },
  {
    "id": "test-003",
    "name": "学术论文分析",
    "prompt": "批判性分析这篇学术论文",
    "context": "argument_or_claim=学术论文结论",
    "analysis_depth=deep",
    "assertions": [
      "argument_analysis.premises 包含 研究方法评估",
      "evidence_evaluation.missing_evidence 已列出",
      "critical_questions 至少 5 个关键问题"
    ],
    "expected_behavior": "深度分析学术论文",
    "critic_attack": "是否真正理解了研究方法？"
  }
]
```

---

## 🔗 关联文档

- [[逻辑谬误检测]] — 逻辑分析
- [[uSkill-agent-认知偏差对抗协议]] — 偏见对抗
- [[决策推理-Schema]] — 决策框架
- [[信息污染检测]] — 信息验证
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：论证分析 + 偏见检测 + 证据评估 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


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


**相关概念**：[[事实与观点]]

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
