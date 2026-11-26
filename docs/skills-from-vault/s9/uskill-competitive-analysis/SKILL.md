---
name: uskill-competitive-analysis
description: "让竞品分析 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-competitive-analysis.md"
  original_id: "SKL-6890"
  version: "3.0.0"
  trust: untrusted
---

# 竞品分析 Agent — 实施手册

description: |
  当用户需要分析某个领域或产品的竞争对手时使用此 Skill。
  触发词包括：'竞品分析'、'竞争对手'、'市场格局'、'差异化策略'、'SWOT分析'。
  当用户说"这个领域有哪些玩家"、"我们和XX比怎么样"，即使未直接说"竞品分析"，也应使用此 Skill。
  不适用于纯学术研究。用于产品战略、投资调研、创业规划等商业场景。

---

# 🔍 uSkill-305: 竞品分析

## 🎯 目标

> AI驱动的竞品情报采集与分析，从海量噪音中提炼战略洞察，生成差异化策略。

**核心价值**：用系统化框架替代直觉判断，确保竞争分析的全面性和客观性。

**适用场景**：
- 新产品立项前的市场格局分析
- 现有产品的竞争定位评估
- 投资调研中的行业竞争分析
- 创业方向选择的可行性评估
- 技术选型的竞品对比

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `domain` | `string` | ✅ | — | 目标领域/赛道名称 |
| `known_competitors` | `array` | ❌ | — | 已知竞品列表 |
| `analysis_depth` | `enum` | ❌ | `standard` | `quick`(3家) / `standard`(5家) / `deep`(8家) |
| `focus_aspects` | `array` | ❌ | 全部 | 重点关注维度（技术/定价/用户/渠道） |
| `our_position` | `object` | ❌ | — | 我方定位（如有） |

**输入约束**：
- `domain` 应明确到具体赛道（如"AI代码助手"而非"AI"）
- `analysis_depth=deep` 时建议提供 our_position 以便差异化分析
- known_competitors 如未提供，将自动识别

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话竞争格局结论",
  "analysis_id": "CMP-YYYY-MMDD-NNN",
  "market_landscape": {
    "total_players": "number",
    "segmentation": [
      {
        "segment": "string",
        "players": ["string"],
        "market_share": "string",
        "growth_trend": "growing|stable|declining"
      }
    ]
  },
  "competitor_profiles": [
    {
      "name": "string",
      "positioning": "string",
      "strengths": ["string"],
      "weaknesses": ["string"],
      "pricing": "string",
      "user_reviews_summary": "string",
      "threat_level": "high|medium|low"
    }
  ],
  "feature_matrix": {
    "headers": ["功能", "竞品A", "竞品B", "我方"],
    "rows": [
      {"feature": "string", "values": ["string"], "importance": "must|should|nice"}
    ]
  },
  "swot_analysis": {
    "strengths": ["string"],
    "weaknesses": ["string"],
    "opportunities": ["string"],
    "threats": ["string"]
  },
  "differentiation_strategies": [
    {
      "type": "offensive|defensive|niche",
      "strategy": "string",
      "rationale": "string",
      "expected_outcome": "string"
    }
  ],
  "action_items": [
    {
      "priority": "P0|P1|P2",
      "action": "string",
      "deadline": "string"
    }
  ]
}
```

---

## 🔄 执行流程

```
1. [竞品识别] → 识别3-8个核心竞品
   → 直接竞品：同赛道、同模式、同用户群
   → 间接竞品：不同模式但解决同一问题
   → 潜在替代品：可能降维打击的新进入者
   → 判断条件：known_competitors 是否提供？
     → 是：以此为基础扩展
     → 否：基于领域知识自动识别
   → 判断条件：识别数量 < analysis_depth要求？
     → 是：继续扩展识别
     → 否：进入步骤2

2. [竞品画像] → 每个竞品深度分析
   → 定位：核心价值主张、目标用户
   → 优势：技术壁垒、品牌、渠道、资金
   → 劣势：短板、用户投诉、增长瓶颈
   → 定价：价格策略、免费/付费模式
   → 用户评价：应用商店评分、核心好评/差评

3. [功能对比矩阵] → 构建结构化对比表
   → 识别核心功能维度（must/should/nice分级）
   → 逐功能对比各竞品
   → 标注差异化机会点

4. [SWOT分析] → 面向我方的竞争定位
   → S: 我方相对竞品的优势
   → W: 我方相对竞品的劣势
   → O: 市场中未被满足的机会
   → T: 竞品可能的威胁（如降价、新功能）
   → 判断条件：our_position 是否提供？
     → 是：基于我方定位做SWOT
     → 否：做通用市场SWOT

5. [差异化策略] → 生成竞争策略
   → 进攻策略：找到竞品薄弱点，集中突破
   → 防御策略：巩固我方优势，防止被蚕食
   → 利基策略：找到未被服务的细分市场
   → 判断条件：我方份额 < 20%？
     → 是：建议利基/进攻策略
     → 否：建议防御+差异化策略

6. [行动建议] → 生成可执行的行动清单
   → 按优先级排序
   → 每条有明确截止日期

7. [输出报告] → 生成结构化竞品分析报告
```

---

## 📝 Prompt 模板

### 标准竞品分析 Prompt

```
你是竞品分析Agent。请分析以下领域的竞争格局。

【输入】
- 目标领域：{domain}
- 已知竞品：{known_competitors}
- 分析深度：{analysis_depth}
- 我方定位：{our_position}

【分析步骤】
1. 识别3-8个核心竞品（直接+间接+替代品）
2. 每个竞品：定位、优势、劣势、定价、用户评价
3. 构建功能对比矩阵（must/should/nice分级）
4. SWOT分析（面向我方）
5. 生成差异化策略（进攻/防御/利基）
6. 输出行动建议（P0/P1/P2优先级）

【输出要求】
- 竞品信息需标注数据来源
- SWOT必须有数据支撑
- 策略必须具体可执行
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 竞品信息不足 | 标注信息缺口，建议补充调研 | 基于公开信息分析，标注置信度低 |
| 领域过于宽泛 | 请求缩小范围 | 聚焦top 3竞品做quick分析 |
| 无法识别竞品 | 输出「该领域竞品格局不明确」 | 基于替代品分析 |
| 我方定位缺失 | 做通用市场分析 | 不生成差异化策略，仅输出格局+SWOT |

---

## ✅ 质量自检

- [ ] 竞品覆盖直接+间接+替代品
- [ ] 每个竞品有数据支撑（非纯主观判断）
- [ ] 功能矩阵重要性分级（must/should/nice）
- [ ] SWOT有具体证据
- [ ] 差异化策略可执行
- [ ] 行动建议有截止日期

---

## 💡 使用示例

### 示例 1：AI代码助手竞品分析

**输入**：
```json
{
  "domain": "AI代码助手",
  "analysis_depth": "standard",
  "focus_aspects": ["技术", "定价", "用户体验"]
}
```

**输出**：
```json
{
  "market_landscape": {"to

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
