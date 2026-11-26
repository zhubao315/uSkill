---
name: uskill-agent-mvp-22c741
description: "让uSkill-知识孪生体 MVP 实现路线图变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-知识孪生体-mvp-实现路线图.md"
  original_id: "SKL-7041"
  version: "3.0.0"
  trust: untrusted
---

# uSkill-知识孪生体 MVP 实现路线图

# 🧠 Knowledge Twin MVP 实现路线图

> **Q3 目标**：跑通每日自动蒸馏循环，Twin Fidelity Score ≥50%
> **时间跨度**：2026-07-01 → 2026-09-30
> **关联**：[[uSkill-agent-twin-mcp-输入契约]] · [[uSkill-agent-知识孪生体深度蒸馏双链织入]] · [[2026-Q3-OKR-草稿]]

---

## 一、架构总览

```
┌─────────────────────────────────────────────────────────────────┐
│                    Knowledge Twin System Architecture            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Layer 1: Data Ingestion               │   │
│  │  Daily Notes │ uSkill Cards │ Investment │ Dialogues     │   │
│  │  (日频)      │ (周频)       │ (事件)     │ (日频+事件)   │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                    Layer 2: Distillation Engine           │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ Chunking │→ │ LLM CoT  │→ │ Schema   │              │   │
│  │  │ Pipeline │  │ Extract  │  │ Validate │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                    Layer 3: Dual Index                    │   │
│  │  ┌──────────────┐  ┌──────────────┐                     │   │
│  │  │ Vector Store │  │ Knowledge    │                     │   │
│  │  │ (ChromaDB)   │  │ Graph (RDF)  │                     │   │
│  │  └──────────────┘  └──────────────┘                     │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                    Layer 4: Query & Serve                 │   │
│  │  MCP Server │ REST API │ Obsidian Plugin │ CLI           │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 二、Phase 1：MVP 跑通（7/1 → 7/15）✅ 已完成

### 目标
每日 ≥1 条经验自动写入 Twin，端到端 pipeline 可观测。

### 任务分解

| # | 任务 | 产出物 | 截止 | 状态 |
|---|------|--------|:----:|:----:|
| T1.1 | 搭建 Zvec 向量存储 | `twin_vector_store.py` | 7/5 | ✅ |
| T1.2 | 实现 Daily Note chunking pipeline | `twin_chunking.py` | 7/7 | ✅ |
| T1.3 | 实现蒸馏引擎 | `twin_distill_engine.py` | 7/9 | ✅ |
| T1.4 | 端到端 pipeline 测试 | 测试报告 | 7/12 | ✅ |
| T1.5 | 首批数据蒸馏（7天日记） | 29条经验入库 | 7/2 | ✅ |

### 技术选型（已落地）

| 组件 | 选型 | 理由 |
|------|------|------|
| 向量数据库 | **Zvec v0.5.0** | 本地文件式，HNSW 索引，无需服务进程 |
| Embedding | hash-based (降级) / all-MiniLM-L6-v2 (生产) | MVP 阶段用 hash-based 跑通，后续切 sentence_transformers |
| 索引 | HNSW (ef=200, m=16) | 高召回率，适合知识库场景 |
| 存储格式 | Zvec 本地文件 | 单目录，易于备份和迁移 |

### 验收标准（已达成）

```bash
# 1. 向量库初始化
python3 twin_vector_store.py
# 产出：twin_index/ 目录，Stats: {'total_docs': 0}

# 2. 蒸馏 pipeline
python3 twin_distill_engine.py --recent 7
# 产出：29 条经验入库，twin_distill_log.jsonl 记录完整

# 3. 语义查询
python3 -c "from twin_vector_store import TwinVectorStore; s=TwinVectorStore(); print(s.query('投资策略', top_k=3))"
# 产出：返回相关洞察，domain 过滤正常
```

---

## 三、Phase 2：双索引上线（7/16 → 7/31）

### 目标
向量数据库 + 知识图谱双索引跑通，Twin Fidelity Score 首次测量。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T2.1 | 知识图谱 schema 设计 | `twin_kg_schema.yaml` | 7/18 | — |
| T2.2 | RDF 三元组提取 | `twin_kg_extractor.py` | 7/22 | T2.1 |
| T2.3 | 向量+图谱联合查询 | `twin_unified_query.py` | 7/25 | T2.2 |
| T2.4 | Twin Fidelity Score 计算 | `twin_fidelity.py` | 7/28 | T2.3 |
| T2.5 | 首次 Fidelity 测量 | 测试报告 | 7/31 | T2.4 |

### 知识图谱 Schema

```yaml
# twin_kg_schema.yaml
entities:
  - type: "Concept"
    properties: [name, domain, confidence, created

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
