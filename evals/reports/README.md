# evals/reports/ — 回归基线

`*.mock-baseline.json` 是用 **MockProvider 确定性响应**生成的结构基线：
它证明技能契约 + 评测断言 + runner 逻辑在版本间没有回归（CI 每次以相同
mock 响应重跑并 `--gate` 比对），**不是**真实模型的分数。

真实模型评测分数请在部署环境运行 `uskills eval`（`--provider` 选择真实
Provider）后另存新文件（命名建议 `<skill>.<model>.<date>.json`），并按
`--compare <baseline> --gate` 做发布门禁。
