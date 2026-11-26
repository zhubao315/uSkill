
description: |
  当用户需要分析行业结构、评估竞争格局、识别行业趋势、进行行业比较时使用此 Skill。
  触发词包括：'行业分析'、'竞争格局'、'波特五力'、'行业趋势'、'市场分析'、
  '行业研究'。当用户讨论投资、战略、市场研究时，
  即使未直接说"行业分析"，也应使用此 Skill。
  不适用于公司层面分析（使用财报解读）。遇到行业层面分析时优先使用。

---

# uSkill-503: 行业分析

## 🎯 目标

> 使用波特五力、价值链、生命周期等框架，全面分析行业结构和竞争动态。

**核心价值**：行业结构决定竞争规则。理解行业是投资和战略的基础。

**适用场景**：
- 投资行业选择
- 竞争战略制定
- 市场进入决策
- 并购目标筛选
- 行业趋势研判

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `industry_name` | `string` | ✅ | — | 行业名称 |
| `analysis_framework` | `array` | ❌ | `all` | 分析框架 |
| `geographic_scope` | `string` | ❌ | `global` | 地理范围 |
| `time_horizon` | `number` | ❌ | `5` | 预测时间范围（年） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话行业分析结论",
  "industry_id": "IA-YYYY-MMDD-NNN",

  "industry_overview": {
    "definition": "string",
    "market_size": "string",
    "growth_rate": "number",
    "key_drivers": ["string"],
    "industry_lifecycle_stage": "introduction|growth|maturity|decline"
  },

  "porter_five_forces": {
    "threat_of_new_entrants": {
      "level": "low|medium|high",
      "barriers": ["string"],
      "factors": ["string"]
    },
    "threat_of_substitutes": {
      "level": "low|medium|high",
      "substitutes": ["string"],
      "switching_costs": "string"
    },
    "bargaining_power_of_buyers": {
      "level": "low|medium|high",
      "factors": ["string"]
    },
    "bargaining_power_of_suppliers": {
      "level": "low|medium|high",
      "factors": ["string"]
    },
    "competitive_rivalry": {
      "level": "low|medium|high",
      "competitors": ["string"],
      "competition_factors": ["string"]
    },
    "overall_attractiveness": "low|medium|high"
  },

  "value_chain_analysis": {
    "primary_activities": [
      {
        "activity": "string",
        "importance": "high|medium|low",
        "key_players": ["string"]
      }
    ],
    "support_activities": ["string"],
    "value_creation_opportunities": ["string"]
  },

  "competitive_landscape": {
    "market_structure": "perfect_competition|monopolistic|oligopoly|monopoly",
    "key_players": [
      {
        "name": "string",
        "market_share": "number",
        "competitive_advantage": "string",
        "strategy": "string"
      }
    ],
    "competitive_dynamics": "string"
  },

  "trend_analysis": {
    "technological_trends": ["string"],
    "regulatory_trends": ["string"],
    "consumer_trends": ["string"],
    "economic_trends": ["string"],
    "impact_assessment": "string"
  },

  "opportunities_and_threats": {
    "opportunities": [
      {
        "opportunity": "string",
        "probability": "high|medium|low",
        "impact": "high|medium|low"
      }
    ],
    "threats": [
      {
        "threat": "string",
        "probability": "high|medium|low",
        "impact": "high|medium|low"
      }
    ]
  },

  "investment_implications": {
    "best_segments": ["string"],
    "avoid_segments": ["string"],
    "key_success_factors": ["string"],
    "risks": ["string"]
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

### Step 1: 行业概况

- **输入**：`industry_name`
- **动作**：
  1. 定义行业边界
  2. 评估市场规模
  3. 识别增长驱动因素
- **输出**：`industry_overview`
- **行业生命周期**：

| 阶段 | 特征 | 投资策略 |
|------|------|----------|
| 导入期 | 高增长、高风险 | 选择性投资 |
| 成长期 | 快速增长、竞争加剧 | 龙头公司 |
| 成熟期 | 增长放缓、利润稳定 | 价值投资 |
| 衰退期 | 增长停滞、利润下降 | 避免或做空 |

### Step 2: 波特五力分析

- **输入**：`industry_name`
- **动作**：
  1. 评估新进入者威胁
  2. 评估替代品威胁
  3. 评估买方议价能力
  4. 评估供应商议价能力
  5. 评估竞争强度
- **输出**：`porter_five_forces`
- **进入壁垒类型**：

| 壁垒 | 描述 | 示例 |
|------|------|------|
| 规模经济 | 大规模生产成本优势 | 制造业 |
| 资本需求 | 需要大量投资 | 芯片制造 |
| 转换成本 | 客户转换成本高 | 企业软件 |
| 品牌忠诚 | 客户品牌偏好 | 消费品 |
| 政策壁垒 | 政府法规限制 | 金融、医疗 |

### Step 3: 价值链分析

- **输入**：`industry_name`
- **动作**：
  1. 识别主要活动
  2. 识别支持活动
  3. 发现价值创造机会
- **输出**：`value_chain_analysis`

### Step 4: 竞争格局

- **输入**：`industry_name`
- **动作**：
  1. 评估市场结构
  2. 分析主要竞争者
  3. 评估竞争动态
- **输出**：`competitive_landscape`

### Step 5: 趋势分析

- **输入**：`industry_name` + `time_horizon`
- **动作**：
  1. 识别技术趋势
  2. 识别监管趋势
  3. 识别消费者趋势
- **输出**：`trend_analysis`

### Step 6: 机会和威胁

- **输入**：所有前序输出
- **动作**：
  1. 识别投资机会
  2. 识别潜在威胁
  3. 评估概率和影响
- **输出**：`opportunities_and_threats`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**忽视行业特定因素
2. **不得**仅看当前状态而忽视趋势
3. **必须**进行横向比较

### 软性约束（建议遵守）
1. 建议考虑多个时间尺度
2. 建议参考多个信息来源
3. 建议定期更新分析

### 人工兜底点
- 当涉及重大投资决策时，**必须**建议专业研究
- 当行业复杂时，**必须**建议细分分析

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IA_WARNING_DATA_GAP` | 数据不足 | 降低置信度 | 🟡 |
| `IA_WARNING_RAPID_CHANGE` | 行业快速变化 | 建议频繁更新 | 🟡 |
| `IA_ERROR_UNDEFINED` | 行业定义不清 | 要求澄清 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 行业概况已分析
- [ ] 波特五力已评估
- [ ] 竞争格局已分析
- [ ] 趋势已识别

### OVP 验证信号
- 行业分析深度评分 ≥ 80/100
- 趋势判断准确率 ≥ 70%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "科技行业分析",
    "prompt": "分析人工智能行业",
    "context": "industry_name=AI, geographic_scope=global",
    "assertions": [
      "industry_overview 包含 市场规模和增长",
      "porter_five_forces 五力都有评估",
      "trend_analysis 包含 技术趋势"
    ],
    "expected_behavior": "全面分析AI行业",
    "critic_attack": "是否考虑了AI的快速变化？"
  },
  {
    "id": "test-002",
    "name": "传统行业分析",
    "prompt": "分析传统汽车制造业",
    "context": "industry_name=Automotive, time_horizon=10",
    "assertions": [
      "industry_overview.industry_lifecycle_stage = maturity",
      "porter_five_forces.threat_of_substitutes 分析电动车",
      "opportunities_and_threats 包含 转型机会"
    ],
    "expected_behavior": "分析传统行业的转型",
    "critic_attack": "是否充分考虑了电动化影响？"
  },
  {
    "id": "test-003",
    "name": "新兴行业分析",
    "prompt": "分析新能源行业",
    "context": "industry_name=Renewable Energy, geographic_scope=China",
    "assertions": [
      "industry_overview.growth_rate > 10%",
      "trend_analysis.regulatory_trends 包含 政策支持",
      "investment_implications.best_segments 已列出"
    ],
    "expected_behavior": "分析高增长行业",
    "critic_attack": "是否考虑了政策风险？"
  }
]
```

---

## 🔗 关联文档

- [[估值分析]] — 估值方法
- [[财报解读]] — 公司分析
- [[uSkill-日程优化-v1]] — 趋势分析
- [[uSkill-日程优化-v1]] — 竞争分析
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：波特五力 + 价值链 + 竞争格局 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [投资决策类型] for [投资者风格], with [风险偏好], leaning toward [分析框架/数据源]."

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
| ""这次不一样"" | "每次泡沫都说这次不一样，这次也一样" |
| ""先满仓再说"" | "满仓=零容错，一个回调就是灾难" |
| ""跌了就补仓"" | "越补越套是亏损扩大的主因" |
| ""长期持有就行"" | "长期持有不等于不做仓位管理" |
| ""这次消息是利好"" | "消息面驱动的交易成功率低于掷硬币" |

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
