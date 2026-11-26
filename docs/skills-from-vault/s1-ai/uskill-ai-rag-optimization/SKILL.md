---
name: uskill-ai-rag-optimization
description: "让RAG优化变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-rag-optimization.md"
  original_id: "SKL-6857"
  version: "3.0.0"
  trust: untrusted
---

# RAG优化

description: |
  当用户需要优化 RAG（检索增强生成）系统时使用此 Skill。
  触发词包括：'RAG'、'检索增强'、'向量数据库'、'Chunk'、'Embedding'、'语义检索'。
  当用户提到"检索不准"、"回答不相关"、"幻觉严重"、"知识库查询"时，
  即使未直接说"RAG优化"，也应使用此 Skill。
  不适用于简单的关键词搜索。遇到语义检索和知识增强生成时优先使用。

---

# uSkill-903: RAG优化

## 🎯 目标

> 优化 RAG 系统的检索质量、生成忠实度和整体性能，构建可靠的知识增强 AI 系统。

**核心价值**：让 AI 基于准确的知识回答问题，减少幻觉，提升可信度。

**适用场景**：
- 企业知识库问答系统
- 文档智能检索
- 客服知识辅助
- 技术文档查询
- 研究文献分析

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `document_source` | `string` | ✅ | — | 知识来源描述 |
| `query_type` | `enum` | ❌ | `factual` | `factual` / `analytical` / `comparative` / `generative` |
| `current_issues` | `array` | ❌ | `[]` | 当前系统存在的问题 |
| `performance_target` | `object` | ❌ | — | `{accuracy, latency, cost}` |
| `tech_stack` | `object` | ❌ | — | `{embedding_model, vector_db, llm}` |

**输入约束**：
- `document_source` 应明确文档类型、数量、更新频率
- `current_issues` 应具体描述问题现象
- `tech_stack` 应列出实际使用的技术

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结 RAG 优化方案",
  "rag_id": "RG-YYYY-MMDD-NNN",

  "ingestion": {
    "chunking_strategy": {
      "method": "string",
      "chunk_size": "number",
      "overlap": "number",
      "separators": ["string"],
      "rationale": "string"
    },
    "preprocessing": ["string"],
    "metadata_enrichment": ["string"]
  },

  "indexing": {
    "embedding_model": "string",
    "index_type": "string",
    "dimensions": "number",
    "optimization": ["string"]
  },

  "retrieval": {
    "strategy": "string",
    "top_k": "number",
    "similarity_threshold": "number",
    "reranking": "string",
    "hybrid_search": "string"
  },

  "generation": {
    "prompt_template": "string",
    "context_window": "string",
    "faithfulness_check": "string",
    "citation_strategy": "string"
  },

  "evaluation": {
    "metrics": [
      {
        "name": "string",
        "target": "string",
        "measurement_method": "string"
      }
    ],
    "test_dataset": "string",
    "ablation_plan": ["string"]
  },

  "optimization": {
    "performance": ["string"],
    "cost": ["string"],
    "scalability": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 文档分析与 Chunk 策略设计

- **输入**：`document_source`, `current_issues`
- **动作**：
  1. 分析文档类型和结构特征
  2. 选择合适的 Chunk 策略
  3. 设计预处理流程
- **输出**：`ingestion`
- **分支条件**：
  - IF 文档有清晰章节结构 → 按章节分块
  - IF 文档是连续文本 → 使用滑动窗口
  - IF 文档包含表格/代码 → 使用语义分块
  - IF 文档长度差异大 → 使用自适应分块
  - ELSE → 使用默认固定大小分块
- **检查点**：✅ 应验证分块保持了语义完整性

### Step 2: 索引与 Embedding 优化

- **输入**：`ingestion`
- **动作**：
  1. 选择或微调 Embedding 模型
  2. 设计索引结构
  3. 优化向量存储
- **输出**：`indexing`
- **分支条件**：
  - IF 领域专业性强 → 考虑微调 Embedding
  - IF 数据量 > 100 万 → 使用 HNSW 或 IVF 索引
  - IF 需要多语言 → 使用多语言 Embedding
  - IF 需要低延迟 → 增加量化压缩
  - ELSE → 使用通用 Embedding + 默认索引
- **检查点**：✅ 应验证索引质量和查询性能

### Step 3: 检索策略设计

- **输入**：`indexing`, `query_type`
- **动作**：
  1. 设计检索策略（语义/关键词/混合）
  2. 选择 Top-K 和阈值
  3. 设计重排序策略
- **输出**：`retrieval`
- **分支条件**：
  - IF 查询是事实性 → 语义检索 + 精确匹配
  - IF 查询是分析性 → 混合检索 + 重排序
  - IF 查询是对比性 → 多路召回 + 聚合
  - IF 需要高召回 → 增加 Top-K + 降低阈值
  - ELSE → 标准混合检索
- **检查点**：✅ 应验证检索结果相关性

### Step 4: 生成优化与忠实度控制

- **输入**：`retrieval`
- **动作**：
  1. 设计 Prompt 模板
  2. 实现忠实度检查
  3. 设计引用策略
- **输出**：`generation`
- **分支条件**：
  - IF 需要高忠实度 → 增加"仅基于上下文回答"约束
  - IF 需要引用来源 → 设计引用格式和验证
  - IF 上下文过长 → 使用 Map-Reduce 或压缩
  - IF 上下文不足 → 标记为"信息不足"
  - ELSE → 标准生成策略
- **检查点**：✅ 应验证生成内容忠实于检索内容

### Step 5: 评估与持续优化

- **输入**：完整 RAG 设计
- **动作**：
  1. 定义评估指标体系
  2. 设计测试数据集
  3. 制定 A/B 测试方案
- **输出**：`evaluation`, `optimization`
- **检查点**：✅ 应验证评估指标可量化且覆盖关键维度

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在生成时编造检索结果中不存在的信息
2. **不得**跳过忠实度验证直接输出
3. **必须**为每个回答提供来源引用
4. **必须**在检索结果不相关时明确说明

### 软性约束（建议遵守）
1. Chunk 大小不超过 1000 tokens
2. 检索延迟 < 500ms
3. 索引更新延迟 < 5 分钟
4. 定期评估检索质量

### 人工兜底点
- 当检索结果全部不相关时，**必须**提示用户换个问法
- 当生成内容涉及敏感信息时，**必须**人工审核
- 当系统无法确定答案时，**必须**诚实说"不知道"

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
