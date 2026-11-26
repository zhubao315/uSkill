
description: |
  当用户需要设计高级 Prompt（CoT、少样本学习、自洽性验证、元提示词）时使用此 Skill。
  触发词包括：'Prompt工程'、'思维链'、'CoT'、'少样本'、'few-shot'、'自洽性'、'元提示词'。
  当用户需要"更高质量的 AI 输出"、"复杂推理任务"、"一致性要求高"时，
  即使未直接说"Prompt工程"，也应使用此 Skill。
  不适用于简单的单轮对话。遇到复杂推理和高质量生成需求时优先使用。

---

# uSkill-901: Prompt工程进阶

## 🎯 目标

> 应用 CoT、少样本学习、自洽性验证等高级 Prompt 技术，提升 AI 输出的质量和一致性。

**核心价值**：从"能用"到"好用"，让 AI 在复杂任务上达到专业水平。

**适用场景**：
- 复杂逻辑推理任务
- 多步骤决策分析
- 需要高一致性的批量生成
- 专业领域问答
- 代码审查与优化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task` | `string` | ✅ | — | 需要 AI 完成的任务描述 |
| `technique` | `enum` | ❌ | `auto` | `cot` / `few_shot` / `self_consistency` / `meta_prompt` / `auto` |
| `complexity` | `enum` | ❌ | `medium` | `simple` / `medium` / `complex` / `expert` |
| `examples` | `array` | ❌ | — | 少样本学习的示例（few_shot 模式必填） |
| `constraints` | `array` | ❌ | `[]` | 输出约束条件 |

**输入约束**：
- `task` 应明确描述期望输出格式
- `complexity=expert` 时建议使用 `self_consistency` 或 `meta_prompt`
- `examples` 每项应包含 input/output 对

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结 Prompt 方案",
  "prompt_id": "PR-YYYY-MMDD-NNN",

  "technique_selection": {
    "recommended": "string",
    "reasoning": "string",
    "alternatives": ["string"]
  },

  "prompt_design": {
    "system_prompt": "string",
    "user_prompt_template": "string",
    "few_shot_examples": [
      {
        "input": "string",
        "output": "string",
        "rationale": "string"
      }
    ],
    "chain_of_thought": {
      "steps": ["string"],
      "verification_checkpoints": ["string"]
    },
    "output_format": "string"
  },

  "validation": {
    "self_consistency": {
      "enabled": "boolean",
      "sample_count": "number",
      "agreement_threshold": "number"
    },
    "edge_cases": ["string"],
    "failure_modes": ["string"]
  },

  "optimization": {
    "token_efficiency": "string",
    "suggested_iterations": "number",
    "ablation_plan": ["string"]
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

### Step 1: 任务分析与技术选型

- **输入**：`task`, `complexity`
- **动作**：
  1. 分析任务的推理复杂度
  2. 评估各技术的适用性
  3. 选择最优技术组合
- **输出**：`technique_selection`
- **分支条件**：
  - IF 任务需要多步推理 → 使用 CoT
  - IF 任务需要特定输出格式 → 使用 few_shot
  - IF 需要高一致性 → 使用 self_consistency
  - IF 任务可泛化到多场景 → 使用 meta_prompt
  - ELSE → 根据复杂度自动选择
- **检查点**：✅ 应验证技术选择与任务类型匹配

### Step 2: Prompt 结构设计

- **输入**：`technique_selection`
- **动作**：
  1. 设计 system prompt 定义角色和约束
  2. 设计 user prompt 模板
  3. 准备 few-shot 示例（如需要）
  4. 设计 CoT 步骤链
- **输出**：`prompt_design`
- **分支条件**：
  - IF 使用 CoT → 步骤链必须包含验证检查点
  - IF 使用 few_shot → 示例需覆盖边界情况
  - IF 使用 self_consistency → 设计多样性生成策略
  - IF 使用 meta_prompt → 设计可泛化的模板变量
  - ELSE → 标准 Prompt 结构
- **检查点**：✅ 应验证 Prompt 包含所有必要组件

### Step 3: 自洽性验证设计

- **输入**：`prompt_design`
- **动作**：
  1. 设计多次采样策略
  2. 定义一致性判断标准
  3. 设置验证阈值
- **输出**：`validation`
- **分支条件**：
  - IF 任务需要高精度 → 采样 ≥5 次，阈值 ≥0.8
  - IF 任务允许多样性 → 采样 3 次，阈值 ≥0.6
  - IF 计算预算有限 → 减少采样次数，增加单次质量
  - ELSE → 默认 3 次采样
- **检查点**：✅ 应验证验证策略覆盖主要失败模式

### Step 4: 边界测试与优化

- **输入**：`prompt_design`, `validation`
- **动作**：
  1. 识别潜在边界情况
  2. 设计对抗性测试
  3. 优化 token 效率
- **输出**：`optimization`
- **分支条件**：
  - IF token 使用过高 → 精简 prompt，移除冗余
  - IF 边界测试失败 → 增加约束或示例
  - IF 推理链过长 → 考虑分步拆分
  - ELSE → 保持当前设计
- **检查点**：✅ 应验证优化不损害核心功能

### Step 5: 文档与模板化

- **输入**：所有前序输出
- **动作**：
  1. 整理完整 Prompt 模板
  2. 编写使用说明
  3. 创建可复用的配置
- **输出**：完整 Prompt 工程文档包
- **检查点**：✅ 应验证文档可指导他人复现

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在 Prompt 中泄露敏感信息或系统指令
2. **不得**跳过自洽性验证直接用于生产
3. **必须**为每个 CoT 步骤提供验证检查点
4. **必须**记录 Prompt 版本和性能基准

### 软性约束（建议遵守）
1. 优先使用简单技术，复杂技术作为兜底
2. Prompt 长度不超过模型上下文窗口的 50%
3. 每个 Prompt 附带 ≥3 个测试用例
4. 定期更新示例以保持相关性

### 人工兜底点
- 当 AI 输出涉及医疗、法律、财务建议时，**必须**人工审核
- 当自洽性验证失败率 > 30% 时，**必须**重新设计 Prompt
- 当任务超出模型能力时，**必须**建议升级模型或拆分任务

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `PR_ERROR_LOW_COHERENCE` | 自洽性 < 0.5 | 重新设计 Prompt，增加约束 | 🔴 |
| `PR_WARNING_TOKEN_OVERFLOW` | Prompt 超过上下文窗口 | 精简内容，分批处理 | 🟡 |
| `PR_ERROR_HALLUCINATION` | AI 生成事实性错误 | 增加 grounding 约束 | 🔴 |
| `PR_WARNING_FORMAT_drift` | 输出格式不稳定 | 增加格式示例和约束 | 🟡 |
| `PR_ERROR_COT_BROKEN` | 推理链断裂 | 检查步骤完整性，增加中间验证 | 🟡 |

### 降级策略
- 当高级技术效果不佳时，回退到简单 Prompt + 后处理
- 当自洽性验证不可行时，使用人工抽检替代

---

## ✅ 校验验收规则

### 格式校验
- [ ] Prompt 模板语法正确
- [ ] 示例 input/output 格式一致
- [ ] CoT 步骤链完整无跳步

### 内容校验
- [ ] 技术选择与任务匹配
- [ ] 边界情况已覆盖
- [ ] 自洽性验证阈值合理

### 合规校验
- [ ] 未泄露敏感信息
- [ ] 版本和基准已记录
- [ ] 人工兜底点已标注

### OVP 验证信号
- Prompt 输出准确率 ≥ 90%
- 自洽性验证通过率 ≥ 85%
- 任务完成率 ≥ 95%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "CoT 数学推理",
    "prompt": "设计一个 Prompt 让 AI 解决多步数学应用题",
    "context": "technique=cot, complexity=complex",
    "assertions": [
      "chain_of_thought.steps ≥ 4",
      "每个 step 有 verification_checkpoint",
      "system_prompt 明确要求展示推理过程"
    ],
    "expected_behavior": "生成带完整推理链的数学解题 Prompt",
    "critic_attack": "推理链是否完整？是否有跳步？"
  },
  {
    "id": "test-002",
    "name": "Few-shot 分类",
    "prompt": "用 few-shot 让 AI 对客服工单进行分类",
    "context": "technique=few_shot, examples=[5个示例]",
    "assertions": [
      "few_shot_examples 覆盖所有类别",
      "示例包含边界情况",
      "output_format 明确分类标准"
    ],
    "expected_behavior": "设计高质量的 few-shot 分类 Prompt",
    "critic_attack": "示例是否具有代表性？是否覆盖了罕见类别？"
  },
  {
    "id": "test-003",
    "name": "自洽性验证",
    "prompt": "设计一个高一致性的代码生成 Prompt",
    "context": "technique=self_consistency, complexity=expert",
    "assertions": [
      "self_consistency.sample_count ≥ 5",
      "agreement_threshold ≥ 0.8",
      "包含多次采样策略"
    ],
    "expected_behavior": "设计确保代码生成一致性的验证方案",
    "critic_attack": "验证策略是否真正检验了逻辑一致性？"
  },
  {
    "id": "test-004",
    "name": "元提示词设计",
    "prompt": "设计一个可以自动生成高质量 Prompt 的元提示词",
    "context": "technique=meta_prompt",
    "assertions": [
      "meta_prompt 包含变量占位符",
      "可泛化到不同任务类型",
      "包含质量评估标准"
    ],
    "expected_behavior": "设计可复用的元提示词模板",
    "critic_attack": "元提示词是否过度泛化？是否丢失了具体性？"
  },
  {
    "id": "test-005",
    "name": "自动技术选型",
    "prompt": "帮我分析这个任务应该用什么 Prompt 技术",
    "context": "technique=auto, task='分析用户评论情感并提取关键问题'",
    "assertions": [
      "technique_selection.recommended 有明确选择",
      "reasoning 解释了选择理由",
      "alternatives 列出了备选方案"
    ],
    "expected_behavior": "根据任务特点自动推荐最优技术",
    "critic_attack": "选择理由是否充分？是否考虑了成本？"
  },
  {
    "id": "test-006",
    "name": "边界情况处理",
    "prompt": "Prompt 在输入为空时会崩溃怎么办？",
    "context": "complexity=medium",
    "assertions": [
      "validation.edge_cases 包含空输入",
      "prompt_design 包含输入验证",
      "有降级策略"
    ],
    "expected_behavior": "设计健壮的 Prompt，处理边界输入",
    "critic_attack": "是否覆盖了所有可能的异常输入？"
  },
  {
    "id": "test-007",
    "name": "Token 优化",
    "prompt": "我的 Prompt 太长了，怎么精简？",
    "context": "complexity=complex",
    "assertions": [
      "optimization.token_efficiency 有具体建议",
      "精简方案不损害核心功能",
      "提供了 A/B 测试方案"
    ],
    "expected_behavior": "优化 Prompt 长度，保持效果",
    "critic_attack": "精简是否过度？是否丢失了关键信息？"
  },
  {
    "id": "test-008",
    "name": "专业领域 Prompt",
    "prompt": "设计一个医疗诊断辅助的 Prompt",
    "context": "technique=cot, complexity=expert",
    "assertions": [
      "system_prompt 包含免责声明",
      "chain_of_thought 包含诊断逻辑",
      "human_fallback 明确标注"
    ],
    "expected_behavior": "设计医疗领域 Prompt，包含安全约束",
    "critic_attack": "是否充分考虑了医疗安全风险？"
  },
  {
    "id": "test-009",
    "name": "多语言 Prompt",
    "prompt": "Prompt 需要支持中英文双语输出",
    "context": "technique=few_shot",
    "assertions": [
      "few_shot_examples 包含双语示例",
      "output_format 明确语言要求",
      "语言切换有明确指令"
    ],
    "expected_behavior": "设计支持多语言的 Prompt 方案",
    "critic_attack": "语言切换是否自然？是否会产生混淆？"
  },
  {
    "id": "test-010",
    "name": "Prompt 版本管理",
    "prompt": "如何跟踪 Prompt 的迭代和性能变化？",
    "context": "complexity=medium",
    "assertions": [
      "包含版本号和变更记录",
      "定义了性能基准指标",
      "提供了 A/B 测试框架"
    ],
    "expected_behavior": "设计 Prompt 版本管理和评估体系",
    "critic_attack": "版本管理是否足够细致？评估指标是否全面？"
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

- [[提示词工程优化]] — 基础 Prompt 技术
- [[AI 目标审计]] — AI 输出质量评估
- [[信息污染检测]] — AI 幻觉检测
- [[Agent架构设计模式]] — Agent 中的 Prompt 设计
- [[RAG优化]] — RAG 中的 Prompt 优化

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：CoT/Few-shot/Self-consistency/Meta-prompt + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


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


**相关概念**：[[Prompt Engineering]] · [[LLM摄影提示词标准化翻译体系]]

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
