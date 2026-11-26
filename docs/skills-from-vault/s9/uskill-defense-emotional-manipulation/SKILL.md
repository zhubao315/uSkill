---
name: uskill-defense-emotional-manipulation
description: "让情绪操纵识别变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-defense-emotional-manipulation.md"
  original_id: "SKL-6902"
  version: "3.0.0"
  trust: untrusted
---

# 情绪操纵识别

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
    "prompt": "不喝这个，你的身体会积累毒素，后果不

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
