---
name: uskill-cognition-cognitive-dikw-knowledge-pyramid
description: "让cognitive dikw knowledge pyramid变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-dikw-knowledge-pyramid.md"
  original_id: "SKL-5137"
  version: "3.0.0"
  trust: untrusted
---

# cognitive dikw knowledge pyramid

# DIKW Knowledge Pyramid

## 🎯 目标

运用 DIKW（Data → Information → Knowledge → Wisdom）金字塔模型，将原始数据逐层提炼为可指导行动的智慧。本技能帮助使用者：

1. **分类** — 判断当前素材处于 D / I / K / W 哪一层级
2. **升级** — 提供从低层级向高层级转化的系统化方法
3. **决策** — 在每一层级匹配恰当的决策方式，避免层级错配
4. **纠偏** — 识别常见的认知层级谬误（如将数据误认为知识）

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `raw_material` | string / object | ✅ | 待分析的原始素材：数据集、报告、文档、经验记录等 |
| `current_level` | enum: `data` \| `information` \| `knowledge` \| `wisdom` | ❌ | 当前素材已达到的层级（默认自动判断） |
| `target_level` | enum: `information` \| `knowledge` \| `wisdom` | ❌ | 希望提升到的目标层级（默认向上提升一层） |
| `context` | string | ❌ | 业务/领域上下文，用于注入经验和背景 |
| `time_horizon` | string | ❌ | 决策时间视野：`immediate` / `short-term` / `long-term`，影响是否需要推向 Wisdom 层 |

---

## 📤 输出

```json
{
  "classification": {
    "current_level": "data | information | knowledge | wisdom",
    "evidence": "判断依据",
    "confidence": 0.0
  },
  "upgrade_path": {
    "from": "data",
    "to": "information",
    "steps": ["步骤1", "步骤2"],
    "estimated_effort": "low | medium | high"
  },
  "content": {
    "level": "information",
    "summary": "转化后的内容摘要",
    "answers": {
      "who": null,
      "what": null,
      "where": null,
      "when": null,
      "how": null,
      "why": null
    }
  },
  "decision_recommendation": {
    "appropriate_actions": ["行动建议1", "行动建议2"],
    "risks": ["风险提示"],
    "next_upgrade_needed": true
  }
}
```

---

## 📋 执行步骤

### 1. **层级识别 — 判断素材所在层级**

对输入素材进行特征匹配：

- **Data（数据）**：原始观察、量度、符号、数字、文字、图像。本身**无意义**，不回答任何问题。例如："本月收到 5000 个故障单"。
- **Information（信息）**：经组织和处理的数据，回答 **谁（Who）、什么（What）、哪里（Where）、何时（When）**。例如："35% 的呼叫是简单咨询，15% 是网络故障"。
- **Knowledge（知识）**：信息结合经验、上下文后的应用，回答 **如何（How）**。能支持建模与仿真。例如："根据历史模式，网络故障通常在季度末高发，应提前扩容"。
- **Wisdom（智慧）**：对未来的外推与判断，回答 **为什么（Why）**，涉及是非、对错、价值判断。人类独有，不可自动化。例如："应启动全组织的 IT 基础设施现代化计划，因为当前架构已无法支撑业务增长"。

输出判定结果与置信度。

### 2. **转化路径规划 — 确定升级方向**

根据 `target_level`（或默认向上一层），规划转化路径：

| 起始层 | 目标层 | 核心转化操作 | 关键问题 |
|--------|--------|-------------|---------|
| Data → Information | 组织、分类、关联、情境化 | "这些数据在说什么？" |
| Information → Knowledge | 应用经验、建立模型、推断因果 | "这些信息如何指导行动？" |
| Knowledge → Wisdom | 外推预测、价值判断、全局权衡 | "这样做对吗？长远影响是什么？" |

### 3. **执行转化 — Data → Information**

- 对原始数据进行**分类、排序、聚合**
- 建立数据之间的**关联关系**
- 回答 Who / What / Where / When
- 产出：有意义的报表、摘要、模式识别结果

### 4. **执行转化 — Information → Knowledge**

- 引入**领域经验和上下文**（`context` 参数）
- 建立信息之间的**因果链**和**作用机制**
- 回答 How — "如何利用这些信息采取行动？"
- 产出：可执行的流程、策略、模型

### 5. **执行转化 — Knowledge → Wisdom**

- 结合**时间视野**（`time_horizon`）进行前瞻推演
- 进行**价值判断**：什么是正确的？什么是最好的？
- 回答 Why — "为什么这样做？未来会怎样？"
- 产出：战略方向、原则性判断、长期规划

### 6. **生成决策建议 — 匹配层级的行动方案**

不同层级支持不同类型的决策：

| 层级 | 决策类型 | 适当行动 | 不当行动 |
|------|---------|---------|---------|
| Data | 不可决策 | 继续收集、组织数据 | 直接基于数据做业务决策 |
| Information | 描述性决策 | 报告现状、识别趋势 | 推断因果、制定战略 |
| Knowledge | 规范性决策 | 优化流程、制定策略 | 忽略不确定性做长期承诺 |
| Wisdom | 战略性决策 | 设定方向、价值取舍 | 用自动化替代人类判断 |

### 7. **异常检查 — 识别层级错配**

运行常见谬误检测（见异常处理表），确保输出不包含层级跳跃。

---

## ⚠️ 异常处理

| 异常场景 | 症状 | 处理方式 |
|---------|------|---------|
| **数据误认为知识** | 直接用原始统计数字指导决策（如"5000个故障单说明系统很差"） | 退回 Data 层，要求先转化为 Information |
| **信息误认为智慧** | 把报表结论当作战略方向（如"网络故障最多，所以要升级网络"） | 提醒需要结合经验和长期视角进一步提炼 |
| **跳过层级** | 试图从 Data 直接跳到 Wisdom | 强制要求逐层转化，每层必须完成才能进入下一层 |
| **上下文缺失** | Knowledge 层转化缺少领域经验 | 请求补充 `context` 参数或领域专家输入 |
| **过度自动化** | 试图用工具替代 Wisdom 层的人类判断 | 明确标注 Wisdom 层输出仅为辅助建议，最终判断需人类完成 |
| **层级回退** | 新数据涌入导致已有知识失效 | 重新从 Data 层开始分析，更新 Information 和 Knowledge |

---

## 📚 参考

- **原始来源**: Framework_DIKW（永久笔记，2022-06-23）
- **模型基础**: DIKW 金字塔模型（Russell Ackoff, 1989）
- **关键概念**:
  - 每一层赋予下一层**不存在的特质**（意义、理解、判断）
  - 理解深度随层级**递增**，考虑范围随之**扩大**
  - Wisdom 是**人类独有**的能力，不可被工具/自动化替代
- **典型应用领域**: IT 服务管理（故障分析）、商业智能、知识管理、学习系统设计


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

> 此区块定义执行后的验证标准，确

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
