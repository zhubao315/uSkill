---
name: uskill-productivity-okr-strategic-goal-management
description: "让productivity okr strategic goal management变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-okr-strategic-goal-management.md"
  original_id: "SKL-5140"
  version: "3.0.0"
  trust: untrusted
---

# uSkill-productivity-okr-strategic-goal-management

# OKR Strategic Goal Management（AI赋能个人战略目标管理）

## 🎯 目标
> 通过OKR框架将年度愿景转化为可衡量的季度行动，配合AI增强的周度检视和季度复盘，确保个人精力始终聚焦于最高价值事务。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `annual_vision` | string | ✅ | 年度愿景或战略方向（如"AI-Led Evolution"） |
| `strategic_pillars` | string[] | ✅ | 战略支柱列表（如智慧学习、效率倍增、身心赋能、沟通精进） |
| `quarter_focus` | string | ❌ | 本季度战略重心（如"提升AI产品商业化能力"） |
| `current_okrs` | object | ❌ | 当前在执行的OKR（用于检视/复盘模式） |
| `mode` | enum | ❌ | `set`（设定）/ `review`（周度检视）/ `reflect`（季度复盘），默认 `set` |

## 📤 输出

```json
{
  "quarterly_okrs": {
    "objectives": [
      {
        "id": "O1",
        "description": "定性目标描述",
        "aligned_pillars": ["战略支柱1", "战略支柱2"],
        "key_results": [
          {
            "id": "KR1.1",
            "description": "可量化的关键结果",
            "target_value": "目标值",
            "current_value": "当前值",
            "confidence": 7
          }
        ]
      }
    ]
  },
  "weekly_tasks": [
    {"task": "具体任务", "linked_kr": "KR1.1", "priority": "high"}
  ],
  "review_insights": ["洞察1", "洞察2"]
}
```

## 📋 执行步骤

### 模式一：季度OKR设定（mode=set）

1. **回顾年度愿景** — 读取 `annual_vision` 和 `strategic_pillars`，明确本季度战略重心
2. **头脑风暴目标** — 生成3-5个鼓舞人心的定性目标（O），与战略支柱对齐
3. **筛选精炼目标** — 选择2-3个最具"非对称回报"价值的目标
4. **拆解关键结果** — 为每个O设定3-5个可量化的KR，符合SMART原则
5. **质量校验** — 检查每个O是否对齐战略支柱，每个KR是否结果导向（非过程列表）
6. **输出OKR文档** — 生成结构化的季度OKR设定文档

### 模式二：周度检视（mode=review）

1. **更新KR进度** — 为每个KR打分（0-100%）
2. **更新信心指数** — 为每个KR完成可能性打分（1-10分）
3. **识别障碍** — 记录阻碍KR进展的Blocker
4. **AI辅助分析** — 分析偏差原因，提出移除障碍的2-3个具体建议
5. **生成周度检视纪要** — 输出进度、信心、障碍、建议

### 模式三：季度复盘（mode=reflect）

1. **KR最终打分** — 为每个KR打出最终分数（0.7-0.8为理想区间）
2. **O达成评估** — 根据KR完成情况定性评估O达成度
3. **深度反思** — 覆盖成就、失败、根本原因、经验教训四维度
4. **沉淀经验** — 将关键教训输出为可复用的经验晶体
5. **启动新周期** — 将复盘洞察作为下一季度OKR设定的输入

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| KR进度停滞超过2周 | 自动触发根因分析，建议调整策略或目标 |
| 信心指数持续低于4 | 建议重新评估KR合理性，考虑降低目标或拆分为更小单元 |
| 季度复盘KR完成率>90% | 提示目标可能不够有挑战性，建议提高下季度目标难度 |
| O与战略支柱无对齐 | 阻断设定流程，要求明确对齐关系 |

## ✅ 自检清单

- [ ] 每个O与至少一个战略支柱直接对齐
- [ ] 每个KR可量化、结果导向，非过程性任务列表
- [ ] 好的KR期末完成度应在70%-80%（100%=目标不够挑战）
- [ ] 周度检视每个KR有客观数据支撑
- [ ] 信心指数<5的KR已识别障碍并有应对方案
- [ ] 季度复盘每个未完成KR都找到了根本原因
- [ ] 总结出≥2条可指导下季度工作的核心经验


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
| 2026-05-09 | 1.0.0 | 初始版本，从 SOP-22-目标管理 转化 |

---
**相关笔记**：[[柳比歇夫时间统计]] [[个人知识管理系统]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

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
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

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
DISCUSS → PLAN → 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
