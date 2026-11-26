---
name: uskill-creative-ideation
description: "让创意发散变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-ideation.md"
  original_id: "SKL-5609"
  version: "3.0.0"
  trust: untrusted
---

# 创意发散

description: |
  当用户需要进行头脑风暴、产品创新、问题解决、创意策划时使用此 Skill。
  触发词包括：'创意'、'头脑风暴'、'创新'、'发散思维'、'SCAMPER'、
  '六顶思考帽'、'类比联想'。
  不适用于执行层面（使用其他专项技能）。当需要产生大量创意选项时优先使用。

---

# uSkill-609: 创意发散

## 🎯 目标

> 运用 SCAMPER、头脑风暴、六顶思考帽、类比联想等方法，产生大量创新方案。

**核心价值**：创意不是天赋，而是可训练的技能。系统化方法能持续产出好点子。

**适用场景**：
- 产品创新
- 问题解决
- 创意策划
- 头脑风暴
- 方案设计
- 创新工作坊

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `challenge` | `string` | ✅ | — | 需要解决的问题/挑战 |
| `constraints` | `array` | ❌ | `[]` | 限制条件 |
| `method` | `enum` | ❌ | `auto` | `auto` / `scamper` / `brainstorm` / `six_hats` / `analogy` |
| `team_size` | `number` | ❌ | `1` | 参与人数 |
| `time_limit` | `number` | ❌ | `30` | 时间限制（分钟） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话创意建议",
  "ideation_id": "IDE-YYYY-MMDD-NNN",

  "method_selection": {
    "primary": "string",
    "secondary": "string",
    "rationale": "string"
  },

  "ideas_generated": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "method_used": "string",
      "novelty_score": "number",
      "feasibility_score": "number",
      "combined_score": "number"
    }
  ],

  "scamper_output": {
    "substitute": ["string"],
    "combine": ["string"],
    "adapt": ["string"],
    "modify": ["string"],
    "put_to_other_use": ["string"],
    "eliminate": ["string"],
    "reverse": ["string"]
  },

  "six_hats_output": {
    "white": "string",
    "red": "string",
    "black": "string",
    "yellow": "string",
    "green": "string",
    "blue": "string"
  },

  "analogy_output": {
    "source_domain": "string",
    "analogies": [
      {
        "source": "string",
        "mapping": "string",
        "insight": "string"
      }
    ]
  },

  "evaluation": {
    "top_ideas": ["string"],
    "next_steps": ["string"],
    "risks": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 方法选择

- **输入**：`challenge` + `constraints` + `team_size`
- **动作**：
  1. 分析问题类型
  2. 选择最适合的方法
  3. 确定使用策略
- **输出**：`method_selection`
- **方法选择指南**：

| 方法 | 适用场景 | 优势 | 局限 |
|------|----------|------|------|
| SCAMPER | 产品改进 | 系统全面 | 需要经验 |
| 头脑风暴 | 开放式问题 | 快速产出 | 质量参差 |
| 六顶思考帽 | 复杂决策 | 多角度分析 | 耗时较长 |
| 类比联想 | 创新突破 | 跨界启发 | 需要知识储备 |

**分支条件**：
- 若 `team_size > 5` → 优先使用六顶思考帽
- 若 `team_size = 1` → 优先使用 SCAMPER 或类比联想
- 若 `time_limit < 15分钟` → 优先使用头脑风暴
- 若 `time_limit > 30分钟` → 综合使用多种方法
- 若问题为"改进现有产品" → 优先使用 SCAMPER
- 若问题为"创造全新方案" → 优先使用类比联想
- 若问题涉及"团队决策" → 优先使用六顶思考帽

### Step 2: SCAMPER 分析

- **输入**：`challenge` + `constraints`
- **动作**：
  1. 逐一应用 SCAMPER 七个维度
  2. 产生创意变体
  3. 筛选可行方案
- **输出**：`scamper_output`
- **SCAMPER 维度指南**：

| 维度 | 问题 | 示例 |
|------|------|------|
| Substitute | 可以替换什么？ | 材料、流程、人员 |
| Combine | 可以组合什么？ | 功能、服务、渠道 |
| Adapt | 可以借鉴什么？ | 其他行业、自然、历史 |
| Modify | 可以改变什么？ | 形状、大小、颜色、流程 |
| Put to other use | 可以用在其他地方吗？ | 新市场、新用户、新用途 |
| Eliminate | 可以去除什么？ | 步骤、功能、成本 |
| Reverse | 可以颠倒什么？ | 顺序、角色、方向 |

**分支条件**：
- 若约束条件多 → 重点关注 Substitute 和 Eliminate
- 若需要突破性创新 → 重点关注 Reverse 和 Put to other use
- 若需要渐进式改进 → 重点关注 Modify 和 Combine
- 若需要借鉴 → 重点关注 Adapt

### Step 3: 头脑风暴

- **输入**：`challenge` + `team_size`
- **动作**：
  1. 设定规则
  2. 快速产生想法
  3. 不批判，只产出
- **输出**：`ideas_generated`（部分）
- **头脑风暴规则**：

| 规则 | 说明 |
|------|------|
| 延迟判断 | 先产出，后评估 |
| 追求数量 | 数量产生质量 |
| 疯狂想法 | 鼓励大胆 |
| 组合改进 | 在他人想法上发展 |
| 一次一人 | 避免打断 |

**分支条件**：
- 若 `team_size = 1` → 使用个人头脑风暴变体
- 若 `team_size > 5` → 分组进行
- 若 `time_limit < 15分钟` → 聚焦核心问题
- 若 `time_limit > 30分钟` → 增加自由联想环节

### Step 4: 六顶思考帽分析

- **输入**：`challenge` + `constraints`
- **动作**：
  1. 逐一戴上六顶帽子
  2. 从不同角度分析
  3. 综合各角度见解
- **输出**：`six_hats_output`
- **六顶帽子指南**：

| 帽子 | 角色 | 问题 |
|------|------|------|
| 白帽 | 事实 | 有什么数据和事实？ |
| 红帽 | 直觉 | 我的直觉是什么？ |
| 黑帽 | 风险 | 有什么风险和问题？ |
| 黄帽 | 价值 | 有什么好处和价值？ |
| 绿帽 | 创意 | 有什么新想法？ |
| 蓝帽 | 控制 | 我们的思考过程如何？ |

**分支条件**：
- 若问题复杂 → 增加白帽和黑帽时间
- 若需要创新 → 增加绿帽时间
- 若团队情绪化 → 增加红帽时间
- 若需要决

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
