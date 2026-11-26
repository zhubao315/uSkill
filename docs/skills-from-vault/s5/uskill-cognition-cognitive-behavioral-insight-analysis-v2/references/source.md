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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-11 转化 |

---
**相关笔记**：[[学习金字塔输出驱动]] [[提示词工程优化]] 


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

### Phase 1: DISCUSS
- [ ] 输出 Context Read 一行判断
- [ ] 确认用户意图
- [ ] 确认约束条件

### Phase 2: PLAN
- [ ] 制定执行方案
- [ ] 确认资源可用
- [ ] 人工审批计划

### Phase 3: EXECUTE
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功


**相关概念**：[[人类误判心理学]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功
