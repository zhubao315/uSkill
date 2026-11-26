
description: |
  当用户需要设计商业模式、分析商业要素、评估商业可行性、进行商业创新时使用此 Skill。
  触发词包括：'商业画布'、'商业模式'、'商业设计'、'价值主张'、'盈利模式'、
  '商业模式设计'。当用户讨论创业、产品、战略时，
  即使未直接说"商业画布"，也应使用此 Skill。
  不适用于已有成熟商业模式的优化（使用其他 Skill）。遇到商业模式设计时优先使用。

---

# uSkill-801: 商业画布

## 🎯 目标

> 使用 Business Model Canvas 9 要素框架，系统化设计和分析商业模式。

**核心价值**：商业画布是理解和设计商业模式的强大工具，一页纸看清商业全貌。

**适用场景**：
- 创业项目规划
- 新业务设计
- 商业模式创新
- 竞争对手分析
- 投资评估

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `business_idea` | `string` | ✅ | — | 商业想法描述 |
| `industry` | `string` | ❌ | — | 行业类型 |
| `stage` | `enum` | ❌ | `idea` | `idea` / `startup` / `growth` / `mature` |
| `existing_canvas` | `object` | ❌ | — | 现有商业模式（用于优化） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话商业模式总结",
  "canvas_id": "BM-YYYY-MMDD-NNN",

  "business_model_canvas": {
    "customer_segments": {
      "primary": "string",
      "secondary": ["string"],
      "personas": ["string"]
    },
    "value_propositions": {
      "core_value": "string",
      "pain_points_addressed": ["string"],
      "gains_created": ["string"],
      "differentiation": "string"
    },
    "channels": {
      "acquisition": ["string"],
      "delivery": ["string"],
      "support": ["string"]
    },
    "customer_relationships": {
      "type": "personal_assistance|self_service|automated|communities|co_creation",
      "retention_strategy": "string",
      "loyalty_programs": ["string"]
    },
    "revenue_streams": {
      "primary": "string",
      "pricing_model": "string",
      "recurring_revenue": "boolean",
      "revenue_mix": ["string"]
    },
    "key_resources": {
      "physical": ["string"],
      "intellectual": ["string"],
      "human": ["string"],
      "financial": ["string"]
    },
    "key_activities": {
      "production": ["string"],
      "platform": ["string"],
      "network": ["string"]
    },
    "key_partnerships": {
      "suppliers": ["string"],
      "strategic_alliances": ["string"],
      "joint_ventures": ["string"],
      "buyer_supplier": ["string"]
    },
    "cost_structure": {
      "fixed_costs": ["string"],
      "variable_costs": ["string"],
      "cost_drivers": ["string"]
    }
  },

  "feasibility_analysis": {
    "market_size": "string",
    "competition": "string",
    "entry_barriers": "string",
    "key_risks": ["string"],
    "mitigation_strategies": ["string"]
  },

  "financial_projections": {
    "revenue_model": "string",
    "break_even_estimate": "string",
    "funding_requirements": "string",
    "key_assumptions": ["string"]
  },

  "improvement_suggestions": [
    {
      "element": "string",
      "current_state": "string",
      "suggestion": "string",
      "impact": "high|medium|low"
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

### Step 1: 客户细分

- **输入**：`business_idea`
- **动作**：
  1. 识别主要客户群体
  2. 创建客户画像
  3. 分析客户需求
- **输出**：`business_model_canvas.customer_segments`

### Step 2: 价值主张

- **输入**：`customer_segments`
- **动作**：
  1. 定义核心价值
  2. 识别痛点解决方案
  3. 分析差异化
- **输出**：`business_model_canvas.value_propositions`
- **价值主张画布**：

| 客户侧 | 产品侧 |
|---------|---------|
| 客户任务 | 产品/服务 |
| 痛点 | 痛点缓解 |
| 期望收益 | 收益创造 |

### Step 3: 渠道通路

- **输入**：`customer_segments`
- **动作**：
  1. 设计获客渠道
  2. 设计交付渠道
  3. 设计支持渠道
- **输出**：`business_model_canvas.channels`

### Step 4: 客户关系

- **输入**：`customer_segments`
- **动作**：
  1. 确定关系类型
  2. 设计留存策略
  3. 设计忠诚度计划
- **输出**：`business_model_canvas.customer_relationships`

### Step 5: 收入来源

- **输入**：`value_propositions`
- **动作**：
  1. 识别收入来源
  2. 设计定价模型
  3. 评估经常性收入
- **输出**：`business_model_canvas.revenue_streams`

### Step 6: 核心资源

- **输入**：`value_propositions` + `channels`
- **动作**：
  1. 识别关键资源
  2. 评估资源需求
  3. 规划资源获取
- **输出**：`business_model_canvas.key_resources`

### Step 7: 关键业务

- **输入**：`value_propositions`
- **动作**：
  1. 识别关键活动
  2. 优化业务流程
  3. 评估外包需求
- **输出**：`business_model_canvas.key_activities`

### Step 8: 重要伙伴

- **输入**：`key_resources` + `key_activities`
- **动作**：
  1. 识别关键合作伙伴
  2. 设计合作模式
  3. 管理合作关系
- **输出**：`business_model_canvas.key_partnerships`

### Step 9: 成本结构

- **输入**：`key_resources` + `key_activities`
- **动作**：
  1. 识别固定成本
  2. 识别可变成本
  3. 分析成本驱动因素
- **输出**：`business_model_canvas.cost_structure`

### Step 10: 可行性分析

- **输入**：所有前序输出
- **动作**：
  1. 评估市场规模
  2. 分析竞争格局
  3. 识别关键风险
- **输出**：`feasibility_analysis`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视任何一个画布要素
2. **不得**假设市场需求而不验证
3. **必须**考虑成本和收入的平衡

### 软性约束（建议遵守）
1. 建议与潜在客户验证价值主张
2. 建议定期更新商业模式
3. 建议考虑多个收入来源

### 人工兜底点
- 当涉及重大投资决策时，**必须**建议专业咨询
- 当商业模式复杂时，**必须**建议专家评审

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `BM_WARNING_INCOMPLETE` | 画布要素不完整 | 建议补充 | 🟡 |
| `BM_WARNING_INCONSISTENT` | 要素间逻辑不一致 | 建议调整 | 🟡 |
| `BM_ERROR_NO_VALUE` | 价值主张不清晰 | 建议重新定义 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 9 个画布要素都有内容
- [ ] 要素间逻辑一致
- [ ] 可行性分析完成

### OVP 验证信号
- 商业模式完整性评分 ≥ 80/100
- 逻辑一致性评分 ≥ 85

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "SaaS商业模式",
    "prompt": "设计一个企业级SaaS产品的商业模式",
    "context": "industry=SaaS, stage=startup",
    "assertions": [
      "business_model_canvas.customer_segments 已定义",
      "business_model_canvas.value_propositions 核心价值清晰",
      "business_model_canvas.revenue_streams 包含 经常性收入"
    ],
    "expected_behavior": "设计完整的SaaS商业模式",
    "critic_attack": "是否考虑了SaaS的特殊性？"
  },
  {
    "id": "test-002",
    "name": "电商平台模式",
    "prompt": "分析一个电商平台的商业模式",
    "context": "industry=电商, stage=growth",
    "assertions": [
      "business_model_canvas 包含 所有9个要素",
      "feasibility_analysis 已完成",
      "improvement_suggestions 已生成"
    ],
    "expected_behavior": "全面分析电商商业模式",
    "critic_attack": "是否考虑了平台经济的特性？"
  },
  {
    "id": "test-003",
    "name": "新业务创新",
    "prompt": "我想做一个基于AI的个人健康助手",
    "context": "industry=HealthTech, stage=idea",
    "assertions": [
      "business_model_canvas.value_propositions 差异化明确",
      "feasibility_analysis.key_risks 已列出",
      "financial_projections 已估算"
    ],
    "expected_behavior": "设计创新的健康科技商业模式",
    "critic_attack": "是否考虑了医疗行业的监管要求？"
  }
]
```

---

## 🔗 关联文档

- [[产品验证]] — MVP验证
- [[增长黑客]] — 增长策略
- 融资准备 — 融资规划
- [[精益创业]] — 精益方法
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：9要素分析 + 可行性评估 + Self-Play |

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
