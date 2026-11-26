---
name: uskill-creative-drama-deep-analysis-v2
description: "让creative drama deep analysis v2变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-drama-deep-analysis-v2.md"
  original_id: "SKL-6873"
  version: "3.0.0"
  trust: untrusted
---

# creative drama deep analysis v2

# 电视剧深度解读全流程

## 🎯 目标
> 对电视剧进行全维度深度解读，产出有观点、有证据、可直接发布的图文/视频脚本双版本内容，涵盖剧情结构、人物弧光、主题内核、隐喻符号、影视语言和文化映射六大维度。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `drama_name` | string | ✅ | 剧集名称，如 `"漫长的季节"` |
| `scope` | enum | ✅ | `single_episode` / `full_season` / `full_series` |
| `episode_range` | string | ❌ | 集数范围，如 `"S01E01-S01E05"`，为空则解读全剧 |
| `interpretation_focus` | array[string] | ❌ | 解读方向：`plot` / `character` / `theme` / `symbol` / `cinematography` / `cultural`，默认全维度 |
| `output_format` | enum | ❌ | `article` / `video_script` / `both`，默认 `both` |
| `target_platform` | enum | ❌ | `wechat` / `zhihu` / `xiaohongshu` / `bilibili` / `douyin` / `video_account`，默认 `wechat` + `bilibili` |
| `style` | enum | ❌ | `serious` / `sharp` / `mild` / `entertaining`，默认 `serious` |
| `taboo_topics` | array[string] | ❌ | 禁忌话题列表，如 `["政治", "宗教"]` |

## 📤 输出

```json
{
  "analysis_report": {
    "timeline": "string — 完整剧情时间线",
    "character_map": "object — 人物关系图（姓名、关系、阵营）",
    "foreshadowing_list": ["string — 伏笔/细节清单（含集数、证据）"],
    "controversy_points": ["string — 公众争议点汇总"],
    "behind_scenes": "string — 幕后创作背景（导演访谈、创作理念、原著差异）"
  },
  "deep_analysis": {
    "plot_structure": "string — 剧情结构分析（叙事节奏、伏笔回收、逻辑闭环、漏洞）",
    "character_arc": "string — 人物弧光分析（动机、转变、矛盾、象征、配角功能）",
    "theme_core": "string — 主题内核分析（阶级、性别、权力、家庭、时代、人性）",
    "metaphor_symbol": "string — 隐喻与符号分析（道具、场景、色彩、镜头、台词双关）",
    "film_language": "string — 影视语言分析（运镜、剪辑、配乐、光影、构图）",
    "cultural_mapping": "string — 文化/现实映射分析（时代背景、社会现象、价值观碰撞）"
  },
  "core_argument": {
    "main_thesis": "string — 1个核心主观点",
    "sub_arguments": ["string — 3个分论点（每个含论据支撑）"]
  },
  "content_output": {
    "article": {
      "title": "string — 爆款向+深度向标题",
      "hook": "string — 开篇钩子（3行抓住读者）",
      "recap": "string — 剧情极简回顾（≤全文20%）",
      "body": "string — 分论点论证（每段带证据：台词/细节/镜头）",
      "elevation": "string — 主题升华（上升到社会/人性/时代）",
      "ending": "string — 结尾留白/引人讨论",
      "tags_summary": "string — 标签与摘要",
      "full_text": "string — 完整图文终稿（Markdown格式）"
    },
    "video_script": {
      "hook_3s": "string — 开头3秒钩子",
      "recap_narration": "string — 剧情快剪旁白",
      "deep_breakdown": "string — 分点深度拆解（带画面提示）",
      "golden_quotes": "string — 金句段落",
      "interactive_ending": "string — 互动结尾（提问/引导弹幕）",
      "full_script": "string — 完整口播脚本（带时间戳/画面提示）"
    },
    "golden_quotes_list": ["string — 金句清单（可用于封面/标题/剪辑）"],
    "evidence_pack": {
      "cited_lines": ["string — 引用台词（含集数/时间点）"],
      "screenshot_positions": ["string — 截图点位（含集数/时间点/画面描述）"],
      "detail_points": ["string — 细节点位"]
    }
  },
  "quality_check": {
    "lines_accuracy": "boolean — 台词引用是否准确",
    "timeline_consistency": "boolean — 时间线是否无矛盾",
    "evidence_validity": "boolean — 伏笔分析是否有证据支撑",
    "argument_soundness": "boolean — 观点是否有据可依",
    "language_quality": "boolean — 语言流畅无口语垃圾"
  },
  "corrections_log": ["string — 错误修正清单"]
}
```

## 📋 执行步骤

### 阶段一：前置准备（5分钟人工输入）

1. **解析输入参数** — 确认剧集名称、季/集范围、解读方向、目标平台、风格禁忌，生成标准化配置
2. **生成解读框架** — 基于输入参数自动生成本剧的解读骨架（固定结构，不跑偏）
3. **输出资料检索清单** — 列出需要爬取/检索的所有信息类型和来源

### 阶段二：全量资料抓取（10-20分钟，多智能体并行）

4. **剧情资料梳理** — 整理完整时间线、关键事件节点、人物关系图谱
5. **伏笔暗线挖掘** — 抓取暗线、前后呼应、细节彩蛋、隐藏线索
6. **公众评论聚合** — 从豆瓣/知乎/Reddit收集高频观点、争议点、评价趋势
7. **幕后背景收集** — 抓取导演访谈、创作理念、原著差异、删减内容、拍摄花絮
8. **资料去重入库** — 对所有抓取资料进行去重、结构化整理，形成统一资料库

### 阶段三：六维深度解构（核心阶段）

9. **剧情结构分析** — 分析叙事节奏、伏笔回收节点、逻辑闭环完整性、剧情漏洞/BUG
10. **人物弧光分析** — 拆解每个主要角色的动机、转变轨迹、内心矛盾、象征意义、配角功能定位
11. **主题内核挖掘** — 挖掘阶级、性别、权力、家庭、时代、人性、社会批判等深层主题
12. **隐喻符号解读** — 解读道具象征、场景隐喻、色彩语言、镜头隐喻、台词双关
13. **影视语言分析** — 分析运镜手法、剪辑节奏、配乐情绪、光影对比、构图意图
14. **文化现实映射** — 关联时代背景、社会现象、价值观碰撞、现实问题投射

### 阶段四：确立核心观点（AI定调）

15. **提炼核心主观点** — 从解构报告中提炼1个有深度、有洞察的核心论点
16. **拆解分论点** — 围绕主观点展开3个可论证的分论点，构成解读灵魂
17. **证据匹配绑定** — 为每个论点匹配台词、镜头、细节、幕后等支撑证据

### 阶段五：内容生成（双版本自动输出）

18. **图文稿生成** — 按标准结构输出：标题→钩子→回顾→论证→升华→结尾→标签
19. **视频脚本生成** — 按标准结构输出：3秒钩子→快剪旁白→深度拆解→金句→互动结尾
20. **素材打包整理** — 整理金句清单、封面文案、证据包（台词/截图点位/细节）

### 阶段六：事实校验与润色

21. **台词准确性校验** — 核实所有引用台词是否与原剧一致
22. **时间线一致性校验** — 检查剧情时间线是否存在矛盾或错误
23. **证据有

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
