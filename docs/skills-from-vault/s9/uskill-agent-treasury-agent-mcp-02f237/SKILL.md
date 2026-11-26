---
name: uskill-agent-treasury-agent-mcp-02f237
description: "让uSkill-Treasury Agent MCP 接入与回测系统变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-treasury-agent-mcp-接入与回测系统.md"
  original_id: "SKL-7012"
  version: "3.0.0"
  trust: untrusted
---

# uSkill-Treasury Agent MCP 接入与回测系统

# 💰 Treasury Agent MCP 接入与回测系统

> **Q3 目标**：MCP 接入券商 API + 调仓策略回测 + 风控闭环验证
> **时间跨度**：2026-07-01 → 2026-09-30
> **关联**：[[∑ 投资条件反射规则]] · [[循环工程-财务智能体红队对抗配置]] · [[2026-Q3-OKR-草稿]]

---

## 一、系统架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Treasury Agent System                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Layer 1: Data Acquisition                 │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ MCP      │  │ 券商 API │  │ 手动录入 │              │   │
│  │  │ Protocol │  │ (模拟)   │  │ (降级)   │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                 Layer 2: Risk Control Engine              │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ CB-1     │  │ CB-2     │  │ CB-3     │              │   │
│  │  │ 集中度   │  │ 现金地板 │  │ 个股止损 │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ R4       │  │ R5       │  │ R6       │              │   │
│  │  │ 回撤控制 │  │ 波动率   │  │ 相关性   │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                 Layer 3: Backtest Engine                  │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ 策略回测 │  │ 历史数据 │  │ 绩效评估 │              │   │
│  │  │ Engine   │  │ Handler  │  │ Metrics  │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│  ┌────────────────────────▼────────────────────────────────┐   │
│  │                 Layer 4: Reporting & Alerts               │   │
│  │  日报 │ 周报 │ 月报 │ OVP 季报 │ IM 推送 │ 邮件       │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 二、Phase 1：MCP API 原型（7/1 → 8/15）

### 目标
模拟券商 API 跑通，自动对账误差 <1%。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T1.1 | MCP 券商 API 接口定义 | `treasury_mcp_schema.yaml` | 7/15 | — |
| T1.2 | 模拟数据生成器 | `treasury_mock_data.py` | 7/25 | T1.1 |
| T1.3 | 持仓同步模块 | `treasury_sync.py` | 8/1 | T1.2 |
| T1.4 | 对账引擎 | `treasury_reconcile.py` | 8/10 | T1.3 |
| T1.5 | 端到端测试 | 测试报告 | 8/15 | T1.4 |

### MCP 接口定义

```yaml
# Treasury MCP Server - Tool Definitions
tools:
  - name: "treasury_sync_positions"
    description: "同步持仓数据"
    input:
      source: "string"          # mock | manual | broker_api
      date: "string"            # YYYY-MM-DD
    output:
      positions: "array"        # 持仓列表
      total_value: "number"     # 总市值
      cash_balance: "number"    # 现金余额

  - name: "treasury_reconcile"
    description: "对账：比较本地记录与券商数据"
    input:
      local_records: "array"    # 本地持仓
      broker_data: "array"      # 券商数据
    output:
      match_rate: "number"      # 匹配率
      discrepancies: "array"    # 差异项

  - name: "treasury_calculate_risk"
    description: "计算风控指标"
    input:
      positions: "array"
      total_value: "number"
    output:
      cb1_tech_concentration: "number"  # 科技集中度
      cb2_cash_floor: "number"          # 现金占比
      cb3_stock_loss: "array"           # 个股止损状态
      risk_level: "string"              # green|y

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
