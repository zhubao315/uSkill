---
name: uskill-agent-1e0b1b
description: "让uSkill-身心循环智能体自适应负荷重排变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-身心循环智能体自适应负荷重排.md"
  original_id: "SKL-7054"
  version: "3.0.0"
  trust: untrusted
---

# uSkill-身心循环智能体自适应负荷重排

# uSkill-身心循环智能体自适应负荷重排

> 身心循环智能体（Bio-Loop Agent）的自适应负荷重排，通过HRV数据动态调整训练计划。

---

## 工程定位

### 核心目标

- **安全机制**：HRV跌破基线10%自动熔断
- **调整策略**：高强度计划自动切换为恢复周
- **验证信号**：实际周跑量上限自动调整

### 运行环境

- **部署位置**：端侧AI
- **数据来源**：Health Connect / Coros API
- **设备**：Coros Pace 4

---

## 自适应机制

### 监测指标

- **HRV基线**：长期追踪的稳态基线（75）
- **近期均值**：最近3天HRV均值
- **训练负荷**：当前周训练计划强度

### 熔断条件

- **触发条件**：HRV均值 < 基线 × 0.90
- **持续时间**：连续3天低于基线
- **调整幅度**：周跑量降低50%

### 恢复机制

- **恢复周期**：1周恢复期
- **逐步恢复**：每周评估恢复情况
- **目标回归**：恢复正常训练计划

---

## 自动化配置（Python端侧逻辑）

```python
# 运行于端侧本地 AI：身心循环智能体状态校验
import coros_api

hrv_baseline = 75  # 长期追踪的稳态基线
recent_hrv_average = coros_api.get_last_3_days_hrv_average()
current_weekly_plan = coros_api.get_current_training_plan()

# 循环工程 OVP 验证信号判断
if recent_hrv_average < (hrv_baseline * 0.90):
    # 连续 3 天低于基线 10%，安全爪硬性挂起
    activated_safety_claw = True
    new_plan = current_weekly_plan.convert_to_recovery_week(target_reduction=0.5)
    
    print(f"⚠️ [身心循环智能体预警] 发现生物算力不足！最近3天HRV均值: {recent_hrv_average}，已低于基线10%。")
    print(f"🚨 [Security Claw 触发] 下周奥运森林公园长跑计划已自动切换为【恢复周】。")
    print(f"📊 [OVP 验证信号] 实际周跑量上限已自动调整，等待宝哥在 Daily Note 签字确认。")
else:
    activated_safety_claw = False
    print("🟢 [身心循环智能体] 生物稳态指标正常，180+高步频'细胞分裂法'训练计划持续空转中。")
```

---

## 执行配置

### 触发词

`「检查身心循环状态」`

### Cron 规则

- **每日**：Coros API 数据同步时自动触发
- **事件触发**：HRV 跌破基线时立即触发熔断

### 与 Daily Loop 联动

- 晨间计划读取 HRV 状态，决定是否启动认知降载阻尼
- 晚间复盘记录当日训练负荷与恢复状态

### 异常重试 SOP

- **Coros API 不可用**：使用上次缓存的 HRV 数据，标记 `⚠️ 数据源离线`
- **HRV 数据异常跳变**：过滤离群值，取中位数替代均值
- **训练计划重排失败**：生成 Operator 签字块，等待手动干预

### 转录本驱动优化（月度）

每月分析身心循环会话中的反馈模式："恢复周不够""这个强度判断太保守"等，更新熔断阈值和恢复计划模板。

---

## 关联

- [[uSkill-日程优化-v1]]
- [[2026年跑步数据]]
- [[姿势跑法]]


![[SKILL]]

---

*关联项目：[[∑ 健身跑者]] · [[健身跑者]]*

---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

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
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

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


**相关概念**：[[姿势跑法]] · [[有氧基础训练]]

---


## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是 uLife OS 身心循环智能体的负荷重排引擎。基于 HRV、睡眠、主观疲劳度数据，动态调整当日训练计划。

输入：
- 当前 HRV：{{current_biometrics_HRV}}（3天均值）
- 今日计划：{{Today_Training_Plan}}
- 主观疲劳度：{{Subjective_Fatigue}}（1-10）
- 睡眠质量：{{Sleep_Quality}}（1-10）
要求：
1. IF HRV < baseline*0.90 OR 主观疲劳度 > 7 THEN 降载 30%
2. IF 睡眠质量 < 5 THEN 取消高强度训练，替换为 Zone2 恢复跑
3. 输出调整后的训练计划 +

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
