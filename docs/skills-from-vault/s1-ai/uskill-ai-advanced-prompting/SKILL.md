---
name: uskill-ai-advanced-prompting
description: "让Prompt工程进阶变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-advanced-prompting.md"
  original_id: "SKL-6860"
  version: "3.0.0"
  trust: untrusted
---

# Prompt工程进阶

description: |
  当用户需要设计高级 Prompt（CoT、少样本学习、自洽性验证、元提示词）时使用此 Skill。
  触发词包括：'Prompt工程'、'思维链'、'CoT'、'少样本'、'few-shot'、'自洽性'、'元提示词'。
  当用户需要"更高质量的 AI 输出"、"复杂推理任务"、"一致性要求高"时，
  即使未直接说"Prompt工程"，也应使用此 Skill。
  不适用于简单的单轮对话。遇到复杂推理和高质量生成需求时优先使用。

---

# uSkill-901: Prompt工程进阶

## 🎯 目标

> 应用 CoT、少样本学习、自洽性验证等高级 Prompt 技术，提升 AI 输出的质量和一致性。

**核心价值**：从"能用"到"好用"，让 AI 在复杂任务上达到专业水平。

**适用场景**：
- 复杂逻辑推理任务
- 多步骤决策分析
- 需要高一致性的批量生成
- 专业领域问答
- 代码审查与优化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task` | `string` | ✅ | — | 需要 AI 完成的任务描述 |
| `technique` | `enum` | ❌ | `auto` | `cot` / `few_shot` / `self_consistency` / `meta_prompt` / `auto` |
| `complexity` | `enum` | ❌ | `medium` | `simple` / `medium` / `complex` / `expert` |
| `examples` | `array` | ❌ | — | 少样本学习的示例（few_shot 模式必填） |
| `constraints` | `array` | ❌ | `[]` | 输出约束条件 |

**输入约束**：
- `task` 应明确描述期望输出格式
- `complexity=expert` 时建议使用 `self_consistency` 或 `meta_prompt`
- `examples` 每项应包含 input/output 对

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结 Prompt 方案",
  "prompt_id": "PR-YYYY-MMDD-NNN",

  "technique_selection": {
    "recommended": "string",
    "reasoning": "string",
    "alternatives": ["string"]
  },

  "prompt_design": {
    "system_prompt": "string",
    "user_prompt_template": "string",
    "few_shot_examples": [
      {
        "input": "string",
        "output": "string",
        "rationale": "string"
      }
    ],
    "chain_of_thought": {
      "steps": ["string"],
      "verification_checkpoints": ["string"]
    },
    "output_format": "string"
  },

  "validation": {
    "self_consistency": {
      "enabled": "boolean",
      "sample_count": "number",
      "agreement_threshold": "number"
    },
    "edge_cases": ["string"],
    "failure_modes": ["string"]
  },

  "optimization": {
    "token_efficiency": "string",
    "suggested_iterations": "number",
    "ablation_plan": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 任务分析与技术选型

- **输入**：`task`, `complexity`
- **动作**：
  1. 分析任务的推理复杂度
  2. 评估各技术的适用性
  3. 选择最优技术组合
- **输出**：`technique_selection`
- **分支条件**：
  - IF 任务需要多步推理 → 使用 CoT
  - IF 任务需要特定输出格式 → 使用 few_shot
  - IF 需要高一致性 → 使用 self_consistency
  - IF 任务可泛化到多场景 → 使用 meta_prompt
  - ELSE → 根据复杂度自动选择
- **检查点**：✅ 应验证技术选择与任务类型匹配

### Step 2: Prompt 结构设计

- **输入**：`technique_selection`
- **动作**：
  1. 设计 system prompt 定义角色和约束
  2. 设计 user prompt 模板
  3. 准备 few-shot 示例（如需要）
  4. 设计 CoT 步骤链
- **输出**：`prompt_design`
- **分支条件**：
  - IF 使用 CoT → 步骤链必须包含验证检查点
  - IF 使用 few_shot → 示例需覆盖边界情况
  - IF 使用 self_consistency → 设计多样性生成策略
  - IF 使用 meta_prompt → 设计可泛化的模板变量
  - ELSE → 标准 Prompt 结构
- **检查点**：✅ 应验证 Prompt 包含所有必要组件

### Step 3: 自洽性验证设计

- **输入**：`prompt_design`
- **动作**：
  1. 设计多次采样策略
  2. 定义一致性判断标准
  3. 设置验证阈值
- **输出**：`validation`
- **分支条件**：
  - IF 任务需要高精度 → 采样 ≥5 次，阈值 ≥0.8
  - IF 任务允许多样性 → 采样 3 次，阈值 ≥0.6
  - IF 计算预算有限 → 减少采样次数，增加单次质量
  - ELSE → 默认 3 次采样
- **检查点**：✅ 应验证验证策略覆盖主要失败模式

### Step 4: 边界测试与优化

- **输入**：`prompt_design`, `validation`
- **动作**：
  1. 识别潜在边界情况
  2. 设计对抗性测试
  3. 优化 token 效率
- **输出**：`optimization`
- **分支条件**：
  - IF token 使用过高 → 精简 prompt，移除冗余
  - IF 边界测试失败 → 增加约束或示例
  - IF 推理链过长 → 考虑分步拆分
  - ELSE → 保持当前设计
- **检查点**：✅ 应验证优化不损害核心功能

### Step 5: 文档与模板化

- **输入**：所有前序输出
- **动作**：
  1. 整理完整 Prompt 模板
  2. 编写使用说明
  3. 创建可复用的配置
- **输出**：完整 Prompt 工程文档包
- **检查点**：✅ 应验证文档可指导他人复现

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在 Prompt 中泄露敏感信息或系统指令
2. **不得**跳过自洽性验证直接用于生产
3. **必须**为每个 CoT 步骤提供验证检查点
4. **必须**记录 Prompt 版本和性能基准

### 软性约束（建议遵守）
1. 优先使用简单技术，复杂技术作为兜底
2. Prompt 长度不超过模型上下文窗口的 50%
3. 每个 Prompt 附带 ≥3 个测试用例
4. 定期更新示例以保持相关性

### 人工兜底点
- 当 AI 输出涉及医疗、法律、财务建议时，**必须**人工审核
- 当自洽性验证失败率 > 30% 时，**必须**重新设计 Prompt
- 当任务超出模型能力时，**必须**建议升级模型或拆分任务

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `PR_ERROR_LOW_COHERENCE` | 自洽性 < 0.5 | 重新设计 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
