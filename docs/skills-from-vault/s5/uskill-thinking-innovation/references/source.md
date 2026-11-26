
description: |
  当用户需要产生创新想法、突破思维定式、进行创造性思考、解决复杂问题时使用此 Skill。
  触发词包括：'创新'、'创意'、'brainstorming'、'头脑风暴'、'SCAMPER'、
  '六顶思考帽'、'水平思考'。当用户讨论创新、设计思维、问题解决时，
  即使未直接说"创新思维"，也应使用此 Skill。
  不适用于执行已确定的方案（使用其他 Skill）。遇到创新需求时优先使用。

---

# uSkill-109: 创新思维

## 🎯 目标

> 应用系统化创新方法，产生高质量的创新想法。

**核心价值**：创新不是天赋，而是可以学习的方法。

**适用场景**：
- 产品创新
- 流程改进
- 问题解决
- 商业模式创新
- 战略创新

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `challenge` | `string` | ✅ | — | 需要创新的挑战 |
| `constraint` | `array` | ❌ | `[]` | 限制条件 |
| `method` | `enum` | ❌ | `auto` | `scamper` / `six_hats` / `lateral` / `auto` |
| `diversity_level` | `enum` | ❌ | `medium` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话创新建议",
  "innovation_id": "IN-YYYY-MMDD-NNN",

  "challenge_analysis": {
    "core_problem": "string",
    "assumptions_to_challenge": ["string"],
    "perspectives": ["string"],
    "success_criteria": "string"
  },

  "innovation_method": {
    "primary_method": "scamper|six_hats|lateral|design_thinking",
    "application": "string",
    "techniques_used": ["string"]
  },

  "ideas_generated": [
    {
      "idea": "string",
      "description": "string",
      "novelty": "low|medium|high",
      "feasibility": "low|medium|high",
      "potential_impact": "low|medium|high",
      "implementation_sketch": "string"
    }
  ],

  "idea_evaluation": {
    "criteria": ["string"],
    "scoring_matrix": [
      {
        "idea": "string",
        "scores": {
          "novelty": "number",
          "feasibility": "number",
          "impact": "number"
        },
        "total_score": "number"
      }
    ],
    "top_ideas": ["string"]
  },

  "implementation_roadmap": {
    "phase_1_explore": {
      "duration": "string",
      "activities": ["string"],
      "deliverables": ["string"]
    },
    "phase_2_prototype": {
      "duration": "string",
      "activities": ["string"],
      "deliverables": ["string"]
    },
    "phase_3_test": {
      "duration": "string",
      "activities": ["string"],
      "deliverables": ["string"]
    }
  },

  "creativity_exercises": [
    {
      "exercise": "string",
      "purpose": "string",
      "time_required": "string"
    }
  ],

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 挑战分析

- **输入**：`challenge` + `constraint`
- **动作**：
  1. 明确核心问题
  2. 识别需要挑战的假设
  3. 确定成功标准
- **输出**：`challenge_analysis`

### Step 2: 创新方法选择

- **输入**：`challenge_analysis` + `method`
- **动作**：
  1. 选择最适合的方法
  2. 应用方法技巧
  3. 生成多样化想法
- **输出**：`innovation_method`
- **创新方法库**：

| 方法 | 描述 | 适用场景 |
|------|------|----------|
| SCAMPER | 替代、合并、调整、修改、另用、消除、重排 | 产品改进 |
| 六顶思考帽 | 白(事实)、红(情感)、黑(风险)、黄(利益)、绿(创意)、蓝(控制) | 全面思考 |
| 水平思考 | 打破常规思维路径 | 突破性创新 |
| 设计思维 | 同情、定义、构思、原型、测试 | 用户中心设计 |

### Step 3: 想法生成

- **输入**：`innovation_method`
- **动作**：
  1. 应用创新技巧
  2. 产生多样化想法
  3. 鼓励疯狂想法
- **输出**：`ideas_generated`
- **SCAMPER 技巧**：

| 字母 | 技巧 | 问题示例 |
|:----:|------|----------|
| S | 替代 | 什么可以被替代？ |
| C | 合并 | 什么可以合并？ |
| A | 调整 | 什么可以调整？ |
| M | 修改 | 什么可以放大/缩小？ |
| P | 另用 | 有什么其他用途？ |
| E | 消除 | 什么可以删除？ |
| R | 重排 | 什么可以重新排列？ |

### Step 4: 想法评估

- **输入**：`ideas_generated`
- **动作**：
  1. 定义评估标准
  2. 评分每个想法
  3. 选择最佳想法
- **输出**：`idea_evaluation`

### Step 5: 实施路线图

- **输入**：`idea_evaluation.top_ideas`
- **动作**：
  1. 设计探索阶段
  2. 设计原型阶段
  3. 设计测试阶段
- **输出**：`implementation_roadmap`

### Step 6: 创造力练习

- **输入**：`challenge_analysis`
- **动作**：
  1. 设计日常练习
  2. 安排团队练习
  3. 提供灵感来源
- **输出**：`creativity_exercises`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在想法生成阶段评判
2. **不得**忽视可行性
3. **必须**考虑约束条件

### 软性约束（建议遵守）
1. 建议先追求数量再追求质量
2. 建议鼓励"疯狂"想法
3. 建议结合多种方法

### 人工兜底点
- 当创新涉及重大风险时，**必须**建议小规模测试
- 当团队创新受阻时，**必须**建议外部刺激

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IN_WARNING_BLOCKED` | 思维受阻 | 换个方法 | 🟡 |
| `IN_WARNING_SAME_IDEAS` | 想法雷同 | 增加多样性 | 🟡 |
| `IN_ERROR_NO_IDEAS` | 无法产生想法 | 换个角度 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 挑战已分析
- [ ] 创新方法已应用
- [ ] 想法已生成
- [ ] 评估已完成

### OVP 验证信号
- 想法数量 ≥ 10
- 可行性评分 ≥ 60/100

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "产品创新",
    "prompt": "如何改进我们的移动应用",
    "context": "challenge=应用改进, method=scamper",
    "assertions": [
      "innovation_method.techniques_used 包含 SCAMPER技巧",
      "ideas_generated 至少 5 个想法",
      "idea_evaluation 已完成"
    ],
    "expected_behavior": "使用SCAMPER产生创新想法",
    "critic_attack": "想法是否真正创新？"
  },
  {
    "id": "test-002",
    "name": "流程改进",
    "prompt": "如何让我们的会议更高效",
    "context": "challenge=会议效率, method=six_hats",
    "assertions": [
      "innovation_method.primary_method = 六顶思考帽",
      "ideas_generated 包含 多角度想法",
      "implementation_roadmap 已设计"
    ],
    "expected_behavior": "使用六顶思考帽改进会议",
    "critic_attack": "是否考虑了所有利益相关者？"
  },
  {
    "id": "test-003",
    "name": "战略创新",
    "prompt": "如何进入一个新市场",
    "context": "challenge=市场进入, diversity_level=high",
    "assertions": [
      "challenge_analysis.perspectives 至少 3 个视角",
      "ideas_generated novelty 多样",
      "creativity_exercises 已设计"
    ],
    "expected_behavior": "产生多样化的市场进入策略",
    "critic_attack": "是否考虑了市场进入壁垒？"
  }
]
```

---

## 🔗 关联文档

- [[禅宗空性与第一性原理：如何剥离日常偏见，还原事物的最底层逻辑]] — 基本原理推理
- [[突破创新协议]] — 创新方法论
- [[生态系统思维]] — 系统分析
- [[逆向工程思维]] — 逆向分析
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：SCAMPER + 六顶思考帽 + 想法评估 + Self-Play |

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


**相关概念**：[[创造力的神经基础]]

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
