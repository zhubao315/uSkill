---
name: uskill-cognition-cognitive-manage-second-brain-pkm
description: "让cognitive manage second brain pkm变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-manage-second-brain-pkm.md"
  original_id: "SKL-6849"
  version: "3.0.0"
  trust: untrusted
---

# cognitive manage second brain pkm

# SKL-130: 第二大脑知识管理 (01-BRAIN/12-模型 + Zettelkasten)

## 🎯 目标

通过 C.O.D.E. 流水线（捕捉→组织→蒸馏→关联→表达）将信息碎片系统化地加工为互联的原子化知识网络，实现知识复利。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `knowledge_source` | string | ✅ | — | 待处理的原始信息（文章、高亮、想法等） |
| `target_area` | string | ✅ | — | 01-BRAIN/12-模型 目标分类路径，如 `Projects/开发个人App` 或 `Areas/投资` |
| `existing_notes` | string | ❌ | `""` | 已有相关笔记内容，用于辅助蒸馏与关联 |
| `output_format` | enum: `cards` / `connections` / `outline` | ❌ | `cards` | 输出格式：原子卡片、关联建议、或大纲 |

## 📤 输出

```json
{
  "type": "object",
  "properties": {
    "atomized_cards": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": { "type": "string", "description": "概括核心思想的标题" },
          "content": { "type": "string", "description": "第一人称永久笔记内容 (<200字)" },
          "tags": { "type": "array", "items": { "type": "string" }, "description": "3-5个标签" },
          "para_path": { "type": "string", "description": "PARA分类路径" }
        }
      }
    },
    "connections": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "target_note": { "type": "string", "description": "关联目标笔记标题" },
          "link_type": { "type": "string", "description": "关联类型：支撑/对比/扩展/因果" },
          "reason": { "type": "string", "description": "关联理由" }
        }
      }
    },
    "express_draft": {
      "type": "string",
      "description": "基于知识网络生成的内容初稿大纲"
    },
    "inbox_status": { "type": "string", "enum": ["cleared", "partial"] }
  }
}
```

## 📋 执行步骤

1. **接收** `knowledge_source`，将其标记为待处理并评估信息类型（文章/高亮/灵感/项目资料）
2. **分类** 根据 `target_area` 和 01-BRAIN/12-模型 框架判定归属：Projects（有截止日的具体目标）→ Areas（长期负责领域）→ Resources（兴趣主题）→ Archives（已完结）
3. **检索** 在 `existing_notes` 中查找与当前信息相关的已有笔记，建立初始关联候选
4. **蒸馏** 将原始信息重构为原子化永久笔记：每张卡片仅含一个核心思想，用第一人称重写，标题概括核心论点
5. **打标签** 为每张原子卡片生成 3-5 个语义标签，确保可检索性
6. **关联** 将新卡片与 `existing_notes` 中的笔记建立双向链接，注明链接类型（支撑/对比/扩展/因果）
7. **关联推荐** 分析新卡片内容，推荐 3-5 个跨领域的潜在知识连接
8. **质量校验** 检查每张卡片：标题是否清晰概括核心思想？删除上下文后是否独立可理解？是否至少关联 2 个已有笔记？
9. **根据 `output_format` 组装输出** — `cards`: 返回原子卡片列表；`connections`: 返回关联建议；`outline`: 整合卡片为创作大纲
10. **记录** 更新元数据：处理时间、来源 ID、01-BRAIN/12-模型 路径、关联数量

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 信息过载 | `knowledge_source` 超过 10,000 字 | 先提取关键段落，分批蒸馏 |
| 分类模糊 | 信息同时适用于多个 01-BRAIN/12-模型 分类 | 优先归入最接近行动的类别（P > A > R） |
| 无关联笔记 | `existing_notes` 为空或无相关内容 | 创建独立卡片，标记为待关联，跳过步骤 6-7 |
| 内容重复 | 新卡片与已有笔记高度相似 | 提示重复，建议合并或建立"强化"链接 |
| 知识源质量低 | 信息模糊、缺乏论据 | 标记为低置信度，建议补充来源后再处理 |

## ✅ 自检清单

- [ ] 每张原子卡片是否仅包含一个核心思想且独立可理解？
- [ ] Inbox 中的信息是否已全部归入 01-BRAIN/12-模型 对应分类？
- [ ] 每张新卡片是否与至少 2 个已有笔记建立了双向链接？
- [ ] 所有链接是否注明了类型（支撑/对比/扩展/因果）？
- [ ] 输出内容是否基于知识网络而非孤立信息拼凑？


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

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-05-09 | 从 SOP-21 转换为 uSkill 标准格式，封装 C.O.D.E. + 01-BRAIN/12-模型 + Zettelkasten 流水线 |

---
**相关笔记**：[[uSkill-cognition-行动前假设验证]] [[二阶思维]] 


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

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
