# Skill Runtime 2.0

运行时是 uSkill 的执行核心：Schema 中声明的控制字段在这里**被真正执行**。

## 执行流程

```
run(skill, inputs, cancel_token=None)
 ├─ 输入治理: 必填校验 / 默认值 / 拒绝未声明参数 / JSON 类型检查
 │            + JSON Schema 约束 (enum / min·max / pattern / 长度 / nullable / 数组元素类型)
 ├─ 计划: approval-gate? → subskill:* (depends_on 时按 DAG 分层并行) → llm 合成步
 ├─ 每步: ThreadPool 超时控制 + 瞬时错误重试(仅 retryable) + 指数退避 + 幂等守卫
 │        + 每步/每次尝试之间检查取消
 ├─ 输出治理: JSON 解析失败=失败(绝不伪装) + 声明字段齐备 + JSON Schema 全量校验
 │            校验失败 → 有限修复环 (control.repair, 默认≤2次, 附错误反馈重问, 超限判失败)
 ├─ 每步落盘检查点(.uskills/runs/<run_id>.json)
 └─ RunRecord: 步骤状态/耗时/token/事件流 (含 step_backoff / cancel_requested)
```

## 步骤状态机

```
PENDING → READY → RUNNING → COMPLETED / FAILED / SKIPPED
                        ├→ RETRYING → RUNNING
                        ├→ INTERRUPTED (人工拒绝)
                        ├→ CANCELLED (CancelToken)
                        └→ WAITING_APPROVAL → (resume) RUNNING
```

## Provider 抽象

| Provider | 说明 |
|---|---|
| `mock` | 脚本化响应，测试与 CI 专用，无需 API Key |
| `openai-chat` | Chat Completions（及任何 `base_url` 兼容网关） |
| `openai-responses` | Responses API（推荐的现代接口） |
| `openai-compatible` | 任意 OpenAI 兼容网关；`base_url` 可用 `USKILLS_OPENAI_BASE_URL` 环境配置 |
| `anthropic` | Anthropic Messages API（懒加载 `anthropic` 包；JSON 约束经引擎复验） |
| `local` | 本地 OpenAI 协议服务（Ollama 默认 `http://localhost:11434/v1`，亦可 llama.cpp/vLLM） |

模型名在技能 YAML 中只是默认值；具体模型/网关由部署配置与 Provider 决定。
能力声明（json_mode / structured_output / function_calling / streaming）是
**信息性协商**：引擎不假设任何 Provider 原生支持结构化输出——无论声明如何，
输出一律经过 Schema 复验，校验失败即进入修复环或判失败（复验才是真门禁）。

## 组合技能：真实调度

`skills/composite/content_pipeline.yaml` 声明 `tools: [text_keyword_extract,
text_summarize, text_translate]`。运行时将其解析为三个子技能步骤并依次执行，
上一步输出注入后续上下文；全部结束后再执行合成 LLM 步。声明的工具无法解析
为子技能或注册工具时，运行**失败**（而不是退化为"让模型自己想象子步骤"）。

## 参数与输出约束（2.0）

输入参数支持 JSON Schema 语义约束（全部可选、向后兼容）：
`enum`、`minimum`/`maximum`、`min_length`/`max_length`、`pattern`、
`nullable`、数组 `items_type`，或整段 `schema:` 覆盖。校验发生在**模型调用
之前**，违规请求根本不会到达 LLM。

输出侧：`output.params` 派生 required 检查；`output.schema:` 可给完整
JSON Schema 做全量校验。校验失败进入**有限修复环**：把错误原文附回提示词
重新请求，`control.repair`（默认 2，可设 0 关闭）封顶，绝不无限重试。

```yaml
input:
  params:
    - {name: priority, type: string, enum: [low, high]}
    - {name: count, type: integer, minimum: 1, maximum: 100}
output:
  format: json
  schema:
    type: object
    required: [summary]
    properties:
      summary: {type: string, maxLength: 500}
control:
  repair: 2
```

## 取消、退避与幂等

```python
token = CancelToken()
record = runtime.run(skill, inputs, cancel_token=token)
token.cancel("用户停止")  # 在步骤/尝试边界生效；进行中的请求由 control.timeout 封顶
```

- `control.backoff_base`：瞬时错误重试按 `base × 2^attempt` 指数退避（30s 封顶），
  默认 0 保持旧行为。
- 工具 `idempotent=False`（付款/删除/发布类副作用）：**永不自动重试**，
  瞬时失败也直接判失败并明确说明原因。

## 组合技能 DAG

`execute.depends_on` 声明子技能依赖（工具名 → 前置工具名列表），运行时做
Kahn 分层：同层步骤在 `control.max_workers`（默认 2）内并行，层间串行合并
输出。依赖环与未声明依赖直接失败（`ExecutionFailedError`）。不写
`depends_on` 时维持声明顺序执行，行为与 1.x 完全一致。

## 安全边界

- `execute.tools` 只是**声明**；实际执行必须经过 `ToolRegistry` 注册 +
  `PermissionPolicy` 白名单（默认只允许 `read`）。
- 技能文本与输入永远被视为数据，不提升为系统指令（系统提示词中显式声明）。
- 技能目录里的 `scripts/` **不会**被运行时自动执行。

## 恢复与审批

```python
runtime = SkillRuntime(provider, library=library, store=RunStore(".uskills/runs"))
record = runtime.run(gated_skill, inputs)  # → WAITING_APPROVAL
record = runtime.resume(record.run_id, approve=True)  # 继续
# resume(..., approve=False) → INTERRUPTED
```

## V1 兼容

`SkillExecutor` 保留旧 API 与返回结构，内部委托新运行时（超时/重试现在真实生效）。
新代码请直接使用 `SkillRuntime`。
