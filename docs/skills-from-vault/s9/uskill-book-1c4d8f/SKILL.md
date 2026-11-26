---
name: uskill-book-1c4d8f
description: "把《时间的纪律》从一套日程变成一个可调用的时间运营 skill。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-book-时间的纪律.md"
  original_id: "SKL-8104"
  version: "1.0.0"
  trust: untrusted
---

# uSkill-书-时间的纪律

description: |
  当用户说"日程满了""目标又倒了""复盘断更""这周很忙但没产出""该不该接这个活"时使用。
  触发词：时间账本、目标减法、五级复盘、深度块、留白、完成率、对齐率、断更。
  不适用于单纯的任务清单整理（用 GTD/任务类 skill）。

---

⚙️ AI-Co 运行配置块
触发场景: "日程满了" / "目标又倒了" / "复盘断更" / "很忙但没产出" / "该不该接"
复用率预估: 高
一键调用: |
  账本 → 目标减法 → 五级复盘 → 深度块 → 留白 → 人机分工
输入Schema: |
  ledger: array — 时间账本（时间块/任务/价值）
  goals: array — 目标与验收线
  reviews: object — 日/周/月/季/年复盘
  deep_work: object — 深度块与打断记录
  whitespace: object — 留白与清仓日/空转日/门合日
  automation: object — 循环状态与退役记录
输出Schema: |
  config: {do, dont, whitespace}
  review: {level, finding, change}
  metrics: {completion, alignment, deep_hours, streak_break_days}
  actions: array — 删目标/降级/留白/退役循环
AI可执行度: 75%（记录/统计/提醒可自动，取舍与承诺必须人）

# uSkill-书-时间的纪律

## 🎯 目标

把《时间的纪律》的运营闭环压缩成一个 skill：**日程满了，不等于人生前进了。**
AI 负责记录、统计、提醒、复盘；人负责取舍、边界、留白、不可逆承诺。

## ✅ 适用 / ❌ 不适用

| 适用 | 不适用 |
|---|---|
| 周/月时间配置 | 单纯任务清单整理 |
| 目标减法与降级 | 无验收线的愿望清单 |
| 复盘断更重启 | 需要临床判断的拖延/抑郁 |
| 自动化分工与退役 | 无数据源的"全自动"幻想 |

## 🔄 工作流

1. **账本**：时间块 / 任务 / 价值判定；先记一周事实。
2. **目标减法**：候选 → 保留 ≤3 → 删除/降级；一票否决。
3. **五级复盘**：日 5 分钟 / 周 20 / 月 60 / 季 120 / 年半天。
4. **深度块**：保护 08:00–10:00；关闭通知；出口记录。
5. **留白**：清仓日 / 空转日 / 门合日；写进日历。
6. **人机分工**：L0–L3；没有 L2 执行的自动化就退役。

## 🧑‍⚖️ 人类签字点

- 接新目标、砍旧目标、不可逆的时间承诺。
- 自动化上线/退役、权限变更。
- 连续两季无进展的目标 → 降级或删除。

## 🚫 反模式

| 反模式 | 真相 |
|---|---|
| 把 AI 当日程秘书 | 排满不等于有产出 |
| 把 skill 当自动排满 | 留白必须由人保护 |
| 把"AI 说高效"当证据 | 完成率不是忙碌度 |
| 把共生当依赖 | 共生的标志是你的取舍变强 |

## 🔗 相关

- [[时间的纪律]] — 书稿本体
- [[时间体检清单实操手册]] — 全书 API
- [[时间的纪律-后记]] — 断更与边界

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
