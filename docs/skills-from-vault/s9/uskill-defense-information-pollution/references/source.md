
description: |
  当用户需要检测信息真实性、识别假新闻、评估信息源可信度、识别误导信息时使用此 Skill。
  触发词包括：'信息污染'、'假新闻'、'事实核查'、'信息验证'、'可信度'、
  '误导信息'、'信息操纵'、'谣言识别'、'信息质量'。当用户分享新闻、文章、
  社交媒体内容并询问其真实性时，即使未直接说"信息污染"，也应使用此 Skill。
  不适用于专业领域技术文档（使用对应领域 Skill）。遇到信息验证需求时优先使用。

---

# uSkill-101: 信息污染检测

## 🎯 目标

> 建立系统化的信息质量评估框架，帮助用户识别假新闻、误导信息、认知攻击，保护认知安全。

**核心价值**：在信息过载时代，快速准确地评估信息质量，避免被虚假或误导信息影响决策。

**适用场景**：
- 新闻文章真实性验证
- 社交媒体内容评估
- 学术论文可信度判断
- 商业宣传信息甄别
- 投资研报质量评估

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `content` | `string` | ✅ | — | 待检测的信息内容 |
| `source` | `string` | ❌ | `unknown` | 信息来源（媒体/个人/机构） |
| `content_type` | `enum` | ❌ | `article` | `news` / `article` / `social` / `academic` / `commercial` |
| `context` | `object` | ❌ | — | `{publish_time, author, platform, shares}` |
| `depth` | `enum` | ❌ | `standard` | `quick` / `standard` / `deep` |

**输入约束**：
- `content` 必须为非空字符串（最少 50 字）
- `content_type` 决定检测侧重点
- `depth = deep` 时执行完整 12 维度检测

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话信息质量结论",
  "pollution_id": "IP-YYYY-MMDD-NNN",

  "source_analysis": {
    "credibility_score": "number — 0-100",
    "source_type": "official|media|individual|unknown",
    "bias_direction": "left|center|right|unknown",
    "track_record": "string — 历史可信度记录"
  },

  "content_analysis": {
    "factual_claims": [
      {
        "claim": "string",
        "verifiable": true,
        "evidence_available": true,
        "supporting_evidence": ["string"],
        "contradicting_evidence": ["string"],
        "confidence": "number"
      }
    ],
    "logical_structure": {
      "argument_valid": true,
      "fallacies_detected": ["string"],
      "evidence_quality": "strong|moderate|weak|absent"
    },
    "emotional_manipulation": {
      "detected": false,
      "techniques": ["string"],
      "intensity": "low|medium|high"
    }
  },

  "pollution_detection": {
    "is_polluted": false,
    "pollution_type": "misinformation|disinformation|propaganda|clickbait|satire|none",
    "confidence": "number",
    "severity": "low|medium|high|critical",
    "evidence": ["string"]
  },

  "credibility_assessment": {
    "overall_score": "number — 0-100",
    "grade": "A|B|C|D|F",
    "key_risks": ["string"],
    "recommendation": "trust|verify|distrust|reject"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

### 异常输出

```json
{
  "status": "partial",
  "error_code": "IP_WARNING_SHORT_CONTENT",
  "error_message": "内容过短，无法进行深度分析",
  "suggestion": "请提供更完整的内容（至少 50 字）",
  "partial_result": {
    "source_analysis": "已完成",
    "content_analysis": "部分完成"
  }
}
```

---

## 📋 执行步骤

### Step 1: 信息源可信度评估

- **输入**：`source` + `context`
- **动作**：
  1. 识别信息源类型（官方/媒体/个人/未知）
  2. 查询信息源历史可信度记录
  3. 评估信息源的立场和偏见
- **输出**：`source_analysis`
- **可信度评分标准**：

| 来源类型 | 基础分 | 加分项 | 减分项 |
|----------|:------:|--------|--------|
| 官方机构 | 80 | 权威认证 +10 | 曾有造假 -30 |
| 主流媒体 | 70 | 多方引用 +5 | 立场鲜明 -10 |
| 个人博主 | 40 | 专业背景 +20 | 营销账号 -20 |
| 未知来源 | 20 | 可验证 +30 | 匿名 -10 |

- **分支条件**：
  - IF `source = unknown` AND 内容涉及重大事件 → 标记 `WARNING_UNVERIFIED_SOURCE`
  - IF 历史记录显示曾有造假 → 标记 `WARNING_SOURCE_CREDIBILITY`
- **检查点**：✅ 验证信息源已识别

### Step 2: 事实性声明提取

- **输入**：`content`
- **动作**：
  1. 提取所有可验证的事实性声明
  2. 区分事实与观点
  3. 评估每个声明的可验证性
- **输出**：`factual_claims`
- **事实性声明特征**：
  - 包含具体数据、日期、人名、地点
  - 可通过公开信息验证
  - 使用确定性语言（"是"、"有"、"发生了"）
- **观点性声明特征**：
  - 使用主观语言（"应该"、"可能"、"我认为"）
  - 无法直接验证
  - 价值判断
- **检查点**：✅ 验证至少提取 3 个事实性声明

### Step 3: 逻辑结构分析

- **输入**：`content` + `factual_claims`
- **动作**：
  1. 分析论证结构
  2. 检测逻辑谬误
  3. 评估证据质量
- **输出**：`logical_structure`
- **常见逻辑谬误清单**：

| 谬误类型 | 特征 | 检测方法 |
|----------|------|----------|
| 稻草人论证 | 歪曲对方观点 | 对比原文与引用 |
| 滑坡谬误 | 无根据的连锁推导 | 检查因果链 |
| 诉诸权威 | 仅因权威就接受 | 验证权威相关性 |
| 虚假二分 | 非黑即白 | 检查是否有第三选项 |
| 循环论证 | 用结论证明前提 | 检查论证结构 |
| 诉诸情感 | 用情感代替逻辑 | 检测情绪化语言 |

- **检查点**：✅ 验证逻辑分析完成

### Step 4: 情绪操纵检测

- **输入**：`content`
- **动作**：
  1. 检测情绪化语言
  2. 识别操纵技术
  3. 评估操纵强度
- **输出**：`emotional_manipulation`
- **情绪操纵技术清单**：

| 技术 | 特征 | 示例 |
|------|------|------|
| **恐惧诉求** | 制造焦虑/恐慌 | "不转不是中国人" |
| **FOMO** | 制造稀缺感 | "限时优惠，仅剩最后..." |
| **社会证明** | 操纵从众心理 | "100万人都在用" |
| **权威背书** | 虚假权威 | "专家推荐"（无具体专家） |
| **情感绑架** | 利用同情/愧疚 | "你的转发能救人" |

- **分支条件**：
  - IF 情绪操纵强度 = high → 标记 `WARNING_EMOTIONAL_MANIPULATION`
  - IF 检测到 FOMO + 恐惧诉求组合 → 标记 `WARNING_MARKETING_MANIPULATION`
- **检查点**：✅ 验证情绪操纵检测完成

### Step 5: 信息污染类型判定

- **输入**：所有前序分析结果
- **动作**：
  1. 综合评估信息污染程度
  2. 判定污染类型
  3. 计算置信度
- **输出**：`pollution_detection`
- **污染类型定义**：

| 类型 | 定义 | 严重度 |
|------|------|:------:|
| **Misinformation** | 非故意的错误信息 | 🟡 |
| **Disinformation** | 故意制造的虚假信息 | 🔴 |
| **Propaganda** | 政治/意识形态宣传 | 🟡 |
| **Clickbait** | 标题党，内容不符 | 🟢 |
| **Satire** | 讽刺/恶搞（被误认为真实） | 🟢 |

- **分支条件**：
  - IF 事实性声明 ≥50% 不可验证 → `disinformation`
  - IF 情绪操纵 + 事实不足 → `propaganda`
  - IF 标题与内容严重不符 → `clickbait`
- **检查点**：✅ 验证污染类型已判定

### Step 6: 综合评估与建议

- **输入**：所有前序输出
- **动作**：
  1. 计算综合可信度评分
  2. 给出信任等级
  3. 提供行动建议
- **输出**：`credibility_assessment`
- **信任等级标准**：

| 等级 | 分数范围 | 建议 |
|:----:|:--------:|------|
| A | 80-100 | 可信，可直接引用 |
| B | 60-79 | 基本可信，建议交叉验证 |
| C | 40-59 | 存疑，需多方验证 |
| D | 20-39 | 不可信，建议忽略 |
| F | 0-19 | 确认虚假，建议举报 |

- **检查点**：✅ 验证评估报告完整

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**将未经验证的信息标记为"真实"（最多标记为"基本可信"）
2. **不得**基于单一来源做出最终判断
3. **不得**忽略任何一方的证据（平衡报道原则）
4. **必须**明确区分"事实"与"观点"

### 软性约束（建议遵守）
1. 建议对重大事件进行多方交叉验证
2. 建议关注信息发布的时机和背景
3. 建议考虑信息源的利益相关性

### 人工兜底点
- 当涉及重大公共事件时，**必须**提醒用户参考官方信息
- 当检测到 `disinformation` 时，**必须**标记并建议举报
- 当信息源为个人时，**必须**提醒用户注意主观性

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `IP_WARNING_SHORT_CONTENT` | 内容 < 50 字 | 降级为快速检测 | 🟡 |
| `IP_WARNING_UNVERIFIED_SOURCE` | 未知来源 + 重大事件 | 标记警告 + 建议官方验证 | 🟡 |
| `IP_WARNING_SOURCE_CREDIBILITY` | 信息源有造假记录 | 降低可信度评分 | 🟡 |
| `IP_WARNING_EMOTIONAL_MANIPULATION` | 情绪操纵强度高 | 标记警告 + 建议冷静 | 🟡 |
| `IP_ERROR_NO_FACTS` | 无法提取事实性声明 | 降级为观点分析 | 🔴 |
| `IP_ERROR_CONTRADICTORY` | 信息内部矛盾 | 标记矛盾 + 建议核实 | 🔴 |

### 降级策略
- 当 `depth = quick` 时，仅执行 Step 1 + Step 5
- 当内容过短时，降级为来源可信度评估
- 当无法验证时，输出"待验证"而非"真实/虚假"

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 字段类型与 Schema 一致
- [ ] 污染检测编号格式正确（IP-YYYY-MMDD-NNN）

### 内容校验
- [ ] 信息源已识别并评分
- [ ] 至少提取 3 个事实性声明
- [ ] 逻辑谬误检测完成
- [ ] 情绪操纵检测完成
- [ ] 污染类型已判定
- [ ] 综合评估报告完整

### 合规校验
- [ ] 未将未经验证的信息标记为"真实"
- [ ] 事实与观点已明确区分
- [ ] 人工兜底点已正确触发

### OVP 验证信号
- 假新闻识别准确率 ≥ 85%
- 误导信息检测率 ≥ 80%
- 用户满意度 ≥ 4.0/5.0

---

## 🔄 迭代触发条件

### Self-Play 触发
- **频率**：weekly
- **触发条件**：
  - 每周自动触发（抽样 20% 检测记录）
  - 新型信息污染手法出现时触发

### 版本升级触发
- minor 版本：新增检测维度或操纵技术
- major 版本：改变评估框架或判定标准

### 废弃触发
- 当检测准确率连续 30 天 < 70% 时，标记需要重构

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags/ovp/self_play）
- [ ] 输入输出 Schema 明确
- [ ] 执行步骤每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 2 个现有 Skill 有双向链接

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "假新闻检测-典型特征",
    "prompt": "转发：某明星昨晚因车祸去世，速转！",
    "context": "source=unknown, content_type=social",
    "assertions": [
      "输出包含 source_analysis",
      "source_type = unknown",
      "pollution_detection.is_polluted = true",
      "credibility_assessment.grade = F"
    ],
    "expected_behavior": "识别为典型假新闻，标记高风险",
    "critic_attack": "是否过于武断？是否有误判可能？"
  },
  {
    "id": "test-002",
    "name": "标题党检测",
    "prompt": "震惊！99%的人都不知道的健康秘密，看完后我哭了...",
    "context": "source=media, content_type=article",
    "assertions": [
      "emotional_manipulation.detected = true",
      "emotional_manipulation.techniques 包含 FOMO",
      "pollution_detection.pollution_type = clickbait"
    ],
    "expected_behavior": "识别标题党特征，标记为 clickbait",
    "critic_attack": "是否将正常的吸引注意力误判为标题党？"
  },
  {
    "id": "test-003",
    "name": "专业报道验证",
    "prompt": "据新华社报道，2026年GDP增长5.2%...",
    "context": "source=Xinhua, content_type=news",
    "assertions": [
      "source_analysis.credibility_score >= 80",
      "source_type = official",
      "credibility_assessment.grade = A 或 B"
    ],
    "expected_behavior": "识别权威来源，给予较高可信度",
    "critic_attack": "是否过度信任权威来源？是否忽略了其他可能？"
  },
  {
    "id": "test-004",
    "name": "情绪操纵检测",
    "prompt": "如果你不转发这条消息，你的家人就会...",
    "context": "source=unknown, content_type=social",
    "assertions": [
      "emotional_manipulation.detected = true",
      "emotional_manipulation.techniques 包含 恐惧诉求",
      "emotional_manipulation.intensity = high"
    ],
    "expected_behavior": "识别情绪操纵，标记高风险",
    "critic_attack": "是否将正常的警告误判为情绪操纵？"
  },
  {
    "id": "test-005",
    "name": "平衡报道验证",
    "prompt": "某公司财报显示营收增长20%，但利润率下降5个百分点",
    "context": "source=financial_media, content_type=article",
    "assertions": [
      "content_analysis.factual_claims 包含 正面和负面事实",
      "未偏向任何一方",
      "credibility_assessment.grade = B 或更高"
    ],
    "expected_behavior": "识别平衡报道，给予公正评价",
    "critic_attack": "是否正确识别了平衡报道？是否有遗漏？"
  }
]
```

---

## 🔗 关联文档

- [[uSkill-agent-认知偏差对抗协议]] — 认知偏差检测框架
- [[元认知-Schema]] — 元认知觉察能力
- [[决策推理-Schema]] — 决策推理框架
- [[情绪操纵识别]] — 情绪操纵检测
- [[逻辑谬误检测]] — 逻辑谬误检测
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：6 步检测流程 + 12 维度分析 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板 · 关联：[[人生操作系统进化-Schema-v2]]*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [商业任务] for [业务阶段], with [资源约束], leaning toward [策略框架/执行路径]."

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
| ""先做再说"" | "方向错了，执行力越强死得越快" |
| ""用户说想要这个"" | "用户说的是解决方案，不是需求本身" |
| ""竞品都在做"" | "竞品犯错不意味着你也应该犯" |
| ""这个市场很大"" | "大市场≠你能切到的市场" |

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
