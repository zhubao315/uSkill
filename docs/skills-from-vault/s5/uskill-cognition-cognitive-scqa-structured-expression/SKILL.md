---
name: uskill-cognition-cognitive-scqa-structured-expression
description: "让cognitive scqa structured expression变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-scqa-structured-expression.md"
  original_id: "SKL-5089"
  version: "3.0.0"
  trust: untrusted
---

# cognitive scqa structured expression

# SCQA 结构化表达

## 🎯 目标
> 使用SCQA框架（情景-冲突-疑问-回答）将模糊的想法组织为清晰、有说服力的结构化表达，适用于汇报、写作、演讲等场景。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `topic` | string | ✅ | 要表达的核心主题或观点 |
| `context` | string | ✅ | 相关背景信息 |
| `audience` | string | ❌ | 目标受众（默认：通用） |
| `style` | enum | ❌ | `formal` / `casual` / `persuasive`，默认 `formal` |
| `max_length` | int | ❌ | 输出最大字数，默认 500 |

## 📤 输出

```json
{
  "situation": "string — 情景描述（背景事实）",
  "complication": "string — 冲突/问题（与期望的矛盾）",
  "question": "string — 核心疑问（受众关心的问题）",
  "answer": "string — 解答（核心观点/方案）",
  "full_text": "string — 完整的结构化表达文本",
  "word_count": "int — 实际字数"
}
```

## 📋 执行步骤

1. **分析主题** — 理解 `topic` 的核心观点，明确要传达的"答案"（A）是什么
2. **构建情景（S）** — 从受众熟悉且认同的背景事实切入，建立共鸣和代入感
3. **引入冲突（C）** — 揭示现实与期望之间的矛盾、挑战或痛点，制造张力
4. **提出疑问（Q）** — 从受众视角提出他们最关心的问题，自然衔接冲突
5. **给出回答（A）** — 清晰、有力地给出解决方案或核心观点，作为全文的落点
6. **润色输出** — 根据 `style` 和 `max_length` 调整语言风格和篇幅

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `topic` 过于模糊 | 返回提示：请提供更具体的主题描述 |
| `context` 缺乏关键信息 | 使用通用背景 + 标注 `[需补充具体数据]` |
| 冲突不够尖锐 | 自动生成多个冲突角度供选择 |
| 输出超出 `max_length` | 优先精简情景描述，保留冲突-疑问-回答的完整性 |

## ✅ 自检清单

- [ ] 情景（S）是否是受众普遍认同的事实？
- [ ] 冲突（C）是否制造了足够的张力？
- [ ] 疑问（Q）是否从受众视角出发？
- [ ] 回答（A）是否清晰有力、直击要害？
- [ ] 整体结构是否遵循 S→C→Q→A 的逻辑递进？
- [ ] 语言风格是否匹配目标受众？

## 📖 示例

**输入**: topic="推行OKR目标管理", context="团队季度目标完成率仅40%", audience="管理层", style="persuasive"

**输出**:
- **S（情景）**: 我们团队每个季度都制定了明确的业务目标，大家也在全力以赴地工作。
- **C（冲突）**: 然而过去三个季度，目标完成率持续徘徊在40%左右，大量精力花在了"紧急但不重要"的事务上。
- **Q（疑问）**: 问题出在哪里？是目标设定不合理，还是执行过程缺乏有效追踪？
- **A（回答）**: 核心原因是缺乏结构化的目标管理体系。建议引入OKR框架——通过设定挑战性目标（O）和量化关键结果（KR），配合每周检视机制，确保精力聚焦于最高价值的事务。


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
| 2026-05-09 | 1.0.0 | 初始版本，从 Framework_SCQA 转化 |

---
**相关笔记**：[[DIKW 知识金字塔]] [[STAR 结构化表达]] 


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


## 🔄 IF/T

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
