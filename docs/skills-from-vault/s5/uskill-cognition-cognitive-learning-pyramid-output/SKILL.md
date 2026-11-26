---
name: uskill-cognition-cognitive-learning-pyramid-output
description: "让cognitive learning pyramid output变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-learning-pyramid-output.md"
  original_id: "SKL-5142"
  version: "3.0.0"
  trust: untrusted
---

# cognitive learning pyramid output

# Learning Pyramid Output Method

## 🎯 目标
> 基于学习金字塔理论（留存率：听讲5%→阅读10%→讨论50%→实践75%→教授他人90%），通过"以教代学"的输出驱动方式，将被动学习转化为主动理解，用费曼技巧四步法验证和巩固知识掌握程度。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `concept` | string | ✅ | 要学习/验证理解的概念名称 |
| `source_material` | string | ❌ | 原始学习材料（书籍、课程、文档路径） |
| `current_understanding` | string | ❌ | 当前对概念的理解描述（用于验证） |
| `target_audience` | enum | ❌ | `child` / `beginner` / `peer` — 解释的目标受众，默认 `child`（8岁孩子） |
| `output_format` | enum | ❌ | `spoken` / `written` / `analogy` — 输出形式，默认 `written` |
| `domain` | string | ❌ | 概念所属领域（用于生成类比时选择跨域参照） |

## 📤 输出

```json
{
  "concept": "string — 概念名称",
  "feynman_explanation": "string — 用简单语言的解释",
  "analogy": "string — 生活化类比",
  "stuck_points": ["string — 卡壳点列表（知识盲区）"],
  "knowledge_level": "solid | partial | pseudo — 真知/半知/伪知",
  "refinement_suggestions": ["string — 需要回头学习的具体点"],
  "verification_questions": ["string — 验证理解的追问"]
}
```

## 📋 执行步骤

### Phase 1：选择与初解释
1. **明确目标概念** — 在白纸顶端写下概念名称，标注所属领域
2. **写出当前理解** — 不查资料，用自己的话写下对这个概念的理解
3. **标记专业术语** — 圈出解释中出现的所有专业术语/行话

### Phase 2：费曼四步法执行
4. **假装教给孩子** — 将解释重写为面向8岁孩子的版本：
   - 禁止使用任何圈出的专业术语
   - 使用"就像..."的类比结构
   - 每句话只包含一个信息点
5. **定位卡壳点** — 标记所有：
   - 写到一半停下来想的地方
   - 不得不用"某种意义上"等模糊词的地方
   - 自己觉得解释不够清楚的地方
6. **回归原始材料** — 针对每个卡壳点，回到 source_material 重新学习该部分

### Phase 3：简化与类比
7. **精炼解释** — 将解释压缩到最简洁版本，目标：3句话以内说清核心
8. **生成类比** — 从目标受众熟悉的领域选择类比：
   - `child`：玩具、游戏、日常生活
   - `beginner`：该领域的基础概念
   - `peer`：同领域的相邻概念
9. **写出最终版** — 产出一个任何人听了都能复述核心要点的版本

### Phase 4：验证与分级
10. **自评知识等级**：
    - 🟢 **solid（真知）**：能用简单语言完整回答"是什么/为什么/怎么运作"
    - 🟡 **partial（半知）**：能回答部分，某些环节模糊
    - 🔴 **pseudo（伪知）**：只知道名称，回答不了实质问题
11. **生成追问** — 写出3个可以进一步验证理解深度的追问
12. **制定补学计划** — 对卡壳点和伪知部分，制定具体的学习行动

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 概念过于抽象无法具象化 | 使用"它的作用/效果是什么"替代"它是什么" |
| 领域过于专业找不到跨域类比 | 先用同领域的简单概念做阶梯类比 |
| 卡壳点太多（>5个） | 该概念需要系统性重学，暂停费曼练习，回归课程/教材 |
| 解释出来仍然很复杂 | 拆分为子概念，每个子概念单独做费曼练习 |
| 目标受众表示听不懂 | 记录具体听不懂的点，这些是最有价值的反馈 |

## ✅ 自检清单

- [ ] 解释中不包含任何未解释的专业术语
- [ ] 有一个生活化的类比
- [ ] 卡壳点已全部标记并有补学计划
- [ ] 知识等级已诚实自评
- [ ] 解释能被目标受众理解（可用真人验证）


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
---
**相关笔记**：[[金线评估]] [[SCQA]] 


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
 Read     确认     任务      检查    Es

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
