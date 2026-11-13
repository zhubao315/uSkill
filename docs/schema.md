# uSkill Schema

`USkill` 是统一技能格式（schema 版本 1.1.0，位于 `core/uskills/schema.py`）。
导出文件：`standards/uskill.schema.json`，声明 JSON Schema 2020-12 方言
（与 Pydantic V2 生成语法一致）。

核心字段：

- `skill_id`：唯一标识，`uskill-{category}-{name}-v{semver}`
- `meta`：名称、版本、分类、领域、标签、所有者
- `input.params[]`：输入参数定义
  - `type`：**严格枚举** `string|number|integer|boolean|object|array`
  - `items_type`（可选）：数组元素类型，用于嵌套 JSON Schema
  - `schema`（可选）：完整 JSON Schema 覆盖
- `execute`：Prompt 模板、步骤、模型、`tools` 声明、`fallback`、
  `requires_approval`（可选，true 时运行前进入人工审批）
- `output`：格式与声明字段（JSON 输出时运行时强制校验字段齐备）
- `control`：`timeout`/`retry`（由运行时强制执行）、中断与 Mock 能力
- `source`（**可选**）：SOP 溯源；新增 `context` 字段保存原文上下文与约束，
  独立技能可省略整个 source

## 语义校验（validate 默认开启）

| 检查 | 级别 |
|---|---|
| 模板变量未在 input 声明 | 错误 |
| 组合技能未声明 tools | 错误 |
| 可选参数无默认值 | 警告 |

## 与 Agent Skills / Manifest 的关系

- 本 Schema 是 **legacy（V1）技能资产格式**，继续受支持并可被运行时执行。
- 新技能推荐双层结构：标准 `SKILL.md` + uSkill Manifest（`uskill.yaml`），
  见 [Agent Skills 标准](agent-skills.md)。
- `uskills export-skill` 可把 legacy 技能转为双层目录；`manifest_from_legacy_skill`
  自动推导 Manifest。

## Schema 导出（2.0）

```bash
uskills schema --target skill     # V1 → standards/uskill.schema.json
uskills schema --target manifest  # V2 → standards/uskill-manifest.schema.json
uskills schema --target both
```

CI 校验两个导出与代码一致。版本目录说明：`standards/manifest/v1|v2/README.md`，
兼容矩阵：`standards/compatibility/README.md`。

## 2.0 新增可选字段（V1.1 格式向后兼容）

- `input.params[].enum / minimum / maximum / min_length / max_length /
  pattern / nullable`：JSON Schema 语义的输入约束，运行时在调用模型前强制。
- `output.schema`：输出文档的完整 JSON Schema（全量校验 + 修复环目标）。
- `execute.depends_on`：组合技能子步骤 DAG（`{工具: [前置工具]}`）。
- `control.repair / backoff_base / max_workers`：修复预算、指数退避底数、
  DAG 层内并行度。

全部为可选字段：旧技能文件无需修改即可继续加载、校验、执行。
