---
name: uskill-wine-blind-tasting-advanced
description: "盲品不是炫技——是训练你的感官成为最精密的分析仪器。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-wine-blind-tasting-advanced.md"
  original_id: "SKL-6808"
  version: "3.0.0"
  trust: untrusted
---

# 葡萄酒盲品进阶

description: |
  当用户需要提升葡萄酒盲品能力、系统化训练感官、分析品鉴推理时使用此 Skill。
  触发词：'盲品'、'品酒'、'葡萄酒品鉴'、'品种识别'、'产区判断'。
  不适用于基础品酒（使用葡萄酒品鉴体系）或餐酒搭配（使用中式餐酒搭配）。

# 葡萄酒盲品进阶

## 🎯 目标

> 通过系统化的感官训练，提升葡萄酒品种和产区的识别能力。

**核心价值**：盲品的核心不是天赋，是「看到 → 描述 → 推理」的训练。本 Skill 建立从感官观察到品种/产区判断的逻辑链路。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `tasting_notes` | string | ✅ | — | 品鉴笔记（外观/香气/口感/余味） |
| `context` | string | ❌ | — | 额外信息（价格范围/产区提示/餐食搭配） |
| `goal` | enum | ❌ | `"identification"` | 目标：`identification`（品种识别）/ `training`（训练建议）/ `analysis`（推理分析） |

## 📤 输出

```json
{
  "status": "success|partial|failed",
  "summary": "string — 一句话执行总结",
  "sensory_analysis": {
    "appearance": {"color": "string", "intensity": "string", "age_indicators": "string"},
    "nose": {"primary": ["string"], "secondary": ["string"], "tertiary": ["string"]},
    "palate": {"sweetness": "string", "acidity": "string", "tannin": "string", "body": "string", "finish": "string"}
  },
  "deduction": {
    "grape_varieties": [{"variety": "string", "confidence": "int%", "reasoning": "string"}],
    "region_candidates": [{"region": "string", "confidence": "int%", "reasoning": "string"}],
    "age_estimate": "string",
    "quality_level": "string"
  },
  "training_recommendation": {
    "weak_areas": ["string"],
    "practice_wines": ["string"],
    "focus_exercises": ["string"]
  }
}
```

## 📋 执行步骤

### Step 1: 感官观察
1. **外观** — 颜色深度/边缘色调/粘稠度（判断年份和品种）
2. **香气** — 一层（果香）/ 二层（发酵）/ 三层（陈年）香气
3. **口感** — 甜度/酸度/单宁/酒体/余味长度
4. **检查点**：✅ 观察是否全面？是否遗漏了关键特征？

### Step 2: 逻辑推理
1. **品种匹配** — 基于感官特征匹配可能的品种
2. **产区推断** — 基于品种 + 风格推断可能的产区
3. **年份估计** — 基于陈年特征判断大致年份
4. **检查点**：✅ 推理是否有逻辑链条？是否有多候选？

### Step 3: 不确定性管理
1. **置信度评估** — 对每个推断给出置信度
2. **替代方案** — 列出 2-3 个可能的品种/产区
3. **信息缺口** — 说明哪些信息不足影响了判断
4. **检查点**：✅ 是否承认了不确定性？是否有替代方案？

### Step 4: 训练建议
1. **弱点识别** — 哪些感官维度需要加强
2. **练习酒款** — 推荐用于训练的具体酒款
3. **专项练习** — 针对弱点的训练方法
4. **检查点**：✅ 训练建议是否具体？是否有可执行的练习？

## ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 品鉴时必须吐酒，不得过量饮酒
2. 不得为了面子而强行猜测，必须承认不确定
3. 品鉴笔记必须基于感官描述，不得使用主观评价

**软性约束（建议遵守）**：
1. 盲品前避免使用香水/强烈食物
2. 每次品鉴不超过 6 款酒

**人工兜底点**：
- 当健康原因不宜饮酒时，**必须**建议替代训练方式
- 当品鉴环境不佳时，**必须**标注环境影响

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 无法分辨香气 | 一层香气不明显 | 建议进行香气训练（咖啡/水果对比） |
| 单宁判断困难 | 不确定单宁强度 | 用「抓涩感」替代「单宁高低」 |
| 品种混淆 | 两个品种特征相似 | 列出两个候选，说明区分要点 |


### 降级策略
- 当数据不足时，基于已有数据给出保守建议并标注置信度
- 当无法自动化时，输出分析框架供人工填充

## 💬 沟通风格

- **感官语言**：用具体的风味词汇（「黑色浆果」「雪松」「烟熏」）
- **逻辑链**：每个推断都有「因为…所以…」的推理过程
- **诚实**：不确定就说不确定，不装专家

## 📝 自检清单

- [ ] 感官观察是否全面（外观/香气/口感/余味）？
- [ ] 推理是否有逻辑链条？
- [ ] 是否给出了置信度和替代方案？
- [ ] 训练建议是否针对弱点？
- [ ] 是否避免了过量饮酒？

## ✅ 校验验收规则

**格式校验**：
- [ ] 输出包含感官分析/推理/训练建议
- [ ] 每个推断有推理过程

**内容校验**：
- [ ] 基于感官描述而非主观喜好
- [ ] 承认不确定性
- [ ] 训练建议具体可执行

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 饮酒建议适度


### OVP 验证信号
- 核心指标趋势是否向好
- 用户使用频率是否稳定
- 输出质量是否达到预期

## 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 盲品测试成绩提升或下降
  - 发现新的品种特征模式
  - 参加品鉴活动获得反馈

**版本升级触发**：
- 当新增品种/产区的品鉴数据库时，升级 minor 版本

**废弃触发**：
- 当所依赖的数据源/API 停止服务时，标记为 deprecated
- 当出现明显更优的替代方案时，评估迁移并标记版本
- 当建立完整的盲品训练课程时，升级 major 版本

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-07-03 | 1.0.0 | 初始版本，基于 WSET 品鉴方法论 + 个人盲品经验定制 |

---

*关联笔记：[[葡萄酒品鉴体系]] · [[葡萄酒品鉴笔记年度合集]] · [[uSkill]] · [[uSkill-creative-葡萄酒产国选酒策略]] · [[中式餐酒搭配]]*


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

> 来源：addyosmani/agent-skills 的边界

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
