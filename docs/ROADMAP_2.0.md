# ROADMAP 2.0（本任务书执行计划）

定位：uSkill 2.0.0 — Agent Skills Engineering Platform。
基线：v1.2.0（阶段 0-4 大部分已落地，见 docs/audit/*）。
发布纪律：不跳过审计；无证据不称完成；未验证不发 2.0.0。

## Sprint 0 · 审计 ✅（本批文档）

docs/audit/{REPOSITORY,PROJECT,ARCHITECTURE,SECURITY,TEST_COVERAGE,ECOSYSTEM_COMPARISON}.md
→ 全部落地，零代码改动。

## Sprint 1 · 标准体系 ✅

- `standards/manifest/v1|v2/` JSON Schema 导出（`uskills schema --target manifest`）
- `core/uskills/standards_compat.py`：格式识别（legacy yaml / manifest / SKILL.md）、
  字段弃用警告、迁移报告
- `uskills migrate <path>`：旧资产 → V2 Manifest 目录（幂等、不覆盖）
- 兼容测试：1.1 技能可加载/校验/执行

## Sprint 2 · Skill Builder ✅

- `core/uskills/builder/`：统一 Importer（md/txt/yaml/json/SKILL.md/技能目录）
- 中间表示 IR：任务目标/原子步/条件/审批/异常/工具需求识别（规则式，确定性）
- 质量评分（证据型 0–100：目标明确、输入完整、输出可验证、边界、溯源、
  安全、可发现性）+ `uskills build` 产出候选+评分+报告（**不自动发布**）
- 测试用例生成：从 IR 生成 evals/dataset.json 草稿

## Sprint 3 · Runtime 补全 ✅

- Provider：Anthropic + OpenAI-compatible + local（ollama），统一能力声明
- 参数引擎：enum/min/max/pattern/nullable/默认值（Schema 即 JSON Schema）
- 输出：JSON Schema 全量校验 + **有限修复环**（默认 ≤2 次，禁止无限重试）
- 控制：cancel（取消）、指数退避 backoff、副作用工具幂等/审批保护
- Workflow：DAG 依赖（`depends_on`）+ 层内并行（max_workers）+ 循环预算上限
- 测试：cancel/backoff/并行/修复环/幂等全部有用例

## Sprint 4 · Evaluation 扩展 ✅

- 指标扩展：一致性（重复运行）、成本（token×单价表）、工具成功率、延迟
- 模式：多模型矩阵对比、版本对比（--compare）、**发布回归门禁**（--gate：
  未解释退化→非零退出，可阻断 CI）
- LLM-as-Judge：固定 rubric、记录 judge 模型、与确定性结果分开存储
- `tests/evaluation/` 目录 + 3 个真实技能评测集（标记待真实模型运行）

## Sprint 5 · 治理与分发 ✅

- 风险分级 L0–L4（由能力推导：scripts/network/write/approval）
- 导入静态扫描（subprocess/network/eval 等模式 → 报告，不阻断但降级状态）
- 审计脱敏（敏感键掩码、输入存摘要）
- Registry 检索：名称/标签/领域/关键词/依赖 五类搜索（`uskills search`）
- 打包：`uskills package`（zip + checksum + 兼容清单）
- MCP 桥接：MCP 工具 → ToolRegistry 注册的适配器（可选依赖，不触网测试）

## Sprint 6 · 发布 2.0.0

- CI：Python 3.11–3.13 矩阵（3.10 已 EOL，仅文档声明兼容策略）、ruff format
  检查、覆盖率门槛 80%、评测门禁步骤
- CLI 补全：`build/migrate/search/package/test/audit` 与 JSON 输出规范
- 文档：概念/指南/参考/治理 四组；迁移指南；≥5 个可运行示例
- CHANGELOG + tag v2.0.0（**由用户触发发布**，本仓库不自动推送）

## 差异化（记录，不挤占主线）

Skill Genome（溯源/演化谱系：现有 provenance+audit 是雏形）；
Skill Benchmark（Sprint 4 多模型矩阵是其最小形态）；Skill Factory（长期）。
