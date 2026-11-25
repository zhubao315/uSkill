# Roadmap 3.0（Workbench 演进）

> **当前 = 2.0.0 已发布**（`core/uskills/_version.py:10`；`docs/index.md:12`「uSkill 2.0 已发布」）。背景：`docs/ROADMAP_2.0.md:7-60` 的 Sprint 0–6 全部标 ✅（all-done）——审计、标准体系、Builder、Runtime、Evaluation、治理分发、发布准备均已落地；本文只列**真正未闭合**的项。状态：`已实现` / `部分实现` / `未实现` / `需要验证`。

## 1. 真正开放的事项（未实现）

| 项 | 来源 | 状态 | 前置条件 |
|---|---|---|---|
| V3.0 生态：语义检索、依赖图、去重与冲突检测 | `docs/roadmap.md:24-27` | 未实现 | 现有五模式元数据检索已可用（`registry.py:83-131`），语义层另起 |
| 技能签名、来源链、私有仓库分发 | `docs/roadmap.md:27` | 未实现 | 现有 `provenance.content_sha256`（`manifest.py:105-115`）只是雏形 |
| 社区技能市场 | `docs/roadmap.md:28-30` | 未实现 | **前提**：治理与评测证据链成熟；「在没有可信执行与评测基础之前不建设市场」 |
| 触发精度自动测量 | `REPOSITORY_AUDIT.md:46`、`docs/evaluation.md:130-132` | 未实现 | 依赖真实 Agent 技能选择行为 |
| 步骤级崩溃续跑（幂等重放） | `REPOSITORY_AUDIT.md:49` | 未实现 | 现有仅审批点 resume（`engine.py:270-319`） |
| 条件路由 / 循环执行 | `REPOSITORY_AUDIT.md:48`（留待 1.3） | 未实现 | IR 已能分类（`builder/ir.py:18-38`），运行时 DAG 尚不执行 |
| 真实模型评测数据 | `PROJECT_AUDIT.md:42`、`docs/evaluation.md:101-102`、`evals/README.md` | 未实现/需要验证 | CI 基线仅 MockProvider（`ci.yml:60-72`）；分数须部署方跑出 |
| Phase 0 文档清理（历史横幅、版本口径、数字生成器） | `PRODUCT_CHARTER.md:48`、`ACCEPTANCE_CRITERIA.md` AC-DOC-01…05 | 未实现 | 先于任何 Workbench 交付 |
| tag `v2.0.0` 与 Release 页 | `ROADMAP_2.0.md:54,60`、`release.yml:3-5` | 需要验证 | 审计勘误指出 tag 存在但 **Release 页/CHANGELOG 缺失** 是历史模式（`REPOSITORY_AUDIT.md:12`） |

## 2. 七阶段交付计划（规划，全部未实现）

规则：**Phase 0–3 完成之前，不启动 Workbench MVP（Phase 4）**。任何阶段不得把规划写成完成；每阶段退出条件引用 `ACCEPTANCE_CRITERIA.md`。

| Phase | 名称 | 交付物（规划） | 退出门禁 |
|---|---|---|---|
| 0 | 校准 | 6 份审计文件历史横幅、版本口径（2.0.0 / SCHEMA 1.1.0 / uskills-v2）、数字生成器、9 资产口径核对 | AC-DOC-01…05 |
| 1 | Registry 3.0 | 稳定 `SkillIdentity`/`SkillVersion`/`SkillSource`、installed_hash vs latest、同名去重规则 | AC-DOC-04；`DATA_MODEL.md` §7 |
| 2 | Agent Install Hub | `SkillInstall`、来源映射、安装预览（不执行脚本） | AC-WB-03、AC-WB-06 |
| 3 | Run & Governance | 复用 `RunRecord`/`SkillRuntime.resume()`、风险/审计视图、`EvaluationRun` 实体 | AC-GOV-01…04、AC-WB-05 |
| 4 | Workbench MVP | 本地启动、Registry 列表/详情、收藏、安装、运行历史、明暗/响应式 | AC-WB-01…10 |
| 5 | Studio / Eval Lab | Builder 草稿、评测矩阵与 `--gate` 结果可视化（judge 仅参考） | AC-GOV-01…03 |
| 6 | Router / Evolution | 语义检索、依赖图、冲突检测、签名与私有仓库；市场仍需前置条件 | 仅在前置成熟后开 |

四道不可跨域：Builder 输出永不自动发布（`builder/pipeline.py:1-5,121-124`）；judge 永不翻转确定性结果（`evaluation.py:190,239-245`）；未知模型/null 诚实（`evaluation.py:42-49,434,447`）；零 DB/零服务端（`docs/distribution.md:3-4`）。

## 3. 与 2.0 的关系

2.0 的七项 Sprint 已完成（`ROADMAP_2.0.md:7-60`），因此 3.0 **不重做**运行时、评测、治理、分发底座；只在其上叠加工作台与生态实体。所有新 UI 必须从现有命令/Runtime 读真实数据：`search`（`cli:447-461`）、`run/resume`（`cli:274-315`、`engine.py:270-319`）、`risk/audit`（`cli:479-542,590-612`）、`package`（`cli:464-476`）、`eval`（`cli:318-410`）。任何「看起来有数据、实际是假数据」的页面视为未通过验收（AC-WB-02…10）。
