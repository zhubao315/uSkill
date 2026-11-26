---
name: uskill-creative-gaming-strategy-analysis
description: "让creative gaming strategy analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-gaming-strategy-analysis.md"
  original_id: "SKL-5037"
  version: "3.0.0"
  trust: untrusted
---

# creative gaming strategy analysis

# Gaming Strategy Analysis & Content Creation

## 🎯 目标
> 建立一套数据驱动的系统化流程，用于深度分析游戏版本与战局，并高效转化为个人竞技水平提升和高价值游戏内容创作。将单局复盘与策略提炼时间缩短 80%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `mode` | enum | ✅ | `competitive`（竞技提升）/ `content`（内容创作）/ `both`（双轨） |
| `version_patch_notes` | string | ❌ | 最新版本更新公告原文 |
| `match_data` | object | ❌ | `{hero_picks: ["string"], team_comps: ["string"], key_events: [{time: "string", event: "string"}], post_match_stats: {"string": "any"}, match_result: "win | loss"}` |
| `target_hero` | string | ❌ | 目标英雄名称（内容创作路径必填） |
| `content_platform` | enum | ❌ | `bilibili` / `zhihu` / `douyin`（内容创作路径选填） |
| `current_rank` | string | ❌ | 当前段位信息 |
| `known_issues` | ["string"] | ❌ | 已知个人短板（如"中期容易迷失节奏"） |

## 📤 输出

### 竞技提升路径 (`mode: competitive`)
```json
{
  "meta_analysis": {
    "tier_list": {"S": ["string"], "A": ["string"], "B": ["string"]},
    "meta_shifts": ["string — 版本 Meta 变化要点"],
    "underrated_picks": ["string — 被低估的潜力股英雄/战术"],
    "recommended_strategies": ["string — 新版本核心打法建议"]
  },
  "match_review": {
    "match_result": "win | loss",
    "winning_condition": "string — 胜负手分析",
    "bp_analysis": "string — Ban/Pick 阶段优劣势",
    "key_moments": [{ "time": "string", "decision": "string", "assessment": "correct | suboptimal", "alternative": "string" }],
    "economy_analysis": "string — 经济曲线与资源置换",
    "psychological_factors": ["string — 心理状态变化"],
    "top_3_improvements": [{ "issue": "string", "root_cause": "string", "practice_method": "string", "measurable_target": "string" }]
  },
  "training_plan": {
    "duration": "string — 如 '1 week'",
    "daily_tasks": [{ "day": "string", "tasks": ["string"], "duration_minutes": "int", "target_metric": "string" }],
    "weekly_goal": "string — 可衡量的周目标"
  }
}
```

### 内容创作路径 (`mode: content`)
```json
{
  "content_strategy": {
    "topic": "string — 具有稀缺性和深度的内容主题",
    "unique_insight": "string — 体现顶尖理解的独家知识点",
    "target_audience": "string",
    "hook": "string — 引人入胜的标题/开场"
  },
  "content_outline": {
    "sections": [{ "title": "string", "key_points": ["string"], "estimated_length": "string" }],
    "discussion_trigger": "string — 能引发评论区热烈讨论的结尾设计"
  },
  "draft": {
    "body": "string — 润色后的攻略文案或视频脚本",
    "tone": "professional-yet-engaging",
    "platform_adaptations": [{ "platform": "string", "adjustments": "string" }]
  }
}
```

## 📋 执行步骤

### 核心分析阶段

1. **版本与 Meta 分析** — 获取最新版本更新公告，让 AI 扮演"顶级战队数据分析师"，分析英雄、装备、地图机制调整，预测 T0/T1 英雄梯度和主流战术。运用价值投资思维寻找被低估的"潜力股"英雄或战术。
2. **对局复盘与数据分析** — 选取代表性对局录像，人工标记关键时间点（一级团、关键击杀、转折点团战），将关键事件、阵容、出装、数据面板输入 AI。让 AI 扮演"电竞复盘教练"，从经济曲线、决策逻辑、操作细节、资源置换角度深度复盘。识别数据背后的因果关系，分析心理状态变化。

### 竞技提升路径

3. **提炼个人提升点** — 基于复盘报告总结 Top 3 待改进项（必须足够具体，如"提高小地图关注频率"而非"提升意识"），让 AI 设计针对性练习方法。
4. **制定周度训练计划** — 将练习项目整合到一周计划，设定可衡量目标（如"本周完成50次特定连招练习，成功率达90%"），兼顾排位、巅峰赛和针对性练习的时间分配。

### 内容创作路径

5. **确定内容主题与框架** — 基于版本分析和复盘洞察确定稀缺性内容主题，让 AI 设计引人入胜的大纲或视频脚本框架。
6. **AI 辅助内容生成与发布** — 结合实战经验撰写初稿或录制素材，让 AI 扮演"游戏 KOL"润色文案使其更具网感和传播力，发布到知乎、B 站等平台。

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 版本更新公告缺失或不完整 | 基于高端局数据和社区讨论反推 Meta 变化 |
| 对局录像无法获取 | 使用赛后数据面板 + 个人回忆重建关键事件时间线 |
| 复盘分析过于笼统 | 要求 AI 聚焦具体时间点和决策，提供"如果重来"的替代方案 |
| 训练计划执行率 < 60% | 简化训练项目，降低单日负荷，增加趣味性 |
| 内容主题缺乏差异化 | 追问 AI "这个观点的独家之处在哪里"，挖掘更深层洞察 |
| 润色后失去专业性 | 设置红线术语清单，要求 AI 保留关键专业表达 |

## ✅ 自检清单

- [ ] Meta 预测与主流高端局表现初步吻合
- [ ] 复盘明确了本局"胜负手"
- [ ] AI 分析指出了自己未曾注意到的细节
- [ ] 待改进项足够具体且可执行
- [ ] 训练计划有可衡量的目标
- [ ] 内容主题体现了独特理解
- [ ] 最终内容既有深度又易于受众理解
- [ ] 内容具有"网感"和传播力


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
