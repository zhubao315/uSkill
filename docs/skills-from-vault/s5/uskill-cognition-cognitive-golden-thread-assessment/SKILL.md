---
name: uskill-cognition-cognitive-golden-thread-assessment
description: "让cognitive golden thread assessment变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-golden-thread-assessment.md"
  original_id: "SKL-6835"
  version: "3.0.0"
  trust: untrusted
---

# cognitive golden thread assessment

# Apply Golden Thread Quality Assessment

## 🎯 目标
> 运用"金线"理念，对难以量化但存在明确品质层级差异的事物（如作品、方案、表达、决策）进行定性评估。帮助用户识别"达标"与"未达标"之间的关键分界线，建立对品质的直觉判断力，避免被表面指标（如销量、流量、权威背书）误导。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `subject` | string | ✅ | 需要评估品质的事物（作品、方案、表达、决策等） |
| `domain` | string | ✅ | 所属领域（如写作、产品设计、演讲、投资决策、代码质量） |
| `criteria_hint` | string | ❌ | 用户认为重要的评估维度或已有评价标准 |
| `audience` | enum | `beginner` / `intermediate` / `expert`，默认 `intermediate` | 评估者的专业水平，影响金线阈值的敏感度 |
| `mode` | enum | `assess` / `calibrate` / `compare`，默认 `assess` | `assess`=单件品质评估；`calibrate`=帮助用户校准自身金线感知；`compare`=对比两件事物的品质差异 |
| `compare_with` | string | `mode=compare` 时必填 | 用于对比的参照物 |
| `output_format` | enum | ❌ | `markdown` / `json`，默认 `markdown` |

## 📤 输出

```json
{
  "golden_line_assessment": {
    "subject": "string — 被评估对象",
    "domain": "string — 所属领域",
    "verdict": "string — above / at / below / approaching（金线之上 / 恰好达标 / 金线之下 / 接近金线）",
    "confidence": "string — 高 / 中 / 低",
    "reasoning": "string — 判定依据，说明为什么高于或低于金线"
  },
  "quality_dimensions": [
    {
      "dimension": "string — 评估维度名称（如：结构完整性、表达清晰度、思想深度）",
      "score": "string — 优秀 / 达标 / 不足",
      "evidence": "string — 具体表现",
      "weight": "string — 高 / 中 / 低（该维度对整体金线判定的影响权重）"
    }
  ],
  "threshold_analysis": {
    "the_line": "string — 该领域金线的具体描述（什么算'达到了'）",
    "what_makes_it_cross": ["string — 使作品/方案跨越金线的关键要素"],
    "what_holds_it_back": ["string — 阻碍跨越金线的关键缺陷"],
    "common_misconceptions": ["string — 该领域中容易与金线混淆的表面指标"]
  },
  "improvement_path": {
    "minimum_to_cross": ["string — 达到金线的最低改进项"],
    "to_excellence": ["string — 从金线到卓越的进阶方向"],
    "estimated_gap": "string — 当前与金线的距离（一步之遥 / 需要显著提升 / 差距较大）"
  }
}
```

## 📋 执行步骤

1. **领域定位** — 明确评估对象所属领域，识别该领域的"金线"具体含义：
   - 金线的本质：**难以量化但确实存在的品质分界线**
   - 不同领域的金线不同：文学看表达力与思想深度，产品看用户体验与问题解决能力，投资看风险收益比与逻辑自洽性
   - 金线与流行度/市场表现无必然正相关，某些时代甚至负相关
2. **多维评估** — 从3-5个关键品质维度逐一审视评估对象：
   - 识别各维度的达标表现与不足表现
   - 为每个维度分配权重（该维度对整体品质的影响程度）
   - 避免被单一亮点或缺陷过度影响判断
3. **金线判定** — 综合各维度表现，给出最终判定：
   - **above**：整体品质明确跨越金线，行家一看便知
   - **at**：恰好踩在线上，有争议空间
   - **approaching**：接近但尚有关键差距
   - **below**：整体品质未达标
4. **阈值分析**（`mode=assess` 时）— 深入解读金线标准：
   - 明确该领域金线的具体定义
   - 指出跨越金线的关键要素与阻碍因素
   - 警示常见的表面指标误导（如以流量代替品质、以资历代替能力）
5. **校准训练**（`mode=calibrate` 时）— 帮助用户校准自身对品质的感知：
   - 提供该领域的经典"达标"与"未达标"案例
   - 分析案例中决定品质的关键差异
   - 给出训练建议：如何通过持续接触高质量作品来提升辨别力
6. **对比评估**（`mode=compare` 时）— 将两件事物放在一起比较：
   - 同维度对照，指出相对差异
   - 判断两者是否处于金线的同一侧
   - 指出各自的优势领域与短板

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 领域过于宽泛或模糊 | 先与用户确认具体细分领域，再定位金线标准 |
| 评估对象信息不充分 | 基于已有信息给出初步评估，标注不确定性，列出需要补充的信息 |
| 用户以流行度/市场表现反推品质 | 温和指出金线与市场表现无必然正相关，提供具体反例 |
| 用户过度自信或过度贬低 | 用具体维度分析替代笼统判断，引导用户关注品质本身 |
| 评估涉及高度主观的领域（如艺术） | 承认主观性存在，但指出即使在主观领域也有公认的专业标准 |
| 用户试图将金线概念用于打压他人 | 拒绝傲慢用法，强调金线是自我审视工具而非攻击武器 |

## ✅ 自检清单

- [ ] 输出包含 `golden_line_assessment`、`quality_dimensions`、`threshold_analysis`、`improvement_path` 四个模块
- [ ] 金线判定基于多维度综合评估，非单一指标
- [ ] 判定依据具体可追溯，非空泛断言
- [ ] 警示了该领域中常见的表面指标误导
- [ ] 改进建议分"达标"和"卓越"两个层次
- [ ] 态度谦逊客观，强调金线是自我审视工具
- [ ] 输出语言通俗易懂，避免故作高深


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
| 2026-05-08 | 1.0.0 | 初始版本，从"金线"方法论转化 |

---
**相关笔记**：[[等击球点决策]] [[知识系统管理]] 


---


---


---

## 📖 Context R

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
