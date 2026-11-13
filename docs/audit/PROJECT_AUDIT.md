# uSkill 项目审计报告（2.0 基线）

审计日期：2026-11-13 ｜ 基线：v1.2.0（本地提交 `30835d4`）｜ 目标版本：2.0.0
方法：代码级核查 + 覆盖率实测（71%）+ 全部门禁运行证据。
历史问题（v1.1 时代）的完整证据链见本目录 `REPOSITORY_AUDIT.md`。

## 结论

v1.2.0 已完成：双层标准（SKILL.md + uskill.yaml）、受治理 Runtime（真实
timeout/retry/审批/检查点）、评测框架（基线对照 + 确定性评分）、基础治理
（权限/审计/生命周期）、完整 CI。**本审计面向 2.0.0 的剩余差距。**

## 功能现状与差距（按任务书十大问题）

| # | 问题 | v1.2 现状 | 证据 | 2.0 差距 | 级别 |
|---|---|---|---|---|---|
| 1 | Schema 完整 | 结构+语义校验齐备 | `validator.py` `validate_skill_semantics` | 参数约束（enum/min/max/regex/nullable）缺失 | P1 |
| 2 | Pydantic↔JSON Schema 一致 | 一致，2020-12 方言，CI diff 强制 | `ci.yml` "Schema is up to date" | 缺 Manifest 的 JSON Schema 导出 | P1 |
| 3 | SOP 复杂结构 | 标题/段落/嵌套/表格全保留（`parse_sop`） | `converter.py` + tests | 条件分支/角色交接/循环未建模为 IR | P1 |
| 4 | AI 转换 | 结构化报告 + 逐项错误 | `ai_converter.py` `ConversionReport` | 无质量评分、无测试用例生成、无人审闭环 | P1 |
| 5 | 执行控制 | timeout/retry/审批/恢复/检查点真实生效 | `runtime/engine.py` + 21 项测试 | 无 cancel、无 backoff、无输出修复环、并行缺失 | P1 |
| 6 | 参数注入安全 | 显式变量替换 + 输入治理 | `engine.render_template` + `validate_inputs` | `{{}}` 值可含指令文本（数据边界靠提示词声明） | P2 |
| 7 | 输入校验 | 必填/默认/多余/JSON 类型 | `engine.validate_inputs` | 约束（范围/正则/枚举）未实现 | P1 |
| 8 | 输出校验 | JSON 解析+声明字段校验 | `engine._run_llm` | 无 JSON Schema 全量校验、无修复环 | P1 |
| 9 | Provider 解耦 | 3 Provider（mock/chat/responses） | `runtime/providers.py` | 无 Anthropic、无 local；能力协商不完整 | P2 |
| 10 | 依赖与组合 | 组合=顺序链+子技能解析+部分回退 | `engine._plan` | 无 DAG 并行/条件分支；无循环预算 | P1 |

## 优先级清单（进入 ROADMAP_2.0）

- P1-A 参数/输出约束引擎（JSON Schema 级）— Sprint 3
- P1-B 执行控制补全：cancel/backoff/修复环/并行 DAG — Sprint 3
- P1-C Builder：IR（任务类型识别）、质量评分、测试用例生成、审核闭环 — Sprint 2
- P1-D 评测扩展：一致性/成本/工具成功率、多模型对比、版本对比门禁、LLM-as-Judge 隔离记录 — Sprint 4
- P1-E 治理：风险分级 L0–L4、脚本扫描、审计脱敏；Registry 检索与打包 — Sprint 5
- P1-F Manifest JSON Schema 导出 + `migrate` 命令 + 版本识别 — Sprint 1
- P2 Provider 扩展（anthropic/local）、CLI 命令补全、indexer/CLI 测试覆盖补齐

## 验收承诺

2.0.0 发布前必须：无未解决 P0；覆盖率 ≥ 80%；旧 YAML 全部可加载
（现有 9 资产 + 8 legacy 为兼容性回归基线）；所有 ✅ 能力有测试证据。
