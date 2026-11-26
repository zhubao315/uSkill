---
name: uskill-productivity-analyze-efficiency
description: "让productivity analyze efficiency变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-analyze-efficiency.md"
  original_id: "SKL-6909"
  version: "3.0.0"
  trust: untrusted
---

# productivity analyze efficiency

# Analyze Personal Efficiency

## 🎯 目标
> AI赋能的个人效能持续改进引擎——通过时间追踪数据系统性识别、分析和消除低效环节，以IAIC循环（识别→分析→实施→固化）持续提升单位时间的价值产出。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `time_log` | string (CSV) | ✅ | 时间追踪日志，包含活动名称、开始时间、结束时间、分类 |
| `tracking_days` | int | ✅ | 数据采集天数（建议 ≥ 7） |
| `focus_area` | string | ❌ | 希望重点优化的领域，为空则由AI从Top 3中推荐 |
| `existing_sops` | array[string] | ❌ | 现有个人SOP清单，用于固化阶段参考 |
| `cycle_phase` | enum | ❌ | `identify` / `analyze` / `implement` / `control`，默认 `identify` |

## 📤 输出

```json
{
  "audit_report": {
    "time_distribution": {
      "high_value_pct": "number — 高价值创造占比(%)",
      "low_value_pct": "number — 低价值维护占比(%)",
      "waste_pct": "number — 纯粹浪费占比(%)"
    },
    "top3_bottlenecks": [
      {
        "rank": "int",
        "activity": "string — 具体活动名称",
        "hours_per_week": "number — 每周耗时",
        "waste_type": "string — 浪费类型(等待/返工/重复/上下文切换等)"
      }
    ]
  },
  "root_cause_analysis": {
    "target_bottleneck": "string — 本周期聚焦的瓶颈",
    "five_whys": ["string — 5 Why分析链"],
    "psychological_insight": "string — 认知心理学角度的深层原因",
    "root_cause": "string — 根本原因总结"
  },
  "experiment_plan": {
    "hypothesis": "string — 改进假设",
    "method": "string — 具体实验方法",
    "duration": "string — 实验周期",
    "success_metric": "string — 量化的成功标准",
    "automation_solution": "string | null — 自动化方案(如有)"
  },
  "standardization": {
    "is_success": "boolean — 实验是否成功",
    "updated_sop": "string | null — 更新后的SOP或习惯",
    "lessons_learned": ["string — 经验教训"]
  }
}
```

## 📋 执行步骤

### 阶段一：识别瓶颈（Identify）

1. **校验数据** — 确认 `time_log` 数据完整性，`tracking_days` ≥ 7，缺失则警告样本不足
2. **聚合统计** — 将原始CSV按分类汇总时间，计算高价值/低价值/浪费三类占比
3. **AI瓶颈定位** — 以"精益生产专家"角色分析时间日志，识别Top 3"浪费"环节（频繁上下文切换、过长会议、重复手动操作等）

### 阶段二：分析根源（Analyze）

4. **聚焦核心问题** — 从Top 3瓶颈中选取 `focus_area`，或由AI推荐本周期最值得解决的瓶颈
5. **执行5 Why分析** — 连续追问至少5个"为什么"，逐层深入直至触及根本原因
6. **心理洞察** — 以"行为分析师"角色，从认知心理学角度（决策疲劳、完美主义、启动困难等）剖析低效行为背后的心理动机

### 阶段三：实施优化（Implement）

7. **设计效率实验** — 针对根本原因，制定具体的、有时限的、可衡量的改进实验方案
8. **生成自动化方案** — 若瓶颈为重复性手动任务，以"自动化工程师"角色生成具体工具建议或脚本代码
9. **输出执行计划** — 明确实验周期、执行细节、成功标准，确保方案足够简单不影响核心工作

### 阶段四：控制固化（Control）

10. **评估实验效果** — 实验周期结束后重新采集数据，对比前后关键指标
11. **成功则固化** — 实验成功则将方法论/自动化工具纳入个人工作流程，更新相关SOP
12. **失败则复盘** — 实验失败则回到阶段二重新分析原因，或回到阶段三设计新方案
13. **记录经验沉淀** — 将本次IAIC循环的经验教训记录到知识管理系统，供未来查阅

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `time_log` 为空或格式错误 | 返回错误：`ERROR_INVALID_LOG`，要求提供标准CSV格式 |
| `tracking_days` < 7 | 返回警告：样本不足，建议积累≥7天数据后再分析 |
| 无明显瓶颈（三类占比均合理） | 建议更细粒度的分类维度，或扩大数据采集范围 |
| 5 Why分析未触及根本原因 | 引导从不同角度（技术、流程、心理）重新追问 |
| 实验方案过于复杂 | 建议拆分为多个小实验，降低执行门槛 |
| 自动化方案涉及敏感数据 | 提醒注意数据安全，建议本地化处理 |

## ✅ 自检清单

- [ ] 时间数据是否覆盖完整周期（≥ 7天）？
- [ ] Top 3瓶颈是否量化了具体耗时和浪费类型？
- [ ] 根本原因是否为具体行为或思维模式（非外部不可控因素）？
- [ ] 实验方案的成功标准是否已量化？
- [ ] 实验方案是否足够简单，不影响核心工作？
- [ ] 成功的实验是否已固化为新SOP或习惯？
- [ ] 本次循环的经验教训是否已记录？


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-23 转化 |

---
**相关笔记**：[[现金流四象限分析]] [[OKR 战略目标管理]] 


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


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
