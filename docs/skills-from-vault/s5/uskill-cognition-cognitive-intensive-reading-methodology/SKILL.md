---
name: uskill-cognition-cognitive-intensive-reading-methodology
description: "让cognitive intensive reading methodology变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-intensive-reading-methodology.md"
  original_id: "SKL-6840"
  version: "3.0.0"
  trust: untrusted
---

# cognitive intensive reading methodology

# Intensive Reading Methodology (强力研读法)

## 🎯 目标
> 通过系统化的强力研读流程，从非虚构类书籍中高效提取可操作的知识点，将阅读转化为实际能力提升。核心宗旨：**只留骨头不留肉**——读完后汲取足够的为我所用的知识点，这本书就可以扔了。不做书的搬运工，只做知识的炼金术士。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_title` | string | ✅ | 书名及作者信息 |
| `reading_purpose` | string | ✅ | 阅读目的（解决什么问题 / 提升什么能力 / 验证什么假设） |
| `time_budget` | string | ✅ | 时间预算（如"2小时"/"3天"/"1周"），决定研读深度 |
| `output_format` | enum | ❌ | 输出格式：`cards`（知识卡片）/ `note`（永久笔记）/ `outline`（行动纲领）/ `all`（全部），默认 `all` |
| `existing_notes` | string | ❌ | 已有的高亮/批注文本（适用于从第二步开始） |
| `prior_knowledge` | string | ❌ | 对该主题的已有认知，用于精准提取新知识 |
| `personal-knowledge-vault_path` | string | ❌ | Obsidian 知识库路径，默认 `~/obsidian` |

## 📤 输出

```json
{
  "reading_session": {
    "book": "string — 书名+作者",
    "purpose": "string — 本次研读目的",
    "duration": "string — 实际耗时",
    "method_applied": "强力研读法"
  },
  "step1_reconnaissance": {
    "book_type": "string — 书籍类型判定（方法论/认知/商业/心理/其他）",
    "author_intent": "string — 作者试图解决的核心问题",
    "core_thesis": "string — 一句话概括全书核心论点",
    "structure_map": "string — 全书逻辑架构（章节→论点→论据层次）",
    "estimated_bones": "number — 预估可提取的知识点数量",
    "go_decision": "boolean — 是否值得强力研读"
  },
  "step2_extraction": {
    "knowledge_points": [
      {
        "id": "string — 编号（如 KP-01）",
        "original": "string — 原文关键段落/观点",
        "essence": "string — 一句话提炼核心要义",
        "type": "enum — principle（原理）/ method（方法）/ insight（洞见）/ fact（事实）",
        "novelty": "enum — new（全新认知）/ reinforce（强化已有认知）/ contradict（颠覆已有认知）"
      }
    ],
    "total_extracted": "number",
    "key_questions_answered": ["string — 精读前提出的核心问题及回答"]
  },
  "step3_crystallization": {
    "knowledge_crystals": [
      {
        "id": "string — 编号（如 KC-01）",
        "title": "string — 知识晶体标题（一个概念）",
        "definition": "string — 用自己的话重述（费曼语言）",
        "how_to_use": "string — 具体使用场景和操作方法",
        "example": "string — 一个具体案例或类比",
        "related_kps": ["string — 关联的知识点编号"],
        "action_hint": "string — 一句话行动提示"
      }
    ],
    "crystal_count": "number",
    "discard_check": "string — 验证：是否已提取完所有有价值的内容？"
  },
  "step4_connection": {
    "connections": [
      {
        "crystal_id": "string — 知识晶体编号",
        "links_to": ["string — 已有笔记的双向链接（Obsidian格式）"],
        "cross_domain": ["string — 跨领域关联"],
        "confirms": "string — 与已有认知相互印证的内容",
        "challenges": "string — 对已有认知的挑战或修正"
      }
    ],
    "network_density": "string — 知识网络连接强度评估（稀疏/适中/密集）",
    "new_hypotheses": ["string — 由连接产生的新假设或新问题"]
  },
  "step5_verification": {
    "one_sentence_summary": "string — 全书一句话总结（只留的骨头）",
    "top3_actionable_insights": ["string — 最值得行动的3个洞见"],
    "teaching_test": "string — 能否用30秒向别人讲清楚这本书的核心？",
    "confidence_score": "number (1-10) — 对提取质量的自信度",
    "discard_ready": "boolean — 此书是否可以扔了？",
    "follow_up": ["string — 需要进一步探索的方向"]
  },
  "deliverables": {
    "evergreen_note": "string — 永久笔记（Markdown格式，可直接存入Obsidian）",
    "knowledge_cards": ["string — 知识卡片列表（Markdown格式）"],
    "action_plan": "string — 行动纲领（可执行的TODO列表）"
  }
}
```

## 📋 执行步骤

### Step 1: 预读侦察（5-15分钟）

> 目标：不读全书，先摸清敌情，判断值不值得研读、从哪里下刀。

1. **扫描外围** — 读书名、副标题、作者背景、推荐序、目录、后记（共10分钟）。回答：这本书到底在说什么？作者有什么资格说？
2. **画出骨架** — 根据目录，用一句话概括每个章节的核心论点，拼出全书的逻辑骨架图：
   ```
   第X章：[一句话论点] → 支撑论据：A/B/C
   ```
3. **标记高价值区域** — 在目录中标记最可能产出"知识晶体"的章节（通常2-4个），其余章节速扫或跳过
4. **做出研读决策** — 基于侦察结果判断：
   - **全面研读**：全书高价值，按完整流程执行
   - **重点研读**：仅精读标记章节，其余跳过
   - **放弃研读**：核心观点已知/价值不高，直接弃书（这本身就是正确决策）
5. **提出核心问题** — 列出3-5个你希望通过研读回答的具体问题（这是精读的导航仪）

### Step 2: 精读提取（核心环节，占总时间60%）

> 目标：带着问题读，只抓取对"我"有用的知识点，原文是原料不是收藏品。

6. **逐章精读** — 对标记的高价值章节进行精读，每读完一节暂停，回答：
   - 这一节的核心观点是什么？（一句话）
   - 这个观点对我有什么用？（具体场景）
   - 我同意吗？为什么？
7. **提取知识点（KP）** — 每发现一个有价值的观点，立即记录为知识点：
   - **原文关键段落**（保留出处，用于日后溯源）
   - **一句话提炼**（用自己的话，不是原文复述）
   - **知识类型标记**：原理 / 方法 / 洞见 / 事实
   - **新旧标注**：全新认知 / 强化已有 / 颠覆已有
8. **跳过噪音** — 以下内容大胆跳过：
   - 已知的常识和背景铺垫
   - 过多的案例和故事（一个就够）
   - 作者的个人经历闲聊
   - 重复论证同一观点的段落
9. **回答核心问题** — 在精读过程中，逐步回答 Step 1 提出的核心问题

### Step 3: 知识晶体化（从原料到成品）

> 目标：将提取的

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
