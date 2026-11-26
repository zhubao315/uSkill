---
name: uskill-v3-5233c0
description: "整合 addyosmani / taste-skill / claude-skills 三大框架精华，定义 uSkill v3 标准。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-v3-进化元技能.md"
  original_id: "SKL-V3-001"
  version: "3.0.0"
  trust: untrusted
---

# uSkill v3 进化元技能

# uSkill v3 进化元技能

> 整合三大 Agent Skills 框架精华，定义下一代 uSkill 标准

---

## 🎯 目标

将 addyosmani/agent-skills（流程纪律）、taste-skill（审美纪律）、claude-skills（规模纪律）的核心方法论融入 uSkill 体系，使每个技能都具备：

1. **反合理化能力**（from addyosmani）— 阻止 Agent 偷懒
2. **验证门禁能力**（from addyosmani + claude-skills）— 确保完成质量
3. **上下文感知能力**（from taste-skill）— 读懂用户真实意图
4. **状态机驱动能力**（from claude-skills）— 自治运行+预算控制

---

## 📐 uSkill v3 Frontmatter 标准

### v2（当前）→ v3（进化后）对比

```yaml
# v2 Frontmatter（当前）
---
title: "曝光三角"
name: "creative-曝光三角"
vibe: "把曝光三角讲成可执行的平衡游戏"
domain: "摄影创意"
id: "SKL-7207"
tags: [...]
---

# v3 Frontmatter（新标准）
---
title: "曝光三角"
name: "creative-曝光三角"
version: "3.0.0"
vibe: "把曝光三角讲成可执行的平衡游戏"
domain: "摄影创意"
id: "SKL-7207"

# 🆕 v3 新增字段
trust_level: "high"           # low/medium/high — 决定 Agent 自治程度
verification: "gated"         # none/gated/adversarial — 验证模式
anti_rationalization: true    # 是否启用反合理化表
context_inference: true       # 是否启用上下文推断（Design Read 模式）
budget:                       # 预算控制（from claude-skills agent-harness）
  max_retries: 3
  escalate_on_exhaust: true
tags: [...]
---
```

---


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


**相关概念**：[[三大Agent-Skills框架方法论对比]] · [[Agent-Skills标准化爆发深度分析]]

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
你是一位 Agent Skills 标准架构师，精通 addyosmani/agent-skills、taste-skill、claude-skills 三大框架。请对以下 uSkill 执行 v3 进化评估：

技能名称：[填入待评估的 uSkill 名称]
当前版本：[填入 v2/v3]
技能内容摘要：[填入核心功能描述]

要求：
1. 对照 v3 标准检查以下能力是否完备：
   - 反合理化表（Anti-Rationalization Table）
   - 门禁工作流（Gated Workflow）
   - 上下文推断（Context Read）
   - 三层边界（Three-Tier Boundaries）
   - 预算控制（Budget Control）
2. 识别缺失模块并给出优先级排序
3. 输出升级路线图（含预计工时）

输出格式：
- v3 合规评分：[X/5 模块]
- 缺失模块清单：[列表 + 优先级]
- 升级建议：[具体改造点 + 预计工时]
```

## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
