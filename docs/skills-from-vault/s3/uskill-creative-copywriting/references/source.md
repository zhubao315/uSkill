
description: |
  当用户需要撰写营销文案、产品描述、广告创意、落地页时使用此 Skill。
  触发词包括：'文案'、'广告词'、'营销文案'、'产品描述'、'CTA'、
  '标题技巧'、'落地页'。
  不适用于演讲稿（使用演讲节奏控制）。当需要书面营销内容时优先使用。

---

# uSkill-608: 文案写作

## 🎯 目标

> 运用 AIDA/PAS/FAB 经典框架，创作高转化率的营销文案。

**核心价值**：好文案能驱动行动，差文案只能自说自话。

**适用场景**：
- 营销文案
- 产品描述
- 广告创意
- 落地页
- 邮件营销
- 社交媒体

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `product` | `string` | ✅ | — | 产品/服务描述 |
| `audience` | `string` | ✅ | — | 目标受众 |
| `goal` | `enum` | ✅ | — | `awareness` / `consideration` / `conversion` / `retention` |
| `medium` | `enum` | ❌ | `ad` | `ad` / `landing` / `email` / `social` / `product` |
| `tone` | `enum` | ❌ | `professional` | `professional` / `casual` / `humorous` / `urgent` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话文案建议",
  "copy_id": "CPY-YYYY-MMDD-NNN",

  "framework_selection": {
    "primary": "string",
    "secondary": "string",
    "rationale": "string"
  },

  "headline_options": [
    {
      "headline": "string",
      "type": "string",
      "score": "number"
    }
  ],

  "body_copy": {
    "opening": "string",
    "problem": "string",
    "solution": "string",
    "benefits": ["string"],
    "proof": ["string"],
    "closing": "string"
  },

  "cta_design": {
    "primary_cta": "string",
    "secondary_cta": "string",
    "urgency_element": "string",
    "placement": "string"
  },

  "copy_variations": [
    {
      "variant": "string",
      "tone": "string",
      "text": "string",
      "target_segment": "string"
    }
  ],

  "optimization_tips": {
    "a_b_test_suggestions": ["string"],
    "common_mistakes": ["string"],
    "improvement_areas": ["string"]
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

### Step 1: 框架选择

- **输入**：`product` + `audience` + `goal`
- **动作**：
  1. 分析产品特点
  2. 选择最适合的写作框架
  3. 确定写作策略
- **输出**：`framework_selection`
- **框架选择指南**：

| 框架 | 结构 | 适用场景 |
|------|------|----------|
| AIDA | 注意-兴趣-欲望-行动 | 广告、落地页 |
| PAS | 问题-激化-解决方案 | 痛点明确的产品 |
| FAB | 特性-优势-利益 | 技术产品、B2B |
| Before-After-Bridge | 之前-之后-桥梁 | 转化类文案 |
| PASTOR | 问题-放大-故事-转变-结果-响应 | 长文案、销售信 |

**分支条件**：
- 若 `goal=awareness` → 优先使用 AIDA
- 若 `goal=consideration` → 优先使用 PAS 或 FAB
- 若 `goal=conversion` → 优先使用 Before-After-Bridge
- 若 `goal=retention` → 优先使用 PASTOR

### Step 2: 标题创作

- **输入**：`framework_selection` + `audience`
- **动作**：
  1. 创作多个标题选项
  2. 评估标题吸引力
  3. 选择最佳标题
- **输出**：`headline_options`
- **标题技巧库**：

| 类型 | 结构 | 示例 |
|------|------|------|
| 数字型 | 数字+好处 | "5个方法让你..."
| 提问型 | 问题+答案 | "你知道...吗？" |
| 如何型 | 如何+结果 | "如何在30天内..." |
| 秘密型 | 秘密+揭示 | "专家不想让你知道的..." |
| 对比型 | 对比+结果 | "别再...试试这个" |
| 证据型 | 证据+结论 | "10000人验证的..." |

**分支条件**：
- 若 `medium=ad` → 使用短标题（<10字）
- 若 `medium=landing` → 使用长标题（15-25字）
- 若 `medium=email` → 使用疑问型标题
- 若 `medium=social` → 使用数字型或对比型
- 若 `audience=年轻人` → 使用幽默或反叛型
- 若 `audience=专业人士` → 使用数据型或证据型

### Step 3: 正文撰写

- **输入**：`framework_selection` + `headline_options`
- **动作**：
  1. 撰写开场、问题、解决方案
  2. 列出利益点和证据
  3. 设计结尾
- **输出**：`body_copy`
- **正文结构**：

| 部分 | 目的 | 长度建议 |
|------|------|----------|
| 开场 | 吸引注意力 | 1-2句 |
| 问题 | 引发共鸣 | 2-3句 |
| 解决方案 | 提供方案 | 2-3句 |
| 利益点 | 强调价值 | 3-5点 |
| 证据 | 建立信任 | 2-3个 |
| 结尾 | 推动行动 | 1-2句 |

**分支条件**：
- 若 `medium=ad` → 正文精简，重点突出
- 若 `medium=landing` → 正文详细，包含完整论证
- 若 `medium=email` → 正文分段，增加可读性
- 若 `medium=social` → 正文简短，突出核心
- 若 `medium=product` → 正文客观，突出特性

### Step 4: CTA 设计

- **输入**：`goal` + `medium`
- **动作**：
  1. 设计主CTA和备选CTA
  2. 添加紧迫感元素
  3. 确定CTA位置
- **输出**：`cta_design`
- **CTA 设计原则**：

| 原则 | 说明 | 示例 |
|------|------|------|
| 明确 | 行动具体 | "立即购买" 而非 "了解更多" |
| 紧迫 | 时间限制 | "限时优惠，仅剩3天" |
| 价值 | 强调好处 | "免费获得..." |
| 低门槛 | 降低风险 | "无需信用卡" |
| 社会证明 | 从众心理 | "已有10000人加入" |

**分支条件**：
- 若 `goal=awareness` → CTA 为 "了解更多"
- 若 `goal=consideration` → CTA 为 "免费试用"
- 若 `goal=conversion` → CTA 为 "立即购买"
- 若 `goal=retention` → CTA 为 "续费优惠"

### Step 5: 文案变体与优化

- **输入**：所有前序输出
- **动作**：
  1. 生成文案变体
  2. 提供 A/B 测试建议
  3. 列出常见错误
- **输出**：`copy_variations` + `optimization_tips`
- **变体类型**：

| 变体 | 目的 | 示例 |
|------|------|------|
| 情感变体 | 情感共鸣 | 温馨、励志、幽默 |
| 理性变体 | 理性说服 | 数据、证据、逻辑 |
| 紧迫变体 | 制造紧迫 | 限时、限量、倒计时 |
| 社会证明变体 | 从众心理 | 用户评价、专家推荐 |

**分支条件**：
- 若 `medium=ad` → 提供 3-5 个变体
- 若 `medium=landing` → 提供 2-3 个变体
- 若 `medium=email` → 提供标题变体
- 若 `medium=social` → 提供内容变体

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**虚假宣传或夸大效果
2. **不得**使用欺骗性 CTA
3. **必须**确保文案真实可信
4. **必须**遵守广告法规

### 软性约束（建议遵守）
1. 建议进行 A/B 测试
2. 建议收集用户反馈
3. 建议定期更新文案
4. 建议关注竞品文案

### 人工兜底点
- 当涉及敏感行业时，**必须**谨慎措辞
- 当需要法律审核时，**必须**建议专业帮助
- 当文案效果不佳时，**必须**重新分析受众

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `CPY_WARNING_FRAMING` | 框架不适合 | 建议更换框架 | 🟡 |
| `CPY_WARNING_TONE` | 语调不适合受众 | 建议调整语调 | 🟡 |
| `CPY_ERROR_CLAIM` | 虚假宣传风险 | 建议修改措辞 | 🔴 |
| `CPY_WARNING_CTA` | CTA 不明确 | 建议重新设计 | 🟡 |
| `CPY_ERROR_LENGTH` | 文案过长或过短 | 建议调整篇幅 | 🔴 |
| `CPY_WARNING_PROOF` | 缺乏证据支撑 | 建议添加证据 | 🟡 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 文案长度符合媒介要求

### 内容校验
- [ ] 框架选择合适
- [ ] 标题吸引人
- [ ] 正文结构清晰
- [ ] CTA 明确且有说服力
- [ ] 无虚假宣传

### OVP 验证信号
- 文案转化率提升 ≥ 15%
- 点击率 ≥ 5%
- 用户反馈正面 ≥ 80%

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 转化率 < 预期 | 重新分析受众 | P1 |
| 点击率 < 5% | 优化标题 | P1 |
| 用户反馈负面 | 调整语调和内容 | P1 |
| 竞品文案变化 | 更新文案策略 | P2 |
| A/B 测试结果 | 优化文案 | P2 |

---

## 📝 自检清单

- [ ] 产品/服务是否清晰？
- [ ] 目标受众是否明确？
- [ ] 写作框架是否合适？
- [ ] 标题是否吸引人？
- [ ] 正文是否结构清晰？
- [ ] 利益点是否突出？
- [ ] 证据是否充分？
- [ ] CTA 是否明确？
- [ ] 是否有虚假宣传？
- [ ] 是否符合广告法规？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-608-01",
  "name": "电商产品描述",
  "prompt": "为一款智能手表撰写产品描述",
  "input": {
    "product": "智能手表，支持心率监测、运动追踪、消息提醒",
    "audience": "25-40岁都市白领",
    "goal": "conversion",
    "medium": "product",
    "tone": "professional"
  },
  "assertions": [
    "framework_selection.primary = FAB 或 PAS",
    "headline_options 包含多个选项",
    "body_copy.benefits 包含至少3个利益点",
    "cta_design.primary_cta 明确"
  ],
  "expected_behavior": "创作有说服力的产品描述",
  "critic_attack": "文案是否突出了产品优势？是否能驱动购买？"
}
```

### 测试用例 2
```json
{
  "id": "test-608-02",
  "name": "SaaS 落地页文案",
  "prompt": "为项目管理SaaS撰写落地页文案",
  "input": {
    "product": "在线项目管理工具，支持团队协作、任务跟踪、进度可视化",
    "audience": "中小企业团队管理者",
    "goal": "conversion",
    "medium": "landing",
    "tone": "professional"
  },
  "assertions": [
    "framework_selection.primary = AIDA 或 PASTOR",
    "headline_options 包含长标题",
    "body_copy 包含完整论证结构",
    "cta_design.primary_cta = 免费试用"
  ],
  "expected_behavior": "创作完整的落地页文案",
  "critic_attack": "文案是否解决了用户痛点？是否提供了足够证据？"
}
```

### 测试用例 3
```json
{
  "id": "test-608-03",
  "name": "社交媒体广告",
  "prompt": "为一款新饮料创作社交媒体广告文案",
  "input": {
    "product": "天然果汁饮料，0添加，新鲜榨取",
    "audience": "18-30岁健康意识年轻人",
    "goal": "awareness",
    "medium": "social",
    "tone": "casual"
  },
  "assertions": [
    "framework_selection.primary = AIDA",
    "headline_options 包含短标题",
    "body_copy 开场简短有力",
    "copy_variations 包含多个变体"
  ],
  "expected_behavior": "创作吸引眼球的社交媒体文案",
  "critic_attack": "文案是否足够吸引人？是否能在3秒内抓住注意力？"
}
```

### 测试用例 4
```json
{
  "id": "test-608-04",
  "name": "邮件营销文案",
  "prompt": "为电商促销活动撰写邮件营销文案",
  "input": {
    "product": "年终大促，全场5折",
    "audience": "老客户",
    "goal": "retention",
    "medium": "email",
    "tone": "urgent"
  },
  "assertions": [
    "framework_selection.primary = PASTOR 或 Before-After-Bridge",
    "headline_options 包含疑问型",
    "cta_design 包含紧迫元素",
    "body_copy.closing 包含限时提醒"
  ],
  "expected_behavior": "创作驱动复购的邮件文案",
  "critic_attack": "文案是否制造了紧迫感？是否能让客户立即行动？"
}
```

### 测试用例 5
```json
{
  "id": "test-608-05",
  "name": "教育产品广告",
  "prompt": "为在线编程课程创作广告文案",
  "input": {
    "product": "Python编程入门课程，零基础可学",
    "audience": "想转行的职场人",
    "goal": "conversion",
    "medium": "ad",
    "tone": "humorous"
  },
  "assertions": [
    "framework_selection.primary = PAS 或 Before-After-Bridge",
    "headline_options 包含对比型或如何型",
    "body_copy.benefits 包含职业发展利益点",
    "cta_design.primary_cta 明确"
  ],
  "expected_behavior": "创作有吸引力的教育产品广告",
  "critic_attack": "文案是否解决了转行焦虑？是否让学习看起来简单？"
}
```

---

## 🔗 关联文档

- [[创意写作]] — 文案的故事化表达
- [[说服力写作]] — 文案的说服力技巧
- [[创意发散]] — 文案创意的发散思维
- [[数据可视化]] — 文案的数据支撑
- [[内容改编]] — 文案的多形态改编

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：框架选择 + 标题技巧 + CTA设计 + Self-Play |

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
