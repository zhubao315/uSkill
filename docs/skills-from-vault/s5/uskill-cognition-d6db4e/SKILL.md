---
name: uskill-cognition-d6db4e
description: "让跨模块联动从'想法'变成 uLife OS 里真正流动的数据与状态同步。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-跨模块联动.md"
  original_id: "SKL-7102"
  version: "3.0.0"
  trust: untrusted
---

# 跨模块联动

description: |
  当用户需要检查或打通 uLife OS 各循环模块之间的数据交换与状态同步时使用此 Skill。
  触发词包括：'跨模块联动'、'链接检查'、'知识图谱'、'模块同步'、'怎么让我的笔记连起来'。
  即使用户只是说'感觉各块是孤岛'，只要意图涉及模块间连接，也应使用此 Skill。
  不适用于企业级系统集成的技术对接（那是工程层面的事）。

---

# 🧠 uSkill-cognition-跨模块联动

> uLife OS 中各循环模块之间的数据交换和状态同步机制。联动的本质不是"建更多链接"，
> 而是让一个模块的变化能顺滑地触发相关模块的更新。

## 🎯 目标

> 检查并打通 uLife OS 模块间的数据联动，识别孤立词条，提升知识图谱连通性，让状态在循环间自动流转。

**联动维度（核心骨架）**：
- Daily Loop ↔ 专项循环：日度产出喂给周/月专项，专项结论回流日度
- 审计系统 ↔ Daily Loop：审计发现转化为次日行动项
- 财务 ↔ 知识蒸馏：投资标的与读书/洞察双向引用
- 身心 ↔ 关系：精力与训练状态影响关系互动质量

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `modules` | `array` | ❌ | 需检查的模块（默认全部核心循环） |
| `changed_doc` | `string` | ❌ | 本次发生变更的文档，用于增量联动 |

---

## 📤 输出

```json
{
  "link_density": [{"pair": "string", "links": "number", "target": "number"}],
  "orphan_entries": [{"entry": "string", "module": "string", "suggestion": "string"}],
  "pending_sync": [{"from": "string", "to": "string", "reason": "string"}],
  "recommendations": ["string"]
}
```

---

## 🔄 执行流程

```
1. [链接扫描] → 扫描各模块间 wikilink
   → 扫描范围：Daily Loop↔专项、审计↔Daily、财务↔知识蒸馏、身心↔关系
   → IF 模块目录不存在 → 跳过该模块 + 标注"缺失"
   → IF 给定 changed_doc → 仅做增量扫描，省去全局遍历

2. [密度计算] → 计算链接密度
   → 密度 = 链接数 / 词条数
   → 目标密度 ≥ 2
   → IF 密度 < 1 → 标注"链接严重不足"，优先处理

3. [孤立识别] → 识别孤立词条
   → 标准：外部链接数 = 0
   → IF 孤立率 > 10% → 标注"知识孤岛风险"
   → IF 孤立率 ≤ 5% → 标注"连通健康"

4. [状态同步检测] → 检查 changed_doc 的下游是否需更新
   → 判断条件：变更是否影响被引用方的语义？
     → 是：标注"需同步"，列出下游文档
     → 否：标注"无需同步"

5. [联动建议] → 生成链接/同步建议
   → 孤立词条 → 建议链接到相关词条
   → 密度低 → 建议增加交叉引用
   → THEN 输出具体链接建议（含目标词条名）

6. [质量自检] → 验证检查结果
   → IF 任一核心循环未被扫描 → 标注"覆盖不全"
   → THEN 输出链接密度 + 孤立列表 + 待同步项 + 建议
```

---

## 📝 Prompt 模板

### 标准联动 Prompt

```
你是跨模块联动 Agent。请检查 uLife OS 的数据联动与状态同步。

【检查模块】{modules}
【变更文档】{changed_doc}

【联动维度】
1. 链接密度：各模块间链接数 / 词条数（目标 ≥2）
2. 孤立词条：无外部链接的词条（孤立率目标 <5%）
3. 状态同步：变更文档的下游是否需更新

【输出格式】
按标准 JSON 输出，包含 link_density、orphan_entries、pending_sync、recommendations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 模块目录不存在 | 跳过该模块 | 仅检查存在的模块 |
| 链接格式异常 | 尝试解析 | 跳过无法解析的链接 |
| 无孤立词条 | 输出"链接健康" | — |
| 增量扫描无下游 | 输出"无需同步" | 仅返回密度快照 |
| 超大库（>5000 词条） | 分批扫描 | 按模块分片返回中间结果 |

---

## ✅ 质量自检

- [ ] 所有核心循环已扫描（或明确标注缺失）
- [ ] 链接密度计算口径一致（链接数/词条数）
- [ ] 孤立词条列表完整，含建议目标
- [ ] 状态同步项已识别下游文档
- [ ] 建议具体可执行，非"加强联动"空话

---

## 💡 使用示例

### 示例 1：正常联动检查

**输入**：检查 uSkill ↔ uWise 联动
**输出**：
```json
{
  "link_density": [{"pair": "uSkill→uWise", "links": 450, "target": 2.5}],
  "orphan_entries": [{"entry": "护城河分析框架", "module": "uWise", "suggestion": "链接到 uSkill-投资标的筛选"}],
  "pending_sync": [],
  "recommendations": ["增加 uSkill ↔ uRead 交叉引用"]
}
```

### 示例 2：增量同步（边界场景）

**输入**：
```json
{
  "changed_doc": "02-BUILD/23-uWise/词条/价值投资.md"
}
```
**输出**：
```json
{
  "pending_sync": [
    {"from": "价值投资.md", "to": "04-Investor/投资哲学/价值投资方法论.md", "reason": "定义更新，下游引用需核对"}
  ],
  "recommendations": ["核对下游文档中'价值投资'的定义表述是否同步"]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常联动 | 密度报告 + 建议 |
| 2 | 孤立词条 | 识别 + 链接建议 |
| 3 | 断链 | 修复建议 |
| 4 | 增量变更 | 识别下游待同步 |
| 5 | 密度过低 | 优化建议 |
| 6 | 模块缺失 | 跳过 + 标注 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得修改 `.obsidian/` 配置目录
2. 不得删除顶层架构目录（00-META ~ 09-REFERENCE）
3. 不得泄露用户隐私数据

**软性约束（建议遵守）**：
1. 优先复用已有 wikilink，避免新建重复词条
2. 联动建议应尊重用户既有的命名与分类体系

**人工兜底点**：
- 当自动合并会删除/改写用户原创内容时，**必须**转交人工确认
- 当涉及跨目录大规模重构时，**必须**先小范围验证

#### ✅ 校验验收规则

**格式校验**：
- [ ] 输出结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具体可执行
- [ ] 数据引用准确
- [ ] 方案考虑实际约束

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的孤立模式
  - 新增循环模块需纳入联动

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated

---

*版本：v2.0 · 2026-07-08 Gen3 升级*


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

### 信号读取
1. **任务类型

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
