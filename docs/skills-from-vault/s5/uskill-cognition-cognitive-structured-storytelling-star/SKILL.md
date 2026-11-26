---
name: uskill-cognition-cognitive-structured-storytelling-star
description: "让cognitive structured storytelling star变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-cognitive-structured-storytelling-star.md"
  original_id: "SKL-6844"
  version: "3.0.0"
  trust: untrusted
---

# cognitive structured storytelling star

# Structured Storytelling with STAR

## 🎯 目标
> 用STAR法则（Situation-Task-Action-Result）结构化表达经历和成果，适用于面试、简历、汇报、复盘等场景，让听众在最短时间内理解你的价值。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `scenario` | string | ✅ | 需要描述的经历或事件 |
| `context` | enum | ❌ | `interview` / `resume` / `presentation` / `review`，默认 `interview` |
| `detail_level` | enum | ❌ | `concise`（1句话概括）/ `standard`（3-5句）/ `detailed`（完整段落），默认 `standard` |
| `audience` | string | ❌ | 听众画像，用于调整专业术语程度 |

## 📤 输出

```json
{
  "situation": "string — 背景描述",
  "task": "string — 任务/目标",
  "action": "string — 采取的行动",
  "result": "string — 量化结果",
  "summary": "string — 一句话概括版",
  "full_story": "string — 完整STAR段落"
}
```

## 📋 执行步骤

1. **分析场景** — 从 `scenario` 中提取关键信息，识别事件的核心冲突和价值点
2. **构建Situation** — 用1-2句话描述背景：时间、地点、角色、面临的挑战
3. **明确Task** — 用1句话说明你的具体任务或目标，突出责任范围
4. **拆解Action** — 描述你采取的具体行动（2-3个关键步骤），用动词开头，体现你的思考过程和决策逻辑
5. **量化Result** — 用数据或对比说明结果，尽量量化（提升了X%、节省了Y小时、获得了Z评价）
6. **组装输出** — 按 `detail_level` 组装不同版本：concise版一句话概括S+T和A+R；standard版分四段；detailed版补充思考过程和经验教训

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `scenario` 描述模糊 | 返回追问提示：请补充具体时间、角色、挑战 |
| 无法量化结果 | 使用定性描述 + 对比（"从X变为Y"） |
| 经历过于复杂 | 建议拆分为多个独立STAR，按影响力排序 |
| 听众为非专业人士 | 自动简化术语，增加类比说明 |

## ✅ 自检清单

- [ ] Situation是否包含具体时间、地点、角色
- [ ] Task是否用一句话说清楚目标
- [ ] Action是否体现"我"的主动性和思考过程（而非团队/公司行为）
- [ ] Result是否有量化数据或明确对比
- [ ] 整体是否能在60秒内讲完（concise版）
- [ ] 是否避免了"我们"而使用"我"（突出个人贡献）

## 💡 使用技巧

### 面试场景
- 提前为每个核心经历准备STAR，预演3遍
- S和T用1句话概括，A用N句话专业表达，R用数据收尾
- 追问时展开A的细节（思考过程、权衡取舍）

### 简历场景
- 每段工作经历用STAR重写
- 格式：动词开头 + 量化结果（如"主导X项目，提升Y%效率"）

### 复盘场景
- S=当时的情况，T=目标，A=做了什么，R=实际结果
- 额外增加：Result vs Expected的差距分析


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
| 2026-05-09 | 1.0.0 | 初始版本，从 Framework_STAR 转化 |

---
**相关笔记**：[[行为洞察分析 v2]] [[SkillOpt技能优化]] 


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
- [ ] 预算耗尽 →

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
