
description: |
  当用户需要启动元认知觉察、暂停自动化反应、部署认知防火墙、进行思维监控时使用此 Skill。
  触发词包括：'元认知'、'觉察'、'暂停'、'自动驾驶'、'思维监控'、'认知防火墙'、
  '自我观察'、'第三视角'、'冥想'、'反思'。当用户讨论情绪管理、习惯打断、
  决策质量提升、思维模式识别时，即使未直接说"元认知"，也应使用此 Skill。
  不适用于具体任务执行（使用对应领域 Skill）。遇到需要"停下来想一想"的场景时优先使用。

---

# uSkill-007: 元认知

## 🎯 目标

> 建立「觉察→暂停→审视→选择」的元认知操作框架，将人从自动驾驶模式切换到主动控制模式，让每一次关键选择都经过理智脑的审视。

**核心价值**：元认知是所有认知能力的"操作系统"——它不直接解决问题，但它让你有能力选择用什么方式解决问题。

**适用场景**：
- 情绪波动时（愤怒、焦虑、恐惧）的自我调节
- 习惯性反应时（刷手机、拖延、冲动消费）的打断
- 重大决策时的思维质量提升
- 日常反思与复盘的深度增强
- 冥想与专注力训练

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `trigger_type` | `enum` | ✅ | — | `emotion` / `habit` / `decision` / `reflection` / `meditation` |
| `stimulus` | `string` | ✅ | — | 触发元认知的刺激/情境描述 |
| `intensity` | `number` | ❌ | `3` | 情绪/习惯强度 1-5（5=极强） |
| `context` | `object` | ❌ | — | `{time_of_day, energy_level, recent_events}` |
| `firewall_mode` | `boolean` | ❌ | `false` | 是否启用认知防火墙模式 |

**输入约束**：
- `stimulus` 必须为非空字符串
- `intensity` 范围 1-5
- `trigger_type = emotion` 时建议提供 `intensity`

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话觉察结论",
  "metacognition_id": "MC-YYYY-MMDD-NNN",

  "trigger_analysis": {
    "type": "emotion|habit|decision|reflection|meditation",
    "stimulus": "string",
    "intensity": "number",
    "autopilot_detected": true,
    "trigger_pattern": "string — 识别到的触发模式"
  },

  "pause_window": {
    "duration_seconds": 3,
    "technique": "string — 使用的暂停技术",
    "space_created": true,
    "first_reaction": "string — 第一反应描述",
    "observed_emotion": "string — 觉察到的情绪",
    "observed_thought": "string — 觉察到的想法"
  },

  "third_person_perspective": {
    "future_self_view": "string — 1年后/5年后/80岁自己的视角",
    "observer_view": "string — 第三视角旁观者的视角",
    "values_alignment": "string — 与核心价值观的对齐度",
    "key_insight": "string — 核心洞察"
  },

  "choice_point": {
    "options": [
      {
        "option": "string",
        "consequence_short": "string",
        "consequence_long": "string",
        "aligned_with_values": true,
        "selected": false
      }
    ],
    "selected_option": "string",
    "selection_reason": "string",
    "confidence": "number"
  },

  "firewall_result": {
    "activated": false,
    "assertion_detected": "string",
    "counter_examples": ["string"],
    "weight_adjustment": "string",
    "cognitive_freedom": "number"
  },

  "post_choice_reflection": {
    "choice_quality": "string",
    "autopilot_switches": "int — 从自动驾驶切换到主动控制的次数",
    "metacognition_strength": "number — 元认知强度评估 1-10",
    "improvement_area": "string"
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
  "error_code": "MC_WARNING_HIGH_INTENSITY",
  "error_message": "情绪强度过高（5/5），元认知介入困难",
  "suggestion": "先执行生理调节（深呼吸10次），再尝试元认知觉察",
  "partial_result": {
    "trigger_analysis": "已完成",
    "pause_window": "失败 — 情绪压过理智脑"
  }
}
```

---

## 📋 执行步骤

### Step 1: 触发识别与信号检测

- **输入**：`trigger_type` + `stimulus`
- **动作**：
  1. 识别触发类型（情绪/习惯/决策/反思/冥想）
  2. 检测自动驾驶信号
  3. 评估触发强度
- **输出**：`trigger_analysis`
- **自动驾驶信号清单**：
  - 情绪类：心跳加速、肌肉紧张、呼吸变浅、思维变窄
  - 习惯类：无意识动作（刷手机、咬指甲）、时间黑洞
  - 决策类：第一反应极快、不愿考虑替代方案、"就是觉得应该这样"
- **分支条件**：
  - IF `intensity` = 5 → 标记 `WARNING_EXTREME_INTENSITY` + 建议先做生理调节
  - IF 触发模式与历史记录匹配 → 标记 `PATTERN_DETECTED`
- **检查点**：✅ 验证触发类型已识别

### Step 2: 元认知暂停（3 秒窗口）

- **输入**：`trigger_analysis`
- **动作**：
  1. 创建暂停窗口（至少 3 秒）
  2. 执行觉察三步法：觉察→命名→选择
  3. 记录第一反应和觉察到的情绪/想法
- **输出**：`pause_window`
- **暂停技术库**：

| 技术 | 适用场景 | 操作 |
|------|----------|------|
| **3 秒呼吸法** | 通用 | 吸气 3 秒 → 屏息 3 秒 → 呼气 3 秒 |
| **5-4-3-2-1 感官锚定** | 焦虑/恐慌 | 说出 5 个看到的 + 4 个触摸到的 + 3 个听到的 + 2 个闻到的 + 1 个尝到的 |
| **命名情绪法** | 情绪波动 | 用精确词汇命名："我在焦虑"、"我在愤怒"、"我在恐惧" |
| **身体扫描法** | 习惯打断 | 从头到脚扫描身体感受，中断自动化回路 |
| **提问锚定法** | 决策场景 | 问自己："这是我真正想要的吗？" |

- **分支条件**：
  - IF `intensity` ≥ 4 → 使用 5-4-3-2-1 感官锚定（更强力的中断）
  - IF `trigger_type` = habit → 使用身体扫描法
  - IF `trigger_type` = decision → 使用提问锚定法
- **检查点**：✅ 验证暂停窗口已创建（space_created = true）

### Step 3: 第三视角审视

- **输入**：`pause_window`
- **动作**：
  1. 切换到第三视角（"如果 1 年后的我看这个选择"）
  2. 切换到观察者视角（"如果我是旁观者"）
  3. 评估与核心价值观的对齐度
  4. 提取核心洞察
- **输出**：`third_person_perspective`
- **视角切换技术**：

| 视角 | 问题 | 适用场景 |
|------|------|----------|
| **未来自我** | "1 年后的我会怎么看这个选择？" | 冲动决策 |
| **80 岁自我** | "80 岁的我会后悔吗？" | 重大人生决策 |
| **旁观者** | "如果我是旁观者，我会怎么建议？" | 陷入困境 |
| **价值观** | "这个选择符合我的核心价值观吗？" | 道德困境 |
| **系统视角** | "这个选择在更大的系统中意味着什么？" | 复杂决策 |

- **检查点**：✅ 验证至少完成 2 个视角切换

### Step 4: 选择点分析

- **输入**：`third_person_perspective`
- **动作**：
  1. 列出所有可行选项（至少 3 个）
  2. 评估每个选项的短期/长期后果
  3. 评估与价值观的对齐度
  4. 做出有意识的选择
- **输出**：`choice_point`
- **分支条件**：
  - IF 选项少于 3 个 → 要求补充替代方案
  - IF 所有选项都不对齐价值观 → 标记 `VALUE_CONFLICT` + 建议暂停
- **检查点**：✅ 验证至少 3 个选项，且有意识选择（非自动驾驶）

### Step 5: 认知防火墙（可选）

- **输入**：`firewall_mode` + `choice_point`
- **动作**（仅当 `firewall_mode = true` 时执行）：
  1. 检测断言中的绝对化用词
  2. 执行 3-反例协议
  3. 计算认知自由度
  4. 调整信息权重
- **输出**：`firewall_result`
- **防火墙触发条件**：
  - 对方使用"绝对"、"必然"、"所有人都"等全称量词
  - 自身产生强烈情绪认同或反感
  - 群体出现 FOMO 式一致预期
- **3-反例协议**：
  1. 将断言写下来
  2. 强制列出 3 个不依赖该断言也能成立的反例
  3. 评估原断言的信息权重是否应下调 50%
- **认知自由度公式**：`认知自由度 = 断言输入 × 反例数 / 情绪唤醒度`
- **检查点**：✅ 验证反例数量 ≥ 3

### Step 6: 事后反思与模式记录

- **输入**：所有前序输出
- **动作**：
  1. 评估本次选择质量
  2. 统计自动驾驶切换次数
  3. 评估元认知强度
  4. 识别改进方向
  5. 写入反思日志
- **输出**：`post_choice_reflection`
- **元认知强度评估维度**：

| 维度 | 1 分 | 5 分 | 10 分 |
|------|------|------|-------|
| 觉察速度 | 事后才觉察 | 几秒内觉察 | 即时觉察 |
| 暂停深度 | 未能暂停 | 短暂暂停 | 深度暂停 |
| 视角切换 | 未能切换 | 切换 1 个视角 | 切换 3+ 视角 |
| 选择质量 | 仍是自动驾驶 | 有意识但犹豫 | 清晰有意识选择 |
| 模式识别 | 未识别 | 识别 1 个模式 | 识别多个模式 |

- **检查点**：✅ 验证反思日志已写入

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. 觉察**不等于**自我批判（"我在拖延"是觉察，"我怎么又拖延了"是批判）
2. 不追求"时刻觉察"（元认知消耗认知资源，低风险事务可让自动驾驶处理）
3. 情绪强度 = 5 时**必须**先做生理调节，再尝试元认知
4. 防火墙**不得**成为拒绝一切行动的借口

### 软性约束（建议遵守）
1. 建议每天 5 分钟冥想训练元认知肌肉
2. 建议选择 1 个高频场景作为"觉察锚点"
3. 建议每周回顾元认知强度趋势

### 人工兜底点
- 当触发 `VALUE_CONFLICT` 时，**必须**暂停执行等待用户评估
- 当情绪强度持续 ≥ 4 时，**必须**建议寻求专业帮助

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `MC_WARNING_HIGH_INTENSITY` | 情绪强度 = 5 | 先做生理调节（深呼吸 10 次） | 🟡 |
| `MC_WARNING_PATTERN_REPEAT` | 触发模式与历史匹配 | 标记重复模式 + 建议根因分析 | 🟡 |
| `MC_WARNING_VALUE_CONFLICT` | 所有选项不对齐价值观 | 暂停执行 + 建议用户评估 | 🟡 |
| `MC_WARNING_FIREWALL_OVERTRIGGER` | 防火墙连续触发 > 3 次 | 评估是否过度防御 | 🟡 |
| `MC_ERROR_PAUSE_FAILED` | 未能创建暂停窗口 | 降级为事后反思模式 | 🔴 |
| `MC_ERROR_NO_OPTIONS` | 无法列出可行选项 | 标记 + 建议扩大选项空间 | 🔴 |

### 降级策略
- 当实时觉察不可用时，降级为事后反思模式
- 当冥想训练不可用时，降级为呼吸练习

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 字段类型与 Schema 一致
- [ ] 元认知编号格式正确（MC-YYYY-MMDD-NNN）

### 内容校验
- [ ] 触发类型已识别
- [ ] 暂停窗口已创建（space_created = true）
- [ ] 至少 2 个视角切换完成
- [ ] 至少 3 个选项列出
- [ ] 有意识选择（非自动驾驶）
- [ ] 事后反思已完成

### 合规校验
- [ ] 觉察 ≠ 自我批判（未出现批判性语言）
- [ ] 情绪强度 ≥ 5 时已先做生理调节
- [ ] 防火墙未过度触发
- [ ] 人工兜底点已正确触发

### OVP 验证信号
- 日均元认知觉察次数 ≥ 3 次
- 自动驾驶切换成功率 ≥ 70%
- 元认知强度周均分 ≥ 5/10
- 冥想/觉察训练执行率 ≥ 80%

---

## 🔄 迭代触发条件

### Self-Play 触发
- **频率**：weekly
- **触发条件**：
  - 每周自动触发（抽样 20% 元认知记录）
  - 元认知强度连续 3 天 < 3 时触发

### 版本升级触发
- minor 版本：新增暂停技术或视角切换方法
- major 版本：改变元认知框架或训练体系

### 废弃触发
- 当元认知强度连续 30 天 < 3 时，标记需要重构训练方案

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
    "name": "情绪觉察-愤怒场景",
    "prompt": "我刚被同事当众批评，非常愤怒",
    "context": "trigger_type=emotion, intensity=4",
    "assertions": [
      "输出包含 trigger_analysis",
      "pause_window.space_created = true",
      "third_person_perspective 至少 2 个视角",
      "choice_point 至少 3 个选项",
      "未出现自我批判语言"
    ],
    "expected_behavior": "识别愤怒触发，创建暂停窗口，切换第三视角，提供有意识选择",
    "critic_attack": "暂停窗口是否足够？3秒能否应对强度4的愤怒？"
  },
  {
    "id": "test-002",
    "name": "习惯打断-刷手机",
    "prompt": "我又无意识刷了30分钟短视频",
    "context": "trigger_type=habit, intensity=3",
    "assertions": [
      "识别为习惯类触发",
      "使用身体扫描法",
      "识别到'逃避'或'无聊'根源",
      "提供替代行为选项"
    ],
    "expected_behavior": "识别习惯自动化，中断回路，找到根源，提供替代",
    "critic_attack": "是否正确识别了习惯根源？是否有遗漏？"
  },
  {
    "id": "test-003",
    "name": "认知防火墙-绝对化断言",
    "prompt": "所有人都应该投资AI，这是必然趋势",
    "context": "firewall_mode=true, intensity=3",
    "assertions": [
      "firewall_result.activated = true",
      "识别到绝对化用词'所有人'和'必然'",
      "counter_examples 至少 3 个",
      "weight_adjustment 已调整"
    ],
    "expected_behavior": "激活防火墙，列出反例，调整信息权重",
    "critic_attack": "反例是否足够有力？是否存在稻草人论证？"
  },
  {
    "id": "test-004",
    "name": "决策觉察-重大选择",
    "prompt": "我是否应该辞职创业",
    "context": "trigger_type=decision, intensity=4",
    "assertions": [
      "使用提问锚定法",
      "至少 3 个视角切换",
      "选项包含短期/长期后果",
      "评估与价值观对齐度",
      "选择有明确理由"
    ],
    "expected_behavior": "深度暂停，多视角审视，有意识选择",
    "critic_attack": "视角切换是否全面？是否遗漏了关键视角？"
  },
  {
    "id": "test-005",
    "name": "高强度情绪-降级处理",
    "prompt": "我极度恐慌，心跳很快",
    "context": "trigger_type=emotion, intensity=5",
    "assertions": [
      "输出包含 MC_WARNING_HIGH_INTENSITY",
      "建议先做生理调节",
      "降级为生理调节模式",
      "未强行执行元认知觉察"
    ],
    "expected_behavior": "识别高强度情绪，降级处理，建议生理调节",
    "critic_attack": "降级策略是否合理？是否有更好的处理方式？"
  }
]
```

---

## 🔗 关联文档

- [[元认知]] — 暂停方法论
- [[元认知觉察法——在自动驾驶与主动控制之间建立切换开关]] — 觉察方法论
- [[uSkill-agent-元认知防火墙]] — 怀疑杠杆 Protocol
- [[系统1与系统2]] — 快慢思维模型
- [[uSkill-Schema-模板]] — 标准化模板
- [[决策推理-Schema]] — 决策推理框架（元认知是决策的质量保障）
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-22 | 1.0.0 | 初始版本：整合暂停法 + 觉察法 + 防火墙 + OVP + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板 · 关联：[[人生操作系统进化-Schema-v2]] · [[决策推理-Schema]]*


---


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [认知任务] for [思考深度], with [问题复杂度], leaning toward [思维框架/分析工具]."

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


**相关概念**：[[观察者]]

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
