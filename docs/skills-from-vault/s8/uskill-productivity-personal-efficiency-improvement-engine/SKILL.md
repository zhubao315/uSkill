---
name: uskill-productivity-personal-efficiency-improvement-engine
description: "让productivity personal efficiency improvement engine变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-personal-efficiency-improvement-engine.md"
  original_id: "SKL-5079"
  version: "3.0.0"
  trust: untrusted
---

# productivity personal efficiency improvement engine

# Personal Efficiency Improvement Engine（AI赋能个人效能持续改进引擎）

## 🎯 目标
> 通过AI赋能的"IAIC"持续改进循环（识别→分析→实施→控制），系统性地识别、分析和消除个人工作与生活中的低效环节，持续提升单位时间价值产出。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `time_tracking_data` | string | ✅ | 至少一周的时间追踪数据（CSV/JSON，含活动名称、开始时间、结束时间、分类） |
| `focus_area` | string | ❌ | 重点优化领域（如"会议效率"、"上下文切换"、"信息焦虑"） |
| `tools_available` | string[] | ❌ | 可用效率工具列表（如Toggl、RescueTime、Zapier、Python） |
| `improvement_goal` | string | ❌ | 期望改进目标（如"深度工作时间提升到每天4小时"） |
| `cycle_number` | number | ❌ | 当前改进周期序号（默认1），用于追踪迭代历史 |

## 📤 输出

```json
{
  "time_audit_report": {
    "total_tracked_hours": 112.5,
    "deep_work_ratio": 0.164,
    "top3_time_sinks": [
      {"activity": "string", "hours": 12.3, "ratio": 0.109}
    ],
    "surprise_findings": ["string"]
  },
  "root_cause_analysis": {
    "target_bottleneck": "string",
    "five_whys": ["string"],
    "psychological_insight": "string",
    "keystone_pattern": true
  },
  "improvement_experiment": {
    "name": "string",
    "duration_days": 7,
    "success_metrics": {
      "primary": "string",
      "secondary": "string"
    }
  }
}
```

## 📋 执行步骤

### 阶段一：识别瓶颈（Identify Bottlenecks）

1. **收集数据** — 确保Toggl/RescueTime等时间追踪工具已稳定运行至少一周，收集至少100小时数据样本
2. **聚合可视化** — 将原始数据导出并生成时间分配饼图（深度工作 vs 辅助工作 vs 浪费），按活动类型排序找出Top 5时间黑洞
3. **AI辅助瓶颈定位** — 使用提示词让AI扮演精益生产专家，分析时间日志，识别Top 3"浪费"环节（频繁上下文切换、过长会议、重复手动操作）

### 阶段二：分析根源（Analyze Root Causes）

4. **聚焦核心问题** — 从Top 3瓶颈中选择本周期最想解决的一个
5. **执行"5 Why"分析** — 连续追问至少5个"为什么"，区分"症状"与"根因"，直到触及根本原因
6. **AI辅助心理洞察** — 使用提示词让AI扮演行为分析师，结合"5 Why"结果，从认知心理学角度（决策疲劳、完美主义、启动困难）深度剖析低效行为的心理动机

### 阶段三：实施优化（Implement Improvements）

7. **设计"效率实验"** — 针对根本原因设计具体的、有时限的、可衡量的改进实验（周期7天，成功标准必须量化，实施步骤≤3步）
8. **AI辅助自动化方案** — 使用提示词让AI扮演自动化工程师，为识别出的重复性手动任务建议具体工具或生成自动化脚本
9. **执行实验** — 在下一周期严格执行实验方案，每天记录关键指标

### 阶段四：控制与固化（Control & Standardize）

10. **评估实验效果** — 实验结束后重新采集数据，对比实验前后关键指标
11. **成功则固化** — 将验证有效的方法纳入个人SOP或习惯清单
12. **失败则复盘** — 回到阶段二重新分析原因，或设计新的实验方案
13. **记录到知识库** — 将本次循环的经验教训记录到个人知识管理系统，供未来查阅

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 时间追踪数据不足 | 先用100小时时间审计法收集一周数据，再进入分析阶段 |
| 找不到根本原因 | 换一个瓶颈重新分析，或请他人做"外部视角"诊断 |
| 实验方案太复杂 | 砍到只保留1个核心变量，确保实验可执行 |
| 实验失败 | 记录"此路不通"作为有价值的排除法数据，回到阶段二迭代 |
| 多个瓶颈并存 | 每个周期只聚焦1个瓶颈，贪多嚼不烂 |

## ✅ 自检清单

- [ ] 时间追踪数据≥100小时且分类清晰
- [ ] Top 3时间黑洞已量化（非主观感觉）
- [ ] "5 Why"分析已触及根本原因（非外部不可控因素）
- [ ] 效率实验的成功标准已量化且可衡量
- [ ] 实验周期≤7天且不影响核心工作
- [ ] 实验结果已记录到知识库


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
| 2026-05-09 | 1.0.0 | 初始版本，从 SOP-23 转化 |

---
**相关笔记**：[[uSkill-agent-优先级排序-agent-实施手册]] [[深度工作四步法——专注力炼金术]] 


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
- 执行核心功能（见原技能

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
