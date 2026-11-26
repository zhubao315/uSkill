---
name: uskill-cognition-cognitive-deep-reading-knowledge-management
description: "让cognitive deep reading knowledge management变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-deep-reading-knowledge-management.md"
  original_id: "SKL-5020"
  version: "3.0.0"
  trust: untrusted
---

# cognitive deep reading knowledge management

# Deep Reading & Knowledge Management

## 🎯 目标
> AI增强的深度阅读与知识管理闭环流程：从战略选书、主动精读、知识原子化到资产沉淀，实现最大化认知回报（ROI）和知识复利。像投资人一样选书，像架构师一样拆解，像学者一样内化。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_info` | string | ✅ | 书名及作者信息 |
| `reading_purpose` | string | ✅ | 阅读目的（主题研究 / 经典研读 / 知识沉淀 / 输出驱动） |
| `current_goals` | string | ❌ | 当前个人目标，用于评估书籍ROI |
| `existing_annotations` | string | ❌ | 已有的高亮和批注文本（适用于第二步起） |
| `atomic_cards` | array | ❌ | 已生成的原子化知识卡片（适用于第四步起） |
| `reading_stage` | enum | ✅ | `pre_read` / `active_reading` / `extraction` / `integration` / `management` |
| `personal-knowledge-vault_path` | string | ❌ | Obsidian知识库路径，默认 `~/obsidian` |

## 📤 输出

```json
{
  "stage": "pre_read | active_reading | extraction | integration | management",
  "pre_read_report": {
    "core_thesis": "string — 本书试图解决的终极问题",
    "unique_value": "string — 相比同类书籍的独特价值",
    "book_structure": "string — 全书逻辑架构概述",
    "top3_concepts": ["string — 最值得关注的核心概念"],
    "roi_score": {
      "relevance": "number (1-10)",
      "inspiration": "number (1-10)",
      "decision": "skip | skim | deep_read"
    }
  },
  "reading_notes": {
    "core_questions": ["string — 带着读的核心问题"],
    "red_highlights": ["string — 核心论点/颠覆性观点"],
    "yellow_highlights": ["string — 个人灵感/实践想法"],
    "green_highlights": ["string — 疑问/难点"],
    "first_principles": ["string — 第一性原理探究"]
  },
  "atomic_cards": [
    {
      "title": "string — 核心概念",
      "content": "string — 通俗语言重述",
      "insight": "string — 个人思考",
      "tags": ["string"],
      "source": "string — 书名+页码"
    }
  ],
  "evergreen_note": {
    "ultimate_puzzle": "string — 作者试图解决的根本问题",
    "first_principles": "string — 核心概念的本质来源",
    "golden_quotes": [{"quote": "string", "analysis": "string"}],
    "action_items": ["string — 具体应用/创作灵感"],
    "obsidian_links": ["string — 双向链接建议"]
  },
  "book_list_entry": "string — 书单归档格式"
}
```

## 📋 执行步骤

### Step 1: 战略选书与预读决策
1. **需求分析** — 运用投资人思维评估：这本书能解决什么关键问题？投资回报率如何？
2. **AI辅助预读** — 让AI扮演"图书投资分析师"，5分钟内扫描全书，输出核心论点、章节结构、关键概念，识别作者的"终极困惑"
3. **决策打分** — 相关性(1-10) + 启发性(1-10)：<6分放弃；6-8分快速检视；>8分深度精读
4. **输出《书籍决策与预读报告》**

### Step 2: 主动式深度精读
5. **带着问题读** — 基于预读报告列出3-5个核心问题
6. **高亮与批注** — 🔴红色=核心论点/颠覆性观点；🟡黄色=个人灵感/实践想法；🟢绿色=疑问/难点
7. **第一性原理探究** — 对核心概念追本溯源，进行跨界联想
8. **AI苏格拉底导读** — 遇到难点让AI通过提问引导深入理解，而非直接给答案

### Step 3: 知识萃取与原子化
9. **导出笔记** — 将高亮和批注导出为文本
10. **AI原子化重构** — 让AI扮演"知识架构师"，将原始笔记拆解为原子化知识卡片
11. **卡片标准** — 一张卡片只讲一个概念；用自己的话重述（费曼技巧）；包含标签和来源

### Step 4: 整合输出与链接
12. **撰写永久笔记** — 整合原子卡片，生成系统化的《永久性核心洞察笔记》
13. **知识联网** — 在Obsidian中将新卡片与已有笔记建立双向链接（≥3个旧笔记）
14. **输出倒逼输入** — 规划≥1个具体应用行动或创作灵感

### Step 5: 资产管理与复盘
15. **更新书单** — 在`我的书单.md`中添加条目
16. **归档** — Markdown文件归档到分类文件夹
17. **间隔复习** — 核心卡片加入Anki或定期回顾清单

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `book_info` 过于模糊 | 返回 `ERROR_INSUFFICIENT_INFO` + 需补充清单（至少需书名） |
| `reading_stage` 与可用数据不匹配 | 返回 `WARNING_STAGE_MISMATCH` + 提示需先完成前置阶段 |
| 预读ROI评分全部 <6 | 建议 `skip` + 推荐同主题替代书目 |
| 原子化卡片数 < 3 | 返回 `WARNING_THIN_EXTRACTION` + 建议回退精读阶段补充批注 |
| 永久笔记双向链接 < 3 | 返回 `WARNING_WEAK_LINKING` + 提示扩展知识网络关联 |

## ✅ 自检清单

- [ ] 预读阶段：是否明确了阅读目的并完成ROI打分？
- [ ] 精读阶段：批注是否多于原文摘抄？核心问题是否找到初步答案？
- [ ] 萃取阶段：每张卡片是否能独立存在？是否用费曼技巧重写？
- [ ] 整合阶段：新笔记是否链入≥3个旧笔记？是否有明确行动计划？
- [ ] 管理阶段：书单是否已更新并计数？文件命名是否符合规范？
- [ ] 全流程：是否输出了至少4类交付物（预读报告/卡片集/永久笔记/书单条目）？


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
- 当所

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
