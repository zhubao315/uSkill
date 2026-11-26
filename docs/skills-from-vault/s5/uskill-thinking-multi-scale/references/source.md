
# 🎯 目标

运用多尺度思考方法论，在时间、空间和抽象层级三个维度上进行系统分析，通过宏观与微观的交替视角，为战略规划、问题诊断、研究设计和系统分析提供层次化的洞察框架。

**核心价值**：避免单一尺度的盲点，发现跨尺度的涌现性质和约束关系。

**适用场景**：企业战略规划（公司-部门-团队-个人）、技术架构设计（系统-模块-组件-函数）、政策分析（国家-地区-社区-个人）、研究设计（理论-假设-实验-数据）。

---

## 📥 输入

## 参数表格

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `problem_description` | string | 是 | - | 需要多尺度分析的问题描述 |
| `analysis_dimensions` | list | 否 | ["time", "space", "abstraction"] | 分析维度：time / space / abstraction |
| `primary_scale` | string | 否 | "" | 用户当前关注的主要尺度 |
| `scale_granularity` | enum | 否 | "standard" | 尺度粒度：coarse / standard / fine |
| `stakeholder_perspective` | string | 否 | "" | 利益相关方视角（可选） |
| `constraints` | list | 否 | [] | 已知的约束条件 |
| `output_format` | enum | 否 | "full" | 输出详细度：summary / standard / full |

## 输入约束

- `problem_description` 必须涉及多层次或多尺度的现象
- `analysis_dimensions` 至少包含 1 个维度
- `scale_granularity` = fine 时，每个维度至少 4 个尺度层级
- 不支持单一尺度即可解决的简单问题

---

## 📤 输出

## 标准输出 JSON Schema

```json
{
  "type": "object",
  "properties": {
    "scale_framework": {
      "type": "object",
      "properties": {
        "dimensions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "dimension": {"type": "string", "enum": ["time", "space", "abstraction"]},
              "scales": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {"type": "string"},
                    "level": {"type": "number"},
                    "description": {"type": "string"},
                    "key_elements": {"type": "array", "items": {"type": "string"}}
                  }
                }
              }
            }
          }
        },
        "scale_interactions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "scales": {"type": "array", "items": {"type": "string"}},
              "interaction_type": {"type": "string", "enum": ["constraint", "emergence", "feedback", "alignment"]},
              "description": {"type": "string"}
            }
          }
        }
      }
    },
    "multi_scale_analysis": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dimension": {"type": "string"},
          "scale_level": {"type": "string"},
          "analysis": {"type": "string"},
          "key_insights": {"type": "array", "items": {"type": "string"}},
          "cross_scale_effects": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "scale_conflicts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "conflict": {"type": "string"},
          "scales_involved": {"type": "array", "items": {"type": "string"}},
          "tension_type": {"type": "string", "enum": ["optimization", "timing", "priority", "resource"]},
          "resolution_approach": {"type": "string"}
        }
      }
    },
    "emergent_properties": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "property": {"type": "string"},
          "emerging_from": {"type": "string"},
          "scale": {"type": "string"},
          "significance": {"type": "string", "enum": ["high", "medium", "low"]}
        }
      }
    },
    "scale_specific_recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "scale": {"type": "string"},
          "recommendation": {"type": "string"},
          "rationale": {"type": "string"},
          "trade_offs": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "integration_synthesis": {
      "type": "object",
      "properties": {
        "cross_scale_insights": {"type": "array", "items": {"type": "string"}},
        "leverage_points": {"type": "array", "items": {"type": "string"}},
        "implementation_priorities": {"type": "array", "items": {"type": "string"}},
        "monitoring_framework": {"type": "array", "items": {"type": "string"}}
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

## Step 1: 问题多尺度建模

**输入**：`problem_description` + `analysis_dimensions`

**动作**：
1. 识别问题涉及的所有分析维度
2. 为每个维度定义尺度层级
3. 确定每个尺度的关键元素
4. 识别尺度间的交互关系

**输出**：多尺度框架文档

**检查点**：
- 尺度层级是否合理？
- 是否遗漏了重要尺度？
- 尺度间交互是否明确？

**IF** `analysis_dimensions` 为空 → **THEN** 从问题描述中推断维度
**IF** `primary_scale` 提供 → **THEN** 以此为中心展开分析
**ELSE** 进入 Step 2

---

## Step 2: 时间维度分析

**输入**：多尺度框架 + 时间维度

**动作**：
1. 按时间尺度组织分析（即时/日/周/月/季/年/十年）
2. 识别每个时间尺度的关键特征
3. 分析时间尺度间的依赖关系
4. 识别时间延迟和临界点

**输出**：时间维度多尺度分析

**检查点**：
- 时间尺度是否覆盖问题相关范围？
- 是否识别了关键时间延迟？
- 长期和短期分析是否平衡？

**IF** `scale_granularity` = fine → **THEN** 至少 5 个时间尺度层级
**IF** 问题涉及快速变化 → **THEN** 加强即时和短期分析
**ELSE** 进入 Step 3

---

## Step 3: 空间维度分析

**输入**：多尺度框架 + 空间维度

**动作**：
1. 按空间尺度组织分析（个体/团队/部门/组织/行业/社会）
2. 识别每个空间尺度的关键特征
3. 分析空间尺度间的包含和影响关系
4. 识别空间聚集和扩散效应

**输出**：空间维度多尺度分析

**检查点**：
- 空间尺度是否覆盖问题相关范围？
- 是否识别了关键的空间交互？
- 全局和局部分析是否平衡？

**IF** `stakeholder_perspective` 提供 → **THEN** 从该视角切入分析
**IF** 问题涉及网络效应 → **THEN** 加强跨尺度交互分析
**ELSE** 进入 Step 4

---

## Step 4: 抽象层级分析

**输入**：多尺度框架 + 抽象维度

**动作**：
1. 按抽象层级组织分析（数据/信息/知识/智慧/原则）
2. 识别每个抽象层级的关键特征
3. 分析抽象层级间的归纳和演绎关系
4. 识别跨层级的模式和原理

**输出**：抽象维度多尺度分析

**检查点**：
- 抽象层级是否合理？
- 是否识别了跨层级模式？
- 具体和抽象分析是否平衡？

**IF** 问题偏技术 → **THEN** 加强数据和信息层分析
**IF** 问题偏战略 → **THEN** 加强知识和智慧层分析
**ELSE** 进入 Step 5

---

## Step 5: 尺度冲突识别

**输入**：三个维度的多尺度分析

**动作**：
1. 识别不同尺度间的优化冲突
2. 识别时间尺度间的优先级冲突
3. 识别空间尺度间的资源冲突
4. 设计冲突解决策略

**输出**：尺度冲突清单 + 解决策略

**检查点**：
- 是否识别了所有主要冲突？
- 冲突类型是否准确分类？
- 解决策略是否可行？

**IF** 冲突无法解决 → **THEN** 标注为"需权衡"，提供权衡框架
**IF** 冲突涉及硬约束 → **THEN** 标注为"需遵守"，不提供违反约束的方案
**ELSE** 进入 Step 6

---

## Step 6: 涌现性质识别

**输入**：多尺度分析 + 尺度冲突

**动作**：
1. 识别从低层尺度涌现的高层性质
2. 分析涌现性质的意义和影响
3. 识别跨尺度的杠杆点
4. 评估涌现性质的可控性

**输出**：涌现性质清单

**检查点**：
- 涌现性质是否真正源于跨尺度交互？
- 涌现性质是否具有实际意义？
- 杠杆点是否位于关键尺度？

**IF** 无法识别涌现性质 → **THEN** 重新检查尺度间交互
**IF** 涌现性质不可控 → **THEN** 标注为"需适应"，建议调整预期
**ELSE** 进入 Step 7

---

## Step 7: 综合输出与文档化

**输入**：所有分析结果

**动作**：
1. 汇总多尺度分析、冲突、涌现性质和建议
2. 生成跨尺度综合洞察
3. 设计监控框架
4. 生成结构化 JSON 输出
5. 标注 `thinking_models_applied`

**输出**：完整分析报告

**检查点**：
- 输出是否符合 JSON Schema？
- 尺度分析是否全面？
- 综合建议是否整合了多尺度洞察？

**IF** 输出不完整 → **THEN** 补充缺失部分
**ELSE** 输出最终结果

---

## ⚠️ 边界约束

## 硬性约束

| # | 约束 | 说明 |
|---|------|------|
| 1 | 不忽略任何重要尺度 | 分析必须覆盖所有相关尺度层级 |
| 2 | 不偏重单一尺度 | 宏观和微观分析必须平衡 |
| 3 | 不假设尺度间独立 | 必须分析尺度间的交互关系 |
| 4 | 不忽略涌现性质 | 低层到高层的涌现必须被识别 |
| 5 | 不忽视时间维度 | 空间和抽象分析必须结合时间尺度 |

## 软性约束

- 尺度层级数量 3-7 个（避免过少或过多）
- 每个尺度的分析深度应与其重要性匹配
- 跨尺度洞察应优先于单尺度洞察

## 人工兜底点

- 尺度划分需要领域专家确认
- 涌现性质的评估需要实证验证
- 冲突解决策略需要利益相关方评审

---

## ⚠️ 异常处理

## 异常表格

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|----------|
| ERR-SCALE-MISS | 遗漏重要尺度层级 | 补充遗漏尺度，重新分析 | high |
| ERR-CONFLICT-UNRESOLVED | 尺度冲突无法解决 | 标注为"需权衡"，提供权衡框架 | medium |
| ERR-EMERGENCE-UNIDENTIFIED | 无法识别涌现性质 | 重新检查尺度间交互，标注"可能无涌现" | medium |
| ERR-DIMENSION-EMPTY | 某维度分析为空 | 补充该维度分析或标注"不适用" | medium |
| WARN-SCALE-IMBALANCED | 尺度分析不平衡 | 建议加强薄弱尺度的分析 | low |
| WARN-CROSS-SCALE-WEAK | 跨尺度洞察不足 | 建议增加尺度间交互分析 | low |
| WARN-ABSTRACTION-MISSING | 缺少抽象层级分析 | 建议补充抽象维度 | low |

## 降级策略

1. **维度不足降级**：仅完成可用维度的分析，标注"部分维度缺失"
2. **粒度不足降级**：使用标准粒度，标注"建议细化"
3. **冲突未解降级**：输出冲突分析但不提供解决方案

---

## ✅ 校验验收规则

## 格式校验

- [ ] 输出为有效 JSON 格式
- [ ] 所有必填字段均已填充
- [ ] 每个维度至少 3 个尺度层级
- [ ] 枚举值在规定范围内

## 内容校验

- [ ] 时间、空间、抽象三个维度均有分析
- [ ] 尺度间交互关系被识别
- [ ] 至少识别 1 个尺度冲突
- [ ] 至少识别 1 个涌现性质
- [ ] 综合建议整合了多尺度洞察

## 合规校验

- [ ] 不忽略任何重要尺度
- [ ] 宏观和微观分析平衡
- [ ] 标注了所有不确定性
- [ ] 建议中包含人工审查提示

## OVP 验证信号

- 尺度切换覆盖完整性：三个维度均有分析
- 跨尺度一致性验证：不同尺度的分析不矛盾
- 涌现性质可追溯性：涌现性质可追溯到尺度交互

---

## 🔄 迭代触发条件

## Self-Play 触发

- 每次执行后自动触发 10 组 Self-Play 测试
- 测试覆盖：战略规划、技术架构、政策分析、研究设计
- critic 攻击重点：尺度遗漏、分析不平衡、涌现忽略

## 版本升级触发

- 当连续 3 次 Self-Play 发现同一类尺度遗漏 → 触发版本升级
- 当用户反馈分析不平衡 → 触发版本升级
- 当新增分析维度需求 → 触发版本升级

## 废弃触发

- 当有更好的多尺度分析方法出现 → 标记为 deprecated
- 连续 6 个月未被使用 → 标记为 deprecated

---

## 📝 自检清单

- [ ] 是否覆盖了时间、空间、抽象三个维度？
- [ ] 每个维度是否至少 3 个尺度层级？
- [ ] 尺度间交互关系是否被识别？
- [ ] 是否识别了尺度冲突？
- [ ] 是否识别了涌现性质？
- [ ] 宏观和微观分析是否平衡？
- [ ] 输出是否符合 JSON Schema？
- [ ] 是否标注了所有不确定性？
- [ ] 综合建议是否整合了多尺度洞察？
- [ ] 是否提供了监控框架？

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "SP-116-01",
    "name": "企业战略多尺度分析",
    "prompt": "我们是一家快速成长的科技公司，从50人扩张到500人。请从多尺度角度分析组织变革。",
    "context": "B2B SaaS，年增长100%，组织效率下降",
    "assertions": [
      "覆盖时间尺度（短期/中期/长期）",
      "覆盖空间尺度（个人/团队/部门/公司）",
      "识别尺度间的冲突",
      "识别涌现的组织性质"
    ],
    "expected_behavior": "分析个人→团队→部门→公司的空间尺度变化，识别文化涌现和效率瓶颈",
    "critic_attack": "是否忽略了行业尺度？是否考虑了时间延迟效应？"
  },
  {
    "id": "SP-116-02",
    "name": "技术架构多尺度设计",
    "prompt": "请从多尺度角度分析一个分布式系统的技术架构设计。",
    "context": "微服务架构，需要支持1000万用户",
    "assertions": [
      "覆盖系统→服务→组件→函数的抽象层级",
      "识别跨层级的性能约束",
      "识别架构的涌现性质",
      "提供尺度特定的优化建议"
    ],
    "expected_behavior": "分析从系统架构到代码实现的多层级设计，识别延迟和吞吐量的跨层级影响",
    "critic_attack": "是否忽略了运维尺度？是否考虑了成本约束？"
  },
  {
    "id": "SP-116-03",
    "name": "政策多尺度评估",
    "prompt": "评估碳税政策在不同尺度上的影响：个人、企业、行业、国家、全球。",
    "context": "气候政策，需要平衡经济发展和减排目标",
    "assertions": [
      "覆盖五个空间尺度的分析",
      "识别尺度间的利益冲突",
      "分析时间维度的延迟效应",
      "识别跨尺度的涌现影响"
    ],
    "expected_behavior": "分析碳税从个人消费到全球气候的多层级影响，识别政策传导机制",
    "critic_attack": "是否忽略了区域差异？是否考虑了国际竞争影响？"
  },
  {
    "id": "SP-116-04",
    "name": "个人成长多尺度规划",
    "prompt": "请从多尺度角度分析我的职业发展规划：日、周、月、年、五年。",
    "context": "30岁，技术背景，希望转向管理",
    "assertions": [
      "覆盖五个时间尺度的分析",
      "识别不同时间尺度的目标冲突",
      "提供尺度特定的行动建议",
      "整合短期和长期视角"
    ],
    "expected_behavior": "分析日常习惯到五年愿景的多时间尺度规划，识别习惯养成和能力积累的关系",
    "critic_attack": "是否忽略了行业周期？是否考虑了个人健康尺度？"
  },
  {
    "id": "SP-116-05",
    "name": "研究设计多尺度框架",
    "prompt": "请从多尺度角度设计一个社会科学研究项目。",
    "context": "研究远程工作对组织效率的影响",
    "assertions": [
      "覆盖理论→假设→实验→数据的抽象层级",
      "识别不同层级的方法论约束",
      "分析微观行为和宏观模式的关系",
      "提供多尺度的验证策略"
    ],
    "expected_behavior": "设计从理论框架到数据采集的多层级研究方案，识别跨层级的因果机制",
    "critic_attack": "是否忽略了伦理尺度？是否考虑了推广性问题？"
  }
]
```

---

## 🔗 关联文档

- [[生态系统思维]] — 多尺度思考是系统思维的重要组成部分
- [[二阶思维]] — 多尺度分析可以揭示二阶效应
- [[禅宗空性与第一性原理：如何剥离日常偏见，还原事物的最底层逻辑]] — 不同抽象层级的分析需要回归基本事实
- [[决策推理-Schema]] — 多尺度分析结果输入决策框架
- [[元认知-Schema]] — 识别自身思维的尺度偏差
- [[概率思维]] — 不同尺度的不确定性评估

---

## 📝 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-06-23 | 初始版本，包含完整的多尺度思考分析框架 |


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


**相关概念**：[[MECE原则]]

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
