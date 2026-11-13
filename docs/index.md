---
template: home.html
hide:
  - navigation
  - toc
---

<div class="hero-v2" markdown>

<div class="hero-v2-copy" markdown>

# uSkill 2.0

**Agent 技能工程平台** —— 以驾驭工程为方法论，把历史 SOP、Prompt 与专家经验，
转换为**可构建、可执行、可评测、可治理、可分发**的标准化技能资产。

开放标准兼容 · 受治理运行时 · 证据化评测 · 全链路零 API Key 可验证

```bash
pip install -e ".[dev]" && uskills doctor
```

[:octicons-rocket-16: 快速开始](quickstart.md){ .md-button .md-button--primary }
[:material-map: 从 1.x 迁移](migration.md){ .md-button .md-button--accent }
[:octicons-mark-github-16: GitHub](https://github.com/zhubao315/uSkill){ .md-button }

</div>

<div class="hero-v2-term" markdown>

```text
$ uskills run content_pipeline \
    --input '{"text":"…","target_lang":"en"}' --library skills

  ✓ run_2f7c3a  COMPLETED  (3 sub-skills · 2 levels · 41ms)
    ├─ extract      COMPLETED   12ms
    ├─ summarize    COMPLETED   14ms   ⊐ 与 translate 并行
    ├─ translate    COMPLETED   13ms
    └─ llm          COMPLETED   2ms
  usage: 87 tokens · checkpoint → .uskills/runs/run_2f7c3a.json
```

</div>

</div>

<div class="stats-strip" markdown>

<div class="stat"><strong>261</strong><span>回归测试</span></div>
<div class="stat"><strong>90%+</strong><span>覆盖率门禁</span></div>
<div class="stat"><strong>6</strong><span>Provider 适配</span></div>
<div class="stat"><strong>L0–L4</strong><span>风险分级</span></div>
<div class="stat"><strong>3.11+</strong><span>Python</span></div>
<div class="stat"><strong>0</strong><span>必需 API Key</span></div>

</div>

## 一条工程闭环

从原始文档到跨 Agent 复用，六个环节全部有产物、有门禁、有证据：

<div class="pipeline" markdown>

**构建**<br>Builder 把 SOP/Prompt 解析为任务 IR，产物固定 Draft

→

**校验**<br>Pydantic + JSON Schema 双栈校验，格式可迁移可导出

→

**执行**<br>timeout / retry / DAG / 取消 / 审批真实强制

→

**评测**<br>基线对照 + 确定性断言 + 回归门禁

→

**治理**<br>能力推导风险分级 + 导入扫描 + 审计脱敏

→

**分发**<br>可校验包 + 五模式检索 + MCP 桥接

</div>

## 2.0 带来了什么

<div class="grid" markdown>

<div class="card" markdown>

:material-robot:{ .icon }

### 受治理运行时

参数 JSON Schema 约束（enum / 范围 / pattern / nullable）在**模型调用前**强制；
输出全量 Schema 校验 + **有限修复环**；组合技能支持 `depends_on` DAG 分层并行、
协作式取消、指数退避；副作用工具（`idempotent=false`）**永不自动重试**。

[运行时详解 →](runtime.md)

</div>

<div class="card" markdown>

:material-hammer-wrench:{ .icon }

### Skill Builder

SOP / Prompt / Markdown / 旧技能 → Draft 技能候选：确定性步骤分类
（atomic / decision / approval / loop，每步带证据）、7 维质量评分（证据可查，
<70 强制复核）、内嵌密钥直接判零分。**生成技能永远停在 Draft**，发布必经人审。

[Builder 详解 →](builder.md)

</div>

<div class="card" markdown>

:material-chart-line:{ .icon }

### 证据化评测

No-Skill 基线对照、任务成功率 / 有效性 / 一致性 / 延迟 / 成本（未知模型如实
`null`）、多模型矩阵；**发布回归门禁**：此前通过的用例翻车或成功率跌破阈值
→ 退出码 1，直接嵌入 CI。LLM-as-Judge 隔离记录，只作参考，从不翻转判定。

[评测详解 →](evaluation.md)

</div>

<div class="card" markdown>

:material-shield-alert:{ .icon }

### 能力推导的风险分级

风险等级 L0–L4 不看作者声明，只看**真实能力面**：可解析工具的权限、磁盘上的
脚本、网络与敏感数据面。未注册的工具声明不升级——运行时根本执行不了它。
导入含脚本技能自动静态扫描并写入 manifest；审计日志默认脱敏。

[治理与风险 →](evaluation.md)

</div>

<div class="card" markdown>

:material-package-variant-closed:{ .icon }

### 轻量分发

本地文件系统即注册中心：五模式检索（name / tag / domain / keyword /
dependency）+ 健康检查；技能打包为内置逐文件 sha256 清单的 zip，**离线可校验**。
没有数据库、没有服务端、没有 Web 控制台——这是刻意的。

[检索与打包 →](distribution.md)

</div>

<div class="card" markdown>

:material-open-source-initiative:{ .icon }

### 开放标准，不造轮子

兼容 Agent Skills 开放规范（`SKILL.md` + `uskill.yaml` 双层，导入导出不改标准
层）；**MCP ≠ Skill**：MCP 管连接，Skill 管怎么做，桥接只发生在受治理的
ToolRegistry 一处，默认 `network` 权限 + 非幂等。

[标准与桥接 →](agent-skills.md)

</div>

</div>

## 向后兼容是契约

**你的 1.x 技能文件不需要任何修改。** 2.0 的全部格式变更都是可选增量字段
（`SCHEMA_VERSION` 保持 1.1.0），存量技能照常加载、校验、执行；CI 每次发布都
重跑全部存量资产。新能力按需启用，一行 `uskills migrate` 可迁移到双层目录。

[迁移指南 →](migration.md){ .md-button .md-button--primary }
[CLI 全命令参考 →](cli.md){ .md-button }

## 五分钟，全程离线

=== "体检 + 运行"

    ```bash
    uskills doctor                    # 环境 + 全部存量资产体检
    uskills validate skills/          # 9/9 存量技能（含 1.x 资产）

    # 无 API Key 运行（MockProvider），超时/重试/DAG 全部真实执行
    uskills run text_summarize --input '{"text":"示例文本","max_length":100}'
    uskills run content_pipeline --input '{"text":"…","target_lang":"en"}' --library skills
    ```

=== "构建 + 迁移"

    ```bash
    # SOP → Draft 候选（质量分 + 评测用例草稿，绝不自动发布）
    uskills build examples/customer_service_sop.md --output skills/generated-builder
    uskills validate skills/generated-builder/drafts

    # 1.x 单文件 → 标准双层目录（幂等，不可表达字段如实列出）
    uskills migrate skills/atomic --output skills/migrated --dry-run
    ```

=== "评测门禁"

    ```bash
    SUITE=evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json
    MOCK='{"summary":"s","key_points":["k"]}'

    uskills eval --skill skills/atomic/text_summarize.yaml \
      --suite $SUITE --mock-response "$MOCK" --format json --output run.json
    # 回归（此前通过的用例翻车 / 成功率跌破阈值）→ 退出码 1，可阻断 CI
    uskills eval --skill skills/atomic/text_summarize.yaml \
      --suite $SUITE --mock-response "$MOCK" --compare run.json --gate
    ```

=== "治理 + 分发"

    ```bash
    uskills risk skills/ --json                 # 能力推导 L0–L4（不看声明）
    uskills search nlp --mode tag skills/       # 五模式元数据检索
    uskills search text_summarize --mode dependency skills/
    uskills package skills/agent-skills/code-review --output dist/
    uskills run text_summarize --input '{"text":"x"}' --audit audit.jsonl
    uskills audit audit.jsonl                   # 敏感值已掩码/摘要
    ```

## 一个技能长什么样

2.0 的约束字段全部可选——旧文件照常工作，新文件可以更严格：

```yaml title="带 2.0 约束的技能片段"
input:
  params:
    - name: priority
      type: string
      enum: [low, medium, high]      # 模型调用前强制
    - name: max_length
      type: integer
      minimum: 20
      maximum: 1000
execute:
  prompt_template: "请把 {{text}} 压缩为不超过 {{max_length}} 字的摘要"
  depends_on: {}                     # 组合技能可声明 DAG 依赖
output:
  format: json
  schema:                            # 全量 JSON Schema 校验 + 有限修复环
    type: object
    required: [summary, key_points]
    properties:
      summary: {type: string, maxLength: 500}
      key_points: {type: array, minItems: 1, items: {type: string}}
control:
  timeout: 15
  retry: 2
  repair: 2                          # 校验失败带错误反馈重问，封顶 2 次
```

## 版本脉络

<div class="timeline" markdown>

**v2.0.0** · 2026-11
:   Agent 技能工程平台：Builder、约束运行时（DAG / 取消 / 退避 / 修复环）、
    评测矩阵与发布门禁、风险分级与审计脱敏、检索 / 打包 / MCP 桥接、
    覆盖率与评测双 CI 门禁。

**v1.2.0** · 2026-11
:   受治理运行时雏形（真实 timeout / retry / 审批 / 检查点）、Agent Skills
    开放标准双层兼容、Manifest V2、评测基线对照、CI 与文档站。

**v1.1.0** · 2025
:   SOP → 技能转换器、Pydantic V2 Schema、JSON Schema 导出、技能索引与文档站。

**v0.x** · 2025
:   uSkill 起点：技能 Schema、校验器与 CLI 骨架。

</div>

## 开始使用

<div class="grid" markdown>

<div class="card" markdown>

### 十分钟上手

从安装到跑通第一个受治理运行，全程无需 API Key。

[:octicons-rocket-16: 快速开始](quickstart.md){ .md-button .md-button--primary }

</div>

<div class="card" markdown>

### 升级不停摆

存量技能零修改；新能力全部可选启用，迁移报告不隐瞒任何损失。

[:material-map: 迁移指南](migration.md){ .md-button .md-button--accent }

</div>

<div class="card" markdown>

### 参与共建

代码、文档、技能资产、发布流程全部开源在 GitHub。

[:octicons-mark-github-16: 访问仓库](https://github.com/zhubao315/uSkill){ .md-button }

</div>

</div>

---

<div style="text-align: center; color: var(--md-default-fg-color--lighter); padding: 2rem 0;">

Made with :material-heart:{ style="color: #FF8C00;" } by [zhubao315](https://github.com/zhubao315) · uSkill 2.0.0

</div>
