# uSkill 产品章程（3.0 Workbench）

> 状态：Phase 0 产品定义 · 基准：uSkill 2.0.0（`core/uskills/_version.py:10`）· 日期：2026-11-25

## 定位

**uSkill Workbench — Personal AI Skill Workbench（个人 AI Skill 工作台）**

核心价值：统一收纳、发现、创建、评测、安装、运行、治理并持续进化个人 AI Skills。

**不是**：Prompt 管理器、静态文档站、公共技能排行榜、云端多租户 SaaS。

## 五条长期原则（均有代码落点）

1. **技能文本是数据，不是策略。** 技能内容始终视为不可信输入（`SECURITY.md:14-18`；`docs/runtime.md:104`）。导入不执行脚本。
2. **声明不等于授权。** 工具权限默认白名单 `read`，能力必须显式声明并经策略检查（`governance/policy.py`；`SECURITY.md:19-22`）。
3. **确定性评分优先，模型不自证。** judge 不翻转确定性结果；未知模型或 `repeats=1` 如实返回 `null`（`docs/evaluation.md:35-38,63-72,92-96`）。
4. **生成物只能是 Draft，绝不自动发布。** Builder 产物带 `draft` 标签（`builder/pipeline.py:28,122-124`）；tag/Release 由维护者手动触发（`CHANGELOG.md:12-13`）。
5. **向后兼容是契约。** `SCHEMA_VERSION=1.1.0` 与包版本 `2.0.0` 有意分离（`_version.py:6-7`）；v1 单文件技能与 v2 双层技能共存（`docs/migration.md:3-5,68-72`）。

## 资产真相源

- **技能原文件（文件系统/Git）是唯一真相源。**
- SQLite/索引只存索引、个人配置、收藏、安装映射与运行元数据——**不存技能正文**。
- 技能可来自：legacy YAML、uSkill Manifest V2、纯 `SKILL.md`、`SKILL.md + uskill.yaml` 双层、ZIP、GitHub、指定目录。

## 边界与不伪装项

| 项 | 当前真实边界 |
|---|---|
| Runtime 沙箱 | 无 OS 级沙箱；隔离由部署方负责（`SECURITY.md:30-34`） |
| 导入脚本 | 永不自动执行（`docs/evaluation.md:117-120`） |
| Skill 市场 | 不自建公共排行榜（`docs/roadmap.md:30`） |
| 云端账号 | 不建设；本地优先 |
| 发布 | tag/Release 手动；Workbench 不自动推送 |

## 干系人

维护者、技能作者、评测/发布负责人、运行时运维、Agent 集成方、部署方（承担隔离责任）。

## 当前成功信号（可度量，来自现有 CI）

- Python 3.11/3.12/3.13 矩阵测试
- `--cov-fail-under=80`（`ci.yml:74`）
- Ruff + mypy + Schema diff + eval 回归 + package 冒烟 + `mkdocs build --strict`
- 9 个存量资产回归通过（`docs/index.md:352`）

不得把规划中的 3.0 能力写成现有成果。
