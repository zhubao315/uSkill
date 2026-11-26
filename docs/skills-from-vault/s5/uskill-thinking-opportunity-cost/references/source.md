
# 🎯 目标

运用机会成本分析方法论，系统评估放弃选项的价值，识别显性和隐性成本，进行比较优势分析，为投资配置、时间管理、职业选择和资源分配提供经济学视角的决策支持。

**核心价值**：将"选择的代价"显性化，避免忽视隐性成本导致的次优决策。

**适用场景**：投资组合优化、时间分配决策、职业路径选择、项目优先级排序、资源分配策略。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `decision_context` | string | 是 | - | 需要分析的决策场景 |
| `options` | list | 是 | - | 可选方案列表，每个选项包含描述 |
| `chosen_option` | string | 否 | "" | 用户倾向或已选的方案（可选） |
| `constraints` | list | 否 | [] | 资源、时间、能力等约束条件 |
| `time_horizon` | string | 否 | "1年" | 分析的时间跨度 |
| `value_dimensions` | list | 否 | ["financial", "time", "opportunity"] | 价值评估维度 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `options` 至少包含 2 个备选方案
- `constraints` 应明确不可违反的硬约束
- `time_horizon` 影响机会成本的评估范围
- 不支持无备选方案的单一选择

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
        "constraints": {"type": "array", "items": {"type": "string"}},
        "time_horizon": {"type": "string"},
        "value_dimensions": {"type": "array", "items": {"type": "string"}}
      }
    },
    "options_analysis": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "option": {"type": "string"},
          "description": {"type": "string"},
          "explicit_costs": {"type": "array", "items": {"type": "object"}},
          "explicit_benefits": {"type": "array", "items": {"type": "object"}},
          "implicit_costs": {"type": "array", "items": {"type": "object"}},
          "opportunity_cost_of_choosing": {"type": "object"},
          "risk_profile": {"type": "object"},
          "time_profile": {"type": "object"},
          "total_value_assessment": {"type": "object"}
        }
      }
    },
    "opportunity_cost_matrix": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "chosen": {"type": "string"},
          "forgone": {"type": "string"},
          "opportunity_cost": {"type": "object"},
          "regret_potential": {"type": "string", "enum": ["high", "medium", "low"]},
          "reversibility": {"type": "string", "enum": ["reversible", "partially", "irreversible"]}
        }
      }
    },
    "comparative_advantage": {
      "type": "object",
      "properties": {
        "analysis": {"type": "string"},
        "best_option_per_dimension": {"type": "array", "items": {"type": "object"}},
        "overall_best": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]}
      }
    },
    "hidden_costs_identified": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "cost": {"type": "string"},
          "associated_option": {"type": "string"},
          "magnitude": {"type": "string", "enum": ["high", "medium", "low"]},
          "visibility": {"type": "string", "enum": ["obvious", "subtle", "hidden"]}
        }
      }
    },
    "recommendation": {
      "type": "object",
      "properties": {
        "recommended_option": {"type": "string"},
        "reasoning": {"type": "string"},
        "key_trade_offs": {"type": "array", "items": {"type": "string"}},
        "sensitivity_factors": {"type": "array", "items": {"type": "string"}},
        "implementation_notes": {"type": "array", "items": {"type": "string"}}
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

**输入**：`decision_context` + `constraints` + `time_horizon`

**动作**：
1. 精确表述需要回答的决策问题
2. 界定资源约束和时间范围
3. 明确价值评估维度
4. 识别决策的关键权衡

**输出**：决策框架文档

**检查点**：
- 决策问题是否清晰？
- 约束条件是否完整？
- 价值维度是否合理？

**IF** `constraints` 包含硬约束 → **THEN** 标注不可违反的边界
**IF** `time_horizon` 未提供 → **THEN** 根据决策类型推断合理时间跨度
**ELSE** 进入 Step 2

---

## Step 2: 选项详细分析

**输入**：决策框架 + `options`

**动作**：
1. 对每个选项进行详细描述
2. 识别每个选项的显性成本和收益
3. 识别每个选项的隐性成本
4. 评估每个选项的风险特征

**输出**：选项详细分析表

**检查点**：
- 选项描述是否充分？
- 显性成本是否全面？
- 隐性成本是否被识别？

**IF** `chosen_option` 提供 → **THEN** 优先详细分析该选项
**IF** 某个选项描述模糊 → **THEN** 要求补充或标注为"信息不足"
**ELSE** 进入 Step 3

---

## Step 3: 机会成本矩阵构建

**输入**：选项详细分析

**动作**：
1. 为每个选项组合计算机会成本
2. 识别每个选择放弃的最大价值
3. 评估后悔潜力和可逆性
4. 构建机会成本矩阵

**输出**：机会成本矩阵

**检查点**：
- 机会成本计算是否合理？
- 是否考虑了所有选项组合？
- 后悔潜力评估是否合理？

**IF** 选项数量 > 5 → **THEN** 优先分析 Top 3 最可能选项的机会成本
**IF** 机会成本难以量化 → **THEN** 使用序数排序代替基数评估
**ELSE** 进入 Step 4

---

## Step 4: 比较优势分析

**输入**：机会成本矩阵 + `value_dimensions`

**动作**：
1. 按每个价值维度评估各选项
2. 识别每个维度的最优选项
3. 进行整体比较优势分析
4. 评估维度间的权衡

**输出**：比较优势分析报告

**检查点**：
- 维度评估是否全面？
- 是否识别了维度间的冲突？
- 整体评估是否合理？

**IF** `value_dimensions` 包含冲突维度 → **THEN** 标注维度冲突，提供权衡框架
**IF** 某维度数据不足 → **THEN** 标注为"不确定"，降低该维度权重
**ELSE** 进入 Step 5

---

## Step 5: 隐性成本深度挖掘

**输入**：选项分析 + 机会成本矩阵

**动作**：
1. 系统识别每个选项的隐性成本
2. 评估隐性成本的可见度（obvious / subtle / hidden）
3. 评估隐性成本的量级
4. 标注隐性成本的不确定性

**输出**：隐性成本清单

**检查点**：
- 是否识别了所有主要隐性成本？
- 隐性成本评估是否合理？
- 是否识别了"hidden"级别的成本？

**IF** 发现高量级隐性成本 → **THEN** 特别标注，重新评估选项排序
**IF** 隐性成本无法量化 → **THEN** 使用定性描述，标注"需主观判断"
**ELSE** 进入 Step 6

---

## Step 6: 敏感性分析与建议生成

**输入**：机会成本矩阵 + 比较优势 + 隐性成本

**动作**：
1. 识别影响排序的关键假设
2. 进行敏感性分析
3. 生成决策建议
4. 设计实施要点和监控指标

**输出**：敏感性分析 + 决策建议

**检查点**：
- 敏感性分析是否覆盖关键假设？
- 建议是否基于机会成本分析？
- 实施要点是否可操作？

**IF** 排序对假设高度敏感 → **THEN** 标注为"高度不确定"，建议收集更多信息
**IF** `chosen_option` 与建议不一致 → **THEN** 说明差异，分析可能原因
**ELSE** 进入 Step 7

---

## Step 7: 综合输出与文档化

**输入**：所有分析结果

**动作**：
1. 汇总决策框架、选项分析、机会成本矩阵和建议
2. 生成结构化 JSON 输出
3. 标注 `thinking_models_applied`

**输出**：完整分析报告

**检查点**：
- 输出是否符合 JSON Schema？
- 机会成本分析是否完整？
- 建议是否可操作？

**IF** 输出不完整 → **THEN** 补充缺失部分
**ELSE** 输出最终结果

---

## ⚠️ 边界约束

## 硬性约束

| # | 约束 | 说明 |
|---|------|------|
| 1 | 不替代主观价值判断 | 机会成本分析提供信息，不替代用户做最终选择 |
| 2 | 不忽略不可量化因素 | 时间、健康、关系等非财务因素必须纳入分析 |
| 3 | 不假设完美信息 | 承认信息不完全，标注不确定性 |
| 4 | 不忽略沉没成本谬误 | 明确区分沉没成本和机会成本 |
| 5 | 不做精确预测 | 机会成本是估计值，不是精确计算 |

## 软性约束

- 优先分析最可能被选择的选项
- 隐性成本评估应保守
- 时间维度的贴现率应合理

## 人工兜底点

- 非财务因素的价值需要用户主观判断
- 隐性成本的识别需要领域知识
- 最终选择需要用户权衡

---

## ⚠️ 异常处理

## 异常表格

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|----------|
| ERR-NO-OPTIONS | 未提供备选方案 | 返回提示，要求提供至少2个选项 | high |
| ERR-ONE-OPTION | 仅提供1个选项 | 返回提示，要求补充备选方案 | high |
| ERR-COST-UNKNOWN | 机会成本无法估计 | 使用定性描述，标注"需主观判断" | medium |
| ERR-DIMENSION-CONFLICT | 价值维度严重冲突 | 标注冲突，提供权衡框架 | medium |
| WARN-HIDDEN-COST | 发现高量级隐性成本 | 特别标注，重新评估选项 | medium |
| WARN-SENSITIVE | 排序对假设高度敏感 | 建议收集更多信息 | low |
| WARN-INCOMPLETE | 选项信息不完整 | 标注缺失信息，降低分析置信度 | low |

## 降级策略

1. **信息不足降级**：仅完成可用信息的分析，标注"信息缺口"
2. **量化困难降级**：使用序数排序代替基数评估
3. **维度冲突降级**：输出各维度最优选项，不提供整体推荐

---

## ✅ 校验验收规则

## 格式校验

- [ ] 输出为有效 JSON 格式
- [ ] 所有必填字段均已填充
- [ ] 机会成本矩阵覆盖所有选项组合
- [ ] 枚举值在规定范围内

## 内容校验

- [ ] 至少识别 2 个隐性成本
- [ ] 机会成本评估考虑了时间维度
- [ ] 比较优势分析覆盖所有价值维度
- [ ] 敏感性分析覆盖关键假设
- [ ] 建议基于机会成本分析

## 合规校验

- [ ] 不忽略不可量化因素
- [ ] 区分了沉没成本和机会成本
- [ ] 标注了所有不确定性
- [ ] 建议中包含人工选择提示

## OVP 验证信号

- 放弃选项价值可追溯性：每个机会成本可追溯到具体选项
- 隐性成本识别完整性：主要隐性成本均被识别
- 分析与建议的一致性：建议基于机会成本排序

---

## 🔄 迭代触发条件

## Self-Play 触发

- 每次执行后自动触发 10 组 Self-Play 测试
- 测试覆盖：投资决策、时间管理、职业选择、资源分配
- critic 攻击重点：机会成本遗漏、隐性成本忽略、维度缺失

## 版本升级触发

- 当连续 3 次 Self-Play 发现同一类成本遗漏 → 触发版本升级
- 当用户反馈分析不准确 → 触发版本升级
- 当新增价值维度需求 → 触发版本升级

## 废弃触发

- 当有更好的资源优化方法出现 → 标记为 deprecated
- 连续 6 个月未被使用 → 标记为 deprecated

---

## 📝 自检清单

- [ ] 决策问题是否清晰表述？
- [ ] 是否识别了所有合理备选方案？
- [ ] 每个选项的显性成本是否全面？
- [ ] 是否识别了隐性成本？
- [ ] 机会成本矩阵是否完整？
- [ ] 比较优势分析是否覆盖所有维度？
- [ ] 敏感性分析是否覆盖关键假设？
- [ ] 输出是否符合 JSON Schema？
- [ ] 是否区分了沉没成本和机会成本？
- [ ] 建议是否可操作？

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "SP-117-01",
    "name": "投资配置机会成本",
    "prompt": "我有100万闲置资金，考虑投资股市、买房或创业。请分析机会成本。",
    "context": "35岁，有家庭，风险偏好中等",
    "assertions": [
      "三个选项均有详细分析",
      "识别了每个选项的隐性成本",
      "机会成本矩阵覆盖所有组合",
      "建议考虑了风险偏好"
    ],
    "expected_behavior": "分析股市、房产、创业的显性隐性成本，构建机会成本矩阵，考虑时间和风险维度",
    "critic_attack": "是否忽略了流动性成本？是否考虑了家庭约束？"
  },
  {
    "id": "SP-117-02",
    "name": "时间分配机会成本",
    "prompt": "我每天有3小时自由时间，考虑用来学习编程、健身或陪伴家人。请分析机会成本。",
    "context": "30岁，工作压力大，希望提升生活质量",
    "assertions": [
      "三个选项的收益和成本分析",
      "考虑了时间的不可逆性",
      "识别了隐性成本（如健康、关系）",
      "建议考虑了生活平衡"
    ],
    "expected_behavior": "分析学习、健身、陪伴的时间价值，考虑长期回报和即时满足的权衡",
    "critic_attack": "是否忽略了社交需求？是否考虑了职业发展影响？"
  },
  {
    "id": "SP-117-03",
    "name": "职业选择机会成本",
    "prompt": "我有两个工作机会：大厂高级工程师（年薪120万）和创业公司CTO（年薪60万+期权）。请分析机会成本。",
    "context": "32岁，技术背景，有创业想法",
    "assertions": [
      "两个选项的全面分析",
      "识别了期权的不确定性成本",
      "考虑了职业发展的长期影响",
      "比较优势分析覆盖多维度"
    ],
    "expected_behavior": "分析大厂稳定性和创业风险的权衡，考虑财务、成长、自主性等维度",
    "critic_attack": "是否忽略了行业周期影响？是否考虑了家庭因素？"
  },
  {
    "id": "SP-117-04",
    "name": "项目优先级机会成本",
    "prompt": "我们团队有3个项目可选，但资源只够做1个。请分析选择每个项目的机会成本。",
    "context": "产品团队，资源有限，季度目标需达成",
    "assertions": [
      "三个项目的机会成本分析",
      "考虑了战略价值和执行难度",
      "识别了放弃项目的机会成本",
      "建议基于整体价值最大化"
    ],
    "expected_behavior": "分析三个项目的资源需求、风险和回报，构建机会成本矩阵",
    "critic_attack": "是否忽略了项目间的依赖关系？是否考虑了团队能力约束？"
  },
  {
    "id": "SP-117-05",
    "name": "生活方式选择机会成本",
    "prompt": "我考虑从北京搬到成都生活。请分析这个选择的机会成本。",
    "context": "30岁，远程工作，无房贷压力",
    "assertions": [
      "识别了社交网络的成本",
      "考虑了职业机会的变化",
      "分析了生活质量的权衡",
      "识别了不可逆的成本"
    ],
    "expected_behavior": "分析搬家的机会成本：社交重建、职业机会、生活成本、心理适应",
    "critic_attack": "是否忽略了未来回流的成本？是否考虑了行业聚集效应？"
  }
]
```

---

## 🔗 关联文档

- [[概率思维]] — 机会成本评估需要概率思维处理不确定性
- [[二阶思维]] — 机会成本可能有二阶效应
- [[生态系统思维]] — 资源分配是系统分析的重要部分
- [[决策推理-Schema]] — 机会成本分析输入决策框架
- [[元认知-Schema]] — 识别自身对机会成本的认知偏差
- [[uSkill-agent-认知偏差对抗协议]] — 对抗沉没成本谬误和现状偏差

---

## 📝 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-06-23 | 初始版本，包含完整的机会成本分析框架 |


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


**相关概念**：[[不可逆决策与可逆决策]]

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
