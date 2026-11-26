---
name: uskill-investment-graham-safety-margin
description: "让investment graham safety margin变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-graham-safety-margin.md"
  original_id: "SKL-5120"
  version: "3.0.0"
  trust: untrusted
---

# investment graham safety margin

---
# Graham Safety Margin Valuation

> **角色**: 价值投资分析师 | **核心工具**: AI大模型, 财务数据API, Python计算脚本 | **效率目标**: 自动化安全边际计算，将估值分析时间缩短80%

## 🎯 目标

以**本杰明·格雷厄姆**的价值投资哲学为核心，构建系统化的[[安全边际计算框架]]，通过定量估值模型识别被低估的优质资产，为投资决策提供数据支撑。

**适用场景**:
1. **个股深度估值** — 对目标公司进行全面的安全边际计算，判断是否具备投资价值
2. **组合定期审视** — 对持仓标的定期重估安全边际，判断是否继续持有
3. **极端市场机会** — 市场恐慌期快速筛选安全边际充足的投资标的

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ticker` | string | ✅ | 股票代码或公司名称 |
| `financial_data` | object | ✅ | 财务数据：`{eps_5y, bvps, dividend_yield, current_price, debt_ratio}` |
| `required_margin` | number | ❌ | 要求的最低安全边际百分比，默认 33% |
| `growth_rate` | number | ❌ | 预期年化增长率（%），默认基于历史数据估算 |
| `discount_rate` | number | ❌ | 折现率，默认 10% |
| `years_projection` | int | ❌ | 预测年数，默认 10 |
| `industry` | string | ❌ | 所属行业，用于行业修正 |

## 📤 输出

```json
{
  "intrinsic_value": {
    "graham_number": "number — 格雷厄姆公式计算的内在价值",
    "dcf_value": "number — DCF折现计算的内在价值",
    "eps_multiplier_value": "number — 盈利倍数法内在价值",
    "weighted_intrinsic_value": "number — 加权综合内在价值"
  },
  "safety_margin": {
    "margin_pct": "number — 安全边际百分比",
    "margin_grade": "enum — substantial / adequate / thin / negative",
    "buy_signal": "boolean — 是否触发买入信号"
  },
  "quality_score": {
    "graham_criteria_met": "int — 满足格雷厄姆准则数量 (满分7)",
    "criteria_detail": [
      {"criterion": "string", "met": "boolean", "value": "string"}
    ],
    "overall_grade": "enum — A / B / C / D"
  },
  "risk_assessment": {
    "downside_scenario": "number — 悲观估值",
    "base_scenario": "number — 基准估值",
    "upside_scenario": "number — 乐观估值",
    "key_risks": ["string — 主要风险因素"]
  },
  "recommendation": {
    "action": "enum — strong_buy / buy / hold / sell",
    "position_size_pct": "number — 建议仓位占比",
    "entry_price_range": "string — 建议买入价格区间"
  }
}
```

## 📋 执行步骤

### 阶段一：数据采集与清洗

1. **获取财务数据** — 收集目标公司近5年核心财务指标：每股收益(EPS)、每股净资产(BVPS)、股息率、资产负债率、流动比率
2. **数据验证** — 检查数据完整性和一致性，标记异常值
3. **行业基准获取** — 获取同行业可比公司的估值倍数作为参考

### 阶段二：多模型估值计算

4. **格雷厄姆公式估值** — 使用经典公式：`Graham Number = √(22.5 × EPS × BVPS)`，适用于稳定盈利公司
5. **DCF折现估值** — 预测未来10年自由现金流，以要求折现率折现至现值，计算终值并折现
6. **盈利倍数法估值** — 使用 `EPS × (8.5 + 2g) × 4.4/Y` 公式，其中g为增长率，Y为AAA企业债收益率
7. **加权综合** — 根据数据可靠性和适用性对三种方法赋予权重，计算加权内在价值

### 阶段三：安全边际计算与质量评估

8. **计算安全边际** — `安全边际 = (内在价值 - 当前价格) / 内在价值 × 100%`
9. **格雷厄姆七项准则检验**:
   - ✅ 充足的公司规模（年营收 > 行业中位数）
   - ✅ 财务状况稳健（流动比率 > 2，长期负债 < 净营运资本）
   - ✅ 盈利稳定性（过去10年无亏损年份）
   - ✅ 持续分红记录（连续20年以上分红）
   - ✅ 盈利增长（过去10年EPS增长 ≥ 33%）
   - ✅ 合理市盈率（PE < 15）
   - ✅ 合理市净率（PB < 1.5 或 PE × PB < 22.5）
10. **综合质量评分** — 满足准则数量映射为A/B/C/D等级

### 阶段四：情景分析与决策输出

11. **三情景分析** — 分别计算悲观/基准/乐观三种情景下的估值范围
12. **生成投资建议** — 综合安全边际、质量评分和风险评估，给出明确的操作建议
13. **记录决策依据** — 保存完整的计算过程和假设条件

## ✅ 检查清单

- [ ] 财务数据是否覆盖至少5年历史
- [ ] 三种估值方法是否均已计算完成
- [ ] 格雷厄姆七项准则是否逐项检验
- [ ] 安全边际是否达到预设最低要求（默认33%）
- [ ] 三情景分析是否合理覆盖极端情况
- [ ] 所有假设条件是否已明确记录
- [ ] 同行业可比估值是否已纳入参考

## ⚠️ 常见陷阱

| 陷阱 | 说明 | 规避方法 |
|------|------|---------|
| 机械套用公式 | 格雷厄姆公式适用于稳定盈利企业，对高成长或周期股失真 | 结合行业特征选择估值方法权重 |
| 忽略资产负债表质量 | 表面EPS增长但负债率急剧攀升 | 重点审查债务结构和偿债能力 |
| 历史数据外推谬误 | 过去的增长率不代表未来 | 使用保守增长率，做敏感性分析 |
| 锚定效应 | 被当前价格锚定，低估内在价值波动区间 | 严格按模型计算，参考多时间维度数据 |
| 忽略管理层质量 | 财务数据好看但管理层诚信存疑 | 纳入定性评估因素 |
| 安全边际不足仍入场 | "差不多够了"心态 | 严格执行最低安全边际要求，宁可错过 |

## 🔗 关联

- **相关技能**: [[SOP-09-投资人-投资机会分析]], 行业轮动分析, 定投策略优化
- **推荐工具**: Python + akshare/tushare, Excel估值模板
- **经典著作**: 《聪明的投资者》《证券分析》— 本杰明·格雷厄姆


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

## 🛡️ Three-Tier Boundaries `[

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
