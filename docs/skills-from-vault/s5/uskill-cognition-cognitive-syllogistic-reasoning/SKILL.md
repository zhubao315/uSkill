---
name: uskill-cognition-cognitive-syllogistic-reasoning
description: "让cognitive syllogistic reasoning变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-syllogistic-reasoning.md"
  original_id: "SKL-5048"
  version: "3.0.0"
  trust: untrusted
---

# cognitive syllogistic reasoning

# Apply Syllogistic Reasoning

## 🎯 目标
> 运用三段式推理（大前提→小前提→结论）构建严密的逻辑论证，对任意论述进行逻辑结构拆解与有效性检验，识别常见逻辑谬误，帮助用户在决策、写作、辩论中建立经得起推敲的推理框架。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `subject` | string | ✅ | 需要推理分析的论题、观点或决策场景 |
| `premise_text` | string | ❌ | 已有的推理过程或论证文本，供拆解分析 |
| `mode` | enum | `construct` / `validate` / `detect`，默认 `construct` | `construct`=构建三段式论证；`validate`=检验已有推理的有效性；`detect`=识别论证中的逻辑谬误 |
| `domain` | string | ❌ | 论题所属领域（如投资、医学、法律、技术），影响大前提的可信度评估标准 |
| `output_format` | enum | ❌ | `markdown` / `json`，默认 `markdown` |

## 📤 输出

```json
{
  "syllogism": {
    "major_premise": {
      "statement": "string — 大前提（普遍规律/一般性陈述）",
      "source_type": "string — 科学规律 / 统计事实 / 经验总结 / 假设",
      "confidence": "string — 高 / 中 / 低",
      "known_exceptions": ["string — 已知的例外情况"]
    },
    "minor_premise": {
      "statement": "string — 小前提（具体事实/个案陈述）",
      "factual_basis": "string — 事实依据来源",
      "relevance_to_major": "string — 与大前提的关联说明"
    },
    "conclusion": {
      "statement": "string — 结论",
      "scope_boundaries": "string — 结论的适用范围限定",
      "validity": "string — 有效 / 无效 / 需补充前提",
      "confidence": "string — 必然 / 高度可能 / 可能 / 不确定"
    }
  },
  "logic_check": {
    "middle_term_distributed": "boolean — 中项是否至少在一个前提中周延",
    "conclusion_exceeds_premises": "boolean — 结论是否超出前提范围",
    "premises_sound": "boolean — 前提是否可靠",
    "identified_fallacies": [
      {
        "type": "string — 谬误类型",
        "description": "string — 谬误描述",
        "location": "string — 出现位置",
        "fix": "string — 修正建议"
      }
    ]
  },
  "strengthening_suggestions": {
    "missing_premises": ["string — 可补充的前提"],
    "counterarguments": ["string — 可能的反驳角度"],
    "improved_version": "string — 加固后的完整推理"
  }
}
```

## 📋 执行步骤

1. **论题解析** — 明确需要论证或验证的核心命题，识别其中隐含的普遍规律假设与具体事实陈述
2. **前提确立** —
   - **大前提**：提取或构建一般性规律/原则，标注其来源类型（科学规律 / 统计事实 / 经验总结 / 假设）和可信度
   - **小前提**：确认具体情境/个案的事实描述，验证其真实性与相关性
   - **中项检验**：确保连接大小前提的中项（如"人"）至少在一个前提中涵盖全部范围
3. **结论推导** — 从前提出发推导必然结论，严格执行范围限定：结论不得超越前提所设边界
4. **有效性检验**（`mode=validate` 时）— 检查已有推理的：
   - 前提真实性：是否有充分证据支持？
   - 中项周延性：连接项是否在至少一个前提中涵盖全范围？
   - 结论范围：是否超出前提允许的边界？
5. **谬误检测**（`mode=detect` 时）— 逐一排查五大常见逻辑陷阱：
   - **滑坡谬误**：无根据的连锁推导（A→B→C→D，每步缺乏证据）
   - **肯定后件**：将"若A则B"误读为"若B则A"
   - **否定前件**：将"若A则B"误读为"若非A则非B"
   - **仓促概括**：从少量特例推导普遍规律
   - **伪两难困境**：将复杂情境简化为非此即彼
6. **加固建议** — 提出可补充的前提、可能的反驳角度，以及加固后的完整推理版本

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 大前提本身存在争议 | 标注争议性，列出支持与反对的证据，降低置信度 |
| 小前提事实性存疑 | 标注事实来源可信度，建议用户补充证据 |
| 中项不周延 | 明确指出失效点，给出修正方案（如将"部分"改为"所有"，或降低结论确定性） |
| 结论无法从前提必然推出 | 将结论降级为"可能"或"高度可能"，明确标注其归纳性质 |
| 用户提供的推理文本含多重推理链 | 逐段拆解，分别检验每一段推理的有效性 |
| 领域专业性超出能力范围 | 在前提可信度中标注不确定性，建议寻求领域专家验证 |

## ✅ 自检清单

- [ ] 输出包含 `syllogism`、`logic_check`、`strengthening_suggestions` 三个模块
- [ ] 大前提标注了来源类型和可信度，非凭空断言
- [ ] 小前提与大前提的关联性已明确说明
- [ ] 中项周延性已检验，结论未超出前提范围
- [ ] 谬误检测覆盖五种常见类型（滑坡、肯定后件、否定前件、仓促概括、伪两难）
- [ ] 加固建议具体可执行，包含补强前提和反驳预判
- [ ] 输出语言通俗易懂，推理过程可视化


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从三段式推理方法论转化 |

---
**相关笔记**：[[uSkill-cognition-知识缺口识别]] [[多尺度思考]] 


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
