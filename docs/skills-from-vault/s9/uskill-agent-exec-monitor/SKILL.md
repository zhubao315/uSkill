---
name: uskill-agent-exec-monitor
description: "让Agent执行监控 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-exec-monitor.md"
  original_id: "SKL-5309"
  version: "3.0.0"
  trust: untrusted
---

# Agent执行监控 Agent — 实施手册

description: |
  当用户需要监控 Agent 执行合规率与准确率时使用此 Skill。
  触发词包括：'Agent监控'、'执行监控'、'Agent健康'、'合规检查'。

---

# 🤖 uSkill-309: Agent执行监控

## 🎯 目标

> 监控 Agent 执行合规率与准确率，识别异常模式，保障系统稳定运行。

**适用场景**：每日 Agent 执行日志分析、异常检测、优化建议生成。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `execution_logs` | `array` | ✅ | Agent 执行日志列表 |
| `compliance_rules` | `array` | ❌ | 合规规则（默认系统内置） |

---

## 📤 输出

```json
{
  "summary": "string",
  "stats": {"total": "number", "success_rate": "number", "compliance_rate": "number"},
  "anomalies": [{"agent": "string", "type": "string", "severity": "string"}],
  "recommendations": [{"priority": "string", "action": "string"}]
}
```

---

## 🔄 执行流程

```
1. [日志解析] → 解析执行日志
   → 提取：Agent名称、执行状态、耗时、错误信息
   → IF 日志格式异常 → 跳过该条日志+标注

2. [统计计算] → 计算成功率和合规率
   → 成功率 = 成功数 / 总数 × 100%
   → 合规率 = 合规数 / 总数 × 100%
   → IF 成功率 < 80% → 标注为"执行异常"

3. [异常检测] → 识别异常模式
   → 连续失败：同一Agent连续3次失败 → 🔴 P0
   → 超时：单次执行 > 阈值 → 🟡 P1
   → 合规违规：违反规则 → 🔴 P0
   → IF 检测到P0异常 → 立即生成预警

4. [分类评级] → 按严重度分级
   → P0：连续失败、数据泄露、严重合规违规
   → P1：单次失败、性能下降>20%
   → P2：偶发异常、轻微波动
   → THEN 输出分级报告

5. [建议生成] → 基于异常类型生成优化建议
   → 连续失败 → 检查Agent配置/依赖
   → 超时 → 检查网络/模型响应
   → 合规违规 → 更新规则+培训

6. [输出报告] → 统计 + 异常 + 建议
```
1. 解析执行日志 → 统计成功率和合规率
2. 异常检测 → 识别失败模式、超时、违规操作
3. 分类评级 → 按严重度分为P0/P1/P2
4. 生成建议 → 基于异常类型生成优化建议
5. 输出报告 → 结构化监控报告
```

---

## 📝 Prompt 模板

### 标准监控 Prompt

```
你是Agent执行监控Agent。请检查今日Agent执行情况。

【执行日志】
{execution_logs}

【合规规则】
{compliance_rules}

【监控维度】
1. 执行成功率：成功数/总数×100%
2. 合规率：合规数/总数×100%
3. 异常检测：超时、失败、违规操作
4. 性能趋势：与昨日对比

【异常分类标准】
- P0（紧急）：连续3次失败、数据泄露、合规严重违规
- P1（重要）：单次失败、性能下降>20%、部分合规违规
- P2（一般）：偶发异常、性能轻微波动

【输出格式】
按标准 JSON 输出，包含 stats、anomalies、recommendations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 日志缺失 | 警告+基于可用日志分析 | 仅统计可用日志 |
| 合规规则冲突 | 取最新规则版本 | 标注规则版本不一致 |
| Agent离线 | 标注为"未响应" | 不计入成功率 |
| 日志格式异常 | 尝试解析+标注 | 跳过无法解析的日志 |

---

## 💡 使用示例

### 示例 1：正常执行日

**输入**：
```json
{
  "execution_logs": [
    {"agent": "风控Agent", "status": "success", "duration_ms": 1200},
    {"agent": "日记Agent", "status": "success", "duration_ms": 800},
    {"agent": "午间资讯", "status": "success", "duration_ms": 2000}
  ]
}
```

**输出**：
```json
{
  "stats": {"total": 3, "success_rate": 100, "compliance_rate": 100},
  "anomalies": [],
  "recommendations": []
}
```

### 示例 2：异常检测

**输入**：
```json
{
  "execution_logs": [
    {"agent": "风控Agent", "status": "timeout", "duration_ms": 30000},
    {"agent": "风控Agent", "status": "timeout", "duration_ms": 30000},
    {"agent": "风控Agent", "status": "timeout", "duration_ms": 30000}
  ]
}
```

**输出**：
```json
{
  "stats": {"total": 3, "success_rate": 0, "compliance_rate": 0},
  "anomalies": [{"agent": "风控Agent", "type": "consecutive_timeout", "severity": "P0"}],
  "recommendations": [{"priority": "P0", "action": "检查风控Agent网络连接和模型响应"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 全部成功 | 🟢 无异常 |
| 2 | 风控Agent超时 | 🔴 P0预警 |
| 3 | 合规违规 | 🟡 P1建议 |
| 4 | 日志缺失 | 降级分析 |
| 5 | 多Agent异常 | 批量预警 |


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

> "Reading this as: [健康任务] for [身体状况], with [生活方式],

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
