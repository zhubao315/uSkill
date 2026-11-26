# Review Document Quality with Writing Checklist

## 🎯 目标
> 运用 Why-Who-How-What 四维文档质量检查框架，对用户提供的文档进行系统性审查，输出结构化评审意见和具体改进建议，适用于方案文档、技术文档、汇报材料、产品文档等各类书面内容。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `document` | string | ✅ | 待审查的文档内容 |
| `doc_type` | enum | ✅ | 文档类型：`proposal`（方案/建议书）/ `report`（汇报/总结）/ `technical`（技术文档）/ `product`（产品文档）/ `general`（通用） |
| `audience` | string | ❌ | 目标读者描述，如"CEO""跨部门协作者""技术团队"，影响评审侧重点 |
| `review_focus` | array | ❌ | 重点关注维度，可选：`why`（目标清晰度）/ `who`（读者适配）/ `how`（结构逻辑）/ `what`（内容质量）/ `format`（格式规范），默认全部 |
| `strictness` | enum | ❌ | 评审严格度：`gentle`（温和建议）/ `standard`（标准评审）/ `strict`（严格审查），默认 `standard` |

## 📤 输出

```json
{
  "overall_score": {
    "total": "number — 总分 1-10",
    "breakdown": {
      "why_purpose_clarity": "number — 目标清晰度 1-10",
      "who_reader_fit": "number — 读者适配度 1-10",
      "how_structure": "number — 结构逻辑 1-10",
      "what_content_quality": "number — 内容质量 1-10",
      "format_polish": "number — 格式规范 1-10"
    }
  },
  "checklist_results": {
    "why_section": {
      "core_problem_clear": {
        "pass": "boolean",
        "comment": "string — 核心问题是否一句话说清"
      },
      "key_points_identified": {
        "pass": "boolean",
        "comment": "string — 核心观点是否明确，不超过3个"
      }
    },
    "who_section": {
      "audience_identified": {
        "pass": "boolean",
        "comment": "string — 目标读者是否明确"
      },
      "reader_needs_addressed": {
        "pass": "boolean",
        "comment": "string — 是否针对不同角色的关注点"
      },
      "background_context_provided": {
        "pass": "boolean",
        "comment": "string — 背景信息是否充分"
      }
    },
    "how_section": {
      "structure_clear": {
        "pass": "boolean",
        "comment": "string — 是否可参考金字塔原理"
      },
      "conclusion_first": {
        "pass": "boolean",
        "comment": "string — 关键结论是否前置"
      },
      "toc_navigable": {
        "pass": "boolean",
        "comment": "string — 目录是否可快速定位重点"
      }
    },
    "what_section": {
      "key_points_highlighted": {
        "pass": "boolean",
        "comment": "string — 段落要点是否醒目"
      },
      "charts_where_needed": {
        "pass": "boolean",
        "comment": "string — 复杂信息是否有图表辅助"
      },
      "redundancy_removed": {
        "pass": "boolean",
        "comment": "string — 是否已精简读者已知信息"
      },
      "points_consolidated": {
        "pass": "boolean",
        "comment": "string — 要点是否控制在7±2条"
      },
      "language_accessible": {
        "pass": "boolean",
        "comment": "string — 是否避免了不必要的黑话"
      },
      "reader_questions_anticipated": {
        "pass": "boolean",
        "comment": "string — 是否预见并回答了读者疑问"
      }
    },
    "format_section": {
      "alignment_ok": {
        "pass": "boolean",
        "comment": "string — 标题/正文/图表对齐"
      },
      "typo_free": {
        "pass": "boolean",
        "comment": "string — 错别字检查"
      },
      "punctuation_consistent": {
        "pass": "boolean",
        "comment": "string — 标点符号和单位统一"
      }
    }
  },
  "priority_fixes": [
    {
      "issue": "string — 问题描述",
      "severity": "critical / major / minor",
      "location": "string — 问题所在段落/位置",
      "suggestion": "string — 具体修改建议",
      "example": "string — 修改示例（可选）"
    }
  ],
  "iteration_advice": {
    "peer_review_suggestion": "string — 是否建议先给同事预览",
    "reference_docs": "string — 可参考的优秀文档方向",
    "top_3_improvements": ["string — 最值得做的3项改进"]
  }
}
```

## 📋 执行步骤

1. **文档预读** — 快速通读全文，建立整体印象：
   - 识别文档类型和目的
   - 判断目标读者（若有 `audience` 参数则以此为准）
   - 形成初步结构认知

2. **Why 维度审查 — 目标清晰度**：
   - 核心问题是否一句话能说清？
   - 核心观点/建议是否明确？不超过3个要点？
   - 读者读完能否回答"所以呢？"

3. **Who 维度审查 — 读者适配度**：
   - 目标读者是否明确？
   - 是否为不同角色（决策者/协作者/信息同步对象）提供了对应信息？
   - 背景信息是否充分，新读者能否理解？
   - 专业术语使用是否匹配读者水平？

4. **How 维度审查 — 结构逻辑**：
   - 整体结构是否清晰？（参考金字塔原理：结论先行，以上统下）
   - 关键结论是否前置？
   - 目录是否一目了然、可快速定位？
   - 段落间逻辑是否连贯（因果/并列/递进）？

5. **What 维度审查 — 内容质量**：
   - **突出重点**：关键结论前置？段落要点醒目？复杂信息有图表？
   - **精简内容**：读者已知信息是否可删减？要点控制在7±2条？去掉该部分是否造成信息减损？（不是肯定Yes就是肯定No）
   - **清晰表达**：是否避免不必要黑话？读者疑问是否被预见并解答？

6. **格式审查**：
   - 对齐、错别字、标点符号、大小写、全角/半角统一
   - 数字、单位格式一致性

7. **综合评分与建议**：
   - 按五维度打分，计算总分
   - 按 severity 排序列出优先修改项
   - 给出迭代建议（是否需要同事预览、可参考的优秀文档方向等）

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 文档过短（<100字） | 仅做基础检查，提示信息量不足 |
| 文档语言非中文 | 根据实际语言调整检查标准（如英文检查 AP style） |
| 文档为纯代码/技术配置 | 跳过语义检查，聚焦格式和结构审查 |
| 用户只关注特定维度 | 根据 `review_focus` 参数仅检查指定维度 |
| 文档包含敏感信息 | 提醒用户注意脱敏，评审中不存储原文 |

## ✅ 自检清单

- [ ] 五个维度均有评审结果，无遗漏
- [ ] 每条检查项有 pass/fail 判定和具体评语
- [ ] 问题描述具体，指出所在位置，非泛泛批评
- [ ] 修改建议可操作，最好附示例
- [ ] 优先级排序合理，critical 项优先于 minor 项
- [ ] 迭代建议务实（同事预览、参考方向、Top 3改进）
- [ ] 评审语气匹配 `strictness` 设置
- [ ] 未过度修改文档风格，尊重作者表达习惯


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
| 2026-05-08 | 1.0.0 | 初始版本，从「写好文档的checklist」转化 |

---
**相关笔记**：[[个人知识管理系统]] [[uSkill-productivity-晚间复盘报告]] 


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


**相关概念**：[[金线质量标准]] · [[质量属性与架构权衡]]

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
