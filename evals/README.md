# evals/ — 技能评测集

`datasets/` 存放按技能版本化的评测套件（`EvalSuite` JSON，确定性断言）。

- 套件名与 `skill` 字段绑定 skill_id，随技能版本演进（新版本→新套件）。
- 运行：`uskills eval --skill <yaml> --suite <suite.json>`；
  真实模型对照：`--provider openai-chat`（无基线提示或 mock 时基线自动跳过，不造假）。
- 发布回归门禁：`--compare <上次报告.json> --gate`（回归→非零退出，可阻断 CI）。
- 多模型对比：`--models gpt-4o-mini,claude-sonnet-4-5`。
- `security-injection-*` 用例为注入探针：真实模型上须人工核对输出未泄露系统信息。

**状态说明**：套件内 `baseline_prompt` 面向真实模型运行；本仓库 CI 只做
MockProvider 离线结构校验（断言加载、字段契约、runner 逻辑），真实模型
分数需在部署环境运行后存入 `reports/`（部署方职责，不在此伪造）。

`reports/*.mock-baseline.json` 是 CI 回归门禁的确定性基线（见
`reports/README.md`），不代表模型效果。
