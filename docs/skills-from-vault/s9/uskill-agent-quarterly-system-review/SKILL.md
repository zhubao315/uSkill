---
name: uskill-agent-quarterly-system-review
description: "让季度收官从'写报告'变成对北极星指标的系统化体检：达成率、风险、缺口一次性看清，而非堆砌流水账。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-quarterly-system-review.md"
  original_id: "SKL-7122"
  version: "3.0.0"
  trust: untrusted
---

# 季度系统评估

# 季度系统评估

description: |
  当用户需要产出季度系统评估 / 收官报告 / 北极星指标体检时使用此 Skill。
  触发词包括：'季度评估'、'Q收官'、'季度复盘'、'系统评估'、'指标体检'。
  即使用户只说'这个季度怎么样'，只要意图是评估多维度系统表现，也应使用此 Skill。
  不适用于单篇日记复盘或单一项目周报。

---

## 🎯 目标

> 基于 uLife OS 北极星指标体系，对季度内认知资产（uSkill/uWise/uRead）、生物算力（月跑量/体脂率/静息心率）、驾驭效能（Agent占比/月收益）进行结构化体检，输出达成率、风险分级与下季度行动项。

**适用场景**：Q1-Q4 收官、半年度复盘、年度校准、北极星指标追踪。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `north_star` | `array` | ✅ | 本季北极星指标（指标/目标/当前值） |
| `quarter` | `enum` | ✅ | Q1/Q2/Q3/Q4 |
| `prior_actions` | `array` | ❌ | 上季行动项及完成状态 |
| `risk_signals` | `array` | ❌ | 已识别的风险信号 |

---

## 📤 输出

```json
{
  "achievement_rate": "number",
  "metric_table": [{"dim": "string", "target": "number", "actual": "number", "rate": "number", "status": "🟢|🟡|🔴"}],
  "risks": [{"level": "P0|P1|P2", "desc": "string", "deadline": "string"}],
  "next_quarter_actions": [{"action": "string", "owner": "string", "due": "string"}]
}
```

---

## 🔄 执行流程

```
1. [指标拉取] → 读取 north_star 逐项比对
    → 判断条件：指标方向（higher=越高越好 / lower=越低越好）？
      → higher：实际值 ≥ 目标 → 🟢；目标×0.7≤实际<目标 → 🟡；实际<目标×0.7 → 🔴
      → lower：实际值 ≤ 目标 → 🟢；目标<实际≤目标×1.2 → 🟡；实际>目标×1.2 → 🔴
    → rate 计算（保留整数）：higher = 实际/目标×100；lower = 目标/实际×100
    → achievement_rate = 各指标 rate 的算术平均（不封顶，保留超额信号）

2. [综合达成率] → 加权计算并识别被掩盖短板
   → 规则：认知资产易超额，须单独暴露生物算力/驾驭效能
   → 判断条件：认知资产达成率 >300% 且某生物指标 🔴？
     → 是：综合达成率下调注释"被认知资产掩盖"
     → 否：直接取均值

3. [风险分级] → 将 risk_signals 归 P0/P1/P2
   → P0：紧急且影响目标达成（如风控缺失、体脂超标）
   → P1：重要偏差（Agent占比不足、收益未达标）
   → P2：轻微波动
   → 判断条件：存在 🔴 且无可执行行动？
     → 是：强制生成 P0 行动项 + 截止日
     → 否：进入下季规划

4. [行动项生成] → 绑定 owner + due
   → 规则：每条行动必须可验证、有期限
   → 判断条件：上季 prior_actions 有未完成？
     → 是：继承并升级优先级
     → 否：基于本季缺口新建

5. [输出报告] → 达成率 + 指标表 + 风险 + 行动项
```

---

## 📝 Prompt 模板

### 标准评估 Prompt

```
你是季度系统评估 Agent。请生成本季度收官体检。

【季度】{quarter}
【北极星指标】{north_star}
【上季行动】{prior_actions}
【风险信号】{risk_signals}

【评估规则】
1. 逐项比对：≥目标🟢，≥70%🟡，<70%🔴
2. 认知资产超额时单独暴露生物算力/驾驭效能短板
3. 风险按 P0/P1/P2 分级，🔴 必须生成带截止日的行动项
4. 行动项绑定负责人与期限

【输出格式】
按标准 JSON 输出 achievement_rate / metric_table / risks / next_quarter_actions。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 指标数据缺失 | 基于可用数据评估 | 标注"部分口径缺失" |
| 目标值未设定 | 用历史均值作基准 | 提示下季先定目标 |
| 风险无负责人 | 默认指派循环官 | 标注"待认领" |
| 跨季口径变化 | 注明不可比 | 仅作趋势参考 |

---

## ✅ 质量自检

- [ ] 所有北极星指标均进入 metric_table
- [ ] 综合达成率含"被掩盖"注释（如适用）
- [ ] 每个 🔴 都有 P0 行动项 + 截止日
- [ ] 行动项含 owner 与 due
- [ ] 结论与原始数据一致可追溯

---

## 💡 使用示例

### 示例 1：Q2 收官（基于真实数据）

**输入**：
```json
{
  "quarter": "Q2",
  "north_star": [
    {"dim": "uSkill", "target": 30, "actual": 229},
    {"dim": "月跑量", "target": 200, "actual": 189.96},
    {"dim": "体脂率", "target": 19, "actual": 20.6},
    {"dim": "Agent占比", "target": 60, "actual": 50}
  ]
}
```

**输出**：
```json
{
  "achievement_rate": 258,
  "metric_table": [
    {"dim": "uSkill", "target": 30, "actual": 229, "rate": 763, "status": "🟢"},
    {"dim": "月跑量", "target": 200, "actual": 189.96, "rate": 95, "status": "🟡"},
    {"dim": "体脂率", "target": 19, "actual": 20.6, "rate": 92, "status": "🔴"},
    {"dim": "Agent占比", "target": 60, "actual": 50, "rate": 83, "status": "🟡"}
  ],
  "risks": [{"level": "P0", "desc": "体脂率20.6%超目标1.6%", "deadline": "Q3-W2测量验收"}],
  "next_quarter_actions": [{"action": "训练+饮食双管下降体脂", "owner": "艺术家", "due": "Q3-W2"}]
}
```

### 示例 2：被掩盖短板（边界）

**输入**：
```json
{
  "quarter": "Q2",
  "north_star": [
    {"dim": "uWise", "target": 1000, "actual": 2506},
    {"dim": "月收益", "target": 8, "actual": 6.16}
  ]
}
```

**输出**：
```json
{
  "achievement_rate": 164,
  "notes": ["认知资产超额掩盖驾驭效能短板：月收益仅77%"]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | Q2 正常收官 | 指标表 + 综合达成率 |
| 2 | 体脂🔴 | 生成 P0 行动项 + 截止日 |
| 3 | 认知超额掩盖 | 标注被掩盖短板 |
| 4 | 指标缺失 | 部分口径降级评估 |
| 5 | 上季未完 | 继承并升级优先级 |
| 6 | 风险无负责人 | 默认指派+待认领 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得美化 🔴 指标为达标
2. 财务/健康结论不得替代专业建议
3. 不得删除或篡改原始指标数据

**软性约束（建议遵守）**：
1. 优先用可量化口径，少用主观描述
2. 行动项可验证、有期限

**人工兜底点**：
- 当指标涉及重大财务/健康决策时暂停等待确认
- 当数据可信度

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
