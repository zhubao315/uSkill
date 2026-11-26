
description: |
  当用户需要识别 FOMO、恐惧营销、社会证明操纵、情感绑架等情绪操纵技术时使用此 Skill。
  触发词包括：'情绪操纵'、'FOMO'、'恐惧营销'、'社会证明'、'情感绑架'、
  '操纵技术'、'心理操纵'、'情绪控制'。当用户讨论营销策略、社交媒体影响、
  人际关系操控时，即使未直接说"情绪操纵"，也应使用此 Skill。
  不适用于正常的情感表达和沟通。遇到情绪操纵识别需求时优先使用。

---

# uSkill-102: 情绪操纵识别

## 🎯 目标

> 识别并解析各种情绪操纵技术，帮助用户保护自己免受心理操纵，建立健康的信息消费习惯。

**核心价值**：在情感泛滥的信息环境中，保持理性判断，不被情绪操纵。

**适用场景**：
- 营销广告分析
- 社交媒体内容评估
- 人际关系边界识别
- 投资决策中的情绪干扰
- 政治宣传识别

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `content` | `string` | ✅ | — | 待检测的内容 |
| `context` | `object` | ❌ | — | `{platform, author, target_audience}` |
| `manipulation_types` | `array` | ❌ | `all` | 指定检测的操纵类型 |
| `sensitivity` | `enum` | ❌ | `standard` | `low` / `standard` / `high` |

**输入约束**：
- `content` 必须为非空字符串
- `sensitivity = high` 时，阈值降低 30%

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话操纵检测结论",
  "manipulation_id": "EM-YYYY-MMDD-NNN",

  "manipulation_detection": {
    "detected": false,
    "techniques": [
      {
        "type": "fomo|fear|social_proof|authority|reciprocity|scarcity|emotional_blackmail",
        "name": "string",
        "description": "string",
        "evidence": ["string"],
        "intensity": "low|medium|high",
        "target_emotion": "string"
      }
    ],
    "overall_intensity": "low|medium|high",
    "confidence": "number"
  },

  "psychological_analysis": {
    "target_audience": "string",
    "emotional_trigger": "string",
    "cognitive_exploitation": "string",
    "defense_mechanism": "string"
  },

  "counter_strategies": [
    {
      "technique": "string",
      "description": "string",
      "effectiveness": "high|medium|low"
    }
  ],

  "health_assessment": {
    "is_manipulative": false,
    "severity": "none|mild|moderate|severe",
    "recommendation": "string"
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

### Step 1: 操纵技术扫描

- **输入**：`content`
- **动作**：
  1. 扫描 7 大类情绪操纵技术
  2. 提取每种技术的证据
  3. 评估每种技术的强度
- **输出**：`manipulation_detection.techniques`
- **操纵技术清单**：

| 技术 | 特征 | 典型话术 |
|------|------|----------|
| **FOMO** | 制造稀缺感/紧迫感 | "限时优惠"、"仅剩最后..."、"错过等一年" |
| **恐惧诉求** | 制造焦虑/恐慌 | "不转不是中国人"、"后果严重" |
| **社会证明** | 操纵从众心理 | "100万人都在用"、"大家都在买" |
| **权威背书** | 虚假/夸大权威 | "专家推荐"、"明星同款" |
| **互惠原则** | 利用亏欠感 | "免费送你..."、"我帮了你..." |
| **稀缺性** | 制造稀缺假象 | "限量版"、"最后机会" |
| **情感绑架** | 利用同情/愧疚 | "你的转发能救人"、"为了孩子" |

- **检查点**：✅ 验证 7 种技术全部扫描

### Step 2: 心理机制分析

- **输入**：检测到的操纵技术
- **动作**：
  1. 分析目标受众特征
  2. 识别情感触发点
  3. 分析认知利用方式
- **输出**：`psychological_analysis`

### Step 3: 反操纵策略生成

- **输入**：检测到的操纵技术
- **动作**：
  1. 为每种检测到的技术生成反制策略
  2. 评估策略有效性
- **输出**：`counter_strategies`

### Step 4: 健康评估与建议

- **输入**：所有前序输出
- **动作**：
  1. 综合评估操纵严重程度
  2. 生成行动建议
- **输出**：`health_assessment`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**将正常的情感表达误判为操纵
2. **不得**忽略任何检测到的操纵技术
3. **必须**区分"说服"与"操纵"的边界

### 软性约束（建议遵守）
1. 建议对高强度操纵内容保持警惕
2. 建议考虑内容发布的背景和目的

### 人工兜底点
- 当检测到高强度情感绑架时，**必须**标记并建议暂停决策
- 当涉及重大财务决策时，**必须**提醒用户冷静思考

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `EM_WARNING_AMBIGUOUS` | 操纵意图不明确 | 标记为"疑似" + 建议谨慎 | 🟡 |
| `EM_WARNING_HIGH_INTENSITY` | 操动强度高 | 标记警告 + 建议暂停 | 🟡 |
| `EM_ERROR_NO_CONTENT` | 内容为空 | 要求提供内容 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 7 种操纵技术全部扫描
- [ ] 每种技术有证据支撑
- [ ] 反操纵策略已生成

### OVP 验证信号
- 识别准确率 ≥ 90%
- 误报率 < 10%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "FOMO检测-电商促销",
    "prompt": "限时2小时！原价999现在只要99！已有10000人购买！",
    "context": "platform=电商, target_audience=年轻女性",
    "assertions": [
      "manipulation_detection.techniques 包含 fomo",
      "manipulation_detection.techniques 包含 scarcity",
      "overall_intensity = high"
    ],
    "expected_behavior": "识别FOMO和稀缺性操纵",
    "critic_attack": "是否过度解读了正常的促销信息？"
  },
  {
    "id": "test-002",
    "name": "恐惧诉求检测-健康营销",
    "prompt": "不喝这个，你的身体会积累毒素，后果不堪设想！",
    "context": "platform=社交媒体, target_audience=中年人",
    "assertions": [
      "manipulation_detection.techniques 包含 fear",
      "target_emotion = 恐惧",
      "health_assessment.is_manipulative = true"
    ],
    "expected_behavior": "识别恐惧营销",
    "critic_attack": "是否将正常的健康警告误判为恐惧营销？"
  },
  {
    "id": "test-003",
    "name": "正常表达验证",
    "prompt": "这款产品确实不错，我用了一个月感觉很好，推荐给大家。",
    "context": "platform=社交媒体, target_audience=普通用户",
    "assertions": [
      "manipulation_detection.detected = false",
      "health_assessment.is_manipulative = false",
      "health_assessment.severity = none"
    ],
    "expected_behavior": "识别为正常的产品推荐，非操纵",
    "critic_attack": "是否正确区分了正常推荐和操纵？"
  }
]
```

---

## 🔗 关联文档

- [[信息污染检测]] — 信息质量评估
- [[uSkill-agent-认知偏差对抗协议]] — 认知偏差检测
- [[元认知-Schema]] — 元认知觉察
- [[决策推理-Schema]] — 决策推理框架
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：7 类操纵技术检测 + 心理分析 + 反制策略 |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

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
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

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


**相关概念**：[[情绪坐标]]

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
