---
name: uskill-creative-content-adaptation
description: "让内容改编变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-content-adaptation.md"
  original_id: "SKL-5611"
  version: "3.0.0"
  trust: untrusted
---

# 内容改编

description: |
  当用户需要将长文改编为短文、图文、视频脚本，或进行跨平台内容分发时使用此 Skill。
  触发词包括：'改编'、'转化'、'跨平台'、'短视频'、'图文'、
  '内容分发'、'多形态'。
  不适用于原创内容创作（使用文案写作）。当需要将已有内容适配不同平台时优先使用。

---

# uSkill-611: 内容改编

## 🎯 目标

> 将内容从一种形态改编为另一种形态，保持核心信息的同时适应不同平台。

**核心价值**：好内容应该能跨平台传播，而非为每个平台从零创作。

**适用场景**：
- 内容运营
- 跨平台发布
- 知识传播
- 教学设计
- 品牌传播
- 个人IP打造

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `source_content` | `string` | ✅ | — | 原始内容 |
| `source_format` | `enum` | ✅ | — | `article` / `video` / `podcast` / `presentation` |
| `target_format` | `enum` | ✅ | — | `short_article` / `social_post` / `video_script` / `infographic` |
| `platform` | `string` | ❌ | — | 目标平台 |
| `audience` | `string` | ❌ | — | 目标受众 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话改编建议",
  "adaptation_id": "ADPT-YYYY-MMDD-NNN",

  "content_analysis": {
    "core_message": "string",
    "key_points": ["string"],
    "supporting_evidence": ["string"],
    "target_audience": "string"
  },

  "format_strategy": {
    "source_format": "string",
    "target_format": "string",
    "adaptation_approach": "string",
    "key_transformations": ["string"]
  },

  "platform_optimization": {
    "platform": "string",
    "algorithm_considerations": ["string"],
    "best_practices": ["string"],
    "content_length": "string",
    "hashtag_strategy": ["string"]
  },

  "adapted_content": {
    "title": "string",
    "body": "string",
    "key_elements": ["string"],
    "call_to_action": "string",
    "visual_suggestions": ["string"]
  },

  "content_variants": [
    {
      "variant": "string",
      "platform": "string",
      "title": "string",
      "body": "string",
      "key_differences": "string"
    }
  ],

  "distribution_plan": {
    "timeline": "string",
    "cross_promotion": ["string"],
    "engagement_strategy": "string"
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

### Step 1: 内容分析

- **输入**：`source_content` + `source_format`
- **动作**：
  1. 提取核心信息
  2. 识别关键点
  3. 分析支撑证据
- **输出**：`content_analysis`
- **内容分析维度**：

| 维度 | 问题 | 目的 |
|------|------|------|
| 核心信息 | 最重要的一句话是什么？ | 保留精华 |
| 关键点 | 有哪些支撑点？ | 内容结构 |
| 证据 | 有哪些数据/案例？ | 可信度 |
| 受众 | 原本面向谁？ | 适配参考 |

**分支条件**：
- 若 `source_format=article` → 提取段落结构和论点
- 若 `source_format=video` → 提取时间轴和画面
- 若 `source_format=podcast` → 提取话题和金句
- 若 `source_format=presentation` → 提取页面和逻辑

### Step 2: 改编策略设计

- **输入**：`content_analysis` + `target_format`
- **动作**：
  1. 选择改编方法
  2. 确定变换重点
  3. 设计改编流程
- **输出**：`format_strategy`
- **改编方法指南**：

| 原格式 | 目标格式 | 改编方法 | 重点 |
|--------|----------|----------|------|
| 长文 | 短文 | 提炼+压缩 | 保留核心 |
| 文章 | 社交帖 | 切片+强化 | 冲击力 |
| 文章 | 视觉化 | 转化+图示 | 视觉呈现 |
| 视频 | 文字 | 提取+整理 | 信息完整 |
| 播客 | 文字 | 转录+编辑 | 可读性 |

**分支条件**：
- 若 `target_format=short_article` → 压缩至500-1000字
- 若 `target_format=social_post` → 压缩至100-300字
- 若 `target_format=video_script` → 转化为口语化脚本
- 若 `target_format=infographic` → 转化为视觉化信息

### Step 3: 平台适配优化

- **输入**：`format_strategy` + `platform`
- **动作**：
  1. 分析平台算法
  2. 应用最佳实践
  3. 优化内容参数
- **输出**：`platform_optimization`
- **平台适配指南**：

| 平台 | 内容特点 | 最佳实践 | 算法考量 |
|------|----------|----------|----------|
| 微信公众号 | 深度长文 | 标题+封面+排版 | 完读率+分享 |
| 小红书 | 图文种草 | 封面+标签+互动 | 收藏+互动 |
| 抖音 | 短视频 | 前3秒+节奏+BGM | 完播率+互动 |
| B站 | 中长视频 | 标题+封面+弹幕 | 播放量+互动 |
| 知乎 | 专业回答 | 深度+数据+案例 | 赞同+收藏 |
| 微博 | 热点话题 | 话题+图片+互动 | 转发+评论 |

**分支条件**：
- 若 `platform=微信` → 长度5000-8000字，深度分析
- 若 `platform=小红书` → 长度300-500字，图片优先
- 若 `platform=抖音` → 时长15-60秒，节奏快
- 若 `platform=B站` → 时长5-15分钟，有深度
- 若 `platform=知乎` → 长度2000-5000字，有数据
- 若 `platform=微博` → 长度140-200字，有话题

### Step 4: 内容改编生成

- **输入**：`content_analysis` + `format_strategy` + `platform_optimization`
- **动作**：
  1. 生成改编内容
  2. 优化标题和正文
  3. 设计行动号召
- **输出**：`adapted_content`
- **改编技巧**：

| 技巧 | 目的 | 示例 |
|------|------|------|
| 提炼金句 | 增加传播力 | 提取原文精华 |
| 制造冲突 | 吸引注意力 | 对比+反转 |
| 添加互动 | 提升参与 | 问题+投票 |
| 视觉化 | 增强理解 | 图表+案例 |
| 口语化 | 亲

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
