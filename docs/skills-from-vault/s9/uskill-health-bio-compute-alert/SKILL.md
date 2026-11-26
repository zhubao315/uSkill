---
name: uskill-health-bio-compute-alert
description: "把身体当作一台算力设备来监控，在'生物算力'透支前预警，防止过劳、受伤与倦怠。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-health-bio-compute-alert.md"
  original_id: "SKL-7099"
  version: "3.0.0"
  trust: untrusted
---

# 生物算力预警

description: |
  当用户需要监控自身精力、睡眠、训练负荷与恢复状态，防止过度透支导致受伤或倦怠时使用此 Skill。
  触发词包括：'生物算力'、'我今天好累'、'训练过度'、'恢复不过来'、'精力预警'、'该休息吗'。
  当用户连续高强度工作/训练、睡眠下降、静息心率升高、情绪低落时，即使未说"预警"，也应使用此 Skill。
  遇到"要不要加练""还能不能扛"类需求优先使用，而非让用户硬撑。

---

# 🔋 生物算力预警 v1.0（Gen3 首发）

## 🎯 目标

> 把人体（精力、睡眠、恢复、训练负荷）当作一台算力设备来监控：当"生物算力"余额低于安全线时提前预警，把过劳、受伤、倦怠消灭在事前。

**核心隐喻**：身体像一台服务器，睡眠是充电、训练/工作是负载、静息心率(HRv/HR)与主观疲劳是利用率指标。算力不是无限的，透支会累积"技术债"（损伤、免疫下降、决策退化）。

**适用场景**：耐力训练周期管理（参考[[全马破330科学训练计划]]）、高强度工作周、减脂/增肌负荷调控、长期熬夜后的恢复评估。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `sleep_hours` | `number` | ✅ | 近7日平均睡眠时长 |
| `rhr_trend` | `array` | ❌ | 静息心率序列（升高=恢复不足） |
| `train_load` | `number` | ❌ | 当周训练负荷（TSS/主观分） |
| `subjective_fatigue` | `enum` | ❌ | 1–10 主观疲劳 |
| `stress_days` | `number` | ❌ | 连续高强度天数 |

---

## 📤 输出

```json
{
  "battery_pct": "number(0-100)",
  "level": "安全|警戒|透支",
  "signals": [{"metric": "string", "value": "string", "verdict": "正常|偏高|危险"}],
  "action": ["string"],
  "recover_plan": ["string"]
}
```

---

## 🔄 执行流程

```
1. [算力折算] → 综合睡眠/负荷/主观疲劳折算 battery_pct
   → 判断条件：sleep_hours < 6 且 train_load 高？
     → 是：直接判"警戒"并进入信号核查
     → 否：按加权公式估算

2. [生理信号核查] → 看 rhr_trend 是否连续上升
   → 判断条件：静息心率较基线升 ≥5bpm 且持续3天？
     → 是：标记"恢复不足"硬信号，level 至少警戒
     → 否：看主观

3. [主观校准] → 用 subjective_fatigue 修正
   → 判断条件：fatigue ≥ 8 且 stress_days ≥ 5？
     → 是：强制"透支"，无视单日指标好转
     → 否：按综合值定级

4. [负荷决策] → 对训练/工作安排给增减量建议
   → 判断条件：level == 透支？
     → 是：建议减量50%或完全休息，禁止加练
     → 否：level==警戒 → 维持并加恢复；安全 → 可正常/微增

5. [输出预警] → 给 battery_pct + 行动 + 恢复方案
```

---

## 📝 Prompt 模板

### 标准预警 Prompt

```
你是生物算力监控 Agent。请把人体当作算力设备评估透支风险。

【睡眠】{sleep_hours} 小时/日均
【静息心率序列】{rhr_trend}
【训练负荷】{train_load}
【主观疲劳】{subjective_fatigue}/10
【连续高强度天数】{stress_days}

【规则】
1. 睡眠<6h且高负荷 → 至少警戒
2. 静息心率较基线升≥5bpm持续3天 → 恢复不足硬信号
3. 疲劳≥8且连续高强度≥5天 → 强制透支
4. 透支禁止加练，建议减量50%或休息
5. 输出可执行的恢复方案（睡眠/营养/减量）

【输出格式】严格按 JSON：battery_pct / level / signals / action / recover_plan
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 数据缺失（无心率） | 仅用睡眠+主观 | 标注"精度降低" |
| 单日异常波动 | 看3日趋势不孤立判断 | 提示复测 |
| 用户拒绝休息 | 给最低风险替代（活性恢复） | 标注"自负风险" |
| 疑似疾病信号 | 建议就医而非训练 | 转医疗兜底 |

---

## ✅ 质量自检

- [ ] battery_pct 与 level 逻辑一致
- [ ] 每条信号有数值依据
- [ ] 透支时明确禁止加练
- [ ] 恢复方案具体到动作

---

## 💡 使用示例

### 示例 1：马拉松备战透支

**输入**：
```json
{
  "sleep_hours": 5.5,
  "rhr_trend": [52, 54, 57, 58],
  "train_load": 620,
  "subjective_fatigue": 8,
  "stress_days": 6
}
```

**输出**：
```json
{
  "battery_pct": 28,
  "level": "透支",
  "signals": [
    {"metric": "静息心率", "value": "升6bpm/4天", "verdict": "危险"},
    {"metric": "睡眠", "value": "5.5h", "verdict": "偏高"}
  ],
  "action": ["今日禁止强度课", "周跑量削减50%", "安排1天完全休息"],
  "recover_plan": ["23:00前睡足8h", "补充碳水+蛋白", "次日30min轻松慢跑或拉伸"]
}
```

### 示例 2：边界——误判防御

**输入**：`sleep_hours=7, rhr平稳, fatigue=4, stress_days=2`

**输出**：`battery_pct=82, level=安全，可正常训练，提示保持睡眠。`

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 标准透支 | level=透支+禁练 |
| 2 | 数据缺失 | 降级精度标注 |
| 3 | 单日波动 | 看趋势不误判 |
| 4 | 拒绝休息 | 活性恢复替代 |
| 5 | 疑似疾病 | 转医疗兜底 |
| 6 | 健康状态 | 安全可训练 |

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 本 Skill 仅作健康参考，不构成医疗诊断
2. 出现疾病/胸痛/眩晕等症状**必须**建议就医
3. 不得鼓励带伤/带病加练

**软性约束（建议遵守）**：
1. 阈值应随个人基线个性化，避免一刀切
2. 建议具体到休息/减量/营养，而非"注意身体"

**人工兜底点**：
- 涉及伤病/疾病信号时**必须**转医疗
- 用户长期透支且拒绝干预时提示专业咨询

#### ✅ 校验验收规则

**格式校验**：
- [ ] JSON 五字段齐全
- [ ] level 与 battery_pct 一致

**内容校验**：
- [ ] 信号有数值依据
- [ ] 恢复方案可执行

**合规校验**：
- [ ] 未替代医疗诊断
- [ ] 透支时明确禁止加练

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：用户反馈 < 7/10；预警与实际受伤不符；新可穿戴指标接入

**版本升级触发**：
- 新增 ≥3 类生理信号 → minor
- 折算模型重构 → major

**废弃触发**：
- 依赖数据源停更 → deprecated

---

---

*版本：v1.0 (Gen3) · 2026-07-08 创建*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
