
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

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `RG_ERROR_NO_RETRIEVAL` | 检索结果为空 | 提示用户调整查询 | 🟡 |
| `RG_ERROR_LOW_RELEVANCE` | 检索相关性 < 0.3 | 使用备选检索策略 | 🟡 |
| `RG_WARNING_HALLUCINATION` | 检测到幻觉 | 重新生成或标记 | 🔴 |
| `RG_ERROR_INDEX_CORRUPT` | 索引损坏 | 重建索引 | 🔴 |
| `RG_WARNING_LATENCY_HIGH` | 检索延迟 > 2s | 优化索引或增加缓存 | 🟡 |

### 降级策略
- 当语义检索失败时，回退到关键词搜索
- 当向量数据库不可用时，使用本地缓存
- 当生成质量差时，直接返回检索结果

---

## ✅ 校验验收规则

### 格式校验
- [ ] Chunk 大小符合策略
- [ ] 索引结构完整
- [ ] Prompt 模板语法正确

### 内容校验
- [ ] 检索结果相关性 ≥ 0.7
- [ ] 生成内容忠实度 ≥ 0.8
- [ ] 引用来源准确

### 合规校验
- [ ] 未编造信息
- [ ] 敏感内容已过滤
- [ ] 人工兜底点已标注

### OVP 验证信号
- 检索准确率 ≥ 85%
- 回答忠实度 ≥ 90%
- 用户满意度 ≥ 4.0/5.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "Chunk 策略评估",
    "prompt": "我的文档有 1000 篇技术文档，每篇 5-20 页，怎么分块？",
    "context": "document_source='技术文档', query_type=factual",
    "assertions": [
      "chunking_strategy.method 适合技术文档",
      "chunk_size 保持语义完整",
      "preprocessing 包含格式处理"
    ],
    "expected_behavior": "设计适合技术文档的 Chunk 策略",
    "critic_attack": "分块是否破坏了技术概念的完整性？"
  },
  {
    "id": "test-002",
    "name": "检索质量诊断",
    "prompt": "用户问'如何配置数据库'，但检索返回了无关的前端文档",
    "context": "current_issues=['检索不准确']",
    "assertions": [
      "retrieval.strategy 包含查询理解",
      "reranking 改善了排序",
      "提供了诊断方法"
    ],
    "expected_behavior": "诊断并修复检索不准确问题",
    "critic_attack": "是否考虑了查询歧义？"
  },
  {
    "id": "test-003",
    "name": "幻觉检测与控制",
    "prompt": "AI 回答时经常编造不存在的 API",
    "context": "current_issues=['幻觉严重']",
    "assertions": [
      "generation.faithfulness_check 有具体机制",
      "prompt_template 包含'仅基于上下文'约束",
      "提供了幻觉检测方法"
    ],
    "expected_behavior": "设计幻觉检测和控制方案",
    "critic_attack": "忠实度检查是否足够严格？"
  },
  {
    "id": "test-004",
    "name": "混合检索设计",
    "prompt": "需要同时支持精确查询和语义理解",
    "context": "query_type=analytical",
    "assertions": [
      "retrieval.hybrid_search 包含语义和关键词",
      "权重分配合理",
      "融合策略明确"
    ],
    "expected_behavior": "设计混合检索策略",
    "critic_attack": "权重是否经过验证？是否需要动态调整？"
  },
  {
    "id": "test-005",
    "name": "大规模索引优化",
    "prompt": "我有 1000 万文档需要索引，查询要快",
    "context": "document_source='大规模文档库', performance_target={latency: '<200ms'}",
    "assertions": [
      "indexing.index_type 适合大规模数据",
      "optimization 包含量化压缩",
      "检索策略考虑了效率"
    ],
    "expected_behavior": "设计大规模文档索引方案",
    "critic_attack": "索引构建时间是否可接受？更新策略如何？"
  },
  {
    "id": "test-006",
    "name": "引用策略设计",
    "prompt": "回答需要标注来源，方便用户验证",
    "context": "query_type=factual",
    "assertions": [
      "generation.citation_strategy 有具体格式",
      "引用与内容对应准确",
      "支持用户追溯原文"
    ],
    "expected_behavior": "设计可验证的引用策略",
    "critic_attack": "引用是否准确？是否覆盖了所有声明？"
  },
  {
    "id": "test-007",
    "name": "多语言 RAG",
    "prompt": "知识库包含中英文文档，查询也可能是双语",
    "context": "document_source='中英文混合文档'",
    "assertions": [
      "embedding_model 支持多语言",
      "检索策略处理语言差异",
      "生成支持跨语言回答"
    ],
    "expected_behavior": "设计多语言 RAG 方案",
    "critic_attack": "跨语言检索质量如何？"
  },
  {
    "id": "test-008",
    "name": "评估体系设计",
    "prompt": "如何衡量 RAG 系统的效果？",
    "context": "performance_target={accuracy: '>85%'}",
    "assertions": [
      "evaluation.metrics 覆盖检索和生成",
      "test_dataset 设计合理",
      "ablation_plan 有具体步骤"
    ],
    "expected_behavior": "设计完整的 RAG 评估体系",
    "critic_attack": "评估指标是否全面？是否有人工评估？"
  },
  {
    "id": "test-009",
    "name": "增量更新策略",
    "prompt": "文档每天更新，如何保持索引最新？",
    "context": "document_source='每日更新的文档库'",
    "assertions": [
      "ingestion 包含增量处理",
      "indexing 支持增量更新",
      "更新延迟在可接受范围"
    ],
    "expected_behavior": "设计增量索引更新方案",
    "critic_attack": "增量更新是否保证一致性？"
  },
  {
    "id": "test-010",
    "name": "成本优化",
    "prompt": "RAG 系统的 Embedding 和检索成本太高了",
    "context": "performance_target={cost: 'reduce 50%'}",
    "assertions": [
      "optimization.cost 有具体方案",
      "量化压缩不显著损害质量",
      "缓存策略合理"
    ],
    "expected_behavior": "设计成本优化方案",
    "critic_attack": "优化是否影响了检索质量？"
  }
]
```

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🔗 关联文档

- [[第二大脑知识系统构建]] — 知识系统架构
- [[个人知识管理系统]] — 知识管理方法论
- [[Prompt工程进阶]] — RAG 中的 Prompt 优化
- [[信息污染检测]] — AI 幻觉检测
- [[Agent架构设计模式]] — Agent 中的 RAG 集成

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：Chunk/Embedding/检索/生成/评估 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [任务类型] for [用户水平], with [约束条件], leaning toward [方法/工具]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定制。

---

## 🚫 Anti-Rationalization Table `[v3新增]`

> 来源：addyosmani/agent-skills 的核心创新

| Agent 常见借口 | 反驳 |
|--------------|------|
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
- 检查常见错误

### ⚠️ Ask first（先问再做）
- 用户意图不明确时
- 操作不可逆时
- 涉及外部系统时

### 🚫 Never do（绝对禁止）
- 不跳过验证步骤
- 不在用户未确认时执行高风险操作
- 不伪装成功（失败就上报）

---

## 🔒 Gated Workflow `[v3新增]`

> 来源：addyosmani 的门禁 + claude-skills 的 Agent Harness

```
DISCUSS → PLAN → EXECUTE → VERIFY → CLOSE
   ↓         ↓        ↓          ↓        ↓
 Context   方案     执行      证据     Done/
 Read     确认     任务      检查    Escalate
```

### Phase 1: DISCUSS
- [ ] 输出 Context Read 一行判断
- [ ] 确认用户意图
- [ ] 确认约束条件

### Phase 2: PLAN
- [ ] 制定执行方案
- [ ] 确认资源可用
- [ ] 人工审批计划

### Phase 3: EXECUTE
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功


**相关概念**：[[RAG]]

---



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功
