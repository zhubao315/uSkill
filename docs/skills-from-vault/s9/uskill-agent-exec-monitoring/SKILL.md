---
name: uskill-agent-exec-monitoring
description: "让 7 套循环工程的执行健康度从'看日志'变成实时可观测：合规率、异常分级、自愈建议一键呈现。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-exec-monitoring.md"
  original_id: "SKL-7123"
  version: "3.0.0"
  trust: untrusted
---

# Agent执行监控

description: |
  当用户需要监控 uLife OS 中 Agent 的执行合规率、成功率与异常模式时使用此 Skill。
  触发词包括：'Agent监控'、'执行监控'、'Agent健康'、'合规检查'、'循环工程体检'。
  即使用户只说'今天 Agent 跑得怎么样'，只要意图是评估执行健康，也应使用此 Skill。
  不适用于单次任务调试或模型微调。

---

# 🤖 uSkill-7123: Agent执行监控

## 🎯 目标

> 监控 uLife OS（1 每日循环 + 6 专项循环，共 7 套循环工程）下各 Agent 的执行合规率与准确率，识别异常模式（连续失败/超时/合规违规），分级预警并给出可执行的自愈建议，保障无人驾驶演练期系统稳定。

**适用场景**：每日执行日志分析、循环工程体检、异常检测、合规审计、自愈建议生成。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `execution_logs` | `array` | ✅ | Agent 执行日志（含 agent/status/duration/error） |
| `compliance_rules` | `array` | ❌ | 合规规则（默认系统内置） |
| `mesh_topology` | `object` | ❌ | 当前 Agent Mesh 依赖关系 |

---

## 📤 输出

```json
{
  "summary": "string",
  "stats": {"total": "number", "success_rate": "number", "compliance_rate": "number", "mesh_coverage": "number"},
  "anomalies": [{"agent": "string", "type": "string", "severity": "P0|P1|P2"}],
  "recommendations": [{"priority": "string", "action": "string"}]
}
```

---

## 🔄 执行流程

```
1. [日志解析] → 解析 execution_logs
   → 提取：agent、status、duration_ms、error
   → 判断条件：日志格式异常？
     → 是：跳过该条并标注"格式异常"
     → 否：进入统计

2. [统计计算] → 成功率 / 合规率 / Mesh覆盖率
   → 成功率 = 成功数/总数×100%
   → 合规率 = 合规数/总数×100%
   → 判断条件：成功率 < 80%？
     → 是：标注"执行异常"
     → 否：正常

3. [异常检测] → 识别模式
   → 连续失败：同 Agent 连续3次失败 → 🔴 P0
   → 超时：单次 > 阈值(如30s) → 🟡 P1
   → 合规违规：违反规则 → 🔴 P0
   → 判断条件：检测到 P0？
     → 是：立即生成预警 + 通知循环官
     → 否：进入分级

4. [分类评级] → P0/P1/P2
   → P0：连续失败、数据泄露、严重合规违规
   → P1：单次失败、性能降>20%
   → P2：偶发波动
   → THEN 输出分级报告

5. [建议生成] → 按异常类型给自愈建议
   → 连续失败 → 检查 Agent 配置/依赖/Mesh 连通
   → 超时 → 检查网络/模型响应
   → 合规违规 → 更新规则 + 重训
   → 判断条件：同类型异常周增 ≥3？
     → 是：升级 minor 版本规则
     → 否：常规建议
```

---

## 📝 Prompt 模板

### 标准监控 Prompt

```
你是 Agent执行监控 Agent。请检查今日 7 套循环工程的执行情况。

【执行日志】
{execution_logs}

【合规规则】
{compliance_rules}

【监控维度】
1. 成功率 = 成功数/总数×100%
2. 合规率 = 合规数/总数×100%
3. Mesh覆盖率 = 已监控 Agent / 总 Agent
4. 异常：超时、失败、违规

【分级标准】
- P0：连续3次失败、数据泄露、严重违规
- P1：单次失败、性能降>20%
- P2：偶发波动

【输出格式】
按标准 JSON 输出 stats / anomalies / recommendations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 日志缺失 | 警告+基于可用日志 | 仅统计可用部分 |
| 合规规则冲突 | 取最新版本 | 标注版本不一致 |
| Agent 离线 | 标"未响应"不计入成功率 | 触发重连探测 |
| 日志格式异常 | 尝试解析+标注 | 跳过不可解析条 |

---

## ✅ 质量自检

- [ ] stats 含 success_rate / compliance_rate / mesh_coverage
- [ ] 每个 P0 均生成预警
- [ ] 建议含具体动作（配置/网络/规则）
- [ ] 离线 Agent 未误计为失败
- [ ] summary 与明细一致

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
  "stats": {"total": 3, "success_rate": 100, "compliance_rate": 100, "mesh_coverage": 100},
  "anomalies": [],
  "recommendations": []
}
```

### 示例 2：连续超时（边界）

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
  "stats": {"total": 3, "success_rate": 0, "compliance_rate": 0, "mesh_coverage": 100},
  "anomalies": [{"agent": "风控Agent", "type": "consecutive_timeout", "severity": "P0"}],
  "recommendations": [{"priority": "P0", "action": "检查风控Agent网络与模型响应并重连 Mesh"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 全部成功 | 🟢 无异常 |
| 2 | 风控超时 | 🔴 P0 预警 |
| 3 | 合规违规 | 🔴 P0 预警 |
| 4 | 日志缺失 | 降级分析 |
| 5 | 多 Agent 异常 | 批量预警 |
| 6 | Agent 离线 | 未响应不误计 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得违反平台规则与法律法规
2. 不得泄露用户隐私数据
3. 不得在未验证时做不可逆操作（如删 Agent）

**软性约束（建议遵守）**：
1. 优先复用已验证方法论
2. 复杂决策记录理由供审计

**人工兜底点**：
- 当异常涉及财务/健康高风险 Agent 时暂停等待确认
- 当数据不足以判定时转交人工

#### ✅ 校验验收规则

**格式校验**：
- [ ] 输出结构完整
- [ ] 必填参数已填充

**内容校验**：
- [ ] 建议可操作
- [ ] 数据引用准确

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已识别

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：用户评分<7/10、发现新异常场景、Mesh 拓扑变更



> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
