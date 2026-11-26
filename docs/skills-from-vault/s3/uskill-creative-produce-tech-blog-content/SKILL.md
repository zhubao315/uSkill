---
name: uskill-creative-produce-tech-blog-content
description: "让creative produce tech blog content变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-produce-tech-blog-content.md"
  original_id: "SKL-6877"
  version: "3.0.0"
  trust: untrusted
---

# creative produce tech blog content

# AI-Powered Tech Blog Content Pipeline

## 🎯 目标
> 建立一套标准化的、AI驱动的五步内容生产线，持续高效地生产具有深度、独特性和广泛影响力的技术博客文章，将单篇高质量博客的平均创作时间缩短80%。通过"一次创作、多次分发、持续互动"，将个人知识资产转化为公开技术影响力。

**核心适用场景**：
1. **技术复盘总结** — 完成高难度项目后，系统性总结经验教训，沉淀为个人知识资产
2. **个人品牌建设** — 持续输出高质量技术文章，提升行业知名度和影响力
3. **复杂概念科普** — 将深奥技术原理用通俗易懂的语言向非技术人员或初学者解释

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `topic` | string | ✅ | — | 博客主题或选题方向 |
| `core_thesis` | string | ✅ | — | 核心论点/价值主张 |
| `target_audience` | string | ❌ | `"技术从业者"` | 目标读者画像 |
| `writing_style` | enum | ❌ | `"professional"` | 写作风格：`professional` / `casual` / `tutorial` / `storytelling` |
| `max_length` | int | ❌ | `3000` | 输出最大字数 |
| `include_code` | boolean | ❌ | `true` | 是否包含代码示例 |
| `code_language` | string | ❌ | `"python"` | 代码示例编程语言 |
| `diagram_type` | enum | ❌ | `"auto"` | 配图类型：`auto` / `mermaid` / `plantuml` / `none` |
| `platforms` | array | ❌ | `["blog","zhihu"]` | 分发平台列表 |
| `seo_level` | enum | ❌ | `"standard"` | SEO优化等级：`basic` / `standard` / `aggressive` |
| `output_mode` | enum | ❌ | `"full"` | 输出模式：`full`(全流程) / `outline-only`(仅大纲) / `draft-only`(仅初稿) / `distribute-only`(仅分发文案) |

## 📤 输出

```json
{
  "topic_analysis": {
    "unique_angle": "string — 基于复合技能的独特切入点",
    "audience_profile": "string — 目标读者画像描述",
    "value_proposition": "string — 文章核心价值主张",
    "topic_score": "number — 选题评分(受众广度×深度×稀缺性×时效性)"
  },
  "outline": {
    "hook": "string — 引言钩子（痛点或悬念）",
    "sections": [
      {
        "title": "string — 章节标题",
        "key_points": ["string — 章节要点"],
        "word_estimate": "int — 预估字数"
      }
    ],
    "conclusion": "string — 总结升华要点",
    "total_estimate": "int — 全文预估字数"
  },
  "article_draft": "string — 完整文章 Markdown 格式",
  "code_examples": [
    {
      "language": "string — 编程语言",
      "description": "string — 功能描述",
      "code": "string — 完整代码（含逐行注释）",
      "output": "string — 预期运行结果"
    }
  ],
  "visuals": {
    "architecture_diagram": "string — Mermaid/PlantUML 架构图代码",
    "flow_diagram": "string — Mermaid/PlantUML 流程图代码",
    "cover_concept": "string — 封面图设计提示词"
  },
  "seo": {
    "titles": ["string — 3个备选标题"],
    "keywords": ["string — 5-8个核心关键词"],
    "meta_description": "string — 150字以内摘要"
  },
  "distribution": [
    {
      "platform": "string — 平台名称",
      "copy": "string — 适配该平台的宣发文案",
      "format_notes": "string — 平台排版注意事项"
    }
  ],
  "content_calendar_entry": {
    "publish_date": "string — 建议发布日期",
    "promotion_schedule": ["string — 推广时间节点"],
    "engagement_plan": "string — 社区互动计划"
  }
}
```

## 📋 执行步骤

### Step 1 — 选题与策略 (Topic Selection & Strategy)
1. **挖掘独特视角** — 结合复合技能背景，寻找交叉领域独特选题（如：AI+投资 = "用AI分析财报挖掘科技股潜力"）
2. **验证选题价值** — 评估选题的受众广度、深度、稀缺性和时效性，打分排序
3. **确定核心论点** — 明确文章要传递的核心观点和价值主张
4. **质量检查点** — ✅ 选题是否充分发挥复合优势？目标读者是谁？能解决什么具体问题？
5. **战略原则** — "写我能写，而非写人已写"，利用能力矩阵创造"信息差"和"认知差"

### Step 2 — 大纲与叙事设计 (Outlining & Narrative Design)
1. **设计故事线** — 构建"痛点引入 → 解决方案 → 深度解析 → 总结升华"的叙事线
2. **构建金字塔结构** — 论点先行，层层递进，归纳总结
3. **AI辅助大纲生成** — 使用资深技术编辑角色，根据核心论点生成详尽、逻辑清晰的文章大纲
4. **质量检查点** — ✅ 大纲逻辑清晰？每个章节要点明确？引言有钩子？

### Step 3 — AI辅助创作与优化 (AI-Assisted Creation & Optimization)
1. **分段式初稿撰写** — 逐章节将要点和AI生成的草稿结合，快速完成初稿
2. **AI辅助代码示例** — 生成清晰、可运行、包含逐行中文注释的代码示例
3. **语言润色与风格统一** — 对全文进行语言优化，使专业概念通俗易懂、生动有趣
4. **质量检查点** — ✅ 核心观点清晰？论据充分？代码可独立运行？风格统一？

### Step 4 — 视觉与SEO增强 (Visual & SEO Enhancement)
1. **架构图/流程图** — 使用 Mermaid/PlantUML，结合AI辅助，快速生成专业图表
2. **概念图/封面图** — 运用美学原理，使用Figma或AI绘画工具创作高质量配图
3. **SEO优化** — 生成3个备选标题、5-8个精准关键词、150字以内Meta Description
4. **质量检查点** — ✅ 配图清晰美观？标题兼具吸引力和关键词覆盖？关键词覆盖核心主题？

### Step 5 — 发布与多平台分发 (Publication & Multi-Platform Distribution)
1. **最终审校** — Markdown编辑器通读，检查格式、链接、图片引用等细节
2. **全平台发布** — 将文章发布到个人博客、知乎、掘金、Medium等目标平台
3. **社交媒体推广** — 为各平台生成不同风格的宣发文案（Twitter简洁有冲击力 / LinkedIn突出商业价值 / 知乎引导深入阅读）
4. **社区互动** — 积极参与评论区和相关社区讨论，回答读者问题，扩大影响力
5. **内容日历更新** — 记录发布日期、推广时间节点和社区互动计划
6. **质量检查点** — ✅ 各平台排版正常？推广文案已发出？互动计划已安排？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| `topic` 过于宽泛 | 无法锁定具体切入点 | 返回缩小建议 + 3个细分选

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
