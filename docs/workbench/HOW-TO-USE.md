# 怎么用这套系统（一页速查）

> 你现在有三层入口：**公开网站**、**命令行**、**本地工作台**。按场景选一个即可。

## 1. 只想看内容 → 公开网站（无需安装）

| 想做什么 | 去哪里 |
|---|---|
| 个人品牌 / 旗舰作品 | https://zhubao315.github.io/ |
| 全部 67 个公开仓库目录 | https://zhubao315.github.io/repositories/ |
| 深度阅读系统 uRead | https://zhubao315.github.io/uRead/ |
| **私库同步的 570 个技能** | https://zhubao315.github.io/uSkill/generated/vault-skills/ |
| 某个技能的原文 | 上页点技能名 → `SKILL.md`，点「原文」→ `source.md` |
| uSkill 产品文档 / Workbench 说明 | https://zhubao315.github.io/uSkill/ |

在技能总览页顶部的搜索框输入关键词（如「投资」「知识管理」「RAG」）即可实时筛选 570 个技能。

## 2. 想让 Agent 用技能 → 安装到 Codex / Claude / OpenCode

技能已是标准 `SKILL.md` 格式，Three Agents 可直接发现。用 CLI 查看与预览安装：

```bash
# 看本机装了哪些 Agent、各有多少技能
uskills agents detect
uskills agents list

# 预览安装计划（只显示，不写入！）
uskills install preview docs/skills-from-vault/s5/uskill-cognition-cognitive-deep-reading-knowledge-management \
  --agent opencode --scope user

# 确认无误后再真正安装（会显示冲突/风险/回滚）
uskills install apply <同一路径> --agent opencode --scope user
```

**安全规则**：默认不覆盖已存在技能；同名不同内容视为冲突；脚本永不自动执行。

## 3. 想管理自己的技能资产 → 本地 Workbench（图形界面）

```bash
pip install -e ".[workbench]"          # 一次性装本地服务依赖
cd workbench/web && npm ci && npm run build && cd ../..   # 一次性构建前端
uskills workbench                       # 启动，自动打开浏览器
```

浏览器打开后（地址含一次性配对令牌）：

| 页面 | 能做什么 |
|---|---|
| Dashboard | 技能总数、最近运行、Agent 状态 |
| My Skills | 搜索/筛选全部 570 个技能，按分类/来源/状态 |
| Skill Detail | 看 `SKILL.md` 原文、元数据、安装预览 |
| Agent Install Hub | 看三个 Agent 的检测状态与已装技能 |
| Run History | 看技能运行记录与详情 |
| Studio | 粘贴 SOP/Markdown → 生成 Draft 技能（不发布、不执行脚本） |
| Eval Lab | 看评测套件/报告，对比基线（mock 与真实结果明确区分） |

服务默认只监听 `127.0.0.1`，每次启动换新令牌，不上传任何本地文件。

## 4. 想让技能持续更新 → 每周自动同步

`.github/workflows/sync-vault-skills.yml` 每周一 03:37 UTC 自动从私库 `02-BUILD/22-uSkill` 同步 570 个技能：
- 内容有变化 → 自动提交 + Pages 重新发布
- 内容没变化 → 不提交、不部署（幂等）

也可手动触发：`gh workflow run sync-vault-skills.yml -R zhubao315/uSkill`

## 5. 想深度读一本书 → 用两个阅读技能

你的技能库里有两个专门的方法论：
- `s5/uskill-cognition-cognitive-deep-reading-knowledge-management`（五阶段：预读→精读→萃取→整合→管理）
- `s5/uskill-cognition-cognitive-intensive-reading-methodology`（强力研读法：只留骨头不留肉）

直接看：https://zhubao315.github.io/uSkill/skills-from-vault/s5/uskill-cognition-cognitive-intensive-reading-methodology/SKILL/

按它的 Step 1–5 走：侦察 → 提取知识点 → 知识晶体 → 跨书连接 → 验证（30 秒讲清楚）。

## 一句话总结

**看** → Pages 网站；**用** → `uskills install`；**管** → `uskills workbench`；**更新** → 每周自动同步；**读** → 用认知类技能的方法论。
