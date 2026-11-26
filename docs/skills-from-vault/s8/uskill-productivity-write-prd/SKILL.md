---
name: uskill-productivity-write-prd
description: "让productivity write prd变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-write-prd.md"
  original_id: "SKL-6912"
  version: "3.0.0"
  trust: untrusted
---

# productivity write prd

# Write Product Requirements Document

## 🎯 目标
> 将产品创意、用户洞察和功能优先级列表转化为结构清晰、可执行的产品需求文档（PRD），确保开发团队对需求有统一、无歧义的理解。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `product_name` | string | ✅ | 产品名称 |
| `problem_statement` | string | ✅ | 核心问题/价值主张（1-3句话） |
| `user_personas` | array | ✅ | 用户画像列表 `[{name, pain_points, scenarios}]` |
| `feature_list` | array | ✅ | 按优先级排序的功能列表 `[{feature, priority, rice_score}]` |
| `target_market` | string | ❌ | 目标市场/行业描述 |
| `team_context` | object | ❌ | `{ tech_stack, sprint_weeks, team_size }` |
| `non_functional` | object | ❌ | `{ performance, scalability, security }` — 非功能性需求 |
| `prd_scope` | enum | ❌ | `full`（完整PRD）/ `feature`（单功能PRD），默认 `full` |

## 📤 输出

```json
{
  "prd": {
    "title": "string — PRD标题",
    "background": "string — 产品背景与问题定义",
    "objectives": ["string — 产品目标（SMART原则）"],
    "user_stories": [
      {
        "id": "US-{NNN}",
        "story": "string — As a [角色], I want [功能], so that [价值]",
        "acceptance_criteria": ["string — 可测试的验收标准"],
        "priority": "P0 | P1 | P2",
        "estimated_effort": "string"
      }
    ],
    "non_functional_requirements": {
      "performance": "string",
      "scalability": "string",
      "security": "string"
    },
    "success_metrics": [
      { "metric": "string", "target": "string", "measurement": "string" }
    ],
    "risks_and_dependencies": [
      { "risk": "string", "mitigation": "string" }
    ],
    "timeline": "string — 里程碑时间线"
  }
}
```

## 📋 执行步骤

1. **梳理背景与目标** — 汇总 `problem_statement`、`user_personas`、`target_market`，撰写 PRD 的背景章节（为什么做）和产品目标（做成什么样，用 SMART 原则约束）
2. **转化用户故事** — 遍历 `feature_list`，使用 AI 提示词将每个功能转化为标准用户故事格式（As a... I want... so that...），并为每个故事编写 ≥3 条可测试的验收标准（Acceptance Criteria）
3. **定义非功能性需求** — 根据 `team_context` 和 `non_functional` 输入，补充性能、可扩展性、安全性、可用性等非功能性约束；若输入缺失，标注 `TBD` 并提示评审时补充
4. **编制成功指标** — 为每个主要功能定义 1-2 个可量化的成功指标（如激活率、使用率、留存率），明确测量方式和目标值
5. **风险识别与排期** — 列出技术风险、依赖项和外部约束，制定里程碑时间线（MVP → Beta → GA）
6. **校验与输出** — 执行自检清单，确保所有用户故事有验收标准、目标可量化、无遗漏模块，输出最终 PRD

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `problem_statement` 过于模糊（< 10字） | 返回 `ERROR_VAGUE_PROBLEM` + 提供 3 个澄清问题模板 |
| `feature_list` 为空 | 返回 `ERROR_NO_FEATURES` + 建议先执行产品发现流程（参考 SKL-011） |
| `user_personas` 缺失 | 使用 AI 生成假设性画像，标记 `HYPOTHETICAL` 待验证 |
| 功能列表 > 15 项 | 提示拆分为多期交付，先输出 P0 级功能的 PRD |
| 验收标准不可测试（含"好""快"等模糊词） | 自动改写为可量化标准 + 标注 `AUTO_REWRITTEN` |

## ✅ 自检清单

- [ ] PRD 包含背景、目标、用户故事、验收标准、非功能性需求、成功指标、风险、排期共 8 个模块
- [ ] 每个用户故事遵循 "As a... I want... so that..." 格式
- [ ] 每个用户故事有 ≥3 条可测试的验收标准（含明确的量化判定条件）
- [ ] 产品目标符合 SMART 原则（具体、可衡量、可实现、相关、有时限）
- [ ] 成功指标均可量化且有明确的测量方式
- [ ] 所有 `TBD` 标记项 ≤ 3 个，且均标注了评审时需补充


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
| 2026-05-09 | 1.0.0 | 初始版本，从 SOP-05 转化，聚焦 PRD 撰写阶段 |

---
**相关笔记**：[[投研备忘撰写]] [[个人效率分析引擎]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定制。

---

## 🚫 Anti-Rationalization Table `[v3新增]`

> 来源：addyosmani/agent-skills 的核心创新

| Agent 常见借口

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
