# 评测与治理

## 核心问题

> 一个 Skill 相比不使用它，是否真的提高了 Agent 的任务完成率？

没有对照实验证据的技能，不得宣称"有效"。

## 评测集（版本化 JSON）

```json
{
  "skill": "uskill-atomic-code-review-v1-1-0",
  "version": "1.0.0",
  "cases": [{
    "task_id": "finds-secret-leak",
    "user_input": {"text": "+API_KEY = 'sk-live-abc'"},
    "baseline_prompt": "Review this diff",
    "assertions": [{"type": "json_key", "key": "verdict"},
                    {"type": "regex", "value": "(?i)(secret|key)"}],
    "security_probe": true
  }]
}
```

## 对照实验

`uskills eval --skill <yaml> --suite <json> [--provider mock|openai-chat]`

- **A. No-Skill baseline**：同模型、同输入，无技能契约（仅 `baseline_prompt`）
- **B. Skill-assisted**：完整技能契约 + 输出校验
- 输出 baseline/assisted 成功率与差值（百分点），支持 `--repeats` 与
  Markdown/JSON 报告。

## 评分器

确定性优先：`contains` / `regex` / `json_key` / `json_type` / `equals`。
模型评分（rubric）只能作为补充证据，**生成技能的模型不能同时是唯一评审者**。

## 建议门禁（初始工程值，可按领域配置）

| 指标 | 建议初始阈值 |
|---|---|
| Trigger Precision | ≥ 0.90 |
| Output Validity | ≥ 0.99 |
| 相对基线 | 无显著退化 |
| 安全用例 | 全部通过 |

## 生命周期门禁

```
Draft → Validated → Reviewed → Published → Deprecated
```

`core/uskills/governance/lifecycle.py` 校验合法转移；跳过门禁直接进入
Published 是非法的。审计日志（`governance/audit.py`，JSONL 追加式）记录
权限检查、工具调用、审批决策与运行状态迁移。

## 2.0 评测扩展

### 指标（全部确定性、可复算）

| 指标 | 语义 | 诚实性规则 |
|---|---|---|
| `task_success_rate` | 断言通过率 | — |
| `output_validity` | 运行完成（格式/契约有效）比例 | 与成功率分开统计 |
| `consistency` | 同一用例 `--repeats` 次的多数一致率 | repeats=1 时为 `null`，不伪造 1.0 |
| `latency_ms` | mean / p95 | 实测 |
| `tokens_total` / `usage` | 按步骤 usage 累加 | — |
| `cost_usd` | usage × 内置单价表 | 未知模型为 `null`，不猜价 |
| `tool_success_rate` | 工具步骤完成比例（含子技能回退到注册工具的路径） | 无工具调用时为 `null` |
| `security_probe_pass_rate` | `security_probe` 用例子集通过率 | 注入探针单列 |

### 多模型对比（Skill Benchmark 最小形态）

```bash
uskills eval --skill s.yaml --suite s.suite.json --models gpt-4o-mini,claude-sonnet-4-5
```

同一套件 × 每个模型跑一遍，输出成功率/一致性/成本/延迟对照矩阵。

### 版本对比与发布回归门禁

```bash
uskills eval ... --format json --output run-2026-11-13.json     # 存档
uskills eval ... --compare run-2026-11-13.json --gate           # 回归→退出码 1
```

门禁问题 = 任一此前通过的用例现在失败，或成功率跌幅超过 `--max-drop-pp`
（默认 10pp）。可直接嵌入 CI 阻断发布。

### LLM-as-a-Judge（隔离记录）

`--judge [--judge-model M]`：固定 rubric（0–5 明文标准），每条判定记录
judge 模型名，存于报告的 `judgments` 独立段落，**永远不影响**确定性
pass/fail；judge 调用失败记录为 error，不伪造分数。

### 评测集

`evals/datasets/*.suite.json`：随技能版本化的真实技能套件（摘要/翻译/
流水线，含注入探针用例）。CI 用 MockProvider 验证套件加载与 runner 逻辑；
真实模型分数须在部署环境产生（见 `evals/README.md`，不造假）。

## 风险分级 L0–L4（由能力推导，不信作者声明）

| 级别 | 含义 | 推导信号 |
|---|---|---|
| L0 | 纯文本指令 | 无可达工具、无脚本 |
| L1 | 只读数据处理 | （只读工具场景由 L2 工具面覆盖） |
| L2 | 调用受限工具 | 存在**可解析**工具的声明 |
| L3 | 脚本 / 写文件 / shell | 目录含 `scripts/`；write/shell 权限工具 |
| L4 | 外部系统 / 敏感数据 | network / sensitive_data 权限工具 |

关键规则：**未注册的工具声明不升级风险**——运行时根本执行不了它；
`uskills risk <path>` 输出推导结果；`--json` 机器可读。

导入静态扫描：导入含 `scripts/` 的技能时，`builder/scan.py` 静态标记
进程执行 / 动态代码 / 文件写删 / 网络 / 环境变量读取等模式，写入导入
报告与 `manifest.security.risk_level`，并置 `untrusted_source=true`。
扫描是信号不是沙箱；**导入的脚本 uSkill 永不执行**。

## 审计脱敏

`governance/audit.py` 默认策略：键名含 `token/secret/key/password/credential`
的值掩码为 `***REDACTED***`；`input/prompt/output/text/body` 等大块值只存
`{sha256, length}` 摘要。完整输入只存在于运维自己控制路径下的 RunRecord。

## 当前边界（如实说明）

- 触发精度（trigger precision）的自动测量依赖目标 Agent 的技能选择行为，
  属于规划中的能力；当前 CLI 报告的是任务成功率与结构有效性。
- 未接入真实模型时的评测结果只能证明管线正确性，不能当作效果证据。
