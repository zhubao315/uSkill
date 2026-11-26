---
name: uskill-investment-industry-rotation-analysis
description: "让investment industry rotation analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S6-投资与财务/uSkill-investment-industry-rotation-analysis.md"
  original_id: "SKL-5122"
  version: "3.0.0"
  trust: untrusted
---

# investment industry rotation analysis

# Industry Rotation Analysis

> **角色**: 宏观策略分析师 | **核心工具**: AI大模型, 宏观数据API, 行业指数数据 | **效率目标**: 系统化识别行业轮动信号，提升行业配置效率

## 🎯 目标

基于**美林时钟**和**行业生命周期理论**，构建系统化的行业轮动分析框架，识别经济周期不同阶段的最优行业配置，捕捉行业切换的领先信号。

**适用场景**:
1. **大类资产配置** — 根据宏观经济阶段调整行业权重
2. **行业ETF轮动** — 在不同行业ETF之间进行轮动操作
3. **投资组合再平衡** — 定期审视行业暴露，优化组合结构

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `macro_indicators` | object | ✅ | 宏观指标：`{gdp_growth, cpi, pmi, m2_growth, credit_impulse, yield_curve}` |
| `industry_data` | object | ✅ | 行业数据：各行业近期表现、估值、资金流向 |
| `portfolio_current` | object | ❌ | 当前持仓的行业分布 |
| `lookback_period` | enum | ❌ | `1m` / `3m` / `6m` / `1y`，默认 `3m` |
| `market` | enum | ❌ | `A_share` / `US` / `global`，默认 `A_share` |

## 📤 输出

```json
{
  "cycle_assessment": {
    "current_phase": "enum — recovery / expansion / overheating / stagflation / recession / early_recovery",
    "phase_confidence": "number — 置信度 (0-1)",
    "transition_signal": "string — 阶段转换信号描述",
    "key_indicators": [
      {"indicator": "string", "value": "number", "trend": "string", "signal": "string"}
    ]
  },
  "industry_ranking": [
    {
      "industry": "string",
      "score": "number — 综合评分 (0-100)",
      "momentum_score": "number — 动量评分",
      "valuation_score": "number — 估值评分",
      "fund_flow_score": "number — 资金流向评分",
      "cycle_fit_score": "number — 周期匹配评分",
      "recommendation": "enum — overweight / neutral / underweight"
    }
  ],
  "rotation_signals": {
    "active_signals": [
      {"from_industry": "string", "to_industry": "string", "strength": "string", "reason": "string"}
    ],
    "watch_list": ["string — 值得关注的潜在轮动信号"]
  },
  "action_plan": {
    "suggested_allocation": [
      {"industry": "string", "weight_pct": "number", "instruments": ["string"]}
    ],
    "execution_timeline": "string — 建议执行节奏",
    "risk_hedges": ["string — 风险对冲建议"]
  }
}
```

## 📋 执行步骤

### 阶段一：宏观经济周期定位

1. **收集宏观数据** — 获取GDP增速、CPI/PPI、PMI、M2增速、信贷脉冲、收益率曲线等核心指标
2. **判断经济周期阶段** — 基于美林时钟框架：
   - **复苏期**: 经济上行 + 通胀下行 → 股票 > 债券 > 商品 > 现金
   - **过热期**: 经济上行 + 通胀上行 → 商品 > 股票 > 现金 > 债券
   - **滞胀期**: 经济下行 + 通胀上行 → 现金 > 商品 > 债券 > 股票
   - **衰退期**: 经济下行 + 通胀下行 → 债券 > 现金 > 股票 > 商品
3. **交叉验证** — 使用多指标交叉确认周期判断，评估置信度

### 阶段二：行业多维评分

4. **动量分析** — 计算各行业近1/3/6个月涨跌幅，识别趋势
5. **估值分析** — 计算各行业PE/PB百分位，识别估值洼地
6. **资金流向分析** — 跟踪北向资金、主力资金、ETF份额变化
7. **周期匹配度** — 根据当前经济周期阶段，评估各行业的历史表现规律
8. **综合评分** — 加权汇总各维度分数，生成行业排名

### 阶段三：轮动信号识别

9. **强弱转换信号** — 监控行业相对强弱(RS)的变化，识别领先/落后切换
10. **政策催化信号** — 跟踪产业政策、监管变化对行业的影响
11. **技术面确认** — 使用行业指数的均线系统、MACD等技术指标确认趋势

### 阶段四：配置建议与执行

12. **生成配置方案** — 基于行业评分和轮动信号，建议行业配置比例
13. **工具映射** — 将行业配置映射到具体ETF/基金标的
14. **设定监控指标** — 建立轮动信号监控看板，定期更新

## ✅ 检查清单

- [ ] 宏观经济周期判断是否有多指标交叉验证
- [ ] 行业评分是否覆盖动量、估值、资金、周期四个维度
- [ ] 轮动信号是否同时包含技术和基本面依据
- [ ] 配置建议是否与风险偏好匹配
- [ ] 是否设定了轮动信号失效的退出条件
- [ ] 交易成本是否纳入策略考量

## ⚠️ 常见陷阱

| 陷阱 | 说明 | 规避方法 |
|------|------|---------|
| 机械套用美林时钟 | 中国经济周期有独特性，不能简单照搬 | 加入中国特色指标（社融、专项债等） |
| 追热点行业 | 行业已大涨才追入 | 坚持逆向思维，在底部区域布局 |
| 频繁轮动 | 每周都想调仓 | 设定最小持仓期（至少1个季度） |
| 忽略行业基本面 | 只看技术信号不看产业逻辑 | 技术信号必须有基本面支撑 |
| 单因子依赖 | 只看动量或只看估值 | 多因子综合评分，避免单一偏差 |

## 🔗 关联

- **相关技能**: 安全边际计算, 定投策略优化, 债券配置策略
- **推荐工具**: Wind/Choice金融终端, 申万行业指数
- **经典框架**: 美林投资时钟, 行业生命周期理论


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---
---
**相关笔记**：[[格雷厄姆安全边际分析]] [[定投策略优

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
