# uSkill 架构说明（现状 2.0.0 + Workbench 目标）

> 基准：`_version.py:10`（2.0.0）。证据来自 `docs/audit/ARCHITECTURE_AUDIT.md`（实测 import 图）与源码。状态标记：`已实现` / `部分实现` / `未实现` / `需要验证`。部署形态：零数据库、零服务端（`docs/distribution.md:3-4`）。

## 1. 实测 import 图（已实现）

| 边 | 审计依据 | 源码证据 |
|---|---|---|
| `cli → converter/indexer/schema/validator` | `ARCHITECTURE_AUDIT.md:6` | `cli/uskills_cli.py:20-23` |
| `adapters → schema/validator` | `:7` | `adapters/langchain_adapter.py:14-15` |
| `agentskills → manifest → schema` | `:8` | `agentskills.py:27`；`manifest.py:189`（函数级局部导入） |
| `evaluation → runtime → providers/tools/state → governance.policy` | `:9` | `evaluation.py:29`；`engine.py:34-39`；`tools.py:21` |
| `executor`（兼容门面）`→ runtime` | `:10` | `executor.py:16-22` |
| `indexer → validator` | `:12` | `indexer.py:22` |
| `ai_converter → runtime.providers, schema` | `:13` | `ai_converter.py:21-22` |
| `validator → schema, manifest`（函数级） | `:11` | `validator.py:18,213` |

无环；治理与评测不绑定具体 Provider；执行只存在于 `runtime/`（`ARCHITECTURE_AUDIT.md:16`）。验收 AC-CI-01、AC-CI-09。

## 2. 依赖方向不变式（已实现，验收用）

1. `schema` 不 import 任何其他 core 模块——`schema.py:14-20` 仅标准库 + Pydantic。
2. `runtime` 不 import `adapters`/`cli`——`engine.py:29-39` 仅 `..errors/governance`、`..schema` 与 `.providers/tools/state`。
3. 评测不被 runtime import——`engine.py` 无 evaluation 导入；评测独立（`ARCHITECTURE_AUDIT.md:45`）。
4. openai/anthropic SDK 仅在 provider 惰性 import——`providers.py:158,338`；工厂 `providers.py:450-469`。

## 3. 执行链（`docs/runtime.md:5-18` → 代码）

`run(skill, inputs, cancel_token)`（`engine.py:211-262`）：

1. **输入治理**：必填/默认值/拒绝未声明参数/JSON 类型 + JSON Schema 约束（`engine.py:81-136`；`docs/runtime.md:9-10`）。
2. **计划**：`approval-gate? → subskill:* → llm`（`engine.py:331-344`）；`depends_on` 走 DAG（`engine.py:148-176,418-443`）。
3. **每步**：ThreadPool 双层 timeout（`engine.py:670-687`）、仅瞬时错误重试（`tools.py:25-31`、`engine.py:543-581`）、指数退避 `base×2^attempt` 封顶 30s（`engine.py:65,568-574`）、幂等守卫（`engine.py:641-652,749-762`）、步骤/尝试边界检查 `CancelToken`（`engine.py:391,604-607`）。
4. **输出治理**：JSON 解析失败即失败；声明字段齐备 + JSON Schema 全量校验；失败进入 `control.repair` 封顶修复环（`engine.py:699-730`、`schema.py:248-268`）。
5. **落盘**：`RunStore.save()` 写 `.uskills/runs/<run_id>.json`（`state.py:163-184`，CLI 默认 `--runs-dir .uskills/runs` 见 `cli:777`）。
6. **RunRecord**：状态/耗时/token/事件流，`step_backoff`/`cancel_requested` 可查（`state.py:104-160`、`engine.py:571-576,606`）。

步骤状态机见 `state.py:20-41`（`PENDING/READY/RUNNING/COMPLETED/FAILED/SKIPPED/RETRYING/INTERRUPTED/CANCELLED/WAITING_APPROVAL`），审批恢复 `engine.py:270-319`。验收 AC-CI-07、AC-GOV-04。

## 4. 六类 Provider（已实现）

| kind | 实现 | 能力/默认 |
|---|---|---|
| `mock` | `providers.py:78-143` | 脚本化，无需 API Key；CI 基线来源 |
| `openai-chat` | `providers.py:179-230` | Chat Completions，`base_url` 兼容网关 |
| `openai-responses` | `providers.py:233-289` | Responses API，streaming=true |
| `openai-compatible` | `providers.py:292-315` | `USKILLS_OPENAI_BASE_URL` 环境变量 |
| `anthropic` | `providers.py:318-411` | 懒加载 SDK；JSON 由引擎复验 |
| `local` | `providers.py:427-447` | Ollama 默认 `localhost:11434/v1` |

工厂 `providers.py:450-469`；能力声明是信息性协商，Schema 复验才是门禁（`docs/runtime.md:41-44`）。状态：已实现；真实模型评测数据**需要验证**（`docs/evaluation.md:101-102`）。

## 5. Registry 五模式检索（已实现）

`registry.py:83-131`：`name`（精确/部分）、`tag`、`domain`、`keyword`、`dependency`；`auto` 五模式并集按模式优先级去重（`registry.py:88-105`）。`health()` 报加载数/坏文件/重复 id（`:135-144`）。indexer 只生成 Markdown 目录（`indexer.py:92-158`），检索真相只在 registry 一处（`docs/distribution.md:26-27`；`ARCHITECTURE_AUDIT.md:36-37`）。CLI 暴露于 `cli:447-461,829-839`。

## 6. 离线打包（已实现）

`package_skill()`（`packaging.py:34-89`）把 Agent Skill 目录或 legacy YAML 打成 zip；内置 `package.json` 记录 format、逐文件 `{path, sha256}`、兼容层、策略声明「包是惰性的」（`packaging.py:66-77`）；归档自身亦有 sha256（`:84-89`）。无服务、无注册中心依赖（`packaging.py:3-6`）。验收 AC-CI-08。

## 7. MCP 桥接（已实现）

`adapters/mcp_bridge.py:1-15` 明确定位：MCP 管连接，Skill 管方法；桥接**只把 MCP 工具声明注册进 ToolRegistry**（`mcp_bridge.py:32-87`），无网络行为、无 MCP SDK 依赖；默认 `permission=network`、`idempotent=False`（`:11-14,37-40`）。传输生命周期由调用方负责。验收 AC-GOV-04。

## 8. 部署形态与架构债

- 部署：零 DB、零 server（`docs/distribution.md:3-4`；`docs/index.md:427`）；Workbench 目标仍为本地工作台，**不引入远端服务**（`PRODUCT_CHARTER.md:27-35`）。
- 单文件模块 `evaluation/indexer/agentskills`：当前规模不必拆包（`ARCHITECTURE_AUDIT.md:30-33`）——`部分实现/可接受`。
- IR 能分类 decision/loop（`builder/ir.py:18-38`），但运行时 DAG 无条件路由/循环执行（`REPOSITORY_AUDIT.md:48`）——`未实现`。
- Workbench 的 Registry/RunStore/Install Hub 访问层尚无源码——`未实现`；现有 CLI/Runtime 是唯一可复用底座。
