---
name: uskill-creative-f73598
description: "让夜景摄影变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-夜景摄影.md"
  original_id: "SKL-6977"
  version: "3.0.0"
  trust: untrusted
---

# 夜景摄影

---

# 夜景摄影

> 低光环境拍摄

## 核心要点

三脚架必备，长曝光+低ISO

## 实操步骤

1. 理解参数含义
2. 在不同场景下练习
3. 对比不同设置的效果
4. 形成肌肉记忆

## 常见误区

- 过度依赖自动模式
- 忽视光线条件
- 后期过度处理

## 关联

- [[uSkill-creative-光圈]] · [[uSkill-creative-快门速度]] · [[uSkill-creative-iso感光度]]
- [[uSkill-creative-曝光三角]] · [[uSkill-creative-景深]]
- [[摄影后期处理]]

## 实践方法

1. **学习路径**：从uSkill-creative-夜景摄影的基础概念入手，逐步深入高级应用
2. **实践场景**：在真实项目中应用，记录经验与反思
3. **持续优化**：定期复盘，迭代改进方法论
## 应用场景

- **日常场景**：uSkill-creative-夜景摄影的基础应用
- **进阶场景**：uSkill-creative-夜景摄影的高阶用法

## 核心原则

1. 基础理论与概念框架
2. 实践中的关键决策点
3. 持续优化的反馈循环

## 进阶方向

- 深入研究底层原理
- 跨领域迁移应用
- 建立个人实践体系


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [摄影场景] for [拍摄者水平], with [创作优先级], leaning toward [器材/环境约束]."

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
| ""直接给一组参数就行了"" | "不知道用户场景就给参数，是赌博不是指导" |
| ""ISO 高一点没关系"" | "后期降噪损失细节，能前期解决就别留后期" |
| ""先拍一张试试看"" | "曝光三角的价值在于拍前就知道结果" |
| ""这个场景太简单了"" | "越简单越容易犯低级错误" |
| ""用户没问安全快门"" | "安全快门是糊片第一道防线，必须主动检查" |

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


**相关概念**：[[长曝光流水]]

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
你是一位夜景摄影专家，擅长低光环境拍摄、长时间曝光与城市光轨。请根据以下输入执行操作：
输入：[夜景拍摄场景（城市夜景/星空/光轨等）与器材条件]
要求：[给出曝光参数、三脚架稳定性建议、降噪策略与构图方案]
输出格式：[夜景拍摄方案（参数+器材+构图）+ 后期降噪方向]
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改


## 🎯 技能概述

> 本技能提供 创意与生活 领域的标准化操作流程，帮助用户高效完成相关任务。

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
