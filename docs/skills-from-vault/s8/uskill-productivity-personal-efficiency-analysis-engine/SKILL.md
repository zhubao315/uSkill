---
name: uskill-productivity-personal-efficiency-analysis-engine
description: "让productivity personal efficiency analysis engine变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-personal-efficiency-analysis-engine.md"
  original_id: "SKL-6922"
  version: "3.0.0"
  trust: untrusted
---

# productivity personal efficiency analysis engine

---
# Personal Efficiency Analysis Engine（个人效能持续改进引擎）

## 🎯 目标
> 通过AI赋能的"IAIC"持续改进循环（识别→分析→实施→控制），系统性地识别、分析和消除个人工作与生活中的低效环节，持续提升单位时间的价值产出。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `time_tracking_data` | string | ✅ | 至少一周的时间追踪数据（CSV/JSON格式，含活动名称、开始时间、结束时间、分类） |
| `focus_area` | string | ❌ | 希望重点优化的领域（如"会议效率"、"上下文切换"、"信息焦虑"） |
| `tools_available` | string[] | ❌ | 可用的效率工具列表（如Toggl、RescueTime、Zapier、Python） |
| `improvement_goal` | string | ❌ | 期望的改进目标（如"深度工作时间提升到每天4小时"） |
| `cycle_number` | number | ❌ | 当前是第几个改进周期（默认1），用于追踪迭代历史 |

## 📤 输出

```json
{
  "time_audit_report": {
    "total_tracked_hours": 112.5,
    "deep_work_hours": 18.5,
    "deep_work_ratio": 0.164,
    "top5_time_sinks": [
      {"activity": "刷社交媒体", "hours": 12.3, "ratio": 0.109},
      {"activity": "无效会议", "hours": 8.7, "ratio": 0.077},
      {"activity": "上下文切换", "hours": 6.2, "ratio": 0.055},
      {"activity": "邮件处理", "hours": 5.8, "ratio": 0.052},
      {"activity": "等待/排队", "hours": 4.1, "ratio": 0.036}
    ],
    "surprise_findings": ["你以为的'8小时工作'实际深度工作仅1.8小时"]
  },
  "root_cause_analysis": {
    "target_bottleneck": "刷社交媒体",
    "five_whys": [
      "为什么刷社交媒体？→ 无聊/需要休息",
      "为什么需要休息？→ 连续工作2小时后注意力下降",
      "为什么注意力下降？→ 没有设定休息节奏",
      "为什么没有休息节奏？→ 没有意识到需要主动休息",
      "为什么没有意识到？→ 把'不间断工作'误解为'高效'"
    ],
    "psychological_insight": "将'忙碌'等同于'高效'的认知偏差",
    "keystone_pattern": true
  },
  "improvement_experiment": {
    "name": "番茄工作法+社交媒体隔离",
    "duration_days": 7,
    "success_metrics": {
      "primary": "社交媒体使用时间减少50%",
      "secondary": "深度工作时间提升到3小时/天"
    }
  }
}
```

## 📋 执行步骤

### 阶段一：识别瓶颈（Identify Bottlenecks）

1. **数据收集** — 确保时间追踪工具（Toggl/RescueTime/手动记录）已稳定运行至少一周，收集至少100小时的数据样本
2. **数据聚合** — 将原始数据导出并可视化处理：
   - 生成时间分配饼图（深度工作 vs 辅助工作 vs 浪费）
   - 按活动类型排序，找出Top 5时间黑洞
3. **AI辅助瓶颈定位** — 使用以下提示词让AI分析时间数据：
   ```
   你是一位顶级的精益生产与时间管理专家。我将提供我过去一周的时间追踪日志。请你：
   1. 识别并量化Top 5的时间花费项
   2. 找出"等待"、"返工"、"上下文切换"等典型的"浪费"环节
   3. 基于"80/20法则"，提出最值得优化的一个时间黑洞
   数据如下：[粘贴时间数据]
   ```

### 阶段二：分析根源（Analyze Root Causes）

4. **聚焦核心问题** — 从Top 3瓶颈中，选择一个本周期内最想解决的问题
5. **"5 Why"分析法** — 针对该问题，连续追问至少5个"为什么"，直到触及根本原因：
   - 每一层追问必须基于上一层的答案
   - 区分"症状"与"根因"：症状是"刷社交媒体"，根因是"把忙碌等同于高效的认知偏差"
6. **AI辅助心理洞察** — 使用以下提示词进行深度分析：
   ```
   你是一位深刻的认知行为心理学家。我存在一个低效行为模式："[描述行为]"。
   我初步分析的原因是"[初步分析]"。请你运用认知心理学理论（如启动障碍、
   完美主义、信息焦虑、决策疲劳），对行为进行深度诊断，指出根本心理原因。
   ```

### 阶段三：实施优化（Implement Improvements）

7. **设计"效率实验"** — 针对根本原因，设计具体的、有时限的、可衡量的改进实验：
   - 实验周期：7天
   - 成功标准：必须量化（如"上下文切换次数减少50%"）
   - 实施步骤：不超过3步，每步都能在5分钟内完成
8. **AI辅助自动化方案** — 识别可自动化的重复任务：
   ```
   你是一位资深的自动化工程师。我有一个重复性手动任务："[描述任务]"。
   请设计自动化方案，包含：1. 建议工具 2. 核心代码框架 3. 预估节省时间
   ```
9. **执行实验** — 在下一周期严格执行，每天记录关键指标

### 阶段四：控制与固化（Control & Standardize）

10. **评估实验效果** — 实验结束后重新采集数据，对比实验前后关键指标
11. **成功则固化** — 将验证有效的方法纳入个人SOP或习惯清单
12. **失败则复盘** — 回到阶段二重新分析，或设计新的实验方案
13. **记录到知识库** — 将本次循环的经验教训记录到个人知识管理系统

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 时间追踪数据不足 | 先用100小时时间审计法收集一周数据，再进入分析阶段 |
| 找不到根本原因 | 换一个瓶颈重新分析，或请他人做"外部视角"诊断 |
| 实验方案太复杂 | 砍到只保留1个核心变量，确保实验可执行 |
| 实验失败 | 记录"此路不通"本身就是有价值的排除法数据 |
| 多个瓶颈并存 | 每个周期只聚焦1个瓶颈，不要贪多 |

## 🔗 关联技能

- [[uSkill-productivity-费曼技巧学习法]] — 用费曼技巧理解效率瓶颈的底层逻辑
- [[默读式会议]] — 飞阅会减少无效会议时间
- [[Palantir_竞品分析]] — 竞品分析方法可迁移为"效率对标分析"
- [[第二大脑知识管理]] — 将改进成果沉淀到第二大脑

## 📚 参考资料

- [[SOP-23-效率分析]] — 原始SOP文档
- 《奇特的一生》- 格拉宁 — 柳比歇夫时间统计法
- 《深度工作》- 卡尔·纽波特 — 深度工作理论
- 《精力管理》- 吉姆·洛尔 — 精力与效率的关系


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

> 来源：addyosmani/agent-ski

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
