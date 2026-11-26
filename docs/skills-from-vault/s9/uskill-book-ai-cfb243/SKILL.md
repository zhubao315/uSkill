---
name: uskill-book-ai-cfb243
description: "把《AI交付的纪律》从一本书变成可调用的交付验收 skill。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-book-AI交付纪律.md"
  original_id: "SKL-8101"
  version: "1.0.0"
  trust: untrusted
---

# uSkill-书-AI交付纪律

description: |
  当用户要把 AI 产出变成可验收交付、或说"AI 说完成了""又返工了""帮我验收/交付"时使用。
  触发词：AI 交付、验收、任务书、三道门、回执、证据、返工、不可逆操作、签字。
  不适用于纯聊天、纯头脑风暴、没有交付物的探索。

---

⚙️ AI-Co 运行配置块
触发场景: "AI 说完成了" / "要验收" / "又返工了" / "帮我把活交付掉"
复用率预估: 高
一键调用: |
  任务书五要素 → 成本门 L0–L3 → 三道门 G0/G1/G2 → 第6章三段清单 → 证据三件套 → 人工签字
输入Schema: |
  goal: string — 一句话目标（必填）
  acceptance: array — ≥3 条可判定验收标准（必填）
  inputs: array — 原始数据/文件/上下文
  budget: object — {time, token, money}
  irreversible: array — 不可逆动作清单
输出Schema: |
  task_book: {goal, acceptance, boundary, evidence, rollback}
  decision_gate: string — 一行回执
  gates: {G0, G1, G2}
  checklist: object — 开工前10问/交付前12项/回滚5条
  evidence: {receipt, log, report}
  signoff: {required, signed_by, at}
AI可执行度: 85%（判断与验收可自动，签字必须人）

# uSkill-书-AI交付纪律

## 🎯 目标

把《AI交付的纪律》的 11 章纪律压缩成一个可调用 skill：**交付 = 可验收的变更 + 证据**。
AI 负责执行、检查、留痕；人负责定义"完成"、验收、不可逆签字。

## ✅ 适用 / ❌ 不适用

| 适用 | 不适用 |
|---|---|
| 有明确交付物的任务 | 纯聊天、纯探索 |
| 需要验收/回滚的任务 | 没有验收标准且无法定义 |
| 多步骤、跨工具任务 | 一次性、无后果的小事 |
| 不可逆操作前的检查 | 紧急救命场景（先处理，再复盘） |

## 🔄 工作流

1. **任务书**：目标 / 验收标准（≥3 条可判定）/ 边界 / 证据 / 回滚。
2. **成本门**：L0 代码 → L1 脚本 → L2 提示词 → L3 Agent，输出一行回执。
3. **三道门**：G0 格式门 → G1 一致性门 → G2 交叉门；G0 不过不落盘。
4. **三段清单**：开工前 10 问 / 交付前 12 项 / 回滚预案 5 条。
5. **证据三件套**：回执 / 日志 / 报告（预期 vs 实测分栏）。
6. **人工签字**：不可逆动作、超预算、验收标准冲突。

## 🧑‍⚖️ 人类签字点

- 删除、覆盖、批量改名、发布、付款、调仓等不可逆动作。
- 验收标准需要放宽或改变。
- 预算超限、连续重试失败、出现安全/隐私风险。

## 🚫 反模式

| 反模式 | 真相 |
|---|---|
| 把"AI 说完成了"当验收 | 它的完成是文本事件，不是现实事件 |
| 把 skill 当自动执行 | 没有签字点的自动化是风险放大器 |
| 把"测试过了"当证据 | 没有对抗的测试只是表演 |
| 把共生当依赖 | 共生的标志是你变强，不是它替你做主 |

## 🔗 相关

- [[AI交付的纪律]] — 书稿本体
- [[AI交付清单实操手册]] — 全书 API
- [[AI交付的纪律-后记]] — 翻车与边界

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
