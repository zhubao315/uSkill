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

## 当前边界（如实说明）

- 触发精度（trigger precision）的自动测量依赖目标 Agent 的技能选择行为，
  属于规划中的能力；当前 CLI 报告的是任务成功率与结构有效性。
- 未接入真实模型时的评测结果只能证明管线正确性，不能当作效果证据。
