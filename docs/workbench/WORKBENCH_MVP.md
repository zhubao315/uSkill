# Workbench MVP · 本地启动与使用

> 状态：3.0 Phase 4 · 本地优先（Local-first）· 无账号、无云端数据库、无技能正文入库。

## 架构

```
workbench/
├── web/          React + TypeScript + Vite 前端（5 个核心页面）
└── server/       FastAPI 本地 API（默认仅 127.0.0.1）
```

- 技能原文件仍是唯一真相源（文件系统/Git）。
- 本地 API 只读取 Registry / RunStore / Agent 适配器，不执行 Skill、不自动安装。
- GitHub Pages 继续是公开产品站与文档站；Workbench 不是网页版 SaaS。

## 启动

```bash
# 安装可选依赖
pip install -e ".[workbench]"

# 构建前端（一次性）
cd workbench/web && npm ci && npm run build && cd ../..

# 启动（仅 loopback，打印一次性配对令牌并自动打开浏览器）
uskills workbench --skills skills --runs-dir .uskills/runs
```

输出示例：

```
uSkill Workbench  ->  http://127.0.0.1:8765/?token=<one-time-token>
Loopback only. Press Ctrl+C to stop.
```

## 五个核心页面

| 页面 | 路由 | 数据来源 |
|---|---|---|
| Dashboard | `/` | `/api/health`、`/api/skills`、`/api/runs`、`/api/agents` |
| My Skills | `/skills` | `/api/skills`（搜索 + 分类/来源/状态筛选） |
| Skill Detail | `/skills/:skillId` | `/api/skills/{id}` + `SKILL.md` 原文 |
| Agent Install Hub | `/agents` | `/api/agents`（检测、目录、已装技能） |
| Run History | `/runs` | `/api/runs`、`/api/runs/{id}` |

安装预览通过 `POST /api/install/preview` 生成 `InstallPlan`（冲突/风险/回滚），**只预览不执行**；真正安装由 CLI `install apply` 在用户确认后进行。

## 本地 API 安全边界

- 仅绑定 `127.0.0.1`；Host 必须是 loopback（TestClient 的 `testserver` 仅在测试放行）
- 每个请求必须携带 `Authorization: Bearer <配对令牌>`（进程一次性生成）
- 状态变更请求（POST/PUT/DELETE）必须带白名单 `Origin`
- 不执行 Skill 内 scripts；不写入 Agent 目录；不上传本地文件
- 配对令牌每次启动更换；刷新页面后需从启动 URL 获取

## 诚实状态

- Dashboard/My Skills/Detail/Agents/Runs 读取的是**真实 Core 数据**；服务不可用或数据为空时显示明确错误/空状态，不伪造。
- Skill Studio、Task Router、Evaluation Lab 尚未实现（Phase 5–6），前端不提供假入口。
- 运行恢复/取消通过 CLI `runs resume/cancel` 完成；Workbench MVP 以查看为主。
