# 生态对标审计（历史快照 · 2026-11-13 · v1.2 vs 2.0 计划）

> 表中"2.0 计划"的多模型对比、回归门禁、MCP 桥接、package 均已交付。

对象：Agent Skills 开放规范、OpenAI Codex Skills、Anthropic Agent Skills、
MCP、评测实践。对比基于公开文档，不代表产品功能完全同构。

## 维度对比

| 维度 | 业界做法 | uSkill v1.2 | 2.0 计划 |
|---|---|---|---|
| 技能格式 | SKILL.md 目录 + frontmatter（name/description） | ✅ 双层：SKILL.md + uskill.yaml（manifest V2） | Manifest JSON Schema 导出、migrate |
| 发现/加载 | 渐进披露：先 name/desc，触发后载正文，需要时读 references/scripts | 校验器强制 ≤500 行 + 引用检查 | 加载器（按层读取）为 Agent 侧行为；uSkill 提供 lint 辅助 |
| 执行 | 宿主 Agent 解释 SKILL.md；scripts 由宿主执行 | ✅ 自有 Runtime：真实 timeout/retry/审批/检查点/子技能调度 | cancel/backoff/DAG 并行/输出修复环 |
| 工具连接 | MCP 提供外部工具/数据；Skill 描述怎么做 | ToolRegistry+权限白名单（read/write/network/shell） | MCP 桥接适配器（把 MCP 工具注册进 ToolRegistry） |
| 参数契约 | 无统一强制（多为约定） | ParamType 枚举 + 输入治理 | 完整 JSON Schema 约束（enum/min/max/regex）+ 输出 Schema 校验与修复环 |
| 评测 | 先建基线再写技能；真实任务回归 | ✅ 基线对照 + 确定性评分器 + CLI | 多模型对比、版本回归门禁、LLM-as-Judge 隔离记录 |
| 治理 | 权限审批、审计 | policy/audit/lifecycle | 风险分级 L0–L4（能力推导）、脚本扫描、审计脱敏 |
| 分发 | Codex `.agents/skills/`；跨 Agent 可移植 | 标准导入/导出 | `package` 打包 + checksum + 安装目标 |

## 关键判断（与任务书一致）

1. **不重新发明 Agent Skills**：官方结构/字段/命名规则已冻结进校验器
   （`agentskills.py`），冲突以官方为准。
2. **MCP ≠ Skill**：MCP 管连接，Skill 管方法。uSkill 的 ToolRegistry 是统一
   执行点；MCP 客户端适配器在 Sprint 5 以"工具注册"方式接入，不引入完整
   MCP server 依赖。
3. **评测是核心差异化**：基线对照已进入 CLI 与 CI 可执行范围；多模型对比
   矩阵（Skill × Model）在 Sprint 4 落地。
4. **不建市场不建 Web**：分发=可校验的包与 Git 仓库；符合"轻量、可安装、
   可测试、可独立运行"原则。
