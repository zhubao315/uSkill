---
name: uskill-creative-beijing-cultural-ambassador
description: "让creative beijing cultural ambassador变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-beijing-cultural-ambassador.md"
  original_id: "SKL-5038"
  version: "3.0.0"
  trust: untrusted
---

# creative beijing cultural ambassador

# Beijing Cultural Ambassador - AI-Powered Global Content Production

## 🎯 目标
> AI赋能的北京文化全球传播内容工坊：五步法生产线从选题挖掘到全渠道发布，将单个文化主题从研究到多平台内容发布的时间缩短70%，产出跨文化深度多媒体内容。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `topic` | string | ✅ | 北京文化主题关键词（如"钟鼓楼"、"豆汁儿"、"中轴线申遗"） |
| `target_platforms` | array | ✅ | 目标发布平台 `["blog", "youtube", "instagram", "bilibili", "zhihu"]` |
| `primary_medium` | enum | ✅ | 主要内容形式 `article`（深度图文）/ `video_script`（短视频脚本）/ `social_series`（系列社媒帖） |
| `target_languages` | array | ❌ | 目标语言，默认 `["zh", "en"]` |
| `personal_experiences` | string | ❌ | 个人与该主题相关的体验、故事素材 |
| `existing_materials` | array | ❌ | 已有的照片/视频/研究资料路径 |
| `audience_profile` | object | ❌ | `{domestic: "string", international: "string"}` — 目标受众画像 |

## 📤 输出

```json
{
  "cultural_content": {
    "research_summary": {
      "topic": "string — 文化主题",
      "historical_context": "string — 核心史料与历史背景",
      "key_story_points": ["string — 关键故事点"],
      "multidimensional_analysis": ["string — 跨学科解读视角"],
      "unique_insights": ["string — 原创观点"]
    },
    "storyline": {
      "core_character": "string — 核心人物",
      "core_conflict": "string — 关键冲突/看点",
      "emotional_arc": "string — 情感线索",
      "narrative_structure": "string — 叙事结构（开头/发展/高潮）",
      "angles": [
        {
          "angle": "string — 故事角度",
          "target_emotion": "string — 期望引发的情感",
          "cultural_depth": "string — 文化深度"
        }
      ]
    },
    "content_output": {
      "zh": {
        "title": "string — 中文标题",
        "body": "string — 正文/脚本",
        "social_posts": ["string — 社媒短文"]
      },
      "en": {
        "title": "string — 英文标题",
        "body": "string — 正文/脚本",
        "social_posts": ["string — 社媒短文"],
        "cultural_adaptation_notes": ["string — 文化适配说明"]
      }
    },
    "distribution_plan": {
      "platforms": [
        {
          "platform": "string",
          "title": "string — 平台定制标题",
          "description": "string — 简介",
          "publish_time": "string — 建议发布时间",
          "engagement_strategy": "string — 互动策略"
        }
      ],
      "review_checklist": {
        "cross_cultural_sensitivity": ["string — 文化敏感点"],
        "localization_issues": ["string — 本地化问题"]
      }
    }
  }
}
```

## 📋 执行步骤

### Step 1: 选题与故事线挖掘 (Topic & Storyline Mining)
1. **寻找"古都新韵"** — 聚焦能体现北京"传统与现代"交融的独特选题
   - 示例方向："AI时代的胡同生活"、"三里屯的建筑美学与青年文化"、"非遗传承人的数字化尝试"
2. **AI辅助头脑风暴** — 使用提示词模板，让AI扮演"文化记者"，基于初步想法头脑风暴3-5个故事角度
   - 每个角度需包含：核心人物、核心冲突/看点、更深层次的文化或人性价值
3. **确定核心故事** — 明确核心人物、关键冲突/看点、期望传递的核心情感或信息
   - 质量检查：选题是否具有独特性和全球吸引力？故事线是否有明确的开头、发展和高潮？

### Step 2: 多维研究与深度解读 (Multi-dimensional Research)
1. **文献研究** — 查阅相关史料、地方志，为故事提供坚实的历史文化深度
2. **实地探访** — 走访相关地点（胡同、寺庙、博物馆），进行沉浸式体验和观察
3. **视觉采集** — 拍摄高质量照片和视频素材
   - 注意光影、构图、色彩，捕捉有故事感的画面
4. **美学分析** — 分析研究对象在建筑、设计、色彩、仪式等方面的美学价值
   - 通过亲身实践和多技能交叉分析，形成独一无二的一手资料和原创观点
   - 质量检查：是否收集到足够的史料和视觉素材？是否形成至少一个独特的跨学科解读视角？

### Step 3: AI辅助多媒体内容创作 (AI-Assisted Content Creation)
1. **选择主媒介** — 根据故事特点，确定主要的内容形式（深度文章、短视频、图集）
2. **AI辅助文案/脚本撰写** — 使用提示词模板，让AI扮演"BBC纪录片导演"，将研究资料转化为生动文案
   - 要求：开头用反差或悬念抓住观众；用充满感官细节的语言描述；结尾落脚于文化连接
3. **视觉内容制作**
   - 摄影后期：对拍摄素材进行后期处理，增强叙事感
   - 视频剪辑：将视频素材、配音、字幕和音乐整合成片
   - AI辅助生成：利用AI工具生成数据可视化图表、动画或辅助性说明图像
   - 质量检查：文案/脚本是否逻辑清晰、引人入胜？视觉内容是否与文字高度匹配？

### Step 4: 跨文化本地化与包装 (Cross-Cultural Localization)
1. **AI辅助翻译与校对** — 将核心文案翻译成英文或其他目标语言
2. **文化适配性审查** — 使用提示词模板，让AI扮演"跨文化传播顾问"
   - 检查是否存在可能引起文化误解的词语或典故
   - 提出更符合目标受众文化习惯的表达方式
3. **重新包装** — 为海外平台（YouTube、Instagram）重新设计标题、封面图和内容简介
   - 全球传播不是简单的翻译，而是基于深刻理解的"文化转码"
   - 质量检查：英文标题和简介是否地道且吸引人？中国特有概念的解释是否清晰易懂？

### Step 5: 全渠道发布与互动 (Omni-Channel Publication & Engagement)
1. **制定发布计划** — 规划不同平台的发布时间、顺序和节奏
2. **多平台分发** — 在个人博客、知乎、B站、YouTube、Instagram等平台发布
3. **社区互动** — 积极回应各平台用户的评论和提问，参与相关话题讨论
   - 发布只是开始，互动才是核心
4. **效果复盘** — 一周后收集各平台数据（阅读量、观看量、互动率），总结经验
   - 质量检查：是否在发布后24小时内回应了首批评论？是否总结了关键成功/失败因素？

## 🤖 AI提示词库

### 提示词-01: 故事挖掘
```
你是一位供职于《纽约客》的资深文化记者，擅长从平凡事物中发现不凡故事。我正在研究北京的"[文化主题]”。请为我头脑风暴3个独特的、适合向国际读者讲述的故事角度。每个角度需包含一个核心人物、一个核心冲突/看点，以及它能揭示的某种更深层次的文化或人性

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
