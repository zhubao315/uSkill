---
name: uskill-code-review
description: "让代码审查 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-code-review.md"
  original_id: "SKL-5312"
  version: "3.0.0"
  trust: untrusted
---

# 代码审查 Agent — 实施手册

description: |
  当用户需要审查代码质量时使用此 Skill。
  触发词包括：'代码审查'、'code review'、'代码检查'、'CR'。

---

# 🔍 uSkill-312: 代码审查

## 🎯 目标

> 基于 CONVENTIONS 审查代码规范、潜在bug、性能问题，输出结构化审查报告。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `code` | `string` | ✅ | 待审查代码 |
| `language` | `string` | ❌ | 编程语言（自动检测） |
| `conventions` | `string` | ❌ | 审查规则文件路径 |

---

## 📤 输出

```json
{
  "score": "number (0-10)",
  "issues": [{"severity": "critical|major|minor", "line": "number", "description": "string", "suggestion": "string"}],
  "verdict": "approve|request_changes|needs_discussion"
}
```

---

## 🔄 执行流程

```
1. [代码解析] → 提取结构、函数、类、导入
   → 识别编程语言
   → 提取代码复杂度指标

2. [规范检查] → 基于 CONVENTIONS 检查
   → 命名规范（变量/函数/类）
   → 格式规范（缩进/空格/换行）
   → 注释规范（函数注释/复杂逻辑注释）

3. [缺陷检测] → 识别潜在问题
   → 安全漏洞（SQL注入、XSS、硬编码密钥）
   → 逻辑错误（空指针、越界、类型错误）
   → 资源泄漏（未关闭连接、内存泄漏）

4. [性能分析] → 评估性能风险
   → 时间复杂度（O(n²)以上的循环）
   → 空间复杂度（大数组/频繁创建对象）
   → I/O效率（不必要的数据库查询）

5. [测试覆盖] → 检查测试用例
   → 是否有对应测试
   → 边界条件是否覆盖

6. [综合评分] → 0-10分 + 审查意见
   → 9-10：优秀，可直接合并
   → 7-8：良好，小修改后合并
   → 5-6：一般，需修改后重新审查
   → <5：较差，需大幅重构
```

---

## 📝 Prompt 模板

### 标准审查 Prompt

```
你是代码审查Agent。请审查以下代码。

【代码】
{code}

【编程语言】{language}

【审查规则】{conventions}

【审查维度】
1. 规范检查：命名、格式、注释
2. 缺陷检测：bug、安全漏洞、逻辑错误
3. 性能分析：复杂度、资源泄漏
4. 测试覆盖：测试用例完整性

【严重度分级】
- critical：安全漏洞、数据丢失风险
- major：逻辑错误、性能问题
- minor：规范不符、建议改进

【输出格式】
按标准 JSON 输出，包含 score、issues、verdict。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 代码过长(>500行) | 分段审查 | 每段独立评分后取平均 |
| 未知语言 | 通用规范检查 | 仅检查格式和注释 |
| 无法解析 | 输出"代码格式异常" | 跳过该文件 |

---

## 💡 使用示例

### 示例 1：优质代码

**输入**：
```python
def calculate_avg(numbers: list[float]) -> float:
    """计算列表平均值"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
```

**输出**：
```json
{
  "score": 9,
  "issues": [],
  "verdict": "approve"
}
```

### 示例 2：有安全漏洞

**输入**：
```python
def get_user(name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return db.execute(query)
```

**输出**：
```json
{
  "score": 3,
  "issues": [
    {"severity": "critical", "line": 2, "description": "SQL注入漏洞：直接拼接用户输入", "suggestion": "使用参数化查询"}
  ],
  "verdict": "request_changes"
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 优质代码 | score≥8, approve |
| 2 | 有安全漏洞 | critical issue |
| 3 | 性能问题 | major issue |
| 4 | 代码过长 | 分段审查 |
| 5 | 未知语言 | 通用检查 |

---

*版本：v2.0 · 2026-06-29 升级*



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

## 关联

- [[uSkill]] — 技能总览


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
-

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
