
description: |
  当用户需要识别信息茧房、回声室效应、群体极化、观点单一化时使用此 Skill。
  触发词包括：'信息茧房'、'回声室'、'群体极化'、'观点单一'、'信息偏食'、
  '算法推荐'、'同温层'、'认知封闭'。当用户讨论社交媒体算法、社群观点趋同、
  意识形态极化时，即使未直接说"群体极化"，也应使用此 Skill。
  不适用于正常的社群学习和知识共享。遇到信息多样性评估需求时优先使用。

---

# uSkill-104: 群体极化防御

## 🎯 目标

> 识别并防御信息茧房、回声室效应、群体极化，帮助用户保持认知开放性和观点多样性。

**核心价值**：在算法推荐和社群同质化的时代，主动打破信息壁垒，保持独立思考。

**适用场景**：
- 社交媒体信息流评估
- 社群观点多样性分析
- 个人信息消费习惯审计
- 投资决策中的从众风险识别
- 意识形态极化预警

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `information_environment` | `object` | ✅ | — | 信息环境描述 |
| `user_profile` | `object` | ❌ | — | 用户信息消费画像 |
| `analysis_depth` | `enum` | ❌ | `standard` | `quick` / `standard` / `deep` |

**information_environment 结构**：
```json
{
  "platforms": ["string"],
  "content_sources": ["string"],
  "social_circle": ["string"],
  "algorithm_feed": true
}
```

**user_profile 结构**：
```json
{
  "political_leaning": "left|center|right|unknown",
  "content_diversity_score": "number — 0-100",
  "echo_chamber_risk": "low|medium|high"
}
```

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话极化风险评估",
  "polarization_id": "GP-YYYY-MMDD-NNN",

  "echo_chamber_analysis": {
    "risk_level": "low|medium|high|critical",
    "risk_factors": [
      {
        "factor": "string",
        "description": "string",
        "severity": "low|medium|high"
      }
    ],
    "information_diversity": {
      "score": "number — 0-100",
      "dimensions": {
        "ideological": "number — 0-100",
        "source_variety": "number — 0-100",
        "topic_range": "number — 0-100",
        "viewpoint_diversity": "number — 0-100"
      }
    }
  },

  "algorithm_bias_detection": {
    "detected": false,
    "bias_types": ["filter_bubble", "reinforcement", "polarization"],
    "evidence": ["string"],
    "impact_assessment": "string"
  },

  "social_influence_analysis": {
    "conformity_pressure": "low|medium|high",
    "groupthink_risk": "low|medium|high",
    "dissent_availability": "low|medium|high",
    "critical_mass_of_diversity": "number — 0-100"
  },

  "defense_strategies": [
    {
      "strategy": "string",
      "description": "string",
      "effectiveness": "high|medium|low",
      "implementation_difficulty": "easy|moderate|hard"
    }
  ],

  "monitoring_plan": {
    "weekly_checks": ["string"],
    "monthly_audits": ["string"],
    "red_flags": ["string"]
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

### Step 1: 信息环境扫描

- **输入**：`information_environment`
- **动作**：
  1. 识别信息来源的多样性
  2. 分析算法推荐的影响
  3. 评估社交圈的同质性
- **输出**：`echo_chamber_analysis`
- **信息茧房风险因素**：

| 风险因素 | 特征 | 检测方法 |
|----------|------|----------|
| **单一平台依赖** | 主要信息来自一个平台 | 平台分布分析 |
| **算法强化** | 只看到相似内容 | 内容相似度分析 |
| **社交同质性** | 朋友圈观点趋同 | 社交网络分析 |
| **信息回避** | 主动回避不同观点 | 内容选择模式 |

- **检查点**：✅ 验证信息环境已扫描

### Step 2: 算法偏见检测

- **输入**：`information_environment`
- **动作**：
  1. 检测过滤气泡（Filter Bubble）
  2. 检测强化效应（Reinforcement）
  3. 检测极化效应（Polarization）
- **输出**：`algorithm_bias_detection`
- **算法偏见类型**：

| 类型 | 机制 | 影响 |
|------|------|------|
| **过滤气泡** | 只显示符合偏好的内容 | 视野狭窄 |
| **强化效应** | 不断强化已有观点 | 观点固化 |
| **极化效应** | 推送极端内容吸引点击 | 观点极端化 |

- **检查点**：✅ 验证算法偏见已检测

### Step 3: 社会影响力分析

- **输入**：`information_environment` + `user_profile`
- **动作**：
  1. 评估从众压力
  2. 检测群体思维风险
  3. 评估异议可用性
- **输出**：`social_influence_analysis`
- **群体思维（Groupthink）信号**：

| 信号 | 特征 | 检测方法 |
|------|------|----------|
| **自我审查** | 压制不同意见 | 发言模式分析 |
| **错觉一致** | 假设所有人都同意 | 观点分布分析 |
| **合理化** | 集体为错误决策辩护 | 事后分析 |
| **对外刻板** | 对外部群体有偏见 | 语言分析 |

- **检查点**：✅ 验证社会影响力已分析

### Step 4: 防御策略生成

- **输入**：所有前序输出
- **动作**：
  1. 生成个性化防御策略
  2. 评估策略有效性
  3. 生成实施计划
- **输出**：`defense_strategies`
- **防御策略库**：

| 策略 | 描述 | 有效性 | 难度 |
|------|------|:------:|:----:|
| **信息多样化** | 主动订阅不同立场的信息源 | 高 | 中 |
| **反向推荐** | 定期查看"不喜欢"的内容 | 中 | 低 |
| **跨圈社交** | 与不同背景的人交流 | 高 | 高 |
| **定期审计** | 每月评估信息消费多样性 | 中 | 低 |
| **批判性消费** | 对每条信息保持质疑 | 高 | 中 |
| **算法透明** | 了解推荐算法的工作原理 | 中 | 低 |

- **检查点**：✅ 验证策略已生成

### Step 5: 监控计划制定

- **输入**：`defense_strategies`
- **动作**：
  1. 制定日常检查清单
  2. 制定月度审计计划
  3. 识别危险信号
- **输出**：`monitoring_plan`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**将正常的社群共识误判为极化
2. **不得**建议完全脱离社群
3. **必须**平衡"开放"与"专注"

### 软性约束（建议遵守）
1. 建议每周检查信息多样性
2. 建议每月审计信息消费习惯
3. 建议保持至少 20% 的"异质信息"

### 人工兜底点
- 当检测到严重信息茧房时，**必须**标记并建议干预
- 当涉及重大决策时，**必须**提醒用户考虑不同观点

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `GP_WARNING_LOW_DIVERSITY` | 信息多样性 < 30 | 标记警告 + 建议增加多样性 | 🟡 |
| `GP_WARNING_HIGH_CONFORMITY` | 从众压力 = high | 标记警告 + 建议寻找异议 | 🟡 |
| `GP_CRITICAL_ECHO_CHAMBER` | 风险等级 = critical | 强烈警告 + 建议立即干预 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 信息环境已扫描
- [ ] 算法偏见已检测
- [ ] 社会影响力已分析
- [ ] 防御策略已生成
- [ ] 监控计划已制定

### OVP 验证信号
- 信息茧房识别率 ≥ 80%
- 防御策略采纳率 ≥ 60%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "社交媒体信息茧房检测",
    "prompt": "我的微博关注列表里都是科技博主，每天看到的都是AI相关的内容",
    "context": "platforms=[微博], content_sources=[科技博主]",
    "assertions": [
      "echo_chamber_analysis.risk_level = medium 或 high",
      "information_diversity.dimensions.topic_range < 50",
      "defense_strategies 包含 信息多样化策略"
    ],
    "expected_behavior": "识别信息茧房风险，提供多样化建议",
    "critic_attack": "是否过度解读了正常的兴趣聚焦？"
  },
  {
    "id": "test-002",
    "name": "社群群体思维检测",
    "prompt": "我们投资群里所有人都看好某个股票，没人提出反对意见",
    "context": "social_circle=[投资群]",
    "assertions": [
      "social_influence_analysis.groupthink_risk = high",
      "social_influence_analysis.dissent_availability = low",
      "monitoring_plan.red_flags 包含 群体思维信号"
    ],
    "expected_behavior": "识别群体思维风险，建议寻找异议",
    "critic_attack": "是否正确区分了真正的共识和群体思维？"
  },
  {
    "id": "test-003",
    "name": "健康信息消费验证",
    "prompt": "我关注了不同立场的媒体，经常阅读不同观点的文章",
    "context": "platforms=[多个], content_sources=[多元化]",
    "assertions": [
      "echo_chamber_analysis.risk_level = low",
      "information_diversity.score >= 70",
      "defense_strategies 主要是维护策略"
    ],
    "expected_behavior": "识别为健康的信息消费模式",
    "critic_attack": "是否正确识别了健康的信息消费？"
  }
]
```

---

## 🔗 关联文档

- [[信息污染检测]] — 信息质量评估
- [[情绪操纵识别]] — 情绪操纵检测
- [[uSkill-agent-认知偏差对抗协议]] — 认知偏差检测
- [[元认知-Schema]] — 元认知觉察
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：信息茧房检测 + 算法偏见分析 + 防御策略 |

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
