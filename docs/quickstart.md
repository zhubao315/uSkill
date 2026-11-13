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

# 7. 评测：技能 vs 无技能基线
uskills eval --skill skills/atomic/code_review.yaml \
  --suite skills/agent-skills/code-review/evals/dataset.json
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
