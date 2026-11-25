# 数据模型（已实现结构 + 3.0 目标实体）

> 已实现部分以 `core/uskills/` 源码为准；3.0 目标实体全部标 **未实现**，不得当作现有表/字段。状态标记：`已实现` / `部分实现` / `未实现` / `需要验证`。

## 1. V1 `USkill`（已实现）

`schema.py:317-337`：根字段 `skill_id`、`meta`、`input`、`execute`、`output`、`control`、`source`（可选，`:333-337`）。`skill_id` 匹配 `uskill-{atomic|composite|domain|governance}-{name}-vX.Y.Z`（`:33-36,339-348`）。子结构：

- `SkillMeta`（`:63-86`）：name/version/category/domain/description/tags/owner，`extra="forbid"`。
- `SkillParam`（`:89-149`）：`name`、`type`（严格 `ParamType` 枚举 `:48-60`）、`required`、`default`、`items_type`、`schema` 覆盖。
- `ExecuteConfig`（`:191-231`）：`prompt_template`、`steps`、`temperature`、`model`、`tools`、`fallback`、`requires_approval`、`depends_on`。
- `OutputConfig`（`:234-268`）：`format`、`params`、`validation_rules`、`schema`；`json_schema()` 由 params 派生 permissive schema。
- `ControlConfig`（`:271-297`）：`timeout/retry/interrupt/breakpoint_allowed/mockable/repair/backoff_base/max_workers`。
- `SourceTrace`（`:300-314`）：`sop_name/sop_path/step_index/raw_step/context`（原文上下文不丢）。

## 2. 2.0 可选字段（已实现，向后兼容）

| 字段 | 语义 | 证据 |
|---|---|---|
| `enum / minimum / maximum / min_length / max_length / pattern / nullable` | 调用模型前的输入约束；`pattern` 定义期即编译校验 | `schema.py:114-138,140-178`；`engine.py:81-136` |
| `output.schema` | 输出文档完整 JSON Schema，全量校验 + 修复环目标 | `schema.py:248-268`；`engine.py:699-730` |
| `execute.depends_on` | 组合技能 DAG 边（工具名 → 前置工具名列表） | `schema.py:213-218`；`engine.py:148-176` |
| `control.repair / backoff_base / max_workers` | 修复预算（默认 2）、退避底数（默认 0）、层内并行（默认 2） | `schema.py:281-297`；`engine.py:568-574,456` |

`SCHEMA_VERSION=1.1.0` 有意不 bump（`schema.py:6-10,23`）；旧文件零改动继续工作（`docs/migration.md:3-5`）。验收 AC-DOC-04。

## 3. V2 Manifest（已实现）

`USkillManifest`（`manifest.py:125-140`）：`apiVersion: uskills/v2`、`kind: Skill`（`manifest.py:24-25,130-131`，Literal 约束 → JSON Schema const，`:142-143`）；`metadata`（`:54-62`）、`compatibility`、`execution`（mode/entry/timeout/retry/requires_approval，`:65-76`）、`inputs`/`outputs`（JSON Schema）、`tools`（permission 枚举 `:44-51,79-85`）、`security`（`:87-103`）、`provenance`（`:105-115`）、`evaluation`（`:117-123`）。双层布局：`SKILL.md` 标准层 + `uskill.yaml` 增强层，官方 frontmatter 不被修改（`agentskills.py:1-15,175-190`）。导入溯源含 `content_sha256`（`agentskills.py:53-57,244-249`）。格式识别 `detect_format()` 区分 `skill-v1 / manifest-v2 / agent-skill`（`standards_compat.py:26-29,48-69`）。

## 4. RunRecord / 步骤状态机（已实现）

`state.py:20-32` 定义 10 个 `StepState`，终态集合 `:35-41`。`StepRun`（`:52-101`）含 `step_id/kind/input/output/error/started_at/finished_at/attempts/retry_errors/usage/execution_time`；`RunRecord`（`:104-160`）含 `run_id/skill_id/status/inputs/outputs/steps/events/error/usage/result`；`new_run_id()` 为 `run-<uuid12>`（`:48-49`）。`RunStore.save/load/list_runs()` 落盘 `.uskills/runs/<run_id>.json`（`:163-184`）。审批路径 `WAITING_APPROVAL → resume(approve) → RUNNING / INTERRUPTED`（`engine.py:270-319`）。`CancelToken` 为协作式信号（`:187-209`）。状态：已实现；**步骤级崩溃续跑未实现**（`REPOSITORY_AUDIT.md:49`）。

## 5. 评测套件与 null 诚实（已实现）

`EvalSuite`（`evaluation.py:102-123`）：`skill/version/cases`；`EvalCase`（`:86-100`）含 `baseline_prompt`、`assertions`、`security_probe`。`EvalReport.to_dict()`（`:206-246`）输出 baseline/assisted 成功率、`delta_pp`、`repeat_outcomes`、独立 `judgments` 段。`_compute_metrics()`（`:418-454`）明确：`consistency` 在 `repeats=1` 为 `null`（`:430-434`）、`cost_usd` 未知模型为 `null`（`:42-49,447`）、`tool_success_rate` 无工具调用为 `null`（`:450`）。实例基线 `evals/reports/text_summarize.mock-baseline.json:12,24` 如实写 `null`。验收 AC-GOV-03。

## 6. 审计 JSONL 与包清单（已实现）

`governance/audit.py:19-39`：敏感键正则 `token|secret|key|password|credential|api[-_]?hdr` → `***REDACTED***`；大块键 `input|inputs|prompt|output|outputs|text|body` → `{sha256(前16位), length, note}`。`AuditLogger.log()` 追加式 JSONL（`:56-67`）。`package.json`（`packaging.py:66-88`）逐文件 `{path, sha256}` + `compatibility_layers` + `verification` +「inert」策略声明。生命周期 `SkillLifecycle` 五态 `draft→validated→reviewed→published→deprecated` 及非法跳转校验（`governance/lifecycle.py:14-53`）。风险 `RiskLevel` L0–L4 及标签（`governance/risk.py:19-33`）。验收 AC-GOV-04。

## 7. 3.0 目标实体（全部 **未实现**）

以下为 Workbench 3.0 规划实体，源码中**不存在对应模型、表或文件**；不得与上文已实现结构混写。

| 实体 | 规划职责 | 状态 |
|---|---|---|
| `SkillIdentity` | 跨源稳定身份（同名不等于同一技能） | 未实现 |
| `SkillVersion` | 版本谱系与 installed_hash vs latest 区分 | 未实现 |
| `SkillSource` | 一个技能可有多个来源（本地/Git/ZIP/导入） | 未实现 |
| `SkillInstall` | 安装目标目录/映射记录 | 未实现 |
| `SkillCollection` | 用户自定义集合（区别于仓库分类） | 未实现 |
| `SkillFavorite` | 收藏关系 | 未实现 |
| `SkillLifecycleRecord` | 3.0 生命周期事件流（区别于现有 `SkillLifecycle` 枚举） | 未实现 |
| `EvaluationRun` | 评测运行记录（现有 `EvalReport` 是文件报告，非持久化实体） | 未实现 |
| `SkillRun` | 运行历史实体（现有 `RunRecord` 是 JSON 文件，非实体表） | 未实现 |
| `SkillFeedback` | 用户反馈/评审意见 | 未实现 |

### 关系与约束（规划，未实现）

1. `SkillIdentity` 1 — N `SkillSource` / `SkillVersion` / `SkillInstall`；同名技能不得自动合并身份，必须用来源 + 内容哈希判定（`PRODUCT_CHARTER.md:23-25` 的「文件是真相源」延伸）。
2. `SkillVersion` 保存 `installed_hash`（当前已安装内容）与 `latest`（远端/仓库最新）**两个不同字段**；相等与否驱动更新提示——现有 `manifest.provenance.content_sha256`（`manifest.py:113`）只是单文件摘要，不是版本实体。
3. `SkillInstall` 指向本地目录，不复制技能正文进 DB（资产真相源仍是文件系统，见 `PRODUCT_CHARTER.md:23-24`）。
4. `EvaluationRun` / `SkillRun` 引用既有 `run_id` 与报告路径，不重新发明执行语义（复用 `engine.py:211-319`、`evaluation.py:457-495`）。
5. 3.0 实体落库必须同时满足：本地优先、无服务端、无敏感数据落盘（`SECURITY_MODEL.md`；AC-WB-01、AC-WB-06）。

验收总表：`ACCEPTANCE_CRITERIA.md`（AC-DOC-04、AC-GOV-03、AC-GOV-04、AC-WB-01…10）。
