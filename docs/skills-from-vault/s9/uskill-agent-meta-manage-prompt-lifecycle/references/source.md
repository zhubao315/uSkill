# Prompt Lifecycle Management

## 🎯 目标
> 工业级提示词全生命周期管理：从构思设计、原型调试、系统化测试到归档版本化，将单个高质量Prompt开发周期缩短70%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | enum | ✅ | `design` / `prototype` / `test` / `optimize` / `archive` — 生命周期阶段 |
| `prompt_goal` | string | ✅ | 提示词要解决的核心问题描述 |
| `target_model` | string | ❌ | 目标模型（如 `claude-3.5` / `gpt-4o` / `llama3`），默认 `auto` |
| `existing_prompt` | string | ❌ | 已有的提示词文本（用于优化/测试阶段） |
| `test_cases` | array | ❌ | `[{input: "string", expected: "string", scenario: "typical|edge|stress|adversarial"}]` — 测试用例 |
| `rubric` | object | ❌ | `{criteria: [{name: "string", weight: "number", description: "string"}]}` — 评分标准 |
| `cross_model_targets` | array | ❌ | `["string"]` — 跨模型测试目标列表 |

## 📤 输出

### design 阶段输出
```json
{
  "action": "design",
  "prompt_template": "string — 结构化提示词模板（含 {{variable}} 变量）",
  "persona": "string — AI角色设定",
  "framework_used": "CRISPE | CO-STAR | custom",
  "design_rationale": "string — 设计思路说明",
  "variables": [{"name": "string", "type": "string", "required": "boolean", "description": "string"}]
}
```

### prototype 阶段输出
```json
{
  "action": "prototype",
  "prompt_v1": "string — v1.0提示词全文",
  "test_results": [{"run": "int", "input": "string", "output": "string", "pass": "boolean", "issue": "string|null"}],
  "pass_rate_pct": "number",
  "iteration_log": [{"version": "string", "change": "string", "reason": "string"}]
}
```

### test 阶段输出
```json
{
  "action": "test",
  "test_plan": {"total_cases": "int", "typical": "int", "edge": "int", "stress": "int", "adversarial": "int"},
  "ab_test_results": [
    {"variant": "string", "avg_score": "number", "pass_rate_pct": "number", "strengths": ["string"], "weaknesses": ["string"]}
  ],
  "cross_model_results": [
    {"model": "string", "avg_score": "number", "pass_rate_pct": "number", "latency_ms": "number", "token_cost": "number"}
  ],
  "evaluation": {
    "ai_evaluation": {"avg_score": "number", "criteria_scores": [{"criterion": "string", "score": "number"}]},
    "human_evaluation": {"avg_score": "number", "notes": "string"}
  },
  "best_variant": "string — 表现最佳的变体标识"
}
```

### optimize 阶段输出
```json
{
  "action": "optimize",
  "final_prompt": "string — 精炼后的最终版提示词",
  "version": "string — 正式版本号",
  "changelog": ["string — 本次优化变更条目"],
  "performance_delta": {"pass_rate_before": "number", "pass_rate_after": "number", "score_before": "number", "score_after": "number"},
  "inline_comments": "string — 含代码级注释的提示词"
}
```

### archive 阶段输出
```json
{
  "action": "archive",
  "asset_id": "string — 归档资产ID",
  "file_path": "string — 归档路径",
  "tags": ["string"],
  "version_history": [{"version": "string", "date": "string", "change": "string"}],
  "metadata": {"author": "string", "created": "string", "last_tested": "string", "recommended_model": "string"}
}
```

## 📋 执行步骤

### 阶段一：构思与设计 (action=design)
1. **定义目标** — 明确提示词解决的核心问题、目标用户、预期输出格式和业务价值
2. **角色设定** — 为AI设定清晰专业的Persona（如"资深投资分析师"、"苛刻技术总监"）
3. **结构设计** — 采用CRISPE框架（Capacity/Role/Insight/Statement/Personality/Experiment），明确上下文、任务指令、约束条件、输出格式
4. **AI辅助构思** — 让AI扮演"世界顶级提示词工程师兼认知心理学家"，优化结构设计，减少AI认知负荷

### 阶段二：原型与调试 (action=prototype)
5. **撰写v1.0** — 输出完整提示词并录入平台
6. **快速测试** — 在主要模型上执行3-5次，检查基本功能
7. **失败分析** — 判断是指令不清、上下文缺失还是模型理解偏差
8. **迭代修复** — 快速修复明显问题直到v1.x可用（通过率≥70%）

### 阶段三：系统化测试 (action=test)
9. **设计测试方案** — 生成10个测试用例：3典型+3边缘+2压力+2对抗性场景
10. **A/B测试** — 对不同措辞/约束顺序的变体进行量化对比
11. **跨模型测试** — 在 `cross_model_targets` 列表中的模型上运行，评估通用性和鲁棒性
12. **AI辅助评估** — 用独立模型按 `rubric` 对输出打分（1-10分）
13. **人工评估** — 对关键结果进行准确性/创造性/实用性人工打分

### 阶段四：优化与定版 (action=optimize)
14. **选定基准** — 选择测试中表现最佳的变体作为基准版本
15. **精炼吸收** — 吸收各变体优点，修复残留缺陷
16. **代码级注释** — 为关键指令添加注释解释设计目的
17. **正式发布** — 命名正式版（如v2.0），更新平台状态

### 阶段五：归档与版本管理 (action=archive)
18. **资产归档** — 将提示词文档和测试报告归档到平台/知识库
19. **版本标记** — 建立语义化版本号，重大修改创建新版本+Changelog
20. **标签索引** — 打标签（如#工作 #报告生成 #代码辅助）方便检索复用

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `prompt_goal` 过于模糊 | 返回 `ERROR_VAGUE_GOAL` + 澄清问题清单（目标用户？输出格式？核心约束？） |
| `action=test` 但 `existing_prompt` 为空 | 返回 `ERROR_NO_PROMPT_TO_TEST` + 建议先执行 design 阶段 |
| A/B测试所有变体通过率 < 50% | 返回 `WARNING_LOW_PERFORMANCE` + 建议回退到 design 阶段重新构思 |
| 跨模型测试结果方差 > 30% | 标记 `FLAG_MODEL_SENSITIVITY` + 建议针对差异大的模型定制变体 |
| `rubric` 未提供但 action=test | 使用默认Rubric（格式遵循度/要点覆盖率/逻辑清晰度/语言专业度 各25%） |
| 归档版本号冲突 | 自动递增PATCH版本 + 标记冲突供人工确认 |

## ✅ 自检清单

- [ ] design阶段：输出包含角色设定、结构框架、变量定义
- [ ] prototype阶段：v1.0通过率 ≥ 70%
- [ ] test阶段：测试用例 ≥ 10个，覆盖4类场景
- [ ] test阶段：A/B测试 ≥ 2个变体对比
- [ ] test阶段：跨模型测试覆盖 ≥ 2个模型
- [ ] optimize阶段：最终版通过率较v1.0提升 ≥ 15%
- [ ] archive阶段：版本号符合语义化规范，Changelog完整
- [ ] 所有阶段：Prompt内变量使用 `{{variable}}` 格式


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

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-03 转化 |

---
**相关笔记**：[[学习计划设计]] [[痛苦反思成长循环]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [学习任务] for [知识背景], with [学习目标], leaning toward [学习方法/输出形式]."

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
| ""以后再整理笔记"" | "以后不会来，现在就做" |
| ""读完就行了"" | "没有输出的阅读是自我感动" |
| ""这个太简单不用记"" | "简单的知识最容易忘" |
| ""收藏=学会"" | "收藏夹是知识的坟墓" |
| ""看完再总结"" | "看完就忘，边读边记才是正道" |

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


**相关概念**：[[Prompt Engineering]]

---


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
