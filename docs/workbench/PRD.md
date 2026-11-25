# uSkill 3.0 Workbench — 产品需求文档（PRD）

> 基准：uSkill **2.0.0 已发布**（`core/uskills/_version.py:10`）。证据约定：标为「已实现」的能力必须给出 `文件:行号`；规划能力一律标「未实现」，不得写成现状。每条需求末尾给出可复算验收锚点，详见 `ACCEPTANCE_CRITERIA.md`。本文件只描述产品，不修改任何仓库或远端数据。

## 1. 问题陈述（审计证据链）

| 痛点 | 升级前证据 | 2.0 现状（已实现） |
|---|---|---|
| 经验锁在 SOP/Prompt 里，无法成为资产 | `docs/audit/REPOSITORY_AUDIT.md:24`（无原生 Agent Skills 支持）、`:35`（SOP 解析丢非列表内容） | 双层标准 `SKILL.md + uskill.yaml`：`agentskills.py:76-91,175-254`、`manifest.py:24-25` |
| 执行是黑盒，控制字段只是声明 | `REPOSITORY_AUDIT.md:25`（Executor 不兑现 timeout/retry/steps）、`PROJECT_AUDIT.md:21,24-26`（无 cancel/backoff/修复环/DAG） | `runtime/engine.py:1-18,81-136,543-581,656-730` 已真实执行 |
| 发布凭感觉，回归无人拦截 | `PROJECT_AUDIT.md:33`（多模型/版本门禁/隔离 judge 缺口）、`REPOSITORY_AUDIT.md:42`（评测仅 PARTIAL） | `evaluation.py:457-636`、`cli/uskills_cli.py:318-410` 已实现门禁 |
| 治理与分发缺位 | `REPOSITORY_AUDIT.md:41`（治理 PARTIAL）、`PROJECT_AUDIT.md:34`（风险分级/检索/打包） | `governance/risk.py:49-83`、`registry.py:83-131`、`packaging.py:34-89` |
| 工程债 | `REPOSITORY_AUDIT.md:20-23`（命名/版本重复/LICENSE/3.10 EOL） | `_version.py:6-10`、`pyproject.toml:10-11,61-63,69-70` |

结论（已实现）：2.0.0 把上述痛点收敛为「有产物、有门禁、有证据」的资产层（`docs/index.md:16-19`）。本 PRD 的 3.0 增量只做**Workbench 工作台**，不改已发布的运行时契约（`docs/migration.md:3-5`）。验收：AC-DOC-04、AC-CI-07。

## 2. 用户画像与真实用例 → 现有命令

| 画像 | 用例 | 现有命令/代码路径 | 状态 |
|---|---|---|---|
| 技能作者/维护者 | 从 SOP 建草稿、迁移旧资产 | `init` `cli:163-200`；`build` `cli:413-444`；`migrate` `cli:102-131`；`convert` `cli:57-79` | 已实现 |
| 评测/发布负责人 | 基线对照、回归门禁、隔离评审 | `eval --compare --gate --judge` `cli:318-410`、`evaluation.py:534-636` | 已实现 |
| 运行时运维 | 执行、审批恢复、风险、审计 | `run` `cli:274-315`；`resume` 仅 Runtime API `engine.py:270-319`（CLI 解析器 `cli:679-890` **无** resume 子命令） | 部分实现 |
| 运行时运维 | 风险推导、审计查看 | `risk` `cli:479-542`；`audit` `cli:590-612` | 已实现 |
| Agent 集成方 | 检索、离线打包、MCP 桥接 | `search` `cli:447-461`；`package` `cli:464-476`；`adapters/mcp_bridge.py:32-87` | 已实现 |

注意：`resume` 是 Runtime 能力而非 CLI 命令，Workbench 若暴露「恢复」按钮必须调用 `SkillRuntime.resume()`（需 `RunStore`），**不得**自称已有 CLI 入口。验收：AC-GOV-04。

## 3. 功能需求（FR）

| ID | 需求 | 状态 | 代码路径 | 验收 |
|---|---|---|---|---|
| FR-1 | 双层技能标准与格式识别 | 已实现 | `standards_compat.py:26-69`、`agentskills.py:94-163` | AC-CI-04 |
| FR-2 | 输入约束（enum/min/max/pattern/nullable） | 已实现 | `schema.py:89-178`、`engine.py:81-136` | AC-CI-07 |
| FR-3 | 超时/重试/退避/取消/幂等 | 已实现 | `engine.py:543-581,625-654`、`state.py:187-209` | AC-CI-07 |
| FR-4 | 组合技能 DAG 分层并行 | 已实现 | `engine.py:148-176,418-516` | AC-CI-07 |
| FR-5 | 输出 Schema 校验 + 有限修复环 | 已实现 | `schema.py:248-268`、`engine.py:699-730` | AC-GOV-03 |
| FR-6 | 基线对照 / 多模型 / `--gate` / 隔离 judge | 已实现 | `evaluation.py:457-636` | AC-CI-06、AC-GOV-02 |
| FR-7 | 风险 L0–L4、导入扫描、审计脱敏 | 已实现 | `risk.py:19-83`、`builder/scan.py:19-50`、`audit.py:19-39` | AC-GOV-04 |
| FR-8 | Registry 五模式检索 | 已实现 | `registry.py:81-131` | AC-CI-04、AC-CI-05 |
| FR-9 | 离线可校验 zip 包 | 已实现 | `packaging.py:34-89` | AC-CI-08 |
| FR-10 | 零数据库/零服务端 | 已实现 | `docs/distribution.md:3-4`、`docs/index.md:427` | AC-WB-01 |
| FR-11 | 步骤级崩溃续跑（幂等重放） | **未实现** | `REPOSITORY_AUDIT.md:49`（OPEN） | 规划，无验收门禁 |
| FR-12 | 触发精度自动测量 | **未实现** | `REPOSITORY_AUDIT.md:46`、`docs/evaluation.md:130-132` | 规划，无验收门禁 |
| FR-13 | 条件路由/循环执行 | **未实现**（IR 仅分类：`builder/ir.py:18-38`） | `REPOSITORY_AUDIT.md:48` | 规划，无验收门禁 |
| FR-14 | Workbench 3.0 实体与界面 | **未实现** | 见 `DATA_MODEL.md` 3.0 目标实体段 | AC-WB-01…10 |
| FR-15 | 社区市场 / 私有仓库分发 | **未实现** | `docs/roadmap.md:24-30` | 前置条件见 `ROADMAP_3.0.md` |

## 4. 非目标（摘自真实边界）

- **无数据库、无服务端**：注册中心 = 本地文件系统 + Git（`docs/distribution.md:3-4`）；Workbench 不得引入 DB 或远端服务（FR-10，AC-WB-01）。
- **不执行脚本**：导入技能的 `scripts/` 永不执行，仅静态扫描并置 `untrusted_source=true`（`agentskills.py:200-222`、`docs/evaluation.md:117-120`）。
- **无 OS 沙箱**：隔离由部署方负责（`SECURITY_AUDIT.md:33`；`PRODUCT_CHARTER.md:31`，原 `SECURITY.md` 未包含在本快照，精确行号**需要验证**）。
- **不建市场/排行榜**：`docs/roadmap.md:28-30`、`docs/distribution.md:4`。
- **Builder 不自动发布**：产物固定 `drafts/` + `draft` 标签 + 生命周期 DRAFT（`builder/pipeline.py:1-5,121-124`）；tag/Release 手动（`ROADMAP_2.0.md:54,60`）。验收 AC-GOV-01。
- **评测不伪造**：未知模型成本 `null`、`repeats=1` 一致性 `null`、judge 不翻转确定性结果（`evaluation.py:7-14,42-49,434,447`）。验收 AC-GOV-02、AC-GOV-03。

每一节均以可复算门禁收尾：`ACCEPTANCE_CRITERIA.md` 中的 AC-CI-01…10、AC-DOC-01…05、AC-GOV-01…04、AC-WB-01…10。
