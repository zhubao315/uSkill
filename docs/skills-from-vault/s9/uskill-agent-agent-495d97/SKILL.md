---
name: uskill-agent-agent-495d97
description: "让五维 Agent 知识源目录索引变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-五维-agent-知识源目录索引.md"
  original_id: "SKL-7014"
  version: "3.0.0"
  trust: untrusted
---

# 五维 Agent 知识源目录索引

# 五维 Agent 知识源目录索引

> **目标**：每个 Agent 可检索 ≥3 个相关目录
> **截止**：2026-08-15
> **关联**：[[2026-Q3-OKR-草稿]] · [[uSkill-agent-循环工程统一调度入口]]

---

## 一、五维 Agent 定义

| Agent | 身份 | 核心职责 | 知识需求 |
|-------|------|---------|---------|
| 🏗️ 架构师 | Agent Architect | 系统设计、技术选型、架构演进 | 架构文档、技术方案、设计模式 |
| 💰 投资人 | Treasury | 投资决策、风控管理、组合优化 | 投资记录、市场数据、风控规则 |
| 📚 终身学习者 | Scholar | 知识管理、技能提升、阅读笔记 | 读书笔记、概念词条、技能卡 |
| 🎨 生活艺术家 | Artist | 创意表达、摄影、生活美学 | 摄影作品、创意技能、生活记录 |
| 🏃 运动员 | Bio-Loop | 健康管理、训练优化、身心平衡 | 训练数据、健康指标、恢复计划 |

---

## 二、知识源目录映射

### 🏗️ 架构师 Agent

| 目录 | 路径 | 内容 | 索引状态 |
|------|------|------|:--------:|
| 架构文档 | `03-Architect/` | 架构风格、设计模式、技术方案 | ✅ |
| uSkill 智能体任务 | `02-BUILD/22-uSkill/智能体任务/` | Agent 实施手册 | ✅ |
| 循环工程 | `02-BUILD/22-uSkill/智能体任务/uSkill-循环工程*` | 7套循环架构 | ✅ |
| Twin 知识库 | `02-BUILD/22-uSkill/智能体任务/twin_index/` | 语义向量库 | ✅ |
| 知识库架构 | `00-META/` | 架构总览、诊断报告 | ✅ |

### 💰 投资人 Agent

| 目录 | 路径 | 内容 | 索引状态 |
|------|------|------|:--------:|
| 投资工具 | `04-Investor/45-投资工具/` | 风控规则、回测系统、MCP接口 | ✅ |
| 投资记录 | `04-Investor/46-投资记录/` | 持仓分析、交易复盘、策略方案 | ✅ |
| 投资哲学 | `04-Investor/41-投资哲学/` | 投资理念、方法论 | ✅ |
| 年度投资计划 | `08-CALENDAR/85-Annual-Review/2026/*投资*` | 年度投资策略 | ✅ |
| 风控参数卡 | `04-Investor/45-投资工具/投资风控Agent-熔断规则-v1.md` | CB-1/2/3规则 | ✅ |

### 📚 终身学习者 Agent

| 目录 | 路径 | 内容 | 索引状态 |
|------|------|------|:--------:|
| uRead 读书笔记 | `07-SOURCES/71-书籍/` | 1,573 本书笔记 | ✅ |
| uWise 百科词条 | `02-BUILD/23-uWise/` | 1,869 条知识词条 | ✅ |
| uSkill 技能卡 | `02-BUILD/22-uSkill/` | 365 个可复用技能 | ✅ |
| 思维模型 | `01-BRAIN/12-模型/` | 118 个思维模型 | ✅ |
| 概念库 | `01-BRAIN/11-概念/` | 2,382 个概念 | ✅ |

### 🎨 生活艺术家 Agent

| 目录 | 路径 | 内容 | 索引状态 |
|------|------|------|:--------:|
| 摄影作品 | `06-Artist/63-摄影家/` | 作品集索引 + 摄影体系 | ✅ |
| 摄影技能 | `02-BUILD/22-uSkill/创意与表达/*摄影*` | 33个摄影技能卡 | ✅ |
| 创意技能 | `02-BUILD/22-uSkill/创意与表达/` | 文案、故事、数据可视化 | ✅ |
| 葡萄酒 | `06-Artist/62-葡萄酒大师/` | 品鉴体系、笔记 | ✅ |
| 生活美学 | `02-BUILD/22-uSkill/健康与生活/` | 生活方式、习惯养成 | ✅ |

### 🏃 运动员 Agent

| 目录 | 路径 | 内容 | 索引状态 |
|------|------|------|:--------:|
| 跑步计划 | `08-CALENDAR/85-Annual-Review/2026/*跑步*` | 年度跑步计划、训练安排 | ✅ |
| 健康技能 | `02-BUILD/22-uSkill/健康与生活/` | 跑步、心率、HRV、恢复 | ✅ |
| 训练数据 | `06-Artist/64-数字人生/` | 身体数据、习惯追踪 | ✅ |
| 运动康复 | `02-BUILD/22-uSkill/健康与生活/*损伤*` | 跑步损伤预防 | ✅ |
| 生物算力 | `02-BUILD/22-uSkill/健康与生活/生物算力预警.md` | HRV预警、负荷重排 | ✅ |

---

## 三、Twin 知识库索引

### Agent → Twin 查询映射

| Agent | 推荐查询词 | 领域过滤 |
|-------|-----------|---------|
| 🏗️ 架构师 | "架构设计", "技术选型", "系统设计", "循环工程" | domain=架构 |
| 💰 投资人 | "投资决策", "风控规则", "持仓分析", "回测策略" | domain=投资 |
| 📚 终身学习者 | "读书笔记", "概念解释", "技能复用", "知识管理" | domain=学习 |
| 🎨 生活艺术家 | "摄影构图", "创意表达", "文案写作", "生活美学" | domain=艺术 |
| 🏃 运动员 | "跑步训练", "心率数据", "HRV", "恢复计划" | domain=健康 |

### Twin 查询示例

```python
from twin_vector_store import TwinVectorStore

store = TwinVectorStore()

# 架构师查询
results = store.query("循环工程调度", domain="架构", top_k=3)

# 投资人查询
results = store.query("风控熔断规则", domain="投资", top_k=3)

# 终身学习者查询
results = store.query("元认知学习方法", domain="学习", top_k=3)
```

---

## 四、索引验证

### 验证标准

每个 Agent 必须能检索到：
- ≥3 个相关目录
- ≥10 条相关记录
- 查询延迟 <1s

### 验证脚本

```python
# 验证五维 Agent 知识源索引
agents = {
    "架构师": {"dirs": ["03-Architect", "02-BUILD/22-uSkill/智能体任务"], "query": "架构设计"},
    "投资人": {"dirs": ["04-Investor/45-投资工具", "04-Investor/46-投资记录"], "query": "投资决策"},
    "学习者": {"dirs": ["07-SOURCES/71-书籍", "02-BUILD/23-uWise"], "query": "读书笔记"},
    "艺术家": {"dirs": ["06-Artist/63-摄影家", "02-BUILD/22-uSkill/创意与表达"], "query": "摄影构图"},
    "运动员": {"dirs": ["08-CALENDAR/85-Annual-Review/2026/*跑步*"], "query": "跑步训练"},
}

for agent, config in agents.items():
    results = store.query(config["query"], top_k=5)
    print(f"{agent}: {len(results)} results")
```

---

## 五、维护机制

### 更新频率

| 内容 | 频率 | 负责人 |
|------|------|--------|
| 新增目录 | 事件触发 | 各 Agent |
| Twin 蒸馏 | 每日 | Twin Agent |
| 索引验证 | 每月 | 架构师 Agent |

### 异常处理

- **目录不存在**：标记为待创建，生成骨架
- **查询无结果**：检查蒸馏是否覆盖该目录
- **延迟过高**：优化向量索引或缓存策略


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
