---
name: uskill-skill-optimize
description: "让SkillOpt技能优化 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-skill-optimize.md"
  original_id: "SKL-5320"
  version: "3.0.0"
  trust: untrusted
---

# SkillOpt技能优化 Agent — 实施手册

description: |
  当用户需要通过闭环优化 Skill 文档时使用此 Skill。
  触发词包括：'Skill优化'、'技能优化'、'Skill改进'、'执行失败分析'。

---

# 🔧 uSkill-320: [[SkillOpt技能优化]]

## 🎯 目标

> 通过分析执行失败案例，识别 Skill 文档缺陷，生成优化建议并更新。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `skill_doc` | `string` | ✅ | 待优化的 Skill 文档路径 |
| `execution_feedback` | `string` | ✅ | 执行反馈（成功/失败/部分成功） |
| `failure_cases` | `array` | ❌ | 失败案例详情 |

---

## 📤 输出

```json
{
  "root_cause": "string",
  "issues": [{"type": "string", "severity": "string", "description": "string"}],
  "optimizations": [{"section": "string", "change": "string", "reason": "string"}]
}
```

---

## 🔄 执行流程

```
1. [失败分析] → 分析执行失败原因
   → 定义不清：概念模糊导致理解偏差
   → 流程缺失：步骤不完整导致执行遗漏
   → 边界遗漏：异常情况未覆盖
   → Prompt缺陷：Prompt模板不准确

2. [缺陷定位] → 定位Skill文档中的具体缺陷
   → 检查：输入Schema是否完整？
   → 检查：执行流程是否有分支？
   → 检查：异常处理是否覆盖？
   → 检查：Self-Play测试是否充分？

3. [优化建议] → 生成针对性优化建议
   → 规则：建议必须具体到文档的哪个section
   → 规则：建议应说明修改原因

4. [文档更新] → 输出更新后的Skill内容
   → 保持原有结构
   → 补充缺失部分
   → 修正错误部分

5. [验证建议] → 建议验证方式
   → Self-Play测试用例
   → 人工审查checklist
```

---

## 📝 Prompt 模板

### 标准优化 Prompt

```
你是Skill优化Agent。请优化以下Skill。

【Skill文档】{skill_doc}
【执行反馈】{execution_feedback}
【失败案例】{failure_cases}

【优化维度】
1. 定义清晰度：概念是否精确？
2. 流程完整性：步骤是否有遗漏？
3. 边界覆盖：异常是否处理？
4. Prompt准确性：模板是否有效？

【输出格式】
按标准 JSON 输出，包含 root_cause、issues、optimizations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 反馈信息不足 | 请求补充 | 基于文档本身分析 |
| 无法定位缺陷 | 标注"需进一步调查" | 输出通用改进建议 |
| 多个问题 | 按严重度排序 | 优先修复P0问题 |

---

## 💡 使用示例

### 示例 1：定义不清

**输入**：
```json
{
  "skill_doc": "风控Agent",
  "execution_feedback": "风控Agent执行超时",
  "failure_cases": ["连续3次超时30s"]
}
```

**输出**：
```json
{
  "root_cause": "规则匹配逻辑过于复杂，每次执行需遍历全部规则",
  "issues": [
    {"type": "流程缺陷", "severity": "major", "description": "执行流程缺少超时处理机制"}
  ],
  "optimizations": [
    {"section": "执行流程", "change": "增加超时判断：单次执行>10s则中断", "reason": "避免无限等待"},
    {"section": "异常处理", "change": "增加超时异常处理：记录日志+降级为简单规则", "reason": "保证系统可用性"}
  ]
}
```

### 示例 2：边界遗漏

**输入**：
```json
{
  "skill_doc": "邮件处理Agent",
  "execution_feedback": "未识别法律邮件",
  "failure_cases": ["合同邮件被分类为P2"]
}
```

**输出**：
```json
{
  "root_cause": "缺少法律/合同类邮件的识别规则",
  "issues": [
    {"type": "边界遗漏", "severity": "major", "description": "分类规则未覆盖法律类邮件"}
  ],
  "optimizations": [
    {"section": "执行流程", "change": "步骤2增加：检查是否涉及法律/合同 → 强制P0+人工处理", "reason": "法律邮件必须人工处理"}
  ]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 定义不清 | 重写定义 |
| 2 | 流程缺失 | 补充步骤 |
| 3 | 边界遗漏 | 补充异常处理 |
| 4 | 无问题 | "质量达标"结论 |
| 5 | 多个问题 | 优先级排序 |


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

> "Reading this as: [任务类型] for [用户水平], with [约束条件], leaning toward [方法/工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

---

## 🛡️ Three-Tier B

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
