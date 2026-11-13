# uSkill 治理规范

## 基本要求

1. 所有技能必须通过 `USkill` Schema 校验（含语义校验：模板变量必须声明、组合技能必须声明 tools）。
2. 技能应保留 `source` 字段以确保 SOP 溯源；独立创作的通用技能可省略 `source`，
   但必须能说明创建来源（导入的技能由 Manifest provenance 记录内容哈希）。
3. 技能必须声明 `control`，禁止无超时、无中断能力的黑盒执行；
   `timeout/retry` 由运行时强制执行，不依赖技能自觉。
4. 组合技能必须引用原子技能，不允许跳过基础资产层。
5. 导入的外部技能一律视为不可信数据；工具权限由运行时白名单强制执行，
   技能声明不构成授权。

## 版本策略

- Patch：描述修正、兼容性增强
- Minor：新增字段或新增技能能力
- Major：Schema 破坏性变更

## 合并门禁

- `ruff check .` 与 `mypy core/`
- `pytest`（全部基于 MockProvider，CI 无需 API Key）
- `uskills validate skills/` 与 `uskills doctor`
- `uskills schema` 重新生成且 `standards/uskill.schema.json` 保持一致
- 技能索引重新生成
- `mkdocs build --strict` 通过
- 技能改动需附带或更新 `evals/dataset.json` 评测依据
