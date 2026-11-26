# IM报告撰写（投资备忘录）

> **角色**: 投资经理 | **核心工具**: AI大模型, 财务模型, 行业数据库 | **效率目标**: 标准化输出高质量投资备忘录

## 🎯 目标
系统化完成投资备忘录(IM)的10章结构化撰写，覆盖项目启动、IC汇报、LP报告三大场景，确保分析深度与格式一致性。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `company_name` | string | ✅ | 标的公司全称 |
| `sector` | string | ✅ | 所属行业/赛道 |
| `deal_stage` | enum | ✅ | `screening` / `due_diligence` / `ic_presentation` / `lp_report` |
| `data_room` | object | ✅ | 尽调数据包（财务报表、业务数据、合同等） |
| `model_assumptions` | object | ❌ | 财务预测假设（增长率、利润率等） |
| `deal_terms` | object | ❌ | 交易条款信息（估值、对价、结构等） |
| `report_format` | enum | ❌ | `full` / `summary` / `ic_deck`，默认 `full` |

## 📤 输出

```json
{
  "report": {
    "chapter_1_executive_summary": {
      "investment_thesis": "string — 核心投资逻辑",
      "key_metrics": { "revenue": "number", "growth_rate": "number", "valuation": "string" },
      "recommendation": "enum — invest / pass / conditional_invest"
    },
    "chapter_2_company_info": { "overview": "string", "history": "string", "shareholders": "object" },
    "chapter_3_business_analysis": { "model": "string", "competitive_advantage": "string", "market_position": "string" },
    "chapter_4_revenue_sustainability": { "revenue_breakdown": "object", "sustainability_score": "number", "drivers": ["string"] },
    "chapter_5_financial_analysis": { "historical": "object", "key_ratios": "object", "quality_flags": ["string"] },
    "chapter_6_financial_forecast": { "projections": "object", "scenarios": ["string"], "assumptions": "object" },
    "chapter_7_deal_structure": { "valuation": "string", "terms": "object", "legal_considerations": "string" },
    "chapter_8_investment_return": { "irr": "number", "moic": "number", "payback_period": "string" },
    "chapter_9_risk_analysis": { "risk_matrix": "array", "mitigation": "object", "residual_risk": "string" },
    "chapter_10_conclusion": { "final_recommendation": "string", "next_steps": ["string"], "conditions": ["string"] }
  },
  "metadata": { "generated_at": "datetime", "version": "string", "author": "string" }
}
```

## 📋 执行步骤

### 阶段一：基础扫描（Basic Scan）

1. **收集公开信息** — 通过天眼查、招股书、行业报告获取公司基础数据
2. **初步筛选判断** — 验证项目是否符合基金投资策略与额度门槛，输出Pass/Proceed

### 阶段二：业务尽调（Business DD）

3. **行业与市场分析** — 评估TAM/SAM/SOM，绘制竞争格局图谱
4. **商业模式拆解** — 识别核心收入来源、客户集中度、定价能力与护城河
5. **管理层访谈** — 使用AI提示词模板(Prompt-3)结构化整理访谈要点

### 阶段三：财务尽调（Financial DD）

6. **历史财务分析** — 审阅3-5年报表，识别收入确认、关联交易、表外负债等质量风险
7. **财务质量校验** — 使用AI提示词模板(Prompt-5)生成财务质量评分卡

### 阶段四：建模（Modeling）

8. **构建财务模型** — 搭建DCF/可比估值模型，设定Base/Bull/Bear三种情景
9. **投资回报测算** — 计算IRR、MOIC、回收期，与基金要求回报对比

### 阶段五：综合撰写（Synthesis）

10. **逐章撰写** — 按10章框架依次填充内容，每章使用对应AI提示词模板
11. **交叉验证** — 确保各章节数据一致、逻辑自洽，财务预测与业务分析吻合
12. **风险矩阵编制** — 汇总所有风险因素，评估影响程度与发生概率
13. **执行摘要提炼** — 最后撰写第1章，确保决策者3分钟内掌握核心结论
14. **格式与合规检查** — 检查排版、数据标注、免责声明、合规要素完整性

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `data_room` 数据不完整 | 标注缺失项，使用公开数据补充并标记`[待确认]` |
| 财务数据勾稽不平 | 触发`ERROR_FINANCIAL_MISMATCH`，要求补充审计调整表 |
| 估值假设争议大 | 提供多情景估值区间，标注敏感性分析结果 |
| 管理层信息不可得 | 降级处理，标注`[未访谈]`并在风险章节反映 |
| IC汇报时间不足 | 切换为`report_format: ic_deck`，输出精简版 |

## ✅ 自检清单

- [ ] 10章结构完整，无遗漏章节
- [ ] 执行摘要包含核心投资逻辑、关键财务指标、明确推荐结论
- [ ] 财务预测三种情景(Bull/Base/Bear)均有呈现
- [ ] 风险矩阵覆盖市场、运营、财务、法律四维度
- [ ] 所有数据标注来源，`[待确认]`项已列出清单
- [ ] IRR/MOIC计算与投资门槛对比结论明确
- [ ] 格式符合基金IC材料标准，无排版错误


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
| 2026-05-09 | 1.0.0 | 初始版本，从SOP-025转化，建立10章框架与5阶段工作流 |

---
**相关笔记**：[[期权基础策略]] [[格雷厄姆安全边际分析]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [投资决策类型] for [投资者风格], with [风险偏好], leaning toward [分析框架/数据源]."

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
| ""这次不一样"" | "每次泡沫都说这次不一样，这次也一样" |
| ""先满仓再说"" | "满仓=零容错，一个回调就是灾难" |
| ""跌了就补仓"" | "越补越套是亏损扩大的主因" |
| ""长期持有就行"" | "长期持有不等于不做仓位管理" |
| ""这次消息是利好"" | "消息面驱动的交易成功率低于掷硬币" |

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
