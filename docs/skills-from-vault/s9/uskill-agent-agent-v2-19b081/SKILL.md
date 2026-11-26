---
name: uskill-agent-agent-v2-19b081
description: "让投资组合监控 Agent v2 — 增强版实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-投资组合监控-agent-v2-增强版实施手册.md"
  original_id: "SKL-7032"
  version: "3.0.0"
  trust: untrusted
---

# 投资组合监控 Agent v2 — 增强版实施手册

# 💰 投资组合监控 Agent v2 — 增强版实施手册

> **定位**：每日收盘后执行 R1-R4 风控检查 + 贵金属专项分析 + 预测分析 + 研报收集 + 结论生成
>
> **关联**：[[风控规则手册]] · [[2026-06 投资策略与风控方案]] · [[2026年度投资计划_AI-Co_Evolution]]

---

## 一、Agent 定义

| 字段 | 值 |
|------|-----|
| 名称 | Portfolio Monitor Agent v2 |
| 触发 | 每日 15:30（收盘后）/ 21:00（海外市场）/ 人工指令 |
| 输入 | 持仓数据 + 行情数据 + 宏观数据 + 研报数据 |
| 输出 | 监控报告 + 预测分析 + 研报摘要 + 调仓结论 |
| 红线 | **不得自动交易**，仅监控+预测+分析+建议 |

---

## 二、R1-R4 规则引擎

### R1：单日止损

```yaml
rule: R1-单日止损
threshold: -30000  # 单日亏损 ≥ 3万
check_frequency: 实时(交易时段) + 收盘确认
action:
  - 关闭当日交易窗口
  - 推送通知：⚠️ R1触发 | 当日亏损: ¥XX | 建议：停止交易24h
  - 记录到日记：原因+情绪+反思
  - 24h冷静期后可恢复，仓位≤50%
exception:
  - 总仓位<30%时不触发
  - 系统性风险(熔断/全球暴跌)单独评估
```

### R2：周度止损

```yaml
rule: R2-周度止损
threshold: -50000  # 本周累计亏损 ≥ 5万
check_frequency: 每周五收盘后
action:
  - 当日减仓50%
  - 周末强制复盘
  - 生成亏损分析报告 → 04-Investor/亏损分析/
  - 下周仓位≤50%，直到连续2周盈利
exception:
  - 月度回撤>8% → 直接R4评估
```

### R3：行业集中度

```yaml
rule: R3-行业集中度
threshold: 0.30  # 单行业 >30%
check_frequency: 每日收盘后 + 每周一9:30
formula: "行业占比 = (单行业持仓市值) / (总持仓市值) × 100%"
action:
  - 推送提醒（不强制减仓）
  - 评估：临时波动 or 结构性问题
  - 结构性问题 → 2周内调整至≤30%
target_allocation:
  半导体: ≤20%
  科创50/AI: ≤20%
  高股息/低波动: ≥20%
  港股/海外: ≤10%
  现金/货基: ≥15%
```

### R4：跨市场敞口

```yaml
rule: R4-跨市场敞口
threshold: 0.10  # 海外 >10%
check_frequency: 每日 + 每周
formula: "海外占比 = (海外持仓市值) / (总持仓市值) × 100%"
action:
  - 评估海外资产与A股相关性
  - 高相关(>0.6) → 2周内减仓至5%
  - 中相关(0.3-0.6) → 减仓至8%
  - 低相关(<0.3) → 可保留但记录
trigger_events:
  - 美股大幅波动(>3%) → 立即评估
  - 港股单日>5% → 立即评估
  - 汇率大幅波动(>2%) → 立即评估
```

### R5：贵金属专项监控（新增）

```yaml
rule: R5-贵金属专项监控
assets:
  - 黄金ETF (华夏/华安)
  - 白银LOF (国投白银)
check_frequency: 每日收盘后 + 每日21:00（海外市场）
monitoring_points:
  - 国际金价/银价走势
  - 美联储利率预期
  - 美元指数
  - VIX恐慌指数
  - 实际收益率
thresholds:
  单日波动: ±2%  # 贵金属单日波动超过2%触发预警
  持仓占比: 40%  # 贵金属总持仓超过40%触发预警
  相关性: 0.8    # 黄金白银相关性超过0.8提示冗余
action:
  - 分析贵金属走势与宏观因素关联
  - 评估持仓合理性
  - 生成贵金属专项分析报告
```

---

## 三、贵金属专项分析模块（新增）

### 3.1 黄金ETF分析框架

```yaml
analysis_framework: gold_etf
data_points:
  - 国际金价 (XAU/USD)
  - 美元指数 (DXY)
  - 美国10年期国债收益率
  - VIX恐慌指数
  - 全球黄金ETF持仓量
  - 央行黄金储备变化
analysis_dimensions:
  - 宏观驱动: 利率、通胀、地缘政治
  - 技术面: 支撑位、阻力位、均线系统
  - 资金面: ETF资金流向、期货持仓
  - 情绪面: 市场情绪指标、散户vs机构
output: 黄金ETF专项分析报告
```

### 3.2 白银ETF分析框架

```yaml
analysis_framework: silver_etf
data_points:
  - 国际银价 (XAG/USD)
  - 金银比
  - 工业需求数据
  - 光伏行业景气度
  - 库存数据
analysis_dimensions:
  - 工业属性: 光伏、电子、新能源
  - 避险属性: 与黄金相关性
  - 供需关系: 矿产银、回收银
  - 技术面: 关键价位、波动率
output: 白银ETF专项分析报告
```

### 3.3 贵金属组合分析

```yaml
analysis_framework: precious_metals_portfolio
analysis_points:
  - 黄金白银配比合理性
  - 与整体组合的对冲效果
  - 宏观环境适配度
  - 风险收益比评估
output: 贵金属组合优化建议
```

---

## 四、预测分析模块（新增）

### 4.1 短期预测（1-5个交易日）

```yaml
prediction_horizon: short_term
methodology:
  - 技术面分析: 均线、MACD、RSI、布林带
  - 资金面分析: 北向资金、主力资金流向
  - 情绪面分析: 成交量、换手率、涨跌家数
output: 短期走势预测 + 关键价位
```

### 4.2 中期预测（1-4周）

```yaml
prediction_horizon: medium_term
methodology:
  - 宏观经济数据: PMI、CPI、社融
  - 政策面分析: 货币政策、产业政策
  - 行业景气度: 盈利预期、估值水平
output: 中期趋势判断 + 行业轮动建议
```

### 4.3 贵金属专项预测

```yaml
prediction_framework: precious_metals
factors:
  - 美联储利率路径
  - 通胀预期
  - 地缘政治风险
  - 美元走势
  - 实际收益率
output: 贵金属价格预测 + 持仓建议
```

---

## 五、研报收集与摘要模块（新增）

### 5.1 研报来源

```yaml
research_sources:
  宏观研究:
    - 中金公司
    - 中信证券
    - 海通证券
  行业研究:
    - 半导体行业
    - 贵金属行业
    - 新能源行业
  策略研究:
    - A股策略
    - 大类资产配置
```

### 5.2 研报摘要模板

```yaml
research_summary_template:
  structure:
    - 核心观点（1-2句话）
    - 关键数据支撑
    - 与持仓相关性
    - 操作建议
  format: |
    📄 研报标题: {{title}}
    🏢 研究机构: {{institution}}
    📅 发布日期: {{date}}
    💡 核心观点: {{key_point}}
    📊 关键数据: {{key_data}}
    🔗 与持仓关联: {{relevance}}
    💼 操作建议: {{suggestion}}
```

### 5.3 研报分类存储

```yaml
storage_structure:
  macro: 04-Investor/43-研究框架/宏观研究/
  industry: 04-Investor/43-研究框架/行业研究/
  strategy: 04-Investor/43-研究框架/策略研究/
  gold_silver: 04-Investor/43-研究框架/贵金属研究/
```

---

## 六、结论生成模块（新增）

### 6.1 每日结论模板

```yaml
daily_conclusion_template: |
  # 📊 每日投资结论 — {{date}}
  
  ## 市场环境总结
  {{market_summary}}
  
  ## 组合表现评估
  {{por

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
