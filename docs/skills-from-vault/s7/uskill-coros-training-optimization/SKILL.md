---
name: uskill-coros-training-optimization
description: "每一跳心率都是身体的语言——学会解读它，就知道该怎么练。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-coros-training-optimization.md"
  original_id: "SKL-6801"
  version: "3.0.0"
  trust: untrusted
---

# Coros数据分析与训练优化

- 维度/健康
- 类型/方法
- 来源/个人经历
- 领域/跑步
- 领域/运动康复


description: |
  当用户需要分析 Coros Pace 4 训练数据、优化[[跑步训练计划]]、解读生理指标时使用此 Skill。
  触发词：'Coros'、'跑步数据'、'训练分析'、'心率区间'、'VO2max'、'跑步训练'、'Cadence'。
  隐式触发：当提到跑步表现、配速下降、恢复不足时也应使用此 Skill。

# Coros 数据分析与训练优化

## 🎯 目标

> 从 Coros 数据中提取可执行的训练洞察，将「感觉式训练」升级为「数据驱动训练」。

**核心价值**：大多数跑者只看配速和距离，忽略了心率漂移、HRV 恢复、训练负荷等关键信号。本 Skill 将 Coros 数据转化为个性化的训练决策。

**适用场景**：
- 赛前训练计划制定与调整
- 训练负荷监控与过度训练预防
- 心率区间校准与 Zone 2 训练验证
- 伤病风险评估与恢复建议
- 半马/全马备赛策略优化

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `data_source` | string | ✅ | — | Coros 数据（导出文件/API/手动输入） |
| `analysis_type` | enum | ❌ | `"weekly"` | 分析周期：`single_run` / `weekly` / `monthly` / `period` |
| `goal` | enum | ❌ | `"performance"` | 目标：`performance`（提速）/ `endurance`（耐力）/ `recovery`（恢复）/ `race_prep`（备赛） |
| `current_weekly_km` | float | ❌ | — | 当前周跑量（公里） |
| `race_target` | string | ❌ | — | 目标赛事（如"2026北京半马"） |

## 📤 输出

```json
{
  "status": "success|partial|failed",
  "summary": "string — 一句话执行总结",
  "training_load": {
    "acute_load": "float — 急性训练负荷（7天）",
    "chronic_load": "float — 慢性训练负荷（28天）",
    "acwr": "float — 急慢性比（0.8-1.3 为安全区）",
    "trend": "string — 负荷趋势（上升/稳定/下降）"
  },
  "heart_rate_analysis": {
    "zone_distribution": {"zone1": "int%", "zone2": "int%", "zone3": "int%", "zone4": "int%", "zone5": "int%"},
    "drift_rate": "float — 心率漂移率（%/km）",
    "hrv_trend": "string — HRV 趋势（上升/稳定/下降）",
    "resting_hr": "int — 静息心率"
  },
  "performance_metrics": {
    "vo2max": "float — 最大摄氧量",
    "pace_at_hr150": "string — 心率150时的配速",
    "cadence_avg": "int — 平均步频",
    "ground_contact_time": "int — 触地时间（ms）"
  },
  "training_recommendation": {
    "weekly_plan": "string — 本周训练建议",
    "zone_adjustment": "string — 心率区间调整建议",
    "recovery_priority": "string — 恢复重点",
    "race_readiness": "string — 备赛就绪度评估"
  }
}
```

## 📋 执行步骤

### Step 1: 数据提取与清洗
1. **数据导入** — 从 Coros 导出训练日志
2. **异常过滤** — 排除 GPS 漂移/心率异常的训练段
3. **指标计算** — 计算训练负荷、心率分布、配速趋势
4. **检查点**：✅ 数据是否完整？是否有异常值需要排除？

### Step 2: 训练负荷分析
1. **急性负荷** — 过去 7 天的 TRIMP（训练冲量）
2. **慢性负荷** — 过去 28 天的平均 TRIMP
3. **ACWR 计算** — 急慢性比，判断训练是否过量或不足
4. **趋势判断** — 负荷是在上升、稳定还是下降
5. **检查点**：✅ ACWR 是否在 0.8-1.3 安全区？趋势是否合理？

### Step 3: 生理指标解读
1. **心率漂移** — 长距离跑步中心率是否稳定（漂移 <5% 为优秀）
2. **HRV 趋势** — 恢复质量的窗口（上升=恢复好，下降=需要休息）
3. **静息心率** — 晨起心率异常升高 = 过度训练信号
4. **VO2max 趋势** — 有氧能力的长期变化
5. **检查点**：✅ HRV 是否支持当前训练强度？是否有过度训练信号？

### Step 4: 训练计划优化
1. **负荷调整** — 根据 ACWR 调整下周训练量
2. **心率区间** — 基于最新数据校准 5 区间
3. **恢复建议** — 针对恢复不足给出具体方案
4. **备赛策略** — 如有赛事目标，调整减量周期
5. **检查点**：✅ 训练计划是否匹配当前状态？恢复建议是否具体？

## ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 当 HRV 连续 3 天低于基线 15% 时，**必须**建议降低训练强度
2. 当 ACWR >1.5 时，**必须**标记为过度训练风险
3. 不得建议任何可能导致伤病的训练方案

**软性约束（建议遵守）**：
1. Zone 2 训练占比应 ≥80%（80/20 原则）
2. 每周跑量递增不超过 10%

**人工兜底点**：
- 当出现胸痛/呼吸困难等异常症状时，**必须**建议就医
- 当数据不足以做出准确判断时，**必须**建议人工审核

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| HRV 异常低 | <基线 20% | 建议完全休息 1-2 天 |
| 心率漂移大 | >10%/km | 建议降低配速、增加 Zone 2 训练 |
| VO2max 下降 | 连续 4 周下降 | 检查训练单调性，建议交叉训练 |
| 静息心率飙升 | >基线 +10bpm | 建议休息并排查身体状况 |


### 降级策略
- 当数据不足时，基于已有数据给出保守建议并标注置信度
- 当无法自动化时，输出分析框架供人工填充

## 💬 沟通风格

### 语气锚点
- **数据驱动**：「你的 ACWR 已达 1.4，接近过度训练阈值」
- **鼓励优先**：「Zone 2 占比从 60% 提升到 75%，有氧基础在变强」
- **行动导向**：「建议明天安排一次 30 分钟的恢复慢跑」

### 输出原则
- 每个建议都附带数据依据
- 用趋势而非单次数据做判断
- 优先保障安全，其次追求成绩

### 风格禁区
- ❌ 禁止：忽略异常生理信号继续建议高强度训练
- ❌ 禁止：用单次训练数据推翻长期趋势
- ⚠️ 谨慎：涉及伤病风险时必须附加免责声明

## 📝 自检清单

- [ ] 训练负荷分析是否完成（ACWR）？
- [ ] 心率漂移率是否已计算？
- [ ] HRV/静息心率趋势是否已分析？
- [ ] Zone 2 占比是否达到 80%？
- [ ] 训练建议是否匹配当前恢复状态？
- [ ] 是否有过度训练风险提示？
- [ ] 备赛减量周期是否已规划（如有赛事）？

## ✅ 校验验收规则

**格式校验**：
- [ ] 输出包含训练负荷/心率/性能/建议四个区块
- [ ] 所有数值指标已计算

**内容校验**：
- [ ] 训练建议有数据支撑
- [ ] 恢复建议具体可执行
- [ ] 考虑了跑者当前状态

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 异常症状已建议就医


### OVP 验证信号
- 核心指标趋势是否向好
- 用户使用频率是否稳定
- 输出质量是否达到预期

## 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：weekly
- **触发条件**：
  - Coros 固件更新导致数据格式变化
  - 用户反馈训练建议不准确
  - 新的跑步科学研究发表

**版本升级触发**：
- 当新增训练分析维度（如跑步动力学）时，升级 minor 版本

**废弃触发**：
- 当所依赖的数据源/API 停止服务时，标记为 deprecated
- 当出现明显更优的替代方案时，评估迁移并

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
