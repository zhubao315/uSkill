# 验收标准（可复算门禁）

> 所有「已实现」结论必须能由下列命令复算。CI 证据来自 `.github/workflows/ci.yml` 精确行号；文档与 Workbench 门禁为新增验收（当前多为**未实现/规划**）。状态：`已实现` / `部分实现` / `未实现` / `需要验证`。

## 1. CI 可复算门禁（已实现，按 ci.yml 行号）

| ID | 门禁 | 精确命令/行号 | 状态 |
|---|---|---|---|
| AC-CI-01 | Lint + 格式 + 类型 | `ruff check .`（`ci.yml:25`）、`ruff format --check .`（`:27`）、`mypy core/ --ignore-missing-imports`（`:29`） | 已实现 |
| AC-CI-02 | Python 矩阵 | `3.11 / 3.12 / 3.13`（`ci.yml:34-37`）；`requires-python >=3.11`（`pyproject.toml:11`） | 已实现 |
| AC-CI-03 | Schema 导出一致 | 两目标导出后 `diff /tmp/skill.json standards/uskill.schema.json` 与 `diff /tmp/manifest.json standards/uskill-manifest.schema.json`（`ci.yml:47-52`） | 已实现 |
| AC-CI-04 | 资产校验 | `uskills validate skills/` + `uskills doctor`（`ci.yml:53-56`） | 已实现 |
| AC-CI-05 | 索引生成 | `uskills index skills --output /tmp/skills-index.md`（`ci.yml:57-59`） | 已实现 |
| AC-CI-06 | 两条 mock 基线 eval --gate | 摘要与翻译各一次 `--mock-response ... --compare evals/reports/*.mock-baseline.json --gate`（`ci.yml:60-72`） | 已实现 |
| AC-CI-07 | 覆盖率 | `pytest --cov=core --cov=cli --cov-report=term --cov-report=xml --cov-fail-under=80`（`ci.yml:73-74`）；3.12 上传 `coverage.xml`（`:75-80`） | 已实现 |
| AC-CI-08 | 打包冒烟 | `python -m build` + `twine check dist/*`（`ci.yml:91-95`）；安装后 `uskills --version`、`uskills doctor`（`:96-100`） | 已实现 |
| AC-CI-09 | 文档严格构建 | `mkdocs build --strict`（`ci.yml:119-120`；Pages 构建另见 `pages.yml:29-34`） | 已实现 |
| AC-CI-10 | 依赖审计 | `pip-audit -r requirements.txt --skip-editable`（`ci.yml:131-135`），但 `continue-on-error: true`（`:125`）且末尾 `|| true`（`:135`）→ **非阻塞** | 部分实现：建议移除 `|| true` 与 `continue-on-error`，改为阻塞 |

门禁细节：`--gate` 语义为任一此前通过用例回归或成功率跌幅 > `--max-drop-pp`（默认 10pp）即退出码 1（`evaluation.py:559-575`、`cli:383-407`）；CI 在 `--gate` 缺 `--compare` 时退出 2（`cli:387-389`）。

## 2. 文档与产品口径门禁（新增）

| ID | 标准 | 状态 |
|---|---|---|
| AC-DOC-01 | 任何当前版本标题不得写「V1.2 / V1.3」；二者只能作历史条目并加历史横幅 | 未实现（`docs/roadmap.md:3,10` 仍用标题；需归档组） |
| AC-DOC-02 | 6 份审计文件（`REPOSITORY/PROJECT/ARCHITECTURE/SECURITY/TEST_COVERAGE/ECOSYSTEM_COMPARISON`）均在导航且带日期/基线横幅（`mkdocs.yml:135-140`） | 已实现/需要验证横幅完整性 |
| AC-DOC-03 | 首页数字必须从生成器重算：`261/90.6%/6/9-of-9`（`docs/index.md:51-52,54,463`）对照 `coverage.xml`、pytest 输出、`docs/generated/skills-index.md:3`（8 技能/7 源）——口径不一致处标「需要验证」 | 未实现 |
| AC-DOC-04 | 必须同时保留 `SCHEMA_VERSION=1.1.0`（`schema.py:23`）、包 `2.0.0`（`_version.py:10`）、`apiVersion uskills/v2`（`manifest.py:24`）；不得混写 | 已实现（源码），文档需持续校验 |
| AC-DOC-05 | 9 个存量资产回归：每次发布重跑加载/校验/执行（`docs/index.md:352,463`；`PROJECT_AUDIT.md:40` 提到 9 资产 + 8 legacy 基线）——实际断言数须可复算 | 需要验证（快照未含 `skills/` 目录） |
| AC-GOV-01 | Builder 输出永不自动发布：产物在 `drafts/`、带 `draft` 标签、生命周期 DRAFT（`builder/pipeline.py:1-5,121-124`）；tag/Release 手动（`ROADMAP_2.0.md:54,60`） | 已实现 |
| AC-GOV-02 | judge 永不翻转确定性结果：独立 `judgments` 段、固定 rubric、记录 judge 模型、失败记 error（`evaluation.py:143-160,190,239-245,581-636`） | 已实现 |
| AC-GOV-03 | 未知模型 `cost_usd=null`、`repeats=1` 时 `consistency=null`、无工具调用 `tool_success_rate=null`（`evaluation.py:42-49,430-434,447,450`；基线 JSON `:12,24`） | 已实现 |
| AC-GOV-04 | 风险由可达能力推导、未注册工具不升级（`risk.py:49-83,96-107`）；审计键掩码 + `{sha256,length}`（`audit.py:19-39`）；MCP 默认 network/idempotent=False（`mcp_bridge.py:11-14,37-40`） | 已实现 |

## 3. Workbench 验收（3.0，未实现）

以下每条均为**规划验收**，当前无 Workbench 源码，不得计入「已实现」：

| ID | 验收点 | 判定方式 |
|---|---|---|
| AC-WB-01 | 本地启动：仅绑定 `127.0.0.1`，无 DB/服务端，启动后可用 | 实际启动进程 + 端口检查 |
| AC-WB-02 | 真实 Registry 加载：调用现有 `SkillRegistry`（`registry.py:47-68`），列表与 `health()` 一致 | 对比 `uskills list/search` 输出 |
| AC-WB-03 | 真实 `SKILL.md` 详情：来自 `inspect_agent_skill`（`agentskills.py:76-91`），不硬编码示例 | 打开详情与源文件逐字段比对 |
| AC-WB-04 | 真实安装预览：展示目标路径与风险/脚本扫描（`scan.py:75-110`），不执行脚本 | 预览与 `import_agent_skill` notes 一致 |
| AC-WB-05 | 真实 RunStore 历史：来自 `.uskills/runs/<run_id>.json`（`state.py:163-184`），与 `inspect_run` 一致 | 触发一次 `run` 后刷新 |
| AC-WB-06 | 无敏感数据泄漏：前端/API 不出现密钥、审计只看脱敏结果（`audit.py:19-39`）；本地 API 需配对 token/Origin 白名单/CSRF | 注入探针 + 抓包检查 |
| AC-WB-07 | 状态 survives refresh：收藏/安装/预览等状态持久化后刷新不丢 | 刷新前后对比 |
| AC-WB-08 | 明暗主题：`mkdocs.yml:31-46` 的 palette 语义延伸至 Workbench | 双主题切换检查 |
| AC-WB-09 | 桌面/移动端响应式 | 两种视口检查 |
| AC-WB-10 | 真实 loading/error 态：加载失败、运行失败、eval 回归失败均显示真实错误文案，不展示假数据 | 断网/坏文件注入 |

## 4. 门禁适用顺序

1. 先跑 AC-CI-01…10（现有 CI 即可复算）；
2. 文档改动追加 AC-DOC-01…05 与 AC-GOV-01…04；
3. 仅当 Phase 0–3 退出条件满足（`ROADMAP_3.0.md` §2），才启动 Workbench MVP 的 AC-WB-01…10；
4. 任何 AC 失败不得标「已实现」，只可标「部分实现」或「未实现/需要验证」。
