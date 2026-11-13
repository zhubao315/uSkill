# Skill Builder（技能构建）

Builder 把 SOP / Prompt / Markdown / 技能目录等**不可信原始文档**转换为
Draft 状态的技能候选，全过程确定性、有证据、可复核。

```bash
# 从 SOP 构建草稿（不自动发布）
uskills build examples/customer_service_sop.md --output skills/generated-builder

# 查看质量分与 IR 分类后，人工复核草稿
uskills validate skills/generated-builder/drafts
uskills run skills/generated-builder/drafts/<file>.json --input ...   # 试运行
```

## 流水线

```
原始文档 → Importer → 任务 IR → 技能生成 → 质量评分 → Draft 输出
                                        ↘ 评测用例草稿  ↘ build-report.json
```

1. **Importer**（`builder.importer`）：识别 Markdown/文本/Prompt/
   legacy skill-v1/SKILL.md 目录，统一为 `SourceDoc`（不可信数据）。
2. **任务 IR**（`builder.ir`）：步骤语义分类——`atomic` / `decision` /
   `approval` / `loop`，基于中英文标记词的确定性规则，每个分类携带证据。
   审批步会使生成的技能 `requires_approval=true`（运行时人工暂停）。
3. **质量评分**（`builder.quality`）：7 个维度共 100 分，每个得分点附证据；
   **总分 < 70 标记 review_required**。检测内嵌密钥字面量（该项直接归零）。
4. **输出**（`builder.pipeline`）：`drafts/*.json`（可加载可校验）、
   `evals-draft/*.suite.json`（评测用例草稿）、`build-report.json`
   （IR 摘要 + 评分 + 风险提示 + 策略声明）。

## 治理约束

- 所有产物固定为 **Draft 生命周期**并带 `draft` 标签；发布必须走
  Draft → Validated → Reviewed → Published 人审门禁（见治理文档）。
- 步骤分类是启发式规则而非 LLM 判断：输出可复现、可测试、可解释；
  分类为 decision/loop 的步骤会在报告中提示人工确认拆分粒度。
- 生成技能的溯源（`source.sop_path` 等）保留，支持 Skill Genome 式审计。

## Python API

```python
from core.uskills import build_skills  # builder 符号已从顶层导出

report = build_skills("docs/sop.md", "skills/generated-builder", domain="support")
for c in report.candidates:
    print(c.skill.skill_id, c.score.total, c.lifecycle.value)
print(report.any_review_required)
```
