---
name: uskill-creative-presentation-rhythm
description: "让演讲节奏控制变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-presentation-rhythm.md"
  original_id: "SKL-5607"
  version: "3.0.0"
  trust: untrusted
---

# 演讲节奏控制

description: |
  当用户需要控制演讲节奏、设计情绪曲线、把握停顿技巧、优化演讲结构时使用此 Skill。
  触发词包括：'演讲节奏'、'停顿'、'情绪曲线'、'演讲结构'、'起承转合'、
  '演讲技巧'、'演讲控制'。
  不适用于纯文本写作（使用文案写作）。当需要口头表达的节奏控制时优先使用。

---

# uSkill-607: 演讲节奏控制

## 🎯 目标

> 掌握演讲的起承转合，运用停顿技巧，设计情绪曲线，提升演讲效果。

**核心价值**：好的节奏能让演讲引人入胜，坏的节奏会让听众昏昏欲睡。

**适用场景**：
- 公开演讲
- 产品发布
- 培训授课
- 路演演示
- 会议发言
- 团队汇报

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `speech_content` | `string` | ✅ | — | 演讲内容/大纲 |
| `duration` | `number` | ✅ | — | 演讲时长（分钟） |
| `audience` | `string` | ✅ | — | 目标受众 |
| `purpose` | `enum` | ❌ | `persuade` | `persuade` / `inform` / `inspire` / `entertain` |
| `skill_level` | `enum` | ❌ | `intermediate` | `beginner` / `intermediate` / `advanced` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话节奏建议",
  "rhythm_id": "RHY-YYYY-MMDD-NNN",

  "structure": {
    "sections": [
      {
        "name": "string",
        "duration_percentage": "number",
        "pacing": "fast|medium|slow",
        "techniques": ["string"]
      }
    ],
    "total_sections": "number",
    "balance_score": "number"
  },

  "pause_strategy": {
    "types": [
      {
        "type": "string",
        "purpose": "string",
        "duration": "string",
        "placement": "string"
      }
    ],
    "total_pauses": "number",
    "average_duration": "string"
  },

  "emotional_curve": {
    "stages": [
      {
        "stage": "string",
        "intensity": "number",
        "techniques": ["string"]
      }
    ],
    "peak_moments": ["string"],
    "resolution": "string"
  },

  "delivery_script": {
    "sections": [
      {
        "content": "string",
        "pacing_note": "string",
        "pause_markers": ["string"],
        "emphasis_words": ["string"]
      }
    ]
  },

  "practice_guide": {
    "warmup": ["string"],
    "key_exercises": ["string"],
    "common_mistakes": ["string"]
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

### Step 1: 结构分析与划分

- **输入**：`speech_content` + `duration`
- **动作**：
  1. 分析内容结构
  2. 划分演讲段落
  3. 分配时间比例
- **输出**：`structure`
- **结构划分指南**：

| 段落 | 目的 | 时间占比 | 节奏 |
|------|------|----------|------|
| 开场 | 吸引注意力 | 10-15% | 慢→快 |
| 主体 | 传达信息 | 60-70% | 中→快→中 |
| 高潮 | 强调重点 | 10-15% | 快→慢 |
| 结尾 | 总结行动 | 10-15% | 慢→稳 |

**分支条件**：
- 若 `duration < 10分钟` → 简化结构，减少段落
- 若 `duration > 30分钟` → 增加互动环节
- 若 `purpose=inspire` → 增加情感段落
- 若 `purpose=inform` → 增加数据段落

### Step 2: 停顿策略设计

- **输入**：`structure` + `skill_level`
- **动作**：
  1. 识别停顿点
  2. 设计停顿类型
  3. 确定停顿时长
- **输出**：`pause_strategy`
- **停顿类型**：

| 类型 | 目的 | 时长 | 适用场景 |
|------|------|------|----------|
| 强调停顿 | 突出重点 | 2-3秒 | 关键观点后 |
| 思考停顿 | 给听众思考 | 3-5秒 | 复杂概念后 |
| 转换停顿 | 段落过渡 | 1-2秒 | 段落之间 |
| 紧张停顿 | 制造悬念 | 5-10秒 | 问题提出后 |
| 恢复停顿 | 调整节奏 | 1-2秒 | 快节奏后 |

**分支条件**：
- 若 `skill_level=beginner` → 减少紧张停顿
- 若 `skill_level=advanced` → 增加戏剧性停顿
- 若 `duration < 10分钟` → 减少总停顿次数
- 若 `duration > 30分钟` → 增加恢复停顿

### Step 3: 情绪曲线设计

- **输入**：`structure` + `purpose`
- **动作**：
  1. 设计情绪强度
  2. 规划高潮时刻
  3. 确定收尾方式
- **输出**：`emotional_curve`
- **情绪曲线模型**：

| 模型 | 结构 | 适用场景 |
|------|------|----------|
| 山峰型 | 低-高-低 | 激励演讲 |
| 波浪型 | 多次起伏 | 长时间演讲 |
| 线性增长 | 低-高 | 说服演讲 |
| U型 | 高-低-高 | 戏剧性演讲 |

**分支条件**：
- 若 `purpose=inspire` → 使用山峰型，高潮在80%处
- 若 `purpose=persuade` → 使用波浪型，多个小高潮
- 若 `purpose=inform` → 使用线性增长，稳步提升
- 若 `purpose=entertain` → 使用U型，中间有反转

### Step 4: 交付脚本生成

- **输入**：`structure` + `pause_strategy` + `emotional_curve`
- **动作**：
  1. 生成分段脚本
  2. 标注节奏提示
  3. 添加停顿标记
- **输出**：`delivery_script`
- **脚本标注系统**：

| 标记 | 含义 | 示例 |
|------|------|------|
| [P1] | 强调停顿 | 观点后 |
| [P2] | 思考停顿 | 问题后 |
| [P3] | 转换停顿 | 段落间 |
| [F] | 快速 | 紧张部分 |
| [S] | 慢速 | 强调部分 |
| [R] | 正常 | 一般内容 |
| *word* | 强调词语 | 重点词 |

**分支条件**：
- 若 `skill_level=beginner` → 增加详细标注
- 若 `skill_level=advanced` → 减少标注，保留关键提示
- 若 `medium=presentation` → 增加视觉配合提示
- 若 `medium=video` → 增加画面切换提示

### Step 5: 练习指南生成

- **输入**：所有前序输出
- **动作**：
  1. 设计热身练

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
