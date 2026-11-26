
⚙️ AI-Co 运行配置块
触发场景: 用户说'逻辑谬误'、'论证分析'、'推理错误'、'稻草人'、'滑坡谬误'
复用率预估: 高
一键调用: |
  论证解析→20种谬误扫描→质量评估→论证重构
输入Schema: argument: string(≥30字), argument_type: deductive|inductive|abductive|unknown, depth: quick|standard|deep, context: {domain, purpose, audience}
输出Schema: argument_analysis, fallacy_detection{total_detected, fallacies[]}, logical_quality{score, grade}, reconstruction{original, corrected}
AI可执行度: 100%

description: |
  当用户需要检测论证中的逻辑谬误、分析论证结构、评估推理有效性时使用此 Skill。
  触发词包括：'逻辑谬误'、'论证分析'、'推理错误'、'逻辑错误'、'谬误检测'、
  '稻草人'、'滑坡谬误'、'诉诸权威'。当用户讨论辩论、学术论文、政策分析、
  投资逻辑时，即使未直接说"逻辑谬误"，也应使用此 Skill。
  不适用于数值计算错误或事实错误（使用信息污染检测）。遇到逻辑分析需求时优先使用。

---

# uSkill-103: 逻辑谬误检测

## 🎯 目标

> 系统化检测 20+ 种常见逻辑谬误，帮助用户识别论证中的推理漏洞，提升批判性思维能力。

**核心价值**：在复杂论证中快速定位逻辑漏洞，避免被似是而非的推理误导。

**适用场景**：
- 学术论文评审
- 政策辩论分析
- 投资逻辑验证
- 法律论证评估
- 日常争论分析

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `argument` | `string` | ✅ | — | 待检测的论证内容 |
| `argument_type` | `enum` | ❌ | `unknown` | `deductive` / `inductive` / `abductive` / `unknown` |
| `depth` | `enum` | ❌ | `standard` | `quick` / `standard` / `deep` |
| `context` | `object` | ❌ | — | `{domain, purpose, audience}` |

**输入约束**：
- `argument` 必须为非空字符串（最少 30 字）
- `depth = deep` 时执行完整 20+ 谬误类型检测

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话逻辑评估结论",
  "fallacy_id": "LF-YYYY-MMDD-NNN",

  "argument_analysis": {
    "structure_valid": true,
    "premises_count": "number",
    "conclusion_identified": "string",
    "argument_type": "deductive|inductive|abductive"
  },

  "fallacy_detection": {
    "total_detected": 0,
    "fallacies": [
      {
        "type": "string",
        "name": "string",
        "description": "string",
        "location": "string — 谬误在原文中的位置",
        "evidence": "string",
        "severity": "low|medium|high",
        "counter_argument": "string"
      }
    ]
  },

  "logical_quality": {
    "score": "number — 0-100",
    "grade": "A|B|C|D|F",
    "strengths": ["string"],
    "weaknesses": ["string"],
    "recommendation": "string"
  },

  "reconstruction": {
    "original": "string",
    "corrected": "string",
    "improvement_notes": "string"
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

### Step 1: 论证结构解析

- **输入**：`argument`
- **动作**：
  1. 识别前提（Premises）
  2. 识别结论（Conclusion）
  3. 判断论证类型
- **输出**：`argument_analysis`
- **论证类型判断标准**：

| 类型 | 特征 | 示例 |
|------|------|------|
| **演绎** | 从一般到特殊，必然性推理 | "所有人都会死→苏格拉底是人→苏格拉底会死" |
| **归纳** | 从特殊到一般，或然性推理 | "观察到100只天鹅是白的→所有天鹅是白的" |
| **溯因** | 从结果推原因，最佳解释推理 | "地上湿了→可能下过雨" |

- **检查点**：✅ 验证前提和结论已识别

### Step 2: 20 种逻辑谬误检测

- **输入**：`argument_analysis`
- **动作**：系统性检测 20 种常见谬误

**谬误分类与检测**：

#### A. 相关性谬误（Relevance Fallacies）

| 谬误 | 特征 | 检测方法 |
|------|------|----------|
| **稻草人** | 歪曲对方观点后攻击 | 对比原文与引用 |
| **人身攻击** | 攻击人而非论点 | 检查是否针对个人 |
| **诉诸权威** | 仅因权威就接受 | 验证权威相关性 |
| **诉诸情感** | 用情感代替逻辑 | 检测情绪化语言 |
| **诉诸传统** | 因为一直如此 | 检查历史依据 |
| **诉诸多数** | 因为大家都这样 | 检查统计依据 |

#### B. 证据不足谬误（Defective Evidence Fallacies）

| 谬误 | 特征 | 检测方法 |
|------|------|----------|
| **草率概括** | 样本太小下结论 | 检查样本量 |
| **虚假类比** | 类比不当 | 检查相似性 |
| **滑坡谬误** | 无根据的连锁推导 | 检查因果链 |
| **假因假果** | 相关≠因果 | 检查因果关系 |
| **合成谬误** | 部分→整体 | 检查推理方向 |
| **分解谬误** | 整体→部分 | 检查推理方向 |

#### C. 逻辑结构谬误（Logical Structure Fallacies）

| 谬误 | 特征 | 检测方法 |
|------|------|----------|
| **循环论证** | 用结论证明前提 | 检查论证结构 |
| **虚假二分** | 非黑即白 | 检查是否有第三选项 |
| **乞题** | 预设结论 | 检查前提假设 |
| **否定前件** | 错误的逆命题推理 | 检查逻辑形式 |
| **肯定后件** | 错误的逆命题推理 | 检查逻辑形式 |
| **歧义谬误** | 歧义词义 | 检查关键术语 |

- **输出**：`fallacy_detection`
- **检查点**：✅ 验证 20 种谬误全部扫描

### Step 3: 逻辑质量评估

- **输入**：`fallacy_detection`
- **动作**：
  1. 计算逻辑质量得分
  2. 识别优势和弱点
  3. 生成改进建议
- **输出**：`logical_quality`
- **评分标准**：

| 等级 | 分数 | 标准 |
|:----:|:----:|------|
| A | 90-100 | 无谬误，论证严密 |
| B | 75-89 | 轻微瑕疵，基本有效 |
| C | 60-74 | 1-2 个中等谬误 |
| D | 40-59 | 多个谬误，论证薄弱 |
| F | 0-39 | 严重谬误，论证无效 |

### Step 4: 论证重构

- **输入**：`argument` + `fallacy_detection`
- **动作**：
  1. 保留有效部分
  2. 修正谬误部分
  3. 生成改进版本
- **输出**：`reconstruction`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**将正常的修辞手法误判为谬误
2. **不得**忽略任何检测到的谬误
3. **必须**区分"谬误"与"弱点"

### 软性约束（建议遵守）
1. 建议对模糊情况标注"疑似"
2. 建议提供改进版本而非仅批评

### 人工兜底点
- 当论证涉及重大决策时，**必须**提醒用户谨慎
- 当检测到多个高严重度谬误时，**必须**标记警告

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `LF_WARNING_AMBIGUOUS` | 谬误意图不明确 | 标记为"疑似" + 建议谨慎 | 🟡 |
| `LF_WARNING_MULTIPLE` | 检测到多个谬误 | 列出所有谬误 + 优先级排序 | 🟡 |
| `LF_ERROR_TOO_SHORT` | 内容过短 | 要求提供完整论证 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 论证结构已解析
- [ ] 20 种谬误全部扫描
- [ ] 每个谬误有证据支撑
- [ ] 论证重构已完成

### OVP 验证信号
- 谬误检测覆盖率 ≥ 95%
- 识别准确率 ≥ 85%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "稻草人论证检测",
    "prompt": "你说应该提高税收？你就是想让所有人都变成穷人！",
    "context": "domain=政治辩论",
    "assertions": [
      "fallacy_detection.fallacies 包含 稻草人",
      "severity = high",
      "reconstruction.corrected 已生成"
    ],
    "expected_behavior": "识别稻草人论证，提供修正版本",
    "critic_attack": "是否正确识别了歪曲？是否有遗漏？"
  },
  {
    "id": "test-002",
    "name": "滑坡谬误检测",
    "prompt": "如果我们允许A，接下来就会B，然后C，最后D，后果不堪设想！",
    "context": "domain=政策分析",
    "assertions": [
      "fallacy_detection.fallacies 包含 滑坡谬误",
      "每个推导步骤都有分析",
      "counter_argument 已提供"
    ],
    "expected_behavior": "识别滑坡谬误，分析每个推导步骤",
    "critic_attack": "是否正确识别了因果链的薄弱环节？"
  },
  {
    "id": "test-003",
    "name": "有效论证验证",
    "prompt": "所有哺乳动物都是温血动物。鲸鱼是哺乳动物。因此，鲸鱼是温血动物。",
    "context": "domain=生物学",
    "assertions": [
      "argument_analysis.structure_valid = true",
      "fallacy_detection.total_detected = 0",
      "logical_quality.grade = A"
    ],
    "expected_behavior": "识别为有效演绎论证",
    "critic_attack": "是否正确识别了有效论证？"
  }
]
```

---

## 🔗 关联文档

- [[决策推理-Schema]] — 决策推理框架
- [[uSkill-agent-认知偏差对抗协议]] — 认知偏差检测
- [[信息污染检测]] — 信息质量评估
- [[元认知-Schema]] — 元认知觉察
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：20 种谬误检测 + 论证重构 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


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
