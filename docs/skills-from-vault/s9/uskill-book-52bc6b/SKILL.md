---
name: uskill-book-52bc6b
description: "把《知识库工程学》从一座库变成一个可调用的知识运维 skill。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-book-知识库工程学.md"
  original_id: "SKL-8102"
  version: "1.0.0"
  trust: untrusted
---

# uSkill-书-知识库工程学

description: |
  当用户说"库乱了""笔记找不到""要体检""这篇该不该入库""AI 能不能删笔记"时使用。
  触发词：知识库运营、体检、断链、孤岛、准入、消化、拓扑、口径、软归档。
  不适用于单篇笔记的写作润色（用写作类 skill）。

---

⚙️ AI-Co 运行配置块
触发场景: "库乱了" / "笔记找不到" / "要体检" / "该不该入库" / "AI 能不能删"
复用率预估: 高
一键调用: |
  G0–G7 准入 → L0–L7 消化 → 拓扑连接 → 体检 12 项 → 应急四联 → 口径四问
输入Schema: |
  scope: string — 库/目录范围（必填）
  candidate: object — 待入库/待处理的笔记
  metrics: object — 现有体检指标与口径
  permissions: object — 读写/移动/删除边界
  baseline: object — 口径版本与时点
输出Schema: |
  gate_result: {G0..G7}
  digest_level: L0..L7
  topology: {inbound, outbound, islands}
  health: {file_score, content_score, twelve_items}
  actions: array — 合并/软归档/补链/重测
  disclosure: string — 口径披露
AI可执行度: 80%（扫描/体检可自动，删除/移动/批量改写必须人批）

# uSkill-书-知识库工程学

## 🎯 目标

把《知识库工程学》的治理链压缩成一个 skill：**收藏不是资产，架构与运营才是。**
AI 负责扫描、体检、归类、补链；人负责资产所有权、删除/移动授权、口径裁决。

## ✅ 适用 / ❌ 不适用

| 适用 | 不适用 |
|---|---|
| 库级体检与治理 | 单篇写作润色 |
| 入库/合并/退役判断 | 无权限的批量删除 |
| 断链/孤岛治理 | 纯收藏、不运营 |
| 口径冲突排查 | 需要医疗/法律判断的内容 |

## 🔄 工作流

1. **准入**：G0 格式 → G1 拓扑 → G2 反注水 → G3 去重 → G4 种子 → G5 索引 → G6 单一正本 → G7 红队。
2. **消化**：L0 原始输入 → L1 概念 → L2 模型 → L3 框架 → L4 原则 → L5 洞察 → L6 晶体 → L7 技能原子。
3. **拓扑**：新笔记入链 ≥1、出链 ≥2；孤岛三路径：桥接/重构/清理。
4. **体检**：文件级 + 内容级双分；体检 12 项；口径四问。
5. **应急四联**：sync-conflict / 0 字节 / 野生标签 / 断链 >10%。
6. **复盘**：每次治理回写一条规则；4 周未复发才算闭环。

## 🧑‍⚖️ 人类签字点

- 物理删除、批量移动/重命名、跨域写入。
- 基线/口径调整、豁免范围变更。
- AI 提出"合并/删除"建议时，必须逐条人工确认。

## 🚫 反模式

| 反模式 | 真相 |
|---|---|
| 把 AI 当收藏机 | 收藏越多，熵增越快 |
| 把 skill 当自动删库 | AI 无删除权是底线 |
| 把"AI 说"当证据 | 口径比结论诚实 |
| 把共生当依赖 | 共生的标志是你的判断变强 |

## 🔗 相关

- [[知识库工程学]] — 书稿入口（正本见 `出版/`）
- 健康度体检实操手册（`出版/第06章-健康度清单.md`）— 全书 API
- `出版/99-后记.md` — 病历与边界

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
