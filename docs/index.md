---
template: home.html
hide:
  - navigation
  - toc
---

<div class="us-hero" markdown>

<div class="us-hero-inner" markdown>

<div class="us-hero-badge">uSkill 2.0 已发布 · 向后兼容是契约</div>

# Agent <span class="us-grad">技能工程</span>平台

把历史 SOP、Prompt 与专家经验，变成**可构建、可执行、可评测、可治理、可分发**
的标准化技能资产——全流程有产物、有门禁、有证据。

开放标准兼容（Agent Skills）· 受治理运行时 · 证据化评测 · L0–L4 风险分级

<div class="us-hero-ctas" markdown>

[:octicons-rocket-16: 五分钟上手](#start){ .md-button .md-button--primary }
[:material-book-open-page-variant: 阅读文档](quickstart.md){ .md-button }
[:octicons-mark-github-16: GitHub](https://github.com/zhubao315/uSkill){ .md-button us-ghost }

</div>

</div>

<div class="us-term">
<div class="us-term-bar"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span><span class="us-term-title">uskills — 一次真实运行（Mock Provider，无需任何 API Key）</span></div>
<div class="us-term-body"><span class="p">$</span> uskills run content_pipeline --input '{"text":"…","target_lang":"en"}' --library skills

  <span class="ok">✓ COMPLETED</span>  4 steps · 2 DAG levels · 23ms
    ├─ <span class="k">subskill:extract</span>    COMPLETED   <span class="t"># level-1</span>
    ├─ <span class="k">subskill:summarize</span>  COMPLETED   <span class="t"># level-2，与 translate 并行执行</span>
    ├─ <span class="k">subskill:translate</span>  COMPLETED   <span class="t"># level-2</span>
    └─ <span class="k">llm</span>               COMPLETED   <span class="t"># 合成输出，schema 校验通过</span>
    usage: 90 tokens · checkpoint → .uskills/runs/run-b43cc1.json

<span class="p">$</span> uskills eval --skill skills/atomic/text_summarize.yaml --suite …suite.json --compare run.json --gate
  vs previous: <span class="ok">+0.0 pp, regressed=none</span> improved=none   <span class="c"># 回归 → 退出码 1，直接阻断 CI</span>
</div>
</div>

</div>

<div class="us-stats" markdown>

<div class="us-stat"><strong>301</strong><span>项测试，2026-11-26 本地实测全部通过（MockProvider）</span></div>
<div class="us-stat"><strong>80%</strong><span>覆盖率门禁下限（见 ci.yml）；实际百分比以最新 CI 报告为准</span></div>
<div class="us-stat"><strong>6</strong><span>Provider：OpenAI / Anthropic / 兼容网关 / Ollama…</span></div>
<div class="us-stat"><strong>L0–L4</strong><span>风险分级由真实能力推导，不看声明</span></div>

</div>

<div class="us-jump" markdown>

[为什么是技能工程](#why) [核心能力](#capabilities) [生命周期门禁](#lifecycle)
[2.0 新契约](#showcase) [上手路径](#start) [定位与边界](#compare)
[工程质量](#quality) [常见问题](#faq)

</div>

<div class="us-section" id="why" markdown>

<div class="us-eyebrow">WHY · 问题</div>

## Agent 不缺聪明，缺的是工程 { .us-h2 }

 Prompt 满天飞、效果靠玄学、上线没门禁——这三件事，uSkill 用同一套资产模型一次解决。

<div class="us-why" markdown>

<div class="us-why-card" markdown>

### 经验锁在聊天记录里

历史 SOP、客服话术、专家 prompt 散落在文档与个人账号中。换模型、换 Agent
框架、换人，一切从零开始，团队没有可复用的"技能资产"。

<div class="us-fix" markdown>
**Builder** 把 SOP/Prompt 确定性解析为任务 IR 与技能草稿：步骤分类带证据、
7 维质量分、评测用例草稿同步生成。产物固定 **Draft**，发布必经人审。
</div>

</div>

<div class="us-why-card" markdown>

### 执行是个黑盒

超时不生效、失败乱重试、副作用被重复执行、子任务只在 prompt 里"说说而已"。
出了事故，拿不出任何可复盘的证据。

<div class="us-fix" markdown>
**受治理运行时**：`control.timeout/retry` 真实强制、指数退避、副作用工具
`idempotent=false` 永不自动重试、审批暂停可恢复、RunRecord 逐步落盘可审计。
</div>

</div>

<div class="us-why-card" markdown>

### 发布全凭感觉

改一版 prompt，旧用例悄悄翻车没人知道；好坏没有定义，回归没有门禁，
"感觉更好了"就是上线理由。

<div class="us-fix" markdown>
**评测即门禁**：基线对照 + 确定性断言 + 多模型矩阵；`--gate` 下任何一个
此前通过的用例翻车、或成功率跌破阈值 → **退出码 1 阻断 CI**，可复算、可存档。
</div>

</div>

</div>

</div>

<div class="us-section" id="capabilities" markdown>

<div class="us-eyebrow">CAPABILITIES · 能力</div>

## 一套平台，覆盖技能资产全生命周期 { .us-h2 }

不是又一个 Prompt 模板库：每个环节都有强制门禁与可验证产物。

<div class="us-bento" markdown>

<div class="us-cell us-cell--wide" markdown>

<span class="us-ic">:material-robot:</span>

### 受治理运行时

声明即执行：Schema 里的控制字段全部在运行时**真实强制**，不是注释。

- 输入 JSON Schema 约束（`enum` / `minimum` / `pattern` / `nullable`…）在**模型调用前**拦截
- 输出全量 JSON Schema 校验 + 有限修复环（`control.repair`，默认 2，封顶不失控）
- `depends_on` DAG：Kahn 分层、同层并行（`control.max_workers`）、环与未知依赖直接拒绝
- `CancelToken` 协作式取消、`backoff_base` 指数退避（30s 封顶）
- 审批门禁 `WAITING_APPROVAL` → `resume(approve/deny)`，长任务检查点随时恢复
- 未注册的工具声明**执行不了也升不了风险级**：运行时是唯一真相

[运行时文档 →](runtime.md){ .us-cell-link }

</div>

<div class="us-cell us-cell--wide" markdown>

<span class="us-ic">:material-chart-line:</span>

### 证据化评测

回答"这个技能到底有没有用"：与 No-Skill 基线同参对照，评分器是**确定性断言**，
模型不当自己的裁判。

- `task_success_rate` / `output_validity` / `consistency` / 延迟 p95 / 成本（未知模型如实 `null`）
- 多模型矩阵：同一套件 × `--models a,b,c` 一跑出对照表
- **发布回归门禁**：`--compare` + `--gate`，回归即非零退出，直接嵌 CI
- LLM-as-Judge 固定 rubric、隔离存储、**永不翻转**确定性判定
- 3 个随技能版本化的评测集已随仓库发布（含注入探针用例）

[评测文档 →](evaluation.md){ .us-cell-link }

</div>

<div class="us-cell us-cell--half" markdown>

<span class="us-ic">:material-hammer-wrench:</span>

### Skill Builder

SOP / Prompt / 旧技能 → Draft 候选：IR 步骤分类（atomic/decision/approval/loop）
每步带证据；质量分 <70 强制复核；内嵌密钥字面量直接判零分。

[Builder 文档 →](builder.md){ .us-cell-link }

</div>

<div class="us-cell us-cell--half" markdown>

<span class="us-ic">:material-shield-alert:</span>

### 治理与风险分级

L0–L4 **由能力面推导**（可达工具权限、磁盘脚本），不看作者声明；导入含脚本
技能自动静态扫描并写入 manifest；审计日志默认脱敏（掩码 + sha256 摘要）。

[治理文档 →](evaluation.md){ .us-cell-link }

</div>

<div class="us-cell us-cell--half" markdown>

<span class="us-ic">:material-package-variant-closed:</span>

### 检索与分发

本地文件系统即注册中心：五模式检索 + 健康检查；打包为内置逐文件 sha256
清单的 zip，离线可校验。**没有数据库、没有服务端**——这是刻意的设计。

[分发文档 →](distribution.md){ .us-cell-link }

</div>

</div>

</div>

<div class="us-section" id="lifecycle" markdown>

<div class="us-eyebrow">LIFECYCLE · 门禁</div>

## 每个技能状态，都有一道过不去的门 { .us-h2 }

生成技能只能是 Draft——这不是口号，是运行时与 CLI 强制的状态机。

<div class="us-lifecycle" markdown>

<div class="us-lc-step" style="--us-lc:#64748b" markdown>
<strong class="us-t">Draft</strong>
Builder 产物或手写初态。**绝不自动发布**；质量分 <70 或含内嵌密钥会被标记复核。
</div>

<span class="us-lc-arrow">→</span>

<div class="us-lc-step" style="--us-lc:#005FB8" markdown>
<strong class="us-t">Validated</strong>
`uskills validate`：Pydantic + JSON Schema 双栈、模板变量语义检查，错误即失败。
</div>

<span class="us-lc-arrow">→</span>

<div class="us-lc-step" style="--us-lc:#00C2CB" markdown>
<strong class="us-t">Reviewed</strong>
人审门禁：Builder 报告（步骤分类证据 + 7 维评分）供决策，审批记录写入运行审计。
</div>

<span class="us-lc-arrow">→</span>

<div class="us-lc-step" style="--us-lc:#17915c" markdown>
<strong class="us-t">Published</strong>
`uskills package`：zip + 逐文件 sha256 清单 + manifest，离线可校验、可分发。
</div>

<span class="us-lc-arrow">→</span>

<div class="us-lc-step" style="--us-lc:#b3541e" markdown>
<strong class="us-t">Deprecated</strong>
风险重估或业务下线后退役；审计日志与历史 RunRecord 永久可追溯。
</div>

</div>

<p class="us-lc-note">审批不是装饰：<code>WAITING_APPROVAL</code> 状态下运行真实挂起，<code>resume(approve/deny)</code> 之后才继续——审批只是缓解记录，风险等级不因审批而降。</p>

</div>

<div class="us-section" id="showcase" markdown>

<div class="us-eyebrow">CONTRACT · 2.0 新契约</div>

## 写进 YAML 的，运行时都认 { .us-h2 }

2.0 的全部约束字段都是**可选增量**——旧文件照常工作，新文件可以更严格。

<div class="us-show" markdown>

```yaml title="skills/atomic/text_summarize.yaml（节选）"
input:
  params:
    - name: max_length
      type: integer
      minimum: 20                    # 调用前强制：越界直接拒绝，不打模型
      maximum: 1000
    - name: tone
      type: string
      enum: [neutral, formal]        # 非法取值在模型调用前拦截
      nullable: false
execute:
  prompt_template: "请把 {{text}} 压缩为不超过 {{max_length}} 字的摘要"
  depends_on:                        # 组合技能：Kahn 分层 DAG，同层并行
    summarize: []
    translate: [summarize]
control:
  timeout: 15                        # 真实超时：挂起即终止并落盘
  retry: 2                           # 仅幂等工具自动重试（指数退避 ≤30s）
  repair: 2                          # 输出校验失败 → 带错误反馈重问，封顶 2
  max_workers: 4                     # 同层 DAG 并行度
output:
  format: json
  schema:                            # 全量 JSON Schema 校验
    type: object
    required: [summary, key_points]
    properties:
      summary:    {type: string, maxLength: 500}
      key_points: {type: array, minItems: 1, items: {type: string}}
```

<div class="us-show-notes" markdown>

<div class="us-note" markdown>
<strong class="us-t">调用前拦截，而不是事后补救</strong>
参数越界 / 非法枚举直接构造 `FAILED` RunRecord，一次模型调用都不发起——省 token，也堵住注入面。
</div>

<div class="us-note" markdown>
<strong class="us-t">输出校验失败 ≠ 直接崩</strong>
有限修复环把 Schema 错误回灌给模型再问一次（封顶 2 次）；仍失败则如实 `FAILED`，绝不静默放水。
</div>

<div class="us-note" markdown>
<strong class="us-t">DAG 不是画饼</strong>
`depends_on` 经 Kahn 算法分层调度，环依赖 / 引用未定义技能在**校验期**就报错，执行期只跑合法图。
</div>

<div class="us-note" markdown>
<strong class="us-t">副作用有刹车</strong>
工具声明 `idempotent: false`（默认）时失败**永不自动重试**；取消走 `CancelToken` 协作式协议，中断可检查点恢复。
</div>

</div>

</div>

</div>

<div class="us-section" id="start" markdown>

<div class="us-eyebrow">GET STARTED · 上手</div>

## 五步跑通，全程不需要 API Key { .us-h2 }

以下每条命令都在本仓库 CI 中真实执行过（MockProvider 模式下 timeout / 重试 / DAG / 审批全部真实生效）。

<div class="us-steps" markdown>

<div class="us-step" markdown>
### 安装 + 体检
零外部依赖起步，`doctor` 一次检查环境与全部存量资产。
```bash
pip install -e ".[dev]"
uskills doctor
```
</div>

<div class="us-step" markdown>
### 校验并运行存量技能
9/9 存量技能（含 1.x 单文件资产）照常加载与执行。
```bash
uskills validate skills/
uskills run text_summarize \
  --input '{"text":"示例文本","max_length":100}'
```
</div>

<div class="us-step" markdown>
### SOP → Draft 技能
确定性解析 + 质量评分 + 评测用例草稿；产物停在草稿区。
```bash
uskills build examples/customer_service_sop.md \
  --output skills/generated-builder
uskills validate skills/generated-builder/drafts
```
</div>

<div class="us-step" markdown>
### 评测 + 回归门禁
基线对照跑分；`--gate` 下任何翻车直接退出码 1，嵌入 CI。
```bash
SUITE=evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json
uskills eval --skill skills/atomic/text_summarize.yaml \
  --suite $SUITE --mock-response '{"summary":"s","key_points":["k"]}' \
  --format json --output run.json
uskills eval --skill skills/atomic/text_summarize.yaml \
  --suite $SUITE --mock-response '{"summary":"s","key_points":["k"]}' \
  --compare run.json --gate
```
</div>

<div class="us-step" markdown>
### 治理：风险 / 检索 / 打包 / 审计
能力推导风险级；五模式检索；离线可校验包；审计默认脱敏。
```bash
uskills risk skills/ --json
uskills search nlp --mode tag skills/
uskills package skills/agent-skills/code-review --output dist/
uskills run text_summarize --input '{"text":"x"}' --audit audit.jsonl
uskills audit audit.jsonl
```
</div>

<div class="us-step" markdown>
### （可选）1.x 资产迁移双层目录
幂等迁移；无法映射的字段在报告中如实列出，绝不静默丢数据。
```bash
uskills migrate skills/atomic --output skills/migrated --dry-run
```
</div>

</div>

</div>

<div class="us-section" id="compare" markdown>

<div class="us-eyebrow">POSITIONING · 定位</div>

## 它不是什么，就是什么 { .us-h2 }

uSkill 站在 Prompt 实践、Agent 框架与 MCP 之间，负责它们都没管的那段：**技能资产本身**。

<div class="us-compare" markdown>

| 能力 | 裸 Prompt 实践 | Agent 框架 | MCP | uSkill |
|---|:---:|:---:|:---:|:---:|
| 技能成为版本化、可分发的独立资产 | <span class="no">–</span> | <span class="part">部分</span> | <span class="no">–</span> | <span class="yes">✓</span> |
| 输入约束在模型调用前强制 | <span class="no">–</span> | <span class="part">部分</span> | <span class="no">–</span> | <span class="yes">✓</span> |
| 输出 Schema 校验 + 有限修复环 | <span class="no">–</span> | <span class="part">部分</span> | <span class="no">–</span> | <span class="yes">✓</span> |
| 副作用工具永不自动重试 | <span class="no">–</span> | <span class="part">部分</span> | <span class="no">–</span> | <span class="yes">✓</span> |
| 评测基线对照 + 回归门禁阻断 CI | <span class="no">–</span> | <span class="no">–</span> | <span class="no">–</span> | <span class="yes">✓</span> |
| 由能力面推导的风险分级 + 审计脱敏 | <span class="no">–</span> | <span class="part">部分</span> | <span class="part">部分</span> | <span class="yes">✓</span> |
| 离线可校验的技能包 | <span class="no">–</span> | <span class="no">–</span> | <span class="part">部分</span> | <span class="yes">✓</span> |
| 零数据库 / 零服务端 / 零必需 API Key | <span class="yes">✓</span> | <span class="part">部分</span> | <span class="part">部分</span> | <span class="yes">✓</span> |
| 管"外部工具怎么连进来" | <span class="no">–</span> | <span class="part">部分</span> | <span class="yes">✓</span> | <span class="part">桥接</span> |

</div>

<p class="us-lc-note">MCP 解决"连接"，Agent 框架解决"编排"，uSkill 解决"技能该长什么样、怎么被驯服"。三者不冲突：MCP 工具经 ToolRegistry 一处桥接进运行时，默认按 <code>network</code> 权限 + 非幂等待遇受治理。</p>

</div>

<div class="us-section" id="quality" markdown>

<div class="us-eyebrow">EVIDENCE · 工程质量</div>

## 平台自己先过自己的门禁 { .us-h2 }

uSkill 的所有承诺都有对应的自动化证据，且全部可在你的 CI 里复现。

<div class="us-evidence" markdown>

<div class="us-ev" markdown>
<strong class="us-t">301 个测试</strong>
2026-11-26 本地执行 `pytest -q` 实测全部通过；全部离线（MockProvider），无需 API Key。评测集、Builder、运行时、治理、分发每个模块都有针对性用例。
</div>

<div class="us-ev" markdown>
<strong class="us-t">覆盖率门禁 80%</strong>
CI 使用 `--cov-fail-under=80`（见 `ci.yml`），任何下降在合入前暴露；实际百分比以最新 CI 报告为准，本页不写死数字。
</div>

<div class="us-ev" markdown>
<strong class="us-t">三道 CI 门禁</strong>
`ruff check` + `ruff format --check`、覆盖率门禁、评测回归门禁（对比 `evals/reports/*.mock-baseline.json` 基线，翻车即红）。
</div>

<div class="us-ev" markdown>
<strong class="us-t">兼容性矩阵</strong>
Python 3.11–3.13 全版本测试；9/9 存量技能资产每次发布重新校验并执行回归。
</div>

</div>

<p class="us-lc-note">诚实声明：CI 评测基线由 MockProvider 生成，只保证<b>管道与判分的结构回归</b>，不代表真实模型的输出质量；单次重复的 <code>consistency</code> 如实返回 <code>null</code>，未知模型的成本如实为 <code>null</code>。评测数字何时可信，<a href="evaluation.md">评测文档</a>写明了边界。</p>

</div>

<div class="us-section" markdown>

<div class="us-eyebrow">HISTORY · 脉络</div>

## 从 Schema 到工程平台 { .us-h2 }

<dl class="us-timeline">

<dt>v2.0.0<span class="us-ver-date">2026-11</span></dt>
<dd>Agent 技能工程平台：Skill Builder、受治理运行时（约束 / 修复环 / DAG / 取消 / 退避 / 幂等保护）、证据化评测矩阵与发布回归门禁、能力推导风险分级与审计脱敏、注册中心检索 / sha256 打包 / MCP 桥接、覆盖率与评测双 CI 门禁。</dd>

<dt>v1.2.0<span class="us-ver-date">2026-11</span></dt>
<dd>受治理运行时雏形（真实 timeout / retry / 审批 / 检查点）、Agent Skills 开放标准双层兼容（SKILL.md + uskill.yaml）、Manifest V2、评测基线对照、CI 与文档站上线。</dd>

<dt>v1.1.0<span class="us-ver-date">2025</span></dt>
<dd>SOP → 技能转换器、Pydantic V2 Schema、JSON Schema 导出、技能索引与文档站。</dd>

<dt>v0.x<span class="us-ver-date">2025</span></dt>
<dd>uSkill 起点：技能 Schema、校验器与 CLI 骨架。</dd>

</dl>

</div>

<div class="us-section" id="faq" markdown>

<div class="us-eyebrow">FAQ · 常见问题</div>

## 你大概率想问的 { .us-h2 }

<details class="us-faq">
<summary>我已经有 Agent 框架 / 已经在用 MCP，为什么还需要 uSkill？</summary>
<p>Agent 框架管编排、MCP 管连接，但"技能"本身——它的输入契约、输出校验、风险面、评测基线、版本与退役——在两者里都是没有一等公民地位的字符串。uSkill 把这段补成有门禁的资产层，并可把 MCP 工具经 ToolRegistry 桥接进来受同一套治理。</p>
</details>

<details class="us-faq">
<summary>升级到 2.0，我的 1.x 技能文件要改吗？</summary>
<p>不改。全部 2.0 字段都是可选增量，SCHEMA_VERSION 保持 1.1.0，存量技能的加载 / 校验 / 执行是向后兼容契约，CI 每次发布重跑全部存量资产。想用双层目录（SKILL.md + uskill.yaml）时跑一行 <code>uskills migrate --dry-run</code> 先看报告。</p>
</details>

<details class="us-faq">
<summary>没有 API Key 能体验多少？</summary>
<p>几乎全部：doctor / validate / build / run / eval / risk / search / package / audit 在 MockProvider 下都能端到端执行，timeout、重试、DAG 调度、审批挂起、Schema 校验、修复环全部真实生效——被 mock 的只是模型文本本身。接入真实模型时配 6 类 Provider 之一即可。</p>
</details>

<details class="us-faq">
<summary>Builder 生成的技能会被自动发布吗？</summary>
<p>不会，这是硬约束：Builder 产物固定落在 <code>drafts/</code>，报告带 <code>requires_approval</code>；质量分低于 70 强制复核，提示词里含密钥字面量直接判零分。发布必经人工评审。</p>
</details>

<details class="us-faq">
<summary>评测报告显示全绿，能说明模型效果好？</summary>
<p>不能，我们也不假装它能。CI 基线由 MockProvider 生成，守护的是"判分管道没有退化"；确定性断言衡量输出契约合规度，不衡量语义质量。真实效果需要你在自己的评测集上接真实模型跑矩阵——工具和门禁都已就位，数字的解释边界文档里写得很清楚。</p>
</details>

<details class="us-faq">
<summary>要不要装数据库、起服务、租服务器？</summary>
<p>都不需要。本地文件系统就是注册中心，分发是带逐文件 sha256 清单的 zip 包，校验完全离线。这是刻意设计：技能资产应该像代码一样可 diff、可归档、可离线审计，而不是锁在某个控制台后面。</p>
</details>

<details class="us-faq">
<summary>怎么接进我现有的 CI？</summary>
<p>三个命令就是一个门禁链：<code>uskills validate skills/</code> → <code>uskills eval … --compare run.json --gate</code>（回归即退出码 1）→ <code>uskills risk skills/ --json</code>。仓库自带可直接抄的 GitHub Actions 工作流。</p>
</details>

</div>

<div class="us-cta" markdown>

## 让下一份 SOP，成为可驾驭的资产

```bash
pip install -e ".[dev]" && uskills doctor
```

[:octicons-rocket-16: 五分钟上手](#start){ .md-button .md-button--primary }
[:material-book-open-page-variant: 完整文档](quickstart.md){ .md-button us-ghost }
[:octicons-mark-github-16: Star 仓库](https://github.com/zhubao315/uSkill){ .md-button us-ghost }

</div>
