
# 🎯 目标

运用二阶思维方法论，超越直接效应分析，系统识别决策的连锁反应、间接效应和长期后果，为政策制定、商业决策、投资判断和人生规划提供更全面的影响评估。

**核心价值**：避免"按下葫芦浮起瓢"的决策陷阱，预见并管理非预期后果。

**适用场景**：政策副作用预测、商业战略长期影响评估、投资决策的隐性风险识别、人生重大选择的全面后果分析。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `decision_or_action` | string | 是 | - | 需要分析的决策或行动 |
| `first_order_effects` | list | 否 | [] | 用户已识别的一阶效应（可选补充） |
| `affected_stakeholders` | list | 否 | [] | 可能受影响的利益相关方 |
| `time_horizon` | enum | 否 | "medium" | 分析时间跨度：short / medium / long |
| `context` | string | 否 | "" | 决策背景信息 |
| `constraints` | list | 否 | [] | 已知的约束条件 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `decision_or_action` 必须是具体的、可执行的决策或行动
- `time_horizon` = long 时，要求提供 `affected_stakeholders` 至少 3 个
- `constraints` 应明确标注不可违反的硬约束
- 不支持分析"什么都不做"作为决策（除非明确选择不行动）

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "decision_analysis": {
      "type": "object",
      "properties": {
        "decision": {"type": "string"},
        "intent": {"type": "string"},
        "assumptions": {"type": "array", "items": {"type": "string"}},
        "constraints": {"type": "array", "items": {"type": "string"}}
      }
    },
    "effect_chain": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "order": {"type": "number"},
          "effect": {"type": "string"},
          "mechanism": {"type": "string"},
          "affected_party": {"type": "string"},
          "probability": {"type": "string", "enum": ["high", "medium", "low"]},
          "magnitude": {"type": "string", "enum": ["high", "medium", "low"]},
          "delay": {"type": "string"},
          "reversibility": {"type": "string", "enum": ["reversible", "partially", "irreversible"]}
        }
      }
    },
    "feedback_loops": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {"type": "string", "enum": ["reinforcing", "balancing"]},
          "description": {"type": "string"},
          "trigger_condition": {"type": "string"},
          "amplification_factor": {"type": "string"}
        }
      }
    },
    "unintended_consequences": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "consequence": {"type": "string"},
          "likelihood": {"type": "string", "enum": ["high", "medium", "low"]},
          "impact": {"type": "string"},
          "early_warning_sign": {"type": "string"},
          "mitigation": {"type": "string"}
        }
      }
    },
    "stakeholder_impact_map": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "stakeholder": {"type": "string"},
          "first_order_impact": {"type": "string"},
          "second_order_impact": {"type": "string"},
          "third_order_impact": {"type": "string"},
          "net_assessment": {"type": "string", "enum": ["positive", "negative", "mixed", "uncertain"]}
        }
      }
    },
    "temporal_analysis": {
      "type": "object",
      "properties": {
        "immediate_effects": {"type": "array", "items": {"type": "string"}},
        "short_term_effects": {"type": "array", "items": {"type": "string"}},
        "medium_term_effects": {"type": "array", "items": {"type": "string"}},
        "long_term_effects": {"type": "array", "items": {"type": "string"}},
        "tipping_points": {"type": "array", "items": {"type": "string"}}
      }
    },
    "mitigation_strategies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "risk": {"type": "string"},
          "strategy": {"type": "string"},
          "cost": {"type": "string", "enum": ["low", "medium", "high"]},
          "effectiveness": {"type": "string", "enum": ["high", "medium", "low"]},
          "monitoring_metric": {"type": "string"}
        }
      }
    },
    "decision_quality_check": {
      "type": "object",
      "properties": {
        "completeness_score": {"type": "number", "minimum": 0, "maximum": 10},
        "blind_spots": {"type": "array", "items": {"type": "string"}},
        "recommended_additional_analysis": {"type": "array", "items": {"type": "string"}}
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

## Step 1: 决策澄清与一阶效应识别

**输入**：`decision_or_action` + `context` + `constraints`

**动作**：
1. 精确表述待分析的决策
2. 识别决策的直接目的和预期效果
3. 列出所有直接的一阶效应
4. 评估一阶效应的概率和影响

**输出**：决策定义 + 一阶效应清单

**检查点**：一阶效应是否全面？是否遗漏了直接影响？

**IF** `first_order_effects` 提供 → **THEN** 验证完整性，补充遗漏
**IF** `constraints` 包含硬约束 → **THEN** 在分析中标注不可违反的边界
**ELSE** 进入 Step 2

---

## Step 2: 二阶效应推导

**输入**：一阶效应清单

**动作**：
1. 对每个一阶效应追问"这会导致什么？"
2. 识别一阶效应引发的二阶效应
3. 评估每个二阶效应的概率和影响
4. 标注时间延迟

**输出**：二阶效应清单

**检查点**：
- 是否每个一阶效应都推导出二阶效应？
- 二阶效应是否有明确的因果机制？
- 时间延迟是否合理标注？

**IF** 某个一阶效应无法推导出二阶效应 → **THEN** 标注为"直接终结"，说明原因
**IF** 二阶效应概率极低 → **THEN** 仍保留但标注为"低概率高影响"
**ELSE** 进入 Step 3

---

## Step 3: 三阶效应与更高阶分析

**输入**：二阶效应清单

**动作**：
1. 对关键二阶效应追问"这又会导致什么？"
2. 识别三阶效应（`time_horizon` = long 时必须）
3. 识别可能的反馈循环
4. 评估效应链的终止条件

**输出**：三阶效应清单 + 反馈循环识别

**检查点**：
- 高阶效应是否仍然有实际意义？
- 反馈循环是否被正确识别？
- 效应链是否有合理的终止点？

**IF** 效应链超过 4 阶 → **THEN** 标注为"高度不确定"，降低置信度
**IF** 发现正反馈循环 → **THEN** 标注为"潜在失控风险"
**ELSE** 进入 Step 4

---

## Step 4: 利益相关方影响分析

**输入**：效应链 + `affected_stakeholders`

**动作**：
1. 识别所有受影响的利益相关方
2. 为每个利益相关方映射一阶、二阶、三阶影响
3. 评估每个利益相关方的净影响
4. 识别利益冲突和协调需求

**输出**：利益相关方影响地图

**检查点**：
- 是否遗漏了隐性利益相关方？
- 每个利益相关方的影响评估是否全面？
- 是否识别了利益冲突？

**IF** `affected_stakeholders` 为空 → **THEN** 从决策直接影响出发推导利益相关方
**IF** 发现利益严重冲突 → **THEN** 标注为"需要协调机制"
**ELSE** 进入 Step 5

---

## Step 5: 时间维度分析

**输入**：效应链 + `time_horizon`

**动作**：
1. 按时间维度组织效应（即时/短期/中期/长期）
2. 识别时间延迟和临界点
3. 评估长期效应的不确定性
4. 标注不可逆效应

**输出**：时间维度分析报告

**检查点**：
- 时间分类是否合理？
- 是否识别了关键临界点？
- 不可逆效应是否被特别标注？

**IF** `time_horizon` = long → **THEN** 必须包含长期效应分析和临界点识别
**IF** 发现不可逆效应 → **THEN** 特别标注，建议慎重评估
**ELSE** 进入 Step 6

---

## Step 6: 风险缓解策略设计

**输入**：效应链 + 利益相关方影响 + 时间分析

**动作**：
1. 识别高概率或高影响的负面效应
2. 为每个风险设计缓解策略
3. 评估缓解策略的成本和有效性
4. 设计监控指标和预警机制

**输出**：风险缓解策略集

**检查点**：
- 缓解策略是否直接针对风险源？
- 成本是否可接受？
- 监控指标是否可操作？

**IF** 缓解策略成本过高 → **THEN** 提供替代方案或接受策略
**IF** 某些风险无法缓解 → **THEN** 标注为"需接受风险"，建议预案
**ELSE** 进入 Step 7

---

## Step 7: 综合输出与文档化

**输入**：所有分析结果

**动作**：
1. 汇总效应链、反馈循环、利益相关方影响和缓解策略
2. 进行决策质量检查（完整性评分、盲点识别）
3. 生成结构化 JSON 输出
4. 标注 `thinking_models_applied`

**输出**：完整分析报告

**检查点**：
- 输出是否符合 JSON Schema？
- 效应链是否完整？
- 是否标注了所有不确定性？

**IF** 输出不完整 → **THEN** 补充缺失部分
**ELSE** 输出最终结果

---

## ⚠️ 边界约束

## 硬性约束

| # | 约束 | 说明 |
|---|------|------|
| 1 | 不做精确预测 | 二阶思维识别可能性，不预测精确结果 |
| 2 | 不替代领域知识 | 效应链分析需要领域知识验证因果机制 |
| 3 | 不忽略一阶效应 | 二阶思维补充而非替代一阶分析 |
| 4 | 不假设线性传递 | 效应可能放大、衰减或转向 |
| 5 | 不忽视时间维度 | 所有效应必须标注时间特征 |

## 软性约束

- 优先分析高概率或高影响的效应
- 效应链长度不超过 4 阶（避免过度推测）
- 缓解策略应考虑成本效益比

## 人工兜底点

- 效应链的因果机制需要领域专家验证
- 利益相关方影响评估需要实际调研
- 长期效应预测需要持续跟踪验证

---

## ⚠️ 异常处理

## 异常表格

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|----------|
| ERR-DECISION-VAGUE | 决策描述过于模糊 | 返回引导性问题，要求具体化 | high |
| ERR-CHAIN-BREAK | 效应链无法继续推导 | 标注为"直接终结"，说明原因 | medium |
| ERR-LOOP-UNBOUNDED | 发现无界正反馈循环 | 标注为"潜在失控风险"，建议干预 | high |
| ERR-STAKEHOLDER-MISS | 利益相关方识别不完整 | 补充推导，标注"可能遗漏" | medium |
| WARN-DELAY-UNKNOWN | 效应延迟无法估计 | 标注为"延迟未知"，建议跟踪 | low |
| WARN-IRREVERSIBLE | 发现不可逆效应 | 特别标注，建议慎重评估 | medium |
| WARN-HIGH-UNCERTAINTY | 高阶效应不确定性极高 | 降低置信度，建议持续观察 | low |

## 降级策略

1. **时间不足降级**：仅分析到二阶效应，跳过高阶
2. **利益相关方未知降级**：仅分析直接影响对象
3. **效应链断裂降级**：标注断点，仅完成可达的分析

---

## ✅ 校验验收规则

## 格式校验

- [ ] 输出为有效 JSON 格式
- [ ] 所有必填字段均已填充
- [ ] 效应链包含至少 2 个阶次
- [ ] 枚举值在规定范围内

## 内容校验

- [ ] 每个一阶效应都推导出二阶效应
- [ ] 效应链有明确的因果机制描述
- [ ] 利益相关方影响评估包含三个阶次
- [ ] 缓解策略包含成本和有效性评估
- [ ] 时间分析覆盖即时到长期

## 合规校验

- [ ] 不包含精确预测
- [ ] 标注了所有不确定性和假设
- [ ] 高阶效应标注为"高度不确定"
- [ ] 建议中包含人工审查提示

## OVP 验证信号

- 连锁反应链条完整性：每个效应可追溯到原始决策
- 利益相关方覆盖：主要利益相关方均有影响评估
- 缓解策略可操作性：每个策略有明确的监控指标

---

## 🔄 迭代触发条件

## Self-Play 触发

- 每次执行后自动触发 10 组 Self-Play 测试
- 测试覆盖：政策分析、商业决策、投资判断、人生规划
- critic 攻击重点：效应遗漏、反馈循环忽略、时间维度缺失

## 版本升级触发

- 当连续 3 次 Self-Play 发现同一类效应遗漏 → 触发版本升级
- 当用户反馈间接效应分析不准确 → 触发版本升级
- 当新增分析维度需求 → 触发版本升级

## 废弃触发

- 当有更好的间接效应分析方法出现 → 标记为 deprecated
- 连续 6 个月未被使用 → 标记为 deprecated

---

## 📝 自检清单

- [ ] 决策是否清晰界定？
- [ ] 是否识别出至少 2 个二阶效应？
- [ ] 效应链是否有明确的因果机制？
- [ ] 是否识别了反馈循环？
- [ ] 利益相关方影响是否全面评估？
- [ ] 时间维度是否覆盖分析范围？
- [ ] 缓解策略是否具有可操作性？
- [ ] 输出是否符合 JSON Schema？
- [ ] 是否标注了所有不确定性？
- [ ] 是否识别了不可逆效应？

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "SP-114-01",
    "name": "政策二阶效应分析",
    "prompt": "政府决定提高最低工资标准20%。请分析这个政策的连锁反应。",
    "context": "中等发达经济体，失业率5%，中小企业占比60%",
    "assertions": [
      "识别出至少3个二阶效应",
      "包含对不同利益相关方的差异化影响",
      "识别了可能的反馈循环",
      "提供缓解策略和监控指标"
    ],
    "expected_behavior": "分析工资上涨→成本增加→裁员/涨价→消费变化→就业影响的连锁反应",
    "critic_attack": "是否忽略了对非正规经济的影响？是否考虑了区域差异？"
  },
  {
    "id": "SP-114-02",
    "name": "商业决策间接效应",
    "prompt": "我们计划大幅降低产品价格50%以抢占市场份额。请分析二阶效应。",
    "context": "SaaS行业，当前市场份额15%，竞争对手3家",
    "assertions": [
      "识别出价格战的潜在风险",
      "分析对客户行为的间接影响",
      "识别竞争对手的可能反应",
      "评估长期盈利能力影响"
    ],
    "expected_behavior": "分析降价→客户获取→竞争反应→利润压力→服务质量下降的潜在链条",
    "critic_attack": "是否忽略了客户价值认知变化？是否考虑了品牌定位影响？"
  },
  {
    "id": "SP-114-03",
    "name": "投资决策长期后果",
    "prompt": "我考虑辞职全职创业。请分析这个决定的二阶和三阶效应。",
    "context": "35岁，有家庭，房贷，技术背景，创业方向为AI",
    "assertions": [
      "识别出对家庭财务的影响",
      "分析职业发展的长期影响",
      "识别心理和健康的影响",
      "评估失败后的恢复路径"
    ],
    "expected_behavior": "分析辞职→收入中断→家庭压力→创业表现→成功/失败→长期影响的链条",
    "critic_attack": "是否忽略了社保和养老金影响？是否考虑了行业周期因素？"
  },
  {
    "id": "SP-114-04",
    "name": "技术选型连锁反应",
    "prompt": "我们决定从微服务架构迁移到单体架构。请分析连锁反应。",
    "context": "中型技术公司，200人研发团队，当前微服务架构维护成本高",
    "assertions": [
      "识别出团队结构的连锁变化",
      "分析对部署流程的影响",
      "识别技术债务的转移效应",
      "评估对业务敏捷性的影响"
    ],
    "expected_behavior": "分析架构迁移→团队重组→技能转型→效率变化→业务影响的链条",
    "critic_attack": "是否忽略了数据迁移风险？是否考虑了团队士气影响？"
  },
  {
    "id": "SP-114-05",
    "name": "人生规划间接效应",
    "prompt": "我考虑搬到另一个城市生活。请分析这个决定的全面后果。",
    "context": "30岁，单身，远程工作，考虑从北京搬到成都",
    "assertions": [
      "识别出社交网络的变化",
      "分析生活成本和质量的变化",
      "识别职业发展的影响",
      "评估心理适应过程"
    ],
    "expected_behavior": "分析搬家→生活成本变化→社交重建→职业机会→心理适应→长期满意度的链条",
    "critic_attack": "是否忽略了回流风险？是否考虑了行业聚集效应？"
  }
]
```

---

## 🔗 关联文档

- [[生态系统思维]] — 二阶思维与系统思维的反馈回路分析互补
- [[概率思维]] — 评估二阶效应的概率和影响
- [[禅宗空性与第一性原理：如何剥离日常偏见，还原事物的最底层逻辑]] — 从基本事实推导效应机制
- [[决策推理-Schema]] — 二阶分析结果输入决策框架
- [[元认知-Schema]] — 识别自身的线性思维偏差
- [[uSkill-agent-认知偏差对抗协议]] — 对抗近因偏差和确认偏差

---

## 📝 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-06-23 | 初始版本，包含完整的二阶思维分析框架 |


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


**相关概念**：[[系统性思维：超越替罪羊效应的风险诊断]]

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
