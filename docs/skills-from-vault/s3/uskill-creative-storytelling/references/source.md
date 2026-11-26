
description: |
  当用户需要用故事包装观点、增强说服力、制作演示文稿、进行品牌叙事时使用此 Skill。
  触发词包括：'故事'、'叙事'、'讲故事'、'演示'、'品牌故事'、
  '内容营销'、'情感共鸣'、'包装观点'。
  不适用于纯数据报告（使用数据可视化）。遇到需要情感共鸣的场景时优先使用。

---

# uSkill-605: 故事化表达

## 🎯 目标

> 用故事结构包装观点和信息，增强说服力和记忆度，建立情感连接。

**核心价值**：人类大脑天生喜欢故事。好故事能让信息深入人心。

**适用场景**：
- 演讲和演示
- 品牌营销
- 内容创作
- 产品介绍
- 团队沟通
- 培训教学

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `core_message` | `string` | ✅ | — | 核心信息/观点 |
| `audience` | `string` | ✅ | — | 目标受众 |
| `purpose` | `enum` | ❌ | `persuade` | `persuade` / `inform` / `entertain` / `inspire` |
| `medium` | `enum` | ❌ | `speech` | `speech` / `written` / `video` / `social` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话故事框架建议",
  "story_id": "ST-YYYY-MMDD-NNN",

  "story_structure": {
    "framework": "string",
    "elements": {
      "hero": "string",
      "villain": "string",
      "conflict": "string",
      "journey": "string",
      "resolution": "string",
      "moral": "string"
    }
  },

  "narrative_arc": [
    {
      "stage": "setup|rising_action|climax|falling_action|resolution",
      "duration_percentage": "number",
      "content": "string",
      "emotional_curve": "string"
    }
  ],

  "storytelling_techniques": [
    {
      "technique": "string",
      "description": "string",
      "application": "string"
    }
  ],

  "audience_engagement": {
    "hooks": ["string"],
    "emotional_triggers": ["string"],
    "call_to_action": "string"
  },

  "script_or_outline": {
    "opening": "string",
    "body": "string",
    "closing": "string",
    "key_moments": ["string"]
  },

  "delivery_tips": {
    "pacing": "string",
    "emphasis": ["string"],
    "visual_aids": ["string"]
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

### Step 1: 故事框架选择

- **输入**：`core_message` + `purpose`
- **动作**：
  1. 分析核心信息
  2. 选择适合的故事框架
  3. 定义故事元素
- **输出**：`story_structure`
- **故事框架选择**：

| 框架 | 结构 | 适用场景 |
|------|------|----------|
| 英雄之旅 | 冒险-挑战-成长 | 激励、品牌故事 |
| 三幕剧 | 设置-对抗-解决 | 演讲、演示 |
| 问题-解决方案 | 问题-分析-方案 | 商业演示 |
| 起承转合 | 引入-发展-转折-结局 | 中式叙事 |

**分支条件**：
- 若 `purpose=inspire` → 优先选择英雄之旅
- 若 `purpose=inform` → 优先选择问题-解决方案
- 若 `purpose=entertain` → 优先选择三幕剧
- 若 `purpose=persuade` → 根据 `medium` 决定

### Step 2: 叙事弧线设计

- **输入**：`story_structure`
- **动作**：
  1. 设计情感曲线
  2. 安排节奏
  3. 制定关键时刻
- **输出**：`narrative_arc`
- **叙事弧线阶段**：

| 阶段 | 目的 | 时长占比 |
|------|------|----------|
| 设置 | 建立背景和角色 | 15-20% |
| 上升 | 建立冲突和张力 | 30-40% |
| 高潮 | 最紧张时刻 | 10-15% |
| 下降 | 解决冲突 | 15-20% |
| 结局 | 总结和启示 | 10-15% |

**分支条件**：
- 若 `medium=speech` → 增加互动停顿点
- 若 `medium=written` → 增加视觉过渡标记
- 若 `medium=video` → 增加画面节奏说明

### Step 3: 故事技巧应用

- **输入**：`story_structure` + `medium`
- **动作**：
  1. 选择适合的技巧
  2. 应用到故事中
  3. 增强感染力
- **输出**：`storytelling_techniques`
- **故事技巧库**：

| 技巧 | 描述 | 应用 |
|------|------|------|
| 悬念 | 制造好奇心 | 开场、过渡 |
| 对比 | 突出差异 | 强调重点 |
| 细节 | 增加真实感 | 角色塑造 |
| 重复 | 加强记忆 | 核心信息 |
| 转折 | 制造惊喜 | 高潮 |
| 感官描写 | 增强沉浸感 | 场景构建 |

**分支条件**：
- 若受众为专业人士 → 减少情感技巧，增加数据支撑
- 若受众为普通大众 → 增加情感技巧，减少专业术语
- 若媒介为社交 → 缩短技巧应用，强调冲击力

### Step 4: 受众参与设计

- **输入**：`audience` + `purpose`
- **动作**：
  1. 设计开场钩子
  2. 识别情感触发点
  3. 制定行动号召
- **输出**：`audience_engagement`
- **钩子类型**：

| 类型 | 示例 | 适用场景 |
|------|------|----------|
| 悬念钩子 | "你有没有遇到过..." | 通用 |
| 数据钩子 | "90%的人不知道..." | 理性受众 |
| 情感钩子 | "那一刻，我明白了..." | 感性受众 |
| 冲突钩子 | "我们曾经面临..." | 团队沟通 |

**分支条件**：
- 若 `purpose=persuade` → 行动号召必须明确具体
- 若 `purpose=inspire` → 行动号召可以是开放式反思
- 若 `purpose=inform` → 行动号召可以是信息获取建议

### Step 5: 脚本/大纲生成

- **输入**：所有前序输出
- **动作**：
  1. 生成开场、主体、结尾
  2. 标注关键时刻
  3. 提供交付建议
- **输出**：`script_or_outline` + `delivery_tips`
- **脚本结构**：

| 部分 | 内容要求 | 时长占比 |
|------|----------|----------|
| 开场 | 钩子 + 背景 + 主题 | 15-20% |
| 主体 | 故事发展 + 冲突 + 转折 | 60-70% |
| 结尾 | 高潮 + 解决 + 启示 | 15-20% |

**分支条件**：
- 若 `medium=speech` → 提供语速和停顿建议
- 若 `medium=written` → 提供段落和过渡建议
- 若 `medium=video` → 提供画面和音效建议
- 若 `medium=social` → 提供字数和标签建议

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**编造虚假信息
2. **不得**操纵听众情感（区别于说服）
3. **必须**确保故事与核心信息一致
4. **必须**尊重受众的文化背景

### 软性约束（建议遵守）
1. 建议先了解受众背景
2. 建议练习至少 3 次
3. 建议收集反馈并迭代
4. 建议准备备选方案

### 人工兜底点
- 当涉及敏感话题时，**必须**谨慎处理
- 当需要专业叙事时，**必须**建议专业帮助
- 当受众反馈负面时，**必须**调整策略

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `ST_WARNING_MISALIGNMENT` | 故事与信息不一致 | 建议调整故事元素 | 🟡 |
| `ST_WARNING_AUDIENCE` | 不适合受众风格 | 建议调整风格 | 🟡 |
| `ST_ERROR_NO_STORY` | 无法构建故事 | 建议简化信息或换框架 | 🔴 |
| `ST_WARNING_CULTURAL` | 文化敏感性问题 | 建议修改元素 | 🟡 |
| `ST_ERROR_MEDIUM` | 媒介不适合 | 建议更换媒介或调整 | 🔴 |
| `ST_WARNING_LENGTH` | 故事过长或过短 | 建议调整篇幅 | 🟡 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] ID 格式符合 SKL-XXX 规范

### 内容校验
- [ ] 故事框架已选择且适合目的
- [ ] 叙事弧线完整覆盖五个阶段
- [ ] 故事技巧已应用且自然
- [ ] 脚本/大纲已生成
- [ ] 受众参与设计已包含

### OVP 验证信号
- 故事吸引力评分 ≥ 80/100
- 信息传达效果 ≥ 75%
- 受众参与度 ≥ 70%

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 故事吸引力评分 < 80 | 重新选择框架 | P1 |
| 受众反馈负面 | 调整风格和技巧 | P1 |
| 信息传达率 < 75% | 强化核心信息 | P1 |
| 中期检查发现不一致 | 重新设计叙事弧线 | P2 |
| 媒介变更 | 调整交付建议 | P2 |

---

## 📝 自检清单

- [ ] 核心信息是否明确？
- [ ] 受众画像是否清晰？
- [ ] 故事框架是否适合目的？
- [ ] 叙事弧线是否完整？
- [ ] 情感曲线是否自然？
- [ ] 故事技巧是否过度使用？
- [ ] 脚本/大纲是否可执行？
- [ ] 交付建议是否具体？
- [ ] 是否有文化敏感性问题？
- [ ] 是否准备了备选方案？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-605-01",
  "name": "产品发布故事",
  "prompt": "为我们的新产品发布会设计一个开场故事",
  "input": {
    "core_message": "我们的产品能解决用户的核心痛点",
    "audience": "潜在客户",
    "purpose": "persuade",
    "medium": "speech"
  },
  "assertions": [
    "story_structure.framework 已选择",
    "narrative_arc 包含完整弧线",
    "audience_engagement.hooks 已设计",
    "script_or_outline.opening 包含钩子"
  ],
  "expected_behavior": "设计有吸引力的产品发布故事",
  "critic_attack": "故事是否真正吸引人？是否能记住产品卖点？"
}
```

### 测试用例 2
```json
{
  "id": "test-605-02",
  "name": "品牌创业故事",
  "prompt": "讲述我们公司的创业故事，激励团队",
  "input": {
    "core_message": "从零到一的创业历程",
    "audience": "团队成员",
    "purpose": "inspire",
    "medium": "speech"
  },
  "assertions": [
    "story_structure.elements.hero 已定义",
    "narrative_arc 包含困难和克服",
    "storytelling_techniques 包含情感技巧",
    "audience_engagement.call_to_action 包含激励"
  ],
  "expected_behavior": "创作激励人心的品牌故事",
  "critic_attack": "故事是否真实可信？是否能激发团队斗志？"
}
```

### 测试用例 3
```json
{
  "id": "test-605-03",
  "name": "数据报告故事化",
  "prompt": "将这份枯燥的数据报告变成一个引人入胜的故事",
  "input": {
    "core_message": "数据表明我们需要改变策略",
    "audience": "管理层",
    "purpose": "inform",
    "medium": "written"
  },
  "assertions": [
    "story_structure.framework = 问题-解决方案",
    "script_or_outline 包含关键数据点",
    "delivery_tips.visual_aids 已建议",
    "audience_engagement.hooks 包含数据钩子"
  ],
  "expected_behavior": "将数据转化为故事",
  "critic_attack": "是否保持了数据的准确性？故事是否清晰？"
}
```

### 测试用例 4
```json
{
  "id": "test-605-04",
  "name": "社交媒体故事",
  "prompt": "为我们的品牌创作一个适合小红书的故事帖",
  "input": {
    "core_message": "生活方式的改变",
    "audience": "年轻用户",
    "purpose": "entertain",
    "medium": "social"
  },
  "assertions": [
    "script_or_outline 符合社交媒体字数限制",
    "audience_engagement.hooks 具有冲击力",
    "storytelling_techniques 包含视觉元素"
  ],
  "expected_behavior": "创作适合社交媒体的故事",
  "critic_attack": "故事是否能在3秒内抓住注意力？"
}
```

### 测试用例 5
```json
{
  "id": "test-605-05",
  "name": "培训教学故事",
  "prompt": "用故事来讲解复杂的概念，让学员更容易理解",
  "input": {
    "core_message": "抽象概念的具体应用",
    "audience": "新入职员工",
    "purpose": "inform",
    "medium": "speech"
  },
  "assertions": [
    "story_structure.framework = 问题-解决方案 或 起承转合",
    "storytelling_techniques 包含类比技巧",
    "script_or_outline.body 包含步骤分解",
    "delivery_tips.pacing 包含互动点"
  ],
  "expected_behavior": "用故事简化复杂概念",
  "critic_attack": "故事是否让概念更易理解？是否有趣？"
}
```

---

## 🔗 关联文档

- [[文案写作]] — 文案技巧与故事结合
- [[说服力写作]] — 影响力原则在故事中的应用
- [[演讲节奏控制]] — 故事的演讲交付
- [[创意发散]] — 故事创意的发散思维
- [[数据可视化]] — 数据的故事化呈现

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：故事框架 + 叙事弧线 + 技巧应用 + Self-Play |

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


**相关概念**：[[事实与观点]]

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
