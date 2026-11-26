---
name: uskill-cognition-cognitive-monitor-intraday-stock-market
description: "让cognitive monitor intraday stock market变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-monitor-intraday-stock-market.md"
  original_id: "SKL-6839"
  version: "3.0.0"
  trust: untrusted
---

# cognitive monitor intraday stock market

# Monitor Intraday Stock Market

## 🎯 目标
> 建立标准化的 A 股日内盯盘流程，通过四个阶段（盘前定调、集合竞价、开盘博弈、盘中观察）系统化捕捉短线情绪和主流热点，将盯盘效率提升 50%，避免情绪化交易。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `watchlist` | array[string] | ✅ | 自选股列表（股票代码或名称） |
| `trading_style` | enum | ❌ | `scalping`（超短线）/ `swing`（波段）/ `mixed`，默认 `mixed` |
| `focus_sectors` | array[string] | ❌ | 重点关注的板块/概念，如 `["AI", "低空经济"]` |
| `max_position_pct` | int | ❌ | 单只股票最大仓位占比（%），默认 20 |
| `risk_tolerance` | enum | ❌ | `aggressive` / `moderate` / `conservative`，默认 `moderate` |

## 📤 输出

```json
{
  "pre_market_briefing": {
    "overnight_sentiment": "bullish | bearish | neutral",
    "a50_futures": "string — A50期指涨跌幅",
    "us_chinese_stocks": "string — 中概股表现",
    "fx_rate_usdcnh": "string — 离岸人民币汇率",
    "key_news": ["string — 重要消息摘要"],
    "predicted_open": "gap_up | flat | gap_down"
  },
  "auction_analysis": {
    "fake_orders_915_920": ["string — 假单诱多/诱空观察"],
    "real_pricing_920_925": {
      "nuclear_buttons": ["string — 被核按钮的高标股"],
      "surprise_high_open": ["string — 超预期高开个股"],
      "top_auction_volume": ["string — 竞价量能前排"]
    },
    "market_mood": "extreme_fear | fear | neutral | greed | extreme_greed"
  },
  "opening_session": {
    "leading_sectors": [{"name": "string", "change_pct": "float", "volume_ratio": "float"}],
    "index_lines": {"white_above_yellow": "boolean — 权重行情vs题材行情"},
    "actionable_stocks": [
      {"code": "string", "name": "string", "signal": "buy | watch | avoid", "reason": "string"}
    ],
    "board_status": {"limit_up_count": "int", "limit_down_count": "int", "seal_rate": "float"}
  },
  "midday_observation": {
    "advance_decline": {"advancing": "int", "declining": "int", "trend": "improving | deteriorating | flat"},
    "mainline_confirmed": "boolean",
    "holding_decisions": [{"code": "string", "action": "hold | sell | reduce", "reason": "string"}],
    "afternoon_outlook": "active | garbage_time | cautious"
  },
  "daily_summary": {
    "pnl_estimate": "float",
    "lessons": ["string — 今日复盘要点"],
    "tomorrow_watchlist": ["string — 明日关注标的"]
  }
}
```

## 📋 执行步骤

### 阶段一：盘前宏观与情绪定调（9:00 - 9:15）

1. **查看外围市场** — 获取隔夜美股（尤其纳斯达克中国金龙指数）、A50期指实时涨跌、离岸人民币汇率
2. **扫描消息面** — 查看 7x24 快讯，确认昨晚热点是否有澄清公告或进一步利好
3. **预判开盘方向** — 综合外围和消息面，判断今日大盘高开/平开/低开概率

### 阶段二：集合竞价——最关键的10分钟（9:15 - 9:25）

4. **9:15-9:20 观察假单** — 此时段可撤单，涨停/跌停多为诱多/诱空，只看不动
5. **9:20-9:25 捕捉真金白银** — 紧盯自选股和涨幅榜，关注：
   - **核按钮**：昨日高标股被按跌停或深水开盘 → 情绪极差，管住手
   - **超预期**：利好+爆量高开 → 可能是今日黑马
   - **竞价涨幅排行**：搜索"竞价涨幅"，看前排对应板块
6. **记录竞价结论** — 将观察到的信号写入当日交易日志

### 阶段三：开盘半小时——黄金博弈期（9:30 - 10:00）

7. **9:30-9:35 情绪宣泄期** — 不急买入，观察大盘黄白线：
   - 白线在上 = 权重行情，赚指数不赚钱
   - 黄线在上 = 题材活跃，赚钱效应好
8. **确认主线板块** — 按概念板块涨幅排序，识别第一时间冲上来的板块
9. **9:35-10:00 卡位与确立** — 对目标股与龙头股叠加比较：
   - 龙头涨它不跟、龙头跌它先跌 → 果断放弃
   - 量比 > 3 且股价上涨 → 主力资金介入明显
   - 前排频繁炸板 → 分歧大，今日难做

### 阶段四：盘中观察与决策（10:00 - 11:30）

10. **10:00-10:30 回落与反包** — 关注涨跌家数：
    - 上涨家数 < 1000 且持续减少 → 普跌行情，空仓或减仓
    - 早盘冲高回落股能否在分时均线上方企稳 → 跌破均线无法收回 = 走弱
11. **11:00-11:30 上午收官** — 关注主力资金和北向资金：
    - 收盘前突袭拉升多为"骗线"，除非有重大利好否则不追
    - 上午无明确主线 → 下午大概率垃圾时间，管住手
12. **生成半日总结** — 汇总上午行情，记录关键信号和持仓决策

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 核按钮导致情绪崩盘 | 全面空仓，不接飞刀，等待情绪修复信号 |
| 竞价阶段无法获取数据 | 切换备用行情源（东方财富/雪球），延迟30秒决策 |
| 主线板块频繁切换 | 说明市场无共识，降低仓位至 30% 以下 |
| 量比数据异常（如 >10） | 可能为消息驱动的脉冲，等回调确认后再介入 |
| 个股触及止损线 | 严格执行止损，不抱侥幸心理，记录止损原因 |

## ✅ 自检清单

- [ ] 盘前是否已完成外围市场和消息面扫描
- [ ] 集合竞价阶段是否区分了假单（9:15-9:20）和真单（9:20-9:25）
- [ ] 开盘30分钟内是否确认了主线板块
- [ ] 每笔交易是否都有明确的买入/卖出理由记录
- [ ] 是否严格执行了止损纪律
- [ ] 是否避免了"骗线高发期"（11:00-11:30）的冲动追高
- [ ] 半日总结是否已生成并归档


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
- [ ] 未

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
