---
name: uskill-cognition-cognitive-psychological-behavior-analysis
description: "让cognitive psychological behavior analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-psychological-behavior-analysis.md"
  original_id: "SKL-6827"
  version: "3.0.0"
  trust: untrusted
---

# cognitive psychological behavior analysis

# Psychological Behavior Analysis

## 🎯 目标
> 建立一套标准化的、AI增强的五步洞察分析循环，用于在非临床场景下，对个人、团队或用户群体的行为与心理模式进行系统化分析，产出数据驱动的洞察、行动建议与验证方案。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `analysis_goal` | string | ✅ | 分析要回答的核心问题（如"用户流失的深层心理原因是什么？"） |
| `scene_type` | enum | ✅ | `product`（用户行为洞察）/ `team`（团队协作诊断）/ `personal`（个人决策复盘） |
| `qualitative_data` | array | ❌ | 定性数据：用户访谈文稿、开放式问卷、会议记录、个人日记 |
| `quantitative_data` | array | ❌ | 定量数据：用户行为日志、App使用时长、社交媒体互动数据 |
| `psychology_framework` | string | ❌ | 指定心理学框架，为空则由AI推荐（如福格行为模型、双系统理论等） |

## 📤 输出

```json
{
  "report_title": "string — 《人性洞察与行为分析报告》标题",
  "scene_type": "product | team | personal",
  "data_summary": {
    "qualitative_themes": [{"topic": "string", "frequency": "int", "sentiment": "positive | neutral | negative"}],
    "quantitative_patterns": [{"pattern": "string", "evidence": "string", "confidence": "number"}]
  },
  "insights": [
    {
      "insight_id": "int",
      "description": "string — 核心洞察描述",
      "framework": "string — 所用心理学理论框架",
      "depth_level": "surface | intermediate | profound",
      "counter_intuitive": "boolean — 是否反直觉"
    }
  ],
  "actionable_recommendations": [
    {
      "action": "string — 具体做什么",
      "reason": "string — 为什么做",
      "expected_effect": "string — 预期效果",
      "owner": "string — 执行负责人",
      "timeline": "string — 执行周期"
    }
  ],
  "validation_plan": {
    "metrics": [{"recommendation": "string", "metric": "string", "method": "A/B test | pre-post comparison | survey"}],
    "review_cycle": "string — 验证周期"
  },
  "quality_checks": {
    "pattern_count": "int — AI识别的模式数",
    "insight_count": "int — 深度洞察能力数",
    "recommendation_count": "int — 可执行建议数",
    "all_anonymized": "boolean — 数据是否完全匿名"
  }
}
```

## 📋 执行步骤

### 第一步：目标定义与数据源确定
1. **明确核心问题** — 将分析目标转化为一个具体、可回答的问题（产品场景："Power User的核心行为动机是什么？"；团队场景："远程协作的沟通瓶颈在哪里？"；个人场景："投资决策中最常见的认知偏误是什么？"）
2. **确定数据源** — 列出所需的定性数据（访谈文稿、问卷）和定量数据（行为日志、使用时长），确保至少两种数据来源

### 第二步：多维数据收集与整理
3. **数据收集** — 执行访谈、导出后台数据、收集相关文本材料
4. **清洗与匿名化** — 移除所有个人身份信息，确保隐私合规
5. **格式化处理** — 使用AI工具对访谈录音转录，将所有数据整理为 `.txt` / `.csv` 格式

### 第三步：AI辅助模式识别与分析
6. **定性分析** — 使用提示词01，让AI扮演"用户体验研究员"，对访谈文稿进行主题建模（Top 5痛点/期望）、情感分析，引用原文总结反直觉观点
7. **定量分析** — 使用Python脚本对行为数据进行探索性分析（EDA），执行用户分群（Clustering）和行为序列分析，寻找异常模式

### 第四步：心理学框架解读与洞察生成（人工主导）
8. **选择框架** — 根据场景选择心理学理论：产品→福格行为模型/马斯洛需求层次；团队→塔克曼团队发展阶段/Lencioni五大障碍；个人→卡尼曼双系统理论/CBT认知扭曲模型
9. **AI辅助解读** — 使用提示词02，将AI发现的数据模式与心理学框架结合，生成初步洞察和待验证假设
10. **人工提炼** — 结合专业知识和经验，将数据模式上升为对"人性"的深刻理解，产出"眼前一亮"的洞察

### 第五步：行动建议与验证方案
11. **生成建议** — 使用提示词03，将核心洞察转化为具体、可执行的行动建议（每个建议含"做什么""为什么做""预期效果"）
12. **设计验证** — 为每个关键建议设计可衡量的验证指标和方法（A/B测试、前后对比等）
13. **撰写报告** — 汇总所有步骤，形成简洁有力的《人性洞察与行为分析报告》

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 分析目标定义模糊 | 返回第一步，要求用户将问题具体化为可回答的单一问题 |
| 数据量不足（定性 < 3份 或 定量 < 100条） | 标记 `WARNING_INSUFFICIENT_DATA`，基于有限数据分析但注明局限性 |
| AI识别的模式与人工阅读感受不一致 | 增加人工抽检比例至30%，以人工判断为准调整AI参数 |
| AI建议过于泛化、缺乏可执行性 | 要求AI补充具体的"做什么/谁来做/什么时候做"三要素 |
| 洞察未触及动机层面（仅停留在表面） | 强制使用追问法："这个行为背后的根本需求是什么？" |
| 数据涉及敏感隐私未充分匿名 | 立即暂停分析，重新执行匿名化处理 |

## ✅ 自检清单

- [ ] 分析目标是一个具体、可回答的问题
- [ ] 至少有两种（定性/定量）数据来源
- [ ] 所有个人身份信息已完全移除
- [ ] AI识别出的主题与人工阅读感受一致
- [ ] 产出了至少1-2个反直觉或深刻的洞察
- [ ] 每个洞察均有心理学理论框架支撑
- [ ] 每个建议足够具体，可直接分配执行
- [ ] 验证方案清晰，可在一定周期内判断有效性
- [ ] 报告包含核心洞察、行动建议和验证计划三部分


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
- 当所依赖的平台/工具停止维护时，标记为 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
