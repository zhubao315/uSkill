---
name: uskill-cognition-cognitive-build-second-brain-knowledge-syst
description: "让cognitive build second brain knowledge system变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-build-second-brain-knowledge-system.md"
  original_id: "SKL-6843"
  version: "3.0.0"
  trust: untrusted
---

# cognitive build second brain knowledge system

# Build AI-Powered Second Brain Knowledge System

## 🎯 目标
> 建立一套基于 P.A.R.A. 和 Zettelkasten 方法论、由 AI 全面赋能的个人知识管理（PKM）操作系统，高效捕捉、组织、提炼和创造知识。对抗信息熵增，实现知识复利。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `raw_information` | string | ✅ | 待处理的原始信息（文章、笔记、高亮、灵感等） |
| `processing_goal` | string | ✅ | 处理目标：organize | distill | connect | express |
| `existing_knowledge_context` | string | ❌ | 现有知识库中相关主题的上下文 |
| `output_type` | string | ❌ | `express` 模式下的输出类型：blog | report | proposal，默认 blog |

## 📤 输出

```json
{
  "capture": {
    "inbox_item": {
      "source": "string — 信息来源",
      "content": "string — 摘要内容",
      "capture_method": "string"
    }
  },
  "organize": {
    "classification": "Projects | Areas | Resources | Archives",
    "sub_folder": "string — 建议的子文件夹路径",
    "reasoning": "string — 分类理由"
  },
  "distill": {
    "atomic_notes": [
      {
        "title": "string — 概括性标题",
        "content": "string — 第一人称核心内容（<200字）",
        "tags": ["string — 3-5个标签"],
        "source": "string — 原始信息来源"
      }
    ]
  },
  "connect": {
    "current_note_concept": "string",
    "related_concepts": [
      {
        "concept": "string — 相关概念/笔记名称",
        "connection_type": "string — 类比/因果/对比/补充",
        "insight_potential": "string — 连接可能产生的洞察"
      }
    ],
    "suggested_links": ["string — 建议的双链目标"]
  },
  "express": {
    "content_type": "string",
    "source_notes": ["string — 使用的原子笔记标题"],
    "outline": {
      "sections": [
        {
          "heading": "string",
          "source_notes": ["string"]
        }
      ]
    },
    "draft_markdown": "string — 内容初稿"
  }
}
```

## 📋 执行步骤

1. **捕捉 (Capture)** — 建立无摩擦信息入口：统一收件箱（`00_Inbox`），配置自动化工具（Readwise 同步、网页剪藏、社媒收藏、即时想法），确保一分钟内可将任何信息发送到收件箱
2. **组织 (Organize)** — 每日/每周清理收件箱，按 P.A.R.A. 框架分类：Projects（有截止日期的具体目标）、Areas（长期负责领域）、Resources（感兴趣主题）、Archives（已完成/不感兴趣），对不确定分类使用 AI 辅助判断
3. **蒸馏 (Distill)** — 对有价值信息进行原子化重构：遵循 Zettelkasten 原则，用自己话重写为独立永久笔记（每条一个核心思想，<200 字），AI 辅助将长文分解为 3-5 张结构清晰的原子笔记
4. **关联 (Connect)** — 建立双向链接：为每张新笔记关联至少 2 个已有笔记，使用 `[[双括号]]` 主动链接相关概念/项目/人物/书籍，AI 建议 3-5 个跨领域关联点，定期审视 Obsidian 关系图谱
5. **表达 (Express)** — 以输出为目的检索知识网络，将多张关联原子笔记组合排序为创作骨架，AI 辅助生成博客/报告/方案初稿，完成知识从输入→内化→创造价值的完整闭环

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `raw_information` 信息量过大 | 分批处理，先提取核心要点再逐步蒸馏 |
| 信息无法归入 P.A.R.A. 任一类 | 归入 Resources 下新建主题，或暂时保留在 Inbox 待观察 |
| 原子笔记内容过长（>200字） | 继续拆分为更小的独立笔记 |
| 找不到可关联的已有笔记 | 先独立存在，标记为"待关联"，后续积累时补充 |
| 知识库结构不清晰 | 先执行一次全面的 P.A.R.A. 重组，再继续日常流程 |

## ✅ 自检清单

- [ ] 一分钟内可将任何平台信息无缝发送到收件箱
- [ ] 收件箱已清空，每条信息已根据行动性合理归类
- [ ] 每张新永久笔记可用一个清晰标题概括核心思想
- [ ] 删除上下文后，笔记仍能独立存在并被理解
- [ ] 每张新笔记至少与 2 个以上已有笔记建立链接
- [ ] 能通过双链在不同领域知识间轻松漫游
- [ ] 最近一次公开分享的素材来源于第二大脑
- [ ] 能为任何熟悉领域快速组织分享大纲


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

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-21 转化 |


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定制。

---

## 🚫 Anti-Rationalization Table `[v3新增]`

> 来源：addyosmani/agent-skills 的核心创新

| Agent 常见借口 | 反驳 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
