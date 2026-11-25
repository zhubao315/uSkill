# 信息架构（IA）

> 现状基准：`mkdocs.yml`（`mkdocs.yml:114-140`）、`docs/index.md`、`docs/overrides/home.html`。3.0 Workbench 的 `workbench/` 分组为**规划**（未实现）。所有数字必须由生成器产出，不得手写（验收 AC-DOC-03）。

## 1. 当前导航分组（已实现）

`mkdocs.yml:114-140` 共六组：

| 组 | 条目 | 行号 |
|---|---|---|
| 首页 | `index.md` | `:115` |
| 入门 | `quickstart.md`、`migration.md` | `:116-118` |
| 概念与架构 | `architecture.md`、`schema.md`、`agent-skills.md`、`builder.md`、`runtime.md` | `:119-124` |
| 指南 | `evaluation.md`、`distribution.md`、`skills.md`、`skill-creator-case.md`、`generated/skills-index.md` | `:125-130` |
| 参考 | `cli.md`、`roadmap.md`、`ROADMAP_2.0.md` | `:131-134` |
| 审计报告 | 6 份 `audit/*.md` | `:135-140` |

主题覆盖目录 `custom_dir: docs/overrides`（`mkdocs.yml:8-11`）；明暗双 palette（`:31-46`）；CJK 锚点与 `indexer.py:_anchor()` 共用 `slugify_unicode`（`mkdocs.yml:78-82`、`indexer.py:71-80`）。导航分组为 已实现；6 份审计文件的「历史横幅完整性」为 部分实现（抬头日期存在，是否明确「非当前版本」需要验证）。验收 AC-CI-09、AC-DOC-02。

## 2. 落地页锚点（已实现）

`docs/index.md` 的 8 个锚点：`#why`（`:66`）、`#capabilities`（`:122`）、`#lifecycle`（`:213`）、`#showcase`（`:262`）、`#start`（`:331`）、`#compare`（`:408`）、`#quality`（`:436`）、`#faq`（`:496`）；跳转条在 `:58-64`。frontmatter `template: home.html`（`index.md:1-6`）触发 `home.html` override：继承 `main.html`、加宽 `.md-content--home`、去掉页间导航（`docs/overrides/home.html:1-18`）。

数据注意：`index.md:51-54` 的「261 测试 / 90.6% 覆盖率 / 6 Provider」与 `:463` 的「9/9 存量资产」是**展示值**；验收必须由 `coverage.xml`/pytest 与生成器重算（AC-DOC-03）。`docs/generated/skills-index.md:3` 由生成器写出的是「8 个技能 / 7 个源」，与落地页「9/9」**需要验证**（可能是资产集口径不同或展示值滞后）。

## 3. 术语与版本三元（已实现）

| 术语 | 含义 | 证据 |
|---|---|---|
| uSkill | 项目/平台名（仓库 `zhubao315/uSkill`） | `pyproject.toml:55-59`、`mkdocs.yml:1-5` |
| `uskills` | Python 包与 CLI 主命令 | `pyproject.toml:6,62` |
| `uskill` | CLI 别名（同一入口），非另一产品 | `pyproject.toml:63`、`REPOSITORY_AUDIT.md:20` |
| skill / 技能 | V1 单文件或 V2 双层目录 | `docs/schema.md:30-36` |

版本三元**必须区分**：包版本 `2.0.0`（`_version.py:10`，`pyproject.toml:69-70`）；技能文件格式 `SCHEMA_VERSION=1.1.0`（`schema.py:8-10,23`，新增字段可选故不 bump）；Manifest `apiVersion: uskills/v2`（`manifest.py:24-25,130-131`）。`docs/migration.md:68-72` 已明确三者语义。验收 AC-DOC-04：禁止把 V1.2/V1.3 写成当前版本标题。

## 4. 产物归属（真相源唯一）

| 产物 | 归属/生成者 | 证据 | 状态 |
|---|---|---|---|
| `standards/uskill.schema.json`（V1） | `exported_json_schema()`；CI diff 强制 | `schema.py:351-363`、`cli:82-91`、`ci.yml:47-52` | 已实现 |
| `standards/uskill-manifest.schema.json`（V2） | `manifest_json_schema()`；CI diff 强制 | `standards_compat.py:40-45`、`cli:92-98`、`ci.yml:49-52` | 已实现 |
| `docs/generated/skills-index.md` | `indexer.build_skills_index()`；Pages 构建时再生成 | `indexer.py:92-158`、`pages.yml:29-33`、`cli:727-731` | 已实现（提交版是否由生成器产出**需要验证**） |
| `evals/reports/*.mock-baseline.json` | CI 回归门禁读取的确定性基线；`ci.yml:60-72` 两次 `eval --compare --gate` | `ci.yml:60-72`、`evals/reports/README.md:1-9` | 已实现（真实模型分数另存，不伪造） |
| `coverage.xml` | `pytest --cov` 产物，仅 3.12 上传 | `ci.yml:73-80` | 已实现 |

原则：技能文件（文件系统/Git）是唯一真相源；索引、配置、运行元数据只是派生数据（`PRODUCT_CHARTER.md:21-25`）。

## 5. 新分组规则（规划，未实现）

- **Workbench 组**：建议顶层新增「工作台」或挂于「指南」下，收录 Workbench 3.0 的安装、Registry、收藏、运行历史、评审页面；每个页面必须标注数据来自现有命令/Runtime 还是 3.0 新实体，未实现处写「未实现」。新增后必须通过 `mkdocs build --strict`（AC-CI-09），且不产生第二份技能真相（AC-DOC-03）。
- **历史归档组**：V1.2/V1.3 的 roadmap 标题与过期审计结论移入「归档」组，并加历史横幅（基线日期 + 「非当前版本」）；原文件保留以免断链，锚点迁移需兼容 `slugify_unicode`（`mkdocs.yml:78-82`）。6 份审计文件当前已在导航末组（`mkdocs.yml:135-140`），均带日期/基线抬头（`REPOSITORY_AUDIT.md:3`、`PROJECT_AUDIT.md:3`、`ARCHITECTURE_AUDIT.md:1`、`SECURITY_AUDIT.md:1-4`、`TEST_COVERAGE_AUDIT.md:3`、`ECOSYSTEM_COMPARISON.md:1-4`）——验收 AC-DOC-02。
- **数字规则**：任何展示数字必须可追溯到生成器/门禁输出；无生成器的数字只能标「需要验证」或从页面移除。

验收总表见 `ACCEPTANCE_CRITERIA.md`：AC-DOC-01…05、AC-CI-09。
