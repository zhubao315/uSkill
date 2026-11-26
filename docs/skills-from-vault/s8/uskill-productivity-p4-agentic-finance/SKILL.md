---
name: uskill-productivity-p4-agentic-finance
description: "让productivity p4 agentic finance变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-p4-agentic-finance.md"
  original_id: "SKL-5039"
  version: "3.0.0"
  trust: untrusted
---

# productivity p4 agentic finance

# P4 Agentic Finance - Adversarial Investment Research System

## 🎯 目标
> 对抗性投研数字孪生系统：基于本地4090集群部署MoA架构，4个Agent（激进派/保守派/裁判官/风控官）对抗辩论，100次虚拟辩论产出"幸存者策略"，目标年化收益18%+，最大回撤<15%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `investment_target` | object | ✅ | `{ticker: "string", market: "A-share" | "crypto", name: "string"}` — 投资标的 |
| `analysis_type` | enum | ✅ | `quick_scan`（快速扫描）/ `full_debate`（完整辩论）/ `risk_check`（风控审查） |
| `hardware_config` | object | ❌ | `{gpu_count: "number", gpu_model: "string", vram_gb: "number"}` — 硬件配置，默认4090集群 |
| `model_config` | object | ❌ | `{aggressive: "string", conservative: "string", referee: "string", risk_officer: "string"}` — 各Agent模型 |
| `market_data` | object | ❌ | `{prices: [], fundamentals: {}, news: []}` — 行情/基本面/新闻数据 |
| `portfolio_context` | object | ❌ | `{current_positions: [], total_capital: "number", max_drawdown: "number"}` — 当前持仓上下文 |
| `custom_constraints` | object | ❌ | `{max_single_position: "number", stop_loss: "number", holding_period: "string"}` — 自定义约束 |

## 📤 输出

```json
{
  "agentic_finance_report": {
    "debate_summary": {
      "target": "string — 标的名称/代码",
      "debate_rounds": "number — 辩论轮次",
      "convergence": "boolean — 是否收敛",
      "total_duration_ms": "number — 总耗时"
    },
    "agent_a_aggressive": {
      "stance": "buy | sell | hold",
      "confidence": "number (0-100)",
      "technical_signals": {
        "rsi": "number",
        "macd": "string",
        "bollinger": "string",
        "volume_anomaly": "boolean"
      },
      "argument": "string — 核心论证",
      "target_price": "number",
      "stop_loss": "number"
    },
    "agent_b_conservative": {
      "stance": "buy | sell | hold",
      "confidence": "number (0-100)",
      "valuation_metrics": {
        "pe_percentile": "number",
        "pb_percentile": "number",
        "roe": "number",
        "moat_score": "string"
      },
      "argument": "string — 核心论证",
      "safety_margin": "string — 安全边际分析"
    },
    "agent_c_referee": {
      "final_verdict": "buy | sell | hold | wait",
      "overall_confidence": "number (0-100)",
      "reasoning": "string — 综合判断逻辑",
      "counterfactual": {
        "if_a_wrong": "string — 如果激进派错了，原因可能是...",
        "if_b_wrong": "string — 如果保守派错了，原因可能是..."
      },
      "recommended_position_pct": "number (0-100)",
      "recommended_holding_days": "number"
    },
    "agent_d_risk_officer": {
      "veto": "boolean — 是否一票否决",
      "risk_level": "low | medium | high | critical",
      "black_swan_flags": ["string — 黑天鹅风险信号"],
      "drawdown_status": {
        "current_drawdown_pct": "number",
        "max_allowed_pct": "number",
        "breach": "boolean"
      },
      "action": "approve | veto | reduce_position",
      "alert_message": "string | null"
    },
    "final_decision": {
      "recommendation": "buy | sell | hold | wait | veto",
      "position_size_pct": "number",
      "entry_price_range": {"low": "number", "high": "number"},
      "stop_loss": "number",
      "take_profit": "number",
      "holding_period": "string",
      "confidence_score": "number (0-100)",
      "human_override_needed": "boolean"
    },
    "backtest_context": {
      "similar_scenarios_count": "number",
      "historical_win_rate": "number",
      "avg_return": "number",
      "max_drawdown_in_similar": "number"
    }
  }
}
```

## 📋 执行步骤

### Step 1: 环境准备与数据接入 (Setup & Data Pipeline)
1. **硬件确认** — 验证4090集群状态，确保GPU可用显存充足
   - 检查项：NVIDIA驱动版本、CUDA版本、vLLM/Ollama服务状态
2. **模型加载** — 加载4个Agent对应模型
   - Agent A（激进派）: Qwen2-7B — 快速决策，动量捕捉
   - Agent B（保守派）: Llama3-8B — 稳健分析，价值评估
   - Agent C（裁判官）: ChatGLM4-9B — 综合判断，Reflection机制
   - Agent D（风控官）: Qwen2-72B（量化版）— 深度风控分析
3. **数据获取** — 接入实时/历史行情数据
   - A股：Tushare / AKShare
   - 加密货币：Binance API
   - 新闻：雪球、东方财富、Twitter API
   - 质量检查：数据完整性>99%，延迟<1s

### Step 2: Agent对抗辩论 (Multi-Agent Debate)
1. **辩论启动** — 将标的信息和市场数据广播给4个Agent
2. **第一轮：独立分析**
   - Agent A 分析技术面（RSI/MACD/布林带/成交量突变/资金流向）
   - Agent B 分析基本面（PE/PB估值分位数/现

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
