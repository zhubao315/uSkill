# Registry 与分发（2.0）

原则：注册中心 = **本地文件系统 + Git**，不引入数据库或服务；分发 =
**可校验的包**，不建市场不建 Web。

## 技能检索（uskills search）

```bash
uskills search "摘要" skills/            # auto：五种模式并集去重
uskills search nlp --mode tag skills/
uskills search text_summarize --mode dependency skills/   # 谁依赖它
uskills search 流水线 --mode keyword --json skills/
```

五种模式：`name`（精确/部分）、`tag`、`domain`、`keyword`（描述/名称）、
`dependency`（声明了该工具/DAG 的技能）。Python API：

```python
from core.uskills import SkillRegistry

registry = SkillRegistry("skills")
hits = registry.search("translate", mode="auto")
registry.health()   # 加载数、坏文件、重复 id —— CI 可用
```

indexer（`uskills index`）继续负责生成 Markdown 目录；检索真相只在
`registry.py` 一处。

## 技能打包（uskills package）

```bash
uskills package skills/agent-skills/code-review --output dist/
# package: dist/code-review-package.zip
# sha256:  <归档校验和>
```

zip 内置 `package.json`：格式、逐文件 sha256、兼容层说明、策略声明
（“包是惰性的，运行需要受治理运行时”）。校验离线、确定性：

```python
from core.uskills import package_skill
result = package_skill("skills/agent-skills/code-review", "dist")
```

## MCP 桥接（adapters/mcp_bridge.py）

MCP ≠ Skill：MCP 管**连接**（外部工具/数据），Skill 管**怎么做**。
桥接的唯一形态是把 MCP 工具声明注册进受治理的 `ToolRegistry`：

```python
from adapters.mcp_bridge import register_mcp_tools

register_mcp_tools(
    registry,
    mcp_session.list_tools(),            # 你的 MCP 客户端会话
    dispatch=mcp_session.call_tool,      # name, args -> result
)
```

安全默认值：MCP 工具 = 外部副作用 → 权限默认 `network`（最小权限运行时
默认拒绝）、`idempotent=False`（永不自动重试）。桥接模块自身无网络行为、
无 MCP SDK 依赖，可离线测试；传输生命周期由调用方的 MCP 客户端负责。

## 生命周期与状态

技能状态由 `governance.lifecycle`（Draft→Validated→Reviewed→Published→
Deprecated）与 `manifest.security.risk_level`（能力推导 L0–L4）共同刻画；
打包与检索都读取同一份元数据，无第二份真相。
