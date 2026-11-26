# AI-Driven Strategic Learning Plan

## 🎯 目标
> 建立以战略目标为导向、AI 全面赋能的 4A 闭环学习系统，高效获取、深度内化并应用新知识，将新领域入门到产出时间缩短 50%，实现知识复利。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `learning_goal` | string | ✅ | SMART 学习目标，如"3 个月内掌握 Rust 并独立完成一个 CLI 工具" |
| `current_level` | enum | ✅ | `beginner` / `intermediate` / `advanced` — 当前知识水平 |
| `time_budget_hours_weekly` | int | ✅ | 每周可投入学习时间（小时） |
| `duration_weeks` | int | ❌ | 学习周期（周），默认 4 |
| `preferred_format` | enum | ❌ | `reading` / `video` / `hands_on` / `mixed`，默认 `mixed` |
| `output_type` | enum | ❌ | `blog` / `side_project` / `presentation` / `sop` — 知识内化产出形式，默认 `blog` |
| `context` | object | ❌ | `{related_okr: "string", existing_skills: ["string"], motivation: "string"}` — 学习背景 |

## 📤 输出

```json
{
  "learning_plan": {
    "smart_goal": "string — 结构化 SMART 目标",
    "alignment_with_okr": "string — 与个人 OKR 的关联说明",
    "weekly_schedule": [
      {
        "week": "int",
        "theme": "string",
        "topics": ["string"],
        "theory_hours": "number",
        "practice_hours": "number",
        "milestone": "string",
        "deliverable": "string"
      }
    ],
    "theory_practice_ratio": "string — 如 '6:4'"
  },
  "resource_collection": {
    "essential_books": [
      {"title": "string", "author": "string", "reason": "string", "priority": "must_read | recommended"}
    ],
    "papers_reports": [
      {"title": "string", "source": "string", "reason": "string"}
    ],
    "courses": [
      {"name": "string", "platform": "string", "duration": "string", "reason": "string"}
    ],
    "open_source_projects": [
      {"name": "string", "url": "string", "difficulty": "easy | medium | hard", "reason": "string"}
    ],
    "minimal_knowledge_set": "string — 最小知识集合摘要"
  },
  "active_learning": {
    "socratic_questions": [
      {"topic": "string", "questions": ["string — 启发性问题"]}
    ],
    "concept_map": "string — Mermaid 概念关系图",
    "misconceptions_to_watch": ["string — 常见误区"]
  },
  "assimilation_project": {
    "project_name": "string",
    "description": "string",
    "core_features": ["string"],
    "tech_stack": ["string"],
    "difficulty": "easy | medium | hard",
    "estimated_hours": "int",
    "learning_outcomes": ["string"]
  },
  "knowledge_output": {
    "type": "blog | side_project | presentation | sop",
    "outline": ["string — 文章/分享大纲"],
    "target_audience": "string",
    "key_insights_to_convey": ["string"]
  },
  "assessment": {
    "quiz": {
      "multiple_choice": [{"question": "string", "options": ["string"], "answer": "string", "explanation": "string"}],
      "short_answer": [{"question": "string", "reference_answer": "string"}],
      "scenario": [{"scenario": "string", "expected_approach": "string"}]
    },
    "pass_threshold_pct": 90,
    "weakness_analysis_template": "string"
  },
  "retrospective": {
    "sprint_review_questions": ["string"],
    "adjustment_actions": ["string"],
    "next_sprint_suggestions": ["string"]
  }
}
```

## 📋 执行步骤

### Phase 1: 对齐目标 (Align)
1. **明确学习意图** — 分析 `learning_goal` 与 `context.related_okr` 的关联，确保学习是战略投资而非随机探索，输出 SMART 目标结构化文档
2. **AI 辅助课程设计** — 根据 SMART 目标和 `current_level`，生成个性化学习大纲，包含每周主题、理论/实践比例、关键里程碑

### Phase 2: 获取知识 (Acquire)
3. **AI 辅助资源策展** — 为每个学习模块推荐"最小知识集合"：2 本圣经级书籍、3 篇核心论文、1-2 门在线课程、2-3 个开源项目
4. **苏格拉底式深度学习** — 对每个核心概念生成 5 个启发性问题，通过追问和诘难深化理解，而非被动接收
5. **概念图谱构建** — 生成 Mermaid 格式的概念关系图，标注知识节点间的依赖和联系

### Phase 3: 内化与应用 (Assimilate & Apply)
6. **结构化笔记沉淀** — 将新知识重构为原子化笔记，建立双向链接，链入 Obsidian 知识网络
7. **实践项目驱动** — 根据学习内容构思 1 个微型 Side Project，将理论转化为可交付的代码/产品
8. **费曼学习法输出** — 按 `output_type` 生成知识产出大纲（技术博客/项目文档/内部分享/SOP），确保能向他人清晰解释所学

### Phase 4: 评估与迭代 (Assess & Adjust)
9. **AI 生成自测卷** — 生成包含选择题、简答题、场景应用题的自测卷，含详细答案和解析
10. **复盘与调整** — 分析学习效率、障碍和成功经验，输出 Sprint 回顾报告和下一阶段调整建议

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `learning_goal` 过于模糊（如"学 AI"） | 返回 `ERROR_GOAL_TOO_VAGUE` + SMART 改写建议 |
| `time_budget_hours_weekly` < 3 | 返回 `WARNING_INSUFFICIENT_TIME` + 精简版学习计划（仅核心 20%） |
| `current_level` 与 `learning_goal` 跨度过大 | 返回 `WARNING_LEVEL_GAP` + 建议分阶段目标 + 前置知识清单 |
| 推荐资源不可获取（付费墙/语言障碍） | 自动替换为免费/中文替代资源 + 标注质量差异 |
| 自测正确率 < 60% | 建议回退到 Acquire 阶段 + 生成针对性补强计划 |
| 学习计划执行偏离 > 30% | 触发计划重排 + 降低当期目标 + 延长周期建议 |

## ✅ 自检清单

- [ ] SMART 目标符合 Specific/Measurable/Achievable/Relevant/Time-bound 五要素
- [ ] 学习目标与个人 OKR 存在明确关联说明
- [ ] 资源策展包含"最小知识集合"（书籍 + 论文 + 课程 + 项目）
- [ ] 每周计划包含理论/实践比例和可交付里程碑
- [ ] 苏格拉底问题覆盖 ≥ 3 个核心概念，每个概念 ≥ 5 个问题
- [ ] 实践项目具备明确的功能点、技术栈和预期学习收获
- [ ] 自测卷正确率阈值设为 90%，含答案和解析
- [ ] 复盘模板包含效率分析、障碍记录和调整建议


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-09 转化 |

---
**相关笔记**：[[SKILLS-CATALOG]] [[uSkill-cognition-贝叶斯决策框架]] 


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


**相关概念**：[[艾宾浩斯遗忘曲线]]

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
