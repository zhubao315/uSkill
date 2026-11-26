
description: |
  当用户需要控制演讲节奏、设计情绪曲线、把握停顿技巧、优化演讲结构时使用此 Skill。
  触发词包括：'演讲节奏'、'停顿'、'情绪曲线'、'演讲结构'、'起承转合'、
  '演讲技巧'、'演讲控制'。
  不适用于纯文本写作（使用文案写作）。当需要口头表达的节奏控制时优先使用。

---

# uSkill-607: 演讲节奏控制

## 🎯 目标

> 掌握演讲的起承转合，运用停顿技巧，设计情绪曲线，提升演讲效果。

**核心价值**：好的节奏能让演讲引人入胜，坏的节奏会让听众昏昏欲睡。

**适用场景**：
- 公开演讲
- 产品发布
- 培训授课
- 路演演示
- 会议发言
- 团队汇报

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `speech_content` | `string` | ✅ | — | 演讲内容/大纲 |
| `duration` | `number` | ✅ | — | 演讲时长（分钟） |
| `audience` | `string` | ✅ | — | 目标受众 |
| `purpose` | `enum` | ❌ | `persuade` | `persuade` / `inform` / `inspire` / `entertain` |
| `skill_level` | `enum` | ❌ | `intermediate` | `beginner` / `intermediate` / `advanced` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话节奏建议",
  "rhythm_id": "RHY-YYYY-MMDD-NNN",

  "structure": {
    "sections": [
      {
        "name": "string",
        "duration_percentage": "number",
        "pacing": "fast|medium|slow",
        "techniques": ["string"]
      }
    ],
    "total_sections": "number",
    "balance_score": "number"
  },

  "pause_strategy": {
    "types": [
      {
        "type": "string",
        "purpose": "string",
        "duration": "string",
        "placement": "string"
      }
    ],
    "total_pauses": "number",
    "average_duration": "string"
  },

  "emotional_curve": {
    "stages": [
      {
        "stage": "string",
        "intensity": "number",
        "techniques": ["string"]
      }
    ],
    "peak_moments": ["string"],
    "resolution": "string"
  },

  "delivery_script": {
    "sections": [
      {
        "content": "string",
        "pacing_note": "string",
        "pause_markers": ["string"],
        "emphasis_words": ["string"]
      }
    ]
  },

  "practice_guide": {
    "warmup": ["string"],
    "key_exercises": ["string"],
    "common_mistakes": ["string"]
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

### Step 1: 结构分析与划分

- **输入**：`speech_content` + `duration`
- **动作**：
  1. 分析内容结构
  2. 划分演讲段落
  3. 分配时间比例
- **输出**：`structure`
- **结构划分指南**：

| 段落 | 目的 | 时间占比 | 节奏 |
|------|------|----------|------|
| 开场 | 吸引注意力 | 10-15% | 慢→快 |
| 主体 | 传达信息 | 60-70% | 中→快→中 |
| 高潮 | 强调重点 | 10-15% | 快→慢 |
| 结尾 | 总结行动 | 10-15% | 慢→稳 |

**分支条件**：
- 若 `duration < 10分钟` → 简化结构，减少段落
- 若 `duration > 30分钟` → 增加互动环节
- 若 `purpose=inspire` → 增加情感段落
- 若 `purpose=inform` → 增加数据段落

### Step 2: 停顿策略设计

- **输入**：`structure` + `skill_level`
- **动作**：
  1. 识别停顿点
  2. 设计停顿类型
  3. 确定停顿时长
- **输出**：`pause_strategy`
- **停顿类型**：

| 类型 | 目的 | 时长 | 适用场景 |
|------|------|------|----------|
| 强调停顿 | 突出重点 | 2-3秒 | 关键观点后 |
| 思考停顿 | 给听众思考 | 3-5秒 | 复杂概念后 |
| 转换停顿 | 段落过渡 | 1-2秒 | 段落之间 |
| 紧张停顿 | 制造悬念 | 5-10秒 | 问题提出后 |
| 恢复停顿 | 调整节奏 | 1-2秒 | 快节奏后 |

**分支条件**：
- 若 `skill_level=beginner` → 减少紧张停顿
- 若 `skill_level=advanced` → 增加戏剧性停顿
- 若 `duration < 10分钟` → 减少总停顿次数
- 若 `duration > 30分钟` → 增加恢复停顿

### Step 3: 情绪曲线设计

- **输入**：`structure` + `purpose`
- **动作**：
  1. 设计情绪强度
  2. 规划高潮时刻
  3. 确定收尾方式
- **输出**：`emotional_curve`
- **情绪曲线模型**：

| 模型 | 结构 | 适用场景 |
|------|------|----------|
| 山峰型 | 低-高-低 | 激励演讲 |
| 波浪型 | 多次起伏 | 长时间演讲 |
| 线性增长 | 低-高 | 说服演讲 |
| U型 | 高-低-高 | 戏剧性演讲 |

**分支条件**：
- 若 `purpose=inspire` → 使用山峰型，高潮在80%处
- 若 `purpose=persuade` → 使用波浪型，多个小高潮
- 若 `purpose=inform` → 使用线性增长，稳步提升
- 若 `purpose=entertain` → 使用U型，中间有反转

### Step 4: 交付脚本生成

- **输入**：`structure` + `pause_strategy` + `emotional_curve`
- **动作**：
  1. 生成分段脚本
  2. 标注节奏提示
  3. 添加停顿标记
- **输出**：`delivery_script`
- **脚本标注系统**：

| 标记 | 含义 | 示例 |
|------|------|------|
| [P1] | 强调停顿 | 观点后 |
| [P2] | 思考停顿 | 问题后 |
| [P3] | 转换停顿 | 段落间 |
| [F] | 快速 | 紧张部分 |
| [S] | 慢速 | 强调部分 |
| [R] | 正常 | 一般内容 |
| *word* | 强调词语 | 重点词 |

**分支条件**：
- 若 `skill_level=beginner` → 增加详细标注
- 若 `skill_level=advanced` → 减少标注，保留关键提示
- 若 `medium=presentation` → 增加视觉配合提示
- 若 `medium=video` → 增加画面切换提示

### Step 5: 练习指南生成

- **输入**：所有前序输出
- **动作**：
  1. 设计热身练习
  2. 提供关键练习
  3. 列出常见错误
- **输出**：`practice_guide`
- **热身练习**：

| 练习 | 目的 | 时长 |
|------|------|------|
| 呼吸练习 | 稳定情绪 | 2分钟 |
| 口腔操 | 发音清晰 | 3分钟 |
| 朗读练习 | 熟悉内容 | 5分钟 |
| 录音回听 | 自我评估 | 10分钟 |

**分支条件**：
- 若 `duration < 10分钟` → 简化热身
- 若 `duration > 30分钟` → 增加体力准备
- 若 `skill_level=beginner` → 增加基础练习
- 若 `skill_level=advanced` → 增加高级技巧

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**过度使用停顿导致冷场
2. **不得**让节奏变化生硬不自然
3. **必须**确保节奏服务于内容
4. **必须**尊重听众的注意力

### 软性约束（建议遵守）
1. 建议提前演练至少 3 次
2. 建议录音回听并调整
3. 建议准备应对突发情况
4. 建议了解场地和设备

### 人工兜底点
- 当遇到技术故障时，**必须**保持镇定
- 当听众反应冷淡时，**必须**调整策略
- 当时间不足时，**必须**优先保留核心内容

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `RHY_WARNING_PACING` | 节奏过快或过慢 | 建议调整段落 | 🟡 |
| `RHY_WARNING_PAUSE` | 停顿过多或过少 | 建议重新分配 | 🟡 |
| `RHY_ERROR_STRUCTURE` | 结构混乱 | 建议重新划分 | 🔴 |
| `RHY_WARNING_EMOTION` | 情绪曲线平淡 | 建议增加高潮 | 🟡 |
| `RHY_ERROR_TIME` | 时间分配不当 | 建议删减内容 | 🔴 |
| `RHY_WARNING_ENGAGE` | 缺乏互动 | 建议增加互动点 | 🟡 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 时间分配总和为 100%

### 内容校验
- [ ] 结构划分合理
- [ ] 停顿策略完整
- [ ] 情绪曲线有层次
- [ ] 脚本标注清晰
- [ ] 练习指南实用

### OVP 验证信号
- 演讲节奏满意度 ≥ 85/100
- 观众参与度 ≥ 80%
- 信息留存率 ≥ 75%

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 节奏过快或过慢 | 调整段落时长 | P1 |
| 情绪曲线平淡 | 增加高潮时刻 | P1 |
| 结构混乱 | 重新划分段落 | P0 |
| 停顿不当 | 重新分配停顿点 | P2 |
| 练习不足 | 增加练习指导 | P2 |

---

## 📝 自检清单

- [ ] 结构划分是否合理？
- [ ] 时间分配是否均衡？
- [ ] 停顿点是否自然？
- [ ] 情绪曲线是否有层次？
- [ ] 高潮时刻是否明确？
- [ ] 脚本标注是否清晰？
- [ ] 练习指南是否实用？
- [ ] 是否考虑了场地因素？
- [ ] 是否准备了应对方案？
- [ ] 是否演练过至少 3 次？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-607-01",
  "name": "10分钟产品发布",
  "prompt": "为10分钟的产品发布演讲设计节奏",
  "input": {
    "speech_content": "新产品功能介绍、优势、使用案例、行动号召",
    "duration": 10,
    "audience": "潜在客户",
    "purpose": "persuade",
    "skill_level": "intermediate"
  },
  "assertions": [
    "structure.total_sections >= 4",
    "structure.balance_score >= 80",
    "pause_strategy.total_pauses >= 5",
    "emotional_curve.peak_moments 包含高潮"
  ],
  "expected_behavior": "设计紧凑有力的演讲节奏",
  "critic_attack": "节奏是否紧凑？是否能在10分钟内完成？"
}
```

### 测试用例 2
```json
{
  "id": "test-607-02",
  "name": "30分钟培训授课",
  "prompt": "设计30分钟培训课程的演讲节奏",
  "input": {
    "speech_content": "概念讲解、案例分析、互动练习、总结",
    "duration": 30,
    "audience": "新员工",
    "purpose": "inform",
    "skill_level": "beginner"
  },
  "assertions": [
    "structure.sections 包含互动环节",
    "pause_strategy.types 包含恢复停顿",
    "practice_guide.warmup 包含热身",
    "delivery_script.sections 标注清晰"
  ],
  "expected_behavior": "设计适合新手的培训节奏",
  "critic_attack": "节奏是否适合新手？是否有足够的互动？"
}
```

### 测试用例 3
```json
{
  "id": "test-607-03",
  "name": "5分钟团队汇报",
  "prompt": "设计5分钟团队汇报的演讲节奏",
  "input": {
    "speech_content": "项目进展、成果、挑战、下一步",
    "duration": 5,
    "audience": "管理层",
    "purpose": "inform",
    "skill_level": "advanced"
  },
  "assertions": [
    "structure.total_sections <= 4",
    "pause_strategy.total_pauses <= 3",
    "emotional_curve.stages 简洁",
    "delivery_script.sections 标注精简"
  ],
  "expected_behavior": "设计简洁高效的汇报节奏",
  "critic_attack": "节奏是否高效？是否能在5分钟内完成？"
}
```

### 测试用例 4
```json
{
  "id": "test-607-04",
  "name": "20分钟激励演讲",
  "prompt": "设计20分钟激励演讲的节奏",
  "input": {
    "speech_content": "挑战、成长、成功、愿景",
    "duration": 20,
    "audience": "全体员工",
    "purpose": "inspire",
    "skill_level": "intermediate"
  },
  "assertions": [
    "emotional_curve.stages 使用山峰型",
    "emotional_curve.peak_moments 包含高潮",
    "pause_strategy.types 包含紧张停顿",
    "practice_guide.key_exercises 包含情感练习"
  ],
  "expected_behavior": "设计激励人心的演讲节奏",
  "critic_attack": "情绪曲线是否有感染力？高潮是否足够震撼？"
}
```

### 测试用例 5
```json
{
  "id": "test-607-05",
  "name": "15分钟路演演示",
  "prompt": "设计15分钟路演演示的节奏",
  "input": {
    "speech_content": "问题、解决方案、市场、团队、融资",
    "duration": 15,
    "audience": "投资人",
    "purpose": "persuade",
    "skill_level": "advanced"
  },
  "assertions": [
    "structure.sections 包含完整路演结构",
    "emotional_curve.stages 使用波浪型",
    "pause_strategy.types 包含强调停顿",
    "delivery_script.sections 包含数据强调"
  ],
  "expected_behavior": "设计有说服力的路演节奏",
  "critic_attack": "节奏是否能抓住投资人注意力？是否突出了关键信息？"
}
```

---

## 🔗 关联文档

- [[创意写作]] — 演讲内容的故事化
- [[说服力写作]] — 演讲的说服力技巧
- [[文案写作]] — 演讲稿的写作技巧
- [[创意发散]] — 演讲创意的发散思维
- [[内容改编]] — 演讲内容的多形态改编

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：结构划分 + 停顿策略 + 情绪曲线 + Self-Play |

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
