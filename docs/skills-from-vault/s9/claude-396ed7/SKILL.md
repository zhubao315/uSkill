---
name: claude-396ed7
description: "CLAUDE 三级配置规范"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/CLAUDE-三级配置规范.md"
  original_id: ""
  version: ""
  trust: untrusted
---

# CLAUDE 三级配置规范

# CLAUDE 三级配置规范

> **D-A1-01 交付物** | v6.0-Graph P1 冷启动
> **定位：** 全局 → 域 → 项目三级配置规范，确保每次 Agent 启动时携带正确的上下文边界
> **验收标准：** 三级配置文档完整覆盖 6 个身份域；Agent 初始化时上下文准确率 ≥ 95%

---

## 一、架构总览

```
L0 ─ 全局 CLAUDE.md (vault 根目录)                    ← 每次会话自动加载
│    ├── 知识库结构（目录/标签/命名规范）
│    ├── 6 身份域定义 + 域切换判定规则
│    ├── 输出约束
│    ├── 诊断脚本入口
│    └── 转录本回写触发配置入口
│
├── L1 ─ 域级上下文 (22-uSkill/.runtime-context/)     ← 按域切换按需加载
│    ├── architect.md   (架构师)
│    ├── investor.md    (投资人)
│    ├── scholar.md     (终身学习者)
│    ├── artist.md      (生活艺术家)
│    ├── creator.md     (创作者)
│    └── runner.md      (健身跑者)
│
└── L2 ─ 项目级配置 (各项目目录)                       ← 项目激活时加载
     ├── 循环工程调度入口 (L2-循环工程.md)
     ├── uGenesis 沙盒 (L2-uGenesis-Lab.md)
     └── 每日 Loop (L2-每日Loop.md)
```

### 配置继承关系

```
L0 (不可变) ──继承──→ L1 (域级) ──继承──→ L2 (项目级)
    ↑                    ↑                    ↑
  全局约束            域特定约束           项目特定约束
  每次加载            域切换时加载         项目激活时加载
```

**冲突解决：** L2 > L1 > L0。低层级的约束不可被高层级覆盖，除非明确标注 `# override`。

### 与现有文档的关系

| 文档 | 层级 | 关系 |
|------|:----:|------|
| `CLAUDE.md` (vault root) | L0 | 三级配置的全局层，Agent 每次启动自动读取 |
| `AGENTS.md` (vault root) | 元 | 智能体操作手册——硬约束、标签体系、诊断工具索引。L0 的补充来源 |
| `CONVENTIONS.md` (`02-BUILD/24-项目支持/规范与标准/`) | 元 | 系统核心公理——四大不可变公理 + 人机权责边界。L0 的哲学层 |
| `2026年度目标...` | 战略 | 年度目标主文件 §9.7 数据契约层——GlobalState Schema、Reducer、Event Log |

**加载顺序：** L0 → (按需) L1 → (按需) L2。`AGENTS.md` 和 `CONVENTIONS.md` 作为元约束常驻。

---

## 二、L0：全局配置

**位置：** `vault-root/CLAUDE.md`
**行数：** 80 行 | **Token 估算：** ~2,500
**加载策略：** 每次 Agent 首次会话自动加载，通过 prompt cache 常驻上下文

### L0 板块清单

| 板块 | 内容 | 行数 | 状态 |
|------|------|:----:|:----:|
| 目录结构 | 10 大顶层目录 + 22-uSkill + 29-uGenesis-Lab | 12 | ✅ |
| 禁止目录 | 8 个受保护路径 | 1 | ✅ |
| Frontmatter 规范 | title/created/tags 必填 | 8 | ✅ |
| 标签白名单 | 15 维度 + 11 类型 + 6 来源 + 21 领域 | 5 | ✅ |
| 文件命名规范 | 5 类命名格式 | 5 | ✅ |
| WikiLink 规范 | 简单格式 + 存在性校验 | 2 | ✅ |
| 6 身份域表 | 域值/目录/触发场景 | 8 | ✅ |
| 输出约束 | 5 条不可变约束 | 5 | ✅ |
| 诊断脚本 | 5 个核心脚本入口 | 5 | ✅ |
| **域切换判定** | **关键词→域映射 + 混合域处理** | — | ⬜ **待补** |
| **转录本回写入口** | **采样 cron + 归因→配置更新** | — | ⬜ **待补** |

### 域切换判定规则（L0 新增板块）

Agent 收到用户输入后，按以下优先级判定身份域：

| 优先级 | 判定方式 | 示例 |
|:------:|---------|------|
| 1 | 用户显式指定 `/architect` `/investor` 等 | `/investor 分析茅台` |
| 2 | 关键词精确匹配（见下表） | "全马配速" → `runner` |
| 3 | 目录路径推断（输入中包含目录名） | "04-Investor 下的…" → `investor` |
| 4 | 默认域（最近一次使用的域） | 无明确信号时沿用上次域 |

**关键词→域映射表：**

| 域 | 触发关键词（不穷举） |
|:--:|---------------------|
| `architect` | 架构、系统设计、图工程、循环、DAG、Schema、ADR、技术选型 |
| `investor` | 投资、持仓、收益、回撤、风控、调仓、股票、基金、贵金属 |
| `scholar` | 读书、笔记、概念、词条、uWise、uRead、蒸馏、知识图谱 |
| `artist` | 生活、健康、摄影、酒、葡萄酒、美学、创作、灵感 |
| `creator` | 写作、文章、博客、公众号、小红书、内容、草稿 |
| `runner` | 跑步、训练、配速、心率、HRV、全马、马拉松、LSD、间歇 |

**混合域处理：** 当输入同时触发多个域时，取关键词命中数最多的域。若并列，按 `runner > artist > investor > scholar > creator > architect` 优先级（身体 > 生活 > 财务 > 知识 > 创作 > 架构）。

### 转录本回写触发配置（L0 新增板块）

```
# 转录本挖矿配置（D-A1-03 前置）
# 位置：09-REFERENCE/93-脚本/transcript_mining_config.md
# 触发：每周日 02:00 cron
# 流程：采样 → Top-5 归因 → 根因映射到 L0/L1/L2 → 自动回写 → 下轮验证
```

---

## 三、L1：域级上下文

**位置：** `22-uSkill/.runtime-context/{domain}.md`
**行数：** 每文件 20-30 行 | **Token 估算：** ~800/文件
**加载策略：** Agent 启动后根据域切换判定规则加载对应域上下文。非活跃域不加载。

### 6 身份域完整映射

| 域值 | 身份 | 核心目录 | 循环工程 | 工具链 | OVP 信号 |
|:----:|------|---------|---------|--------|---------|
| `architect` | 架构师 | `03-Architect/` | 循环 2（技能审计）+ 循环 6（全局审计） | `baoyu-diagram` `senior-architect` | A 类 uSkill ≥300，复用率 ≥30% |
| `investor` | 投资人 | `04-Investor/` | 循环 1（财务红队） | `zhengxi-views` `invest-review` `stock-analyzer` | 月收益 ≥+8万，胜率 ≥65% |
| `scholar` | 终身学习者 | `05-Scholar/` | 循环 5（知识蒸馏） | `reading-pipeline` `baoyu-format` | 词条 ≥1000，保真度 ≥70% |
| `artist` | 生活艺术家 | `06-Artist/` | 循环 4（关系网络） | `baoyu-article-illustrator` `baoyu-post-to-wechat` | LQS ≥70，摄影 ≥50 张 |
| `creator` | 创作者 | `07-Creator/` | — | `writing-shape` `baoyu-image-gen` `baoyu-infographic` | 深度内容 ≥4 篇/月 |
| `runner` | 健身跑者 | `02-BUILD/25-运动/` | 循环 3（身心循环） | `running-cycle` | 全马 Sub4:00，体脂 ≤19% |

### L1 文件标准

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
