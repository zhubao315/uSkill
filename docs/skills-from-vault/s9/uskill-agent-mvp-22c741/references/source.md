
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
    properties: [name, domain, confidence, created_at]
  - type: "Decision"
    properties: [context, rationale, outcome, timestamp]
  - type: "Insight"
    properties: [content, domain, source, confidence]
  - type: "Task"
    properties: [name, status, priority, deadline]

relations:
  - type: "derives_from"
    source: "Insight"
    target: "Decision"
  - type: "related_to"
    source: "Concept"
    target: "Concept"
  - type: "feeds_into"
    source: "Task"
    target: "Decision"
  - type: "learned_from"
    source: "Insight"
    target: "DailyNote"
```

### Twin Fidelity Score 定义

```
Twin Fidelity = (正确回答的问题数 / 总测试问题数) × 100%

测试集设计：
- 事实性问题（30%）：「7/1 晨跑配速是多少？」
- 决策性问题（40%）：「为什么清仓宏英智能？」
- 关联性问题（30%）：「投资风控规则与哪些概念相关？」
```

---

## 四、Phase 3：Agent Mesh 接入（8/1 → 8/15）

### 目标
五维 Agent 均可通过 MCP 协议检索 Twin 知识库。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T3.1 | MCP Server 实现 | `twin_mcp_server.py` 更新 | 8/5 | Phase 2 |
| T3.2 | Agent 目录索引 | `twin_agent_index.yaml` | 8/10 | T3.1 |
| T3.3 | 五维 Agent 接入测试 | 测试报告 | 8/15 | T3.2 |

### MCP Server 接口定义

```yaml
# Twin MCP Server - Tool Definitions
tools:
  - name: "twin_query"
    description: "查询 Knowledge Twin 知识库"
    input:
      query: "string"           # 自然语言查询
      domain: "string"          # 可选：架构|投资|健康|生活|思维
      top_k: "int"              # 返回条数，默认 5
    output:
      results: "array"          # 结构化结果
      fidelity_score: "float"   # 该查询的置信度

  - name: "twin_distill"
    description: "触发新一轮蒸馏"
    input:
      source_path: "string"     # 源文件路径
      force: "bool"             # 是否强制重新蒸馏
    output:
      distilled_count: "int"    # 提取条数
      new_concepts: "array"     # 新发现的概念

  - name: "twin_fidelity_report"
    description: "生成 Twin Fidelity 季报"
    input:
      period: "string"          # Q3-2026
    output:
      report: "object"          # 完整报告
```

---

## 五、Phase 4：OVP 季报（9/1 → 9/30）

### 目标
首份 OVP 季度验证报告产出，Twin Fidelity ≥50%，每日蒸馏连续 60 天。

### 验收清单

| 指标 | 目标值 | 衡量方式 |
|------|:------:|---------|
| Twin Fidelity Score | ≥50% | 测试集问答准确率 |
| 每日蒸馏连续天数 | ≥60 天 | `twin_distill_log.jsonl` 记录 |
| 知识图谱实体数 | ≥500 | RDF 三元组计数 |
| 向量库条目数 | ≥300 | ChromaDB count |
| Agent 可检索率 | 100% | 5/5 Agent 均可查询 |

### OVP 季报模板

```markdown
# Knowledge Twin OVP 季报 — Q3 2026

## 核心指标
| 指标 | 目标 | 实际 | 状态 |
|------|:----:|:----:|:----:|
| Twin Fidelity | ≥50% | XX% | 🟢/🔴 |
| 每日蒸馏 | 连续 60 天 | XX 天 | 🟢/🔴 |
| 知识图谱实体 | ≥500 | XX | 🟢/🔴 |

## 蒸馏质量分析
## Agent 使用分析
## 改进计划
```

---

## 六、风险与缓解

| 风险 | 概率 | 影响 | 缓解措施 |
|------|:----:|:----:|---------|
| 本地 LLM 推理慢 | 高 | 中 | 先用云端 API 跑通，再迁移本地 |
| 蒸馏质量不稳定 | 中 | 高 | 引入人工抽检 + confidence 阈值 |
| 知识图谱噪声大 | 中 | 中 | 先建小规模图谱，逐步扩展 |
| Obsidian 插件兼容 | 低 | 低 | MCP Server 独立运行，不依赖插件 |

---

## 七、文件产出物清单

| 文件 | 路径 | 说明 |
|------|------|------|
| Twin 蒸馏引擎 | `02-BUILD/22-uSkill/智能体任务/twin_distill_engine.py` | 核心蒸馏逻辑 |
| 向量存储 | `02-BUILD/22-uSkill/智能体任务/twin_vector_store.py` | ChromaDB 封装 |
| 知识图谱 Schema | `02-BUILD/22-uSkill/智能体任务/twin_kg_schema.yaml` | RDF 定义 |
| MCP Server | `02-BUILD/22-uSkill/智能体任务/twin_mcp_server.py` | MCP 接口 |
| Fidelity 计算 | `02-BUILD/22-uSkill/智能体任务/twin_fidelity.py` | 质量评估 |
| 蒸馏 Prompt | `02-BUILD/22-uSkill/智能体任务/prompts/distill_cot.md` | CoT 提取模板 |
| 实现路线图 | `02-BUILD/22-uSkill/智能体任务/uSkill-知识孪生体MVP实现路线图-v1.md` | 本文件 |


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---
---

*版本：v1.0 · 2026-07-02 创建 · Q3 里程碑：7/15 MVP → 7/31 双索引 → 8/15 Agent 接入 → 9/30 季报*


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


**相关概念**：[[信息管理系统]]

---


## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

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
