---
name: uskill-defense-information-pollution
description: "让信息污染检测变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-defense-information-pollution.md"
  original_id: "SKL-6891"
  version: "3.0.0"
  trust: untrusted
---

# 信息污染检测

description: |
  当用户需要检测信息真实性、识别假新闻、评估信息源可信度、识别误导信息时使用此 Skill。
  触发词包括：'信息污染'、'假新闻'、'事实核查'、'信息验证'、'可信度'、
  '误导信息'、'信息操纵'、'谣言识别'、'信息质量'。当用户分享新闻、文章、
  社交媒体内容并询问其真实性时，即使未直接说"信息污染"，也应使用此 Skill。
  不适用于专业领域技术文档（使用对应领域 Skill）。遇到信息验证需求时优先使用。

---

# uSkill-101: 信息污染检测

## 🎯 目标

> 建立系统化的信息质量评估框架，帮助用户识别假新闻、误导信息、认知攻击，保护认知安全。

**核心价值**：在信息过载时代，快速准确地评估信息质量，避免被虚假或误导信息影响决策。

**适用场景**：
- 新闻文章真实性验证
- 社交媒体内容评估
- 学术论文可信度判断
- 商业宣传信息甄别
- 投资研报质量评估

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `content` | `string` | ✅ | — | 待检测的信息内容 |
| `source` | `string` | ❌ | `unknown` | 信息来源（媒体/个人/机构） |
| `content_type` | `enum` | ❌ | `article` | `news` / `article` / `social` / `academic` / `commercial` |
| `context` | `object` | ❌ | — | `{publish_time, author, platform, shares}` |
| `depth` | `enum` | ❌ | `standard` | `quick` / `standard` / `deep` |

**输入约束**：
- `content` 必须为非空字符串（最少 50 字）
- `content_type` 决定检测侧重点
- `depth = deep` 时执行完整 12 维度检测

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话信息质量结论",
  "pollution_id": "IP-YYYY-MMDD-NNN",

  "source_analysis": {
    "credibility_score": "number — 0-100",
    "source_type": "official|media|individual|unknown",
    "bias_direction": "left|center|right|unknown",
    "track_record": "string — 历史可信度记录"
  },

  "content_analysis": {
    "factual_claims": [
      {
        "claim": "string",
        "verifiable": true,
        "evidence_available": true,
        "supporting_evidence": ["string"],
        "contradicting_evidence": ["string"],
        "confidence": "number"
      }
    ],
    "logical_structure": {
      "argument_valid": true,
      "fallacies_detected": ["string"],
      "evidence_quality": "strong|moderate|weak|absent"
    },
    "emotional_manipulation": {
      "detected": false,
      "techniques": ["string"],
      "intensity": "low|medium|high"
    }
  },

  "pollution_detection": {
    "is_polluted": false,
    "pollution_type": "misinformation|disinformation|propaganda|clickbait|satire|none",
    "confidence": "number",
    "severity": "low|medium|high|critical",
    "evidence": ["string"]
  },

  "credibility_assessment": {
    "overall_score": "number — 0-100",
    "grade": "A|B|C|D|F",
    "key_risks": ["string"],
    "recommendation": "trust|verify|distrust|reject"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

### 异常输出

```json
{
  "status": "partial",
  "error_code": "IP_WARNING_SHORT_CONTENT",
  "error_message": "内容过短，无法进行深度分析",
  "suggestion": "请提供更完整的内容（至少 50 字）",
  "partial_result": {
    "source_analysis": "已完成",
    "content_analysis": "部分完成"
  }
}
```

---

## 📋 执行步骤

### Step 1: 信息源可信度评估

- **输入**：`source` + `context`
- **动作**：
  1. 识别信息源类型（官方/媒体/个人/未知）
  2. 查询信息源历史可信度记录
  3. 评估信息源的立场和偏见
- **输出**：`source_analysis`
- **可信度评分标准**：

| 来源类型 | 基础分 | 加分项 | 减分项 |
|----------|:------:|--------|--------|
| 官方机构 | 80 | 权威认证 +10 | 曾有造假 -30 |
| 主流媒体 | 70 | 多方引用 +5 | 立场鲜明 -10 |
| 个人博主 | 40 | 专业背景 +20 | 营销账号 -20 |
| 未知来源 | 20 | 可验证 +30 | 匿名 -10 |

- **分支条件**：
  - IF `source = unknown` AND 内容涉及重大事件 → 标记 `WARNING_UNVERIFIED_SOURCE`
  - IF 历史记录显示曾有造假 → 标记 `WARNING_SOURCE_CREDIBILITY`
- **检查点**：✅ 验证信息源已识别

### Step 2: 事实性声明提取

- **输入**：`content`
- **动作**：
  1. 提取所有可验证的事实性声明
  2. 区分事实与观点
  3. 评估每个声明的可验证性
- **输出**：`factual_claims`
- **事实性声明特征**：
  - 包含具体数据、日期、人名、地点
  - 可通过公开信息验证
  - 使用确定性语言（"是"、"有"、"发生了"）
- **观点性声明特征**：
  - 使用主观语言（"应该"、"可能"、"我认为"）
  - 无法直接验证
  - 价值判断
- **检查点**：✅ 验证至少提取 3 个事实性声明

### Step 3: 逻辑结构分析

- **输入**：`content` + `factual_claims`
- **动作**：
  1. 分析论证结构
  2. 检测逻辑谬误
  3. 评估证据质量
- **输出**：`logical_structure`
- **常见逻辑谬误清单**：

| 谬误类型 | 特征 | 检测方法 |
|----------|------|----------|
| 稻草人论证 | 歪曲对方观点 | 对比原文与引用 |
| 滑坡谬误 | 无根据的连锁推导 | 检查因果链 |
| 诉诸权威 | 仅因权威就接受 | 验证权威相关性 |
| 虚假二分 | 非黑即白 | 检查是否有第三选项 |
| 循环论证 | 用结论证明前提 | 检查论证结构 |
| 诉诸情感 | 用情感代替逻辑 | 检测情绪化语言 |

- **检查点**：✅ 验证逻辑分析完成

### Step 4: 情绪操纵检测

- **输入**：`content`
- **动作**：
  1. 检测情绪化语言
  2. 识

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
