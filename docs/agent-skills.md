# Agent Skills 开放标准兼容

uSkill 拥抱 [Agent Skills 开放规范](https://agentskills.io/specification)
（由 Linux Foundation Agentic AI Foundation 托管），不与其竞争。

## 双层标准

| 层 | 文件 | 职责 | 可移植性 |
|---|---|---|---|
| 开放标准层 | `SKILL.md` + `scripts/` `references/` `assets/` | 技能发现、加载、指令、渐进式资料 | 任何兼容 Agent Skills 的 Agent |
| uSkill 增强层 | `uskill.yaml` | 类型化 I/O、执行模式、权限、溯源、评测 | uSkill 运行时 |

!!! warning "不要把自定义字段塞进官方 Frontmatter"
    `uskill.yaml` 是 uSkill 自有扩展，**不是**开放规范的一部分。官方
    Frontmatter 只允许 `name` `description` `license` `compatibility`
    `metadata` `allowed-tools`，校验器会拒绝其它键。

## 规范约束（校验器强制）

- `name`：1–64 字符，小写字母/数字/单个连字符，必须与父目录同名
- `description`：必填，≤1024 字符，说明做什么以及何时使用
- `SKILL.md` 正文 ≤500 行（渐进式加载原则，细节进 `references/`）
- 正文引用的 `references/…` `scripts/…` `assets/…` 路径必须真实存在

## CLI

```bash
# 脚手架（双层结构 + evals 目录）
uskills init my-skill

# 校验（自动识别是 Agent Skill 目录还是 legacy YAML）
uskills validate path/to/my-skill/

# 导入：为已有标准技能生成 uskill.yaml，SKILL.md 原样保留
uskills import-skill ./my-skill/

# 导出：legacy YAML → 标准技能目录 + 转换报告（列出无法无损表达的能力）
uskills export-skill skills/atomic/text_summarize.yaml

# 查看元数据与内容哈希
uskills inspect path/to/my-skill/

# 批量迁移 legacy 技能为双层结构（幂等、不覆盖、列出丢失能力）
uskills migrate skills/ --output skills/migrated --dry-run
uskills migrate skills/ --output skills/migrated
```

## 格式检测与 Schema 版本

`uskills.standards_compat.detect_format()` 识别三种格式：`skill-v1`（legacy
YAML）、`manifest-v2`（`apiVersion: uskills/v2`）、`agent-skill`（SKILL.md 目录）。
导出文件的规范位置与版本目录说明见 `standards/manifest/` 与
`standards/compatibility/`。

## 转换语义

- 导入**永不修改** `SKILL.md`，并在 provenance 中记录内容 sha256。
- 导出 legacy 技能时，uSkill 专属能力（类型化 Schema、权限执行、工作流
  模式、内容哈希）无法用纯 Agent Skills 表达，`inspect_compatibility()`
  会显式列出——没有静默丢数据。

## 安装目标约定

Codex 等项目级 Agent 常见发现路径是 `.agents/skills/`；本仓库自身的开发
技能即位于该目录。向其它 Agent 安装时，请以对方文档实际支持的路径为准，
不要假设所有平台一致。
