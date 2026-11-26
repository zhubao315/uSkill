---
name: uskill-agent-reference-bridge-scheme
description: "uSkill 引用桥接方案"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-reference-bridge-scheme.md"
  original_id: ""
  version: "3.0"
  trust: untrusted
---

# uSkill 引用桥接方案

# uSkill 引用桥接方案

> 解决 71%（485/674）uSkill 零入链的结构性问题

---

## 问题诊断

| 指标 | 数值 |
|------|------|
| uSkill 总数 | 674 |
| 零入链（孤立） | 485（71%） |
| 有入链 | 189（28%） |
| 高价值孤立（>5KB） | 327 |

**核心问题**：uSkill 被创建后，没有被日记、项目笔记、概念笔记引用，变成了「写了但没人看」的知识孤岛。

---

## 桥接策略

### 策略一：日记织链（最高效）

**规则**：每次写日记时，如果内容涉及某个领域，末尾自动织入该领域最相关的 uSkill wikilink。

**执行方式**：
1. 写完日记正文后，扫描内容关键词
2. 匹配 uSkill 名称或内容关键词
3. 在 `## 🔗 相关` 区域添加 1-3 个 uSkill 链接

**示例**：
```
## 🔗 相关
- [[肖雪]]
- [[跑步训练计划]]
- [[uSkill-health-lifestyle-plan-outdoor-expedition]]  ← 新增桥接
```

### 策略二：概念笔记挂载（中等效率）

**规则**：01-BRAIN 概念笔记的「知识关联」区域，挂载相关 uSkill 作为「实践方法」。

**执行方式**：
1. 概念笔记已有上游/下游关联
2. 新增「实践方法」层级，指向具体 uSkill
3. 每个概念笔记挂载 1-2 个最相关的 uSkill

**示例**：
```markdown
## 知识关联
- **上游概念**：[[内心堡垒]]
- **实践方法**：[[uSkill-thinking-first-principles]] ← 新增桥接
```

### 策略三：项目笔记嵌入（低频但高价值）

**规则**：项目笔记中涉及具体 SOP/工具时，嵌入对应 uSkill 的引用。

---

## TOP 20 高价值孤立 uSkill 优先桥接清单

| # | uSkill | 大小 | 建议桥接至 |
|---|--------|------|-----------|
| 1 | `uSkill-agent-循环工程统一调度入口` | 40KB | `[[循环工程]]` 概念笔记 |
| 2 | `SOP-01-架构师-系统设计分析` | 33KB | `[[3-Architect]]` 项目笔记 |
| 3 | `SOP-13-对抗性投研系统` | 24KB | `[[我的交易系统]]` |
| 4 | `agency-agents-全量映射索引` | 20KB | `[[AGENTS]]` |
| 5 | `uSkill-health-lifestyle-plan-outdoor-expedition` | 19KB | `[[∑ 健身跑者]]` |
| 6 | `uSkill-thinking-first-principles` | 19KB | `[[第一性原理思考框架]]` |
| 7 | `uSkill-thinking-analogical` | 18KB | `[[类比思维]]` |
| 8 | `uSkill-thinking-opportunity-cost` | 17KB | `[[机会成本]]` |
| 9 | `uSkill-agent-每日领域共生循环系统` | 17KB | `[[循环工程]]` |
| 10 | `SOP-05-大规模代码AI开发工作流` | 17KB | `[[3-Architect]]` |
| 11 | `uSkill-cognitive-decision-reasoning` | 17KB | `[[决策框架]]` |
| 12 | `uSkill-health-circadian-rhythm-optimization` | 17KB | `[[睡眠与恢复策略]]` |
| 13 | `uSkill-agent-全局审计专项循环` | 16KB | `[[循环工程]]` |
| 14 | `uSkill-cognitive-metacognition` | 16KB | `[[元认知]]` |
| 15 | `uSkill-agent-认知偏差对抗协议` | 16KB | `[[认知偏差]]` |
| 16 | `uSkill-health-outdoor-sport-planning` | 15KB | `[[∑ 健身跑者]]` |
| 17 | `uSkill-cognition-cognitive-poverty-trap-diagnosis` | 15KB | `[[认知科学]]` |
| 18 | `uSkill-defense-information-pollution` | 15KB | `[[信息污染]]` |
| 19 | `uSkill-cognition-抽象思维...` | 15KB | `[[抽象思维]]` |
| 20 | `uSkill-agent-twin-mcp-输入契约` | 17KB | `[[知识孪生]]` |

---

## 自动化脚本草案

```python
# bridge_underscore_skills.py — 扫描日记并自动织入 uSkill 链接
# 输入：当日日记路径
# 逻辑：
#   1. 读取日记正文，提取关键词
#   2. 在 uSkill 目录中 grep 匹配关键词的文件
#   3. 选取相关度最高的 1-3 个
#   4. 在日记末尾 ## 🔗 相关 区域添加 wikilink
# 输出：修改后的日记文件
```

---

## 执行节奏

| 阶段 | 时间 | 动作 |
|------|------|------|
| 第一批 | 本周 | 手动桥接 TOP 20 高价值 uSkill |
| 第二批 | 下周 | 运行自动化脚本，批量桥接剩余 305 篇 |
| 持续 | 每日 | 写日记时自动织入 1-2 个 uSkill 链接 |
| 验证 | 每月 | 运行 link_checker 检查孤立率变化 |

## 相关

- [[uSkill-agent-循环工程统一调度入口]]
- [[循环工程]]
- [[优化任务清单]]


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
-

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
