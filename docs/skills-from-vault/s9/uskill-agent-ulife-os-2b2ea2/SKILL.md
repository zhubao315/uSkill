---
name: uskill-agent-ulife-os-2b2ea2
description: "让uLife OS 主入口变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-ulife-os-主入口.md"
  original_id: "SKL-7007"
  version: "3.0.0"
  trust: untrusted
---

# uLife OS 主入口

# uLife OS 主入口

> 详细版本请查看 → [[uLife OS v5.0-Operator]]

## 快速入口

- [[Home|宝哥上下文工作台]]
- [[uSkill-agent-循环工程统一调度入口|循环工程调度中枢]]
- [[uSkill-agent-定时自动化可靠性协议|定时 Agent 可靠性协议（八步 + 磁盘文件契约）]]
- [[诊断分析报告|健康度诊断]]

## 实践方法

1. **学习路径**：从uSkill-agent-ulife-os-主入口的基础概念入手，逐步深入高级应用
2. **实践场景**：在真实项目中应用，记录经验与反思
3. **持续优化**：定期复盘，迭代改进方法论

## 关联
- [[∑ uSkill]]

## 核心原则

1. 基础理论与概念框架
2. 实践中的关键决策点
3. 持续优化的反馈循环

## 常见误区

- 误区一：过度简化uSkill-agent-ulife-os-主入口的适用场景
- 误区二：忽视前提条件和边界情况
- 误区三：缺乏数据驱动的验证机制

## 进阶方向

- 深入研究底层原理
- 跨领域迁移应用
- 建立个人实践体系


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

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
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

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

---


## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位uLife OS知识管理系统导航专家。请根据以下用户需求进行系统路由：
输入：[用户的问题或需求描述]
要求：1) 判断用户需求属于哪个子系统（循环工程/晨间计划/五维Agent/知识孪生/健康/投资/学习/创意）；2) 路由到对应的uSkill智能体；3) 如果需求跨多个子系统，给出执行顺序建议；4) 输出快速入口链接和下一步操作指引
输出格式：路由判断+推荐入口+操作指引
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改


## 🎯 技能概述

> 本技能提供 通用 领域的标准化操作流程，帮助用户高效完成相关任务。

**核心价值**：将复杂操作标准化为可重复执行的步骤，降低出错率，提升效率。

**适用场景**：
1. 日常操作执行
2. 新手快速上手
3. 质量一致性保证

## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
