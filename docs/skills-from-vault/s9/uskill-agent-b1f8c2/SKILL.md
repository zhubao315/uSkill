---
name: uskill-agent-b1f8c2
description: "让uSkill-自进化飞轮与循环工程整合架构变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-自进化飞轮与循环工程整合架构.md"
  original_id: "SKL-7047"
  version: "3.0.0"
  trust: untrusted
---

# uSkill-自进化飞轮与循环工程整合架构 v1

# 🔄 自进化飞轮 × 循环工程 整合架构 v1

> **系统状态：** 🟢 飞轮阶段二运行中 | **循环工程：** 7循环联动
> **核心理念：** 错题本驱动 → Few-Shot 注入 → 规则固化 → 永续进化
> **关联：** [[uSkill-agent-循环工程统一调度入口]] · [[uSkill-日程优化-v1]]

---

## 一、架构总览

```
┌─────────────────────────────────────────────────────────────────────┐
│                    自进化飞轮 × 循环工程 联合架构                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    Layer 1: 数据飞轮                          │   │
│  │                                                             │   │
│  │   ┌──────────┐    ┌──────────┐    ┌──────────┐             │   │
│  │   │ 📝 Core  │───▶│ 🔍 Agent │───▶│ 📊 Eval  │             │   │
│  │   │ Prompt   │    │ 执行     │    │ 扫描     │             │   │
│  │   └────┬─────┘    └──────────┘    └────┬─────┘             │   │
│  │        │                               │                    │   │
│  │        │    ┌──────────────────┐       │                    │   │
│  │        └────│ 🧠 人工修正      │◀──────┘                    │   │
│  │             └──────────────────┘                            │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                           │                                         │
│  ┌────────────────────────▼────────────────────────────────────┐   │
│  │                    Layer 2: 循环工程                          │   │
│  │                                                              │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐   │   │
│  │  │📅Daily │ │💰Treas │ │🧠Skill │ │🏃Bio   │ │📂Twin  │   │   │
│  │  │Loop    │ │ury     │ │Audit   │ │Loop    │ │Distill │   │   │
│  │  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                           │                                         │
│  ┌────────────────────────▼────────────────────────────────────┐   │
│  │                    Layer 3: 监控与审计                        │   │
│  │                                                              │   │
│  │  ┌──────────────────┐  ┌──────────────────┐                 │   │
│  │  │ 🌲 三层冷审计    │  │ 📈 OVP 验证      │                 │   │
│  │  │ L1/L2/L3         │  │ 指标回流          │                 │   │
│  │  └──────────────────┘  └──────────────────┘                 │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 二、目录结构

```
22-uSkill/智能体任务/
├── 00-Agent-Evals/              ← 飞轮：错题本 & 黄金样本
│   ├── golden-01.md             ← 黄金标准样本
│   ├── correction-01.md         ← 人工修正记录
│   └── ...                      ← 持续积累
│
├── .runtime-core/               ← 飞轮：运行时核心
│   ├── uSkill-Core-Prompt.md    ← 动态提示词模板
│   ├── run-orchestrator.sh      ← 飞轮编排器
│   ├── eval-scan.sh             ← 错题扫描器
│   ├── .flywheel-mode           ← 飞轮模式 (standard/audit/self-play)
│   └── .active-runtime-prompt.md ← 自动生成的运行时提示词
│
├── twin_index/                  ← Twin：向量知识库
│   └── knowledge_twin_v4/       ← Zvec v4 (日期感知+多源)
│
├── twin_vector_store.py         ← Twin：向量存储
├── twin_distill_engine.py       ← Twin：蒸馏引擎
├── twin_chunking.py             ← Twin：细粒度分块
├── twin_distill_log.jsonl       ← Twin：蒸馏日志
│
├── uSkill-循环工程统一调度入口-v1.md  ← 循环工程中央调度
├── uSkill-自进化飞轮与循环工程整合架构-v1.md ← 本文件
└── ...                          ← 其他 uSkill 文件
```

---

## 三、飞轮三阶段执行路径

### 阶段一：基础建设（✅ 已完成）

| 任务 | 状态 | 产出 |
|------|:----:|------|
| 物理目录初始化 | ✅ | `00-Agent-Evals/` + `.runtime-core/` |
| Core Prompt 模板 | ✅ | `uSkill-Core-Prompt.md` |
| 首批黄金样本 | ✅ | `golden-01.md` |
| 首批错题记录 | ✅ | `correction-01.md` |
| 飞轮编排器 | ✅ | `run-orchestrator.sh` |

### 阶段二：飞轮运转（🟢 进行中）

| 任务 | 状态 | 说明 |
|------|:----:|------|
| Few-Shot 动态注入 | ✅ | `run-orchestrator.sh` 自动从 `00-Agent-Evals/` 提取 |
| 错题本积累 | 🟢 |

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
