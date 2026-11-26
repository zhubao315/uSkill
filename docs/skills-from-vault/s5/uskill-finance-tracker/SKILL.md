---
name: uskill-finance-tracker
description: "不知道钱花在哪，就永远赚不到更多的钱。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-finance-tracker.md"
  original_id: "SKL-6302"
  version: "3.0.0"
  trust: untrusted
---

# 财务健康追踪

description: |
  当用户需要追踪个人/项目财务健康、编制预算、分析现金流、生成财务报告时使用此 Skill。
  触发词：'财务追踪'、'预算'、'现金流'、'财务报表'、'记账'、'finance tracking'。

# 财务健康追踪

## 🎯 目标

> 建立从数据采集到洞察输出的财务追踪体系，让每一笔收支都有去处。

**核心价值**：财务追踪的核心不是记账，是「通过数据理解钱的流向并做出更好的决策」。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `scope` | enum | ✅ | — | 范围：`personal`（个人）/ `project`（项目）/ `business`（业务） |
| `data_source` | string | ✅ | — | 数据源（银行流水/Excel/手动输入） |
| `report_frequency` | enum | ❌ | `"monthly"` | 报告频率：`weekly` / `monthly` / `quarterly` |
| `budget_mode` | enum | ❌ | `"zero_based"` | 预算模式：`zero_based`（零基）/ `incremental`（增量）/ `flexible`（弹性） |

## 📤 输出

```json
{
  "financial_summary": {
    "income": "string — 收入汇总",
    "expenses": "string — 支出汇总（按类别）",
    "net_flow": "string — 净现金流",
    "savings_rate": "float — 储蓄率 (%)"
  },
  "budget_variance": [{"category": "string", "budget": "int", "actual": "int", "variance": "int", "reason": "string"}],
  "cashflow_forecast": {"next_3_months": "string — 未来 3 个月现金流预测"},
  "recommendations": ["string — 财务优化建议"]
}
```

## 📋 执行步骤

### Step 1: 数据采集与分类
1. **数据导入** — 从银行/支付平台导出交易记录
2. **自动分类** — 按预设规则自动分类（餐饮/交通/办公等）
3. **异常标记** — 标记大额/异常交易供人工确认
4. **检查点**：✅ 交易是否全部导入？分类是否准确？

### Step 2: 预算对比
1. **预算编制** — 按类别设定月度预算
2. **实际 vs 预算** — 逐项对比偏差
3. **偏差分析** — 超支/节余的原因分析
4. **检查点**：✅ 预算是否合理？偏差是否有原因分析？

### Step 3: 现金流预测
1. **收入预测** — 基于已确认的收入来源
2. **支出预测** — 基于历史支出模式 + 已知大额支出
3. **余额预测** — 预测未来 3 个月的账户余额
4. **检查点**：✅ 预测是否考虑了已知大额支出？

### Step 4: 优化建议
1. **节流建议** — 哪些支出可以优化
2. **开源建议** — 收入增长机会
3. **投资建议** — 闲置资金的配置建议
4. **检查点**：✅ 建议是否具体可执行？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 数据缺失 | 某月数据不完整 | 标记缺失，基于已有数据估算 |
| 分类争议 | 交易无法自动分类 | 人工确认后更新分类规则 |
| 预算偏差大 | 超支 >30% | 重新评估预算合理性 |

## 💬 沟通风格

- **数字精确**：金额精确到分，百分比精确到小数点
- **趋势导向**：不只看当月，还要看趋势
- **建议具体**：不说「节省开支」，说「外卖支出从 3000 降到 2000」

## 📝 自检清单

- [ ] 交易是否全部导入且分类准确？
- [ ] 预算偏差是否分析了原因？
- [ ] 现金流预测是否覆盖未来 3 个月？
- [ ] 优化建议是否具体可执行？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Finance Tracker |


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
- [ ] 输出 Context R

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
