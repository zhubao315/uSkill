# Skill Runtime 2.0

运行时是 uSkill 的执行核心：Schema 中声明的控制字段在这里**被真正执行**。

## 执行流程

```
run(skill, inputs)
 ├─ 输入治理: 必填校验 / 默认值 / 拒绝未声明参数 / JSON 类型检查
 ├─ 计划: approval-gate? → subskill:* → llm 合成步
 ├─ 每步: ThreadPool 超时控制 + 瞬时错误重试(仅 retryable)
 ├─ 输出治理: JSON 解析失败=失败(绝不伪装成 JSON) + 声明字段齐备校验
 ├─ 每步落盘检查点(.uskills/runs/<run_id>.json)
 └─ RunRecord: 步骤状态/耗时/token/事件流
```

## 步骤状态机

```
PENDING → READY → RUNNING → COMPLETED / FAILED / SKIPPED
                        ├→ RETRYING → RUNNING
                        ├→ INTERRUPTED (人工拒绝/取消)
                        └→ WAITING_APPROVAL → (resume) RUNNING
```

## Provider 抽象

| Provider | 说明 |
|---|---|
| `mock` | 脚本化响应，测试与 CI 专用，无需 API Key |
| `openai-chat` | Chat Completions（及任何 `base_url` 兼容网关） |
| `openai-responses` | Responses API（推荐的现代接口） |

模型名在技能 YAML 中只是默认值；具体模型/网关由部署配置与 Provider 决定。
能力声明（json_mode / structured_output / function_calling）不满足时
显式报错，不静默降级。

## 组合技能：真实调度

`skills/composite/content_pipeline.yaml` 声明 `tools: [text_keyword_extract,
text_summarize, text_translate]`。运行时将其解析为三个子技能步骤并依次执行，
上一步输出注入后续上下文；全部结束后再执行合成 LLM 步。声明的工具无法解析
为子技能或注册工具时，运行**失败**（而不是退化为"让模型自己想象子步骤"）。

## 安全边界

- `execute.tools` 只是**声明**；实际执行必须经过 `ToolRegistry` 注册 +
  `PermissionPolicy` 白名单（默认只允许 `read`）。
- 技能文本与输入永远被视为数据，不提升为系统指令（系统提示词中显式声明）。
- 技能目录里的 `scripts/` **不会**被运行时自动执行。

## 恢复与审批

```python
runtime = SkillRuntime(provider, library=library, store=RunStore(".uskills/runs"))
record = runtime.run(gated_skill, inputs)      # → WAITING_APPROVAL
record = runtime.resume(record.run_id, approve=True)   # 继续
# resume(..., approve=False) → INTERRUPTED
```

## V1 兼容

`SkillExecutor` 保留旧 API 与返回结构，内部委托新运行时（超时/重试现在真实生效）。
新代码请直接使用 `SkillRuntime`。
