---
name: uskill-ai-engineering-technical-rpvi-prompt-engineering
description: "让technical rpvi prompt engineering变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-rpvi-prompt-engineering.md"
  original_id: "SKL-6861"
  version: "3.0.0"
  trust: untrusted
---

# technical rpvi prompt engineering

⚙️ AI-Co 运行配置块
触发场景: 用户说'提示词工程'、'RPVI'、'AI编程'、'代码生成'
复用率预估: 高
一键调用: Research压缩→Plan规划→Implement编码→Verify验证
输入Schema: phase(enum: research/plan/implement/verify), project_context(object), task_description(string)
输出Schema: prompt(phase, system_prompt, user_prompt, expected_output_format, anti_patterns)
AI可执行度: 100%

# RPVI Prompt Engineering for Large-Scale Code

## 🎯 目标
> 为 RPVI（Research-Plan-Verify-Implement）工作流的每个阶段提供工业级提示词模板，解决 AI 在 5000+ 行代码库中"智商断崖式下降"的上下文工程问题。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `phase` | enum | ✅ | `research` / `plan` / `implement` / `verify` |
| `project_context` | object | ✅ | `{name, line_count, modules, language, problem}` |
| `task_description` | string | ✅ | 功能需求或 Bug 描述 |
| `existing_context` | string | ❌ | 已有的 AI_CONTEXT.md 内容（复用时传入） |
| `branch_name` | string | ❌ | Implement 阶段的分支名 |
| `test_failure_info` | string | ❌ | Verify 阶段的测试失败信息 |

## 📤 输出

```json
{
  "prompt": {
    "phase": "string — research | plan | implement | verify",
    "system_prompt": "string — 完整的系统提示词",
    "user_prompt": "string — 完整的用户提示词",
    "expected_output_format": "string — 期望输出格式说明",
    "anti_patterns": ["string — 该阶段常见的提示词反模式"]
  },
  "context_engineering": {
    "compression_strategy": "string — 上下文压缩策略建议",
    "injection_order": ["string — 上下文注入顺序"],
    "token_budget": "number — 建议的 token 预算"
  }
}
```

## 📋 执行步骤

### 阶段一：Research — 代码压缩与知识萃取

1. **选择压缩策略** — 根据项目类型（Web/CLI/库/微服务）选择 5 层压缩策略：架构层（Mermaid 图）→ 接口层（API 签名）→ 逻辑层（伪代码）→ 依赖层（第三方库）→ 问题层（已知 Bug/技术债）
2. **生成 Research 提示词** — 使用 R01 模板，填入项目元数据（名称、行数、模块、当前问题），输出 <500 行的 `AI_CONTEXT.md`
3. **验证压缩质量** — 确认压缩后上下文 AI 可直接理解，无关键信息遗漏，压缩比 >10x

### 阶段二：Plan — AI 生成 + 人工审查

4. **注入上下文** — 将 Research 阶段生成的 `AI_CONTEXT.md` 作为系统上下文注入
5. **生成 Plan 提示词** — 使用 P01 模板，要求 AI 输出分阶段实施计划（3-5 阶段）、技术决策、风险评估（≥3 个）和备选方案
6. **人工审查强化** — 在提示词中追加约束："你必须列出至少 3 个技术风险，每个风险必须有缓解方案；你必须提供至少 1 个 Plan B 备选方案"

### 阶段三：Implement — Git Worktree 并行编码

7. **分支策略设计** — 为每个并行分支定义不同的实现策略（速度优先/性能优先/可维护性优先）
8. **生成 Implement 提示词** — 使用 V01 模板，注入 AI 知识库 + 实施计划 + 当前阶段任务 + 约束条件（代码风格/测试要求/性能要求）
9. **强制测试驱动** — 在提示词中明确要求："一次输出完整文件，包含核心代码 + 测试代码 + 文档更新，不要分段"

### 阶段四：Verify — Bug 定位与修复循环

10. **生成 Verify 提示词** — 使用 I01 模板，注入测试失败信息 + 相关代码上下文
11. **要求三层分析** — 在提示词中要求 AI 输出：(a) 根因分析（直接原因 + 深层设计问题 + 为什么测试没发现）(b) 修复方案（具体代码修改 + 影响面评估）(c) 预防措施
12. **迭代修复** — 将修复后的代码重新运行测试，循环直到所有测试通过且覆盖率达标

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 提示词输出截断 | 追加"请继续输出，从上次中断处开始"，或拆分为更小的任务单元 |
| AI 生成的计划过于乐观 | 在提示词中强制要求"列出最可能导致失败的 3 个原因" |
| 上下文超出 token 限制 | 使用分段注入策略：先注入架构层，再按需注入逻辑层 |
| AI 输出格式不规范 | 在提示词末尾追加严格的 JSON/Markdown 格式模板 |
| 并行方案差异太小 | 在 Implement 提示词中明确差异化约束（如"方案 A 优先使用函数式编程"） |

## ✅ 自检清单

- [ ] 每个阶段的提示词是否包含明确的角色定义？
- [ ] Research 阶段的上下文压缩后是否 < 500 行？
- [ ] Plan 阶段是否强制要求 ≥ 3 个风险点和备选方案？
- [ ] Implement 阶段是否要求一次输出完整文件（含测试）？
- [ ] Verify 阶段是否要求三层分析（根因/修复/预防）？
- [ ] 所有提示词是否指定了期望的输出格式？
- [ ] 是否记录了每个阶段的 token 消耗和压缩比？

## 🤖 AI 提示词模板

**R01（Research — 代码压缩）**: `你是一位资深系统架构师。项目：{name}，{line_count}行，模块：{modules}，问题：{problem}。请生成 <500 行的 AI 知识库，包含：1. Mermaid 架构图 2. 核心 API 签名 3. 业务逻辑伪代码 4. 已知 Bug/技术债 5. 开发规范。`

**P01（Plan — 实施计划）**: `你是一位技术负责人。基于以下知识库：{AI_CONTEXT.md}。需求：{task_description}。请生成实施计划，包含：1. 3-5 阶段任务分解 2. 技术选型及理由 3. ≥3 个风险+缓解方案 4. Plan B 备选方案 5. 验收标准。`

**V01（Implement — AI 编码）**: `你是全栈工程师，在 {branch_name} 分支实现功能。上下文：{AI_CONTEXT.md + Plan}。当前任务：{stage_task}。约束：{code_style, test_requirement, perf_requirement}。请一次输出完整代码+测试+文档，不要分段。`

**I01（Verify — Bug 定位）**: `你是调试专家。测试失败：{test_failure_info}。相关代码：{code_context}。请分析：1. 根因（直接原因+深层问题+为何未发现）2. 修复（具体代码修改+影响面）3. 预防（避免复发的措施）。`


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
- [ ] 方案考虑了实际约

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
