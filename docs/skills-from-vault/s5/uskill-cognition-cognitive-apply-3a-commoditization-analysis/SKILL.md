---
name: uskill-cognition-cognitive-apply-3a-commoditization-analysis
description: "让cognitive apply 3a commoditization analysis变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-apply-3a-commoditization-analysis.md"
  original_id: "SKL-6842"
  version: "3.0.0"
  trust: untrusted
---

# cognitive apply 3a commoditization analysis

# 3A Commoditization Analysis (3A左脑商品化分析)

## 🎯 目标
> 通过"富裕(Abundance)、亚洲(Asia)、自动化(Automation)"三大推手框架，评估一项工作或能力的商品化风险，识别需要叠加右脑能力的转型方向。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `target_work` | string | ✅ | 待评估的工作/能力/项目描述 |
| `industry` | string | ❌ | 所属行业，默认为通用评估 |
| `time_horizon` | enum | ❌ | 评估时间范围：1y/3y/5y，默认 3y |

## 📤 输出

```json
{
  "commoditization_score": "int — 商品化风险评分(0-100)",
  "risk_level": "enum — low/medium/high/critical",
  "abundance_risk": {
    "score": "int (0-33)",
    "evidence": "string — 具体证据"
  },
  "asia_risk": {
    "score": "int (0-33)",
    "evidence": "string — 具体证据"
  },
  "automation_risk": {
    "score": "int (0-34)",
    "evidence": "string — 具体证据"
  },
  "brain_profile": "enum — left-brain-dominant/right-brain-dominant/balanced",
  "recommended_actions": ["string — 转型建议列表"],
  "right_brain_skills_to_add": ["string — 建议叠加的右脑能力"]
}
```

## 📋 执行步骤

1. **定义评估对象** — 清晰描述待评估的工作内容、核心技能和产出物
2. **Abundance评估** — 分析该工作是否仅满足"基本功能需求"：物质丰富后，客户是否已不满足于仅"有用"，而要求"美观""有情感""有体验"
3. **Asia评估** — 分析该工作是否可标准化、流程化：是否有全球化的更低成本替代者（包括其他城市、其他国家的从业者）
4. **Automation评估** — 分析AI/自动化对该工作的替代能力：当前AI能完成多少比例？3年后能完成多少？
5. **综合评分** — 将三项风险加总为0-100的商品化风险评分
6. **脑型分析** — 判断该工作是左脑主导（逻辑/分析/计算）还是右脑主导（创造/共情/整合）
7. **生成转型建议** — 基于风险等级和脑型，推荐需要叠加的右脑能力（设计感/故事感/交响能力/共情/娱乐感/意义感）

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 目标描述模糊 | 返回 `ERROR_VAGUE_TARGET`，要求补充具体工作内容 |
| 行业信息缺失 | 使用通用评估标准，标注 `GENERAL_ASSESSMENT` |
| 评估时间范围不明确 | 默认使用3年，标注 `DEFAULT_HORIZON` |
| 数据不足无法判断 | 返回 `INSUFFICIENT_DATA`，列出需要补充的信息 |

## ✅ 自检清单

- [ ] 三个维度（Abundance/Asia/Automation）均有独立评分和证据
- [ ] 商品化风险评分在0-100之间，与三项子评分加总一致
- [ ] 风险等级与评分匹配：low(0-25)/medium(26-50)/high(51-75)/critical(76-100)
- [ ] 转型建议至少包含2项具体可执行的行动
- [ ] 右脑能力建议来自六大能力（设计感/故事感/交响能力/共情/娱乐感/意义感）


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
| 2026-05-09 | 1.0.0 | 初始版本，从《全新思维》读书笔记转化 |

---
**相关笔记**：[[行为洞察分析 v2]] [[心理行为分析]] 


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

### Phase

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
