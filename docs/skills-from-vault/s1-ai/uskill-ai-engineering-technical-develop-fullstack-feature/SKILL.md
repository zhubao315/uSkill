---
name: uskill-ai-engineering-technical-develop-fullstack-feature
description: "让technical develop fullstack feature变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-develop-fullstack-feature.md"
  original_id: "SKL-6870"
  version: "3.0.0"
  trust: untrusted
---

# technical develop fullstack feature

# Full-Stack Feature Development

## 🎯 目标
> 以 TDD 为核心、AI 赋能的端到端功能开发流水线，将用户故事转化为通过 CI/CD 验证的完整 PR，开发周期缩短 60%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `user_story` | string | ✅ | 用户故事或 PRD 需求描述 |
| `tech_stack` | object | ✅ | `{frontend: "string", backend: "string", db: "string"}` |
| `design_mockup` | string | ❌ | UI/UX 设计稿描述或链接 |
| `existing_codebase` | string | ❌ | 现有代码库上下文（架构、编码规范） |
| `coverage_target` | number | ❌ | 测试覆盖率目标，默认 90 |

## 📤 输出

```json
{
  "task_breakdown": {
    "frontend_tasks": [{"task": "string", "complexity": "high | mid | low", "estimated_hours": "number"}],
    "backend_tasks": [{"task": "string", "complexity": "high | mid | low", "estimated_hours": "number"}],
    "api_contract": [{"method": "string", "path": "string", "request": "object", "response": "object", "status_codes": ["int"]}]
  },
  "test_cases": {
    "unit_tests": [{"name": "string", "given": "string", "when": "string", "then": "string", "type": "happy | boundary | error"}],
    "integration_tests": [{"name": "string", "scenario": "string", "expected": "string"}],
    "coverage_pct": "number"
  },
  "implementation": {
    "backend_code": "string — 关键代码摘要",
    "frontend_code": "string — 关键代码摘要",
    "database_changes": "string — DDL/Migration"
  },
  "code_review": {
    "bugs": ["string"],
    "performance_issues": ["string"],
    "security_issues": ["string"],
    "readability_score": "number",
    "suggestions": ["string"]
  },
  "ci_cd": {
    "pipeline_status": "pass | fail",
    "test_results": {"passed": "int", "failed": "int", "skipped": "int"},
    "quality_gates": [{"gate": "string", "status": "pass | fail"}]
  },
  "monitoring": {
    "key_metrics": ["string"],
    "alert_rules": ["string"],
    "rollback_plan": "string"
  }
}
```

## 📋 执行步骤

1. **任务分解** — 阅读 `user_story`，用 AI 将其分解为前后端技术任务清单，定义 RESTful API 接口（路径/方法/请求体/响应），绘制组件交互图
2. **编写失败测试** — 根据 API 定义和业务逻辑编写后端测试（正常/边界/异常），根据 UI 设计编写前端组件测试，所有测试初始状态为失败（红色）
3. **AI 辅助编码** — 使用 AI 生成后端代码（控制器/服务/数据访问层）和前端代码（组件/交互逻辑），持续运行测试直到全部通过（绿色）
4. **代码审查** — 自我审查 + AI 审查（检查潜在 Bug、性能、安全、可读性），根据审查建议重构优化，消除所有 Linter 警告
5. **CI/CD 部署** — 推送到特性分支，创建 PR，触发 CI/CD 流水线（测试/质量扫描/构建），获得 PR 批准后合并并自动部署
6. **生产验证** — 监控关键指标（响应时间/错误率），检查应用日志，与产品经理验证业务目标达成

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `user_story` 需求不清晰 | 返回 `ERROR_VAGUE_STORY` + 待澄清问题列表 |
| 测试持续失败 | 进入调试循环：分析失败 → 定位根因 → 修复 → 重跑，最多 3 轮 |
| CI/CD 流水线失败 | 分析失败日志 → 修复 → 重新触发，标记 `CI_PIPELINE_BLOCKED` |
| 代码审查发现安全漏洞 | 标记 `SECURITY_ALERT`，强制修复后方可继续 |

## ✅ 自检清单

- [ ] 每个技术任务可在一个工作日内完成
- [ ] API 接口定义无歧义
- [ ] 测试覆盖率 ≥ 90%
- [ ] 所有 CI/CD 质量门通过
- [ ] PR 描述清晰且关联任务卡片
- [ ] 生产环境关键指标正常


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-04 转化 |

---
**相关笔记**：[[LLM摄影提示词工程]] [[云原生容器化部署]] 


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

| Agent 常见借口 | 反驳 |
|--------------|-----

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
