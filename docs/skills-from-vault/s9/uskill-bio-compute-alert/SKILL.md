---
name: uskill-bio-compute-alert
description: "让生物算力预警 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-bio-compute-alert.md"
  original_id: "SKL-6901"
  version: "3.0.0"
  trust: untrusted
---

# 生物算力预警 Agent — 实施手册

description: |
  当用户需要监控和评估睡眠、运动、专注时长、身心状态等生物算力指标时使用此 Skill。
  触发词包括：'生物算力'、'睡眠预警'、'运动负荷'、'精力状态'、'身体状态评估'。
  当用户说"我今天状态怎么样"、"最近身体指标如何"，即使未直接说"生物算力"，也应使用此 Skill。
  不适用于医疗诊断。仅用于个人健康管理与优化。

---

# 🏃 uSkill-301: 生物算力预警

## 🎯 目标

> 监控睡眠/跑量/专注时长/身心状态，量化评估生物算力水平，提供预警和优化建议。

**核心价值**：把身体视为"生物算力基座"，用数据驱动健康决策，避免过度训练或精力透支。

**适用场景**：
- 每日晨间/晚间身体状态评估
- 训练负荷监控（跑步/健身前后）
- 工作专注力追踪
- 睡眠质量分析
- 疲劳累积预警

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `sleep_data` | `object` | ✅ | — | 睡眠数据（时长、深睡、浅睡、REM、醒来次数） |
| `exercise_data` | `object` | ❌ | — | 运动数据（类型、时长、心率、配速、训练负荷） |
| `focus_data` | `object` | ❌ | — | 专注数据（专注时长、打断次数、任务完成率） |
| `subjective_feeling` | `enum` | ❌ | `normal` | `great` / `normal` / `tired` / `exhausted` |
| `hrv_data` | `number` | ❌ | — | 最近 HRV 值（ms），如有 |

**输入约束**：
- `sleep_data` 至少包含 `duration_hours` 和 `quality_score`（0-100）
- `exercise_data` 如提供，需包含 `type`（run/cycle/strength/rest）和 `duration_min`
- 数据来源建议：Coros 手表 / Apple Health / 手动录入

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话生物算力状态总结",
  "date": "YYYY-MM-DD",
  "compute_score": {
    "total": "number (0-100)",
    "sleep": "number (0-100)",
    "exercise": "number (0-100)",
    "focus": "number (0-100)",
    "recovery": "number (0-100)"
  },
  "alerts": [
    {
      "level": "red|yellow|green",
      "category": "sleep|exercise|focus|recovery",
      "message": "string",
      "threshold": "string",
      "current_value": "string"
    }
  ],
  "recommendations": [
    {
      "priority": "P0|P1|P2",
      "action": "string",
      "reason": "string",
      "deadline": "string"
    }
  ],
  "training_adjustment": {
    "today_plan": "string",
    "adjustment": "maintain|reduce|intensify|rest",
    "reason": "string"
  }
}
```

### 异常输出

- 数据缺失 → 输出警告「部分数据缺失，评估结果可能不准确」+ 基于可用数据的降级评估
- 指标异常极端（如睡眠<4h或>12h）→ 标注数据可能异常，建议核实

---

## 🔄 执行流程

```
1. [数据采集] → 接收输入数据
   → 判断条件：sleep_data 是否完整？
     → 是：进入步骤2
     → 否：输出警告，使用默认值降级处理

2. [睡眠评估] → 计算睡眠质量分
   → 规则：时长<6h → -20分；深睡<15% → -10分；REM<20% → -5分
   → 规则：醒来次数>3 → -5分/次
   → 计算公式：sleep_score = max(0, 100 - deductions)
   → 判断条件：sleep_score < 60？
     → 是：触发 🔴 睡眠预警
     → 否：sleep_score < 75？→ 触发 🟡 睡眠关注 → 继续

3. [运动负荷评估] → 计算运动恢复分
   → 判断条件：exercise_data 是否提供？
     → 是：计算训练负荷(TL)和恢复度
     → 否：默认恢复度=80%（假设无额外消耗）
   → 规则：连续2天高强度(TL>300) → 🔴 过训预警
   → 规则：当日TL>400 → 🟡 高负荷关注
   → 计算公式：exercise_score = 100 - (TL/5) - (consecutive_high*10)

4. [专注力评估] → 计算专注效能分
   → 判断条件：focus_data 是否提供？
     → 是：计算专注时长/总工作时长比例
     → 否：跳过此项，focus_score=70（默认中等）
   → 规则：专注比例<40% → 🟡 专注力关注
   → 规则：打断次数>10/小时 → 🔴 环境干扰预警

5. [综合评估] → 计算生物算力总分
   → 公式：total = sleep*0.35 + exercise*0.25 + focus*0.25 + recovery*0.15
   → 判断条件：total < 50？
     → 是：🔴 生物算力低谷，建议休息日
     → 否：total < 70？→ 🟡 生物算力一般，建议调整
     → 否：total ≥ 70？→ 🟢 生物算力良好，可正常执行计划

6. [生成建议] → 基于评估结果生成优化建议
   → 睡眠问题 → 建议早睡/减少屏幕/改善环境
   → 运动问题 → 建议减量/休息/交叉训练
   → 专注问题 → 建议番茄钟/降噪/任务拆分
   → 综合低谷 → 建议强制休息日+早睡+轻度活动

7. [输出报告] → 生成结构化生物算力报告
   → 包含：状态总览 + 三维评分 + 预警列表 + 优化建议 + 训练调整
```

---

## 📝 Prompt 模板

### 晨间评估 Prompt

```
你是生物算力预警Agent。请评估今日生物算力状态。

【输入数据】
- 日期：{date}
- 睡眠数据：{sleep_data}
- 运动数据：{exercise_data}
- 专注数据：{focus_data}
- 主观感受：{subjective_feeling}

【评估维度】
1. 睡眠质量分（0-100）：时长、深睡比、REM比、醒来次数
2. 运动恢复分（0-100）：训练负荷、连续高强度天数
3. 专注效能分（0-100）：专注比例、打断频率
4. 综合生物算力分 = 睡眠*0.35 + 运动*0.25 + 专注*0.25 + 恢复*0.15

【预警规则】
- 🔴 红色预警：score < 60（必须调整/休息）
- 🟡 黄色关注：60 ≤ score < 75（建议优化）
- 🟢 绿色正常：score ≥ 75（维持现状）

【输出格式】
按标准 JSON 输出格式，包含 compute_score、alerts、recommendations、training_adjustment。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| sleep_data 缺失 | 输出警告，使用默认值 | sleep_score=50，标注"数据缺失" |
| exercise_data 缺失 | 假设无额外运动消耗 | recovery_score=80 |
| focus_data 缺失 | 跳过专注评估 | focus_score=70 |
| HRV 数据异常 | 标注数据可能不可靠 | 不参与综合评分 |
| 连续3天红色预警 | 触发强制休息建议 | 建议停训1-2天 |

---

## ✅ 质量自检

- [ ] sleep_data 字段完整性检查（duration_hours + quality_score）
- [ ] 计算公式正确性验证（各维度分值范围 0-100）
- [ ] 预警阈值合理性检查（红色<60，黄色<75）
- [ ] 建议可执

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
