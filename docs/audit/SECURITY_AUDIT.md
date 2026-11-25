# 安全审计（历史快照 · v1.2 基线 · 2026-11-13）

> 文中 Sprint 3/5 缺口均已交付；当前安全模型见 SECURITY.md 与 docs/evaluation.md。

威胁模型：技能内容（SOP/SKILL.md/生成结果）= 不可信数据；运行时与权限系统
= 唯一执行边界；密钥只来自环境/配置。

## 已实现防线（v1.2，有测试）

| 控制 | 实现 | 证据 |
|---|---|---|
| 数据边界 | 系统提示词显式声明"技能文本与输入是数据非策略"；技能文本仅入 user prompt | `engine.system_prompt` + `tests/test_runtime.py::test_success` |
| 最小权限 | 工具权限白名单，默认仅 `read`；越权 `PermissionDeniedError` | `governance/policy.py` + `TestPermissions` |
| 声明≠授权 | `execute.tools` 仅声明，须注册 ToolRegistry/库内解析 | `engine._run_subskill` + `TestCompositeWorkflow` |
| 超时边界 | provider 调用与 future 双层 timeout | `engine._run_llm` + `test_provider_timeout_enforced` |
| 审批门 | `requires_approval` → WAITING_APPROVAL，resume 批准/拒绝 | `TestApproval` |
| 审计追踪 | JSONL 追加式审计（run/approval/tool 事件） | `governance/audit.py` |
| 导入溯源 | Manifest provenance 记录 sha256 与来源路径 | `agentskills.import_agent_skill` + tests |
| 发布门禁 | Draft→…→Published 生命周期枚举校验非法跳转 | `governance/lifecycle.py` |
| 密钥卫生 | 技能文件禁止存密钥（SECURITY.md + 校验无该字段通道）；provider 读环境变量 | `providers.py` |

## 风险与缺口（Sprint 3/5 处理）

1. **P1 脚本执行无静态扫描**：导入技能的 `scripts/` 不执行（正确），但导入时
   不提示"含可执行脚本"。→ `builder/scan.py` 标记 subprocess/network/eval 等
   高风险模式，写入导入报告。验收：含 `subprocess.` 的 scripts 导入必产生警告。
2. **P1 风险分级缺失**：L0–L4 需由实际能力（是否带 scripts、tools 权限、
   network 声明、requires_approval）**推导**而非作者声明。→ `governance/risk.py`。
3. **P2 审计未脱敏**：审计 detail 可能包含输入片段。→ AuditLogger 增加脱敏
   （key 名含 token/secret/key 的值掩码；输入只存摘要与长度）。
4. **P2 提示注入纵深**：当前依赖系统提示词声明。补：输入值进入模板前
   标记数据边界（如包裹 XML 定界符），并在评测集加入 injection_probe 用例。
5. **P2 重试幂等**：有副作用工具（write/shell 权限）重试需幂等键；Sprint 3 在
   ToolRegistry.invoke 增加 `idempotent: bool` 标记，非幂等工具失败不自动重试。
6. **已知边界（不伪装）**：无 OS 级沙箱；`SECURITY.md` 明确隔离由部署方负责。

## 安全测试基线

现有：permission deny、approval reject、越权 tool 解析失败、超时。
Sprint 5 新增：脚本扫描、风险推导、脱敏、注入探针用例（评测层）。
