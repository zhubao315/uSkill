---
name: uskill-cognition-cognitive-manage-second-brain-knowledge
description: "让cognitive manage second brain knowledge变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-manage-second-brain-knowledge.md"
  original_id: "SKL-6836"
  version: "3.0.0"
  trust: untrusted
---

# cognitive manage second brain knowledge

# Manage Second Brain Knowledge

## 🎯 目标
> AI驱动的第二大脑知识管理系统——基于P.A.R.A.和Zettelkasten方法论，通过C.O.D.E.流水线（Capture→Organize→Distill→Connect→Express）将碎片化信息转化为原子化、互相关联的永久笔记，实现知识复利。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `vault_path` | string | ✅ | Obsidian知识库根目录路径（如 `/path/to/vault`） |
| `inbox_items` | array[object] | ✅ | 待处理的收件箱条目列表，每项包含 `title`、`content`、`source_type`（阅读高亮/网页文章/社媒灵感/即时想法）、`source_url`（可选） |
| `project_context` | object | ❌ | 当前活跃项目上下文，包含 `project_name`、`project_goal`、`deadline`（可选）、`related_areas`（可选） |
| `output_type` | enum | ❌ | `notes`（仅生成笔记）/ `outline`（生成笔记+大纲）/ `draft`（生成笔记+初稿），默认 `notes` |

## 📤 输出

```json
{
  "processing_summary": {
    "total_items": "int — 处理条目总数",
    "classified": {
      "projects": "int — 归入项目的条目数",
      "areas": "int — 归入领域的条目数",
      "resources": "int — 归入资源的条目数",
      "archived": "int — 归入归档的条目数"
    },
    "atomic_notes_created": "int — 新建原子笔记数",
    "connections_made": "int — 新建链接数"
  },
  "atomic_notes": [
    {
      "id": "string — 笔记唯一ID",
      "title": "string — 概括核心思想的标题",
      "content": "string — 用自己的话重写的核心内容（<200字）",
      "para_category": "string — P.A.R.A.分类（Projects/Areas/Resources/Archives）",
      "para_subfolder": "string — 具体子文件夹名",
      "tags": ["string — 标签列表"],
      "linked_notes": ["string — 关联笔记ID或标题列表"],
      "source_item_index": "int — 来源收件箱条目索引"
    }
  ],
  "connections_suggested": [
    {
      "note_title": "string — 当前笔记标题",
      "related_concepts": [
        {
          "concept": "string — 关联概念",
          "existing_note": "string | null — 已有笔记标题",
          "connection_reason": "string — 关联理由"
        }
      ]
    }
  ],
  "output_content": {
    "outline": "string | null — 基于知识库素材的大纲（output_type=outline/draft时）",
    "draft": "string | null — AI生成的初稿（output_type=draft时）"
  }
}
```

## 📋 执行步骤

### 阶段一：捕捉（Capture）

1. **验证知识库路径** — 检查 `vault_path` 是否存在且包含 `.obsidian` 目录，确认是有效的Obsidian知识库
2. **确保收件箱目录** — 在 `vault_path` 下确认 `00_Inbox` 文件夹存在，不存在则自动创建
3. **导入收件箱条目** — 将 `inbox_items` 中的每条信息转换为Markdown文件，保存至 `00_Inbox`，保留原始来源元数据（URL、平台、日期）

### 阶段二：组织（Organize）

4. **分析条目意图** — 对每条收件箱条目，判断其行动导向：是为了一个有截止日期的具体**项目**？需要长期负责的**领域**？感兴趣未来可能用的**资源**？还是已过时应**归档**？
5. **AI智能分类** — 对分类不确定的条目，以"信息架构师"角色分析内容，建议最适合的P.A.R.A.分类及具体子文件夹名称
6. **执行分类移动** — 将条目移入对应的P.A.R.A.目录结构：`10_Projects/`、`20_Areas/`、`30_Resources/` 或 `40_Archives/`，确保 `00_Inbox` 清空

### 阶段三：蒸馏（Distill）

7. **识别高价值信息** — 从 `Projects` 和 `Areas` 中筛选值得深度内化的条目，跳过低价值或纯存档内容
8. **原子化重构** — 以"Zettelkasten大师"角色，将每条高价值信息分解为3-5张独立的原子笔记：用第一人称、自己的话重写核心思想，每张笔记只包含一个核心观点（<200字），并打上3-5个语义标签
9. **验证原子性** — 检查每张笔记是否标题概括核心思想、删除上下文后是否仍可独立理解

### 阶段四：关联（Connect）

10. **扫描已有笔记** — 在 `vault_path` 中检索与新建原子笔记主题相关的已有笔记（通过标签匹配和关键词搜索）
11. **建立双向链接** — 为每张新原子笔记至少建立2个以上的 `[[双向链接]]`，连接到已有的概念、项目、人物或书籍笔记
12. **AI关联建议** — 以"创意催化剂"角色分析每张新笔记，从AI、投资、心理学、技术等知识领域建议3-5个跨域关联概念

### 阶段五：表达（Express）

13. **组装知识骨架** — 根据 `output_type`，将相关的原子笔记按逻辑顺序组合，形成创作骨架
14. **生成输出内容** — 若 `output_type=outline`，生成结构化大纲；若 `output_type=draft`，以"内容创作者"角色将骨架扩展为初稿，包含引言和总结
15. **写入知识库** — 将所有新建笔记、链接更新和输出内容写入 `vault_path` 对应目录

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `vault_path` 不存在或非Obsidian库 | 返回错误：`ERROR_INVALID_VAULT`，提示路径错误或缺少 `.obsidian` 目录 |
| `inbox_items` 为空 | 返回警告：无待处理条目，跳过全流程 |
| 收件箱条目缺少 `content` 字段 | 返回错误：`ERROR_EMPTY_CONTENT`，指出具体条目索引 |
| P.A.R.A.分类目录不存在 | 自动创建对应目录结构后继续 |
| 原子笔记拆分后单条超过300字 | 返回警告：建议进一步精简，但不阻断流程 |
| 找不到可关联的已有笔记 | 建议先积累更多笔记再运行Connect阶段，或跳过链接步骤 |
| `output_type=draft` 但无足够素材 | 降级为 `outline` 模式并返回警告 |
| 知识库中存在同名笔记 | 自动在标题后追加日期后缀避免覆盖 |

## ✅ 自检清单

- [ ] `00_Inbox` 是否已完全清空？
- [ ] 每条收件箱信息是否已根据行动导向归入P.A.R.A.对应分类？
- [ ] 新建原子笔记是否均为单一核心观点（标题可概括）？
- [ ] 原子笔记内容是否为用自己的话重写（非原文复制）？
- [ ] 每张新原子笔记是否与至少2个已有笔记建立了双向链接？
- [ ] 笔记标签是否准确反映内容语义（3-5个）？
- [ ] 输出JSON是否包含所有必填字段且类型正确？
- [ ] 所有文件写入是否成功（无路径错误或权限问题）？


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
- 当输入数据质量不足以支撑自动化决策时，

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
