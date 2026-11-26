
description: |
  当用户需要设计评估方法、衡量学习效果、提供有效反馈、改进教学时使用此 Skill。
  触发词包括：'学习评估'、'评估方法'、'学习效果'、'反馈'、'考核'、
  '学习测试'。当用户讨论教育、培训、知识管理时，
  即使未直接说"学习评估"，也应使用此 Skill。
  不适用于简单的考试出题（使用其他 Skill）。遇到系统化评估设计时优先使用。

---

# uSkill-702: 学习评估

## 🎯 目标

> 设计有效的学习评估方法，衡量学习效果，提供改进建议。

**核心价值**：没有评估就没有改进。好的评估能驱动持续学习。

**适用场景**：
- 课程效果评估
- 员工培训评估
- 个人学习效果衡量
- 教学质量改进
- 知识掌握度测试

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `learning_objectives` | `array` | ✅ | — | 学习目标 |
| `assessment_type` | `enum` | ❌ | `formative` | `formative` / `summative` / `diagnostic` |
| `learner_context` | `string` | ❌ | — | 学习者背景 |
| `constraints` | `object` | ❌ | — | 时间、资源限制 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话评估建议",
  "assessment_id": "LA-YYYY-MMDD-NNN",

  "assessment_design": {
    "type": "formative|summative|diagnostic",
    "methods": [
      {
        "method": "string",
        "purpose": "string",
        "alignment": "string",
        "pros": ["string"],
        "cons": ["string"]
      }
    ],
    "rubric": {
      "criteria": ["string"],
      "levels": ["string"],
      "scoring_guide": "string"
    }
  },

  "assessment_tools": [
    {
      "tool": "string",
      "description": "string",
      "best_for": "string",
      "implementation": "string"
    }
  ],

  "feedback_framework": {
    "timeliness": "string",
    "specificity": "string",
    "constructiveness": "string",
    "feedback_templates": ["string"]
  },

  "data_collection": {
    "metrics": ["string"],
    "collection_methods": ["string"],
    "frequency": "string",
    "responsible_parties": ["string"]
  },

  "analysis_and_reporting": {
    "analysis_methods": ["string"],
    "reporting_format": "string",
    "stakeholder_communication": ["string"]
  },

  "improvement_cycle": {
    "data_to_insights": "string",
    "insights_to_actions": "string",
    "actions_to_results": "string"
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

### Step 1: 评估设计

- **输入**：`learning_objectives` + `assessment_type`
- **动作**：
  1. 选择评估方法
  2. 设计评分标准
  3. 对齐学习目标
- **输出**：`assessment_design`
- **评估方法选择**：

| 方法 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| 测试 | 知识掌握 | 客观、可量化 | 无法评估应用 |
| 项目 | 综合能力 | 真实、全面 | 耗时 |
| 观察 | 技能操作 | 直接、真实 | 主观 |
| 反思 | 元认知 | 深度、个性化 | 难以标准化 |

### Step 2: 评估工具

- **输入**：`assessment_design`
- **动作**：
  1. 选择评估工具
  2. 设计实施流程
  3. 准备资源
- **输出**：`assessment_tools`

### Step 3: 反馈框架

- **输入**：`assessment_design`
- **动作**：
  1. 设计反馈原则
  2. 创建反馈模板
  3. 培训反馈者
- **输出**：`feedback_framework`
- **有效反馈原则**：

| 原则 | 描述 |
|------|------|
| 及时性 | 尽快提供反馈 |
| 具体性 | 指出具体行为 |
| 建设性 | 提供改进方向 |
| 平衡性 | 肯定优点和改进点 |

### Step 4: 数据收集

- **输入**：`assessment_tools`
- **动作**：
  1. 定义关键指标
  2. 设计收集方法
  3. 安排收集频率
- **输出**：`data_collection`

### Step 5: 分析和报告

- **输入**：`data_collection`
- **动作**：
  1. 选择分析方法
  2. 设计报告格式
  3. 规划沟通方式
- **输出**：`analysis_and_reporting`

### Step 6: 改进循环

- **输入**：所有前序输出
- **动作**：
  1. 设计数据到洞察的转化
  2. 设计洞察到行动的转化
  3. 设计行动到结果的验证
- **输出**：`improvement_cycle`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**仅使用单一评估方法
2. **不得**忽视评估公平性
3. **必须**与学习目标对齐

### 软性约束（建议遵守）
1. 建议结合定量和定性评估
2. 建议提供多次评估机会
3. 建议让学习者参与评估设计

### 人工兜底点
- 当涉及重要决策时，**必须**建议多角度评估
- 当评估结果异常时，**必须**建议深入分析

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `LA_WARNING_MISALIGNMENT` | 评估与目标不对齐 | 建议调整 | 🟡 |
| `LA_WARNING_BIAS` | 评估可能存在偏见 | 建议校准 | 🟡 |
| `LA_ERROR_NO_DATA` | 无法收集数据 | 建议更换方法 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 评估方法已选择
- [ ] 评分标准已设计
- [ ] 反馈框架已制定
- [ ] 改进循环已设计

### OVP 验证信号
- 评估有效性评分 ≥ 85/100
- 学习效果提升 ≥ 20%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "课程效果评估",
    "prompt": "评估一个在线Python课程的学习效果",
    "context": "learning_objectives=[掌握Python基础], assessment_type=summative",
    "assertions": [
      "assessment_design.methods 至少 2 种方法",
      "assessment_design.rubric 已设计",
      "feedback_framework 已制定"
    ],
    "expected_behavior": "设计全面的课程效果评估",
    "critic_attack": "是否考虑了不同学习风格？"
  },
  {
    "id": "test-002",
    "name": "培训效果评估",
    "prompt": "评估销售培训的效果",
    "context": "learning_objectives=[提升销售技巧], assessment_type=formative",
    "assertions": [
      "assessment_tools 包含 观察和角色扮演",
      "data_collection.metrics 包含 销售业绩",
      "improvement_cycle 已设计"
    ],
    "expected_behavior": "设计培训效果的持续评估",
    "critic_attack": "是否将评估与业务结果挂钩？"
  },
  {
    "id": "test-003",
    "name": "个人学习评估",
    "prompt": "如何评估我的自学效果",
    "context": "assessment_type=formative, learner_context=自学者",
    "assertions": [
      "assessment_design.methods 包含 自我测试",
      "feedback_framework 包含 自我反馈模板",
      "data_collection 包含 学习日志"
    ],
    "expected_behavior": "为自学者设计评估方法",
    "critic_attack": "是否考虑了自学者的特殊需求？"
  }
]
```

---

## 🔗 关联文档

- [[教学设计]] — 课程设计
- [[学习金字塔输出驱动]] — 学习方法
- [[深度学习方法]] — 深度学习
- [[知识蒸馏]] — 知识简化
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：评估设计 + 反馈框架 + 改进循环 + Self-Play |

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


**相关概念**：[[艾宾浩斯遗忘曲线]]

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
