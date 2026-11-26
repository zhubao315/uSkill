---
name: uskill-productivity-cash-flow-quadrant-analysis
description: "让productivity cash flow quadrant analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-cash-flow-quadrant-analysis.md"
  original_id: "SKL-6919"
  version: "3.0.0"
  trust: untrusted
---

# productivity cash flow quadrant analysis

# 现金流象限分析与转换规划

## 🎯 目标
> 运用现金流象限（E-S-B-I）模型分析个人当前财务定位，识别象限转换机会，制定从主动收入向被动收入过渡的分阶段行动计划，实现财务自由路径规划。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `current_income` | object | ✅ | 当前收入结构：`{salary, side_hustle, investment, passive}` 各项年收入 |
| `current_expenses` | number | ✅ | 年生活总开支 |
| `career_stage` | enum | ✅ | `early`（0-5年）/ `mid`（5-15年）/ `senior`（15年+） |
| `risk_tolerance` | enum | ❌ | `conservative` / `moderate` / `aggressive`，默认 `moderate` |
| `target_freedom_years` | int | ❌ | 希望几年内实现财务自由，默认 10 |
| `existing_assets` | array | ❌ | 已有的资产列表（房产、股票、企业股权等） |

## 📤 输出

```json
{
  "quadrant_diagnosis": {
    "current_quadrant": "string — E/S/B/I 及混合象限",
    "income_breakdown": {
      "active_income_pct": "number — 主动收入占比",
      "passive_income_pct": "number — 被动收入占比"
    },
    "freedom_ratio": "number — 被动收入/生活开支（目标≥1.0）",
    "key_risk": "string — 当前象限的核心风险"
  },
  "asset_liability_audit": {
    "true_assets": ["string — 正现金流资产"],
    "disguised_liabilities": ["string — 伪装成资产的负债"],
    "net_cash_flow": "number — 月净现金流"
  },
  "transition_plan": {
    "target_quadrant": "string — 目标象限",
    "phases": [
      {
        "phase": "string — 阶段名称",
        "duration": "string — 预计时长",
        "actions": ["string — 具体行动"],
        "milestone": "string — 阶段里程碑"
      }
    ],
    "skill_gaps": ["string — 需要学习的技能"],
    "capital_requirements": "string — 所需启动资金估算"
  },
  "passive_income_targets": {
    "year_1": "number — 第1年被动收入目标",
    "year_3": "number — 第3年被动收入目标",
    "year_5": "number — 第5年被动收入目标",
    "freedom_target": "number — 财务自由所需被动收入"
  }
}
```

## 📋 执行步骤

1. **象限定位** — 根据 `current_income` 的收入结构，判断当前主力象限（E/S/B/I）及混合象限状态
2. **现金流审计** — 将 `existing_assets` 按现金流方向分类为真资产（正现金流）和伪负债（负现金流），计算月净现金流
3. **自由比率计算** — 用被动收入 ÷ 生活开支得出自由比率（freedom_ratio），比率≥1.0即为财务自由
4. **风险评估** — 识别当前象限的核心风险（E=裁员风险、S=停工风险、B=经营风险、I=市场风险）
5. **技能差距分析** — 对比当前象限与目标象限所需的技能组合，识别关键技能缺口
6. **阶段规划** — 制定3-5个阶段的象限转换计划，每阶段包含具体行动、里程碑和时间线
7. **被动收入目标设定** — 按1/3/5年设定被动收入增长目标，与财务自由目标对齐
8. **行动清单生成** — 输出本月内可启动的3-5个具体行动项

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 被动收入为零 | 标注"尚未启动象限转换"，优先规划I象限入门行动 |
| 生活开支远超收入 | 先解决现金流为负的紧急问题，再规划象限转换 |
| 风险承受力与目标不匹配 | 调整时间线，保守策略延长1-2年 |
| 职业阶段过晚（senior） | 聚焦E→I路径（投资为主），而非E→B（创业为主） |

## ✅ 自检清单

- [ ] 象限诊断准确反映了收入结构，非仅凭职业头衔判断
- [ ] 资产/负债分类基于现金流方向，非会计定义
- [ ] 自由比率计算准确，被动收入口径一致
- [ ] 阶段规划每步都有具体可执行的行动项
- [ ] 被动收入目标保守估计，留有安全边际
- [ ] 技能差距分析具体到可学习的课程或书籍


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

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-05-09 | 1.0.0 | 初始版本，从《穷爸爸富爸爸》现金流象限理论转化 |

---
**相关笔记**：[[邮件处理]] [[客户点单工作流优化]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

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
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
-

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
