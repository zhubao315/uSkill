---
name: uskill-agent-meta-pain-reflection-growth-cycle
description: "让meta pain reflection growth cycle变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-pain-reflection-growth-cycle.md"
  original_id: "SKL-5078"
  version: "3.0.0"
  trust: untrusted
---

# meta pain reflection growth cycle

# Apply Pain-Reflection Growth Cycle

## 🎯 目标
> 运用"痛苦+反思=进步"的达利欧公式，将任何痛苦/失败/不适经历转化为可复用的个人原则，实现从"受苦"到"成长"的认知跃迁。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `pain_event` | string | ✅ | 痛苦/失败/不适事件的描述 |
| `emotions` | string[] | ❌ | 当时的情绪感受，如 `["焦虑", "自责", "愤怒"]` |
| `domain` | enum | `investment` / `career` / `relationship` / `health` / `learning` / `general` | 事件所属领域，默认 `general` |
| `depth` | enum | `quick` / `standard` / `deep`，默认 `standard` | 反思深度：`quick`=仅提炼原则；`standard`=含根因分析；`deep`=含关联过往经历 |
| `existing_principles` | string[] | ❌ | 已有的相关原则，用于避免重复或冲突 |

## 📤 输出

```json
{
  "event_analysis": {
    "what_happened": "string — 客观描述事件经过",
    "what_i_felt": "string — 情绪识别与命名",
    "automatic_reaction": "string — 我的本能反应是什么"
  },
  "root_cause": {
    "surface_cause": "string — 直接原因",
    "deep_cause": "string — 根本原因（能力/认知/环境/系统）",
    "cause_category": "string — 根因分类：skill_gap / cognitive_bias / system_flaw / environment_factor",
    "five_whys": ["string — 5个为什么的推理链"]
  },
  "principle_extracted": {
    "principle": "string — 提炼的原则（格式：当X情况发生时，我应该Y）",
    "rationale": "string — 为什么这条原则能防止类似痛苦",
    "confidence": "float — 0-1，对这条原则的信心指数",
    "test_scenario": "string — 下次可以用什么场景来验证这条原则"
  },
  "action_plan": {
    "immediate": "string — 今天就可以做的一件事",
    "this_week": "string — 本周要做的事",
    "ongoing": "string — 持续的习惯或检查机制"
  },
  "connections": {
    "related_past_events": "string — 是否有类似的过往经历",
    "related_principles": "string — 与已有原则的关系（补充/冲突/替代）"
  }
}
```

## 📋 执行步骤

1. **事件还原** — 客观描述痛苦事件的经过，区分"事实"和"我的解读"。事实是"项目延期3天"，解读是"我能力不行"。先记录事实，解读放到后面分析。
2. **情绪命名** — 识别并命名当时的情绪（焦虑、愤怒、羞耻、恐惧等）。情绪命名本身就有降低情绪强度的效果（心理学中的"affect labeling"效应）。
3. **本能反应记录** — 记录我的第一反应是什么（逃避、自责、怪罪他人、过度补偿等）。本能反应往往指向根因。
4. **根因分析** — 用"5个为什么"法追问根因：
   - 第1个为什么：直接原因（如"需求变更导致延期"）
   - 第2个为什么：为什么需求会变更？（如"需求评审不充分"）
   - 第3个为什么：为什么评审不充分？（如"没有标准化的评审流程"）
   - 第4个为什么：为什么没有流程？（如"觉得流程太重，想快速迭代"）
   - 第5个为什么：为什么会这样觉得？（如"对'敏捷'的误解——以为敏捷=不要流程"）
5. **原则提炼** — 把根因分析的结果转化为一条可复用的原则。原则格式："当X情况发生时，我应该Y，因为Z"。原则要足够具体，下次遇到类似情境可以直接调用。
6. **行动计划** — 制定三层行动计划：立即（今天）、短期（本周）、持续（习惯）。
7. **关联检查** — 检查新提炼的原则是否与已有原则冲突或重复。如果有冲突，需要明确哪个原则优先级更高。

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 事件描述过于模糊 | 要求补充具体细节：时间、地点、人物、结果 |
| 情绪无法命名 | 提供情绪轮盘参考，帮助用户精确定位 |
| 根因分析停在表面 | 强制要求至少追问到第3个"为什么" |
| 提炼的原则太泛（如"下次注意"） | 要求具体化：什么情况下注意？注意什么？怎么注意？ |
| 发现与已有原则冲突 | 标注冲突，引导用户决定哪个原则优先 |

## ✅ 自检清单

- [ ] 事件描述区分了"事实"和"解读"
- [ ] 情绪被准确命名，而非笼统的"不开心"
- [ ] 根因分析至少追问了3层"为什么"
- [ ] 提炼的原则格式为"当X时，我应该Y"
- [ ] 行动计划包含"今天就能做"的一件事
- [ ] 检查了与已有原则的冲突/重复


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
| 2026-05-09 | 1.0.0 | 初始版本，从《原则》痛苦反思公式转化 |

---
**相关笔记**：[[人生操作系统进化-Schema-v2]] [[提示词全生命周期管理]] 


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

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
