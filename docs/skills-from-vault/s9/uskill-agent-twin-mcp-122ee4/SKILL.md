---
name: uskill-agent-twin-mcp-122ee4
description: "让Twin MCP 输入契约变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-twin-mcp-输入契约.md"
  original_id: "SKL-7006"
  version: "3.0"
  trust: untrusted
---

# Twin MCP 输入契约

# Twin MCP 输入契约

> **用途**：定义 Knowledge Twin Agent 的 4 类输入源结构、字段 schema、蒸馏频率与优先级规则
> **关联**：[[uSkill-agent-每日领域共生循环系统]] · [[uSkill-agent-循环工程统一调度入口]] · [[2026年度目标 AI-Co Evolution]]
> **Q3 里程碑**：7/15 MVP 跑通，每日蒸馏 ≥1 条经验自动写入 Twin

---

## 架构总览

```
┌──────────────────────────────────────────────────────────────┐
│                    Knowledge Twin 蒸馏引擎                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ 📅 Daily  │  │ 🤖 uSkill │  │ 💰 投资  │  │ 💬 对话  │   │
│  │  Notes   │  │  Cards   │  │  复盘    │  │  流水    │   │
│  │ (日频)   │  │ (周频)   │  │ (周频)   │  │ (事件)   │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │              │              │              │          │
│       └──────────────┴──────┬───────┴──────────────┘          │
│                             │                                 │
│                    ┌────────┴────────┐                        │
│                    │  蒸馏 + 向量化   │                        │
│                    │  (本地 LLM)     │                        │
│                    └────────┬────────┘                        │
│                             │                                 │
│                    ┌────────┴────────┐                        │
│                    │  Twin 向量库    │                        │
│                    │  (知识图谱)     │                        │
│                    └─────────────────┘                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 源 1：Daily Notes（日记）

### 路径

```
08-CALENDAR/81-Daily-Notes/2026/YYYY-MM-DD.md
```

### 文件规模

- **总量**：~130 篇（2026-01-04 至 2026-06-26）
- **平均行数**：100-250 行/篇
- **增量**：日均 1 篇（非每日都有）

### Frontmatter Schema

```yaml
---
title: "YYYY-MM-DD"          # 必填，日期格式
created: YYYY-MM-DD          # 必填
updated: YYYY-MM-DD          # 必填
tags:                         # 必填
  - "维度/成长"               # 固定标签
  - "类型/日记"               # 固定标签
  - "来源/个人经历"           # 固定标签
---
```

### 内部结构（固定区块）

```markdown
# YYYY-MM-DD 领域共生日志与复盘    # 或 "每日日志"

## 📥 晨间计划 (08:00 AM)          # Block A：晨间计划
### 📌 建议任务一（🏗️ 架构师）      # 3 个任务 + 可选审计任务
### 📌 建议任务二（💰 投资人）
### 📌 建议任务三（📚 终身学习者）
## 📋 晨间计划状态                  # 表格：任务/身份/状态/完成时间/产出文件

## 📰 午间资讯 (12:00 PM)          # Block B：午间资讯
### 🔥 今日必读                     # 3-4 条高价值资讯
### 📊 数据速览                     # 市场指标表格

## 📝 生活记录                      # Block C：生活记录（可选）
## 全天对话流水备份                 # Block D：对话原始语料（占位）

## 🌙 晚间复盘总结                  # Block E：晚间复盘
### 完成率                         # 计划 vs 实际
### 今日洞察                       # 1-3 条核心洞察
### 明日建议                       # 1-3 条明日行动

## 🔄 循环工程执行记录              # Block F：循环状态表
```

### 蒸馏规则

| 区块 | 蒸馏频率 | 提取目标 | 优先级 |
|------|:--------:|---------|:------:|
| 晨间计划 | 日频 | 任务决策逻辑、Area→Project 映射 | P1 |
| 午间资讯 | 日频 | 市场判断、行业趋势信号 | P2 |
| 生活记录 | 日频 | 个人状态、精力模式、关系动态 | P2 |
| 对话流水 | 事件触发 | 原始思考、决策过程、情感信号 | P0 |
| 晚间复盘 | 日频 | 洞察、反思、方法论提炼 | P0 |
| 循环状态 | 日频 | 系统健康信号 | P3 |

### 提取字段

```yaml
daily_note:
  date: "YYYY-MM-DD"
  morning_tasks:
    - identity: "架构师|投资人|学习者|艺术家"
      task: "string"
      status: "done|pending|partial"
      output: "string"              # 产出文件链接
  market_snapshot:
    shanghai_index: float
    growth_index: float
    gold_price: "string"
    sentiment: "bullish|bearish|neutral"
  life_log:
    sleep_quality: "good|fair|poor"
    energy_level: "high|medium|low"
    relationships: "string"          # 关键关系动态
  evening_insights:
    - insight: "string"
      domain: "架构|投资|学习|生活"
      confidence: 0.0-1.0
  next_day_suggestions:
    - suggestion: "string"
      priority: "P0|P1|P2"
```

---

## 源 2：uSkill 技能卡

### 路径

```
02-BUILD/22-uSkill/
├── 智能体任务/           # 60 篇 Agent 实施手册
├── 投资/                 # 13 篇投资技能
├── 健康与生活/
├── 元技能/
├── 思维与认知/
├── 效率与工具/
├── 创意与表达/
└── ...（共 ~333 篇）
```

### 文件规模

- **总量**：

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
