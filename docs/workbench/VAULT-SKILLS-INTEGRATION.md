# 私库技能 × Workbench × Pages · 整合价值报告

> 2026-11-26 · 10 轮测试迭代结论

## 规模与来源

- 源：私有 `zhubao315/obsidian-vault` @ `02-BUILD/22-uSkill`，**570 个技能**（S1–S9 + 创意与表达）
- 转换：每个技能 → 标准 Agent Skill 目录（`SKILL.md` + `references/source.md` + `references/source-metadata.md`）
- 发布：`docs/skills-from-vault/**` 由 MkDocs 发布到 `https://zhubao315.github.io/uSkill/skills-from-vault/`
- 目录页：`https://zhubao315.github.io/uSkill/generated/vault-skills/`

## 10 轮测试迭代结果

| 轮次 | 检查 | 发现 → 修复 |
|---|---|---|
| 1 | 产物格式 | 570 SKILL.md 格式完整、索引一致 |
| 2 | Registry 发现 | **发现 bug**：中文 name 折叠导致仅 461/570 → ASCII slug + hash 后缀；`index.json` 误加载 → 移出技能树；`version` 非官方键 → 移入 metadata。最终 570/570、0 broken |
| 3 | 内容完整性 | 原文与 frontmatter 完整保留；6 个文件脱敏；敏感 0 命中 |
| 4 | Workbench API | API 默认 limit=500 会漏 70 个 → 提到 2000 |
| 5 | Pages 链接 | **1140 个链接全断**（相对路径解析错误）→ 改绝对路径 `/uSkill/skills-from-vault/...`，0 断链 |
| 6 | 内容质量 | 234 个空壳、97 个兜底描述 → 正文扩到 4000 字符、描述用 title/vibe，0 空壳 |
| 7 | 幂等性 | `generated_at` 导致每周空提交 → 内容未变时沿用旧时间戳，字节级幂等 |
| 8 | 远端状态 | 发现推送因并发重建目录失败 → 重新一次性推送 |
| 9 | 自动化 | 工作流语法、PAT secret、私库读权限全部验证 |
| 10 | 价值整合 | 见下 |

## 三层价值

### L1 · 内容资产（已实现）
570 个技能以开放标准格式进入公开仓库，**原文一字不丢**、来源与版本可追溯。这比"只发一份 Markdown 列表"有价值得多：每个技能可被 Codex / Claude Code / OpenCode 直接发现和使用。

### L2 · Workbench 操作（已实现）
Registry 3.0 已能发现全部 570 个技能；`uskills workbench` 的 My Skills / Detail 页面可直接查看、搜索、筛选、安装预览。私库技能从"躺在笔记里"变成"可操作资产"。

### L3 · 持续运营（已实现）
每周一 03:37 UTC 自动同步；内容不变不提交；变更后 Pages 自动重新发布。个人技能库成为一个**活的、自更新的产品**，而不是一次性快照。

## 进一步优化建议（按价值）

1. **搜索增强**（高价值/中成本）：570 个技能的 `description` 来自 `vibe`，适合做关键词检索；Workbench 已有 12 种元数据搜索模式，下一步可加全文搜索索引。
2. **健康度门禁**（高价值/低成本）：在同步工作流中调用 `uskills doctor` 与 `validate`，把 broken/重复/缺描述的技能生成报告，每周一随同步产出。
3. **分类映射优化**（中价值/低成本）：`s9-专业领域与智能体` 有 169 个技能，占 30%；可按 `domain` frontmatter 做二级分类，提升 Discover 体验。
4. **Stats 页面**（中价值）：570 技能的来源分布、版本分布、最近更新，让"我的技能资产"可量化。
5. **安装热度反馈**（长期）：Workbench Install Hub 记录安装到哪个 Agent，回流到技能详情，形成"哪些技能真的被用"的证据——这正是 uSkill 差异化的核心（Trust/Effectiveness 分离）。

## 诚实边界

- 转换是**格式转换与发布**，不是质量升级；源技能质量参差，质量分数是启发式，不代表真实效果。
- 所有条目标记 `trust: untrusted`；脚本永不自动执行。
- 隐私：6 个文件经自动脱敏（飞书 token、私库路径、用户名）；原始敏感信息未进入公开仓库。
- 许可证：源 frontmatter 无 license 字段，统一按仓库 MIT 发布；如需逐技能授权需人工决定。
