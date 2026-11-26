
description: |
  当用户需要通过闭环优化 Skill 文档时使用此 Skill：分析执行失败案例、对照 Gen3 标准
  （[[Skill开发完全规范]]、[[P0升级清单]]）识别缺陷、生成针对性修订并更新文档。
  触发词包括：'Skill优化'、'技能优化'、'Skill改进'、'执行失败分析'、'Gen3 升级'、'文档重构'。
  即使用户没有明确说"优化"，只要意图涉及"这个 Agent 老出错/不达标/要升级到 Gen3"，也应触发。
  不适用：从零新建一个完全无关的 Skill（那走创作流程而非优化流程）。

---

# 🔧 uSkill-7105: SkillOpt 技能优化（Gen3）

## 🎯 目标

> 通过分析执行失败案例与 Gen3 审计缺口，定位 Skill 文档根因缺陷，生成对齐
> [[P0升级清单]] 9 模块标准的修订方案并闭环验证，让 Skill 越用越准。

**适用场景**：`uSkill_upgrade_audit.py` 不达标项的修复、运行期 failure_cases 复盘、
把旧版 Gen2/Gen1 文档升级为 Gen3 Schema。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `skill_doc` | `string` | ✅ | 待优化的 Skill 文档路径 |
| `execution_feedback` | `string` | ✅ | 执行反馈（成功/失败/部分成功 + 现象） |
| `failure_cases` | `array` | ❌ | 失败案例详情（输入/实际输出/期望） |
| `target_standard` | `string` | ❌ | 目标标准，默认 `Gen3` |

---

## 📤 输出

```json
{
  "root_cause": "string",
  "gen3_gap": [{"check": "9模块|IF/THEN|Self-Play|行数|Frontmatter", "passed": "bool", "detail": "string"}],
  "issues": [{"type": "定义不清|流程缺失|边界遗漏|Prompt缺陷|Schema不符", "severity": "P0|P1|P2", "description": "string", "section": "string"}],
  "optimizations": [{"section": "string", "change": "string", "reason": "string"}],
  "verification": {"before_score": "number", "after_score": "number", "rerun_cmd": "string"}
}
```

---

## 🔄 执行流程

```
1. [Gen3 审计] → 先对 skill_doc 跑标准校验
    → 9 模块 H2 是否齐全（🎯目标/📥输入/📤输出/🔄执行流程/📝Prompt/⚠️异常/✅自检/💡示例/🧪Self-Play）
    → IF 缺模块：标 P0 gap，记入 gen3_gap
    → IF 行数<200 或 IF/THEN<3 或 Self-Play<5：标 P0 gap
    → ELSE：进入失败分析分支

2. [失败分析] → 结合 execution_feedback 分析
    → 定义不清：概念模糊导致理解偏差
    → 流程缺失：步骤不完整导致执行遗漏
    → 边界遗漏：异常未覆盖
    → Prompt缺陷：模板槽位/指令不准确
    → IF 反馈为"超时"：优先查执行流程是否缺超时/中断分支
    → ELSE IF 反馈为"分类错"：优先查输入 Schema 与判定规则

3. [缺陷定位] → 定位到具体 section
    → 检查：输入 Schema 是否完整？执行流程是否有 IF/THEN 分支？
    → 检查：异常处理是否覆盖？Self-Play ≥5 且真实？
    → IF 缺陷跨多 section：按严重度排序后批量修订

4. [优化建议] → 生成针对性修订
    → 规则：每条建议必须指向具体 section + 修改内容 + 原因
    → IF 改动 Frontmatter：校验 title/version/created/tags 等齐全

5. [文档更新+验证] → 输出修订并闭环
    → 保持原有结构，补充缺失、修正错误
    → THEN 重跑 uSkill_upgrade_audit.py，对比 before/after_score
    → IF after_score 仍不达标：返回步骤 2 二次迭代
```

---

## 📝 Prompt 模板

### 标准优化 Prompt

```
你是 Skill 优化 Agent。请对照 Gen3 标准优化以下 Skill。

【Skill 文档】{skill_doc}
【执行反馈】{execution_feedback}
【失败案例】{failure_cases}
【目标标准】{target_standard}

【优化维度】
1. Gen3 合规：9 模块 / IF≥3 / Self-Play≥5 / ≥200 行 / Frontmatter 齐全
2. 定义清晰度：概念是否精确、无歧义
3. 流程完整性：步骤是否有遗漏、是否有决策分支
4. 边界覆盖：异常是否处理、人工兜底是否明确
5. Prompt 准确性：模板槽位与指令是否有效

【硬性要求】
- 每条优化必须具体到 section，并说明修改原因
- 修订后必须可经 uSkill_upgrade_audit.py 验证

【输出格式】
严格按标准 JSON 输出，包含 root_cause、gen3_gap、issues、optimizations、verification。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 反馈信息不足 | 请求补充或仅做静态审计 | 基于文档本身分析 Gen3 gap |
| 无法定位缺陷 | 标"需进一步调查" | 输出通用改进建议清单 |
| 多个问题并存 | 按严重度排序 | 优先修复 P0（Gen3 硬约束） |
| 审计脚本缺失 | 改用人工清单核对 | 逐项比对 9 模块标准 |
| 修订引入新冲突 | 回滚该次 edit | 保留上一版并记录冲突原因 |

---

## ✅ 质量自检

- [ ] gen3_gap 覆盖全部 5 项硬约束且结论明确
- [ ] 每条 issue 都定位到具体 section
- [ ] 每条 optimization 含 change + reason，非泛泛而谈
- [ ] 涉及 Frontmatter 的改动已校验字段齐全
- [ ] verification 含可复跑的 rerun_cmd 与前后分对比
- [ ] 无虚构失败案例，引用真实现象

---

## 💡 使用示例

### 示例 1：Gen3 模块缺失

**输入**：
```json
{
  "skill_doc": "uSkill-邮件处理-v1.md",
  "execution_feedback": "审计未通过：仅 198 行，缺 ✅质量自检 模块",
  "failure_cases": ["uSkill_upgrade_audit 报 missing_module=质量自检"]
}
```

**输出**：
```json
{
  "root_cause": "文档在重构时遗漏了 ✅ 质量自检 模块，且总行数不足 200",
  "gen3_gap": [{"check": "9模块", "passed": false, "detail": "缺 ✅质量自检"}, {"check": "行数", "passed": false, "detail": "198<200"}],
  "issues": [{"type": "Schema不符", "severity": "P0", "description": "缺少质量自检 checklist", "section": "✅ 质量自检"}],
  "optimizations": [
    {"section": "✅ 质量自检", "change": "新增输出结构/内容/合规三类 checklist（≥6 项）", "reason": "满足 Gen3 9 模块硬约束"},
    {"section": "全文", "change": "扩充使用示例至 2 个边界场景，+12 行", "reason": "行数达 200 阈值"}
  ],
  "verification": {"before_score": 71, "after_score": 100, "rerun_cmd": "python3 uSkill_upgrade_audit.py uSkill-邮件处理-v1.md"}
}
```

### 示例 2：执行超时（边界）

**输入**：
```json
{
  "skill_doc": "风控Agent",
  "execution_feedback": "风控 Agent 执行超时（连续 3 次 >30s）",
  "failure_cases": ["遍历全部规则导致超时"]
}
```

**输出**：
```json
{
  "root_cause": "规则匹配逻辑过于复杂，每次执行需遍历全部规则且无超时保护",
  "gen3_gap": [{"check": "IF/THEN", "passed": true, "detail": "分支足够"}, {"check": "边界覆盖", "passed": false, "detail": "缺超时异常处理"}],
  "issues": [{"type": "边界遗漏", "severity": "P0", "description": "执行流程缺少超时/中断分支", "section": "🔄 执行流程"}],
  "optimizations": [
    {"section": "🔄 执行流程", "change": "增加：IF 单次执行>10s 则中断并降级为简单规则", "reason": "避免无限等待"},
    {"section": "⚠️ 异常处理", "change": "增加超时行：记录日志+降级", "reason": "保证可用性"}
  ],
  "verification": {"before_score": 68, "after_score": 94, "rerun_cmd": "python3 uSkill_upgrade_audit.py 风控Agent"}
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 模块缺失 | 标 P0 gap + 补模块 |
| 2 | 定义不清 | 重写定义到 section |
| 3 | 流程缺失 | 补充步骤 + 分支 |
| 4 | 边界遗漏 | 补异常处理 |
| 5 | 执行超时 | 加超时分支 |
| 6 | 已达标 | "质量达标"结论 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得未经确认直接删除原文档，须保留可回滚版本
2. 不得泄露用户隐私数据
3. 修订不得破坏既有合规（如 AGENTS.md 硬约束），**必须**先审计再改

**软性约束（建议遵守）**：
1. 优先对齐已验证的 Gen3 Schema，而非临场发明结构
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当优化涉及其他 Agent/循环的核心契约时，**必须**转人工确认
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

**格式校验**：
- [ ] 输出结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义 JSON 规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - Gen3 标准本身发生变更

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的审计脚本停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---
---

*版本：v2.0 · 2026-07-08 Gen3 升级*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [任务类型] for [用户水平], with [约束条件], leaning toward [方法/工具]."

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


**相关概念**：[[三大Agent-Skills框架方法论对比]] · [[Agent-Skills标准化爆发深度分析]]

---

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
