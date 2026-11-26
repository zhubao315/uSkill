
description: |
  当用户需要验证产品假设、进行客户开发、测试PMF、设计MVP时使用此 Skill。
  触发词包括：'产品验证'、'MVP'、'客户开发'、'PMF'、'假设验证'、
  '最小可行产品'。当用户讨论创业、产品开发、市场验证时，
  即使未直接说"产品验证"，也应使用此 Skill。
  不适用于成熟产品的优化（使用其他 Skill）。遇到产品验证需求时优先使用。

---

# uSkill-802: 产品验证

## 🎯 目标

> 应用精益创业方法，系统化验证产品假设，找到产品市场契合点（PMF）。

**核心价值**：避免在错误的产品上浪费资源，快速学习和迭代。

**适用场景**：
- 创业产品验证
- 新功能验证
- 市场需求验证
- 商业模式验证
- PMF 测试

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `product_idea` | `string` | ✅ | — | 产品想法描述 |
| `target_market` | `string` | ✅ | — | 目标市场 |
| `assumptions` | `array` | ❌ | `[]` | 待验证假设 |
| `resources` | `object` | ❌ | — | 可用资源 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话验证建议",
  "validation_id": "PV-YYYY-MMDD-NNN",

  "assumption_mapping": [
    {
      "assumption": "string",
      "type": "value|growth|usability|viability",
      "risk_level": "high|medium|low",
      "testable": true,
      "priority": "number"
    }
  ],

  "mvp_design": {
    "type": "landing_page|wizard_of_oz|concierge|piecemeal|prototype",
    "features": ["string"],
    "scope": "string",
    "timeline": "string",
    "budget": "string"
  },

  "customer_discovery": {
    "interview_guide": {
      "target_users": "string",
      "interview_questions": ["string"],
      "red_flags": ["string"]
    },
    "validation_experiments": [
      {
        "experiment": "string",
        "method": "string",
        "success_criteria": "string",
        "timeline": "string"
      }
    ]
  },

  "pmf_metrics": {
    "primary_metric": "string",
    "secondary_metrics": ["string"],
    "pmf_thresholds": {
      "score_4_5": "number — 认为非常失望的比例",
      "retention": "number — 月留存率",
      "nps": "number — 净推荐值"
    }
  },

  "iteration_plan": {
    "build_measure_learn_cycles": [
      {
        "cycle": "number",
        "hypothesis": "string",
        "experiment": "string",
        "success_criteria": "string"
      }
    ],
    "pivot_or_persevere_criteria": "string"
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

### Step 1: 假设识别

- **输入**：`product_idea` + `assumptions`
- **动作**：
  1. 识别关键假设
  2. 分类假设类型
  3. 评估风险等级
- **输出**：`assumption_mapping`
- **假设类型**：

| 类型 | 描述 | 示例 |
|------|------|------|
| 价值假设 | 客户是否需要 | 用户愿意付费 |
| 增长假设 | 如何获客 | 口碑传播 |
| 可用性假设 | 产品是否好用 | 用户能完成任务 |
| 可行性假设 | 业务是否可行 | 能盈利 |

### Step 2: MVP 设计

- **输入**：`assumption_mapping`
- **动作**：
  1. 选择 MVP 类型
  2. 定义核心功能
  3. 设计开发计划
- **输出**：`mvp_design`
- **MVP 类型选择**：

| 类型 | 描述 | 适用场景 |
|------|------|----------|
| 落地页 | 单页网站测试需求 | 早期验证 |
| 乌兹别克 | 人工模拟产品 | 验证价值 |
| 走廊测试 | 手动服务少量用户 | 验证可用性 |
| 原型 | 可交互原型 | 验证设计 |

### Step 3: 客户开发

- **输入**：`assumption_mapping` + `target_market`
- **动作**：
  1. 设计访谈指南
  2. 制定验证实验
  3. 定义成功标准
- **输出**：`customer_discovery`
- **访谈问题示例**：

| 问题类型 | 示例 |
|----------|------|
| 痛点 | 你目前如何解决这个问题？ |
| 价值 | 这个解决方案对你有多大价值？ |
| 意愿 | 你愿意为这个解决方案付费吗？ |
| 行为 | 你最近一次遇到这个问题是什么时候？ |

### Step 4: PMF 指标

- **输入**：`product_idea` + `target_market`
- **动作**：
  1. 定义主要指标
  2. 设定 PMF 阈值
  3. 制定跟踪计划
- **输出**：`pmf_metrics`
- **PMF 判断标准**：

| 指标 | 阈值 | 说明 |
|------|------|------|
| Sean Ellis 测试 | ≥40% | 认为"非常失望"的比例 |
| 月留存率 | ≥30% | 30天后仍活跃 |
| NPS | ≥50 | 净推荐值 |

### Step 5: 迭代计划

- **输入**：`assumption_mapping` + `mvp_design`
- **动作**：
  1. 设计构建-测量-学习循环
  2. 设定转型或坚持标准
  3. 制定时间表
- **输出**：`iteration_plan`

### Step 6: 风险评估

- **输入**：所有前序输出
- **动作**：
  1. 识别关键风险
  2. 制定缓解策略
  3. 设定终止标准
- **输出**：`risk_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**跳过验证直接开发完整产品
2. **不得**忽视负面反馈
3. **必须**设定明确的终止标准

### 软性约束（建议遵守）
1. 建议在 2 周内完成一次验证循环
2. 建议至少访谈 10 个潜在用户
3. 建议记录所有学习和发现

### 人工兜底点
- 当验证结果与预期严重不符时，**必须**建议深度分析
- 当资源耗尽时，**必须**建议是否继续

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `PV_WARNING_NO_TRACTION` | 无市场反响 | 建议调整方向 | 🟡 |
| `PV_WARNING_LOW_RETENTION` | 留存率低 | 建议改进产品 | 🟡 |
| `PV_ERROR_KILL_CRITERIA` | 达到终止标准 | 建议停止或转型 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 假设已识别和分类
- [ ] MVP 设计完成
- [ ] 客户开发计划已制定
- [ ] PMF 指标已定义

### OVP 验证信号
- 假设验证率 ≥ 80%
- PMF 达成率 ≥ 50%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "SaaS产品验证",
    "prompt": "验证一个项目管理SaaS的想法",
    "context": "target_market=SMB, assumptions=[用户需要协作功能]",
    "assertions": [
      "assumption_mapping 包含 价值假设",
      "mvp_design.type = landing_page 或 prototype",
      "customer_discovery.interview_guide 已生成"
    ],
    "expected_behavior": "设计SaaS产品的验证计划",
    "critic_attack": "是否考虑了竞争格局？"
  },
  {
    "id": "test-002",
    "name": "电商产品验证",
    "prompt": "我想做一个垂直领域的电商平台",
    "context": "target_market=细分市场",
    "assertions": [
      "assumption_mapping 包含 需求假设",
      "pmf_metrics.primary_metric 已定义",
      "iteration_plan.build_measure_learn_cycles 至少 2 个"
    ],
    "expected_behavior": "设计电商平台的验证计划",
    "critic_attack": "是否验证了支付意愿？"
  },
  {
    "id": "test-003",
    "name": "移动应用验证",
    "prompt": "验证一个健康管理App的想法",
    "context": "target_market=健身爱好者",
    "assertions": [
      "mvp_design 包含 核心功能列表",
      "risk_assessment.key_risks 已列出",
      "risk_assessment.kill_criteria 已定义"
    ],
    "expected_behavior": "设计App的验证计划",
    "critic_attack": "是否考虑了用户获取成本？"
  }
]
```

---

## 🔗 关联文档

- [[商业画布]] — 商业模式设计
- [[增长黑客]] — 增长策略
- [[精益创业]] — 精益方法
- 融资准备 — 融资规划
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：假设识别 + MVP设计 + 客户开发 + Self-Play |

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


**相关概念**：[[需求分析]] · [[价值网络]]

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
