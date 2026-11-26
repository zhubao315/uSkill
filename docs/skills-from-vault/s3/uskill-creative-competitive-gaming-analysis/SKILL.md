---
name: uskill-creative-competitive-gaming-analysis
description: "让creative competitive gaming analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-competitive-gaming-analysis.md"
  original_id: "SKL-6875"
  version: "3.0.0"
  trust: untrusted
---

# creative competitive gaming analysis

# Competitive Gaming Analysis & Content Creation

## 🎯 目标

> AI增强的竞技游戏分析与内容创作流水线——从版本Meta分析、对局深度复盘到个人提升训练和高价值内容产出，将单局复盘与策略提炼时间缩短80%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 | 默认值 |
|------|------|------|------|--------|
| `game` | string | ✅ | 游戏名称（如"王者荣耀"、"英雄联盟"、"原神"） | — |
| `analysis_mode` | enum | ✅ | 分析模式：`review`（对局复盘）/ `meta`（版本分析）/ `training`（训练计划）/ `content`（内容创作） | — |
| `match_data` | object | ❌ | 对局数据（阵容、关键事件、赛后数据面板） | `{}` |
| `player_role` | string | ❌ | 玩家角色/位置（如"打野"、"中路"） | `""` |
| `current_rank` | string | ❌ | 当前段位 | `""` |
| `pain_points` | string[] | ❌ | 当前遇到的问题或瓶颈 | `[]` |
| `content_type` | enum | ❌ | 内容输出类型：`guide`（攻略）/ `video_script`（视频脚本）/ `social_post`（社交帖子） | `"guide"` |

## 📤 输出

```json
{
  "meta_analysis": {
    "tier_list": {
      "S_tier": ["T0英雄列表"],
      "A_tier": ["T1英雄列表"],
      "meta_shifts": "版本主要变化"
    },
    "strategy_trends": ["主流战术趋势"],
    "underrated_picks": ["被低估的英雄/战术"],
    "patch_impact": "版本更新影响分析"
  },
  "match_review": {
    "match_summary": {
      "result": "胜负",
      "duration": "时长",
      "key_moments": [
        {
          "timestamp": "关键时刻",
          "event": "事件描述",
          "decision_quality": "决策评价",
          "better_alternative": "更优解"
        }
      ]
    },
    "player_performance": {
      "strengths": ["做得好的方面"],
      "weaknesses": ["需要改进的方面"],
      "turning_point": "胜负手分析"
    },
    "improvement_items": [
      {
        "area": "改进领域",
        "specific_issue": "具体问题",
        "training_method": "针对性练习方法",
        "measurable_target": "可衡量目标"
      }
    ]
  },
  "training_plan": {
    "weekly_schedule": [
      {
        "day": "周一",
        "tasks": ["训练任务"],
        "duration": "时长",
        "target": "目标"
      }
    ],
    "focus_areas": ["重点提升方向"],
    "success_metrics": ["衡量指标"]
  },
  "content_output": {
    "title": "内容标题",
    "outline": ["内容大纲"],
    "draft": "初稿正文",
    "platform_adaptations": {
      "bilibili": "B站适配文案",
      "zhihu": "知乎适配文案",
      "douyin": "抖音适配文案"
    },
    "hashtags": ["话题标签"]
  }
}
```

## 📋 执行步骤

### Step 1: 版本Meta分析与信息优势建立

**动作：**
- 获取最新的游戏版本更新公告（英雄/装备/地图机制调整）
- AI扮演"顶级战队数据分析师"，快速分析版本变化并预测强势英雄（T0/T1）和主流战术
- 运用"价值投资"思维，寻找版本中被低估的"潜力股"英雄或战术
- 建立个人的版本理解笔记，形成信息优势

**战略考量：**
版本理解是所有竞技提升的基础。在赛季初抢先建立信息优势，比盲目跟风更有效。重点关注那些"悄悄变强"但尚未被广泛认知的英雄和战术。

**质量检查点：**
- [ ] AI的Meta预测是否与主流高端局表现初步吻合？
- [ ] 是否找到了至少1-2个被低估的"潜力股"英雄？
- [ ] 版本理解笔记是否已记录并可随时查阅？

**AI提示词：**

```
你是一位顶级的{game}职业战队数据分析师。
请基于最新的版本更新公告，分析并预测新赛季的Meta。

【版本更新公告】
{patch_notes}

报告需包含：
1. T0-T1级别的英雄梯度排行（按位置/分路）
2. 主流阵容搭配的变化趋势
3. 装备改动对哪些英雄影响最大
4. 被低估的"潜力股"英雄推荐（附理由）
5. 对新版本打法思路的3条核心建议
```

---

### Step 2: 对局深度复盘与数据驱动分析

**动作：**
- 选取有代表性的对局录像（关键胜利局或典型失利局）
- 人工快速回顾，标记关键时间点（一级团、关键击杀、转折点团战）
- 将对局关键事件、双方阵容、出装和赛后数据面板输入AI
- AI扮演"电竞复盘教练"，从经济曲线、决策逻辑、操作细节、资源置换等角度深度复盘

**战略考量：**
数据告诉你"发生了什么"，分析告诉你"为什么发生"。重点关注转折点的决策——那些"如果当时做了不同选择"的时刻，才是提升的关键。

**质量检查点：**
- [ ] 是否明确了本局的"胜负手"是什么？
- [ ] AI的分析是否指出了自己未曾注意到的细节？
- [ ] 是否识别了至少3个具体可改进的决策点？

**AI提示词（对局复盘）：**

```
你是一位KPL/顶级联赛冠军赛复盘教练。
我将提供一场{game}对局的简要信息，请进行深度复盘。

【对局信息】
我方阵容：{our_comp}
敌方阵容：{enemy_comp}
我的角色：{my_role}
比赛结果：{result}
关键事件时间戳：{key_events}
赛后数据面板：{post_match_data}

请分析：
1. BP阶段的优劣势分析
2. 关键转折点的决策是否正确，有无更优解？
3. 我方（特别是我的角色）的核心贡献和主要失误
4. 经济曲线和资源控制分析
5. 给出3条如果重来一次的具体改进建议
```

---

### Step 3: 个人提升点提炼与训练计划制定

**动作：**
- 基于复盘报告，总结个人在意识、操作、决策或英雄池方面的Top 3待改进项
- AI扮演"个人技术教练"，为每个待改进项设计具体的、可执行的针对性练习方法
- 将针对性练习整合到未来一周的训练计划中
- 设定可衡量的训练目标（如"本周完成50次特定连招练习，成功率达90%"）

**战略考量：**
改进必须具体化。"提升意识"不是改进项，"提高小地图关注频率至每5秒一次"才是。将模糊的不足转化为可量化、可练习的具体技能。

**质量检查点：**
- [ ] 待改进项是否足够具体（而非"提升意识"这类模糊表述）？
- [ ] 训练计划是否兼顾了排位、巅峰赛和针对性练习的时间分配？
- [ ] 是否为每个练习设定了可衡量的成功标准？

**AI提示词（训练方案）：**

```
你是一位针对个人的电竞技术教练。

【玩家信息】
游戏：{game}
当前段位：{current_rank}
主要角色/位置：{player_role}
最近复盘发现的问题：{pain_points}

请为我设计一个为期一周的针对性训练方案：
1. 每天的训练任务（含排位赛、针对性练习、观赛学习的时间分配）
2. 每个练习的具体方法和步骤
3. 可衡量的训练目标（如成功率、完成次数等）
4. 训练效果的自评方法
```

---

### Step 4: 高价值内容创作与分发

**动作：**
- 基于版本分析和对局复盘的洞察，确定具有稀缺性和深度的内容主题
- AI扮演"爆款游戏内容策划"，设计引人入胜的内容大纲或视频脚本框架
- 结合实战经验撰写攻略初稿或录制视频素材
- AI扮演"游戏KOL"对文案进行语言润色，使其更具网感和传播力
- 多平台分发：知乎

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
