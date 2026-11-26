
description: |
  当用户需要评估和改进 AI 系统的伦理合规性（偏见、公平性、可解释性、透明度）时使用此 Skill。
  触发词包括：'AI伦理'、'偏见检测'、'公平性'、'可解释性'、'透明度'、'算法审计'。
  当用户提到"AI 有偏见"、"不公平"、"不知道为什么这样输出"、"需要解释"时，
  即使未直接说"AI伦理"，也应使用此 Skill。
  不适用于性能优化。遇到 AI 安全和伦理合规时优先使用。

---

# uSkill-904: AI伦理

## 🎯 目标

> 评估和改进 AI 系统的伦理合规性，包括偏见检测、公平性评估、可解释性和透明度。

**核心价值**：确保 AI 系统公正、透明、可信赖，符合社会伦理和法规要求。

**适用场景**：
- AI 模型上线前审计
- 算法公平性评估
- 决策可解释性改进
- 合规性检查（GDPR、AI Act）
- AI 伦理培训

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `system_type` | `enum` | ✅ | — | `classification` / `generation` / `recommendation` / `decision` |
| `domain` | `string` | ✅ | — | 应用领域（如招聘、贷款、医疗） |
| `sensitive_attributes` | `array` | ❌ | `[]` | 需要检查的敏感属性 |
| `current_issues` | `array` | ❌ | `[]` | 已知的伦理问题 |
| `regulatory_requirements` | `array` | ❌ | `[]` | 需要遵守的法规 |

**输入约束**：
- `domain` 影响偏见检测的重点维度
- `sensitive_attributes` 应覆盖所有相关敏感属性
- `regulatory_requirements` 应明确具体的合规要求

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结 AI 伦理评估结果",
  "ethics_id": "AE-YYYY-MMDD-NNN",

  "bias_assessment": {
    "dimensions_checked": ["string"],
    "bias_metrics": [
      {
        "attribute": "string",
        "metric": "string",
        "value": "number",
        "threshold": "number",
        "status": "pass|fail|warning"
      }
    ],
    "root_cause_analysis": "string",
    "mitigation_strategies": ["string"]
  },

  "fairness_evaluation": {
    "fairness_definition": "string",
    "metrics": [
      {
        "name": "string",
        "value": "number",
        "target": "number",
        "explanation": "string"
      }
    ],
    "group_analysis": "string",
    "trade_offs": ["string"]
  },

  "explainability": {
    "method": "string",
    "features": [
      {
        "feature": "string",
        "importance": "number",
        "explanation": "string"
      }
    ],
    "decision_path": "string",
    "user_friendly_summary": "string"
  },

  "transparency": {
    "documentation": ["string"],
    "disclosure_items": ["string"],
    "limitation_disclosure": "string",
    "data_provenance": "string"
  },

  "compliance": {
    "regulations": [
      {
        "name": "string",
        "status": "compliant|non_compliant|partial",
        "gaps": ["string"],
        "remediation": ["string"]
      }
    ]
  },

  "recommendations": {
    "immediate": ["string"],
    "short_term": ["string"],
    "long_term": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 系统画像与风险评估

- **输入**：`system_type`, `domain`, `sensitive_attributes`
- **动作**：
  1. 分析系统类型和应用领域
  2. 识别潜在的伦理风险维度
  3. 评估风险等级
- **输出**：风险评估报告
- **分支条件**：
  - IF 领域是高风险（招聘、贷款、医疗）→ 全面审计
  - IF 领域是中风险（推荐、搜索）→ 重点审计
  - IF 领域是低风险（内容生成）→ 基础审计
  - IF 有已知问题 → 针对性深度审计
  - ELSE → 标准审计流程
- **检查点**：✅ 应验证风险维度覆盖完整

### Step 2: 偏见检测与分析

- **输入**：风险评估结果
- **动作**：
  1. 选择偏见检测指标
  2. 执行统计测试
  3. 分析偏见来源
- **输出**：`bias_assessment`
- **分支条件**：
  - IF 检测到显著偏见 → 进行根因分析
  - IF 偏见不显著但接近阈值 → 标记为预警
  - IF 偏见来源是数据 → 建议数据增强或重采样
  - IF 偏见来源是模型 → 建议去偏见技术
  - ELSE → 记录为通过
- **检查点**：✅ 应验证检测覆盖所有敏感属性

### Step 3: 公平性评估

- **输入**：`bias_assessment`
- **动作**：
  1. 选择公平性定义和指标
  2. 执行公平性测试
  3. 分析群体差异
- **输出**：`fairness_evaluation`
- **分支条件**：
  - IF 使用群体公平性 → 检查统计平等、机会平等
  - IF 使用个体公平性 → 检查相似个体相似对待
  - IF 存在公平性权衡 → 明确权衡并记录
  - IF 无法满足所有公平性标准 → 选择最适合的
  - ELSE → 使用默认公平性标准
- **检查点**：✅ 应验证公平性指标选择与领域匹配

### Step 4: 可解释性设计

- **输入**：`fairness_evaluation`
- **动作**：
  1. 选择可解释性方法
  2. 生成特征重要性分析
  3. 设计用户友好的解释
- **输出**：`explainability`
- **分支条件**：
  - IF 是黑盒模型 → 使用 LIME/SHAP 等事后解释
  - IF 是白盒模型 → 使用内在可解释性
  - IF 面向普通用户 → 使用自然语言解释
  - IF 面向技术人员 → 使用特征重要性图
  - ELSE → 选择通用可解释性方法
- **检查点**：✅ 应验证解释准确反映了模型决策过程

### Step 5: 透明度与合规报告

- **输入**：所有前序评估结果
- **动作**：
  1. 生成透明度文档
  2. 评估法规合规性
  3. 制定改进建议
- **输出**：`transparency`, `compliance`, `recommendations`
- **检查点**：✅ 应验证报告完整且可操作

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在高风险应用中跳过偏见检测
2. **不得**隐瞒已知的伦理问题
3. **必须**为每个决策提供可解释性支持
4. **必须**披露系统的局限性和已知偏见

### 软性约束（建议遵守**
1. 定期（至少每季度）重新评估伦理合规性
2. 建立伦理审查委员会或指定伦理负责人
3. 记录所有伦理相关的决策和权衡
4. 关注最新的法规和行业标准变化

### 人工兜底点
- 当检测到严重偏见且无法自动修复时，**必须**人工干预
- 当伦理权衡涉及重大利益时，**必须**升级到伦理委员会
- 当法规要求不明确时，**必须**咨询法律专家

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `AE_ERROR_SEVERE_BIAS` | 偏见指标 > 阈值 2 倍 | 暂停系统，人工审查 | 🔴 |
| `AE_WARNING_FAIRNESS_TRADEOFF` | 公平性指标冲突 | 记录权衡，请求人工决策 | 🟡 |
| `AE_ERROR_NO_EXPLANATION` | 无法生成有效解释 | 降低模型复杂度或使用代理模型 | 🔴 |
| `AE_WARNING_REGULATION_GAP` | 合规性存在缺口 | 制定整改计划，跟踪进度 | 🟡 |
| `AE_ERROR_DATA_BIAS` | 训练数据存在系统性偏见 | 建议数据清洗或增强 | 🔴 |

### 降级策略
- 当无法完全消除偏见时，至少披露偏见并监控
- 当可解释性方法不可用时，使用简化模型或增加人工审核
- 当合规要求冲突时，选择更严格的标准

---

## ✅ 校验验收规则

### 格式校验
- [ ] 评估报告结构完整
- [ ] 所有指标有明确数值
- [ ] 建议可执行

### 内容校验
- [ ] 偏见检测覆盖所有敏感属性
- [ ] 公平性指标选择合理
- [ ] 解释准确反映模型行为
- [ ] 合规评估覆盖所有相关法规

### 合规校验
- [ ] 已知偏见已披露
- [ ] 局限性已说明
- [ ] 人工兜底点已标注

### OVP 验证信号
- 偏见检测覆盖率 ≥ 95%
- 公平性指标达标率 ≥ 90%
- 可解释性满意度 ≥ 4.0/5.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "招聘系统偏见检测",
    "prompt": "我们用 AI 筛选简历，担心有性别偏见",
    "context": "system_type=classification, domain='招聘', sensitive_attributes=['gender', 'age']",
    "assertions": [
      "bias_assessment.dimensions_checked 包含 gender 和 age",
      "bias_metrics 每项有 value 和 threshold",
      "mitigation_strategies 提供具体去偏见方案"
    ],
    "expected_behavior": "全面检测招聘 AI 的性别和年龄偏见",
    "critic_attack": "是否考虑了交叉偏见？是否检查了间接歧视？"
  },
  {
    "id": "test-002",
    "name": "贷款公平性评估",
    "prompt": "我们的贷款审批 AI 对不同种族的通过率不同",
    "context": "system_type=decision, domain='贷款', sensitive_attributes=['race', 'income']",
    "assertions": [
      "fairness_evaluation 使用统计平等或机会平等",
      "trade_offs 明确了公平性与准确性的权衡",
      "compliance 检查了公平贷款法规"
    ],
    "expected_behavior": "评估贷款 AI 的公平性并提供合规建议",
    "critic_attack": "是否考虑了历史偏见的传递？"
  },
  {
    "id": "test-003",
    "name": "推荐系统可解释性",
    "prompt": "用户不知道为什么推荐这个商品，需要解释",
    "context": "system_type=recommendation, domain='电商'",
    "assertions": [
      "explainability.method 选择适合推荐系统的方法",
      "user_friendly_summary 清晰易懂",
      "features 包含推荐原因"
    ],
    "expected_behavior": "为推荐系统设计可解释性方案",
    "critic_attack": "解释是否真正帮助用户理解？是否过于技术化？"
  },
  {
    "id": "test-004",
    "name": "内容生成偏见",
    "prompt": "AI 生成的文本经常强化刻板印象",
    "context": "system_type=generation, domain='内容生成'",
    "assertions": [
      "bias_assessment 覆盖内容偏见维度",
      "mitigation_strategies 包含 prompt 优化",
      "transparency.disclosure_items 包含生成内容局限"
    ],
    "expected_behavior": "检测和改善生成内容的偏见",
    "critic_attack": "是否考虑了文化差异？"
  },
  {
    "id": "test-005",
    "name": "医疗 AI 透明度",
    "prompt": "医生需要知道 AI 为什么做出这个诊断建议",
    "context": "system_type=decision, domain='医疗', regulatory_requirements=['FDA']",
    "assertions": [
      "explainability.method 符合医疗领域要求",
      "compliance 检查了 FDA 要求",
      "transparency.disclosure_items 包含临床验证信息"
    ],
    "expected_behavior": "设计满足医疗监管要求的可解释性方案",
    "critic_attack": "是否满足了医疗器械的透明度要求？"
  },
  {
    "id": "test-006",
    "name": "多维度偏见交叉",
    "prompt": "需要同时检查性别、年龄、地域多个维度的偏见",
    "context": "system_type=classification, sensitive_attributes=['gender', 'age', 'region']",
    "assertions": [
      "bias_assessment 覆盖所有维度",
      "检查了交叉偏见（如年龄+性别）",
      "分析了偏见的来源（数据 vs 模型）"
    ],
    "expected_behavior": "进行多维度交叉偏见检测",
    "critic_attack": "是否检查了维度组合产生的偏见？"
  },
  {
    "id": "test-007",
    "name": "GDPR 合规检查",
    "prompt": "我们的 AI 系统需要符合 GDPR 的自动化决策条款",
    "context": "domain='欧盟市场', regulatory_requirements=['GDPR']",
    "assertions": [
      "compliance 检查了 GDPR 第 22 条",
      "explainability 支持数据主体的解释权",
      "transparency 包含数据处理说明"
    ],
    "expected_behavior": "评估 GDPR 合规性并提供整改建议",
    "critic_attack": "是否覆盖了所有 GDPR 相关条款？"
  },
  {
    "id": "test-008",
    "name": "公平性权衡决策",
    "prompt": "提高对少数群体的公平性会降低整体准确率，怎么平衡？",
    "context": "system_type=classification",
    "assertions": [
      "fairness_evaluation.trade_offs 明确列出了权衡",
      "提供了决策框架",
      "建议人工参与权衡决策"
    ],
    "expected_behavior": "帮助用户理解和做出公平性权衡决策",
    "critic_attack": "是否提供了足够的信息让用户做出知情决策？"
  },
  {
    "id": "test-009",
    "name": "偏见根因分析",
    "prompt": "检测到偏见，但不知道原因在哪里",
    "context": "current_issues=['检测到性别偏见']",
    "assertions": [
      "bias_assessment.root_cause_analysis 有具体分析",
      "区分了数据偏见和模型偏见",
      "提供了针对性的修复方案"
    ],
    "expected_behavior": "诊断偏见的根本原因并提供修复方案",
    "critic_attack": "根因分析是否准确？修复方案是否可行？"
  },
  {
    "id": "test-010",
    "name": "伦理培训材料",
    "prompt": "需要给开发团队做 AI 伦理培训",
    "context": "system_type=decision",
    "assertions": [
      "recommendations 包含培训建议",
      "transparency 包含可教学的案例",
      "提供了评估清单"
    ],
    "expected_behavior": "生成可用于团队培训的伦理指南",
    "critic_attack": "培训内容是否实用？是否涵盖了常见陷阱？"
  }
]
```

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🔗 关联文档

- [[信息污染检测]] — AI 信息质量检测
- [[逻辑谬误检测]] — 逻辑错误识别
- [[批判性思维]] — 批判性分析方法
- [[Prompt工程进阶]] — Prompt 中的伦理约束
- [[Agent架构设计模式]] — Agent 中的伦理模块

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：偏见检测/公平性/可解释性/透明度 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


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


**相关概念**：[[AI伦理与社会影响]] · [[全球贫困与道德责任]]

---



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


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
