
description: |
  当用户需要将复杂概念简化、进行知识传达、制作教学材料、解释专业概念时使用此 Skill。
  触发词包括：'知识蒸馏'、'简化'、'通俗易懂'、'教学'、'解释'、
  '复杂概念简化'。当用户讨论教学、知识分享、沟通时，
  即使未直接说"知识蒸馏"，也应使用此 Skill。
  不适用于深度技术文档（使用其他 Skill）。遇到知识简化需求时优先使用。

---

# uSkill-703: 知识蒸馏

## 🎯 目标

> 将复杂知识简化为易于理解的形式，同时保持准确性。

**核心价值**：能够简单解释复杂概念，才是真正理解的标志。

**适用场景**：
- 教学材料制作
- 技术文档简化
- 知识分享
- 跨部门沟通
- 客户教育

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `complex_knowledge` | `string` | ✅ | — | 复杂知识描述 |
| `target_audience` | `string` | ✅ | — | 目标受众 |
| `simplification_level` | `enum` | ❌ | `moderate` | `light` / `moderate` / `heavy` |
| `format` | `enum` | ❌ | `text` | `text` / `visual` / `interactive` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话简化建议",
  "distillation_id": "KD-YYYY-MMDD-NNN",

  "knowledge_analysis": {
    "core_concept": "string",
    "key_components": ["string"],
    "common_misconceptions": ["string"],
    "prerequisites": ["string"]
  },

  "simplification_strategy": {
    "analogy": {
      "analogy_description": "string",
      "mapping": {
        "source_domain": "string",
        "target_domain": "string",
        "correspondences": ["string"]
      },
      "limitations": ["string"]
    },
    "metaphor": "string",
    "story": "string",
    "visual_metaphor": "string"
  },

  "simplified_explanations": {
    "one_liner": "string",
    "elevator_pitch": "string",
    "detailed_explanation": "string",
    "visual_representation": "string"
  },

  "progressive_disclosure": {
    "level_1_basic": "string",
    "level_2_intermediate": "string",
    "level_3_advanced": "string",
    "level_4_expert": "string"
  },

  "common_questions": [
    {
      "question": "string",
      "answer": "string",
      "misconception_addressed": "string"
    }
  ],

  "validation": {
    "accuracy_check": "string",
    "clarity_check": "string",
    "engagement_check": "string"
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

### Step 1: 知识分析

- **输入**：`complex_knowledge`
- **动作**：
  1. 识别核心概念
  2. 分解关键组件
  3. 识别常见误解
- **输出**：`knowledge_analysis`

### Step 2: 简化策略

- **输入**：`knowledge_analysis` + `target_audience`
- **动作**：
  1. 选择类比
  2. 设计隐喻
  3. 创作故事
- **输出**：`simplification_strategy`
- **简化技术**：

| 技术 | 描述 | 适用场景 |
|------|------|----------|
| 类比 | 用熟悉事物解释新概念 | 概念引入 |
| 隐喻 | 用形象语言描述 | 抽象概念 |
| 故事 | 用叙事传达知识 | 情感连接 |
| 可视化 | 用图表展示 | 关系展示 |

### Step 3: 分层解释

- **输入**：`simplification_strategy`
- **动作**：
  1. 设计基础解释
  2. 设计进阶解释
  3. 设计专家解释
- **输出**：`simplified_explanations` + `progressive_disclosure`

### Step 4: 常见问题

- **输入**：`knowledge_analysis.common_misconceptions`
- **动作**：
  1. 预测常见问题
  2. 准备清晰答案
  3. 纠正常见误解
- **输出**：`common_questions`

### Step 5: 验证

- **输入**：所有前序输出
- **动作**：
  1. 检查准确性
  2. 检查清晰度
  3. 检查吸引力
- **输出**：`validation`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**牺牲准确性换取简单
2. **不得**过度简化导致误解
3. **必须**标注简化局限性

### 软性约束（建议遵守）
1. 建议使用多种简化技术
2. 建议测试简化效果
3. 建议提供深入学习路径

### 人工兜底点
- 当涉及专业领域时，**必须**建议专家审核
- 当简化可能导致误解时，**必须**标注警告

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `KD_WARNING_OVERSIMPLIFY` | 过度简化 | 建议增加细节 | 🟡 |
| `KD_WARNING_INACCURATE` | 简化不准确 | 建议修正 | 🟡 |
| `KD_ERROR_TOO_COMPLEX` | 无法简化 | 建议分步简化 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 核心概念已识别
- [ ] 类比已设计
- [ ] 分层解释已生成
- [ ] 常见问题已准备

### OVP 验证信号
- 简化准确率 ≥ 90%
- 受众理解率 ≥ 85%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "技术概念简化",
    "prompt": "用简单语言解释机器学习",
    "context": "target_audience=非技术人员",
    "assertions": [
      "knowledge_analysis.core_concept 已识别",
      "simplification_strategy.analogy 已设计",
      "simplified_explanations.one_liner 已生成"
    ],
    "expected_behavior": "将机器学习简化为通俗概念",
    "critic_attack": "简化是否保持了准确性？"
  },
  {
    "id": "test-002",
    "name": "商业概念简化",
    "prompt": "如何向客户解释我们的AI产品",
    "context": "target_audience=客户, simplification_level=moderate",
    "assertions": [
      "simplification_strategy.story 已设计",
      "progressive_disclosure.level_1_basic 已生成",
      "common_questions 至少 3 个常见问题"
    ],
    "expected_behavior": "为客户提供易懂的产品解释",
    "critic_attack": "是否突出了客户价值？"
  },
  {
    "id": "test-003",
    "name": "儿童教育简化",
    "prompt": "如何向10岁孩子解释太阳系",
    "context": "target_audience=儿童, simplification_level=heavy",
    "assertions": [
      "simplification_strategy.analogy 使用 太阳系家庭类比",
      "simplified_explanations.visual_representation 已设计",
      "progressive_disclosure.level_1_basic 非常简单"
    ],
    "expected_behavior": "为儿童设计太阳系解释",
    "critic_attack": "是否足够吸引儿童？"
  }
]
```

---

## 🔗 关联文档

- [[uSkill-productivity-费曼技巧学习法]] — 费曼技巧
- [[深度学习方法]] — 深度学习
- [[教学设计]] — 课程设计
- [[学习评估]] — 效果评估
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：知识分析 + 简化策略 + 分层解释 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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


**相关概念**：[[DIKW 知识金字塔]]

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
