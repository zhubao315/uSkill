---
name: uskill-skill-golden-sample-1-9fff96
description: "把'执行晨间计划'的黄金标准固化下来：三件事必须绑定身份、继承昨日 P0、按精力匹配时间块。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/00-Agent-Evals/uSkill-skill-golden-sample-1-晨间计划生成.md"
  original_id: "SKL-7070"
  version: "2.0.0"
  trust: untrusted
---

# Golden Sample #1 — 晨间计划生成

description: |
  当用户需要生成每日晨间计划（黄金标准版）时使用此 Skill。
  触发词包括：'晨间计划'、'今日计划'、'今天干什么'、'安排今天'、'执行晨间计划'。
  即使用户没有说关键词，只要意图是制定当日优先级与日程，也应使用此 Skill。
  不适用于周/月级规划或纯日历同步。

---

# 🌅 uSkill-7070: 晨间计划生成（黄金样本）

## 🎯 目标

> 每日 06:30 自动生成当日三件事 + 日程安排，每个任务绑定身份维度，确保每天聚焦最重要的事。

**适用场景**：每日晨间计划制定、工作日安排、任务优先级排序、多身份（架构师/投资人/学习者/艺术家）平衡。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `yesterday_review` | `object` | ❌ | 昨日复盘（含 completed / missed） |
| `weekly_goals` | `array` | ✅ | 本周目标列表 |
| `fixed_items` | `array` | ❌ | 固定事项（会议等） |
| `energy_level` | `enum` | ❌ | high / normal / low |

---

## 📤 输出

```json
{
  "top_3": [
    {"task": "string", "priority": "P0|P1|P2", "est_min": "number", "identity": "架构师|投资人|学习者|艺术家"}
  ],
  "schedule": [{"time": "string", "task": "string", "duration_min": "number"}],
  "notes": ["string"]
}
```

---

## 🔄 执行流程

```
1. [P0 继承] → 检查昨日是否有未完成的 P0
   → 判断条件：yesterday_review.missed 含 P0 任务？
     → 是：继承为今日 P0，置顶
     → 否：从本周目标选最重要的

2. [身份绑定] → 为每件事分配身份维度
   → 规则：投资人→调仓/风控；学习者→读书/笔记；架构师→系统设计；艺术家→创作
   → 判断条件：三件事是否覆盖 ≥2 个身份？
     → 是：保留多样性
     → 否：提示用户补充缺失身份维度的任务

3. [精力匹配] → 根据精力分布安排时间块
   → 高精力(09:00-12:00) → P0
   → 中精力(14:00-17:00) → P1
   → 低精力(17:00后) → P2
   → 判断条件：energy_level = low？
     → 是：减少任务量，增加休息
     → 否：正常安排

4. [耗时预估] → 预估 ×1.2 缓冲
   → 判断条件：固定事项总时长 > 可用时间 50%？
     → 是：标注"时间紧张"，P2 延后
     → 否：正常插入

5. [输出计划] → 生成结构化计划，notes 记录继承/紧张标记
```

---

## 📝 Prompt 模板

### 标准生成 Prompt

```
你是晨间计划 Agent。请生成今日计划（黄金标准）。

【昨日复盘】{yesterday_review}
【本周目标】{weekly_goals}
【固定事项】{fixed_items}
【精力】{energy_level}

【计划规则】
1. 检查昨日 P0 未完成则继承为今日 P0
2. 每个任务必须绑定身份维度（架构师/投资人/学习者/艺术家）
3. 高精力时段→P0，低精力→P1/P2
4. 耗时预估 ×1.2 缓冲

【输出格式】
按标准 JSON 输出 top_3（含 identity）/ schedule / notes。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 本周目标缺失 | 基于昨日复盘推断 | 输出通用计划 + 警告 |
| 固定事项过多(>50%) | P2 延后 | 标注"时间紧张" |
| 昨日 P0 未完成 | 今日优先 | 标注"继承任务" |
| 身份维度单一 | 提示补充 | 仍输出但标注风险 |

---

## ✅ 质量自检

- [ ] top_3 恰好 3 件事且含 priority
- [ ] 每个任务含 identity 字段
- [ ] 昨日 P0 已继承检查
- [ ] 时间块匹配精力曲线
- [ ] notes 含继承/紧张标记

---

## 💡 使用示例

### 示例 1：黄金标准输出（原始样本）

**输入**：
```json
{ "trigger": "执行晨间计划" }
```

**输出**：
```json
{
  "top_3": [
    {"task": "执行科创50ETF减仓20%", "priority": "P0", "est_min": 30, "identity": "投资人"},
    {"task": "创建3篇读书笔记骨架", "priority": "P1", "est_min": 45, "identity": "学习者"},
    {"task": "设计投资风控Agent熔断规则", "priority": "P1", "est_min": 60, "identity": "架构师"}
  ],
  "schedule": [
    {"time": "09:30", "task": "执行科创50ETF减仓", "duration_min": 30},
    {"time": "10:00", "task": "创建读书笔记骨架", "duration_min": 45},
    {"time": "14:00", "task": "设计风控规则", "duration_min": 60}
  ],
  "notes": ["昨日P0未完成，今日继承"]
}
```

### 示例 2：时间紧张（边界）

**输入**：
```json
{
  "weekly_goals": ["交付项目A", "准备演讲"],
  "fixed_items": [
    {"time": "09:00", "task": "客户会议", "duration_min": 120},
    {"time": "14:00", "task": "项目评审", "duration_min": 180}
  ]
}
```

**输出**：
```json
{ "notes": ["今日固定事项占70%时间，P2任务可能需延后"] }
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常输入 | 3件事+身份绑定+日程 |
| 2 | 目标缺失 | 推断+警告 |
| 3 | 固定事项多 | 调整P2+紧张标记 |
| 4 | 昨日P0未完成 | 继承为今日P0 |
| 5 | 精力低 | 减负建议 |
| 6 | 单身份 | 提示补充多样性 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得违反平台规则与法律法规
2. 不得泄露用户隐私数据
3. 不得在未经验证时做不可逆财务决策

**软性约束（建议遵守）**：
1. 优先复用已验证方法论
2. 复杂决策记录理由供审计

**人工兜底点**：
- 财务/医疗/法律高风险时暂停等待确认
- 输入不足以支撑决策时转交人工

#### ✅ 校验验收规则

**格式校验**：
- [ ] JSON 结构完整
- [ ] 必填参数已填充
- [ ] identity 字段齐全

**内容校验**：
- [ ] 建议可操作、非泛泛
- [ ] 数据引用准确

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已识别

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：用户评分 < 7/10、发现新异常场景、领域重大变化

**版本升级触发**：
- 新增 ≥3 种异常 → minor
- 核心方法论根本变化 → major

---

---

*版本：v2.0 · 2026-07-08 升级（基于 Golden Sample #1 固化）*

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
