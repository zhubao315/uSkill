---
name: uskill-cognition-6934e2
description: "让行动前假设验证变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-行动前假设验证.md"
  original_id: "SKL-6837"
  version: "3.0.0"
  trust: untrusted
---

# 行动前假设验证

# 行动前假设验证

## 🎯 目标
> 在投入任何重大资源（时间、金钱、精力）之前，识别隐藏假设、按致命性排序、设计最小实验验证——用1天的学习避免1年的浪费。

**核心公式：** `决策价值 = 假设识别清晰度 × 验证实验成本效率`

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `decision_context` | string | ✅ | 要做的决策/计划/项目的描述（如"我要做一个AI写作工具"、"我要跳槽做产品经理"） |
| `known_assumptions` | string[] | ❌ | 已知的假设列表（如有） |
| `available_resources` | string | ❌ | 可用于验证的资源约束（时间、预算、渠道） |
| `deadline` | string | ❌ | 决策截止日期，影响验证深度 |
| `risk_tolerance` | enum | ❌ | `conservative` / `moderate` / `aggressive`，默认 `moderate` |

## 📤 输出

```json
{
  "assumption_analysis": {
    "all_assumptions": [
      {
        "id": "A1",
        "description": "string — 假设描述",
        "type": "value | need | growth | technical | channel",
        "uncertainty": "int 1-5",
        "criticality": "int 1-5",
        "priority_score": "int — uncertainty × criticality"
      }
    ],
    "top_assumptions": ["string — 按优先级排序的致命假设ID列表"]
  },
  "validation_experiments": [
    {
      "target_assumption": "string — 对应假设ID",
      "method": "string — 验证方法（视频MVP / 落地页测试 / 礼宾MVP / 绿野仙踪MVP / 用户访谈 / 数据分析）",
      "cost": "极低 | 低 | 中",
      "speed": "string — 预计耗时",
      "success_criteria": "string — 假设成立的判断标准",
      "failure_criteria": "string — 假设被推翻的判断标准"
    }
  ],
  "execution_plan": {
    "sequence": ["string — 实验执行顺序"],
    "total_estimated_cost": "string",
    "total_estimated_time": "string"
  },
  "decision_framework": {
    "if_validated": "string — 假设全部成立时的下一步行动",
    "if_invalidated": "string — 关键假设被推翻时的调整策略",
    "pivot_options": ["string — 可选的转型方向"]
  }
}
```

## 📋 执行步骤

1. **列出所有假设** — 对目标决策问："要让这件事成功，哪些条件必须为真？"将隐含假设显式化，按类型分类（价值/需求/增长/技术/渠道）。
2. **排序致命假设** — 用「不确定性 × 致命性」双维度矩阵排序。不确定性=你有多不确定这件事是否成立；致命性=如果它不成立，后果有多严重。优先级分数最高的先验证。
3. **设计最小验证实验** — 对每个致命假设，问："用最少的时间和金钱，我能怎样判断它是对是错？"选择验证方法：视频MVP（极低成本验证概念）、落地页测试（验证付费意愿）、礼宾MVP（验证服务价值）、绿野仙踪MVP（验证用户行为）、用户访谈（验证需求假设）。
4. **定义成功/失败标准** — 在实验前明确：什么数据/行为算"假设成立"，什么算"假设被推翻"。避免事后合理化。
5. **执行实验并收集数据** — 按优先级顺序执行。假设被推翻是**好消息**——用最小代价避免了最大浪费。
6. **做出数据驱动决策** — 根据实验结果决定：继续推进、调整方向、还是彻底转型。

## ⚠️ 异常处理

| 异常场景 | 识别信号 | 处置策略 |
|----------|----------|----------|
| 无法识别假设 | 决策描述过于模糊，无法拆解为条件 | 先执行 `cognitive-decompose-problem` 技能，将模糊目标结构化后再识别假设 |
| 验证成本超过决策价值 | 实验成本 > 决策失败的损失 | 降级为专家访谈或案例分析，用间接证据替代直接实验 |
| 假设之间高度耦合 | 改变一个假设会影响其他假设的验证 | 设计联合实验同时验证多个假设，或按依赖关系排序验证 |
| 数据相互矛盾 | 不同实验给出矛盾信号 | 延长验证周期、增加样本量、或切换验证方法 |
| 决策时间紧迫 | deadline 远早于实验完成时间 | 缩小验证范围，只验证优先级最高的1-2个假设 |

## ✅ 自检清单

- [ ] 所有隐含假设已被显式列出（≥3个）
- [ ] 每个假设都标注了不确定性和致命性评分
- [ ] 最致命的假设有对应的最小验证实验设计
- [ ] 每个实验都有明确的成功/失败判定标准
- [ ] 验证成本与决策规模成比例（不超过决策价值的10%）
- [ ] 输出了假设被推翻时的调整策略（不止一条路径）
- [ ] 没有"验证自己舒服的假设"的确认偏误


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
| 2026-05-09 | 1.0.0 | 初始版本，从「假设先行验证法则」SOP 转化 |

---
**相关笔记**：[[盘中行情监控]] [[uSkill-cognition-意义审计协议]] 


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


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
