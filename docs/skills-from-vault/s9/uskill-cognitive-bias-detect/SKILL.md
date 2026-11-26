---
name: uskill-cognitive-bias-detect
description: "让认知偏差检测 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-cognitive-bias-detect.md"
  original_id: "SKL-6900"
  version: "3.0.0"
  trust: untrusted
---

# 认知偏差检测 Agent — 实施手册

description: |
  当用户需要检测决策过程中的认知偏差时使用此 Skill。
  触发词包括：'认知偏差'、'确认偏误'、'锚定效应'、'损失厌恶'、'思维陷阱'、'决策检视'。
  当用户说"我这个决定对不对"、"帮我看看有没有偏见"，即使未直接说"认知偏差"，也应使用此 Skill。
  不适用于纯技术性决策（如代码bug排查）。用于投资、战略、人事等重大决策的质量审查。

---

# 🧠 uSkill-302: 认知偏差检测

## 🎯 目标

> 识别并纠偏确认偏误/锚定/损失厌恶等20种常见认知偏差，提升决策质量。

**核心价值**：让每一次重大决策都经过"认知偏差扫描"，避免系统性思维陷阱。

**适用场景**：
- 投资决策前的偏差审查
- 项目优先级判断的公正性检验
- 人事/招聘决策的客观性评估
- 战略选择的全面性检查
- 日常重大决策的复盘

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `decision_process` | `string` | ✅ | — | 决策过程的完整描述 |
| `assumptions` | `array` | ✅ | — | 关键假设列表 |
| `context` | `object` | ❌ | — | 决策背景（时间压力、信息量、利益相关方） |
| `bias_focus` | `array` | ❌ | 全部20种 | 重点关注的偏差类型 |
| `check_depth` | `enum` | ❌ | `standard` | `quick`(5种核心) / `standard`(15种) / `deep`(20种全覆盖) |

**输入约束**：
- `decision_process` 应包含：决策目标、可选方案、选择依据、预期结果
- `assumptions` 每项应有明确陈述（如"市场会继续上涨"）
- `check_depth=deep` 时建议提供完整决策文档

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话偏差检测结论",
  "decision_id": "BD-YYYY-MMDD-NNN",
  "biases_detected": [
    {
      "bias_type": "string",
      "bias_name_cn": "string",
      "severity": "high|medium|low",
      "evidence": "string — 检测到该偏差的具体证据",
      "impact": "string — 该偏差对决策的潜在影响",
      "debiasing": "string — 具体纠偏方法"
    }
  ],
  "coverage": {
    "total_checked": "number",
    "detected_count": "number",
    "high_severity_count": "number",
    "detection_rate": "string"
  },
  "overall_assessment": {
    "bias_risk_level": "high|medium|low",
    "confidence_in_decision": "string",
    "recommended_action": "string"
  },
  "improvement_suggestions": ["string"]
}
```

---

## 🔄 执行流程

```
1. [输入解析] → 提取决策过程和假设
   → 判断条件：decision_process 是否完整？
     → 是：进入步骤2
     → 否：输出警告「决策过程描述不完整，检测可能遗漏」+ 降级处理

2. [偏差扫描] → 逐项检测20种认知偏差
   → 第一梯队（高频致命）：确认偏误、锚定效应、损失厌恶、过度自信、可得性偏差
   → 第二梯队（中频）：框架效应、禀赋效应、沉没成本、从众效应、光环效应
   → 第三梯队（低频但致命）：幸存者偏差、后见之明、乐观偏差、计划谬误、选择性注意
   → 第四梯队（专业场景）：专家盲点、功能固着、心理账户、代表性偏差、对比效应
   → 每种偏差：检查 → 如检测到 → 标注严重度 → 记录证据

3. [严重度评级] → 对检测到的偏差评级
   → high: 直接影响核心决策逻辑（如投资金额>10万的确认偏误）
   → medium: 影响决策质量但可修正（如信息不完整的锚定效应）
   → low: 存在但影响有限（如日常选择的轻微从众）

4. [纠偏建议] → 为每个偏差生成具体纠偏方法
   → 确认偏误 → 主动寻找反面证据，设置"红队"挑战
   → 锚定效应 → 使用多个独立锚点，咨询外部视角
   → 损失厌恶 → 将决策框架从"失去"转换为"获得"
   → 过度自信 → 使用参考类别预测，设定置信区间
   → 可得性偏差 → 系统性收集数据，不依赖直觉印象

5. [综合评估] → 生成整体偏差风险判断
   → 判断条件：high_severity_count >= 2？
     → 是：🔴 偏差风险高，建议暂停决策+外部评审
     → 否：high_severity_count == 1？
       → 是：🟡 存在显著偏差，建议修正后决策
       → 否：🟢 偏差风险低，可继续推进

6. [输出报告] → 生成结构化偏差检测报告
```

---

## 📝 Prompt 模板

### 标准检测 Prompt

```
你是认知偏差检测Agent。请检测以下决策中的认知偏差。

【决策过程】
{decision_process}

【关键假设】
{assumptions}

【检测深度】{check_depth}

【检测清单】
请逐项检查以下偏差（check_depth决定检查范围）：

第一梯队（必检）：
1. 确认偏误：是否只关注支持性证据？
2. 锚定效应：是否被初始信息过度锚定？
3. 损失厌恶：是否因害怕损失而错过机会？
4. 过度自信：是否高估了自己的判断准确率？
5. 可得性偏差：是否因信息易获取而过度加权？

第二梯队（standard以上）：
6. 框架效应：决策是否因表述方式不同而改变？
7. 禀赋效应：是否因"已拥有"而高估其价值？
8. 沉没成本：是否因已投入成本而继续错误决策？
9. 从众效应：是否因他人做法而跟随？
10. 光环效应：是否因某个优点而全面高估？

第三梯队（deep模式）：
11-20. 幸存者偏差、后见之明、乐观偏差、计划谬误、选择性注意、专家盲点、功能固着、心理账户、代表性偏差、对比效应

【输出要求】
每个检测到的偏差提供：类型、严重度、证据、影响、纠偏方法。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| decision_process 过于简短(<50字) | 输出警告，请求补充 | 仅检测第一梯队5种偏差 |
| assumptions 为空 | 标注"假设未明确" | 跳过假设相关偏差检测 |
| 检测结果为0个偏差 | 输出"未检测到明显偏差" | 建议人工复核+外部视角 |
| 决策涉及金额巨大(>100万) | 自动升级为 deep 模式 | 强制覆盖20种偏差 |

---

## ✅ 质量自检

- [ ] 20种偏差检测清单完整
- [ ] 每个检测到的偏差有具体证据（非泛泛而谈）
- [ ] 严重度评级有明确标准
- [ ] 纠偏建议具体可执行（非"注意一下"）
- [ ] 综合评估逻辑清晰
- [ ] 输出 JSON 格式合规

---

## 💡 使用示例

### 示例 1：投资决策偏差检测

**输入**：
```json
{
  "decision_process": "考虑加仓科创50ETF，理由是最近涨势好，身边朋友都在买，感觉还会继续涨",
  "assumptions": ["科技牛市会持续", "政策会继续支持"],
  "check_depth": "standard"
}
```

**输出**：
```json
{
  "biases_detected": [
    {"bias_type": "availability", "bias_name_cn": "可得性偏差", "severity": "high", "evidence": "仅依据近期涨势判断，忽视了历史回调数据", "debiasing": "查看科创50过去3年的最大回撤数据"},
    {"bias_type": "herding", "bias_name_cn": "从众效应", "severity": "medium", "evidence": "'身边朋友都在买'是决策依据之一", "debiasing": "独立评估投资价值，不以他人行为作为决策依据"}
  

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
