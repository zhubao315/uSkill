
# 🎯 目标

运用概率思维方法论，在不确定性环境下进行结构化决策，包括先验概率设定、贝叶斯信念更新、期望值计算和概率校准，为投资决策、风险评估、不确定性决策和预测校准提供理性的分析框架。

**核心价值**：将模糊的不确定性转化为可计算的概率分布，避免确定性偏差和过度自信。

**适用场景**：投资标的评估、项目风险量化、预测校准训练、战略决策的不确定性分析、医学/法律中的证据评估。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `decision_context` | string | 是 | - | 需要概率分析的决策场景描述 |
| `possible_outcomes` | list | 是 | - | 可能结果列表，每个结果包含描述和初始判断 |
| `prior_beliefs` | object | 否 | {} | 已有的先验信念（概率分布或主观判断） |
| `new_evidence` | list | 否 | [] | 新证据列表，用于贝叶斯更新 |
| `evidence_reliability` | object | 否 | {} | 证据可靠性评估（每个证据的可信度） |
| `risk_tolerance` | enum | 否 | "moderate" | 风险偏好：conservative / moderate / aggressive |
| `time_horizon` | string | 否 | "" | 决策的时间跨度 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `possible_outcomes` 至少包含 2 个互斥结果
- `new_evidence` 中的每个证据必须有 `evidence_reliability` 对应评估
- `prior_beliefs` 如果提供，概率之和必须为 1.0（±0.01 容差）
- `risk_tolerance` 影响期望值计算中的风险调整权重

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "decision_framing": {
      "type": "object",
      "properties": {
        "question": {"type": "string"},
        "time_horizon": {"type": "string"},
        "key_uncertainties": {"type": "array", "items": {"type": "string"}},
        "reference_class": {"type": "string"}
      }
    },
    "probability_distribution": {
      "type": "object",
      "properties": {
        "outcomes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "outcome": {"type": "string"},
              "prior_probability": {"type": "number", "minimum": 0, "maximum": 1},
              "evidence_impact": {"type": "array", "items": {"type": "object"}},
              "posterior_probability": {"type": "number", "minimum": 0, "maximum": 1},
              "confidence_level": {"type": "string", "enum": ["high", "medium", "low"]}
            }
          }
        },
        "total_probability": {"type": "number"},
        "distribution_shape": {"type": "string"}
      }
    },
    "bayesian_update_log": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "evidence": {"type": "string"},
          "reliability": {"type": "number", "minimum": 0, "maximum": 1},
          "likelihood_ratio": {"type": "number"},
          "prior": {"type": "number"},
          "posterior": {"type": "number"},
          "update_magnitude": {"type": "string", "enum": ["large", "moderate", "small"]}
        }
      }
    },
    "expected_value_analysis": {
      "type": "object",
      "properties": {
        "outcomes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "outcome": {"type": "string"},
              "probability": {"type": "number"},
              "value": {"type": "number"},
              "expected_contribution": {"type": "number"}
            }
          }
        },
        "total_expected_value": {"type": "number"},
        "risk_adjusted_value": {"type": "number"},
        "variance": {"type": "number"},
        "downside_risk": {"type": "number"}
      }
    },
    "calibration_check": {
      "type": "object",
      "properties": {
        "overconfidence_risk": {"type": "string", "enum": ["high", "medium", "low", "none"]},
        "base_rate neglect": {"type": "boolean"},
        "availability_bias_risk": {"type": "string", "enum": ["high", "medium", "low", "none"]},
        "suggested_calibration": {"type": "string"}
      }
    },
    "decision_recommendation": {
      "type": "object",
      "properties": {
        "recommended_option": {"type": "string"},
        "reasoning": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "sensitivity_factors": {"type": "array", "items": {"type": "string"}},
        "pre_commitment": {"type": "string"}
      }
    },
    "thinking_models_applied": {"type": "array", "items": {"type": "string"}}
  }
}
```

## 异常输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "error": {"type": "string"},
    "error_code": {"type": "string"},
    "suggestion": {"type": "string"},
    "partial_result": {"type": "object"}
  }
}
```

---

## 📋 执行步骤

## Step 1: 决策框架构建

**输入**：`decision_context` + `possible_outcomes` + `time_horizon`

**动作**：
1. 精确表述需要回答的概率问题
2. 界定时间范围和决策窗口
3. 识别关键不确定性因素
4. 确定参考类别（reference class）

**输出**：决策框架文档

**检查点**：问题是否可以被概率化表述？是否识别了所有关键不确定性？

**IF** `decision_context` 无法转化为概率问题 → **THEN** 返回提示：建议将问题表述为"X 发生的概率是多少"
**IF** `time_horizon` 为空 → **THEN** 根据决策类型推断合理时间跨度
**ELSE** 进入 Step 2

---

## Step 2: 先验概率设定

**输入**：决策框架 + `prior_beliefs`

**动作**：
1. 为每个可能结果设定初始先验概率
2. 使用参考类别数据校准先验
3. 检查先验概率之和是否为 1.0
4. 标注先验的来源和置信度

**输出**：先验概率分布

**检查点**：
- 先验概率之和是否为 1.0？
- 先验是否基于参考类别而非直觉？
- 是否避免了极端概率（0 或 1）？

**IF** `prior_beliefs` 提供 → **THEN** 验证概率之和，标注为"用户自定义先验"
**IF** 无参考类别数据 → **THEN** 使用无信息先验（均匀分布），标注为"最大不确定性"
**IF** 先验概率之和 ≠ 1.0 → **THEN** 按比例归一化，标注调整幅度
**ELSE** 进入 Step 3

---

## Step 3: 证据评估与似然比计算

**输入**：先验分布 + `new_evidence` + `evidence_reliability`

**动作**：
1. 评估每个证据的可靠性（0-1）
2. 计算每个证据的似然比（likelihood ratio）
3. 评估证据对每个结果的支持/反对程度
4. 识别证据间的独立性

**输出**：证据评估表 + 似然比计算

**检查点**：
- 似然比计算是否正确？
- 证据可靠性评估是否合理？
- 是否识别了证据间的相关性？

**IF** `evidence_reliability` 缺失 → **THEN** 根据证据类型推断可靠性，标注"自动推断"
**IF** 证据间存在相关性 → **THEN** 标注依赖关系，避免重复计算
**IF** 证据与先验严重冲突 → **THEN** 标注为"强冲突证据"，建议人工审查
**ELSE** 进入 Step 4

---

## Step 4: 贝叶斯信念更新

**输入**：先验分布 + 证据评估

**动作**：
1. 对每个证据执行贝叶斯更新
2. 记录更新过程（先验→似然→后验）
3. 计算更新幅度
4. 检查最终后验概率之和

**输出**：贝叶斯更新日志 + 后验概率分布

**检查点**：
- 每次更新的后验是否合理？
- 更新幅度是否与证据强度匹配？
- 后验概率之和是否为 1.0？

**IF** 更新后出现极端概率（>0.99 或 <0.01）→ **THEN** 标注为"高置信度结论"，同时提醒过度更新风险
**IF** 多个证据导致后验振荡 → **THEN** 识别冲突证据，建议分组分析
**ELSE** 进入 Step 5

---

## Step 5: 期望值计算

**输入**：后验概率分布 + 结果价值评估

**动作**：
1. 为每个结果分配价值/效用值
2. 计算期望值（EV）
3. 计算风险调整后期望值（考虑 `risk_tolerance`）
4. 计算方差和下行风险

**输出**：期望值分析报告

**检查点**：
- 价值评估是否合理？
- 风险调整是否匹配用户偏好？
- 是否计算了尾部风险？

**IF** `risk_tolerance` = conservative → **THEN** 增加下行风险权重，降低高方差选项的评分
**IF** 结果价值难以量化 → **THEN** 使用序数排序代替基数效用
**ELSE** 进入 Step 6

---

## Step 6: 校准检查与偏差识别

**输入**：概率分布 + 期望值分析

**动作**：
1. 检查过度自信风险
2. 识别基础率忽略（base rate neglect）
3. 评估可得性偏差风险
4. 提供校准建议

**输出**：校准检查报告

**检查点**：
- 概率分布是否过于集中？
- 是否忽略了基础率数据？
- 结论是否受近期事件影响？

**IF** 发现过度自信 → **THEN** 建议扩大概率区间
**IF** 发现基础率忽略 → **THEN** 补充参考类别数据
**ELSE** 进入 Step 7

---

## Step 7: 综合输出与文档化

**输入**：所有分析结果

**动作**：
1. 汇总决策框架、概率分布、期望值分析和校准检查
2. 生成决策建议
3. 生成结构化 JSON 输出
4. 标注 `thinking_models_applied`

**输出**：完整分析报告

**检查点**：
- 输出是否符合 JSON Schema？
- 决策建议是否基于期望值分析？
- 是否标注了所有不确定性？

**IF** 输出不完整 → **THEN** 补充缺失部分
**ELSE** 输出最终结果

---

## ⚠️ 边界约束

## 硬性约束

| # | 约束 | 说明 |
|---|------|------|
| 1 | 不提供精确概率值 | 概率是主观信念的量化，不是客观频率 |
| 2 | 不替代领域知识 | 概率分析需要领域知识来设定先验和似然比 |
| 3 | 不保证决策正确 | 概率思维优化决策过程，不保证结果 |
| 4 | 不忽略未知的未知 | 标注"模型不确定性"，承认分析框架的局限性 |
| 5 | 不做确定性承诺 | 所有结论都带有不确定性标注 |

## 软性约束

- 优先使用参考类别数据校准先验
- 似然比计算应保守（避免极端值）
- 期望值计算应包含敏感性分析

## 人工兜底点

- 先验概率的选择需要领域专家确认
- 似然比的设定需要实证数据支持
- 价值/效用的评估需要用户主观判断

---

## ⚠️ 异常处理

## 异常表格

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|----------|
| ERR-PROB-SUM | 先验或后验概率之和 ≠ 1.0 | 归一化处理，标注调整幅度 | high |
| ERR-LR-INVALID | 似然比计算出现无效值 | 重新检查证据评估逻辑 | high |
| ERR-EV-UNDEFINED | 结果价值无法量化 | 降级为序数分析 | medium |
| ERR-EVIDENCE-CONFLICT | 多个证据严重冲突 | 分组分析，标注冲突点 | medium |
| WARN-OVERCONFIDENCE | 概率分布过于集中 | 建议扩大区间，增加不确定性 | low |
| WARN-BASE-RATE | 未使用基础率数据 | 补充参考类别数据 | low |
| WARN-CALIBRATION | 校准检查发现偏差 | 提供校准建议 | low |

## 降级策略

1. **证据不足降级**：仅输出先验分析，标注"需要更多证据"
2. **价值不确定降级**：使用序数排序代替基数效用
3. **校准失败降级**：输出分析过程但降低结论置信度

---

## ✅ 校验验收规则

## 格式校验

- [ ] 输出为有效 JSON 格式
- [ ] 所有概率值在 [0, 1] 范围内
- [ ] 概率之和为 1.0（±0.01）
- [ ] 所有必填字段均已填充

## 内容校验

- [ ] 先验概率有参考类别或逻辑依据
- [ ] 贝叶斯更新过程可追溯
- [ ] 期望值计算包含方差和下行风险
- [ ] 校准检查覆盖过度自信和基础率忽略
- [ ] 决策建议基于期望值分析

## 合规校验

- [ ] 所有概率标注为主观信念而非客观事实
- [ ] 不包含确定性承诺
- [ ] 标注了模型不确定性
- [ ] 建议中包含人工审查提示

## OVP 验证信号

- 贝叶斯更新可追溯性：每个后验可从先验和证据还原
- 期望值计算的完整性：所有结果都纳入计算
- 校准建议的可操作性：提供具体的调整方向

---

## 🔄 迭代触发条件

## Self-Play 触发

- 每次执行后自动触发 10 组 Self-Play 测试
- 测试覆盖：投资决策、风险评估、预测校准、医疗决策
- critic 攻击重点：先验偏差、更新错误、校准失败

## 版本升级触发

- 当连续 3 次 Self-Play 发现概率计算错误 → 触发版本升级
- 当用户反馈校准建议无效 → 触发版本升级
- 当新增概率方法需求 → 触发版本升级

## 废弃触发

- 当有更好的不确定性分析方法出现 → 标记为 deprecated
- 连续 6 个月未被使用 → 标记为 deprecated

---

## 📝 自检清单

- [ ] 概率问题是否清晰表述？
- [ ] 先验概率是否有参考类别依据？
- [ ] 贝叶斯更新过程是否正确？
- [ ] 期望值计算是否包含所有结果？
- [ ] 风险调整是否匹配用户偏好？
- [ ] 是否进行了校准检查？
- [ ] 是否标注了所有不确定性？
- [ ] 输出是否符合 JSON Schema？
- [ ] 是否避免了确定性承诺？
- [ ] 决策建议是否可操作？

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "SP-113-01",
    "name": "投资决策概率分析",
    "prompt": "我考虑投资一家AI初创公司，预计3年后可能被收购（回报5x）或失败（亏损80%）。请用概率思维分析。",
    "context": "AI行业，种子轮，团队有大厂背景，赛道竞争激烈",
    "assertions": [
      "设定合理的先验概率（参考AI初创公司成功率）",
      "计算期望值并考虑风险调整",
      "识别关键不确定性因素",
      "提供校准建议"
    ],
    "expected_behavior": "基于AI初创公司的历史成功率设定先验，计算期望回报，考虑下行风险",
    "critic_attack": "先验是否过于乐观？是否考虑了团队背景的调整因子？风险调整是否充分？"
  },
  {
    "id": "SP-113-02",
    "name": "贝叶斯信念更新",
    "prompt": "我原本认为A方案成功的概率是60%。现在收到两个新消息：1) 竞争对手推出了类似产品（中等可靠性）；2) 我们的用户测试反馈很好（高可靠性）。请更新我的信念。",
    "context": "产品决策，两个新证据方向相反",
    "assertions": [
      "正确应用贝叶斯更新",
      "考虑证据可靠性差异",
      "识别证据间的潜在相关性",
      "输出更新后的概率分布"
    ],
    "expected_behavior": "根据证据可靠性和似然比进行两次更新，识别相反证据的抵消效应",
    "critic_attack": "两个证据是否独立？是否过度更新？最终概率是否过于极端？"
  },
  {
    "id": "SP-113-03",
    "name": "风险评估量化",
    "prompt": "我们计划下季度进入新市场，有三个可能结果：大成功（30%概率，收入+50%）、小成功（40%，+15%）、失败（30%，-20%）。请评估风险。",
    "context": "B2B SaaS，新市场为东南亚，已有产品在北美",
    "assertions": [
      "概率之和为1.0",
      "计算期望值",
      "计算方差和下行风险",
      "根据风险偏好给出建议"
    ],
    "expected_behavior": "验证概率分布，计算EV和风险指标，根据风险偏好调整建议",
    "critic_attack": "概率设定是否过于乐观？是否考虑了进入时机的影响？"
  },
  {
    "id": "SP-113-04",
    "name": "预测校准训练",
    "prompt": "请帮我评估以下陈述的概率：'2030年自动驾驶汽车将占新车销售的50%以上'。要求给出校准后的概率估计。",
    "context": "技术预测，需要概率校准",
    "assertions": [
      "使用参考类别数据校准",
      "识别影响概率的关键因素",
      "提供概率区间而非点估计",
      "进行校准检查"
    ],
    "expected_behavior": "基于自动驾驶发展历史和现状，给出校准后的概率区间，识别过度自信风险",
    "critic_attack": "是否考虑了监管和技术瓶颈？概率区间是否足够宽？"
  },
  {
    "id": "SP-113-05",
    "name": "多结果期望值分析",
    "prompt": "我在考虑三个职业选择：1) 大厂（稳定，年薪80万）；2) 创业（高风险，成功年入500万，失败失业）；3) 自由职业（中等风险，年收入波动大）。请分析。",
    "context": "35岁，有家庭，房贷压力，技术背景",
    "assertions": [
      "为每个选择设定概率分布",
      "计算期望值",
      "考虑风险承受能力（有家庭）",
      "进行敏感性分析"
    ],
    "expected_behavior": "基于职业选择的参考数据设定概率，计算EV和风险，考虑家庭约束",
    "critic_attack": "是否忽略了隐性成本（健康、时间）？概率设定是否有行业数据支撑？"
  }
]
```

---

## 🔗 关联文档

- [[生态系统思维]] — 系统分析提供概率分析的结构框架
- [[禅宗空性与第一性原理：如何剥离日常偏见，还原事物的最底层逻辑]] — 从基本事实设定先验概率
- [[决策推理-Schema]] — 概率分析结果输入决策框架
- [[元认知-Schema]] — 识别自身的概率认知偏差
- [[uSkill-agent-认知偏差对抗协议]] — 对抗过度自信和基础率忽略
- [[概率思维]] — 自引用，持续迭代

---

## 📝 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-06-23 | 初始版本，包含完整的概率思维分析框架 |


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


**相关概念**：[[贝叶斯推断]]

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
