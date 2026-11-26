
description: |
  当用户需要进行重大决策推理、量化决策信念、检测认知偏差、构建反方论证时使用此 Skill。
  触发词包括：'决策分析'、'贝叶斯'、'认知偏差'、'反方论证'、'决策推理'、
  '先验后验'、'决策日志'、'风险评估'、'决策复盘'。当用户讨论投资决策、
  技术选型、项目优先级、职业选择等需要理性量化支撑的场景时，即使未直接说
  "决策推理"，也应使用此 Skill。不适用于简单日常决策（直接执行即可）。
  遇到重大决策时优先使用，而非凭直觉判断。

---

# uSkill-006: 决策推理

## 🎯 目标

> 将重大决策从直觉判断升级为结构化推理，集成贝叶斯量化、认知偏差检测、反方论证、逻辑校验四维能力，建立「先验→证据→反方→后验→决策→回测」的完整决策闭环。

**核心价值**：让每一次重大决策都有迹可循、可回测、可迭代，沉淀为长期复利的认知资产。

**适用场景**：
- 投资决策（标的筛选、仓位管理、止盈止损）
- 技术选型（架构方案、工具选择、云平台迁移）
- 项目优先级（OKR 设定、资源分配、砍需求）
- 职业选择（跳槽、创业、合作）
- 系统设计（架构决策、方案评审）

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `decision_question` | `string` | ✅ | — | 待决策问题（一句话清晰陈述） |
| `decision_type` | `enum` | ✅ | — | `strategic` / `tactical` / `operational` |
| `prior_belief` | `object` | ✅ | — | `{hypothesis: string, probability: float, basis: string, confidence: float}` |
| `evidence_list` | `array` | ✅ | — | `[{description, strength, reliability, direction}]` |
| `context` | `object` | ❌ | — | `{deadline, stakeholders, risk_tolerance}` |
| `skip_devil_advocate` | `boolean` | ❌ | `false` | 是否跳过反方论证（仅限操作级决策） |

**输入约束**：
- `prior_belief.probability` 范围 0-1
- `prior_belief.basis` 必须为非空（不允许凭空设定先验）
- `evidence_list` 至少包含 1 条证据
- `decision_type = strategic` 时**必须**执行反方论证

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话决策结论",
  "decision_id": "DR-YYYY-NNN",
  "decision_question": "string",
  "decision_type": "strategic|tactical|operational",

  "bayesian_analysis": {
    "prior": {
      "hypothesis": "string",
      "probability": "number",
      "basis": "string",
      "confidence": "number"
    },
    "evidence": [
      {
        "description": "string",
        "strength": "number",
        "reliability": "number",
        "direction": "supportive|contradictory|neutral",
        "bayes_factor": "number"
      }
    ],
    "posterior": {
      "probability": "number",
      "change": "number",
      "robustness": "fragile|stable|robust"
    },
    "sensitivity": {
      "key_variable": "string",
      "flip_threshold": "number",
      "conclusion_stable": true
    }
  },

  "cognitive_bias_check": {
    "confirmation_bias": {"detected": false, "evidence": "string"},
    "anchoring_bias": {"detected": false, "evidence": "string"},
    "overconfidence_bias": {"detected": false, "evidence": "string"},
    "availability_bias": {"detected": false, "evidence": "string"},
    "sunk_cost_bias": {"detected": false, "evidence": "string"},
    "loss_aversion_bias": {"detected": false, "evidence": "string"},
    "survivorship_bias": {"detected": false, "evidence": "string"},
    "overall_risk": "low|medium|high"
  },

  "devil_advocate": {
    "counter_arguments": [
      {
        "title": "string",
        "evidence": "string",
        "severity": "high|medium|low",
        "rebuttal_needed": true
      }
    ],
    "weakness_points": ["string"],
    "revised_confidence": "number"
  },

  "logical_validation": {
    "premises_valid": true,
    "inference_valid": true,
    "fallacies_detected": ["string"],
    "argument_structure": "deductive|inductive|abductive"
  },

  "decision_output": {
    "recommendation": "string",
    "action": "string",
    "stop_loss_condition": "string",
    "key_evidence_needed": ["string"],
    "confidence_level": "number",
    "caveats": ["string"]
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
  "error_code": "DR_ERROR_001",
  "error_message": "先验依据不足，无法进行贝叶斯分析",
  "suggestion": "请提供先验信念的历史数据或专家判断依据",
  "partial_result": {
    "bias_check": "已完成",
    "devil_advocate": "未执行"
  }
}
```

---

## 📋 执行步骤

### Step 1: 问题定义与假设空间构建

- **输入**：`decision_question` + `decision_type`
- **动作**：
  1. 将模糊决策问题拆解为可量化的假设
  2. 确保假设互斥且穷尽（MECE 原则）
  3. 确定决策边界（什么在范围内、什么不在）
- **输出**：结构化假设空间
- **分支条件**：
  - IF 假设不互斥 → 重新定义假设空间
  - IF 假设不穷尽 → 补充"其他"假设
  - IF 问题过于模糊 → 要求用户澄清
- **检查点**：✅ 验证假设满足 MECE 原则

### Step 2: 先验信念评估

- **输入**：`prior_belief`
- **动作**：
  1. 验证先验依据的有效性
  2. 评估先验置信度的合理性
  3. 检查是否存在先验偏差
- **输出**：经校验的先验信念
- **分支条件**：
  - IF 先验依据为空 → 输出 `DR_WARNING_PRIOR_WEAK` + 使用无信息先验（50%）
  - IF 先验概率 < 0.1 或 > 0.9 → 标记 `WARNING_EXTREME_PRIOR` + 建议重新评估
- **检查点**：✅ 验证先验有明确依据

### Step 3: 证据收集与贝叶斯更新

- **输入**：`evidence_list` + 经校验的先验
- **动作**：
  1. 逐条评估证据（强度 × 可靠性 → 贝叶斯因子）
  2. 顺序应用贝叶斯定理更新信念
  3. 记录每次更新的中间结果
- **输出**：后验概率分布 + 更新轨迹
- **分支条件**：
  - IF 存在矛盾证据 → 分别计算支持/反对路径的后验
  - IF 所有证据方向一致 → 正常更新
- **检查点**：✅ 验证贝叶斯因子计算正确

### Step 4: 认知偏差检测（7 维度）

- **输入**：完整的推理过程
- **动作**：系统性排查 7 种认知偏差

| 偏差 | 检测方法 | 修正建议 |
|------|----------|----------|
| 确认偏误 | 是否只关注支持性证据？ | 主动寻找反面证据 |
| 锚定效应 | 先验是否被初始信息过度锚定？ | 重新评估先验依据 |
| 过度自信 | 置信区间是否过窄？ | 扩大置信区间 |
| 可得性偏差 | 证据是否因易获取而被过度加权？ | 补充不易获取的证据 |
| 沉没成本 | 先验是否受已投入成本影响？ | 忽略已投入成本重新评估 |
| 损失厌恶 | 止损条件是否过于宽松？ | 设定客观止损标准 |
| 幸存者偏差 | 是否只看了成功案例？ | 补充失败案例数据 |

- **输出**：`cognitive_bias_check`（7 项检测结果）
- **检查点**：✅ 验证 7 项偏差全部检测

### Step 5: 反方论证（Devil's Advocate）

- **输入**：决策假设 + 支持证据 + 认知偏差检测结果
- **动作**：
  1. 构建 3 个最强反面论点
  2. 寻找反面证据
  3. 评估原决策的脆弱点
  4. 修正置信度
- **输出**：`devil_advocate` 报告
- **分支条件**：
  - IF `decision_type = operational` AND `skip_devil_advocate = true` → 跳过此步骤
  - IF `decision_type = strategic` → **必须**执行，且反方论证必须包含至少 1 个高严重度论点
- **检查点**：✅ 验证反方论证至少 3 个论点

### Step 6: 逻辑校验

- **输入**：完整推理链路
- **动作**：
  1. 验证前提有效性
  2. 验证推理有效性
  3. 检测逻辑谬误
- **输出**：`logical_validation`
- **常见谬误清单**：
  - 稻草人论证（歪曲对方观点）
  - 滑坡谬误（无根据的连锁推导）
  - 诉诸权威（仅因权威就接受）
  - 虚假二分（非黑即白）
  - 循环论证（用结论证明前提）
- **检查点**：✅ 验证推理链路无逻辑谬误

### Step 7: 敏感性分析

- **输入**：后验概率 + 关键变量
- **动作**：
  1. 识别关键变量（对后验影响最大的变量）
  2. 测试关键变量 ±50% 时后验变化
  3. 判断结论稳健性
- **输出**：`sensitivity` 分析结果
- **分支条件**：
  - IF 关键变量变化导致后验翻转 → 标记 `FRAGILE_CONCLUSION`
  - IF 后验变化 < 10% → 标记 `ROBUST_CONCLUSION`
- **检查点**：✅ 验证敏感性分析完成

### Step 8: 决策输出与回测设定

- **输入**：所有前序分析结果
- **动作**：
  1. 综合贝叶斯后验 + 反方论证 + 逻辑校验 → 生成决策建议
  2. 设定止损条件
  3. 设定回测时间点
  4. 生成决策日志
- **输出**：`decision_output` + 决策日志文件
- **检查点**：✅ 验证决策日志已写入 `01-BRAIN/12-模型/贝叶斯决策日志/`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. 先验概率**必须**有明确依据，不得凭空设定
2. 不利证据**不得**被忽略（确认偏误防范）
3. 所有概率估计**必须**标注置信区间
4. 后验概率**不得**直接等同于决策结论（概率是输入，决策是输出）
5. 战略决策**必须**执行反方论证
6. 决策日志**必须**写入指定路径，不可跳过

### 软性约束（建议遵守）
1. 建议每次决策后 3 个月进行回测
2. 建议月度汇总决策胜率
3. 建议季度校准先验信念库

### 人工兜底点
- 当 `decision_type = strategic` 时，最终决策**必须**经用户确认
- 当后验概率翻转时，**必须**暂停执行等待用户评估
- 当认知偏差整体风险 = high 时，**必须**标记并提醒用户

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `DR_WARNING_PRIOR_WEAK` | 先验依据为空 | 使用无信息先验（50%）+ 警告 | 🟡 |
| `DR_WARNING_EXTREME_PRIOR` | 先验概率 < 0.1 或 > 0.9 | 标记警告 + 建议重新评估 | 🟡 |
| `DR_WARNING_CONTRADICTORY` | 存在矛盾证据 | 分别计算两条路径 | 🟡 |
| `DR_ERROR_FRAGILE` | 敏感性分析显示结论脆弱 | 标记 `FRAGILE` + 建议补充证据 | 🔴 |
| `DR_ERROR_BIAS_HIGH` | 认知偏差整体风险 = high | 暂停执行 + 提醒用户 | 🔴 |
| `DR_ERROR_LOGIC_FALLACY` | 检测到逻辑谬误 | 标记谬误类型 + 建议修正 | 🔴 |
| `DR_ERROR_INCOMPLETE` | 输入参数不完整 | 输出缺失字段清单 + 要求补充 | 🔴 |

### 降级策略
- 当 Self-Play 不可用时，降级为单方案执行（无 Critic 验证）
- 当反方论证不可用时，降级为认知偏差检测 + 贝叶斯分析

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 字段类型与 Schema 一致
- [ ] 决策编号格式正确（DR-YYYY-NNN）

### 内容校验
- [ ] 先验有明确依据（非凭空设定）
- [ ] 不利证据未被忽略
- [ ] 贝叶斯因子计算正确
- [ ] 认知偏差 7 项检查完成
- [ ] 反方论证至少 3 个论点
- [ ] 逻辑校验无谬误
- [ ] 敏感性分析完成

### 合规校验
- [ ] 未将后验概率等同于决策结论
- [ ] 战略决策已执行反方论证
- [ ] 人工兜底点已正确触发
- [ ] 决策日志已写入指定路径

### OVP 验证信号
- 决策日志年度累计 ≥ 200 条
- 回测命中率 ≥ 60%（后验概率与实际结果偏差 < 20%）
- 认知偏差检查覆盖率 100%
- 反方论证执行率：战略 100%、战术 80%、操作 50%

---

## 🔄 迭代触发条件

### Self-Play 触发
- **频率**：monthly
- **触发条件**：
  - 每月自动触发（抽样 10% 决策日志）
  - 新增认知偏差类型时触发

### 版本升级触发
- minor 版本：新增检测维度或调整参数
- major 版本：改变推理框架或决策流程

### 废弃触发
- 当回测命中率连续 3 个月 < 50% 时，标记需要重构

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags/ovp/self_play）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥5 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 2 个现有 Skill 有双向链接（贝叶斯决策 + 认知偏差对抗）

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "投资决策-正常流程",
    "prompt": "分析是否应该买入某科技股",
    "context": "先验概率 60%，有 3 条支持证据和 1 条反对证据",
    "assertions": [
      "输出包含 bayesian_analysis",
      "posterior 概率已更新",
      "认知偏差 7 项检查完成",
      "反方论证至少 3 个论点",
      "决策日志已写入"
    ],
    "expected_behavior": "完整执行 8 步推理链路，输出结构化决策报告",
    "critic_attack": "先验 60% 是否有充分依据？是否过度乐观？"
  },
  {
    "id": "test-002",
    "name": "投资决策-先验依据不足",
    "prompt": "分析是否应该投资某个新领域",
    "context": "无历史数据，先验完全基于直觉",
    "assertions": [
      "输出包含 DR_WARNING_PRIOR_WEAK",
      "使用无信息先验（50%）",
      "建议补充先验依据"
    ],
    "expected_behavior": "识别先验不足，降级处理，给出警告",
    "critic_attack": "降级为 50% 是否合理？是否有更好的处理方式？"
  },
  {
    "id": "test-003",
    "name": "技术选型-反方论证",
    "prompt": "分析是否应该从 MySQL 迁移到 PostgreSQL",
    "context": "战略级决策，有 5 条支持证据",
    "assertions": [
      "输出包含 devil_advocate",
      "反方论证至少 3 个论点",
      "包含至少 1 个高严重度论点",
      "revised_confidence 已修正"
    ],
    "expected_behavior": "执行完整反方论证，修正置信度",
    "critic_attack": "反方论证是否足够有力？是否存在稻草人？"
  },
  {
    "id": "test-004",
    "name": "认知偏差检测-确认偏误",
    "prompt": "分析是否应该继续投入某项目",
    "context": "已投入 100 万，有 5 条支持证据但无反面证据",
    "assertions": [
      "检测到确认偏误",
      "检测到沉没成本偏差",
      "overall_risk = high",
      "建议暂停执行"
    ],
    "expected_behavior": "识别认知偏差，标记高风险，建议人工介入",
    "critic_attack": "是否正确识别了所有偏差？是否有遗漏？"
  },
  {
    "id": "test-005",
    "name": "敏感性分析-结论脆弱",
    "prompt": "分析市场趋势判断",
    "context": "后验概率 75%，但关键证据可靠性仅 0.3",
    "assertions": [
      "输出 sensitivity 分析",
      "标记 FRAGILE_CONCLUSION",
      "建议补充关键证据"
    ],
    "expected_behavior": "识别结论脆弱性，建议补充证据",
    "critic_attack": "脆弱性判断阈值是否合理？"
  }
]
```

---

## 🔗 关联文档

- [[uSkill-Schema-模板]] — 标准化模板
- [[uSkill-日程优化-v1]] — 贝叶斯推理方法论
- [[uSkill-agent-认知偏差对抗协议]] — 认知偏差检测框架
- [[贝叶斯决策日志模板]] — 决策日志格式
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览
- [[2026年度核心成果物与输出物清单（四大身份领域）]] — 年度交付物清单

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-22 | 1.0.0 | 初始版本：集成贝叶斯推理 + 认知偏差检测 + 反方论证 + 逻辑校验 + OVP + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板 · 关联：[[人生操作系统进化-Schema-v2]]*


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


**相关概念**：[[决策模型]] · [[70%信息即可决策]]

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
