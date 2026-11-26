---
name: uskill-agent-doc-update-sync
description: "让一次文档修改，自动牵动全库该改的地方，断链归零。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-doc-update-sync.md"
  original_id: "SKL-7105"
  version: "3.0.0"
  trust: untrusted
---

# 文档更新同步

description: |
  当用户修改了一篇笔记、需要同步更新所有关联文档与链接时使用此 Skill。
  触发词包括：'文档同步'、'更新关联'、'链接检查'、'我改了这篇笔记'、'断链修复'。
  即使用户只是说'这篇改了，别的地方要不要动'，只要意图是保持知识库一致，也应使用此 Skill。
  本 Skill 遵循 vault wikilink 规范：链接用简单格式 `[[笔记名]]`，**禁止路径格式**。

---

# 🔄 uSkill-文档更新同步-v1

> 跨模块同步更新关联文档，确保知识库链接完整、内容一致、断链归零。

## 🎯 目标

> 一次修改，牵动全库：识别所有受影响文档与断链，给出可执行的同步/修复动作。

**vault 链接规范（来自 [[AGENTS]]）**：
- wikilink 必须用简单格式 `[[笔记名]]`，**禁止** `[[笔记名]]` 这类路径格式
- 每篇笔记必须有完整 frontmatter（`title`/`created`/`tags`）
- 标签必须从标准体系取（15 维度 / 11 类型 / 6 来源 + 21 领域）

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `modified_doc` | `string` | ✅ | 被修改的文档路径或笔记名 |
| `related_docs` | `array` | ❌ | 已知关联文档列表（缺则自动扫描） |
| `change_summary` | `string` | ❌ | 本次改了什么（定义/结论/删除） |

---

## 📤 输出

```json
{
  "affected": [{"doc": "string", "impact_type": "string", "action": "string"}],
  "broken_links": [{"from": "string", "to": "string", "fix": "string"}],
  "pending_sync": [{"from": "string", "to": "string", "reason": "string"}]
}
```

---

## 🔄 执行流程

```
1. [链接扫描] → 提取修改文档中的所有 wikilink
   → 匹配模式：`[[笔记名]]` 或 `[[笔记名|显示文本]]`
   → 提取所有链接目标

2. [有效性检查] → 检查链接目标是否存在
   → 判断条件：链接目标文件是否存在？
     → 是：标记为有效
     → 否：标记为断链，进入 broken_links

3. [格式检查] → 校验 wikilink 是否合规
   → 判断条件：是否使用了路径格式 `[[笔记名]]`？
     → 是：标注为格式违规，建议改为简单格式
     → 否：通过

4. [影响分析] → 识别受影响的关联文档
   → 反向扫描：哪些文档链接到了修改的文档？
   → 判断条件：修改是否影响链接的语义？
     → 是：标注为"需同步"，列出下游文档
     → 否：标注为"无需同步"

5. [同步建议] → 生成具体同步操作
   → 断链：建议修复（建目标文档）或删除引用
   → 语义变化：建议更新引用内容
   → 新增链接：建议创建目标文档骨架
   → IF 关联文档列表缺失 → 自动扫描全库反向链接

6. [输出报告] → 影响分析 + 断链列表 + 待同步项
   → IF 无任何关联/断链 → 输出"无影响"，仍可给出格式检查结论
```

---

## 📝 Prompt 模板

### 标准同步 Prompt

```
你是文档同步 Agent。请检查并同步文档，遵守 vault wikilink 规范。

【修改文档】{modified_doc}
【关联文档列表】{related_docs}
【本次变更】{change_summary}

【检查维度】
1. 链接有效性：所有 wikilink 是否指向存在的文件
2. 格式合规：是否使用了禁止的路径格式
3. 影响分析：修改是否影响关联文档的语义
4. 同步建议：需要同步的操作列表

【输出格式】
按标准 JSON 输出，包含 affected、broken_links、pending_sync。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 关联文档列表缺失 | 自动扫描反向链接 | 基于 wikilink 全库扫描 |
| 链接格式异常 | 尝试解析 + 标注 | 跳过无法解析的链接 |
| 无关联文档 | 输出"无影响" | 仍返回格式检查结论 |
| 目标文档被删除 | 标注断链 + 建议新建或清理 | 列出所有引用点 |
| 超大库扫描超时 | 按目录分片 | 返回已扫描分片结果 |

---

## ✅ 质量自检

- [ ] 所有 wikilink 目标已验证存在/断链
- [ ] 路径格式违规已标注并给出修正
- [ ] 反向链接（下游文档）已识别
- [ ] 同步建议具体到"改哪篇、改什么"
- [ ] 未误删用户原创内容

---

## 💡 使用示例

### 示例 1：正常同步

**输入**：
```json
{
  "modified_doc": "02-BUILD/23-uWise/词条/价值投资.md",
  "related_docs": ["02-BUILD/23-uWise/词条/护城河.md", "04-Investor/投资哲学/价值投资方法论.md"],
  "change_summary": "补充了'长期持有'的定义"
}
```

**输出**：
```json
{
  "affected": [
    {"doc": "护城河.md", "impact_type": "定义引用", "action": "检查引用是否仍准确"},
    {"doc": "价值投资方法论.md", "impact_type": "框架引用", "action": "无需同步"}
  ],
  "broken_links": [],
  "pending_sync": []
}
```

### 示例 2：断链 + 格式违规（边界场景）

**输入**：
```json
{
  "modified_doc": "02-BUILD/23-uWise/词条/刻意练习.md"
}
```

**输出**：
```json
{
  "affected": [],
  "broken_links": [
    {"from": "刻意练习.md", "to": "《刻意练习》-安德斯·艾利克森", "fix": "检查目标文件是否存在，不存在则创建或删除引用"}
  ],
  "pending_sync": []
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常同步 | 识别受影响文档 |
| 2 | 断链 | 输出修复建议 |
| 3 | 无关联 | 无影响 |
| 4 | 新增链接 | 建议创建目标文档 |
| 5 | 路径格式违规 | 标注并给修正 |
| 6 | 关联列表缺失 | 自动反向扫描 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得修改 `.obsidian/` 配置目录
2. 不得删除顶层架构目录（00-META ~ 09-REFERENCE）
3. wikilink 必须用简单格式，禁止路径格式

**软性约束（建议遵守）**：
1. 优先复用已有词条，避免重复创建
2. 同步建议应尊重用户既有分类与命名

**人工兜底点**：
- 当自动合并会删除/改写用户原创内容时，**必须**转交人工确认
- 当涉及跨目录大规模重构时，**必须**先小范围验证

#### ✅ 校验验收规则

**格式校验**：
- [ ] 输出结构完整
- [ ] 所有必填参数已填充
- [ ] 输出格式符合规范

**内容校验**：
- [ ] 建议可操作
- [ ] 数据准确无虚构
- [ ] 考虑实际约束

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已识别

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 发现新的断链模式
  - vault 链接规范更新

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当有更好替代方案时，评估迁移

---

*版本：v2.0 · 2026-07-08 Gen3 升级*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
