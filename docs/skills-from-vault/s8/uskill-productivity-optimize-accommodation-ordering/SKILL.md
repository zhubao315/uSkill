---
name: uskill-productivity-optimize-accommodation-ordering
description: "让productivity optimize accommodation ordering变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-optimize-accommodation-ordering.md"
  original_id: "SKL-5214"
  version: "3.0.0"
  trust: untrusted
---

# productivity optimize accommodation ordering

# Optimize Accommodation Customer Ordering Flow

## 🎯 目标
> 标准化民宿/住宿类客户的下单接待流程，通过自动化回复和信息前置，减少人工沟通成本，提升客户体验和转化率。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `platform_channels` | list[string] | ✅ | 客户来源渠道（如美团、携程、Airbnb等） |
| `property_info` | object | ✅ | 房源信息（地址、价格、设施、联系方式） |
| `faq_list` | list[string] | ❌ | 常见问题及回答列表 |
| `wechat_id` | string | ✅ | 房东微信号，用于引导添加 |

## 📤 输出

```json
{
  "workflow_map": "object — 各渠道客户下单流程图",
  "auto_reply_scripts": "object — 语音/短信自动回复话术模板",
  "faq_document": "object — 结构化常见问题文档",
  "optimization_checklist": "list — 流程优化检查清单"
}
```

## 📋 执行步骤

1. **梳理客户触点** — 列出客户从发现房源到完成入住的全部接触点，按渠道分类（美团直接下单、电话咨询、下单后联系等）
2. **设计自动化回复** — 为每个触点设计语音自动回复和短信自动回复，关键信息前置（地址导航、入住须知、联系方式）
3. **构建FAQ文档** — 整理客户高频问题，形成结构化FAQ，嵌入自动回复短信中
4. **设置微信引流** — 在各自动回复中嵌入微信号引导语，将客户从平台引流至私域
5. **测试与迭代** — 模拟客户流程测试各环节，收集真实客户反馈，持续优化话术

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 客户跳过自动回复直接上门 | 门口张贴指引牌，包含Wi-Fi密码和紧急联系电话 |
| 自动回复未被读取 | 增加短信二次提醒，或人工电话跟进 |
| 客户投诉流程复杂 | 简化为"一键联系房东"按钮，减少跳转步骤 |

## ✅ 自检清单

- [ ] 所有渠道的客户触点已梳理完毕
- [ ] 自动回复话术覆盖下单前、下单后、入住前三个阶段
- [ ] FAQ文档包含至少10个高频问题
- [ ] 微信号引导语已嵌入所有自动回复中
- [ ] 至少完成3次模拟客户流程测试


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
| 2026-05-09 | 1.0.0 | 初始版本，从接客流程优化方法论转化 |

---
**相关笔记**：[[AI回忆录撰写服务-PRD与实现方案]] [[P4 Agentic 金融]] 


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


**相关概念**：[[住宿订单优化]]

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
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
