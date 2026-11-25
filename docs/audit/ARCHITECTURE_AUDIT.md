# 架构审计（历史快照 · v1.2 基线 · 2026-11-13）

> 文中 Sprint 1–5 架构缺口均已交付；当前架构见 docs/architecture.md。

## 当前模块依赖（实测 import 图）

```
cli ──► converter/indexer/schema/validator
adapters ──► schema/validator
agentskills ──► manifest ──► schema
evaluation ──► runtime ──► providers/tools/state ──► governance.policy
executor(兼容门面) ──► runtime
validator ──► schema, manifest(函数级)
indexer ──► validator
ai_converter ──► runtime.providers, schema
```

无环；治理与评测不依赖具体 Provider；执行只存在于 `runtime/`。

## 与任务书七层的映射

| 任务书层 | 现有模块 | 状态 |
|---|---|---|
| L1 输入 | `converter.parse_sop`、`agentskills.inspect` | ✅ 基础；统一 Importer 接口缺 |
| L2 构建 | `converter`、`ai_converter` | ⚠ 无 IR/评分/审闭环 → Sprint 2 `builder/` |
| L3 标准 | `schema`(V1)、`manifest`(V2)、`standards/` | ✅ 双层；Schema 版本目录与 migrate 缺 |
| L4 执行 | `runtime/`(engine/providers/tools/state) | ✅ 核心；DAG 并行/取消缺 → Sprint 3 |
| L5 评测 | `evaluation.py` | ✅ 基线对照；judge/多模型/回归门禁缺 → Sprint 4 |
| L6 治理 | `governance/`(policy/audit/lifecycle) | ⚠ 风险分级/脱敏/脚本扫描缺 → Sprint 5 |
| L7 分发 | `agentskills.export`、`adapters/` | ⚠ 打包/搜索缺 → Sprint 5 |

## 架构债（如实）

1. `evaluation.py`、`indexer.py`、`agentskills.py` 是单文件模块；超过 ~400 行
   或新增第二职责时应拆包（当前规模不必拆，符合"不以文件数论架构"）。
2. `runtime.engine._plan` 只支持 approval+子技能顺序链；DAG 需要 `dependencies`
   声明与分层并行执行（Sprint 3，保持单进程）。
3. `indexer` 与未来 `registry.search` 职责重叠：indexer 保留"生成 Markdown
   目录"，检索能力放 `registry/`，避免双份真相。
4. Manifest 与 V1 schema 是两套模型，转换器在 `agentskills.py`/`manifest.py`；
   Sprint 1 补 `standards/manifest/v1,v2` 导出与 `detect_format()`。

## 依赖方向不变式（Sprint 验收用）

- `schema` 不 import 任何其他 core 模块（纯定义）。
- `runtime` 不 import `adapters`/`cli`。
- 评测不得被 runtime import（评测独立于被测系统）。
- openai/anthropic SDK 仅出现在 provider 文件的惰性 import 中。
