# Agent Connectors · 官方目录与安装约束

> 基准：2026-11-25 官方公开文档核实。路径以文档为准；标记 `needs verification` 的项需在实现中保守处理，不凭猜测编码。

## Codex

**首选路径**
- Project: `<repo>/.agents/skills/<name>/SKILL.md`（从 CWD 向上扫描至仓库根）
- User: `~/.agents/skills/<name>/`（**当前规范路径**）

**Legacy fallback（仍可加载）**：`$CODEX_HOME/skills/<name>/`，默认 `~/.codex/skills`。官方贡献者确认 `~/.codex/skills` 是旧名称，行业已统一到 `~/.agents/skills`；适配器中仅作为低优先级 fallback。

**同名规则（重要）**：官方明确同名 Skill **不合并、无优先级**，两者都会出现在选择器中。适配器因此把同名不同内容视为冲突，安装前必须提示用户改名或选择目标。

**Frontmatter**：必需 `name`、`description`；额外展示/隐式调用策略在 `agents/openai.yaml`，不要把 Claude 的 `allowed-tools` 等键当作 Codex 特性。

**官方安装器**：bundled `$skill-installer`，目标已存在时**中止而非覆盖**；私钥库可用 `GH_TOKEN`/`GITHUB_TOKEN`。

来源：https://developers.openai.com/codex/skills/ · https://github.com/openai/codex/issues/14337

## Claude Code

**路径与优先级**
- Enterprise/managed（最高）：`/etc/claude-code/.claude/skills/`（Linux）
- Personal: `~/.claude/skills/<name>/SKILL.md`
- Project: `<repo>/.claude/skills/<name>/SKILL.md`（含父目录）
- 保留名：`synced`、`anthropic-skills` 不作为用户 Skill 加载

**同名规则**：enterprise > personal > project。本地 Skill 覆盖内置/同名命令。

**Frontmatter**：遵循 Agent Skills；`description` 强烈推荐（缺失时取首行）；1,536 字符截断。

**安全注意**：`~/.claude/skills/synced/` 由 claude.ai 同步托管，**手工修改会在下次同步被覆盖/删除**——适配器不把此目录作为写入目标。

来源：https://code.claude.com/docs/en/skills · https://code.claude.com/docs/en/managed-settings.md

## OpenCode

**官方发现优先级（低 → 高）**
1. built-in
2. `~/.claude/skills`（global）
3. `~/.agents/skills`（global）
4. `~/.config/opencode/skills`
5. `<project>/.opencode/skills`（project root → CWD）
6. `opencode.json(c)` 中显式 `skills: [...]` 条目

**同名**：后加载者覆盖先加载者（按 ID）。适配器把同名不同内容视为冲突，安装前预检。

**Frontmatter**：全可选，但无 `description` 不会被发现；ID 由路径派生且大小写敏感。

**兼容**：`npx skills -a opencode` 安装到项目 `.agents/skills/` 和全局 `~/.config/opencode/skills/`，不是 `.opencode/skills`。

来源：https://opencode.ai/docs/skills/ · https://opencode.ai/docs/config/

## Vercel `skills` CLI（可选外部安装器）

- 支持 18+（README 称 75+）Agent；需 Node.js 22.20+
- 语法：`npx skills add <owner/repo> --skill <name> -a claude-code -g -y`
- 默认 **symlink** 到 `.agents/skills/` 规范目录；`--copy` 独立复制
- **同名会覆盖**——建议 `--rename`；`skills-lock.json` 记录 hash
- telemetry 默认开启，可设 `DISABLE_TELEMETRY=1`

**决策**：作为**可选外部安装器**集成（`InstallAction.kind = "external-tool"`），不作为硬依赖；不自动执行 `npx`，不静默覆盖。来源：https://skills.sh · https://github.com/vercel-labs/skills

## 适配器的硬性约束

1. 安装前生成 `InstallPlan`，显示来源、目标、范围、hash 差异、冲突与回滚。
2. 未经用户确认不得执行（`plan.approved`）。
3. 目标已存在且内容不同 → 冲突，拒绝覆盖（除非显式 `--force` 且仍不覆盖内容）。
4. 禁止路径穿越；检查 symlink；Skill 内 scripts 永不自动执行。
5. 外部来源默认 `untrusted`，直到校验通过。
6. 不在测试中修改真实用户的 Agent 目录（全部临时目录）。

## `needs verification`

- 三个官方页面的最后更新日期
- Codex 同名优先级（文档称无优先级，第三方说法矛盾）
- OpenCode 系统级目录 `/etc/opencode/skills` 的优先级
- Vercel 支持 Agent 的精确数量
- Codex 是否计划移除 legacy `~/.codex/skills`
