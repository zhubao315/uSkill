# uSkill 仓库审计报告（历史快照 · 2026-11-13 · 升级前问题清单）

审计日期：2026-11-13 ｜ 分支：main（b5c4b08）｜ 实施后基线：v1.2.0

本报告记录升级前的问题清单（含代码证据）、严重程度与处置结果。
处置状态：**FIXED** = 本次已修复并有测试；**PARTIAL** = 核心已落地、边界见说明；**OPEN** = 规划中。

## 一、勘误（对外部审计意见的更正）

| 外部结论 | 实际核查 |
|---|---|
| “Release 只到 v0.1.0-preview.1，1.1.0 无正式发布证据” | `git tag` 存在 `v1.1.0`。缺的是 **GitHub Release 页与 CHANGELOG**，不是 tag。已补 CHANGELOG 与 Release 工作流。 |
| “JSON Schema 被手动改成 Draft-07，而 Pydantic 生成 2020-12” | 实际 Pydantic V2 的 `model_json_schema()` **默认不含 `$schema`**；原代码声明 draft-07 属于无依据手写。现显式声明 2020-12 与生成语法一致。 |
| “CI 有 Build Passing 徽章但无真实状态” | 属实（静态徽章）。已改为 `actions/workflows/ci.yml/badge.svg` 真实徽章。 |

## 二、P0 问题与处置

| # | 问题 | 证据（修复前） | 处置 |
|---|---|---|---|
| 1 | 命名混乱 `uSkill`/`uSkills` | README、pyproject URLs、docs 全部指向 `uSkills`，仓库为 `uSkill` | **FIXED**：文档/URL/徽章统一 `uSkill`；Python 包名 `uskills` 保留（不破坏安装），新增 `uskill` 命令别名 |
| 2 | 版本手工重复 | `pyproject.toml:7`、`__init__.py:83`、`cli:27`、`schema.py:16` 四处版本号 | **FIXED**：`_version.py` 单一来源，pyproject dynamic 读取；schema 版本独立并注明语义。CI Release 工作流校验 tag==版本 |
| 3 | LICENSE 缺失 | 根目录无 LICENSE 文件，GitHub 识别不到许可证 | **FIXED**：补 MIT LICENSE，pyproject `license = {file="LICENSE"}` |
| 4 | Python 3.10 已 EOL | `requires-python = ">=3.10"` | **FIXED**：提升至 `>=3.11`，CI 矩阵 3.11–3.13 |
| 5 | 无原生 Agent Skills 支持 | 全仓库无 SKILL.md 解析/校验/导入导出 | **FIXED**：`agentskills.py` 校验/inspect/import/export + 双层 `uskill.yaml`（`manifest.py`）+ CLI `init/import-skill/export-skill/inspect` + 19 项测试 |
| 6 | Executor 不兑现 control 字段 | `executor.py` 单次 chat 调用，timeout/retry/steps/tools 均未实现；`content_pipeline` 的 3 个子技能只在 Prompt 里提及 | **FIXED**：`runtime/engine.py` 真实执行 timeout（线程级强制）、retry（仅瞬时错误）、组合技能 DAG 调度（子技能解析失败=运行失败）、输出 JSON 校验、审批/恢复、磁盘检查点。端到端测试证明 content_pipeline 真实调度 3 子技能 |
| 7 | `validate_template_variables()` 未接入 | `validator.py:122` 存在但 `validate_skill_file()` 不调用 | **FIXED**：`validate_skill_semantics()` 并入 `validate_skill_file/_skill_data/_directory`；未定义变量=错误，歧义配置=警告 |
| 8 | `SkillParam.type` 自由字符串 | `schema.py:65` | **FIXED**：`ParamType` 枚举（typo `strin` 即拒绝，测试覆盖）；新增可选 `items_type`/`schema` 供嵌套 JSON Schema |
| 9 | AIConverter 打印后跳过 | `ai_converter.py:82,87` print+空数组 | **FIXED**：`ConversionReport`（skills/errors/model/raw），逐项错误记录；`last_report` 兼容保留。JSON Schema 约束输出经 Provider 层支持（PARTIAL：strict 视网关能力降级为 json_object，见代码注释） |
| 10 | `source` 必填阻碍独立技能 | `schema.py:173` | **FIXED**：`source: SourceTrace | None`；indexer 归组 `(standalone)` |

## 三、P1 问题与处置

| # | 问题 | 证据 | 处置 |
|---|---|---|---|
| 1 | SOP 解析丢失非列表内容 | `extract_steps()` 仅匹配列表行，段落约束直接丢弃 | **FIXED**：`parse_sop()` 结构化解析（标题/段落/嵌套列表/表格），步骤约束写入 `source.context` 并注入 prompt；原文双向溯源测试覆盖 |
| 2 | JSON Schema 方言不实 | `schema.py:194` 手写 draft-07 | **FIXED**：声明 2020-12，`$id` 指向 uSkill 文档域 |
| 3 | Indexer 仅扫 `*.yaml` | `indexer.py:69`；manifest 文件会被误当技能报错 | **FIXED**：扫描 yaml/yml/json；跳过 `uskill.*`；重复 skill_id 与无效文件明细上报（stats 含 `invalid_files`/`duplicate_ids`） |
| 4 | Adapter 不完整 | `_build_properties` 对 object/array 不产出嵌套 schema；`_build_args_schema` 非 JSON Schema | **FIXED**：嵌套 schema 支持 + `run()` 委托核心运行时（适配层不再各自实现执行） |
| 5 | 测试覆盖窄 | 仅 3 个文件 37 项 | **FIXED**：7 个文件 106 项：runtime 21（超时/重试/输出校验/调度/权限/审批/恢复/检查点）、agentskills 19、评测 9、AI/executor 7、v2 核心 14 等 |
| 6 | CI 单版本、无覆盖率/构建检查 | `ci.yml` 仅 3.11 + pytest | **FIXED**：矩阵 + ruff + mypy + 覆盖率 + schema 一致性 diff + 资产校验 + wheel 构建安装冒烟 + docs strict + pip-audit；新增 tag 驱动 Release 工作流 |
| 7 | 无治理机制 | — | **PARTIAL**：权限策略/审计日志/生命周期枚举已实现并被运行时强制；沙箱执行接口为接口级（SECURITY.md 明确无 OS 级沙箱） |
| 8 | 无独立评测 | — | **PARTIAL**：评测框架+基线对照+确定性评分已落地并有测试；各官方技能的真实模型评测数据待接入（框架禁止伪造，见门禁规则） |

## 四、遗留问题（OPEN，见 Roadmap）

- 触发精度（trigger precision）自动测量依赖真实 Agent 选择行为。
- 语义检索/去重推荐/技能市场：执行与评测基础稳固前不投入。
- Workflow DAG 当前为顺序链 + 条件跳过；并行分支与循环留待 1.3。
- 长任务 `resume` 支持审批点恢复；步骤级崩溃续跑（幂等重放）待实现。

## 五、兼容性承诺验证

- 8 个历史技能 YAML 全部可加载、可校验、可被新运行时执行（测试+CLI 双重验证）。
- `SkillExecutor.execute()` 返回结构保持向后兼容（新增字段不删旧字段）。
- `validate_skill_data/_directory` 签名不变（新参数均有默认值）。
- CLI 五命令 `validate/convert/schema/index/stats` 行为不变。
