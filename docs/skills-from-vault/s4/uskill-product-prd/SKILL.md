---
name: uskill-product-prd
description: "PRD 不是写给产品经理看的——是写给工程师和设计师执行的。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S4-商业运营与增长/uSkill-product-prd.md"
  original_id: "SKL-6410"
  version: "3.0.0"
  trust: untrusted
---

# 产品需求文档PRD

description: |
  当用户需要撰写产品需求文档、定义功能需求、进行需求评审时使用此 Skill。
  触发词：'PRD'、'产品需求'、'需求文档'、'用户故事'、'验收标准'。

# 产品需求文档 PRD

## 🎯 目标

> 撰写无歧义、可执行、有验收标准的产品需求文档。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `feature_name` | string | ✅ | — | 功能名称 |
| `user_problem` | string | ✅ | — | 用户问题描述 |
| `priority` | enum | ❌ | `"P1"` | 优先级 |
| `scope` | enum | ❌ | `"mvp"` | 范围：`mvp` / `full` / `phase1` |

## 📤 输出

```json
{
  "prd": {
    "background": "string — 背景和目标",
    "user_stories": [{"actor": "string", "action": "string", "benefit": "string"}],
    "functional_requirements": [{"id": "string", "requirement": "string", "acceptance": "string"}],
    "non_functional": ["string"],
    "edge_cases": ["string"],
    "metrics": "string — 成功指标"
  }
}
```

## 📋 执行步骤

### Step 1: 问题定义
1. **用户故事** — 「作为[角色]，我想要[功能]，以便[价值]」
2. **成功指标** — 用数字定义成功
3. **范围边界** — 明确做什么/不做什么
4. **检查点**：✅ 用户问题是否清晰？成功指标是否可量化？

### Step 2: 需求细化
1. **功能需求** — 每个需求有唯一 ID 和验收标准
2. **非功能需求** — 性能/安全/可用性要求
3. **边界情况** — 异常输入/极端场景
4. **依赖关系** — 与其他功能/系统的依赖
5. **检查点**：✅ 每个需求是否有验收标准？是否考虑了边界？

### Step 3: 技术可行性
1. **技术预研** — 关键技术方案是否可行
2. **工期估算** — 开发团队的工时估算
3. **风险评估** — 技术风险和缓解方案
4. **检查点**：✅ 技术可行性是否评估？工期是否合理？

### Step 4: 评审与确认
1. **跨部门评审** — 产品/设计/开发/测试共同评审
2. **问题记录** — 评审中发现的问题和修改
3. **签字确认** — 各方确认需求冻结
4. **检查点**：✅ 是否经过跨部门评审？需求是否已冻结？

## 💬 沟通风格
- **无歧义**：每句话只有一种理解
- **可测试**：每个需求都能写出测试用例
- **具体化**：不说「性能好」，说「P99 <200ms」

## 📝 自检清单
- [ ] 每个需求是否有验收标准？
- [ ] 是否考虑了边界和异常情况？
- [ ] 技术可行性是否已评估？
- [ ] 是否经过跨部门评审？
- [ ] 成功指标是否可量化？

---


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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Product Manager + Sprint Prioritizer |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务] for [业务阶段], with [资源约束], leaning toward [策略框架/执行路径]."

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
| ""先做再说"" | "方向错了，执行力越强死得越快" |
| ""用户说想要这个"" | "用户说的是解决方案，不是需求本身" |
| ""竞品都在做"" | "竞品犯错不意味着你也应该犯" |
| ""这个市场很大"" | "大市场≠你能切到的市场" |

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
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功


**相关概念**：[[需求分析]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
