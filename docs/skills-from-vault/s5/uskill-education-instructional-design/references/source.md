
description: |
  当用户需要设计课程、开发教学内容、制定学习目标、设计评估方法时使用此 Skill。
  触发词包括：'教学设计'、'课程设计'、'学习目标'、'教学大纲'、'课程开发'、
  '教学方法'。当用户讨论培训、教育、知识传授时，
  即使未直接说"教学设计"，也应使用此 Skill。
  不适用于简单的知识分享（使用其他 Skill）。遇到系统化教学设计时优先使用。

---

# uSkill-701: 教学设计

## 🎯 目标

> 基于 ADDIE 模型和 Bloom 分类法，设计有效的教学活动和评估方法。

**核心价值**：好的教学设计能大幅提升学习效果，让知识传递更高效。

**适用场景**：
- 在线课程设计
- 企业培训设计
- 工作坊设计
- 教材编写
- 知识库设计

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `topic` | `string` | ✅ | — | 教学主题 |
| `target_audience` | `string` | ✅ | — | 目标学员 |
| `learning_objectives` | `array` | ❌ | `[]` | 学习目标 |
| `duration` | `string` | ❌ | `1hour` | 教学时长 |
| `format` | `enum` | ❌ | `online` | `online` / `offline` / `hybrid` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话教学设计建议",
  "instructional_id": "ID-YYYY-MMDD-NNN",

  "needs_analysis": {
    "learner_profile": {
      "prior_knowledge": "low|medium|high",
      "learning_style": "visual|auditory|kinesthetic|reading",
      "motivation": "intrinsic|extrinsic",
      "constraints": ["string"]
    },
    "learning_gaps": ["string"],
    "success_criteria": ["string"]
  },

  "learning_objectives": [
    {
      "objective": "string",
      "bloom_level": "remember|understand|apply|analyze|evaluate|create",
      "assessment_method": "string",
      "success_criteria": "string"
    }
  ],

  "curriculum_design": {
    "structure": {
      "modules": [
        {
          "name": "string",
          "duration": "string",
          "objectives": ["string"],
          "activities": ["string"],
          "materials": ["string"]
        }
      ],
      "total_duration": "string"
    },
    "pedagogical_approach": "string",
    "engagement_strategies": ["string"]
  },

  "assessment_design": {
    "formative": [
      {
        "method": "string",
        "purpose": "string",
        "timing": "string"
      }
    ],
    "summative": [
      {
        "method": "string",
        "alignment": "string",
        "rubric": "string"
      }
    ],
    "feedback_mechanism": "string"
  },

  "materials_and_resources": [
    {
      "type": "string",
      "description": "string",
      "purpose": "string"
    }
  ],

  "implementation_plan": {
    "preparation": ["string"],
    "delivery_tips": ["string"],
    "contingency_plans": ["string"]
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

### Step 1: 需求分析

- **输入**：`topic` + `target_audience`
- **动作**：
  1. 分析学员画像
  2. 识别学习差距
  3. 确定成功标准
- **输出**：`needs_analysis`

### Step 2: 学习目标制定

- **输入**：`needs_analysis` + `learning_objectives`
- **动作**：
  1. 应用 Bloom 分类法
  2. 制定可衡量的目标
  3. 对齐评估方法
- **输出**：`learning_objectives`
- **Bloom 分类法**：

| 层级 | 动词 | 评估方法 |
|------|------|----------|
| 记忆 | 列举、识别、背诵 | 选择题、填空题 |
| 理解 | 解释、总结、举例 | 简答题、概念图 |
| 应用 | 使用、计算、演示 | 案例分析、实操 |
| 分析 | 比较、区分、组织 | 论文、报告 |
| 评估 | 判断、评价、辩护 | 辩论、评审 |
| 创造 | 设计、构建、发明 | 项目、作品 |

### Step 3: 课程设计

- **输入**：`learning_objectives`
- **动作**：
  1. 设计课程结构
  2. 安排教学活动
  3. 选择教学方法
- **输出**：`curriculum_design`
- **教学方法选择**：

| 方法 | 适用场景 | 优点 |
|------|----------|------|
| 讲授 | 知识传递 | 高效 |
| 讨论 | 观点交流 | 深入 |
| 案例 | 应用实践 | 真实 |
| 项目 | 综合能力 | 实践 |
| 翻转课堂 | 自主学习 | 灵活 |

### Step 4: 评估设计

- **输入**：`learning_objectives`
- **动作**：
  1. 设计形成性评估
  2. 设计总结性评估
  3. 制定评分标准
- **输出**：`assessment_design`
- **评估类型**：

| 类型 | 目的 | 时机 |
|------|------|------|
| 形成性 | 监控学习进度 | 学习过程中 |
| 总结性 | 评估学习成果 | 学习结束后 |

### Step 5: 材料和资源

- **输入**：`curriculum_design`
- **动作**：
  1. 列出所需材料
  2. 推荐学习资源
  3. 设计辅助工具
- **输出**：`materials_and_resources`

### Step 6: 实施计划

- **输入**：所有前序输出
- **动作**：
  1. 制定准备清单
  2. 提供交付建议
  3. 准备应急预案
- **输出**：`implementation_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽略学习目标的可衡量性
2. **不得**使用单一评估方法
3. **必须**考虑学员多样性

### 软性约束（建议遵守）
1. 建议每 15-20 分钟变换活动
2. 建议提供多种学习路径
3. 建议收集学员反馈

### 人工兜底点
- 当学员基础差异大时，**必须**建议分层教学
- 当涉及敏感话题时，**必须**建议谨慎处理

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `ID_WARNING_VAGUE_OBJECTIVES` | 目标不明确 | 建议重新制定 | 🟡 |
| `ID_WARNING_MISALIGNMENT` | 活动与目标不匹配 | 建议调整 | 🟡 |
| `ID_ERROR_NO_ASSESSMENT` | 缺乏评估 | 要求添加 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 学习目标已制定
- [ ] 课程结构已设计
- [ ] 评估方法已设计
- [ ] 材料已列出

### OVP 验证信号
- 学习目标达成率 ≥ 80%
- 学员满意度 ≥ 4.0/5.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "在线课程设计",
    "prompt": "设计一个2小时的Python入门在线课程",
    "context": "topic=Python入门, duration=2hours, format=online",
    "assertions": [
      "learning_objectives 包含 Bloom 分类目标",
      "curriculum_design.structure.modules 至少 3 个",
      "assessment_design.formative 已设计"
    ],
    "expected_behavior": "设计结构化的在线课程",
    "critic_attack": "是否考虑了在线学习的特殊性？"
  },
  {
    "id": "test-002",
    "name": "企业培训设计",
    "prompt": "为销售团队设计一个客户沟通技巧培训",
    "context": "topic=客户沟通, target_audience=销售团队, duration=4hours",
    "assertions": [
      "needs_analysis.learner_profile 已分析",
      "curriculum_design 包含 角色扮演活动",
      "assessment_design 包含 实操评估"
    ],
    "expected_behavior": "设计实践导向的企业培训",
    "critic_attack": "是否足够贴近实际工作场景？"
  },
  {
    "id": "test-003",
    "name": "工作坊设计",
    "prompt": "设计一个设计思维工作坊",
    "context": "topic=设计思维, duration=1day, format=offline",
    "assertions": [
      "curriculum_design.modules 包含 原型制作",
      "engagement_strategies 包含 互动活动",
      "materials_and_resources 包含 工作坊材料"
    ],
    "expected_behavior": "设计互动性强的工作坊",
    "critic_attack": "是否为参与者留出了足够的实践时间？"
  }
]
```

---

## 🔗 关联文档

- [[学习金字塔输出驱动]] — 学习方法
- [[深度学习方法]] — 深度学习
- [[知识蒸馏]] — 知识简化
- [[uSkill-日程优化-v1]] — 课程设计
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：需求分析 + Bloom分类 + 课程设计 + Self-Play |

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
