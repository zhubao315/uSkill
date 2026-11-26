---
name: uskill-doc-sync
description: "让文档更新同步 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-doc-sync.md"
  original_id: "SKL-5314"
  version: "3.0.0"
  trust: untrusted
---

# 文档更新同步 Agent — 实施手册

description: |
  当用户需要跨模块同步更新关联文档时使用此 Skill。
  触发词包括：'文档同步'、'更新关联'、'链接检查'。

---

# 🔄 uSkill-314: 文档更新同步

## 🎯 目标

> 跨模块同步更新关联文档，确保知识库链接完整、内容一致。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `modified_doc` | `string` | ✅ | 被修改的文档路径 |
| `related_docs` | `array` | ❌ | 已知关联文档列表 |

---

## 📤 输出

```json
{
  "affected": [{"doc": "string", "impact_type": "string", "action": "string"}],
  "broken_links": [{"from": "string", "to": "string", "fix": "string"}]
}
```

---

## 🔄 执行流程

```
1. [链接扫描] → 提取修改文档中的所有 wikilink
   → 匹配模式：`[[链接目标]]` 或 `[[链接目标|显示文本]]`
   → 提取所有链接目标

2. [有效性检查] → 检查链接目标是否存在
   → 判断条件：链接目标文件是否存在？
     → 是：标记为有效
     → 否：标记为断链

3. [影响分析] → 识别受影响的关联文档
   → 反向扫描：哪些文档链接到了修改的文档？
   → 判断条件：修改是否影响链接的语义？
     → 是：标注为"需同步"
     → 否：标注为"无需同步"

4. [同步建议] → 生成具体同步操作
   → 断链：建议修复或删除
   → 语义变化：建议更新引用内容
   → 新增链接：建议创建目标文档

5. [输出报告] → 影响分析 + 断链列表 + 同步建议
```

---

## 📝 Prompt 模板

### 标准同步 Prompt

```
你是文档同步Agent。请检查并同步文档。

【修改文档】{modified_doc}
【关联文档列表】{related_docs}

【检查维度】
1. 链接有效性：所有 wikilink 是否指向存在的文件
2. 影响分析：修改是否影响关联文档的语义
3. 同步建议：需要同步的操作列表

【输出格式】
按标准 JSON 输出，包含 affected 和 broken_links。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 关联文档列表缺失 | 自动扫描反向链接 | 基于 wikilink 扫描 |
| 链接格式异常 | 尝试解析+标注 | 跳过无法解析的链接 |
| 无关联文档 | 输出"无影响" | — |

---

## 💡 使用示例

### 示例 1：正常同步

**输入**：
```json
{
  "modified_doc": "02-BUILD/23-uWise/词条/价值投资.md",
  "related_docs": ["02-BUILD/23-uWise/词条/护城河.md", "04-Investor/投资哲学/价值投资方法论.md"]
}
```

**输出**：
```json
{
  "affected": [
    {"doc": "护城河.md", "impact_type": "定义引用", "action": "检查引用是否仍准确"},
    {"doc": "投资哲学/价值投资方法论.md", "impact_type": "框架引用", "action": "无需同步"}
  ],
  "broken_links": []
}
```

### 示例 2：断链检测

**输入**：
```json
{
  "modified_doc": "02-BUILD/23-uWise/词条/刻意练习.md"
}
```

**输出**：
```json
{
  "affected": [],
  "broken_links": [{"from": "刻意练习.md", "to": "《刻意练习》-安德斯·艾利克森", "fix": "检查目标文件是否存在"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常同步 | 识别受影响文档 |
| 2 | 断链 | 输出修复建议 |
| 3 | 无关联 | 无影响 |
| 4 | 新增链接 | 建议创建目标文档 |
| 5 | 删除链接 | 建议清理引用 |


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
---

*版本：v2.0 · 2026-06-29 升级*


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
- [ ] 输出 Con

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
