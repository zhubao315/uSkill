---
name: uskill-creative-storytelling
description: "让故事化表达变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-storytelling.md"
  original_id: "SKL-5605"
  version: "3.0.0"
  trust: untrusted
---

# 故事化表达

description: |
  当用户需要用故事包装观点、增强说服力、制作演示文稿、进行品牌叙事时使用此 Skill。
  触发词包括：'故事'、'叙事'、'讲故事'、'演示'、'品牌故事'、
  '内容营销'、'情感共鸣'、'包装观点'。
  不适用于纯数据报告（使用数据可视化）。遇到需要情感共鸣的场景时优先使用。

---

# uSkill-605: 故事化表达

## 🎯 目标

> 用故事结构包装观点和信息，增强说服力和记忆度，建立情感连接。

**核心价值**：人类大脑天生喜欢故事。好故事能让信息深入人心。

**适用场景**：
- 演讲和演示
- 品牌营销
- 内容创作
- 产品介绍
- 团队沟通
- 培训教学

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `core_message` | `string` | ✅ | — | 核心信息/观点 |
| `audience` | `string` | ✅ | — | 目标受众 |
| `purpose` | `enum` | ❌ | `persuade` | `persuade` / `inform` / `entertain` / `inspire` |
| `medium` | `enum` | ❌ | `speech` | `speech` / `written` / `video` / `social` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话故事框架建议",
  "story_id": "ST-YYYY-MMDD-NNN",

  "story_structure": {
    "framework": "string",
    "elements": {
      "hero": "string",
      "villain": "string",
      "conflict": "string",
      "journey": "string",
      "resolution": "string",
      "moral": "string"
    }
  },

  "narrative_arc": [
    {
      "stage": "setup|rising_action|climax|falling_action|resolution",
      "duration_percentage": "number",
      "content": "string",
      "emotional_curve": "string"
    }
  ],

  "storytelling_techniques": [
    {
      "technique": "string",
      "description": "string",
      "application": "string"
    }
  ],

  "audience_engagement": {
    "hooks": ["string"],
    "emotional_triggers": ["string"],
    "call_to_action": "string"
  },

  "script_or_outline": {
    "opening": "string",
    "body": "string",
    "closing": "string",
    "key_moments": ["string"]
  },

  "delivery_tips": {
    "pacing": "string",
    "emphasis": ["string"],
    "visual_aids": ["string"]
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

### Step 1: 故事框架选择

- **输入**：`core_message` + `purpose`
- **动作**：
  1. 分析核心信息
  2. 选择适合的故事框架
  3. 定义故事元素
- **输出**：`story_structure`
- **故事框架选择**：

| 框架 | 结构 | 适用场景 |
|------|------|----------|
| 英雄之旅 | 冒险-挑战-成长 | 激励、品牌故事 |
| 三幕剧 | 设置-对抗-解决 | 演讲、演示 |
| 问题-解决方案 | 问题-分析-方案 | 商业演示 |
| 起承转合 | 引入-发展-转折-结局 | 中式叙事 |

**分支条件**：
- 若 `purpose=inspire` → 优先选择英雄之旅
- 若 `purpose=inform` → 优先选择问题-解决方案
- 若 `purpose=entertain` → 优先选择三幕剧
- 若 `purpose=persuade` → 根据 `medium` 决定

### Step 2: 叙事弧线设计

- **输入**：`story_structure`
- **动作**：
  1. 设计情感曲线
  2. 安排节奏
  3. 制定关键时刻
- **输出**：`narrative_arc`
- **叙事弧线阶段**：

| 阶段 | 目的 | 时长占比 |
|------|------|----------|
| 设置 | 建立背景和角色 | 15-20% |
| 上升 | 建立冲突和张力 | 30-40% |
| 高潮 | 最紧张时刻 | 10-15% |
| 下降 | 解决冲突 | 15-20% |
| 结局 | 总结和启示 | 10-15% |

**分支条件**：
- 若 `medium=speech` → 增加互动停顿点
- 若 `medium=written` → 增加视觉过渡标记
- 若 `medium=video` → 增加画面节奏说明

### Step 3: 故事技巧应用

- **输入**：`story_structure` + `medium`
- **动作**：
  1. 选择适合的技巧
  2. 应用到故事中
  3. 增强感染力
- **输出**：`storytelling_techniques`
- **故事技巧库**：

| 技巧 | 描述 | 应用 |
|------|------|------|
| 悬念 | 制造好奇心 | 开场、过渡 |
| 对比 | 突出差异 | 强调重点 |
| 细节 | 增加真实感 | 角色塑造 |
| 重复 | 加强记忆 | 核心信息 |
| 转折 | 制造惊喜 | 高潮 |
| 感官描写 | 增强沉浸感 | 场景构建 |

**分支条件**：
- 若受众为专业人士 → 减少情感技巧，增加数据支撑
- 若受众为普通大众 → 增加情感技巧，减少专业术语
- 若媒介为社交 → 缩短技巧应用，强调冲击力

### Step 4: 受众参与设计

- **输入**：`audience` + `purpose`
- **动作**：
  1. 设计开场钩子
  2. 识别情感触发点
  3. 制定行动号召
- **输出**：`audience_engagement`
- **钩子类型**：

| 类型 | 示例 | 适用场景 |
|------|------|----------|
| 悬念钩子 | "你有没有遇到过..." | 通用 |
| 数据钩子 | "90%的人不知道..." | 理性受众 |
| 情感钩子 | "那一刻，我明白了..." | 感性受众 |
| 冲突钩子 | "我们曾经面临..." | 团队沟通 |

**分支条件**：
- 若 `purpose=persuade` → 行动号召必须明确具体
- 若 `purpose=inspire` → 行动号召可以是开放式反思
- 若 `purpose=inform` → 行动号召可以是信息获取建议

### Step 5: 脚本/大纲生成

- **输入**：所有前序输出
- **动作**：
  1. 生成开场、主体、结尾
  2. 标注关键时刻
  3. 提供交付建议
- **输出**：`script_or_outline` + `delivery_tips`
- **脚本结构**：

| 部分 | 内容要求 | 时长占比 |
|------|----------|----------|
| 开场 | 钩子 + 背景 + 主题 | 15-20% |
| 主体 | 故事发展 + 冲突 + 转折 | 60-70% |
| 结尾 | 高潮 + 解决 + 启示 | 15-20% |

**分支条件**：
- 若 `medium=speech` → 提供语速和停顿建议
- 若 `medium=written` → 提供段落和过渡建议
- 若 `medium=video` → 提供画面和音效建议
- 若

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
