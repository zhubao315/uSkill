---
name: uskill-cognition-cognitive-behavioral-insight-analysis-v2
description: "让cognitive behavioral insight analysis v2变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-behavioral-insight-analysis-v2.md"
  original_id: "SKL-6834"
  version: "3.0.0"
  trust: untrusted
---

# cognitive behavioral insight analysis v2

# Behavioral Insight Analysis

## 🎯 目标
> AI增强的人性洞察与行为分析：对个人、团队或用户群体的行为与心理模式进行系统化分析，2小时内完成数据驱动的洞察报告，产出可执行的行动建议。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `analysis_target` | enum | ✅ | `user_behavior` / `team_dynamics` / `personal_decision` / `custom` |
| `core_question` | string | ✅ | 本次分析要回答的核心问题 |
| `qualitative_data` | array | ❌ | 访谈文稿、会议记录、开放式问卷等定性数据 |
| `quantitative_data` | object | ❌ | `{behavior_logs: [], usage_stats: [], survey_scores: []}` — 行为日志、使用数据等定量数据 |
| `psychology_framework` | enum | ❌ | `fogg_bmap` / `maslow` / `dual_process` / `cbt_distortions` / `tuckman` / `lencioni` / `auto` — 心理学分析框架，`auto` 为自动选择 |
| `privacy_level` | enum | ❌ | `strict` / `moderate` / `relaxed`，默认 `strict` |

## 📤 输出

```json
{
  "data_summary": {
    "qualitative_themes": [
      {"theme": "string", "frequency": "number", "sentiment": "positive | neutral | negative", "sample_quotes": ["string"]}
    ],
    "quantitative_patterns": [
      {"pattern": "string", "confidence": "high | mid | low", "data_points": "number"}
    ],
    "counterintuitive_finding": "string — 最反直觉的发现"
  },
  "insights": [
    {
      "insight": "string — 核心洞察",
      "framework_used": "string — 使用的心理学框架",
      "evidence": ["string — 支撑证据"],
      "depth_level": "surface | motivational | structural"
    }
  ],
  "actionable_recommendations": [
    {
      "action": "string — 具体行动",
      "rationale": "string — 为什么做",
      "expected_effect": "string — 预期效果",
      "validation_method": "string — 验证方法",
      "validation_metric": "string — 衡量指标",
      "validation_timeline": "string — 验证周期"
    }
  ],
  "psychological_profile": {
    "key_traits": ["string"],
    "cognitive_biases_detected": ["string"],
    "motivation_drivers": ["string"]
  },
  "report_summary": "string — 300字以内的报告摘要"
}
```

## 📋 执行步骤

### Step 1: 目标定义与数据源确定
1. **明确分析目标** — 根据 `analysis_target` 和 `core_question` 定义具体、可回答的问题
   - 产品场景：核心用户最主要的行为动机是什么？
   - 团队场景：团队在远程协作中主要的沟通瓶颈在哪里？
   - 个人场景：做决策时最容易受到哪些认知偏误影响？
2. **确定数据源** — 根据目标确定定性数据（访谈/问卷/日记）和定量数据（行为日志/使用时长/互动数据）
3. **问题质量校验** — 确保问题具体、可回答，避免过于宽泛

### Step 2: 多维数据收集与整理
1. **收集定性数据** — 整理访谈文稿、会议记录、文本材料
2. **收集定量数据** — 从数据库或分析工具导出行为数据
3. **数据清洗与匿名化** — 严格移除个人身份信息（`privacy_level=strict` 时必须）
4. **AI辅助整理** — 对访谈录音进行转录和初步摘要，统一为 `.txt` / `.csv` 格式

### Step 3: AI辅助模式识别与分析
1. **定性数据分析** — 让AI扮演"用户体验研究员"，对文稿进行主题建模和情感分析，识别高频关键词、情绪和观点
2. **定量数据分析** — 让AI进行探索性数据分析（EDA），如用户分群、行为序列分析，寻找异常模式
3. **交叉验证** — 对比AI识别的主题与人工阅读感受是否一致，确认发现至少1-2个反直觉模式

### Step 4: 心理学框架解读与洞察生成
1. **选择解读框架** — 根据 `psychology_framework` 选择合适的理论框架
   - 产品场景：福格行为模型（B=MAP）、马斯洛需求层次、用户心智模型
   - 团队场景：塔克曼团队发展阶段理论、Lencioni团队协作五大障碍
   - 个人场景：卡尼曼双系统理论、CBT认知扭曲模型
2. **AI辅助深度解读** — 将数据模式与心理学框架结合，形成初步洞察
3. **人工提炼与升华** — 基于AI初步解读，结合专业知识提炼深刻、独特的洞察

### Step 5: 行动建议与验证方案
1. **生成行动建议** — 将核心洞察转化为具体、可执行的行动建议
2. **设计验证方案** — 为每个关键建议设计可衡量的验证指标和方法（A/B测试/前后对比）
3. **撰写报告** — 汇总所有步骤，形成简洁有力的《人性洞察与行为分析报告》

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `qualitative_data` 和 `quantitative_data` 均为空 | 返回 `ERROR_NO_DATA` + 至少需要一种数据源 |
| 数据量过少（<5份访谈或<30条行为记录） | 返回 `WARNING_SMALL_SAMPLE` + 标注结论可信度为"探索性" |
| 未脱敏数据混入 | 返回 `ERROR_PRIVACY_VIOLATION` + 拒绝分析直到数据匿名化 |
| `core_question` 过于宽泛 | 返回 `WARNING_VAGUE_QUESTION` + 提供3个细化建议 |
| AI主题与人工感受严重不一致 | 标记 `FLAG_INTERPRETATION_CONFLICT` + 要求人工复核原始数据 |
| `psychology_framework=auto` 但场景模糊 | 返回框架选择建议列表，要求用户确认 |

## ✅ 自检清单

- [ ] 分析目标是否为一个具体、可回答的问题？
- [ ] 是否已明确至少两种（定性/定量）数据来源？
- [ ] 所有个人身份信息是否已完全移除？
- [ ] AI识别出的主题是否与人工阅读感受一致？
- [ ] 是否发现了至少1-2个反直觉的或有趣的模式？
- [ ] 解读是否超越数据表面，触及背后的动机或原因？
- [ ] 是否产出了至少1-2个令人"眼前一亮"的深刻洞察？
- [ ] 每个建议是否足够具体，可以直接分配给某人执行？
- [ ] 验证方案是否清晰，可在一定周期内判断有效性？


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
- [ ] 建议具有可操作性，

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
