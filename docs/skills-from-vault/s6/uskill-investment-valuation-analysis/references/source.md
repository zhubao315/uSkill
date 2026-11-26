
description: |
  当用户需要对公司或资产进行估值分析、选择估值方法、评估投资价值时使用此 Skill。
  触发词包括：'估值'、'DCF'、'PE'、'PB'、'PS'、'估值分析'、'公司估值'、
  '股票估值'。当用户讨论投资分析、股票研究、并购估值时，
  即使未直接说"估值分析"，也应使用此 Skill。
  不适用于技术分析（使用其他 Skill）。遇到基本面估值需求时优先使用。

---

# uSkill-501: 估值分析

## 🎯 目标

> 应用多种估值方法，对公司或资产进行全面估值，识别低估或高估机会。

**核心价值**：估值是投资决策的基础。正确的估值能帮助识别安全边际。

**适用场景**：
- 股票投资分析
- 并购估值
- 创业公司估值
- 房地产估值
- 资产评估

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `target` | `string` | ✅ | — | 待估值公司/资产 |
| `valuation_methods` | `array` | ❌ | `all` | 指定估值方法 |
| `data_sources` | `object` | ❌ | — | 财务数据来源 |
| `time_horizon` | `number` | ❌ | `5` | 预测时间范围（年） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话估值结论",
  "valuation_id": "VA-YYYY-MMDD-NNN",

  "company_overview": {
    "name": "string",
    "industry": "string",
    "competitive_position": "string",
    "key_metrics": {
      "revenue": "number",
      "growth_rate": "number",
      "profit_margin": "number",
      "market_cap": "number"
    }
  },

  "dcf_valuation": {
    "assumptions": {
      "growth_rate": "number",
      "discount_rate": "number",
      "terminal_growth_rate": "number",
      "projection_years": "number"
    },
    "free_cash_flow_projections": [
      {
        "year": "number",
        "fcf": "number",
        "pv": "number"
      }
    ],
    "terminal_value": "number",
    "enterprise_value": "number",
    "equity_value": "number",
    "per_share_value": "number",
    "sensitivity_analysis": {
      "optimistic": "number",
      "base": "number",
      "pessimistic": "number"
    }
  },

  "relative_valuation": {
    "comparable_companies": [
      {
        "name": "string",
        "pe_ratio": "number",
        "pb_ratio": "number",
        "ps_ratio": "number",
        "ev_ebitda": "number"
      }
    ],
    "peer_average": {
      "pe_ratio": "number",
      "pb_ratio": "number",
      "ps_ratio": "number",
      "ev_ebitda": "number"
    },
    "implied_valuation": {
      "pe_based": "number",
      "pb_based": "number",
      "ps_based": "number"
    }
  },

  "asset_valuation": {
    "book_value": "number",
    "tangible_assets": "number",
    "intangible_assets": "number",
    "net_asset_value": "number"
  },

  "valuation_summary": {
    "methods_used": ["string"],
    "value_range": {
      "low": "number",
      "high": "number",
      "midpoint": "number"
    },
    "current_price": "number",
    "margin_of_safety": "number",
    "recommendation": "undervalued|fairly_valued|overvalued"
  },

  "key_assumptions": [
    {
      "assumption": "string",
      "impact": "high|medium|low",
      "sensitivity": "string"
    }
  ],

  "risks_and_caveats": ["string"],

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 公司概况分析

- **输入**：`target`
- **动作**：
  1. 收集公司基本信息
  2. 分析竞争地位
  3. 评估关键财务指标
- **输出**：`company_overview`

### Step 2: DCF 估值

- **输入**：`company_overview` + `data_sources`
- **动作**：
  1. 预测自由现金流
  2. 确定折现率
  3. 计算终值和企业价值
- **输出**：`dcf_valuation`
- **DCF 关键假设**：

| 参数 | 说明 | 典型范围 |
|------|------|----------|
| 增长率 | 未来 FCF 增长 | 2-15% |
| 折现率 | WACC | 8-12% |
| 终值增长率 | 永续增长 | 2-3% |

### Step 3: 相对估值

- **输入**：`company_overview`
- **动作**：
  1. 选择可比公司
  2. 计算估值倍数
  3. 应用倍数估值
- **输出**：`relative_valuation`
- **常用估值倍数**：

| 倍数 | 公式 | 适用场景 |
|------|------|----------|
| PE | 市值/净利润 | 盈利稳定公司 |
| PB | 市值/净资产 | 资产密集型 |
| PS | 市值/营收 | 成长型公司 |
| EV/EBITDA | 企业价值/EBITDA | 资本结构差异大 |

### Step 4: 资产估值

- **输入**：`company_overview` + `data_sources`
- **动作**：
  1. 评估账面价值
  2. 评估有形资产
  3. 评估无形资产
- **输出**：`asset_valuation`

### Step 5: 综合估值

- **输入**：所有前序输出
- **动作**：
  1. 综合多种方法
  2. 确定价值区间
  3. 计算安全边际
- **输出**：`valuation_summary`
- **安全边际计算**：
  ```
  安全边际 = (内在价值 - 市场价格) / 内在价值
  ```

### Step 6: 敏感性分析

- **输入**：`dcf_valuation`
- **动作**：
  1. 测试关键假设变化
  2. 识别价值驱动因素
  3. 评估估值稳健性
- **输出**：`dcf_valuation.sensitivity_analysis`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**将估值等同于投资建议
2. **不得**忽视风险因素
3. **必须**标注关键假设和不确定性

### 软性约束（建议遵守）
1. 建议使用多种估值方法交叉验证
2. 建议进行敏感性分析
3. 建议定期更新估值

### 人工兜底点
- 当涉及重大投资决策时，**必须**建议专业咨询
- 当数据质量差时，**必须**标注不确定性

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `VA_WARNING_LOW_DATA` | 数据不足 | 降低置信度 | 🟡 |
| `VA_WARNING_NEGATIVE_FCF` | FCF 为负 | 使用替代方法 | 🟡 |
| `VA_ERROR_NO_VALUATION` | 无法估值 | 说明原因 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] DCF 估值完成
- [ ] 相对估值完成
- [ ] 综合估值已计算
- [ ] 敏感性分析已进行

### OVP 验证信号
- 估值偏差率 < 25%
- 投资决策正确率 ≥ 60%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "成熟公司估值",
    "prompt": "分析苹果公司的估值，当前股价150美元",
    "context": "target=Apple, time_horizon=5",
    "assertions": [
      "dcf_valuation 包含 FCF 预测",
      "relative_valuation 包含 可比公司",
      "valuation_summary.recommendation 已给出"
    ],
    "expected_behavior": "全面估值分析",
    "critic_attack": "增长率假设是否过于乐观？"
  },
  {
    "id": "test-002",
    "name": "成长公司估值",
    "prompt": "评估一个未盈利的SaaS公司",
    "context": "target=SaaS Startup, valuation_methods=[PS, EV/Revenue]",
    "assertions": [
      "relative_valuation 包含 PS 倍数",
      "key_assumptions 列出关键假设",
      "risks_and_caveats 已列出"
    ],
    "expected_behavior": "适用于成长公司的估值方法",
    "critic_attack": "是否过度依赖相对估值？"
  },
  {
    "id": "test-003",
    "name": "安全边际计算",
    "prompt": "这只股票的内在价值是多少？当前价格是否有安全边际？",
    "context": "target=Value Stock",
    "assertions": [
      "valuation_summary.value_range 已计算",
      "valuation_summary.margin_of_safety 已计算",
      "recommendation 基于安全边际"
    ],
    "expected_behavior": "计算安全边际并给出建议",
    "critic_attack": "内在价值估计是否准确？"
  }
]
```

---

## 🔗 关联文档

- [[uSkill-日程优化-v1]] — 标的筛选
- [[决策推理-Schema]] — 决策框架
- [[uSkill-日程优化-v1]] — 概率决策
- [[uSkill-日程优化-v1]] — 风险管理
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：DCF + 相对估值 + 资产估值 + Self-Play |

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
