
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
- [ ] 建议可执行性验证（每条建议有具体行动）
- [ ] 训练调整逻辑合理性（低谷→休息，正常→维持）
- [ ] 输出 JSON 格式合规性

---

## 💡 使用示例

### 示例 1：正常状态评估

**输入**：
```json
{
  "sleep_data": {"duration_hours": 7.5, "quality_score": 82, "deep_pct": 18, "rem_pct": 22, "wake_count": 1},
  "exercise_data": {"type": "run", "duration_min": 60, "tl": 180},
  "focus_data": {"focus_ratio": 0.65, "interruptions_per_hour": 4},
  "subjective_feeling": "normal"
}
```

**输出**：
```json
{
  "compute_score": {"total": 78, "sleep": 82, "exercise": 76, "focus": 75, "recovery": 80},
  "alerts": [{"level": "green", "category": "overall", "message": "生物算力良好"}],
  "training_adjustment": {"today_plan": "正常训练", "adjustment": "maintain"}
}
```

### 示例 2：睡眠不足预警

**输入**：
```json
{
  "sleep_data": {"duration_hours": 5.0, "quality_score": 45, "deep_pct": 10, "rem_pct": 15, "wake_count": 4}
}
```

**输出**：
```json
{
  "compute_score": {"total": 48, "sleep": 35, "exercise": 70, "focus": 50, "recovery": 60},
  "alerts": [
    {"level": "red", "category": "sleep", "message": "睡眠严重不足(5h)，深睡比过低(10%)", "threshold": "≥7h", "current_value": "5h"},
    {"level": "red", "category": "overall", "message": "生物算力低谷(48分)，建议强制休息"}
  ],
  "training_adjustment": {"today_plan": "原定跑步", "adjustment": "rest", "reason": "睡眠不足，免疫力下降风险"}
}
```

### 示例 3：过训预警（边界场景）

**输入**：
```json
{
  "sleep_data": {"duration_hours": 7, "quality_score": 70},
  "exercise_data": {"type": "run", "duration_min": 90, "tl": 420}
}
```

**输出**：
```json
{
  "alerts": [
    {"level": "red", "category": "exercise", "message": "训练负荷过高(TL=420)，有过训风险", "threshold": "TL≤350", "current_value": "420"}
  ],
  "training_adjustment": {"adjustment": "rest", "reason": "高负荷后需恢复"}
}
```

---

## 🧪 Self-Play 测试

### 测试用例

| # | 场景 | 输入要点 | 期望输出 | 边界条件 |
|---|------|----------|----------|----------|
| 1 | 正常状态 | 睡7.5h+中等运动+正常专注 | 🟢 总分≥70，maintain | 无 |
| 2 | 睡眠不足 | 睡5h+深睡10% | 🔴 睡眠红色预警+建议休息 | 极端睡眠 |
| 3 | 连续过训 | TL>300连续2天 | 🔴 过训预警+强制休息 | 连续天数 |
| 4 | 数据缺失 | 仅提供睡眠数据 | 降级评估+警告 | 部分输入 |
| 5 | 全面低谷 | 睡5h+无运动+专注差 | 🔴 全维度红色+强制休息日 | 多维度叠加 |

### Critic 攻击

- "预警阈值是否太敏感？是否会频繁误报？"
- "建议是否足够具体？'早睡'不如'22:30前上床'可执行"
- "是否考虑了个体差异？不同人睡眠需求不同"

---

## 📊 版本记录

| 版本 | 日期 | 变更内容 | 验证结果 |
|------|------|----------|----------|
| v1.0 | 2026-06-17 | 初始 Prompt wrapper 版本 | — |
| v2.0 | 2026-06-29 | 升级为 Gen3 Schema：补齐 9 模块 | 待验证 |


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

*Agent可读性标记：search_keywords=[生物算力预警；睡眠监控；运动负荷；精力评估]；context_triggers=[健康管理；跑步训练；晨间习惯；疲劳预警]*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [训练类型] for [跑者水平], with [身体状态], leaning toward [训练计划/恢复策略]."

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
| ""今天状态不好不记录了"" | "跑完不记等于没跑，数据是训练的基础" |
| ""少跑一次没关系"" | "连续中断是放弃的前兆" |
| ""配速慢一点无所谓"" | "配速是训练强度的直接指标" |
| ""伤了再休息"" | "伤了再休息是被动休息，主动恢复才是正道" |
| ""不需要热身"" | "热身5分钟省的是5天伤病假" |

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


**相关概念**：[[运动生物力学基础]]

---

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
