---
name: uskill-existential-risk-scan
description: "让存在性风险扫描 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-existential-risk-scan.md"
  original_id: "SKL-5319"
  version: "3.0.0"
  trust: untrusted
---

# 存在性风险扫描 Agent — 实施手册

description: |
  当用户需要识别可能危及系统存续的尾部风险时使用此 Skill。
  触发词包括：'存在性风险'、'尾部风险'、'黑天鹅'、'系统安全'。

---

# ☠️ uSkill-319: 存在性风险扫描

## 🎯 目标

> 识别低概率高影响事件，评估最坏情景，生成应急预案。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `system` | `string` | ✅ | 系统描述 |
| `status` | `object` | ✅ | 当前状态数据 |

---

## 📤 输出

```json
{
  "risks": [{"risk": "string", "probability": "string", "impact": "string", "mitigation": "string"}],
  "worst_case": "string",
  "defense_measures": ["string"],
  "early_warning_signals": ["string"]
}
```

---

## 🔄 执行流程

```
1. [风险扫描] → 识别系统各层面风险
   → 技术风险：数据丢失、系统崩溃、安全漏洞
   → 运营风险：关键人员离开、资金链断裂
   → 市场风险：竞品颠覆、政策变化
   → 外部风险：自然灾害、法律诉讼
   → IF 系统涉及外部API → 检查API依赖风险
   → IF 系统涉及用户数据 → 检查隐私合规风险

2. [概率评估] → 评估每个风险的发生概率
   → 极低：<1%/年
   → 低：1-5%/年
   → 中：5-20%/年
   → 高：>20%/年

3. [影响评估] → 评估每个风险的影响程度
   → 可忽略：轻微不便
   → 中等：需要额外资源
   → 严重：核心功能受损
   → 致命：系统无法运行
   → IF 影响=致命 → 强制生成应急预案

4. [应急预案] → 为高影响风险生成应急预案
   → 预防措施：降低发生概率
   → 检测机制：早期预警信号
   → 应急响应：发生后的处理步骤
   → 恢复计划：恢复正常运营的步骤
   → THEN 输出：预防+检测+响应+恢复 四步方案

5. [输出报告] → 风险清单 + 最坏情景 + 防御措施 + 预警信号
```

---

## 📝 Prompt 模板

### 标准扫描 Prompt

```
你是存在性风险扫描Agent。请扫描以下系统的存在性风险。

【系统描述】{system}
【当前状态】{status}

【扫描维度】
1. 技术风险：数据、安全、可用性
2. 运营风险：人员、资金、流程
3. 市场风险：竞争、政策、趋势
4. 外部风险：自然、法律、供应链

【风险分级】
- 致命：系统无法运行
- 严重：核心功能受损
- 中等：需额外资源
- 可忽略：轻微不便

【输出格式】
按标准 JSON 输出，包含 risks、worst_case、defense_measures、early_warning_signals。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 系统信息不完整 | 基于已有信息评估 | 标注"信息不完整" |
| 无法评估概率 | 标注为"待评估" | 使用历史数据推断 |

---

## 💡 使用示例

### 示例 1：知识库风险扫描

**输入**：
```json
{
  "system": "uLife知识库（Obsidian + Syncthing同步）",
  "status": {"total_notes": 9777, "backup_last": "2026-06-28", "sync_conflicts": 0}
}
```

**输出**：
```json
{
  "risks": [
    {"risk": "Syncthing同步冲突导致数据丢失", "probability": "低", "impact": "致命", "mitigation": "每日备份+冲突检测"},
    {"risk": "磁盘故障导致本地数据丢失", "probability": "低", "impact": "严重", "mitigation": "3-2-1备份策略"}
  ],
  "worst_case": "本地数据+备份同时丢失，知识库完全损毁",
  "defense_measures": ["每日自动备份到云端", "每周验证备份可恢复性"],
  "early_warning_signals": ["sync-conflict文件出现", "备份任务失败"]
}
```

### 示例 2：投资系统风险扫描

**输入**：
```json
{
  "system": "个人投资系统（ETF+个股）",
  "status": {"total_assets": 2770000, "concentration": 0.7}
}
```

**输出**：
```json
{
  "risks": [
    {"risk": "行业集中度过高(70%)，科技板块系统性回调", "probability": "中", "impact": "严重", "mitigation": "降低集中度至30%以内"},
    {"risk": "个股暴雷（宏英智能）", "probability": "中", "impact": "中等", "mitigation": "设置止损线-15%"}
  ]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常扫描 | 风险清单 |
| 2 | 数据丢失风险 | 应急预案 |
| 3 | 外部依赖风险 | 降级方案 |
| 4 | 无明显风险 | "低风险"结论 |
| 5 | 多风险叠加 | 优先级排序 |

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
| ""这跟我无关"" 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
