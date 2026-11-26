
description: |
  当用户需要撰写提案、影响力建设、谈判准备、政策建议时使用此 Skill。
  触发词包括：'说服'、'提案'、'影响力'、'论证'、'修辞'、
  'Cialdini'、'谈判'。
  不适用于营销文案（使用文案写作）。当需要深度说服和论证时优先使用。

---

# uSkill-610: 说服力写作

## 🎯 目标

> 运用 Cialdini 六大影响力原则，构建严密的论证结构，创作有说服力的内容。

**核心价值**：说服不是操纵，而是帮助受众理解并接受正确的观点。

**适用场景**：
- 提案写作
- 影响力建设
- 谈判准备
- 政策建议
- 学术论文
- 商业计划

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `position` | `string` | ✅ | — | 需要论证的立场/观点 |
| `audience` | `string` | ✅ | — | 目标受众 |
| `context` | `string` | ✅ | — | 应用场景 |
| `evidence` | `array` | ❌ | `[]` | 已有证据/数据 |
| `style` | `enum` | ❌ | `logical` | `logical` / `emotional` / `balanced` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话说服策略建议",
  "persuasion_id": "PRSU-YYYY-MMDD-NNN",

  "influence_principles": {
    "reciprocity": "string",
    "commitment": "string",
    "social_proof": "string",
    "authority": "string",
    "liking": "string",
    "scarcity": "string"
  },

  "argument_structure": {
    "thesis": "string",
    "premises": ["string"],
    "evidence": ["string"],
    "counterarguments": ["string"],
    "rebuttals": ["string"],
    "conclusion": "string"
  },

  "rhetoric_techniques": [
    {
      "technique": "string",
      "description": "string",
      "application": "string"
    }
  ],

  "logical_framework": {
    "type": "string",
    "structure": "string",
    "flow": ["string"]
  },

  "psychological_hooks": {
    "emotional_appeals": ["string"],
    "cognitive_biases": ["string"],
    "framing_strategies": ["string"]
  },

  "delivery_recommendations": {
    "tone": "string",
    "pacing": "string",
    "emphasis": ["string"]
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

### Step 1: 影响力原则分析

- **输入**：`position` + `audience` + `context`
- **动作**：
  1. 分析受众心理
  2. 选择适合的影响力原则
  3. 设计应用策略
- **输出**：`influence_principles`
- **Cialdini 六大原则**：

| 原则 | 原理 | 应用方法 |
|------|------|----------|
| 互惠 | 给予后获得 | 提供价值后再请求 |
| 承诺一致 | 言行一致 | 获取小承诺 |
| 社会认同 | 从众心理 | 展示他人选择 |
| 权威 | 信任专家 | 引用权威观点 |
| 喜好 | 喜欢则同意 | 建立好感 |
| 稀缺 | 害怕失去 | 强调稀缺性 |

**分支条件**：
- 若 `context=商业提案` → 优先使用权威和互惠
- 若 `context=政策建议` → 优先使用社会认同和权威
- 若 `context=谈判` → 优先使用承诺一致和稀缺
- 若 `context=学术论文` → 优先使用权威和逻辑论证
- 若受众为理性人群 → 优先使用逻辑论证
- 若受众为感性人群 → 优先使用情感诉求

### Step 2: 论证结构设计

- **输入**：`position` + `evidence`
- **动作**：
  1. 确定核心论点
  2. 构建论证结构
  3. 准备反驳回应
- **输出**：`argument_structure`
- **论证结构类型**：

| 类型 | 结构 | 适用场景 |
|------|------|----------|
| 演绎法 | 大前提-小前提-结论 | 逻辑严密的论证 |
| 归纳法 | 案例-规律-结论 | 经验性论证 |
| 溯因法 | 结果-原因-解释 | 解释性论证 |
| 辩证法 | 正-反-合 | 复杂问题讨论 |

**分支条件**：
- 若有大量数据支持 → 使用归纳法
- 若需要逻辑严密 → 使用演绎法
- 若需要解释现象 → 使用溯因法
- 若存在争议 → 使用辩证法

### Step 3: 修辞技巧应用

- **输入**：`argument_structure` + `style`
- **动作**：
  1. 选择修辞技巧
  2. 应用到论证中
  3. 增强说服力
- **输出**：`rhetoric_techniques`
- **修辞技巧库**：

| 技巧 | 描述 | 示例 |
|------|------|------|
| 隐喻 | 类比说明 | "时间就是金钱" |
| 排比 | 增强气势 | "我们需要...我们需要...我们需要..." |
| 反问 | 引发思考 | "难道我们不应该...吗？" |
| 对比 | 突出差异 | "过去...现在..." |
| 故事 | 情感共鸣 | "让我讲一个故事..." |
| 数据 | 理性支撑 | "数据显示..." |

**分支条件**：
- 若 `style=logical` → 优先使用数据和对比
- 若 `style=emotional` → 优先使用故事和隐喻
- 若 `style=balanced` → 综合使用各种技巧
- 若 `audience=专业人士` → 减少情感技巧
- 若 `audience=普通大众` → 增加情感技巧

### Step 4: 心理钩子设计

- **输入**：`position` + `audience`
- **动作**：
  1. 设计情感诉求
  2. 识别认知偏差
  3. 确定框架策略
- **输出**：`psychological_hooks`
- **认知偏差应用**：

| 偏差 | 原理 | 应用方法 |
|------|------|----------|
| 锚定效应 | 先入为主 | 提供参考点 |
| 损失厌恶 | 害怕失去 | 强调损失 |
| 确认偏差 | 符合预期 | 符合既有观点 |
| 从众效应 | 随大流 | 展示多数选择 |
| 光环效应 | 以偏概全 | 突出正面特质 |

**分支条件**：
- 若需要理性决策 → 减少认知偏差应用
- 若需要快速决策 → 适当应用认知偏差
- 若涉及伦理考量 → 谨慎使用心理技巧
- 若 `context=学术` → 避免使用认知偏差

### Step 5: 论证完善与交付

- **输入**：所有前序输出
- **动作**：
  1. 检查逻辑严密性
  2. 优化表达方式
  3. 确定交付策略
- **输出**：`delivery_recommendations`
- **交付策略**：

| 策略 | 目的 | 适用场景 |
|------|------|----------|
| 渐进式 | 逐步推进 | 复杂论证 |
| 冲击式 | 强烈开场 | 需要关注 |
| 故事式 | 情感共鸣 | 需要认同 |
| 数据式 | 理性说服 | 需要信任 |

**分支条件**：
- 若 `context=提案` → 使用渐进式
- 若 `context=演讲` → 使用故事式或冲击式
- 若 `context=书面` → 使用渐进式或数据式
- 若 `context=谈判` → 根据对方风格调整

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**使用欺骗性论证
2. **不得**隐瞒重要信息
3. **必须**确保论证真实可信
4. **必须**尊重受众的理性判断

### 软性约束（建议遵守）
1. 建议保持论证的平衡性
2. 建议准备反驳回应
3. 建议使用适当的修辞技巧
4. 建议考虑伦理影响

### 人工兜底点
- 当涉及敏感话题时，**必须**谨慎处理
- 当需要专业论证时，**必须**建议专业帮助
- 当受众情绪化时，**必须**调整策略

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `PRSU_WARNING_LOGIC` | 逻辑漏洞 | 建议修正论证 | 🟡 |
| `PRSU_WARNING_EVIDENCE` | 证据不足 | 建议补充证据 | 🟡 |
| `PRSU_ERROR_ETHICS` | 伦理问题 | 建议修改策略 | 🔴 |
| `PRSU_WARNING_AUDIENCE` | 不适合受众 | 建议调整风格 | 🟡 |
| `PRSU_WARNING_CULTURAL` | 文化敏感性 | 建议修改内容 | 🟡 |
| `PRSU_ERROR_FALLACY` | 逻辑谬误 | 建议修正论证 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 论证结构完整

### 内容校验
- [ ] 影响力原则应用恰当
- [ ] 论证逻辑严密
- [ ] 修辞技巧使用得当
- [ ] 无逻辑谬误
- [ ] 伦理考量充分

### OVP 验证信号
- 说服成功率 ≥ 70%
- 目标达成率 ≥ 80%
- 反馈满意度 ≥ 85%

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 逻辑漏洞 | 修正论证结构 | P1 |
| 证据不足 | 补充证据 | P1 |
| 受众不接受 | 调整说服策略 | P1 |
| 反驳有力 | 准备回应 | P2 |
| 伦理问题 | 修改策略 | P0 |

---

## 📝 自检清单

- [ ] 立场是否明确？
- [ ] 受众是否清晰？
- [ ] 影响力原则是否恰当？
- [ ] 论证结构是否严密？
- [ ] 证据是否充分？
- [ ] 修辞技巧是否得当？
- [ ] 是否有逻辑谬误？
- [ ] 是否考虑了反驳？
- [ ] 是否符合伦理？
- [ ] 是否准备了交付策略？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-610-01",
  "name": "投资提案",
  "prompt": "为一个创业项目撰写投资提案",
  "input": {
    "position": "我们的AI教育平台值得投资",
    "audience": "天使投资人",
    "context": "商业提案",
    "evidence": ["市场数据", "团队背景", "技术优势"],
    "style": "balanced"
  },
  "assertions": [
    "influence_principles 包含权威和互惠",
    "argument_structure.thesis 明确",
    "argument_structure.evidence 包含市场数据",
    "rhetoric_techniques 包含数据和故事"
  ],
  "expected_behavior": "创作有说服力的投资提案",
  "critic_attack": "论证是否严密？是否能打动投资人？"
}
```

### 测试用例 2
```json
{
  "id": "test-610-02",
  "name": "政策建议",
  "prompt": "为教育政策改革撰写建议书",
  "input": {
    "position": "应该增加STEM教育投入",
    "audience": "教育部门决策者",
    "context": "政策建议",
    "evidence": ["国际比较数据", "就业市场分析", "学生反馈"],
    "style": "logical"
  },
  "assertions": [
    "influence_principles 包含社会认同和权威",
    "argument_structure.premises 包含多条论证",
    "logical_framework.type = 归纳法或演绎法",
    "delivery_recommendations.tone = 专业"
  ],
  "expected_behavior": "创作有数据支撑的政策建议",
  "critic_attack": "论证是否基于可靠数据？是否考虑了多方观点？"
}
```

### 测试用例 3
```json
{
  "id": "test-610-03",
  "name": "谈判策略",
  "prompt": "为薪资谈判准备说服材料",
  "input": {
    "position": "我的薪资应该提升20%",
    "audience": "直属上级",
    "context": "谈判准备",
    "evidence": ["绩效数据", "市场薪资", "额外贡献"],
    "style": "balanced"
  },
  "assertions": [
    "influence_principles 包含承诺一致和稀缺",
    "argument_structure.counterarguments 包含可能反驳",
    "argument_structure.rebuttals 包含回应",
    "psychological_hooks.framing_strategies 包含框架"
  ],
  "expected_behavior": "准备有说服力的谈判材料",
  "critic_attack": "是否考虑了对方的立场？是否准备了让步空间？"
}
```

### 测试用例 4
```json
{
  "id": "test-610-04",
  "name": "学术论文论证",
  "prompt": "为一篇学术论文构建论证结构",
  "input": {
    "position": "远程工作提高生产力",
    "audience": "学术同行",
    "context": "学术论文",
    "evidence": ["研究数据", "案例分析", "理论支持"],
    "style": "logical"
  },
  "assertions": [
    "argument_structure.premises 逻辑严密",
    "argument_structure.evidence 包含学术引用",
    "logical_framework.type = 演绎法",
    "delivery_recommendations.tone = 学术"
  ],
  "expected_behavior": "构建严密的学术论证",
  "critic_attack": "论证是否基于可靠研究？是否避免了逻辑谬误？"
}
```

### 测试用例 5
```json
{
  "id": "test-610-05",
  "name": "变革推动提案",
  "prompt": "说服公司采用新的项目管理方法",
  "input": {
    "position": "应该采用敏捷开发方法",
    "audience": "公司高层",
    "context": "变革提案",
    "evidence": ["行业案例", "效率数据", "团队反馈"],
    "style": "balanced"
  },
  "assertions": [
    "influence_principles 包含社会认同和权威",
    "argument_structure 包含正反合",
    "rhetoric_techniques 包含故事和数据",
    "psychological_hooks 包含损失厌恶"
  ],
  "expected_behavior": "创作推动变革的提案",
  "critic_attack": "是否考虑了变革阻力？是否提供了过渡方案？"
}
```

---

## 🔗 关联文档

- [[文案写作]] — 说服力的文案表达
- [[创意写作]] — 说服力的故事化呈现
- [[创意发散]] — 说服策略的发散思维
- [[数据可视化]] — 说服力的数据支撑
- [[内容改编]] — 说服内容的多形态改编

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：Cialdini原则 + 论证结构 + 修辞技巧 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Gen3 Skill Schema*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [摄影场景] for [拍摄者水平], with [创作优先级], leaning toward [器材/环境约束]."

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
| ""直接给一组参数就行了"" | "不知道用户场景就给参数，是赌博不是指导" |
| ""ISO 高一点没关系"" | "后期降噪损失细节，能前期解决就别留后期" |
| ""先拍一张试试看"" | "曝光三角的价值在于拍前就知道结果" |
| ""这个场景太简单了"" | "越简单越容易犯低级错误" |
| ""用户没问安全快门"" | "安全快门是糊片第一道防线，必须主动检查" |

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


**相关概念**：[[事实与观点]] · [[积极倾听]]

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
