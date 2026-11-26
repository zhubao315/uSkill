
description: |
  当用户需要创新商业模式、重新设计盈利方式、颠覆传统行业、寻找蓝海市场时使用此 Skill。
  触发词包括：'商业模式创新'、'盈利模式'、'颠覆式创新'、'蓝海战略'、
  '重新设计商业模式'。当用户讨论创业、战略转型、行业变革时，
  即使未直接说"商业模式创新"，也应使用此 Skill。
  不适用于现有模式优化（使用商业画布）。遇到颠覆性创新需求时优先使用。

---

# uSkill-803: 商业模式创新

## 🎯 目标

> 使用商业模式创新工具，发现新的价值创造和价值获取方式。

**核心价值**：商业模式创新比产品创新更能改变行业格局。

**适用场景**：
- 行业颠覆
- 新市场创造
- 盈利模式重构
- 平台经济设计
- 生态系统构建

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `current_model` | `string` | ✅ | — | 当前商业模式描述 |
| `innovation_goal` | `enum` | ❌ | `disrupt` | `disrupt` / `expand` / `optimize` / `create` |
| `industry_context` | `string` | ❌ | — | 行业背景 |
| `constraints` | `array` | ❌ | `[]` | 限制条件 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话创新建议",
  "innovation_id": "BI-YYYY-MMDD-NNN",

  "current_model_analysis": {
    "strengths": ["string"],
    "weaknesses": ["string"],
    "opportunities": ["string"],
    "threats": ["string"]
  },

  "innovation_frameworks": {
    "blue_ocean_strategy": {
      "eliminate": ["string"],
      "reduce": ["string"],
      "raise": ["string"],
      "create": ["string"]
    },
    "business_model_patterns": [
      {
        "pattern": "string",
        "description": "string",
        "applicability": "high|medium|low"
      }
    ]
  },

  "innovation_ideas": [
    {
      "idea": "string",
      "description": "string",
      "value_proposition": "string",
      "revenue_model": "string",
      "key_resources": ["string"],
      "feasibility": "high|medium|low",
      "impact": "high|medium|low"
    }
  ],

  "implementation_roadmap": {
    "phase_1": {
      "name": "验证期",
      "duration": "string",
      "key_activities": ["string"],
      "success_criteria": "string"
    },
    "phase_2": {
      "name": "构建期",
      "duration": "string",
      "key_activities": ["string"],
      "success_criteria": "string"
    },
    "phase_3": {
      "name": "扩展期",
      "duration": "string",
      "key_activities": ["string"],
      "success_criteria": "string"
    }
  },

  "risk_assessment": {
    "key_risks": ["string"],
    "mitigation_strategies": ["string"],
    "kill_criteria": "string"
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

### Step 1: 当前模式分析

- **输入**：`current_model`
- **动作**：
  1. 分析当前模式的优势
  2. 识别弱点和机会
  3. 评估威胁
- **输出**：`current_model_analysis`

### Step 2: 创新框架应用

- **输入**：`current_model_analysis` + `innovation_goal`
- **动作**：
  1. 应用蓝海战略 ERRC 矩阵
  2. 应用商业模式模式库
  3. 生成创新想法
- **输出**：`innovation_frameworks`
- **商业模式创新模式**：

| 模式 | 描述 | 示例 |
|------|------|------|
| 平台模式 | 连接双方或多边市场 | 淘宝、Uber |
| 订阅模式 | 定期收费 | Netflix、Spotify |
| 免费增值 | 基础免费，高级付费 | Dropbox、LinkedIn |
| 共享经济 | 共享闲置资源 | Airbnb、滴滴 |
| 数据变现 | 利用数据创造价值 | Google、Facebook |

### Step 3: 创新想法生成

- **输入**：`innovation_frameworks`
- **动作**：
  1. 生成多个创新想法
  2. 评估每个想法
  3. 选择最有潜力的想法
- **输出**：`innovation_ideas`

### Step 4: 实施路线图

- **输入**：`innovation_ideas`
- **动作**：
  1. 设计验证期
  2. 设计构建期
  3. 设计扩展期
- **输出**：`implementation_roadmap`

### Step 5: 风险评估

- **输入**：`innovation_ideas`
- **动作**：
  1. 识别关键风险
  2. 制定缓解策略
  3. 设定终止标准
- **输出**：`risk_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视市场需求
2. **不得**过度理想化
3. **必须**考虑可执行性

### 软性约束（建议遵守）
1. 建议从小规模验证开始
2. 建议保持迭代心态
3. 建议关注现金流

### 人工兜底点
- 当涉及重大投资时，**必须**建议专业评估
- 当创新颠覆性强时，**必须**建议深度验证

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `BI_WARNING_UNFEASIBLE` | 方案不可行 | 建议调整 | 🟡 |
| `BI_WARNING_INCREMENTAL` | 创新不够颠覆 | 建议更大胆 | 🟡 |
| `BI_ERROR_NO_VALUE` | 无价值创造 | 建议重新思考 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 当前模式已分析
- [ ] 创新框架已应用
- [ ] 创新想法已生成
- [ ] 实施路线图已设计

### OVP 验证信号
- 创新想法数量 ≥ 3
- 可行性评分 ≥ 75/100

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "传统行业颠覆",
    "prompt": "如何颠覆传统出租车行业",
    "context": "current_model=传统出租车, innovation_goal=disrupt",
    "assertions": [
      "innovation_frameworks.blue_ocean_strategy 已应用",
      "innovation_ideas 至少 2 个创新想法",
      "implementation_roadmap 已设计"
    ],
    "expected_behavior": "生成颠覆性创新方案",
    "critic_attack": "是否考虑了监管因素？"
  },
  {
    "id": "test-002",
    "name": "盈利模式创新",
    "prompt": "如何为免费产品设计盈利模式",
    "context": "current_model=免费产品, innovation_goal=create",
    "assertions": [
      "innovation_frameworks.business_model_patterns 包含 免费增值",
      "innovation_ideas.revenue_model 已设计",
      "risk_assessment 已完成"
    ],
    "expected_behavior": "设计新的盈利模式",
    "critic_attack": "用户是否愿意付费？"
  },
  {
    "id": "test-003",
    "name": "平台经济设计",
    "prompt": "设计一个双边平台的商业模式",
    "context": "current_model=双边市场, innovation_goal=expand",
    "assertions": [
      "innovation_frameworks.business_model_patterns 包含 平台模式",
      "innovation_ideas.key_resources 包含 网络效应",
      "implementation_roadmap.phase_1 包含 冷启动策略"
    ],
    "expected_behavior": "设计平台经济模式",
    "critic_attack": "如何解决冷启动问题？"
  }
]
```

---

## 🔗 关联文档

- [[商业画布]] — 商业模式设计
- [[产品验证]] — 假设验证
- [[增长黑客]] — 增长策略
- [[精益创业]] — 精益方法
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：蓝海战略 + 创新模式 + 实施路线 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务] for [业务阶段], with [资源约束], leaning toward [策略框架/执行路径]."

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
| ""先做再说"" | "方向错了，执行力越强死得越快" |
| ""用户说想要这个"" | "用户说的是解决方案，不是需求本身" |
| ""竞品都在做"" | "竞品犯错不意味着你也应该犯" |
| ""这个市场很大"" | "大市场≠你能切到的市场" |

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


**相关概念**：[[价值网络]]

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
