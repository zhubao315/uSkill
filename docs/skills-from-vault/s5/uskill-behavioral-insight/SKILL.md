---
name: uskill-behavioral-insight
description: "人的行为不理性——但不理性是有规律的。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-behavioral-insight.md"
  original_id: "SKL-6306"
  version: "3.0.0"
  trust: untrusted
---

# 行为洞察分析

description: |
  当用户需要分析用户/用户行为模式、设计行为干预方案、利用认知偏差优化体验时使用此 Skill。
  触发词：'行为分析'、'认知偏差'、'行为设计'、'助推'、'nudge'、'behavioral'。

# 行为洞察分析

## 🎯 目标

> 基于行为科学原理理解用户行为，设计有效的行为干预方案。

**核心价值**：用户不是「不理性」，而是遵循可预测的认知模式。本 Skill 将行为科学原理转化为可执行的设计/营销/管理策略。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `behavior_question` | string | ✅ | — | 需要解释的行为现象 |
| `context` | string | ❌ | — | 行为发生的场景 |
| `intervention_goal` | enum | ❌ | `"increase"` | 干预目标：`increase`（增加）/ `decrease`（减少）/ `change`（改变） |
| `bias_focus` | array | ❌ | — | 关注的认知偏差（如有） |

## 📤 输出

```json
{
  "behavior_analysis": {
    "observed_behavior": "string — 观察到的行为",
    "likely_biases": [{"bias": "string", "explanation": "string", "evidence": "string"}],
    "underlying_drivers": ["string — 行为背后的驱动力"]
  },
  "intervention_design": {
    "strategy": "string — 干预策略",
    "principles_used": ["string — 使用的行为科学原理"],
    "implementation": ["string — 实施步骤"],
    "measurement": "string — 效果衡量方案"
  },
  "ethical_notes": "string — 伦理考量"
}
```

## 📋 执行步骤

### Step 1: 行为诊断
1. **行为观察** — 记录实际行为（不是推测）
2. **偏差识别** — 识别涉及的认知偏差
3. **驱动力分析** — 动机/能力/触发因素（Fogg 行为模型）
4. **检查点**：✅ 是否基于观察而非假设？偏差识别是否有证据？

### Step 2: 干预设计
1. **策略选择** — 利用偏差的方向（正面利用 vs 对抗）
2. **最小干预** — 用最小的改变达到目标
3. **Fogg 模型** — 提升动机/降低门槛/增加触发
4. **检查点**：✅ 干预是否最小化？是否基于行为科学原理？

### Step 3: 效果验证
1. **A/B 测试** — 对照组 vs 干预组
2. **行为数据** — 追踪实际行为变化
3. **长期效果** — 确认不是短期效应
4. **检查点**：✅ 是否有 A/B 测试？效果是否可持续？

### Step 4: 伦理评估
1. **透明度** — 干预是否透明？
2. **选择自由** — 是否保留了用户的选择权？
3. **利益对齐** — 干预是否同时惠及用户和目标？
4. **检查点**：✅ 干预是否符合伦理？是否保留了用户选择权？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 干预无效 | A/B 测试无显著差异 | 重新诊断行为驱动力 |
| 伦理争议 | 被质疑操纵用户 | 重新评估伦理合规性 |
| 效果衰减 | 短期有效长期失效 | 设计新的触发机制 |

## 💬 沟通风格

- **科学导向**：每个偏差引用行为科学原理
- **实证驱动**：用数据验证而非理论推演
- **伦理透明**：明确说明干预的伦理边界

## 📝 自检清单

- [ ] 行为诊断是否基于观察？
- [ ] 是否识别了涉及的认知偏差？
- [ ] 干预方案是否基于行为科学原理？
- [ ] 是否有 A/B 测试验证效果？
- [ ] 是否评估了伦理合规性？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Behavioral Nudge Engine + Organizational Psychologist |


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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

### Phase 1: DIS

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
