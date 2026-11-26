---
name: uskill-agent-meta-manage-prompt-lifecycle
description: "让meta manage prompt lifecycle变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-manage-prompt-lifecycle.md"
  original_id: "SKL-6895"
  version: "3.0.0"
  trust: untrusted
---

# meta manage prompt lifecycle

# Prompt Lifecycle Management

## 🎯 目标
> 工业级提示词全生命周期管理：从构思设计、原型调试、系统化测试到归档版本化，将单个高质量Prompt开发周期缩短70%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | enum | ✅ | `design` / `prototype` / `test` / `optimize` / `archive` — 生命周期阶段 |
| `prompt_goal` | string | ✅ | 提示词要解决的核心问题描述 |
| `target_model` | string | ❌ | 目标模型（如 `claude-3.5` / `gpt-4o` / `llama3`），默认 `auto` |
| `existing_prompt` | string | ❌ | 已有的提示词文本（用于优化/测试阶段） |
| `test_cases` | array | ❌ | `[{input: "string", expected: "string", scenario: "typical|edge|stress|adversarial"}]` — 测试用例 |
| `rubric` | object | ❌ | `{criteria: [{name: "string", weight: "number", description: "string"}]}` — 评分标准 |
| `cross_model_targets` | array | ❌ | `["string"]` — 跨模型测试目标列表 |

## 📤 输出

### design 阶段输出
```json
{
  "action": "design",
  "prompt_template": "string — 结构化提示词模板（含 {{variable}} 变量）",
  "persona": "string — AI角色设定",
  "framework_used": "CRISPE | CO-STAR | custom",
  "design_rationale": "string — 设计思路说明",
  "variables": [{"name": "string", "type": "string", "required": "boolean", "description": "string"}]
}
```

### prototype 阶段输出
```json
{
  "action": "prototype",
  "prompt_v1": "string — v1.0提示词全文",
  "test_results": [{"run": "int", "input": "string", "output": "string", "pass": "boolean", "issue": "string|null"}],
  "pass_rate_pct": "number",
  "iteration_log": [{"version": "string", "change": "string", "reason": "string"}]
}
```

### test 阶段输出
```json
{
  "action": "test",
  "test_plan": {"total_cases": "int", "typical": "int", "edge": "int", "stress": "int", "adversarial": "int"},
  "ab_test_results": [
    {"variant": "string", "avg_score": "number", "pass_rate_pct": "number", "strengths": ["string"], "weaknesses": ["string"]}
  ],
  "cross_model_results": [
    {"model": "string", "avg_score": "number", "pass_rate_pct": "number", "latency_ms": "number", "token_cost": "number"}
  ],
  "evaluation": {
    "ai_evaluation": {"avg_score": "number", "criteria_scores": [{"criterion": "string", "score": "number"}]},
    "human_evaluation": {"avg_score": "number", "notes": "string"}
  },
  "best_variant": "string — 表现最佳的变体标识"
}
```

### optimize 阶段输出
```json
{
  "action": "optimize",
  "final_prompt": "string — 精炼后的最终版提示词",
  "version": "string — 正式版本号",
  "changelog": ["string — 本次优化变更条目"],
  "performance_delta": {"pass_rate_before": "number", "pass_rate_after": "number", "score_before": "number", "score_after": "number"},
  "inline_comments": "string — 含代码级注释的提示词"
}
```

### archive 阶段输出
```json
{
  "action": "archive",
  "asset_id": "string — 归档资产ID",
  "file_path": "string — 归档路径",
  "tags": ["string"],
  "version_history": [{"version": "string", "date": "string", "change": "string"}],
  "metadata": {"author": "string", "created": "string", "last_tested": "string", "recommended_model": "string"}
}
```

## 📋 执行步骤

### 阶段一：构思与设计 (action=design)
1. **定义目标** — 明确提示词解决的核心问题、目标用户、预期输出格式和业务价值
2. **角色设定** — 为AI设定清晰专业的Persona（如"资深投资分析师"、"苛刻技术总监"）
3. **结构设计** — 采用CRISPE框架（Capacity/Role/Insight/Statement/Personality/Experiment），明确上下文、任务指令、约束条件、输出格式
4. **AI辅助构思** — 让AI扮演"世界顶级提示词工程师兼认知心理学家"，优化结构设计，减少AI认知负荷

### 阶段二：原型与调试 (action=prototype)
5. **撰写v1.0** — 输出完整提示词并录入平台
6. **快速测试** — 在主要模型上执行3-5次，检查基本功能
7. **失败分析** — 判断是指令不清、上下文缺失还是模型理解偏差
8. **迭代修复** — 快速修复明显问题直到v1.x可用（通过率≥70%）

### 阶段三：系统化测试 (action=test)
9. **设计测试方案** — 生成10个测试用例：3典型+3边缘+2压力+2对抗性场景
10. **A/B测试** — 对不同措辞/约束顺序的变体进行量化对比
11. **跨模型测试** — 在 `cross_model_targets` 列表中的模型上运行，评估通用性和鲁棒性
12. **AI辅助评估** — 用独立模型按 `rubric` 对输出打分（1-10分）
13. **人工评估** — 对关键结果进行准确性/创造性/实用性人工打分

### 阶段四：优化与定版 (action=optimize)
14. **选定基准** — 选择测试中表现最佳的变体作为基准版本
15. **精炼吸收** — 吸收各变体优点，修复残留缺陷
16. **代码级注释** — 为关键指令添加注释解释设计目的
17. **正式发布** — 命名正式版（如v2.0），更新平台状态

### 阶段五：归档与版本管理 (action=archive)
18. **资产归档** — 将提示词文档和测试报告归档到平台/知识库
19. **版本标记** — 建立语义化版本号，重大修改创建新版本+Changelog
20. **标签索引** — 打标签（如#工作 #报告生成 #代码辅助）方便检索复用

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `prompt_goal` 过于模糊 | 返回 `ERROR_VAGUE_GOAL` + 澄清问题清单（目标用户？输出格式？核心约束？） |
| `action=test` 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
