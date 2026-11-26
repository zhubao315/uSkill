---
name: uskill-ai-engineering-technical-rpvi-large-scale-code-dev
description: "让technical rpvi large scale code dev变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-rpvi-large-scale-code-dev.md"
  original_id: "SKL-5004"
  version: "3.0.0"
  trust: untrusted
---

# technical rpvi large scale code dev

# RPVI Large-Scale Code Development

## 🎯 目标
> 解决 AI 在 5000+ 行代码库中"智商断崖式下降"问题，通过 Research-Plan-Verify-Implement 四步工作流实现万行级代码的高效 AI 辅助开发。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `codebase_info` | object | ✅ | `{name: "string", line_count: "int", modules: ["string"], language: "string"}` |
| `task_description` | string | ✅ | 功能需求或 Bug 描述 |
| `parallel_branches` | int | ❌ | 并行方案数，默认 2（范围 1-3） |
| `coverage_target` | number | ❌ | 测试覆盖率目标，默认 80 |

## 📤 输出

```json
{
  "research": {
    "ai_knowledge_base": "string — 压缩后的 AI_CONTEXT.md 内容（<500行）",
    "architecture_summary": "string — Mermaid 架构图",
    "core_apis": ["string — 关键函数/类签名"],
    "known_issues": ["string — 已知 Bug 和技术债"],
    "compression_ratio": "number — 原始行数/压缩行数"
  },
  "plan": {
    "phases": [
      {
        "name": "string",
        "tasks": ["string"],
        "estimated_hours": "number",
        "deliverables": ["string"]
      }
    ],
    "tech_decisions": [{"decision": "string", "options": ["string"], "chosen": "string", "rationale": "string"}],
    "risks": [{"name": "string", "level": "high | mid | low", "mitigation": "string"}],
    "acceptance_criteria": ["string"],
    "plan_b": "string — 备选方案"
  },
  "implementations": [
    {
      "branch": "string",
      "approach": "string — 速度优先 | 性能优先 | 可维护性优先",
      "code_summary": "string",
      "test_results": {"passed": "int", "failed": "int", "coverage_pct": "number"},
      "performance": {"execution_time_ms": "number", "memory_mb": "number"}
    }
  ],
  "verification": {
    "chosen_branch": "string",
    "comparison_report": "string — 方案对比说明",
    "final_test_results": {"passed": "int", "failed": "int", "coverage_pct": "number"},
    "bug_density": "number — Bug/千行",
    "ai_context_efficiency": "number — 原始行数/AI处理行数"
  }
}
```

## 📋 执行步骤

1. **Research — 代码压缩与知识萃取** — 扫描代码库生成架构图和依赖关系，识别核心模块/关键函数/数据流，按 5 层压缩策略（架构层→接口层→逻辑层→依赖层→问题层）生成 <500 行的 `AI_CONTEXT.md` 知识库
2. **Plan — AI 生成 + 人工审查** — AI 基于知识库生成分阶段实施计划（3-5 阶段），人工审查技术可行性、风险识别和资源评估，标记高风险和关键决策点，确保有 Plan B 备选方案
3. **Implement — Git Worktree 并行赛马** — 创建 2-3 个 Git worktree 并行分支，每个分支用不同策略实现（速度优先/性能优先/可维护性优先），每个方案必须有完整测试覆盖
4. **Verify — 自动化测试循环** — 并行运行所有方案测试，记录性能指标（执行时间/内存），评估代码质量，选择最优方案合并到主分支，更新 AI 知识库（什么容易出错）

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 压缩丢失关键信息 | 增加"问题层"标记，保留关键代码片段，调整压缩策略 |
| AI 计划过于乐观 | 人工审查强制要求 ≥3 个风险点，补充悲观场景 |
| 并行方案差异太小 | 在 Implement 步骤前重新定义评估标准 |
| 测试通过但功能不正确 | 增加端到端测试和用户场景测试 |
| 上下文仍然不足 | 提高伪代码比例，使用分段注入策略 |

## ✅ 自检清单

- [ ] AI 知识库 < 500 行且无关键信息遗漏
- [ ] 实施计划覆盖所有需求点
- [ ] 识别 ≥ 3 个关键风险
- [ ] 所有并行方案能通过基础测试
- [ ] 最终方案选择有数据支撑
- [ ] 测试覆盖率 ≥ 80%
- [ ] Bug 密度 < 0.1/千行
- [ ] AI 知识库已更新


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-26-RPVI 转化 |

---
**相关笔记**：[[向量数据库选型实战]] [[SOP-03-云计算专家-容器化部署]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [学习任务] for [知识背景], with [学习目标], leaning toward [学习方法/输出形式]."

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
