---
name: uskill-cognition-172820
description: "精读与心智模型提取"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-精读与心智模型提取.md"
  original_id: "SKL-6832"
  version: ""
  trust: untrusted
---

# 精读与心智模型提取

name: "cognition-精读与心智模型提取"
version: "3.0.0"
vibe: "让精读与心智模型提取变成可执行的行动，而非停留在想法。"
emoji: "🔬"
domain: "cognition"

# Intense Reading Method（强力研读法）

## 🎯 目标

> 对非虚构类书籍进行高强度研读，最大化提取可行动知识点，避免无效阅读。

**核心理念**：不追求逐字阅读，追求知识点提取。读完一本书后，要能汲取足够多「为我所用」的知识点，而不是仅仅「读过」。

**适用范围**：非虚构类且非专业性书籍（如科普、商业、心理学、自我提升、历史等）。不适用于小说、诗歌等文学作品，也不适用于需要精读的专业教材。

**关键原则**：
1. **主动阅读** — 带着问题和目的去读，而非被动接收信息
2. **选择性吸收** — 识别并提取核心知识点，跳过填充内容
3. **行动导向** — 每个知识点都应转化为可执行的行动或思维模型
4. **输出驱动** — 以笔记输出倒逼阅读质量

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_title` | string | ✅ | 书籍名称 |
| `book_type` | enum | ✅ | 书籍类型：`business` / `science` / `psychology` / `history` / `self-help` / `technology` / `other` |
| `reading_goal` | string | ✅ | 本次阅读希望解决的具体问题或获取的知识领域 |
| `time_budget` | int | ⬜ | 预计投入时间（分钟），默认 `120` |
| `existing_knowledge` | string | ⬜ | 对该主题已有的了解程度：`beginner` / `intermediate` / `advanced` |
| `output_format` | enum | ⬜ | 输出格式：`obsidian_note` / `flashcards` / `action_list` / `all`，默认 `all` |

---

## 📤 输出

```json
{
  "book_meta": {
    "title": "string",
    "author": "string",
    "type": "string",
    "one_sentence_summary": "string"
  },
  "key_insights": [
    {
      "id": "K001",
      "insight": "string — 核心知识点陈述",
      "evidence": "string — 书中的支撑论据或案例",
      "relevance": "high | medium | low",
      "action_item": "string — 基于此知识点的可执行行动",
      "category": "string — 知识分类标签"
    }
  ],
  "mental_models": [
    {
      "model_name": "string",
      "description": "string",
      "applicable_scenarios": ["string"],
      "book_reference": "string — 书中页码或章节"
    }
  ],
  "reading_stats": {
    "total_insights_extracted": "int",
    "high_relevance_count": "int",
    "mental_models_count": "int",
    "estimated_reading_time_minutes": "int",
    "knowledge_gap_filled": "string — 填补了什么认知空白"
  },
  "next_actions": [
    {
      "action": "string",
      "priority": "high | medium | low",
      "deadline": "string — 建议完成时间"
    }
  ]
}
```

---

## 📋 执行步骤

### 阶段一：阅读前准备（Pre-Reading）

1. **明确阅读目的**
   - 写下你希望通过这本书解决的具体问题（1-3 个）
   - 评估自己对该主题的现有认知水平
   - 设定预期收获：读完后你应该知道什么？

2. **快速侦察（10-15 分钟）**
   - 阅读目录、序言、后记，建立全书框架认知
   - 翻阅每章标题和小标题，标记可能相关的章节
   - 阅读最后一章（通常是总结），快速了解全书核心论点
   - 记录初步疑问和兴趣点

3. **制定阅读策略**
   - 根据侦察结果，将章节分为三类：
     - 🟢 **精读** — 与目标高度相关的章节
     - 🟡 **略读** — 有一定价值但非核心的章节
     - ⚪ **跳过** — 与目标无关或已掌握的内容
   - 预估时间分配

### 阶段二：高强度研读（Active Reading）

4. **逐章精读（🟢 标记章节）**
   - 边读边问：**「作者在这里说了什么？」→「这是真的吗？」→「这对我有什么用？」**
   - 识别每个论点的三层结构：
     - **结论** — 作者主张什么
     - **证据** — 用什么支撑这个结论（数据、案例、逻辑推理）
     - **假设** — 作者隐含了什么前提
   - 对重要段落做标记，但不要过度标记（每章标记不超过 5-8 处）

5. **区分核心知识与填充内容**
   - **核心知识标志**：
     - 🔑 作者反复强调的观点
     - 🔑 有具体数据或案例支撑的论点
     - 🔑 与你阅读目的直接相关的内容
     - 🔑 颠覆或扩展你现有认知的观点
     - 🔑 可以迁移到其他领域的思维模型
   - **填充内容标志**：
     - 🗑 大家都知道的常识
     - 🗑 没有新信息的过渡段落
     - 🗑 重复前文观点但无新增价值
     - 🗑 纯粹的修辞或故事（除非故事本身是核心论据）
     - 🗑 与你阅读目的无关的拓展内容

6. **快速扫描（🟡 标记章节）**
   - 只读每段的第一句话和最后一句话
   - 重点关注数字、案例、结论性表述
   - 如发现意外重要信息，升级为精读

### 阶段三：笔记整理与知识提取（Extraction）

7. **即时笔记记录**
   - 每读完一章，立即用 **3-5 句话** 总结本章核心要点
   - 使用自己的话复述，不要照抄原文
   - 格式：`[页码/章节] 核心观点 → 支撑论据 → 对我的意义`

8. **构建知识点清单**
   - 将所有标记内容整理为结构化知识点
   - 每个知识点包含：
     - **一句话概括**（不超过 30 字）
     - **详细说明**（用自己的话，2-4 句）
     - **证据来源**（书中引用）
     - **行动转化**（这个知识怎么用？）
   - 为目标筛选：只保留 `relevance = high` 或 `medium` 的知识点

9. **提取思维模型**
   - 识别可迁移的思维框架或方法论
   - 为每个模型命名，方便日后调用
   - 标注适用场景和限制条件

### 阶段四：输出与行动（Output & Action）

10. **生成结构化笔记**
    - 将知识点整理为 Obsidian 笔记格式
    - 使用双向链接关联已有知识库中的相关概念
    - 创建 MOC（Map of Content）如果该主题有多本相关书籍

11. **制定行动清单**
    - 每个高相关度知识点对应至少一个行动项
    - 行动项应具体、可执行、有时间限制
    - 区分「立即行动」和「长期实践」

12. **阅读回顾**
    - 回顾最初设定的阅读目的，检查是否达成
    - 记录最大的 3 个收获
    - 记录遗留问题（需要进一步研究的内容）
    - 评估：这本书值得推荐给谁？值得二读吗？

---

## ⚠️ 异常处理

| 场景 | 症状 | 应对策略 |
|------|------|----------|
| 信息过载 | 读了大量内容但感觉什么都记不住 | 立即暂停，回到步骤 1 重新明确目标；降低精读范围，只聚焦最相关的 2-3 章 |
| 注意力涣散 | 阅读速度明显下降，反复读同一段 | 采用番茄工作法（25 分钟专注 + 5 分钟休息）；站起来走动后继续 |
| 知识点太少 | 整本书读完只提取了 2-3 个知识点 | 可能是选书问题——这本书对你来说太浅或太深；记录原因，下次改进选书标

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
