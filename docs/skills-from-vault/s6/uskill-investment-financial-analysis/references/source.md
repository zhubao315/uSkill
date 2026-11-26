
description: |
  当用户需要解读财务报表、分析公司财务健康、识别财务风险、评估投资价值时使用此 Skill。
  触发词包括：'财报'、'财务分析'、'资产负债表'、'利润表'、'现金流量表'、
  '财务比率'、'财务健康'。当用户讨论投资分析、股票研究、公司评估时，
  即使未直接说"财报解读"，也应使用此 Skill。
  不适用于技术分析（使用其他 Skill）。遇到基本面财务分析时优先使用。

---

# uSkill-502: 财报解读

## 🎯 目标

> 系统化解读三大财务报表，识别关键财务指标，发现潜在风险和机会。

**核心价值**：财务报表是公司的"体检报告"。读懂财报是投资的基本功。

**适用场景**：
- 股票投资分析
- 公司财务健康评估
- 并购尽职调查
- 信用风险评估
- 竞争对手分析

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `company_name` | `string` | ✅ | — | 公司名称 |
| `financial_statements` | `object` | ❌ | — | 财务报表数据 |
| `analysis_focus` | `enum` | ❌ | `full` | `profitability` / `liquidity` / `solvency` / `efficiency` / `full` |
| `comparison_period` | `enum` | ❌ | `yoy` | `yoy` / `qoq` / `trend` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话财务分析结论",
  "financial_id": "FA-YYYY-MMDD-NNN",

  "income_statement_analysis": {
    "revenue": {
      "amount": "number",
      "growth_rate": "number",
      "quality": "string"
    },
    "profitability": {
      "gross_margin": "number",
      "operating_margin": "number",
      "net_margin": "number",
      "trend": "improving|stable|declining"
    },
    "red_flags": ["string"]
  },

  "balance_sheet_analysis": {
    "assets": {
      "total_assets": "number",
      "asset_quality": "string",
      "goodwill_ratio": "number"
    },
    "liabilities": {
      "total_liabilities": "number",
      "debt_level": "low|medium|high",
      "debt_structure": "string"
    },
    "equity": {
      "shareholders_equity": "number",
      "retained_earnings": "number",
      "equity_quality": "string"
    }
  },

  "cash_flow_analysis": {
    "operating_cash_flow": "number",
    "investing_cash_flow": "number",
    "financing_cash_flow": "number",
    "free_cash_flow": "number",
    "cash_flow_quality": "string"
  },

  "financial_ratios": {
    "profitability": {
      "roe": "number",
      "roa": "number",
      "roic": "number"
    },
    "liquidity": {
      "current_ratio": "number",
      "quick_ratio": "number"
    },
    "solvency": {
      "debt_to_equity": "number",
      "interest_coverage": "number"
    },
    "efficiency": {
      "asset_turnover": "number",
      "inventory_turnover": "number",
      "receivable_turnover": "number"
    }
  },

  "quality_of_earnings": {
    "accrual_ratio": "number",
    "cash_conversion": "number",
    "recurring_revenue": "number",
    "earnings_quality": "high|medium|low"
  },

  "risk_assessment": {
    "financial_health_score": "number",
    "key_risks": ["string"],
    "warning_signs": ["string"],
    "strengths": ["string"]
  },

  "peer_comparison": {
    "industry_average": {
      "roe": "number",
      "debt_to_equity": "number",
      "margin": "number"
    },
    "relative_position": "above|at|below"
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

### Step 1: 利润表分析

- **输入**：`financial_statements.income_statement`
- **动作**：
  1. 分析收入增长
  2. 评估盈利能力
  3. 识别异常项目
- **输出**：`income_statement_analysis`
- **关键指标**：

| 指标 | 公式 | 说明 |
|------|------|------|
| 毛利率 | (收入-成本)/收入 | 产品盈利能力 |
| 营业利润率 | 营业利润/收入 | 经营效率 |
| 净利率 | 净利润/收入 | 整体盈利 |

### Step 2: 资产负债表分析

- **输入**：`financial_statements.balance_sheet`
- **动作**：
  1. 评估资产质量
  2. 分析负债结构
  3. 评估权益质量
- **输出**：`balance_sheet_analysis`

### Step 3: 现金流量表分析

- **输入**：`financial_statements.cash_flow`
- **动作**：
  1. 分析经营现金流
  2. 评估投资活动
  3. 分析融资活动
- **输出**：`cash_flow_analysis`
- **现金流质量指标**：

| 指标 | 健康标准 | 风险信号 |
|------|----------|----------|
| 经营现金流/净利润 | > 1 | < 0.8 |
| 自由现金流 | 正且增长 | 持续为负 |
| 资本支出/折旧 | 合理比例 | 过高或过低 |

### Step 4: 财务比率计算

- **输入**：所有财务数据
- **动作**：
  1. 计算盈利能力比率
  2. 计算流动性比率
  3. 计算偿债能力比率
  4. 计算效率比率
- **输出**：`financial_ratios`

### Step 5: 盈利质量评估

- **输入**：`income_statement_analysis` + `cash_flow_analysis`
- **动作**：
  1. 计算应计比率
  2. 评估现金转换率
  3. 识别经常性收入
- **输出**：`quality_of_earnings`

### Step 6: 风险评估

- **输入**：所有前序输出
- **动作**：
  1. 计算财务健康评分
  2. 识别关键风险
  3. 发现优势和机会
- **输出**：`risk_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**仅看单一指标下结论
2. **不得**忽视会计政策变更
3. **必须**进行横向和纵向比较

### 软性约束（建议遵守）
1. 建议至少分析 3 年数据
2. 建议与行业平均比较
3. 建议关注现金流而非仅利润

### 人工兜底点
- 当发现会计操纵迹象时，**必须**深入调查
- 当涉及重大投资决策时，**必须**建议专业分析

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `FA_WARNING_DATA_QUALITY` | 数据质量差 | 降低置信度 | 🟡 |
| `FA_WARNING_ACCOUNTING` | 会计政策变更 | 标记警告 | 🟡 |
| `FA_ERROR_MANIPULATION` | 疑似会计操纵 | 深入调查 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 三大报表已分析
- [ ] 关键比率已计算
- [ ] 盈利质量已评估
- [ ] 风险已识别

### OVP 验证信号
- 财务分析准确率 ≥ 85%
- 风险预警准确率 ≥ 80%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "科技公司财报分析",
    "prompt": "分析苹果公司最新财报",
    "context": "company_name=Apple, analysis_focus=full",
    "assertions": [
      "income_statement_analysis 包含 收入和利润分析",
      "financial_ratios 包含 所有类别",
      "risk_assessment 已生成"
    ],
    "expected_behavior": "全面分析科技公司财报",
    "critic_attack": "是否考虑了科技公司的特殊性？"
  },
  {
    "id": "test-002",
    "name": "盈利能力分析",
    "prompt": "重点分析这家公司的盈利能力",
    "context": "analysis_focus=profitability",
    "assertions": [
      "income_statement_analysis.profitability 详细分析",
      "financial_ratios.profitability 包含 ROE、ROA、ROIC",
      "peer_comparison 已完成"
    ],
    "expected_behavior": "深度分析盈利能力",
    "critic_attack": "是否考虑了会计政策的影响？"
  },
  {
    "id": "test-003",
    "name": "风险预警",
    "prompt": "检查这家公司是否有财务风险",
    "context": "analysis_focus=solvency",
    "assertions": [
      "risk_assessment.warning_signs 已列出",
      "balance_sheet_analysis.liabilities.debt_level 已评估",
      "cash_flow_analysis 已分析偿债能力"
    ],
    "expected_behavior": "识别财务风险",
    "critic_attack": "是否遗漏了隐性负债？"
  }
]
```

---

## 🔗 关联文档

- [[估值分析]] — 估值方法
- [[uSkill-日程优化-v1]] — 标的筛选
- [[格雷厄姆安全边际分析]] — 价值投资
- [[现金流四象限分析]] — 现金流分析
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：三表分析 + 财务比率 + 盈利质量 + Self-Play |

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
