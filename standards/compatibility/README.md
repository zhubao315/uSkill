# 格式兼容矩阵

| 格式 | 识别特征 | 加载 | 迁移方向 |
|---|---|---|---|
| skill-v1 | `skill_id` + `meta` | `load_skill` | → V2：`uskills migrate` |
| manifest-v2 | `apiVersion: uskills/v2` | `load_manifest` | 与 SKILL.md 组成双层技能 |
| agent-skill | 目录含 `SKILL.md` | `inspect_agent_skill` | 导入生成 uskill.yaml |

迁移规则：幂等、不覆盖、不静默丢字段（`MigrationReport.lossy_fields` 列出
无法用纯 Agent Skills 表达的能力）。格式检测：`standards_compat.detect_format()`。
