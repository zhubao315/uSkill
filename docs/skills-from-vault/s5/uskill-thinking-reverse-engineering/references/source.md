
# 🎯 目标

运用逆向工程思维方法论，从可观测的结果出发，反向推导原因、机制和因果链条，为问题诊断、竞品分析、系统理解和根因分析提供结构化的逆向推理框架。

**核心价值**：将"结果"转化为"可复制的知识"，从成功中学习、从失败中避免。

**适用场景**：产品竞品分析、技术故障诊断、成功案例研究、系统行为逆向分析、市场现象归因。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `observed_result` | string | 是 | - | 需要逆向分析的可观测结果 |
| `result_type` | enum | 否 | "unknown" | 结果类型：success / failure / neutral / unknown |
| `available_evidence` | list | 否 | [] | 可获取的证据和数据 |
| `analysis_depth` | enum | 否 | "standard" | 分析深度：surface / standard / deep |
| `context` | string | 否 | "" | 结果发生的背景信息 |
| `comparison_targets` | list | 否 | [] | 需要对比的案例（可选） |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `observed_result` 必须是具体的、可观测的结果描述
- `available_evidence` 至少包含 1 条证据或数据点
- `analysis_depth` = deep 时，要求提供 `available_evidence` 至少 3 条
- 不支持纯假设性的结果分析

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "result_analysis": {
      "type": "object",
      "properties": {
        "result": {"type": "string"},
        "type": {"type": "string"},
        "observable_indicators": {"type": "array", "items": {"type": "string"}},
        "anomalies": {"type": "array", "items": {"type": "string"}},
        "baseline_comparison": {"type": "string"}
      }
    },
    "reverse_causal_chain": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step": {"type": "number"},
          "effect": {"type": "string"},
          "cause": {"type": "string"},
          "mechanism": {"type": "string"},
          "evidence": {"type": "array", "items": {"type": "string"}},
          "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
          "alternative_explanations": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "root_cause_analysis": {
      "type": "object",
      "properties": {
        "primary_cause": {"type": "string"},
        "contributing_causes": {"type": "array", "items": {"type": "string"}},
        "enabling_factors": {"type": "array", "items": {"type": "string"}},
        "root_cause_confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "five_whys_log": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "level": {"type": "number"},
              "question": {"type": "string"},
              "answer": {"type": "string"}
            }
          }
        }
      }
    },
    "mechanism_decomposition": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "component": {"type": "string"},
          "function": {"type": "string"},
          "interaction": {"type": "string"},
          "criticality": {"type": "string", "enum": ["critical", "important", "supportive"]}
        }
      }
    },
    "competitive_analysis": {
      "type": "object",
      "properties": {
        "target": {"type": "string"},
        "success_factors": {"type": "array", "items": {"type": "string"}},
        "differentiation": {"type": "array", "items": {"type": "string"}},
        "replicability": {"type": "string", "enum": ["high", "medium", "low"]},
        "lessons_learned": {"type": "array", "items": {"type": "string"}}
      }
    },
    "diagnostic_recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "finding": {"type": "string"},
          "recommendation": {"type": "string"},
          "priority": {"type": "string", "enum": ["high", "medium", "low"]},
          "implementation_effort": {"type": "string", "enum": ["low", "medium", "high"]}
        }
      }
    },
    "knowledge_extracted": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "principle": {"type": "string"},
          "applicability": {"type": "string"},
          "transferability": {"type": "string", "enum": ["high", "medium", "low"]}
        }
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

## Step 1: 结果观测与描述

**输入**：`observed_result` + `context` + `available_evidence`

**动作**：
1. 精确描述观测到的结果
2. 列出所有可观测的指标和异常
3. 与基线或预期进行对比
4. 确定结果的类型（success / failure / neutral）

**输出**：结果描述文档

**检查点**：
- 结果描述是否客观、具体？
- 是否区分了事实和推断？
- 异常点是否被识别？

**IF** `result_type` = unknown → **THEN** 先分类结果类型，再进行分析
**IF** `available_evidence` 不足 → **THEN** 标注"信息有限"，建议补充证据
**ELSE** 进入 Step 2

---

## Step 2: 逆向因果链构建

**输入**：结果描述

**动作**：
1. 从结果出发，逐层追问"这导致了什么？"
2. 反向构建因果链条
3. 为每个因果环节寻找证据支持
4. 标注每个环节的置信度和替代解释

**输出**：逆向因果链

**检查点**：
- 因果链是否完整（从结果追溯到根因）？
- 每个环节是否有证据支持？
- 是否考虑了替代解释？

**IF** 因果链断裂 → **THEN** 标注为"待验证环节"，提供可能的补充路径
**IF** 多个根因并存 → **THEN** 识别主因和次因，评估相对贡献
**ELSE** 进入 Step 3

---

## Step 3: 根因分析（5 Whys）

**输入**：逆向因果链

**动作**：
1. 对每个关键因果环节应用 5 Whys 追问
2. 追问至少 3 层，直到达到可行动的根因
3. 识别主因、贡献因素和使能因素
4. 评估根因分析的置信度

**输出**：根因分析报告

**检查点**：
- 5 Whys 追问是否到达真正根因？
- 根因是否可行动？
- 是否区分了不同类型的因果因素？

**IF** 5 Whys 追问超过 5 层 → **THEN** 标注为"深层根因"，可能需要系统性解决
**IF** 根因不可行动 → **THEN** 回溯到可行动的上层原因
**ELSE** 进入 Step 4

---

## Step 4: 机制分解

**输入**：根因分析

**动作**：
1. 分解结果背后的机制和组件
2. 识别每个组件的功能和交互
3. 评估每个组件的关键性
4. 识别关键路径和瓶颈

**输出**：机制分解表

**检查点**：
- 机制分解是否深入到组件层面？
- 组件间交互是否明确？
- 关键性评估是否合理？

**IF** 机制过于复杂 → **THEN** 分层分解，标注不同层级
**IF** 信息不足以深入分解 → **THEN** 标注"黑箱组件"，提供推测
**ELSE** 进入 Step 5

---

## Step 5: 竞品/案例对比分析

**输入**：机制分解 + `comparison_targets`

**动作**：
1. 如果有 `comparison_targets`，进行对比分析
2. 识别成功/失败的关键差异因素
3. 评估因素的可复制性
4. 提取可迁移的知识和原则

**输出**：竞品分析报告

**检查点**：
- 对比是否公平（控制变量）？
- 是否识别了真正差异因素？
- 可复制性评估是否合理？

**IF** `comparison_targets` 为空 → **THEN** 跳过对比，直接提取知识
**IF** 差异因素难以归因 → **THEN** 标注为"可能因素"，提供多角度分析
**ELSE** 进入 Step 6

---

## Step 6: 诊断建议生成

**输入**：根因分析 + 机制分解 + 竞品分析

**动作**：
1. 基于根因分析生成诊断建议
2. 按优先级排序建议
3. 评估每个建议的实施难度
4. 设计验证方法

**输出**：诊断建议清单

**检查点**：
- 建议是否直接针对根因？
- 优先级排序是否合理？
- 实施难度评估是否准确？

**IF** 建议与根因不对应 → **THEN** 重新审视根因分析
**IF** 所有建议实施难度高 → **THEN** 寻找更简单的切入点
**ELSE** 进入 Step 7

---

## Step 7: 综合输出与文档化

**输入**：所有分析结果

**动作**：
1. 汇总结果分析、因果链、根因、机制分解和建议
2. 提取可迁移的知识原则
3. 生成结构化 JSON 输出
4. 标注 `thinking_models_applied`

**输出**：完整分析报告

**检查点**：
- 输出是否符合 JSON Schema？
- 因果链是否完整？
- 建议是否可操作？

**IF** 输出不完整 → **THEN** 补充缺失部分
**ELSE** 输出最终结果

---

## ⚠️ 边界约束

## 硬性约束

| # | 约束 | 说明 |
|---|------|------|
| 1 | 不做无证据推断 | 每个因果环节必须有证据或标注为"待验证" |
| 2 | 不忽略替代解释 | 每个根因必须提供替代解释 |
| 3 | 不假设单一根因 | 可能存在多个并行的根因 |
| 4 | 不替代领域专业知识 | 机制分解需要领域知识验证 |
| 5 | 不做因果倒置 | 逆向推导不等于反向因果 |

## 软性约束

- 优先分析最可能的因果路径
- 置信度评估应保守
- 建议应直接针对根因

## 人工兜底点

- 根因分析需要领域专家验证
- 机制分解需要技术细节补充
- 竞品分析需要数据来源验证

---

## ⚠️ 异常处理

## 异常表格

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|----------|
| ERR-RESULT-VAGUE | 结果描述过于模糊 | 返回引导性问题，要求具体化 | high |
| ERR-NO-EVIDENCE | 无任何证据支持分析 | 标注为"纯推测分析"，降低置信度 | high |
| ERR-CAUSAL-LOOP | 因果链出现循环 | 标注循环点，重新构建因果链 | medium |
| ERR-ROOT-UNREACHABLE | 5 Whys 无法到达可行动根因 | 标注为"系统性根因"，建议系统级干预 | medium |
| WARN-ALTERNATIVE-STRONG | 替代解释与主因竞争 | 标注为"竞争性假设"，建议进一步验证 | medium |
| WARN-MECHANISM-BLACKBOX | 关键机制无法分解 | 标注为"黑箱"，提供推测性分析 | low |
| WARN-REPLICATION-LOW | 关键因素可复制性低 | 标注为"难以迁移"，建议寻找替代方案 | low |

## 降级策略

1. **证据不足降级**：仅完成可用证据支持的分析，标注"需更多证据"
2. **深度不足降级**：仅完成表面因果链，建议深入分析
3. **信息黑箱降级**：标注不可分解的组件，提供推测性分析

---

## ✅ 校验验收规则

## 格式校验

- [ ] 输出为有效 JSON 格式
- [ ] 所有必填字段均已填充
- [ ] 因果链至少包含 3 个环节
- [ ] 枚举值在规定范围内

## 内容校验

- [ ] 因果链从结果追溯到根因
- [ ] 每个环节有证据支持或标注为"待验证"
- [ ] 根因分析到达可行动层级
- [ ] 机制分解深入到组件层面
- [ ] 诊断建议直接针对根因

## 合规校验

- [ ] 不做无证据推断
- [ ] 提供了替代解释
- [ ] 标注了所有不确定性
- [ ] 建议中包含验证需求

## OVP 验证信号

- 因果链条可验证性：每个因果环节可追溯到证据
- 根因可行动性：根因分析到达可干预层级
- 建议针对性：建议直接针对识别的根因

---

## 🔄 迭代触发条件

## Self-Play 触发

- 每次执行后自动触发 10 组 Self-Play 测试
- 测试覆盖：成功分析、失败诊断、竞品拆解、系统逆向
- critic 攻击重点：因果遗漏、根因误判、机制简化

## 版本升级触发

- 当连续 3 次 Self-Play 发现同一类因果遗漏 → 触发版本升级
- 当用户反馈诊断不准确 → 触发版本升级
- 当新增分析维度需求 → 触发版本升级

## 废弃触发

- 当有更好的逆向分析方法出现 → 标记为 deprecated
- 连续 6 个月未被使用 → 标记为 deprecated

---

## 📝 自检清单

- [ ] 结果描述是否客观、具体？
- [ ] 因果链是否完整追溯到根因？
- [ ] 每个环节是否有证据支持？
- [ ] 是否提供了替代解释？
- [ ] 根因是否到达可行动层级？
- [ ] 机制分解是否深入到组件？
- [ ] 诊断建议是否直接针对根因？
- [ ] 输出是否符合 JSON Schema？
- [ ] 是否标注了所有不确定性？
- [ ] 是否提取了可迁移的知识？

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "SP-118-01",
    "name": "产品成功逆向分析",
    "prompt": "Notion 在5年内从0做到100亿美元估值。请逆向分析其成功的关键因素。",
    "context": "生产力工具市场，竞争激烈，Notion实现了差异化",
    "assertions": [
      "构建完整的逆向因果链",
      "识别关键成功因素",
      "评估因素的可复制性",
      "提取可迁移的原则"
    ],
    "expected_behavior": "分析Notion的产品设计、增长策略、社区建设等关键因素的因果机制",
    "critic_attack": "是否忽略了时机因素？是否考虑了创始人背景的影响？"
  },
  {
    "id": "SP-118-02",
    "name": "技术故障诊断",
    "prompt": "我们的API响应时间突然从100ms增加到2秒。请逆向诊断原因。",
    "context": "SaaS产品，最近无代码部署，数据库未变更",
    "assertions": [
      "构建从现象到根因的因果链",
      "应用5 Whys追问",
      "提供多个可能的根因",
      "诊断建议针对根因"
    ],
    "expected_behavior": "分析响应时间增加的可能原因：网络、数据库、依赖服务、负载等",
    "critic_attack": "是否考虑了外部因素？是否检查了监控数据？"
  },
  {
    "id": "SP-118-03",
    "name": "竞品机制拆解",
    "prompt": "TikTok 的推荐算法为什么比其他平台更精准？请拆解其机制。",
    "context": "内容推荐领域，TikTok用户粘性极高",
    "assertions": [
      "深入到算法机制层面",
      "识别关键差异化因素",
      "评估技术可复制性",
      "提取设计原则"
    ],
    "expected_behavior": "分析TikTok的推荐机制：数据收集、算法设计、内容理解、反馈循环",
    "critic_attack": "是否忽略了数据规模效应？是否考虑了内容供给侧的影响？"
  },
  {
    "id": "SP-118-04",
    "name": "失败案例诊断",
    "prompt": "一个众筹项目在达到目标金额后仍然失败了。请逆向分析原因。",
    "context": "硬件产品众筹，筹集50万美元，但最终未能交付",
    "assertions": [
      "构建失败的因果链",
      "识别根本原因和贡献因素",
      "提供改进建议",
      "提取避免失败的原则"
    ],
    "expected_behavior": "分析众筹失败的可能原因：技术、供应链、资金管理、预期管理",
    "critic_attack": "是否忽略了团队能力因素？是否考虑了市场变化？"
  },
  {
    "id": "SP-118-05",
    "name": "组织效能逆向分析",
    "prompt": "为什么Netflix能持续产出高质量原创内容？请逆向分析其组织机制。",
    "context": "内容行业，Netflix每年投入170亿美元内容制作",
    "assertions": [
      "分析组织机制而非个人能力",
      "识别系统性成功因素",
      "评估机制的可迁移性",
      "提取组织设计原则"
    ],
    "expected_behavior": "分析Netflix的文化、决策机制、人才策略、数据驱动的内容制作",
    "critic_attack": "是否忽略了资金规模效应？是否考虑了品牌溢价？"
  }
]
```

---

## 🔗 关联文档

- [[生态系统思维]] — 逆向工程需要系统视角理解机制
- [[禅宗空性与第一性原理：如何剥离日常偏见，还原事物的最底层逻辑]] — 逆向分析需要回归基本事实
- [[二阶思维]] — 逆向分析可能揭示二阶效应
- [[决策推理-Schema]] — 诊断结果输入决策框架
- [[元认知-Schema]] — 识别自身逆向推理的认知偏差
- [[uSkill-agent-认知偏差对抗协议]] — 对抗后见之明偏差和确认偏差

---

## 📝 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-06-23 | 初始版本，包含完整的逆向工程思维分析框架 |


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
