
# RPVI 大规模代码开发

> O-101 断链治理正本：中文入口，承接 uSkill 索引与 agency-agents 映射入链；详版见关联 uSkill。

## 一句话

以 RPVI（Relevance–Precision–Verifiability–Iterability）约束 AI 在 5000+ 行代码库上的大规模开发工作流，对抗长上下文「智商断崖」。

## 要点
- 问题：传统对话式开发在超 5000 行代码后上下文膨胀、准确率骤降；RPVI 工作流以 worktree 隔离 + 压缩上下文 + 验证回路把上下文使用 ↓60%、Bug 修复 ↑10x。
- 四要素：相关性（只装入相关切片）· 精确性（明确接口契约）· 可验证性（测试/类型即门禁）· 可迭代性（小步提交 + 回归）。
- SOP 全文见 [[SOP-26-RPVI-大规模代码AI开发工作流]]；提示词工程见 [[RPVI 提示词工程]]。

## 关联
- - 详版：[[uSkill-ai-engineering-technical-rpvi-large-scale-code-dev]] · [[uSkill-architecture-rpvi-large-scale-code-dev]]
- - SOP：[[SOP-05-大规模代码AI开发工作流]] · [[SOP-26-RPVI-大规模代码AI开发工作流]]
- - 概念：[[RPVI 提示词工程]] · [[∑ uSkill 索引]]
