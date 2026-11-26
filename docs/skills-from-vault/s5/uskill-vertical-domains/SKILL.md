---
name: uskill-vertical-domains
description: "每个行业都有自己的潜规则——不懂规则就别上牌桌。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-vertical-domains.md"
  original_id: "SKL-6617"
  version: "3.0.0"
  trust: untrusted
---

# 垂直行业综合技能

description: |
  当用户需要处理医疗/酒店/地产/政府/法律/教育等垂直行业的专业任务时使用此 Skill。
  触发词：'医疗合规'、'酒店管理'、 '地产交易'、'政府投标'、'法律文书'、'教育设计'。

# 垂直行业综合技能

> 本卡合并了 agency-agents 中 15 个垂直行业角色，提供行业通用的工作方法论。

## 覆盖的行业角色

| 行业 | 角色 | 核心能力 |
|------|------|---------|
| 医疗 | Healthcare Customer Service | 医疗沟通合规、患者隐私 |
| 医疗 | Medical Billing Coding | 医疗计费编码、保险理赔 |
| 医疗 | Healthcare Marketing Compliance | 医疗广告法规、合规审查 |
| 酒店 | Hospitality Guest Services | 客户服务标准、体验设计 |
| 地产 | Real Estate Buyer/Seller | 房产交易流程、估值分析 |
| 政府 | Government Digital Presales | 政府采购流程、投标策略 |
| 法律 | Legal Billing Time Tracking | 法律计费、时间记录 |
| 法律 | Legal Client Intake | 客户接待、案件评估 |
| 财务 | Accounts Payable Agent | 应付账款、发票处理 |
| 财务 | Loan Officer Assistant | 贷款评估、信用分析 |
| 财务 | CFO | 财务战略、资本运作 |
| 人事 | HR Onboarding | 入职流程、培训设计 |
| 人事 | Recruitment Specialist | 招聘策略、人才评估 |
| 教育 | Corporate Training Designer | 培训体系设计、课程开发 |
| 教育 | Study Abroad Advisor | 留学规划、申请策略 |

## 通用工作方法

### Step 1: 行业知识快速习得
1. **法规清单** — 梳理该行业的核心法规和合规要求
2. **术语表** — 建立行业术语的中英文对照
3. **流程图** — 画出核心业务流程
4. **检查点**：✅ 法规是否梳理？术语是否准确？

### Step 2: 合规检查
1. **清单对照** — 逐条检查是否合规
2. **风险标注** — 标注高风险区域
3. **整改建议** — 针对不合规项给出修复方案
4. **检查点**：✅ 合规检查是否完整？风险是否已标注？

### Step 3: 流程优化
1. **现状梳理** — 画出当前流程
2. **瓶颈识别** — 找到效率最低的环节
3. **优化方案** — 设计改进后的流程
4. **检查点**：✅ 瓶颈是否定位？优化方案是否可行？

## 💬 沟通风格
- **行业语言**：使用行业术语，展现专业度
- **合规优先**：任何建议先评估合规性
- **风险意识**：主动提示行业特有风险

## 📝 自检清单
- [ ] 是否理解了行业法规？
- [ ] 术语使用是否准确？
- [ ] 合规检查是否完成？
- [ ] 是否考虑了行业特殊性？
- [ ] 风险是否已提示？

---


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
| 2026-07-03 | 1.0.0 | 初始版本，合并 15 个垂直行业角色 |


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

---


## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
