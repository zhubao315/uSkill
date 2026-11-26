---
name: uskill-personal-knowledge-graph
description: "知识的价值不在于你记住了多少——在于你能连接多少。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-personal-knowledge-graph.md"
  original_id: "SKL-6805"
  version: "3.0.0"
  trust: untrusted
---

# 个人知识图谱构建

description: |
  当用户需要在 Obsidian 中构建知识图谱、优化笔记结构、增加双链密度、管理知识资产时使用此 Skill。
  触发词：'知识图谱'、'双链'、'Obsidian'、'笔记管理'、'知识管理'、'Zettelkasten'、'第二大脑'。
  不适用于单篇笔记的内容创作（使用技术博客内容创作）。

# 个人知识图谱构建

## 🎯 目标

> 在 Obsidian 中构建高密度、高检索性、可持续增长的知识网络。

**核心价值**：知识管理的终极目标不是「记住了什么」，而是「能快速找到并连接什么」。本 Skill 将 Zettelkasten 方法与 Obsidian 特性结合，确保每篇笔记都是网络中的有效节点。

**适用场景**：
- 新笔记的结构化创建
- 已有笔记的双链补全
- 知识体系的分类与索引
- 断链修复与质量审计

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `action` | enum | ✅ | — | 操作：`create`（创建）/ `link`（补链）/ `audit`（审计）/ `reorganize`（重组） |
| `note_content` | string | ❌ | — | 笔记内容（create 时必填） |
| `target_dir` | string | ❌ | — | 目标目录 |
| `link_count` | int | ❌ | `3` | 每篇笔记的目标双链数 |

## 📤 输出

```json
{
  "status": "success|partial|failed",
  "summary": "string — 一句话执行总结",
  "creation_result": {
    "file_path": "string — 创建的文件路径",
    "frontmatter": "string — 生成的 frontmatter",
    "auto_links": ["string — 自动发现的关联笔记"],
    "suggested_tags": ["string — 建议的标签"]
  },
  "link_analysis": {
    "total_notes": "int — 总笔记数",
    "avg_links": "float — 平均双链数",
    "orphan_notes": ["string — 孤岛笔记列表"],
    "hub_notes": ["string — 高连接度枢纽笔记"]
  },
  "quality_report": {
    "frontmatter_completeness": "float — frontmatter 完整率",
    "broken_links": "int — 断链数",
    "tag_coverage": "float — 标签覆盖率"
  }
}
```

## 📋 执行步骤

### Step 1: 笔记创建（create）
1. **Frontmatter 生成** — 自动生成 title/created/tags/aliases
2. **内容结构** — 按模板组织：标题 → 核心观点 → 关联 → 来源
3. **自动链接** — 搜索语义相关的已有笔记，建议双链
4. **标签建议** — 基于内容推荐标准标签
5. **检查点**：✅ Frontmatter 是否完整？是否至少链接了 2 篇笔记？

### Step 2: 双链补全（link）
1. **孤岛扫描** — 找到链接数为 0 的笔记
2. **语义匹配** — 为孤岛笔记找到语义相关的已有笔记
3. **双向链接** — 在两篇笔记中互相添加 wikilink
4. **检查点**：✅ 每篇孤岛笔记是否至少新增 1 个链接？

### Step 3: 质量审计（audit）
1. **Frontmatter 检查** — title/created/tags 是否齐全
2. **断链检查** — wikilink 指向的笔记是否存在
3. **标签一致性** — 标签是否遵循标准体系
4. **双链密度** — 每篇笔记的平均链接数
5. **检查点**：✅ 断链是否已修复？标签是否一致？

### Step 4: 结构优化（reorganize）
1. **目录重组** — 按主题重新组织笔记目录
2. **索引页更新** — 更新 MOC（Map of Content）页面
3. **别名管理** — 为重要笔记添加 aliases
4. **检查点**：✅ 目录结构是否清晰？索引页是否更新？

## ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得删除用户已有笔记的内容
2. Frontmatter 必须包含 title/created/tags 三个必填字段
3. wikilink 必须指向存在的笔记（避免断链）

**软性约束（建议遵守）**：
1. 每篇笔记至少 3 个双链
2. 标签使用标准体系（15 维度 + 11 类型 + 6 来源）

**人工兜底点**：
- 当自动链接建议不准确时，**必须**由用户确认
- 当涉及目录重组时，**必须**先备份

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 断链过多 | >50 条 | 分批修复，优先修复高引用笔记 |
| 标签混乱 | 大量野生标签 | 批量归类到标准标签体系 |
| Frontmatter 缺失 | >30% 笔记无 frontmatter | 批量补全基础字段 |


### 降级策略
- 当数据不足时，基于已有数据给出保守建议并标注置信度
- 当无法自动化时，输出分析框架供人工填充

## 💬 沟通风格

- **网络思维**：用「节点」「连接」「密度」描述知识管理
- **自动化优先**：能自动发现的链接不手动添加
- **渐进改进**：不追求一步到位，持续迭代

## 📝 自检清单

- [ ] 新笔记是否有 ≥2 个双链？
- [ ] Frontmatter 是否完整？
- [ ] 标签是否遵循标准体系？
- [ ] 是否有定期断链检查？
- [ ] 孤岛笔记是否在减少？

## ✅ 校验验收规则

**格式校验**：
- [ ] Frontmatter 包含 title/created/tags
- [ ] wikilink 格式正确（`[[笔记名]]`）

**内容校验**：
- [ ] 双链指向语义相关的笔记
- [ ] 标签归类准确
- [ ] 索引页内容最新

**合规校验**：
- [ ] 未删除用户已有内容
- [ ] 未创建断链


### OVP 验证信号
- 核心指标趋势是否向好
- 用户使用频率是否稳定
- 输出质量是否达到预期

## 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：weekly
- **触发条件**：
  - 新增笔记 >20 篇
  - 断链率 >5%
  - 孤岛笔记增加

**版本升级触发**：
- 当新增知识图谱分析功能（如社区检测）时，升级 minor 版本

**废弃触发**：
- 当所依赖的数据源/API 停止服务时，标记为 deprecated
- 当出现明显更优的替代方案时，评估迁移并标记版本
- 当集成 AI 自动链接建议时，升级 major 版本

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-07-03 | 1.0.0 | 初始版本，基于 uLife 知识库结构定制 |

---

*关联笔记：[[DIKW 知识金字塔]] · [[个人知识管理系统]] · [[第二大脑 PKM 管理]] · [[uSkill-agent-知识孪生体深度蒸馏双链织入]]*


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

| Agent 常见借口 | 反驳 |
|--------------|------|
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
