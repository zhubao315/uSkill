---
name: uskill-ai-engineering-fullstack-develop-feature
description: "让fullstack develop feature变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-fullstack-develop-feature.md"
  original_id: "SKL-6862"
  version: "3.0.0"
  trust: untrusted
---

# fullstack develop feature

# Full-Stack Feature Development

## 🎯 目标
> 建立以 TDD 为核心、AI 全面赋能的端到端功能交付流水线，将新功能从开发到部署的周期缩短 60%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `user_story` | string | ✅ | 用户故事 / 产品需求描述 |
| `tech_stack` | object | ✅ | 技术栈信息（前端框架、后端语言、数据库） |
| `design_mockup` | string | ❌ | UI/UX 设计稿链接或描述 |
| `existing_codebase` | string | ❌ | 现有代码库上下文（重构场景） |
| `acceptance_criteria` | list | ❌ | 验收标准列表 |
| `priority` | enum | ❌ | `P0` / `P1` / `P2`，默认 `P1` |

## 📤 输出

```json
{
  "task_breakdown": {
    "backend_tasks": [{"task": "string", "complexity": "high|medium|low", "estimated_hours": "float"}],
    "frontend_tasks": [{"task": "string", "complexity": "high|medium|low", "estimated_hours": "float"}],
    "api_spec": [{"method": "string", "path": "string", "request": "object", "response": "object"}]
  },
  "test_cases": {
    "unit_tests": [{"name": "string", "given": "string", "when": "string", "then": "string"}],
    "integration_tests": [{"name": "string", "scenario": "string", "expected": "string"}],
    "edge_cases": ["string"],
    "error_cases": ["string"]
  },
  "implementation": {
    "backend_code": "string — 后端实现代码",
    "frontend_code": "string — 前端实现代码",
    "test_code": "string — 测试代码"
  },
  "code_review": {
    "bugs": [{"issue": "string", "severity": "high|medium|low", "fix": "string"}],
    "performance": [{"issue": "string", "suggestion": "string"}],
    "security": [{"issue": "string", "mitigation": "string"}],
    "readability_score": "float"
  },
  "ci_cd": {
    "pipeline_status": "pass | fail",
    "test_coverage": "float",
    "build_artifact": "string",
    "deploy_target": "string"
  },
  "monitoring": {
    "key_metrics": ["string"],
    "log_queries": ["string"],
    "alert_rules": [{"metric": "string", "threshold": "string"}]
  }
}
```

## 📋 执行步骤

1. **任务分解** — 解析 `user_story`，拆分为前后端技术任务清单（每个任务 ≤ 1 个工作日），定义 RESTful API 接口（含请求/响应结构），绘制组件交互图
2. **编写失败测试** — 根据 API 定义和验收标准，编写后端单元/集成测试和前端组件测试，覆盖正常路径、≥ 3 个边界条件、≥ 2 个异常场景
3. **AI 辅助编码** — 使用 Copilot/AI 大模型生成后端代码（控制器/服务/数据访问层）和前端组件代码，持续运行测试直至全部通过
4. **代码审查** — 自我审查 + AI 审查（检查潜在 Bug / 性能问题 / 安全漏洞 / 可读性），修复所有高优先级问题
5. **CI/CD 流水线** — 推送特性分支，创建 PR，触发自动化测试 + 代码质量扫描 + 构建，等待审批并合并
6. **生产监控验证** — 部署后监控关键指标（响应时间 / 错误率），与产品经理确认业务目标达成

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `user_story` 描述模糊 | 返回澄清问题清单 |
| 测试覆盖率 < 90% | 标记未覆盖模块，补充测试 |
| CI/CD 流水线失败 | 解析失败日志，自动定位问题代码 |
| PR 审查超 24h 未响应 | 通知相关 reviewer |
| 生产监控异常 | 自动回滚 + 创建热修任务 |

## ✅ 自检清单

- [ ] 每个技术任务 ≤ 1 个工作日
- [ ] API 接口定义清晰无歧义
- [ ] 测试用例覆盖所有验收标准
- [ ] 测试确实因功能未实现而失败（红灯）
- [ ] 所有测试通过（绿灯）
- [ ] 代码遵循项目编码规范
- [ ] Linter / 静态分析无警告
- [ ] AI 审查高优问题已修复
- [ ] CI/CD 流水线 100% 通过
- [ ] 测试覆盖率 ≥ 90%
- [ ] PR 描述清晰，关联任务卡片
- [ ] 生产环境指标正常


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-004 转化 |

---
**相关笔记**：[[LLM摄影提示词工程]] [[缓存架构设计]] 


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

> 来源：addyosmani/

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
