# 测试与覆盖率审计（历史快照 · v1.2.0 基线 · 2026-11-13）

> **历史文档**：以下为 2.0 立项前基线（106 项测试、71% 覆盖、CLI 0%），非当前状态。当前指标由 CI 生成。

实测（Python 3.14 + MockProvider，全部离线）：**106 项测试，行覆盖 71%**。

## 覆盖率明细（关键项）

| 模块 | 覆盖 | 评价 |
|---|---|---|
| runtime/engine.py | 87% | 强：超时/重试/调度/审批/权限均有用例 |
| runtime/state.py | 98% | 强 |
| schema / __init__ / errors | 98–100% | 强 |
| agentskills / evaluation / converter / validator | 88–95% | 良 |
| manifest | 95% | 良 |
| **runtime/providers** | **55%** | 弱：真实 API 路径仅构造级（合理，但需契约测试桩） |
| **runtime/tools** | **69%** | 中：registry timeout/异常分支缺 |
| **indexer** | **15%** | **弱：v1.2 改写后仅有间接覆盖** |
| **cli/uskills_cli.py** | **0%** | **弱：无任何 CLI 级测试** |

## 缺口与整改（Sprint 0 → 6 的测试任务）

| 缺口 | 严重度 | 整改 |
|---|---|---|
| CLI 无测试 | P1 | `tests/test_cli.py`：subprocess 调 main()，断言退出码与 JSON 输出（validate/schema/index/init/export/run/eval/doctor/search/package/migrate） |
| indexer 改写后覆盖不足 | P1 | `tests/test_indexer.py`：分组/standalone/重复 id/无效文件明细/evals 跳过 |
| ToolRegistry 超时与未知工具 | P2 | test_tools.py：timeout、invoke 未知、重复注册 |
| Providers 契约 | P2 | 用假 client 注入测 OpenAIChat/Responses 的参数与错误分类（不触网） |
| 兼容回归基线 | P1 | `tests/test_compat_v1.py`：加载全部 9 资产 + v1.1 字段子集构造 + 旧→新→旧往返 |
| 安全用例 | P1 | 脚本扫描/风险推导/脱敏（Sprint 5 随功能交付） |
| 评测门禁 | P1 | eval --gate 回归阻断测试（Sprint 4） |
| 目标 | — | **2.0.0 发布门槛：总覆盖 ≥ 80%，CLI ≥ 70%** |

## 既有测试资产

tests/ 共 7 文件 106 用例：validator 16、converter 19、v2 核心 14、runtime 22、
agentskills+manifest 19、executor/ai 7、evaluation 9。全部确定性、离线、可进 CI。
