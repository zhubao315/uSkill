# CLI 参考

命令：`uskills <command>`（别名 `uskill`）。通用约定：文本目录参数默认
`skills/`；`--json` 输出机器可读；退出码 0 成功、1 业务失败、2 用法错误。

## 校验与标准

| 命令 | 说明 |
|---|---|
| `validate <path>` | 校验技能文件/目录（V1 + 语义 + 模板变量） |
| `schema [--target skill\|manifest\|both]` | 导出 JSON Schema（CI 校验其与代码一致） |
| `migrate <path> [--output --dry-run --force]` | legacy 技能 → 双层技能目录（幂等、列出不可表达字段） |
| `inspect <path>` | Agent Skill 包元数据与内容哈希 |
| `import-skill <path>` | 导入标准技能目录（含脚本静态安全扫描） |
| `export-skill <…>` | 导出标准 Agent Skills 目录 |

## 构建

| 命令 | 说明 |
|---|---|
| `convert <sop.md>` | SOP → 技能 YAML（规则式） |
| `build <path> [--output --domain]` | 技能候选 + IR 分类 + 质量分（产物固定 Draft，绝不自动发布） |

## 执行（受治理运行时）

| 命令 | 说明 |
|---|---|
| `run <skill> [--input k=v …] [--provider …] [--audit 文件]` | 运行技能（timeout/retry/审批/检查点真实生效；可选脱敏审计落盘） |
| `resume <run_id> [--deny]` | 审批恢复/拒绝 WAITING_APPROVAL 运行 |

Provider：`mock`、`openai-chat`、`openai-responses`、`openai-compatible`
（`USKILLS_OPENAI_BASE_URL`）、`anthropic`、`local`（Ollama）。密钥只来自
环境变量/配置，技能文件内禁止存放。

## 评测

| 命令 | 说明 |
|---|---|
| `eval --skill S --suite X [--repeats N]` | 基线对照 + 确定性断言 + 指标 |
| `… --models a,b,c` | 多模型对比矩阵 |
| `… --compare R.json --gate [--max-drop-pp 10]` | 回归门禁（回归→退出码 1，可阻断 CI） |
| `… --judge [--judge-model M]` | LLM-as-Judge（固定 rubric，隔离记录，仅参考） |
| `test --skill S --suite X [--provider …]` | 把套件当测试跑（纯断言，PASS/FAIL 退出码） |

## 检索 / 治理 / 分发

| 命令 | 说明 |
|---|---|
| `search <query> [--mode auto\|name\|tag\|domain\|keyword\|dependency --json]` | 元数据检索 |
| `list [path] [--filter Q --json]` | 列出注册表中的技能（健康异常 → 退出码 1） |
| `risk <path> [--json]` | 由真实能力推导 L0–L4 风险级别 |
| `package <path> [--output dist --force]` | 打包 zip + package.json（逐文件 sha256） |
| `audit <path> [--action A --limit N --json]` | 查看脱敏审计轨迹（`run --audit` 生成） |

## 工程

| 命令 | 说明 |
|---|---|
| `index <path> [--json]` | 生成 Markdown 技能目录 |
| `stats <path>` | 技能统计 |
| `init <name>` | 生成双层技能脚手架 |
| `doctor` | 环境与资产体检 |
