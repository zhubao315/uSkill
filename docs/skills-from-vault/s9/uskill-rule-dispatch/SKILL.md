---
name: uskill-rule-dispatch
description: "让规则分发同步 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-rule-dispatch.md"
  original_id: "SKL-5315"
  version: "3.0.0"
  trust: untrusted
---

# 规则分发同步 Agent — 实施手册

description: |
  当用户需要将规则变更同步至所有相关 Agent 时使用此 Skill。
  触发词包括：'规则分发'、'规则同步'、'更新规则'。

---

# 📤 uSkill-315: 规则分发同步

## 🎯 目标

> 将规则变更同步至所有相关 Agent，确保全系统规则一致性。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `rule_change` | `object` | ✅ | 规则变更内容 |
| `affected_agents` | `array` | ❌ | 受影响 Agent 列表（自动识别） |

---

## 📤 输出

```json
{
  "affected_agents": [{"agent": "string", "sync_status": "synced|pending|failed"}],
  "pending_confirmations": ["string"]
}
```

---

## 🔄 执行流程

```
1. [变更解析] → 提取规则变更内容
   → 变更类型：新增/修改/删除
   → 影响范围：哪些Agent依赖此规则

2. [Agent识别] → 识别受影响的Agent
   → 基于规则依赖关系图
   → 判断条件：Agent是否使用此规则？
     → 是：加入受影响列表
     → 否：跳过

3. [通知生成] → 为每个Agent生成同步通知
   → 通知内容：变更详情+生效时间+回滚方案
   → 通知方式：推送/邮件/日志

4. [状态检查] → 确认所有Agent已接收
   → 判断条件：所有Agent状态=synced？
     → 是：输出"同步完成"
     → 否：标注未同步Agent+重试

5. [输出报告] → 分发报告 + 待确认列表
```

---

## 📝 Prompt 模板

### 标准分发 Prompt

```
你是规则分发Agent。请同步规则变更。

【规则变更】{rule_change}
【受影响Agent列表】{affected_agents}

【分发规则】
1. 识别所有依赖此规则的Agent
2. 生成同步通知（含变更详情+生效时间）
3. 推送通知并检查接收状态
4. 未接收的Agent进行重试

【输出格式】
按标准 JSON 输出，包含 affected_agents 和 pending_confirmations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| Agent离线 | 标注为pending+重试 | 等待上线后同步 |
| 规则冲突 | 标注冲突+人工确认 | 暂不生效 |
| 批量变更 | 批量处理 | 逐个同步 |

---

## 💡 使用示例

### 示例 1：正常分发

**输入**：
```json
{
  "rule_change": {"rule": "R1止损", "field": "threshold", "old": -30000, "new": -25000},
  "affected_agents": ["风控Agent", "投资组合监控"]
}
```

**输出**：
```json
{
  "affected_agents": [
    {"agent": "风控Agent", "sync_status": "synced"},
    {"agent": "投资组合监控", "sync_status": "synced"}
  ],
  "pending_confirmations": []
}
```

### 示例 2：Agent离线

**输入**：
```json
{
  "rule_change": {"rule": "R3集中度", "threshold": 0.25},
  "affected_agents": ["风控Agent", "午间资讯Agent"]
}
```

**输出**：
```json
{
  "affected_agents": [
    {"agent": "风控Agent", "sync_status": "synced"},
    {"agent": "午间资讯Agent", "sync_status": "pending"}
  ],
  "pending_confirmations": ["午间资讯Agent"]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常分发 | 全部synced |
| 2 | Agent离线 | pending+重试 |
| 3 | 规则冲突 | 标注冲突 |
| 4 | 无影响 | 空列表 |
| 5 | 批量变更 | 批量同步 |


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
   ↓         ↓        ↓          ↓      

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
