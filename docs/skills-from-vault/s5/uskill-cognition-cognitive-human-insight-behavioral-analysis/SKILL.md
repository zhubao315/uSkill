---
name: uskill-cognition-cognitive-human-insight-behavioral-analysis
description: "让cognitive human insight behavioral analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-human-insight-behavioral-analysis.md"
  original_id: "SKL-5027"
  version: "3.0.0"
  trust: untrusted
---

# cognitive human insight behavioral analysis

# Human Insight & Behavioral Pattern Analysis

## 🎯 目标

> AI增强的人性洞察与行为分析流水线——在非临床场景下，对个人、团队或用户群体的行为与心理模式进行系统化分析，产出数据驱动的洞察报告与可执行行动建议，将单次分析报告生成时间缩短70%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 | 默认值 |
|------|------|------|------|--------|
| `analysis_target` | enum | ✅ | 分析对象类型：`user` / `team` / `self` | — |
| `core_question` | string | ✅ | 本次分析要回答的核心问题 | — |
| `qualitative_data` | file[] | ❌ | 定性数据（访谈文稿、会议记录、日记等） | `[]` |
| `quantitative_data` | file[] | ❌ | 定量数据（行为日志、使用数据等） | `[]` |
| `psychology_framework` | string | ❌ | 指定心理学解读框架（如"双系统理论"、"福格行为模型"） | `""` |
| `output_scope` | enum | ❌ | 输出范围：`insight_only` / `with_actions` / `full_report` | `"full_report"` |

## 📤 输出

```json
{
  "analysis_report": {
    "target": "分析对象",
    "core_question": "核心问题",
    "executive_summary": "3句话执行摘要"
  },
  "data_analysis": {
    "qualitative_findings": {
      "top_themes": [
        {
          "theme": "主题名称",
          "frequency": "提及频次",
          "representative_quotes": ["原文引用"],
          "sentiment": "positive/neutral/negative"
        }
      ],
      "counter_intuitive_insights": ["反直觉发现"]
    },
    "quantitative_findings": {
      "key_patterns": ["数据模式描述"],
      "user_segments": ["用户分群结果"],
      "behavioral_sequences": ["行为序列分析"]
    }
  },
  "psychological_insights": {
    "framework_applied": "使用的心理学框架",
    "core_insights": [
      {
        "insight": "洞察描述",
        "evidence": "支撑证据",
        "psychological_mechanism": "心理机制解释",
        "confidence": "high/medium/low"
      }
    ],
    "cognitive_biases_detected": ["识别到的认知偏误"]
  },
  "actionable_recommendations": [
    {
      "action": "具体行动",
      "rationale": "行动理由",
      "expected_effect": "预期效果",
      "validation_method": "验证方法",
      "validation_metric": "验证指标",
      "timeline": "验证周期"
    }
  ],
  "prompt_templates": []
}
```

## 📋 执行步骤

### Step 1: 目标定义与数据源确定

**动作：**
- **明确分析目标**：清晰定义本次分析要回答的核心问题。例如：
  - **产品场景**: "我的核心用户（Power User）最主要的行为动机是什么？"
  - **团队场景**: "我们团队在远程协作中，主要的沟通瓶颈在哪里？"
  - **个人场景**: "我在做投资决策时，最容易受到哪些认知偏误的影响？"
- **确定数据源**：根据目标，确定需要收集的数据类型
  - **定性数据**: 用户访谈录音/文稿、开放式问卷、会议记录、个人日记
  - **定量数据**: 产品后台用户行为日志、App使用时长、社交媒体互动数据

**战略考量：**
问题比答案更重要。一个定义清晰的问题，是后续所有分析不跑偏的前提。

**质量检查点：**
- [ ] 分析目标是否是一个具体、可回答的问题？
- [ ] 是否已明确至少两种（定性/定量）数据来源？

---

### Step 2: 多维数据收集与整理

**动作：**
- **收集定性数据**: 进行用户访谈、收集会议记录或相关文本材料
- **收集定量数据**: 从数据库或分析工具中导出用户行为数据
- **数据清洗与匿名化**: 对所有数据进行清洗和严格的匿名化处理，保护隐私
- **AI辅助整理**: 对于访谈录音，使用AI工具进行转录和初步摘要

**战略考量：**
尊重隐私是第一原则。所有涉及他人的数据，必须在获得授权且匿名化后使用。结合定性和定量数据，形成完整视角，避免单一数据源带来的偏见。

**质量检查点：**
- [ ] 所有个人身份信息是否已完全移除？
- [ ] 数据是否已整理成便于AI处理的格式（如.txt, .csv）？

---

### Step 3: AI辅助模式识别与分析

**动作：**
- **定性数据分析**: 使用**AI提示词-01**，让AI扮演"用户体验研究员"，对访谈文稿进行主题建模（Topic Modeling）和情感分析，快速识别高频关键词、情绪和观点
- **定量数据分析**: 使用Python脚本对行为数据进行探索性数据分析（EDA），如用户分群（Clustering）、行为序列分析等，寻找异常模式或群体特征

**战略考量：**
让AI做它擅长的事——从海量、无结构的数据中发现人类难以察觉的模式和关联。

**质量检查点：**
- [ ] AI识别出的主题是否与人工阅读的感受一致？
- [ ] 数据分析是否发现了至少1-2个反直觉的或有趣的模式？

**AI提示词（定性数据分析）：**

```
你是一位资深的用户体验研究员。我将提供{count}份用户访谈的匿名文稿。

请你：
1. 使用主题建模，识别出被提及次数最多的Top 5痛点和Top 5期望
2. 对整体文稿进行情感分析，判断用户的主流情绪是积极、中立还是消极
3. 引用原文，总结出2-3个最有趣或最反直觉的用户观点

文稿如下：
{interview_transcripts}
```

---

### Step 4: 心理学框架解读与洞察生成（人工主导）

**动作：**
- **选择解读框架**: 针对AI发现的模式和分析目标，选择合适的心理学理论框架：
  - **产品场景**: 福格行为模型（B=MAP）、马斯洛需求层次、用户心智模型
  - **团队场景**: 塔克曼团队发展阶段理论、Lencioni团队协作的五大障碍
  - **个人场景**: 卡尼曼的双系统理论、认知行为疗法（CBT）中的认知扭曲模型
- **深度解读**: 使用**AI提示词-02**，让AI辅助将数据模式与心理学框架结合，进行深度解读
- **人工提炼与升华**: 基于AI的初步解读，结合个人专业知识和经验，提炼出真正深刻、独特的洞察

**战略考量：**
AI提供素材，人来赋予智慧。这是整个流程中最核心、最体现个人价值的一步。将数据模式上升为对"人性"的理解。

**质量检查点：**
- [ ] 解读是否超越了数据表面，触及了背后的动机或原因？
- [ ] 是否产出了至少1-2个令人"眼前一亮"的深刻洞察？

**AI提示词（心理学框架应用）：**

```
你是一位{psychology_school}的专家。我发现了一个行为模式：

【数据模式】
{data_pattern}

请你运用{psychology_theory}来解释这个模式背后可能的心理机制，并提出2-3个待验证的假设。

要求：
1. 解释需结合具体的理论概念，而非泛泛而谈
2. 每个假设应说明验证方法
3. 标注解释的置信度（高/中/低）
```

---

### Step 5: 行动建议与验证方案

**动作：**
- **生成行动建议**: 使用**AI提示词-03**，将核心洞察转化为具体、可执行的行动建议。例如：
  - **产品洞察 → 产品功能**: "用户在决策时表现出'选择困难'，建议新增'智能推荐'功能。"
  - **团队洞察 → 管理举措**: "团队在异步沟通中信息损耗严重，建议引入'每日书面站会'SOP。"
  - **

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
