---
name: uskill-productivity-5ee5b0
description: "让外部知识变成 uWise 百科中可检索、可织网、可复用的结构化词条，而非停留在收藏夹里。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-知识词条录入.md"
  original_id: "SKL-7082"
  version: "3.0.0"
  trust: untrusted
---

# 知识词条录入

description: |
  当用户需要将外部知识（读书、文章、对话、项目经验）结构化录入 uWise 百科词条库时使用此 Skill。
  触发词包括：'录入词条'、'知识词条'、'记一条笔记'、'存到 uWise'、'结构化这条概念'。
  即使用户只说'这条有价值'，只要意图是沉淀可复用知识，也应使用此 Skill。
  不适用于日记流水、待办清单或纯情感记录。

---

# 📚 uSkill-7082: 知识词条录入

## 🎯 目标

> 将零散外部知识转化为符合 uLife 知识库规范的结构化词条，做到「一次录入、处处可链、长期可查」。

**适用场景**：读书摘抄固化、概念卡片生成、模型/框架沉淀、项目经验归档、对话洞察记录。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `raw_source` | `string` | ✅ | 原始素材（原文、转写、截图 OCR 文本） |
| `source_type` | `enum` | ✅ | reading / project / media / dialogue / experience |
| `author` | `string` | ❌ | 来源作者（读书笔记必填） |
| `existing_links` | `array` | ❌ | 已知可关联的已存在词条名 |

---

## 📤 输出

```json
{
  "title": "string",
  "frontmatter": {"tags": ["维度/...", "类型/..."], "aliases": ["..."]},
  "summary": "string",
  "core_insight": "string",
  "wikilinks": ["相关词条1", "相关词条2"],
  "status": "已录入"
}
```

---

## 🔄 执行流程

```
1. [采集筛选] → 从 raw_source 提取高信号片段
   → 判断条件：素材是否包含可证伪的观点或可执行方法？
     → 是：标记为「核心洞察」候选
     → 否：降级为背景描述，不占主词条

2. [智慧提炼] → 从 raw_source 提炼可调用智慧（非书名/概念名镜像，O-105/O-107）
   → 规则：抽 1 个主主题智慧 + ≤3 条分论点；每条含 原文核心 / 通俗理解 / 产品启示 / 面试可提问（按需）
   → 判断条件：该智慧是否已存在于概念库/词条库（G3 先检索）？
     → 是：合并差异化视角，禁重复新建
     → 否：命名用**智慧短语**（如「可消亡部件·架构演进·分布式取舍——《凤凰架构》三条智慧」）
   → 禁止：`《书名》-作者.md` 直接进 uWise；禁套 expand_placeholders 占位句「是一个重要的知识概念…」
   → 范例：[[可消亡部件·架构演进·分布式取舍——《凤凰架构》三条智慧]]（source→真书正本）

3. [模板填充] → 套用标准 frontmatter + 操作面 section
   → 必填：title、created、tags、name、version、**source**（指向 07-SOURCES/01-BRAIN 真本）
   → 规则：tags 必须 = 1 维度 + 1 类型（+ 可选来源/项目/领域）
   → **必含 section**：`## 调用示例`（trigger/场景×3）+ `## 边界约束`（适用/不适用/失效条件）
   → 判断条件：维度标签不在 15 维度清单内？
     → 是：归入最接近的维度，禁止野生标签
     → 否：直接写入

4. [双链织入] → 写入 wikilinks 区块
   → 规则：使用简单文件名格式「词条名」，禁止路径格式
   → **source 必回链真本**；正文 ≥1 个真本 wikilink；入 01-BRAIN 新笔记出链 ≥2（G1）
   → 判断条件：目标词条是否存在？
     → 是：建立双向链接（概念稿/真本回链词条）
     → 否：先建占位词条并标注待补，避免断链堆积

5. [质量审查] → 自检合规率
   → 规则：FM 完整、标签合规、无断链、核心洞察非空
   → **非镜像校验**：title ≠ 真本标题；无占位句；含调用示例+边界约束
   → 判断条件：自检未通过？
     → 是：退回第 3 步修正
     → 否：输出结构化结果
```

---

## 📝 Prompt 模板

### 标准录入 Prompt

```
你是知识词条录入 Agent。请将以下素材结构化为 uWise 词条。

【原始素材】
{raw_source}

【来源类型】{source_type}
【作者】{author}

【录入规则】
1. 词条须是**书中/概念中提炼的可调用智慧**（1 主主题 + ≤3 分论点），禁书名/概念名镜像、禁占位句
2. Frontmatter 必填：title、created、tags、name、version、source（指向真本 wikilink）
3. tags = 1 维度 + 1 类型（+可选来源/项目/领域），禁止野生标签
4. 核心洞察须是可复用的洞察，而非原文摘抄；命名用智慧短语，禁纯书名
5. **必含 `## 调用示例`（场景×3）+ `## 边界约束`**；wikilink 用「词条名」简单格式，禁止路径
6. 范例：[[可消亡部件·架构演进·分布式取舍——《凤凰架构》三条智慧]]

【输出格式】
按标准 JSON 输出 title / frontmatter / summary / core_insight / usage_examples / boundaries / wikilinks / status。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 素材语义模糊 | 向用户追问核心观点 | 先存草稿词条标「待澄清」 |
| 同名词条已存在 | 合并差异化视角 | 追加而非覆盖 |
| 目标 wikilink 不存在 | 建占位并标注 | 断链数 +1，周更清理 |
| 标签无法归类 | 归入最近维度 | 记录待人工校准 |

---

## ✅ 质量自检

- [ ] Frontmatter 含 title/created/tags/name/version/source 且非空
- [ ] **非书名/概念名镜像**（title ≠ 真本标题；无「是一个重要的知识概念…」占位句）
- [ ] **必含 `## 调用示例` + `## 边界约束`**（uWise_fill_audit 口径）
- [ ] **source 指向真本**且正文有对应 wikilink；提炼自 source 非凭空套模板
- [ ] tags 符合「1 维度 + 1 类型」结构，无野生标签
- [ ] 核心洞察非空且非原文照搬
- [ ] wikilink 全部使用简单文件名格式
- [ ] 无新增断链（或已建占位并标注）

---

## 💡 使用示例

### 示例 1：读书概念录入

**输入**：
```json
{
  "raw_source": "《思考，快与慢》指出系统1是直觉式自动处理，系统2是需费力的理性分析。",
  "source_type": "reading",
  "author": "Daniel Kahneman"
}
```

**输出**：
```json
{
  "title": "双系统思维",
  "frontmatter": {"tags": ["维度/心理", "类型/模型"], "aliases": ["系统1", "系统2"]},
  "summary": "人类认知由直觉系统1与理性系统2构成。",
  "core_insight": "多数误判源于系统1的过度自信，关键决策应主动唤起系统2复核。",
  "wikilinks": ["元认知", "认知偏差"],
  "status": "已录入"
}
```

### 示例 2：断链防御（边界）

**输入**：
```json
{
  "raw_source": "心流是高度专注的沉浸状态。",
  "source_type": "reading",
  "author": "Mihaly Csikszentmihalyi"
}
```

**输出**：
```json
{
  "title": "心流",
  "wikilinks": ["[待建] 专注力"],
  "status": "已录入（1 条占位待补）"
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 标准读书概念 | 完整词条 + 合规标签 |
| 2 | 同名已存在 | 合并不新建 |
| 3 | 模糊素材 | 追问后存草稿 |
| 4 | 目标链接缺失 | 建占位防断链 |
| 5 | 野生标签 | 归入标准维度 |
| 6 | 无作者读书笔记 | 标注待

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
