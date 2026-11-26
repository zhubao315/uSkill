
# 🎯 目标

运用类比推理方法论，通过跨领域的结构映射，从已知领域迁移模型和解决方案到新领域，为创新启发、教学解释、方案借鉴和概念理解提供系统化的类比分析框架。

**核心价值**：将陌生问题转化为熟悉问题，利用已有知识加速理解和创新。

**适用场景**：创新方案构思、复杂概念教学、跨行业方案借鉴、新产品设计启发、组织变革路径规划。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `target_domain` | string | 是 | - | 需要理解或解决的目标领域问题 |
| `source_domain_hint` | string | 否 | "" | 用户提示的可能类比源域（可选） |
| `problem_type` | enum | 否 | "understanding" | 问题类型：understanding / innovation / explanation / design |
| `mapping_depth` | enum | 否 | "structural" | 映射深度：surface / structural / deep |
| `constraints` | list | 否 | [] | 目标域的约束条件 |
| `existing_analogies` | list | 否 | [] | 用户已有的类比想法（可选验证） |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `target_domain` 必须是具体的、可描述的问题或概念
- `mapping_depth` = deep 时，要求提供 `constraints` 至少 2 条
- `source_domain_hint` 如果提供，系统将优先评估该类比的适用性
- 不支持纯抽象概念的类比（需要具体的结构或过程）

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "target_analysis": {
      "type": "object",
      "properties": {
        "problem": {"type": "string"},
        "key_elements": {"type": "array", "items": {"type": "string"}},
        "relationships": {"type": "array", "items": {"type": "string"}},
        "constraints": {"type": "array", "items": {"type": "string"}},
        "goal": {"type": "string"}
      }
    },
    "analogy_candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source_domain": {"type": "string"},
          "structural_similarity": {"type": "number", "minimum": 0, "maximum": 1},
          "surface_similarity": {"type": "number", "minimum": 0, "maximum": 1},
          "mapping_quality": {"type": "string", "enum": ["excellent", "good", "fair", "poor"]},
          "strengths": {"type": "array", "items": {"type": "string"}},
          "limitations": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "selected_analogy": {
      "type": "object",
      "properties": {
        "source_domain": {"type": "string"},
        "selection_reason": {"type": "string"},
        "structural_mapping": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "source_element": {"type": "string"},
              "target_element": {"type": "string"},
              "mapping_type": {"type": "string", "enum": ["direct", "analogous", "functional"]},
              "confidence": {"type": "string", "enum": ["high", "medium", "low"]}
            }
          }
        },
        "process_mapping": {"type": "array", "items": {"type": "object"}},
        "principle_mapping": {"type": "array", "items": {"type": "object"}}
      }
    },
    "insights_generated": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "insight": {"type": "string"},
          "source": {"type": "string"},
          "implications": {"type": "array", "items": {"type": "string"}},
          "novelty": {"type": "string", "enum": ["high", "medium", "low"]},
          "actionability": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "analogical_reasoning": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step": {"type": "number"},
          "reasoning": {"type": "string"},
          "evidence": {"type": "string"},
          "confidence": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "limitations_and_caveats": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "limitation": {"type": "string"},
          "impact": {"type": "string"},
          "mitigation": {"type": "string"}
        }
      }
    },
    "validation_results": {
      "type": "object",
      "properties": {
        "structural_fit": {"type": "number", "minimum": 0, "maximum": 1},
        "surface_fit": {"type": "number", "minimum": 0, "maximum": 1},
        "overall_quality": {"type": "string", "enum": ["excellent", "good", "fair", "poor"]},
        "recommendation": {"type": "string"}
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

## Step 1: 目标域分析

**输入**：`target_domain` + `constraints`

**动作**：
1. 精确描述目标域的问题、概念或过程
2. 识别目标域的关键元素和关系
3. 明确约束条件
4. 定义分析目标（understanding / innovation / explanation / design）

**输出**：目标域分析文档

**检查点**：目标域是否足够具体？是否识别了核心结构？

**IF** `target_domain` 过于抽象 → **THEN** 要求具体化，提供具体案例或情境
**IF** `constraints` 为空 → **THEN** 推断隐含约束，标注"推断约束"
**ELSE** 进入 Step 2

---

## Step 2: 类比源域搜索

**输入**：目标域分析 + `source_domain_hint`

**动作**：
1. 如果有 `source_domain_hint`，优先评估该源域
2. 搜索结构相似的候选源域
3. 评估每个候选源域的结构相似度和表面相似度
4. 排序候选源域

**输出**：候选源域列表 + 相似度评估

**检查点**：
- 候选源域是否真正结构相似？
- 是否避免了仅表面相似的源域？
- 是否覆盖了不同领域的候选？

**IF** `source_domain_hint` 提供 → **THEN** 优先评估，标注"用户提议"
**IF** 无法找到结构相似的源域 → **THEN** 降低映射深度到 surface，标注"仅表面类比"
**ELSE** 进入 Step 3

---

## Step 3: 结构映射

**输入**：目标域分析 + 选定源域

**动作**：
1. 建立源域和目标域的元素映射
2. 建立过程映射
3. 建立原则映射
4. 评估映射的置信度

**输出**：结构映射表

**检查点**：
- 映射是否一一对应？
- 映射是否保持了结构一致性？
- 是否标注了映射的置信度？

**IF** 某些元素无法映射 → **THEN** 标注为"类比局限"，不强行映射
**IF** 映射出现矛盾 → **THEN** 重新评估源域选择
**ELSE** 进入 Step 4

---

## Step 4: 洞察生成

**输入**：结构映射表

**动作**：
1. 从映射关系中提取洞察
2. 识别源域中目标域没有但可能有用的元素
3. 识别源域的解决方案如何迁移到目标域
4. 评估洞察的新颖性和可操作性

**输出**：洞察清单

**检查点**：
- 洞察是否真正源于结构映射？
- 洞察是否具有可操作性？
- 是否识别了"非显而易见"的洞察？

**IF** 洞察仅为常识 → **THEN** 深入挖掘，寻找更深层的迁移
**IF** 洞察过于理想化 → **THEN** 评估约束条件下的可行性
**ELSE** 进入 Step 5

---

## Step 5: 类比推理链条构建

**输入**：洞察清单 + 结构映射

**动作**：
1. 构建从源域到目标域的推理链条
2. 每一步标注推理依据和置信度
3. 检查推理链条的逻辑一致性
4. 识别推理中的假设和跳跃

**输出**：类比推理链条

**检查点**：
- 推理链条是否逻辑自洽？
- 是否有逻辑跳跃？
- 每步推理是否有依据？

**IF** 推理链条出现断裂 → **THEN** 补充中间步骤或标注为"待验证"
**IF** 推理得出意外结论 → **THEN** 回溯检查，确认不是类比误用
**ELSE** 进入 Step 6

---

## Step 6: 局限性分析与验证

**输入**：推理链条 + 结构映射

**动作**：
1. 系统识别类比的局限性
2. 评估类比的适用边界
3. 设计验证方法
4. 提供使用建议

**输出**：局限性报告 + 验证结果

**检查点**：
- 是否识别了所有主要局限性？
- 验证方法是否可操作？
- 使用建议是否清晰？

**IF** 局限性大于相似性 → **THEN** 建议寻找更好的类比源域
**IF** `existing_analogies` 提供 → **THEN** 评估已有类比的质量，提供改进建议
**ELSE** 进入 Step 7

---

## Step 7: 综合输出与文档化

**输入**：所有分析结果

**动作**：
1. 汇总目标分析、类比候选、结构映射、洞察和局限性
2. 生成结构化 JSON 输出
3. 标注 `thinking_models_applied`

**输出**：完整分析报告

**检查点**：
- 输出是否符合 JSON Schema？
- 映射是否完整？
- 是否标注了所有局限性？

**IF** 输出不完整 → **THEN** 补充缺失部分
**ELSE** 输出最终结果

---

## ⚠️ 边界约束

## 硬性约束

| # | 约束 | 说明 |
|---|------|------|
| 1 | 不替代领域分析 | 类比是启发工具，不替代对目标域的深入理解 |
| 2 | 不忽略类比局限 | 每个类比必须标注局限性和适用边界 |
| 3 | 不过度依赖表面相似 | 结构相似性优先于表面相似性 |
| 4 | 不做因果推断 | 类比识别相似性，不证明因果关系 |
| 5 | 不替代实证验证 | 类比洞察需要实证数据验证 |

## 软性约束

- 优先选择结构相似度 > 0.7 的源域
- 类比推理链条不超过 5 步
- 局限性分析必须覆盖

## 人工兜底点

- 源域选择需要领域专家确认
- 结构映射需要验证因果机制
- 洞察的可操作性需要实践检验

---

## ⚠️ 异常处理

## 异常表格

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|----------|
| ERR-TARGET-VAGUE | 目标域描述过于模糊 | 返回引导性问题，要求具体化 | high |
| ERR-NO-ANALOGY | 无法找到结构相似的源域 | 降低映射深度，标注为"启发性类比" | high |
| ERR-MAPPING-CONFLICT | 结构映射出现矛盾 | 重新评估源域选择 | medium |
| ERR-REASONING-GAP | 推理链条出现断裂 | 补充中间步骤或标注为"待验证" | medium |
| WARN-SURFACE-ONLY | 仅表面相似，缺乏结构相似 | 标注为"表面类比"，建议深入挖掘 | low |
| WARN-WEAK-MAPPING | 部分映射置信度低 | 标注为"低置信度映射"，建议验证 | low |
| WARN-LIMITATION-MAJOR | 类比局限性大于相似性 | 建议寻找更好的类比源域 | medium |

## 降级策略

1. **结构相似不足降级**：降低到 surface 映射，标注为"启发性"
2. **源域未知降级**：使用通用类比库，标注为"推荐类比"
3. **推理断裂降级**：仅输出已验证的映射，跳过推测性推理

---

## ✅ 校验验收规则

## 格式校验

- [ ] 输出为有效 JSON 格式
- [ ] 所有必填字段均已填充
- [ ] 映射表至少包含 3 个元素映射
- [ ] 枚举值在规定范围内

## 内容校验

- [ ] 类比源域和目标域真正结构相似
- [ ] 映射保持了一一对应关系
- [ ] 洞察具有新颖性和可操作性
- [ ] 局限性分析覆盖了主要限制
- [ ] 推理链条逻辑自洽

## 合规校验

- [ ] 不忽略类比局限性
- [ ] 不做因果推断
- [ ] 标注了所有不确定性
- [ ] 建议中包含验证需求

## OVP 验证信号

- 跨领域迁移可验证性：洞察可追溯到结构映射
- 映射质量：结构相似度 > 0.6
- 局限性覆盖：所有主要局限性均已标注

---

## 🔄 迭代触发条件

## Self-Play 触发

- 每次执行后自动触发 10 组 Self-Play 测试
- 测试覆盖：技术创新、商业模式、教学解释、组织设计
- critic 攻击重点：表面类比、映射错误、局限性忽略

## 版本升级触发

- 当连续 3 次 Self-Play 发现同一类映射错误 → 触发版本升级
- 当用户反馈类比洞察不准确 → 触发版本升级
- 当新增类比源域库 → 触发版本升级

## 废弃触发

- 当有更好的跨领域推理方法出现 → 标记为 deprecated
- 连续 6 个月未被使用 → 标记为 deprecated

---

## 📝 自检清单

- [ ] 目标域是否足够具体？
- [ ] 源域是否真正结构相似？
- [ ] 映射是否保持了一一对应？
- [ ] 洞察是否具有新颖性？
- [ ] 推理链条是否逻辑自洽？
- [ ] 是否识别了类比的局限性？
- [ ] 输出是否符合 JSON Schema？
- [ ] 是否标注了所有不确定性？
- [ ] 是否避免了表面类比的陷阱？
- [ ] 是否提供了验证方法？

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "SP-115-01",
    "name": "技术创新类比",
    "prompt": "我在设计一个去中心化协作平台，有没有其他领域的类似系统可以借鉴？",
    "context": "Web3方向，需要支持大规模协作，当前方案效率低下",
    "assertions": [
      "找到结构相似的源域",
      "映射保持结构一致性",
      "洞察具有可操作性",
      "识别了类比的局限性"
    ],
    "expected_behavior": "可能找到生物系统（如蚁群）、市场机制、开源社区等类比源域",
    "critic_attack": "类比是否过度简化了技术复杂性？是否考虑了激励机制差异？"
  },
  {
    "id": "SP-115-02",
    "name": "商业模式借鉴",
    "prompt": "我们是一家教育科技公司，想借鉴游戏行业的用户留存策略。请分析类比。",
    "context": "在线教育平台，完课率30%，用户流失严重",
    "assertions": [
      "识别游戏行业的核心留存机制",
      "建立结构映射",
      "评估映射的适用性",
      "识别局限性和适配挑战"
    ],
    "expected_behavior": "分析游戏的即时反馈、成就系统、社交机制如何迁移到教育场景",
    "critic_attack": "是否忽略了学习动机的本质差异？是否考虑了道德风险？"
  },
  {
    "id": "SP-115-03",
    "name": "教学概念类比",
    "prompt": "如何用类比向非技术人员解释区块链的共识机制？",
    "context": "需要面向普通用户的科普",
    "assertions": [
      "找到日常生活的类比源域",
      "映射简化但不失真",
      "识别类比的教学价值和局限",
      "提供多层次的解释"
    ],
    "expected_behavior": "可能使用投票、日记本、公证处等日常概念进行类比",
    "critic_attack": "类比是否过度简化了技术细节？是否引入了新的误解？"
  },
  {
    "id": "SP-115-04",
    "name": "组织设计类比",
    "prompt": "我们想设计一个自组织团队结构，有没有自然界的类似系统？",
    "context": "科技公司，200人，希望提高创新效率",
    "assertions": [
      "找到生物学或物理学的类比",
      "映射组织原则",
      "识别实施挑战",
      "评估文化适配性"
    ],
    "expected_behavior": "可能找到鸟群、鱼群、免疫系统等自组织系统的类比",
    "critic_attack": "是否忽略了人类社会的特殊性？是否考虑了文化差异？"
  },
  {
    "id": "SP-115-05",
    "name": "验证已有类比",
    "prompt": "有人说'创业就像登山'，请评估这个类比的质量。",
    "context": "创业者，正在评估这个类比的适用性",
    "assertions": [
      "评估结构相似度",
      "识别相似点和差异点",
      "分析类比的适用边界",
      "提供改进建议"
    ],
    "expected_behavior": "评估'创业-登山'类比的结构映射，识别局限性，建议更精确的类比",
    "critic_attack": "是否忽略了创业的迭代性质？是否考虑了团队协作维度？"
  }
]
```

---

## 🔗 关联文档

- [[禅宗空性与第一性原理：如何剥离日常偏见，还原事物的最底层逻辑]] — 类比推理与第一性原理互补，提供不同视角
- [[生态系统思维]] — 类比可以帮助理解复杂系统的结构
- [[概率思维]] — 评估类比洞察的不确定性
- [[决策推理-Schema]] — 类比洞察输入决策框架
- [[元认知-Schema]] — 识别类比推理中的认知偏差
- [[uSkill-agent-认知偏差对抗协议]] — 对抗确认偏差和锚定效应

---

## 📝 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-06-23 | 初始版本，包含完整的类比推理分析框架 |


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
