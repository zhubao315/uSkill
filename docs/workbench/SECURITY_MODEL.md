# 安全模型

> 威胁模型（`docs/audit/SECURITY_AUDIT.md:3-4`）：技能内容（SOP / SKILL.md / 生成结果）= **不可信数据**；运行时 + 权限系统是**唯一执行边界**；密钥只来自环境/配置（`providers.py:295-315`）。状态标记：`已实现` / `部分实现` / `未实现` / `需要验证`。

## 1. 已实现的九道防线（有测试）

| # | 控制 | 证据 | 状态 |
|---|---|---|---|
| 1 | 数据边界：系统提示词声明「技能文本与输入是数据非策略」，技能文本只入 user prompt | `engine.py:190-193,666-669`；`SECURITY_AUDIT.md:10` | 已实现 |
| 2 | 最小权限：白名单默认仅 `read`，越权 `PermissionDeniedError` | `governance/policy.py:11-38`；`tools.py:89-104` | 已实现 |
| 3 | 声明≠授权：`execute.tools` 仅声明，须注册并解析 | `engine.py:741-766`；`SECURITY_AUDIT.md:12` | 已实现 |
| 4 | 超时边界：provider future + 线程级双层 timeout | `engine.py:670-687`、`tools.py:95-104` | 已实现 |
| 5 | 审批门：`requires_approval → WAITING_APPROVAL`，resume 批准/拒绝 | `engine.py:331-335,370-382,270-319` | 已实现 |
| 6 | 审计追踪：JSONL 追加式 run/approval/tool 事件 | `governance/audit.py:42-76`；`engine.py:232-233,280-283,640` | 已实现 |
| 7 | 导入溯源：`content_sha256` + 来源路径，`untrusted_source=true` | `agentskills.py:53-57,240-249`；`SECURITY_AUDIT.md:16` | 已实现 |
| 8 | 发布门禁：五态生命周期，非法跳转拒绝 | `governance/lifecycle.py:14-53` | 已实现 |
| 9 | 密钥卫生：技能无密钥字段通道；provider 从环境读 key | `providers.py:295-315,149-160`；`SECURITY_AUDIT.md:18` | 已实现 |

## 2. 风险 L0–L4 的推导（`已实现`）

`governance/risk.py:19-33` 定义 L0 纯文本、L1 只读数据处理、L2 受限工具、L3 脚本/写文件/shell、L4 外部系统/敏感数据。`assess_skill_risk()`（`:49-83`）从**真实能力**推导：目录含 `scripts/` → ≥L3（`:65-67`）；可达工具 → ≥L2（`:69-72`）；write/shell → ≥L3（`:73-75`）；network/sensitive_data → ≥L4（`:76-78`）；`requires_approval` 只记缓解因素（`:80-81`）。

关键规则：**未注册的工具声明不升级风险**——`tool_permissions_for()` 只收集 registry 中可解析的工具（`:96-107`），注释明言「Unregistered declared tools do NOT raise the level」（`:58-60`）。CLI `risk`（`cli:479-542`）；`docs/evaluation.md:114-115` 同述。L1 在推导中实际由 L2 工具面覆盖（`docs/evaluation.md:109`）——**需要验证**业务口径。验收 AC-GOV-04。

## 3. 导入扫描（信号，不是沙箱）

`builder/scan.py:1-8` 明示：扫描是信号不是沙箱，发现不静默阻断导入，而是进入报告 + 抬高推导风险 + 标记不可信；部署隔离由部署方决定。模式表（`:19-50`）：`process-exec`（L3）、`dynamic-code`（L3）、`file-write`（L3）、`network`（L4）、`env-secrets`（L4）；只读 `.py/.sh/.js/.ts/...` 后缀（`:52,75-103`）。导入路径 `agentskills.py:200-222`：`untrusted_source=true`、`risk_level=L{...}`，并在 notes 写「scripts are NEVER executed by uSkill」；运行时不执行 `scripts/`（`docs/runtime.md:100-105`）。验收 AC-GOV-04。

## 4. 审计脱敏（已实现）

`governance/audit.py:19-21`：`_SENSITIVE_KEY = token|secret|key|password|credential|api[-_]?hdr`，`_BULK_KEYS = input|inputs|prompt|output|outputs|text|body`，掩码 `***REDACTED***`。`redact()`（`:24-39`）对大块值只存 `{sha256: 前16位, length, note}`；完整输入只留在运维控制路径的 RunRecord（`audit.py:5-7`），不进审计流。CLI `audit` 输出同样脱敏（`cli:590-612`）。验收 AC-GOV-04、AC-WB-06。

## 5. MCP 默认姿态（已实现）

`adapters/mcp_bridge.py:11-14,32-40`：MCP 工具视为外部副作用，默认 `permission=network`（最小权限运行时默认拒绝）且 `idempotent=False`（永不自动重试）；桥接本身无网络、无 MCP SDK 依赖（`:1-9`），传输由调用方客户端管理（`docs/distribution.md:61-63`）。验收 AC-GOV-04。

## 6. 不伪装的安全边界

| 边界 | 真实状态 | 证据 |
|---|---|---|
| OS 级沙箱 | **未实现**（无沙箱）；隔离由部署方负责 | `SECURITY_AUDIT.md:33`、`PRODUCT_CHARTER.md:31`（原 `SECURITY.md` 不在本快照，精确行号**需要验证**） |
| 部署隔离 | 责任在部署方，不是库能力 | `SECURITY_AUDIT.md:6`、`PRODUCT_CHARTER.md:31` |
| 提示注入纵深防御 | **部分实现**：当前仅系统提示词声明 + 导入 `<sop>` 数据定界（`ai_converter.py:102-113`）+ 注入探针字段（`evaluation.py:97-99`）；XML 定界符通用化与更多探针仍规划中 | `SECURITY_AUDIT.md:29-30` |
| 审计脱敏 | 已实现（见 §4），但 RunRecord 明文需运维自控路径 | `audit.py:5-7` |
| 步骤级崩溃幂等重放 | **未实现** | `REPOSITORY_AUDIT.md:49` |

## 7. Local Workbench API 安全要求（规划，未实现）

Workbench 3.0 若引入本地 API/HTTP 层，必须满足以下**尚未实现**的要求：

1. 仅绑定 `127.0.0.1`，不得监听 `0.0.0.0`（未实现）；
2. 配对 token（pairing token）才能访问本地端口（未实现）；
3. `Origin` 允许列表校验，阻断任意站点浏览器调用（未实现）；
4. CSRF 防护（状态变更需 token/同源校验）（未实现）；
5. 不提供任意远程访问——无公网暴露、无反向隧道、无远端控制面（未实现）；
6. 不得把密钥写入技能文件或前端状态；沿用 provider 环境变量边界（已实现底座：`providers.py:295-315`）。

验收锚点：AC-WB-06（无敏感数据泄漏）、AC-WB-01（本地启动）。CI 安全门禁现状：`pip-audit` **非阻塞**（`ci.yml:122-135`，`continue-on-error: true` + `|| true`）——建议改为阻塞，见 AC-CI-10。
