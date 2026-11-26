---
name: uskill-cognition-cognitive-mbti-personality-analysis
description: "让cognitive mbti personality analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-mbti-personality-analysis.md"
  original_id: "SKL-5061"
  version: "3.0.0"
  trust: untrusted
---

# cognitive mbti personality analysis

# Apply MBTI Personality Type Analysis

## 🎯 目标
> 运用 MBTI（Myers-Briggs Type Indicator）四维八极性格分析框架，帮助用户理解自身性格偏好、优化沟通方式、改善团队协作，并提供针对性的个人发展建议。强调务实应用，避免刻板贴标签。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `context` | string | ✅ | 分析场景描述，如"我经常在会议中沉默但事后发长文表达"、"团队协作冲突"等 |
| `analysis_mode` | enum | ✅ | 分析模式：`self_discovery`（自我认知）/ `team_dynamics`（团队互动）/ `communication`（沟通优化）/ `career`（职业匹配） |
| `known_type` | string | ❌ | 已知的 MBTI 类型，如 "INTJ"、"ENFP"，若有则直接基于该类型分析 |
| `interaction_parties` | array | ❌ | 涉及的其他人及其类型（团队模式），如 [{"role": "领导", "type": "ESTJ"}] |
| `include_limitations` | boolean | ❌ | 是否包含框架局限性说明，默认 `true` |

## 📤 输出

```json
{
  "type_profile": {
    "four_dimensions": {
      "energy": {
        "preference": "E/I — 外向/内向",
        "indicators": ["string — 从输入中识别的偏好信号"],
        "explanation": "string — 该维度的具体表现说明"
      },
      "information": {
        "preference": "S/N — 感觉/直觉",
        "indicators": ["string"],
        "explanation": "string"
      },
      "decision": {
        "preference": "T/F — 思维/情感",
        "indicators": ["string"],
        "explanation": "string"
      },
      "lifestyle": {
        "preference": "J/P — 判断/知觉",
        "indicators": ["string"],
        "explanation": "string"
      }
    },
    "likely_type": "string — 推断的 MBTI 类型（如 INTJ）",
    "type_nickname": "string — 类型昵称（如 建筑师）",
    "confidence": "string — 推断置信度：high/medium/low"
  },
  "insights": {
    "strengths": ["string — 该类型的核心优势"],
    "blind_spots": ["string — 容易忽视的盲区"],
    "stress_triggers": ["string — 常见的压力来源"],
    "growth_areas": ["string — 可发展的方向"]
  },
  "scenario_advice": {
    "communication_tips": ["string — 针对该类型的沟通建议"],
    "collaboration_tips": ["string — 协作建议"],
    "energy_management": "string — 精力管理建议"
  },
  "framework_caveats": {
    "limitations": ["string — MBTI 框架的局限性说明"],
    "better_alternatives": "string — 大五人格等更严谨的替代方案建议"
  }
}
```

## 📋 执行步骤

1. **信号采集** — 从输入的 `context` 中提取与四维度相关的行为信号：
   - **E/I**：发言频率、社交偏好、能量来源（独处 vs 互动）
   - **S/N**：关注细节 vs 抽象概念、偏好具体数据 vs 未来可能性
   - **T/F**：决策依据（逻辑分析 vs 价值感受）、表达风格
   - **J/P**：计划偏好、截止日期态度、灵活性需求

2. **类型推断** — 根据信号强度判断每个维度的偏好方向：
   - 若提供 `known_type`，直接验证并解释
   - 若需推断，逐维度给出判断依据和置信度
   - 信号不足的维度标注为"倾向不明显"

3. **深度画像** — 基于确定的类型，生成：
   - 核心优势（该类型的典型长处）
   - 盲区（该类型容易忽略的方面）
   - 压力触发因素与应对

4. **场景化建议** — 根据 `analysis_mode` 输出针对性建议：
   - **self_discovery**：自我认知深化，如何发挥优势
   - **team_dynamics**：与 `interaction_parties` 中各类型的互动模式和潜在冲突点
   - **communication**：根据类型调整沟通风格的实操建议
   - **career**：适合的工作环境、角色类型、需避开的场景

5. **框架局限性说明** — 主动提醒：
   - MBTI 是自我认知的起点，不是终点
   - 人格是连续谱，不是非此即彼的二分法
   - 同一类型内部差异可能很大
   - 大五人格（OCEAN）在学术界认可度更高，可作为进阶工具

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 输入信息过少，无法推断类型 | 列出每个维度的两种可能，给出探索性问题帮助用户自我判断 |
| 用户对推断结果不认同 | 尊重用户自判，解释推断依据，建议用户以自身感受为准 |
| 用户将 MBTI 等同于星座 | 引导区别：MBTI 基于行为偏好观察，非天定命运；强调实用价值在于"认知起点"而非"标签终点" |
| 团队模式中缺少他人类型信息 | 提供通用的类型间互动矩阵，覆盖主要可能类型 |
| 试图用 MBTI 做重大决策（如辞退） | 明确警告：MBTI 不适合作为人事决策依据，仅用于自我认知和沟通改善 |

## ✅ 自检清单

- [ ] 四个维度均有分析，未遗漏
- [ ] 推断依据来自输入的具体行为信号，非臆测
- [ ] 如推断类型，标注了置信度
- [ ] 建议具体可操作，非泛泛的类型描述
- [ ] 主动包含框架局限性说明，避免过度依赖
- [ ] 建议用户以自身真实感受为最终判断依据
- [ ] 团队场景下分析了各方类型间的互动模式
- [ ] 未使用 MBTI 做任何歧视性或决定性判断


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
| 2026-

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
