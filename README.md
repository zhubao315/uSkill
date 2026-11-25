<div align="center">

<img src="docs/assets/images/logo.svg" alt="uSkill Logo" width="360">

**uSkill — Agent Skill Engineering Platform**

开放标准 · 可治理运行时 · 证据驱动的持续进化
以驾驭工程为方法论，让 AI 技能：可定义 → 可发现 → 可调用 → 可执行 → 可验证 → 可追溯 → 可治理。

[![CI](https://github.com/zhubao315/uSkill/actions/workflows/ci.yml/badge.svg)](https://github.com/zhubao315/uSkill/actions/workflows/ci.yml)
[![Version](https://img.shields.io/github/v/tag/zhubao315/uSkill?label=version&sort=semver)](https://github.com/zhubao315/uSkill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docs](https://img.shields.io/badge/Docs-Published-00C2CB)](https://zhubao315.github.io/uSkill/)

[快速开始](#快速开始) • [文档](https://zhubao315.github.io/uSkill/) • [贡献指南](CONTRIBUTING.md) • [安全](SECURITY.md)

</div>

---

## 这是什么

uSkill 不是又一个 Prompt 文件管理器。它把 AI 技能当作**工程资产**来管理：

| 能力 | 说明 | 状态 |
|:---|:---|:---|
| **双层标准** | 标准 `SKILL.md`（Agent Skills 开放规范，跨 Agent 可移植）+ `uskill.yaml`（uSkill 增强契约：类型、权限、溯源、评测） | ✅ 已实现，含校验/导入/导出 |
| **受治理运行时** | Provider 抽象（OpenAI Responses / Chat 兼容网关 / Mock）、真实 timeout/retry 强制执行、组合技能真实子技能调度、输出结构校验、权限白名单、人工审批与恢复、磁盘检查点 | ✅ 已实现，测试覆盖 |
| **SOP 转换** | 规则式结构化解析（保留标题/约束/嵌套/表格，不丢原文）+ AI 转换（JSON Schema 约束输出、机器可读转换报告） | ✅ 已实现 |
| **技能评测** | 版本化评测集、确定性断言评分器、**No-Skill 基线 vs Skill 辅助**对照、Markdown/JSON 报告 | ✅ 已实现 |
| **治理** | 最小权限策略、审计日志、Draft→Validated→Reviewed→Published→Deprecated 生命周期门禁 | ✅ 核心已实现 |
| **技能市场 / 语义检索** | Registry、去重、语义推荐 | 🚧 规划中（见 Roadmap） |

> 我们只对已实现且有测试证据的能力打 ✅。规划中的能力见 [Roadmap](docs/roadmap.md)。

## 双层技能标准

```
skills/agent-skills/code-review/
├── SKILL.md          # 开放标准层：任何兼容 Agent Skills 的 Agent 都能加载
├── uskill.yaml       # uSkill 增强层：类型化 I/O、执行策略、权限、溯源（非官方规范文件）
├── references/       # 渐进式加载的领域知识
├── scripts/          # 确定性操作（须注册进 ToolRegistry 才可执行）
└── evals/            # 评测集：证明这个技能真的有用
```

## 快速开始

```bash
# 安装（Python >= 3.11）
pip install -e ".[dev]"          # 开发安装
# 或作为依赖使用：core + cli，模型能力为可选 extras
pip install -e ".[llm]"          # 接入 OpenAI / 兼容网关

# 校验与体检
uskills validate skills/
uskills doctor

# 创建一个新的标准技能（双层结构一键脚手架）
uskills init my-skill

# 导入 / 导出开放标准技能
uskills import-skill ./some-agent-skill/
uskills export-skill skills/atomic/text_summarize.yaml

# 无 Key 运行技能（Mock Provider 驱动，CI 可跑）
uskills run content_pipeline --input '{"text":"示例"}' --library skills

# SOP 转技能（保留原文全部信息）
uskills convert examples/customer_service_sop.md --output skills/generated

# 评测：技能相对无技能基线是否真的提升了任务完成率
uskills eval --skill skills/atomic/code_review.yaml \
  --suite skills/agent-skills/code-review/evals/dataset.json
```

Python 中使用运行时：

```python
from core.uskills import SkillRuntime, load_skill
from core.uskills.runtime import MockProvider, SkillLibrary

library = SkillLibrary()
library.load_directory("skills")

runtime = SkillRuntime(MockProvider('{"keywords": [], "summary": ""}'), library=library)
skill = load_skill("skills/atomic/text_keyword_extract.yaml")

record = runtime.run(skill, {"text": "..."})
print(record.status, record.result, record.usage, record.execution_time)
```

## V2.0 新能力（含自 1.2 起延续并强化的能力）

- **Runtime 2.0**：`control.timeout/retry` 不再只是声明，而是被真实强制执行；`content_pipeline` 这类组合技能现在通过工作流引擎**真实调度**子技能，而不是在 Prompt 里"告诉模型应该调用"。
- **Agent Skills 开放标准兼容**：原生校验/导入/导出 `SKILL.md` 技能包；uSkill 扩展只放 `uskill.yaml`，不碰官方 Frontmatter。
- **Provider 抽象**：Mock / OpenAI Chat / OpenAI Responses API；任何 OpenAI 兼容网关可通过 `base_url` 接入。
- **评测体系**：每个技能可携带评测集，确定性评分器优先，支持基线对照与回归追踪。
- **治理**：最小权限执行、审计日志、发布生命周期门禁。
- **工程修复**：补齐 LICENSE、真实 CI 徽章、版本单一来源、Python ≥3.11、JSON Schema 方言修正、模板变量校验并入 Validator。

## 项目结构

```
uSkill/
├── AGENTS.md                 # 编码 Agent 工作规则
├── .agents/skills/           # 仓库自身的研发技能（repo-audit/authoring/evaluation/release）
├── core/uskills/
│   ├── schema.py validator.py converter.py ai_converter.py indexer.py
│   ├── manifest.py           # uskill.yaml V2
│   ├── agentskills.py        # Agent Skills 开放标准兼容层
│   ├── evaluation.py         # 评测框架
│   ├── runtime/              # providers · tools · engine · state
│   ├── governance/           # policy · audit · lifecycle
│   └── executor.py           # V1 兼容门面 → 委托 runtime
├── cli/ adapters/            # CLI 与框架适配层（执行统一走 runtime）
├── skills/                   # 技能资产（legacy YAML + agent-skills 双层包）
├── standards/ examples/ docs/ tests/ scripts/
└── .github/workflows/        # CI（矩阵+覆盖率+构建）、Release、Pages
```

## 核心方法论：驾驭工程

1. **定义驾驭**：标准 Schema + 双层标准固化技能边界、约束与依赖
2. **过程驾驭**：运行时强制执行超时、重试、权限、审批、中断与恢复
3. **结果驾驭**：输出结构校验与确定性断言前置，模型不能自证正确
4. **迭代驾驭**：评测数据回流 + 生命周期门禁，驱动版本化进化

## 开发与贡献

```bash
pytest                    # 全部测试基于 MockProvider，无需 API Key
ruff check . && mypy core/
mkdocs build --strict
```

完整文档：[https://zhubao315.github.io/uSkill/](https://zhubao315.github.io/uSkill/)
· 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)
· 仓库审计报告：[docs/audit/REPOSITORY_AUDIT.md](docs/audit/REPOSITORY_AUDIT.md)

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

<div align="center">

**[文档](https://zhubao315.github.io/uSkill/)** • **[GitHub](https://github.com/zhubao315/uSkill)** • **[Issues](https://github.com/zhubao315/uSkill/issues)**

Made with ❤️ by [zhubao315](https://github.com/zhubao315)

</div>
