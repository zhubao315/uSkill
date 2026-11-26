
description: |
  当用户需要进行头脑风暴、产品创新、问题解决、创意策划时使用此 Skill。
  触发词包括：'创意'、'头脑风暴'、'创新'、'发散思维'、'SCAMPER'、
  '六顶思考帽'、'类比联想'。
  不适用于执行层面（使用其他专项技能）。当需要产生大量创意选项时优先使用。

---

# uSkill-609: 创意发散

## 🎯 目标

> 运用 SCAMPER、头脑风暴、六顶思考帽、类比联想等方法，产生大量创新方案。

**核心价值**：创意不是天赋，而是可训练的技能。系统化方法能持续产出好点子。

**适用场景**：
- 产品创新
- 问题解决
- 创意策划
- 头脑风暴
- 方案设计
- 创新工作坊

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `challenge` | `string` | ✅ | — | 需要解决的问题/挑战 |
| `constraints` | `array` | ❌ | `[]` | 限制条件 |
| `method` | `enum` | ❌ | `auto` | `auto` / `scamper` / `brainstorm` / `six_hats` / `analogy` |
| `team_size` | `number` | ❌ | `1` | 参与人数 |
| `time_limit` | `number` | ❌ | `30` | 时间限制（分钟） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话创意建议",
  "ideation_id": "IDE-YYYY-MMDD-NNN",

  "method_selection": {
    "primary": "string",
    "secondary": "string",
    "rationale": "string"
  },

  "ideas_generated": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "method_used": "string",
      "novelty_score": "number",
      "feasibility_score": "number",
      "combined_score": "number"
    }
  ],

  "scamper_output": {
    "substitute": ["string"],
    "combine": ["string"],
    "adapt": ["string"],
    "modify": ["string"],
    "put_to_other_use": ["string"],
    "eliminate": ["string"],
    "reverse": ["string"]
  },

  "six_hats_output": {
    "white": "string",
    "red": "string",
    "black": "string",
    "yellow": "string",
    "green": "string",
    "blue": "string"
  },

  "analogy_output": {
    "source_domain": "string",
    "analogies": [
      {
        "source": "string",
        "mapping": "string",
        "insight": "string"
      }
    ]
  },

  "evaluation": {
    "top_ideas": ["string"],
    "next_steps": ["string"],
    "risks": ["string"]
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

### Step 1: 方法选择

- **输入**：`challenge` + `constraints` + `team_size`
- **动作**：
  1. 分析问题类型
  2. 选择最适合的方法
  3. 确定使用策略
- **输出**：`method_selection`
- **方法选择指南**：

| 方法 | 适用场景 | 优势 | 局限 |
|------|----------|------|------|
| SCAMPER | 产品改进 | 系统全面 | 需要经验 |
| 头脑风暴 | 开放式问题 | 快速产出 | 质量参差 |
| 六顶思考帽 | 复杂决策 | 多角度分析 | 耗时较长 |
| 类比联想 | 创新突破 | 跨界启发 | 需要知识储备 |

**分支条件**：
- 若 `team_size > 5` → 优先使用六顶思考帽
- 若 `team_size = 1` → 优先使用 SCAMPER 或类比联想
- 若 `time_limit < 15分钟` → 优先使用头脑风暴
- 若 `time_limit > 30分钟` → 综合使用多种方法
- 若问题为"改进现有产品" → 优先使用 SCAMPER
- 若问题为"创造全新方案" → 优先使用类比联想
- 若问题涉及"团队决策" → 优先使用六顶思考帽

### Step 2: SCAMPER 分析

- **输入**：`challenge` + `constraints`
- **动作**：
  1. 逐一应用 SCAMPER 七个维度
  2. 产生创意变体
  3. 筛选可行方案
- **输出**：`scamper_output`
- **SCAMPER 维度指南**：

| 维度 | 问题 | 示例 |
|------|------|------|
| Substitute | 可以替换什么？ | 材料、流程、人员 |
| Combine | 可以组合什么？ | 功能、服务、渠道 |
| Adapt | 可以借鉴什么？ | 其他行业、自然、历史 |
| Modify | 可以改变什么？ | 形状、大小、颜色、流程 |
| Put to other use | 可以用在其他地方吗？ | 新市场、新用户、新用途 |
| Eliminate | 可以去除什么？ | 步骤、功能、成本 |
| Reverse | 可以颠倒什么？ | 顺序、角色、方向 |

**分支条件**：
- 若约束条件多 → 重点关注 Substitute 和 Eliminate
- 若需要突破性创新 → 重点关注 Reverse 和 Put to other use
- 若需要渐进式改进 → 重点关注 Modify 和 Combine
- 若需要借鉴 → 重点关注 Adapt

### Step 3: 头脑风暴

- **输入**：`challenge` + `team_size`
- **动作**：
  1. 设定规则
  2. 快速产生想法
  3. 不批判，只产出
- **输出**：`ideas_generated`（部分）
- **头脑风暴规则**：

| 规则 | 说明 |
|------|------|
| 延迟判断 | 先产出，后评估 |
| 追求数量 | 数量产生质量 |
| 疯狂想法 | 鼓励大胆 |
| 组合改进 | 在他人想法上发展 |
| 一次一人 | 避免打断 |

**分支条件**：
- 若 `team_size = 1` → 使用个人头脑风暴变体
- 若 `team_size > 5` → 分组进行
- 若 `time_limit < 15分钟` → 聚焦核心问题
- 若 `time_limit > 30分钟` → 增加自由联想环节

### Step 4: 六顶思考帽分析

- **输入**：`challenge` + `constraints`
- **动作**：
  1. 逐一戴上六顶帽子
  2. 从不同角度分析
  3. 综合各角度见解
- **输出**：`six_hats_output`
- **六顶帽子指南**：

| 帽子 | 角色 | 问题 |
|------|------|------|
| 白帽 | 事实 | 有什么数据和事实？ |
| 红帽 | 直觉 | 我的直觉是什么？ |
| 黑帽 | 风险 | 有什么风险和问题？ |
| 黄帽 | 价值 | 有什么好处和价值？ |
| 绿帽 | 创意 | 有什么新想法？ |
| 蓝帽 | 控制 | 我们的思考过程如何？ |

**分支条件**：
- 若问题复杂 → 增加白帽和黑帽时间
- 若需要创新 → 增加绿帽时间
- 若团队情绪化 → 增加红帽时间
- 若需要决策 → 增加黄帽和黑帽对比

### Step 5: 类比联想

- **输入**：`challenge`
- **动作**：
  1. 选择源领域
  2. 建立映射关系
  3. 提取洞察
- **输出**：`analogy_output`
- **类比源领域**：

| 领域 | 适用问题 | 示例 |
|------|----------|------|
| 自然界 | 生物设计问题 | 仿生学 |
| 历史 | 组织管理问题 | 古代战争策略 |
| 其他行业 | 流程优化问题 | 航空业安全检查 |
| 艺术 | 体验设计问题 | 戏剧叙事 |
| 体育 | 团队协作问题 | 球队战术 |

**分支条件**：
- 若问题为技术性 → 优先选择科技领域类比
- 若问题为管理性 → 优先选择历史或体育类比
- 若问题为体验性 → 优先选择艺术或自然类比
- 若需要突破性 → 选择完全不同的领域

### Step 6: 评估与筛选

- **输入**：所有前序输出
- **动作**：
  1. 评估每个创意
  2. 筛选 Top 方案
  3. 确定下一步行动
- **输出**：`evaluation`
- **评估标准**：

| 标准 | 权重 | 评估方法 |
|------|------|----------|
| 新颖性 | 25% | 1-10分 |
| 可行性 | 30% | 1-10分 |
| 价值性 | 25% | 1-10分 |
| 风险性 | 20% | 1-10分（反向） |

**分支条件**：
- 若所有方案得分 < 6 → 重新发散
- 若方案可行性低 → 简化方案
- 若方案新颖性低 → 增加类比联想
- 若方案风险高 → 增加黑帽分析

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**在发散阶段进行批判
2. **不得**忽视任何创意（即使看似荒谬）
3. **必须**确保创意与问题相关
4. **必须**尊重参与者的想法

### 软性约束（建议遵守）
1. 建议设定明确的时间限制
2. 建议记录所有想法
3. 建议在评估前完成发散
4. 建议结合多种方法

### 人工兜底点
- 当创意枯竭时，**必须**休息或换方法
- 当团队冲突时，**必须**使用六顶思考帽
- 当方案不可行时，**必须**回到问题定义

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IDE_WARNING_BLOCK` | 创意枯竭 | 建议休息或换方法 | 🟡 |
| `IDE_WARNING_SCOPE` | 创意偏离问题 | 建议重新定义问题 | 🟡 |
| `IDE_ERROR_NO_IDEA` | 无法产生创意 | 建议简化问题 | 🔴 |
| `IDE_WARNING_TEAM` | 团队冲突 | 建议使用六顶思考帽 | 🟡 |
| `IDE_WARNING_TIME` | 时间不足 | 建议聚焦核心 | 🟡 |
| `IDE_WARNING_FEASIBILITY` | 方案不可行 | 建议增加约束条件 | 🟡 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 创意数量达到目标

### 内容校验
- [ ] 方法选择合适
- [ ] SCAMPER 分析完整
- [ ] 六顶帽子分析全面
- [ ] 类比联想有洞察
- [ ] 评估标准合理

### OVP 验证信号
- 创意产出量 ≥ 20个可行方案
- 方案可行性评分 ≥ 7/10
- 创新度评分 ≥ 7/10

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 创意数量不足 | 增加发散时间 | P1 |
| 创意质量不高 | 换用其他方法 | P1 |
| 方案不可行 | 增加约束条件 | P1 |
| 团队参与度低 | 调整引导方式 | P2 |
| 评估标准不合理 | 重新设定标准 | P2 |

---

## 📝 自检清单

- [ ] 问题定义是否清晰？
- [ ] 方法选择是否合适？
- [ ] SCAMPER 是否逐项分析？
- [ ] 头脑风暴是否遵循规则？
- [ ] 六顶帽子是否全面覆盖？
- [ ] 类比联想是否有洞察？
- [ ] 评估标准是否合理？
- [ ] 是否产生了足够数量的创意？
- [ ] 是否避免了思维定式？
- [ ] 是否考虑了实际约束？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-609-01",
  "name": "产品创新头脑风暴",
  "prompt": "为智能音箱设计5个创新功能",
  "input": {
    "challenge": "智能音箱功能同质化严重，需要创新功能",
    "constraints": ["技术可行", "成本可控"],
    "method": "auto",
    "team_size": 1,
    "time_limit": 20
  },
  "assertions": [
    "method_selection.primary 已选择",
    "ideas_generated.length >= 5",
    "scamper_output 包含7个维度",
    "evaluation.top_ideas 包含推荐方案"
  ],
  "expected_behavior": "产生至少5个可行的创新功能",
  "critic_attack": "创意是否足够新颖？是否考虑了技术约束？"
}
```

### 测试用例 2
```json
{
  "id": "test-609-02",
  "name": "团队效率问题解决",
  "prompt": "如何提高远程团队的协作效率？",
  "input": {
    "challenge": "远程团队沟通效率低，项目进度慢",
    "constraints": ["预算有限", "现有工具"],
    "method": "six_hats",
    "team_size": 6,
    "time_limit": 45
  },
  "assertions": [
    "six_hats_output 包含6顶帽子分析",
    "ideas_generated.length >= 10",
    "evaluation.risks 包含风险分析",
    "evaluation.next_steps 包含行动计划"
  ],
  "expected_behavior": "通过多角度分析找到解决方案",
  "critic_attack": "是否考虑了团队成员的不同观点？方案是否可执行？"
}
```

### 测试用例 3
```json
{
  "id": "test-609-03",
  "name": "营销活动创意",
  "prompt": "为新品牌设计一个病毒式营销活动",
  "input": {
    "challenge": "新品牌需要快速获得知名度",
    "constraints": ["预算50万", "3个月内"],
    "method": "scamper",
    "team_size": 3,
    "time_limit": 30
  },
  "assertions": [
    "scamper_output 包含7个维度",
    "ideas_generated.length >= 8",
    "ideas_generated 包含病毒传播元素",
    "evaluation.top_ideas 包含推荐方案"
  ],
  "expected_behavior": "产生有传播力的营销创意",
  "critic_attack": "创意是否足够有趣？是否能引起分享？"
}
```

### 测试用例 4
```json
{
  "id": "test-609-04",
  "name": "跨领域类比创新",
  "prompt": "如何借鉴航空业的安全管理来改进医疗流程？",
  "input": {
    "challenge": "医疗流程中人为错误导致安全事故",
    "constraints": ["法规要求", "现有流程"],
    "method": "analogy",
    "team_size": 1,
    "time_limit": 25
  },
  "assertions": [
    "analogy_output.source_domain = 航空业",
    "analogy_output.analogies.length >= 3",
    "analogy_output.analogies 包含具体映射",
    "evaluation.top_ideas 包含可行方案"
  ],
  "expected_behavior": "通过跨领域类比产生创新方案",
  "critic_attack": "类比是否合理？映射是否准确？方案是否适用于医疗？"
}
```

### 测试用例 5
```json
{
  "id": "test-609-05",
  "name": "服务设计创新",
  "prompt": "重新设计图书馆的服务体验",
  "input": {
    "challenge": "传统图书馆服务模式不适应数字时代",
    "constraints": ["预算有限", "保持核心功能"],
    "method": "brainstorm",
    "team_size": 4,
    "time_limit": 30
  },
  "assertions": [
    "ideas_generated.length >= 15",
    "ideas_generated 包含数字服务",
    "evaluation.top_ideas 包含可行性高的方案",
    "evaluation.risks 包含实施风险"
  ],
  "expected_behavior": "产生适应数字时代的服务创新",
  "critic_attack": "创意是否真正解决了用户痛点？是否考虑了技术趋势？"
}
```

---

## 🔗 关联文档

- [[文案写作]] — 创意的文案表达
- [[创意写作]] — 创意的故事化呈现
- [[说服力写作]] — 创意的说服力包装
- [[数据可视化]] — 创意的数据化展示
- [[内容改编]] — 创意的多形态改编

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：SCAMPER + 头脑风暴 + 六顶思考帽 + 类比联想 + Self-Play |

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


**相关概念**：[[头脑风暴]] · [[创造力的神经基础]] · [[灵魂被想法染色——习惯性思维决定心智状态]]

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
