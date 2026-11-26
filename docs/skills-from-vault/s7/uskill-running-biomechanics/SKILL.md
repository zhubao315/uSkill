---
name: uskill-running-biomechanics
description: "跑步效率的差距不在心肺——在每一步的力学效率。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-running-biomechanics.md"
  original_id: "SKL-6807"
  version: "3.0.0"
  trust: untrusted
---

# 跑步生物力学分析

- 维度/健康
- 类型/方法
- 来源/个人经历
- 领域/跑步
- 领域/运动康复


description: |
  当用户需要分析跑步姿势、优化跑步经济性、改善步态、预防跑步损伤时使用此 Skill。
  触发词：'跑步姿势'、'步态分析'、'跑步经济性'、'触地时间'、'步频'、'垂直振幅'。

# 跑步生物力学分析

## 🎯 目标

> 通过生物力学指标分析，找到提升跑步效率和预防伤病的切入点。

**核心价值**：跑步成绩 = 心肺能力 × 力量 × 生物力学效率。大多数人只练心肺，忽略了力学优化。本 Skill 用 Coros 数据中的生物力学指标找到最高效的改进方向。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `data_source` | string | ✅ | — | Coros 训练数据 |
| `analysis_focus` | enum | ❌ | `"comprehensive"` | 重点：`comprehensive` / `injury_prevention` / `performance` / `economy` |
| `current_issues` | array | ❌ | — | 当前问题（如"膝盖痛""配速瓶颈"） |

## 📤 输出

```json
{
  "status": "success|partial|failed",
  "summary": "string — 一句话执行总结",
  "biomechanical_metrics": {
    "cadence": "int — 步频（spm）",
    "ground_contact_time": "int — 触地时间（ms）",
    "vertical_oscillation": "float — 垂直振幅（cm）",
    "vertical_ratio": "float — 垂直步幅比",
    "left_right_balance": "float — 左右平衡度（%）"
  },
  "economy_score": {
    "score": "int — 跑步经济性评分（0-100）",
    "strengths": ["string"],
    "weaknesses": ["string"]
  },
  "improvement_plan": {
    "priority": "string — 最优先改进的指标",
    "exercises": ["string — 针对性训练动作"],
    "cues": ["string — 跑步时的心理提示"],
    "timeline": "string — 预期改善时间"
  }
}
```

## 📋 执行步骤

### Step 1: 指标提取
1. **Coros 数据** — 提取步频/触地时间/垂直振幅等指标
2. **基准对比** — 与精英跑者数据对比
3. **趋势分析** — 这些指标的变化趋势
4. **检查点**：✅ 指标是否完整？是否有足够数据量？

### Step 2: 经济性评估
1. **垂直步幅比** — 越低越好（<8% 为优秀）
2. **触地时间** — 越短越好（<250ms 为优秀）
3. **左右平衡** — 偏差 >3% 可能导致伤病
4. **检查点**：✅ 经济性评分是否合理？弱点是否识别？

### Step 3: 改进方案
1. **优先级排序** — 从影响最大的指标开始改进
2. **训练动作** — 针对每个弱点的具体训练
3. **跑步提示** — 跑步时的心理暗示（如"轻触地面""高步频"）
4. **检查点**：✅ 改进方案是否循序渐进？是否可执行？

### Step 4: 效果追踪
1. **定期测试** — 每 4 周测试一次关键指标
2. **对比分析** — 改进前后的数据对比
3. **方案调整** — 根据效果调整训练重点
4. **检查点**：✅ 是否有追踪计划？是否有效果对比？

## ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 姿势改变必须渐进，不得一次性大幅调整
2. 有伤病时必须先治疗再优化姿势
3. 不得建议可能导致代偿的动作

**软性约束（建议遵守）**：
1. 优先改善步频（最容易见效）
2. 每次只改变一个变量

**人工兜底点**：
- 当出现疼痛时，**必须**停止姿势调整并就医
- 当数据不足时，**必须**建议增加数据采集

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 左右失衡 | 偏差 >5% | 建议就医排查结构性问题 |
| 触地时间过长 | >300ms | 建议增加步频训练 |
| 垂直振幅过大 | >10cm | 建议「轻触地面」提示训练 |


### 降级策略
- 当数据不足时，基于已有数据给出保守建议并标注置信度
- 当无法自动化时，输出分析框架供人工填充

## 💬 沟通风格

- **力学语言**：用数据描述姿势，不用「好看/难看」
- **渐进导向**：强调小步改进而非大改
- **体验结合**：将力学指标与跑步感受关联

## 📝 自检清单

- [ ] 生物力学指标是否完整提取？
- [ ] 是否与精英跑者基准对比？
- [ ] 改进优先级是否明确？
- [ ] 训练动作是否具体可执行？
- [ ] 是否有追踪计划？

## ✅ 校验验收规则

**格式校验**：
- [ ] 输出包含指标/评分/改进方案
- [ ] 指标有具体数值

**内容校验**：
- [ ] 改进方案循序渐进
- [ ] 有针对弱点的训练动作
- [ ] 有跑步时的心理提示

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 伤病风险已评估


### OVP 验证信号
- 核心指标趋势是否向好
- 用户使用频率是否稳定
- 输出质量是否达到预期

## 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - Coros 固件更新新增指标
  - 用户反馈改进效果
  - 新的跑步生物力学研究

**版本升级触发**：
- 当新增分析维度（如跑步动力学）时，升级 minor 版本

**废弃触发**：
- 当所依赖的数据源/API 停止服务时，标记为 deprecated
- 当出现明显更优的替代方案时，评估迁移并标记版本
- 当集成视频分析时，升级 major 版本

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-07-03 | 1.0.0 | 初始版本，基于 Coros Pace 4 跑力数据定制 |

---

*关联笔记：[[uSkill-health-跑步训练姿势矫正协议]] · [[心率区间训练]] · [[Coros 数据体系]] · [[Zone 2 耐力训练]]*


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
   ↓         ↓ 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
