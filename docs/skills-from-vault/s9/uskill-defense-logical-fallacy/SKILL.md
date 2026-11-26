---
name: uskill-defense-logical-fallacy
description: "让逻辑谬误检测变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-defense-logical-fallacy.md"
  original_id: "SKL-5103"
  version: "3.0.0"
  trust: untrusted
---

# 逻辑谬误检测

⚙️ AI-Co 运行配置块
触发场景: 用户说'逻辑谬误'、'论证分析'、'推理错误'、'稻草人'、'滑坡谬误'
复用率预估: 高
一键调用: |
  论证解析→20种谬误扫描→质量评估→论证重构
输入Schema: argument: string(≥30字), argument_type: deductive|inductive|abductive|unknown, depth: quick|standard|deep, context: {domain, purpose, audience}
输出Schema: argument_analysis, fallacy_detection{total_detected, fallacies[]}, logical_quality{score, grade}, reconstruction{original, corrected}
AI可执行度: 100%

description: |
  当用户需要检测论证中的逻辑谬误、分析论证结构、评估推理有效性时使用此 Skill。
  触发词包括：'逻辑谬误'、'论证分析'、'推理错误'、'逻辑错误'、'谬误检测'、
  '稻草人'、'滑坡谬误'、'诉诸权威'。当用户讨论辩论、学术论文、政策分析、
  投资逻辑时，即使未直接说"逻辑谬误"，也应使用此 Skill。
  不适用于数值计算错误或事实错误（使用信息污染检测）。遇到逻辑分析需求时优先使用。

---

# uSkill-103: 逻辑谬误检测

## 🎯 目标

> 系统化检测 20+ 种常见逻辑谬误，帮助用户识别论证中的推理漏洞，提升批判性思维能力。

**核心价值**：在复杂论证中快速定位逻辑漏洞，避免被似是而非的推理误导。

**适用场景**：
- 学术论文评审
- 政策辩论分析
- 投资逻辑验证
- 法律论证评估
- 日常争论分析

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `argument` | `string` | ✅ | — | 待检测的论证内容 |
| `argument_type` | `enum` | ❌ | `unknown` | `deductive` / `inductive` / `abductive` / `unknown` |
| `depth` | `enum` | ❌ | `standard` | `quick` / `standard` / `deep` |
| `context` | `object` | ❌ | — | `{domain, purpose, audience}` |

**输入约束**：
- `argument` 必须为非空字符串（最少 30 字）
- `depth = deep` 时执行完整 20+ 谬误类型检测

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话逻辑评估结论",
  "fallacy_id": "LF-YYYY-MMDD-NNN",

  "argument_analysis": {
    "structure_valid": true,
    "premises_count": "number",
    "conclusion_identified": "string",
    "argument_type": "deductive|inductive|abductive"
  },

  "fallacy_detection": {
    "total_detected": 0,
    "fallacies": [
      {
        "type": "string",
        "name": "string",
        "description": "string",
        "location": "string — 谬误在原文中的位置",
        "evidence": "string",
        "severity": "low|medium|high",
        "counter_argument": "string"
      }
    ]
  },

  "logical_quality": {
    "score": "number — 0-100",
    "grade": "A|B|C|D|F",
    "strengths": ["string"],
    "weaknesses": ["string"],
    "recommendation": "string"
  },

  "reconstruction": {
    "original": "string",
    "corrected": "string",
    "improvement_notes": "string"
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

### Step 1: 论证结构解析

- **输入**：`argument`
- **动作**：
  1. 识别前提（Premises）
  2. 识别结论（Conclusion）
  3. 判断论证类型
- **输出**：`argument_analysis`
- **论证类型判断标准**：

| 类型 | 特征 | 示例 |
|------|------|------|
| **演绎** | 从一般到特殊，必然性推理 | "所有人都会死→苏格拉底是人→苏格拉底会死" |
| **归纳** | 从特殊到一般，或然性推理 | "观察到100只天鹅是白的→所有天鹅是白的" |
| **溯因** | 从结果推原因，最佳解释推理 | "地上湿了→可能下过雨" |

- **检查点**：✅ 验证前提和结论已识别

### Step 2: 20 种逻辑谬误检测

- **输入**：`argument_analysis`
- **动作**：系统性检测 20 种常见谬误

**谬误分类与检测**：

#### A. 相关性谬误（Relevance Fallacies）

| 谬误 | 特征 | 检测方法 |
|------|------|----------|
| **稻草人** | 歪曲对方观点后攻击 | 对比原文与引用 |
| **人身攻击** | 攻击人而非论点 | 检查是否针对个人 |
| **诉诸权威** | 仅因权威就接受 | 验证权威相关性 |
| **诉诸情感** | 用情感代替逻辑 | 检测情绪化语言 |
| **诉诸传统** | 因为一直如此 | 检查历史依据 |
| **诉诸多数** | 因为大家都这样 | 检查统计依据 |

#### B. 证据不足谬误（Defective Evidence Fallacies）

| 谬误 | 特征 | 检测方法 |
|------|------|----------|
| **草率概括** | 样本太小下结论 | 检查样本量 |
| **虚假类比** | 类比不当 | 检查相似性 |
| **滑坡谬误** | 无根据的连锁推导 | 检查因果链 |
| **假因假果** | 相关≠因果 | 检查因果关系 |
| **合成谬误** | 部分→整体 | 检查推理方向 |
| **分解谬误** | 整体→部分 | 检查推理方向 |

#### C. 逻辑结构谬误（Logical Structure Fallacies）

| 谬误 | 特征 | 检测方法 |
|------|------|----------|
| **循环论证** | 用结论证明前提 | 检查论证结构 |
| **虚假二分** | 非黑即白 | 检查是否有第三选项 |
| **乞题** | 预设结论 | 检查前提假设 |
| **否定前件** | 错误的逆命题推理 | 检查逻辑形式 |
| **肯定后件** | 错误的逆命题推理 | 检查逻辑形式 |
| **歧义谬误** | 歧义词义 | 检查关键术语 |

- **输出**：`fallacy_detection`
- **检查点**：✅ 验证 20 种谬误全部扫描

### Step 3: 逻辑质量评估

- **输入**：`fallacy_detection`
- **动作**：
  1. 计算逻辑质量得分
  2. 识别优势和弱点
  3. 生成改进建议
- **输出**：`logical_quality`
- **评分标准**：

| 等级 | 分数 | 标准 |
|:----:|:----:|------|
| A | 90-100 | 无谬误，论证严密 |
| B | 75-89 | 轻微瑕疵，基本有效 |
| C | 60-74 | 1-2 个中等谬误 |
| D | 40-59 | 多个谬误，论证薄弱 |
| F | 0-39 | 严重谬误，论证无效 |

### Step 4: 论证重构

- **输入**：`argument

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
