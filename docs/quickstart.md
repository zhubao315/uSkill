# 快速开始

## 安装

```bash
# 开发安装（含测试与工具链，Python >= 3.11）
pip install -e ".[dev]"

# 运行时最小安装（模型能力为可选 extras）
pip install -e ".[llm]"      # OpenAI / 兼容网关
```

安装后可直接使用 `uskills`（或别名 `uskill`）命令。

## 五分钟体验

```bash
# 1. 体检：环境 + 全部技能资产
uskills doctor

# 2. 校验（legacy YAML 与双层 Agent Skill 目录都支持）
uskills validate skills/

# 3. 无 API Key 运行一个技能（Mock Provider）
uskills run text_summarize --input '{"text":"示例文本","max_length":100}'

# 4. 组合技能真实调度子技能（不是 prompt 里"说说而已"）
uskills run content_pipeline --input '{"text":"示例文本","target_lang":"en"}' --library skills

# 5. SOP 转技能（标题/约束/嵌套细节全部保留）
uskills convert examples/customer_service_sop.md --output skills/generated

# 6. 创建标准双层技能
uskills init my-skill
uskills validate my-skill/

# 7. 评测：技能 vs 无技能基线（确定性 mock，无需 API Key）
uskills eval --skill skills/atomic/text_summarize.yaml \
  --suite evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json \
  --mock-response '{"summary": "s", "key_points": ["k"]}'
```

## 2.0 新能力速览（全部可离线复跑）

```bash
# SOP/Prompt → Draft 技能候选 + 质量分 + 评测用例草稿（绝不自动发布）
uskills build examples/customer_service_sop.md --output /tmp/my-build
uskills validate /tmp/my-build/drafts

# legacy 单文件 → 标准双层技能目录（幂等；--dry-run 先看不可表达字段）
uskills migrate skills/atomic --output /tmp/my-migrated --dry-run

# 元数据检索（name/tag/domain/keyword/dependency 五种模式）
uskills search nlp --mode tag skills/
uskills search text_summarize --mode dependency skills/   # 谁依赖它

# 由真实能力推导风险级别（未注册的工具声明不升级）
uskills risk skills/ --json

# 可校验分发包：zip 内置逐文件 sha256 的 package.json
uskills package skills/agent-skills/code-review --output /tmp/dist

# 发布回归门禁：先存档，再对比；回归 → 退出码 1（可阻断 CI）
uskills eval --skill skills/atomic/text_summarize.yaml \
  --suite evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json \
  --mock-response '{"summary": "s", "key_points": ["k"]}' \
  --format json --output /tmp/eval-run.json
uskills eval --skill skills/atomic/text_summarize.yaml \
  --suite evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json \
  --mock-response '{"summary": "s", "key_points": ["k"]}' \
  --compare /tmp/eval-run.json --gate

# 多模型对比矩阵（真实 Provider 时；模型名换进 --models 即可）
uskills eval --skill skills/atomic/text_summarize.yaml \
  --suite evals/datasets/uskill-atomic-text-summarize-v1-1-0.suite.json \
  --models gpt-4o-mini,claude-sonnet-4-5 --provider openai-chat

# 运行审计轨迹：run 时落盘，audit 时脱敏展示
uskills run text_summarize --input '{"text":"示例文本"}' --audit /tmp/audit.jsonl
uskills audit /tmp/audit.jsonl          # 敏感键已掩码、大块值已摘要化
```

## 典型流程（资产化）

1. 导入历史 SOP 文本 → `uskills convert`
2. 人工微调元数据与 `source.context` 溯源 → `uskills validate`
3. 补充 `evals/dataset.json` → `uskills eval`
4. 双层化：`uskills export-skill` 生成标准 SKILL.md 目录
5. 走生命周期门禁 Draft → Validated → Reviewed → Published（见[评测与治理](evaluation.md)）

## 测试

```bash
pytest                      # 全部基于 MockProvider，无需任何 API Key
ruff check . && mypy core/
mkdocs build --strict
```
