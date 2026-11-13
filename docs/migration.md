# 从 1.x 迁移到 2.0

**结论先行：技能文件不需要任何修改。** uSkill 2.0 的全部格式变更都是
可选增量字段（`SCHEMA_VERSION` 保持 1.1.0）；1.x 写的技能照常加载、校验、
执行。本指南面向两类人：只想升级包的人，和想用上新能力的维护者。

## 升级步骤

```bash
pip install -e ".[dev]"        # 或 pip install --upgrade uskills
uskills doctor                 # 环境 + skills/ 资产体检
uskills validate skills/       # 存量资产必须全绿（向后兼容是契约）
```

2.0 新增核心依赖 `jsonschema`（输出契约校验用），`pip install -e .` 会自动带上。

## 你会直接观察到的行为变化

| 变化 | 说明 | 是否破坏性 |
|---|---|---|
| 审计日志脱敏 | 敏感键掩码、大块值存 sha256 摘要 | 否（读日志方式不变） |
| 导入含脚本的技能 | 自动静态安全扫描，报告写入 notes 与 `manifest.security.risk_level` | 否（只增信息） |
| 组合技能 `tools` 解析失败 | 明确报错（1.2 已如此）；现在支持 `depends_on` 可选 DAG | 否 |
| `mock` Provider 默认响应 | 仍是 `"{}"`，可用 CLI `--mock-response` 脚本化 | 否 |

## 可选新能力（按需启用）

### 1. 参数约束与输出 Schema

```yaml
input:
  params:
    - {name: priority, type: string, enum: [low, high]}
output:
  format: json
  schema: {type: object, required: [summary]}
```

运行时在模型调用前强制约束；输出全量 Schema 校验 + 有限修复环
（`control.repair`，默认 2）。不加这些字段 = 行为与 1.x 一致。

### 2. legacy 单文件 → 双层技能目录

```bash
uskills migrate skills/atomic --output skills/migrated --dry-run   # 先看报告
uskills migrate skills/atomic --output skills/migrated             # 幂等迁移
```

迁移报告会列出无法用标准 SKILL.md 表达的 uSkill 专有字段（不静默丢弃）。

### 3. 评测与发布门禁

```bash
uskills eval --skill s.yaml --suite s.suite.json --format json --output run.json
uskills eval --skill s.yaml --suite s.suite.json --compare run.json --gate
```

回归（此前通过的用例现在失败，或成功率跌幅 > `--max-drop-pp`）→ 退出码 1。

### 4. 检索 / 打包 / 风险分级

```bash
uskills search nlp --mode tag skills/
uskills package skills/agent-skills/code-review --output dist/
uskills risk skills/ --json
```

## 版本号语义

- 包版本：`core/uskills/_version.py` 唯一来源（2.0.0）。
- 技能格式：`SCHEMA_VERSION = 1.1.0` 不变——2.0 的字段全部可选。
- Manifest：`apiVersion: uskills/v2` 不变（自 1.2 起就是这个值）。

## 遇到问题

`uskills doctor` 检查环境与资产；`uskills audit <jsonl>` 查看脱敏后的运行
审计轨迹。破坏性变更只可能出现在主版本，且会先走 Deprecated 流程。
