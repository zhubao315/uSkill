
description: |
  当用户需要将长文改编为短文、图文、视频脚本，或进行跨平台内容分发时使用此 Skill。
  触发词包括：'改编'、'转化'、'跨平台'、'短视频'、'图文'、
  '内容分发'、'多形态'。
  不适用于原创内容创作（使用文案写作）。当需要将已有内容适配不同平台时优先使用。

---

# uSkill-611: 内容改编

## 🎯 目标

> 将内容从一种形态改编为另一种形态，保持核心信息的同时适应不同平台。

**核心价值**：好内容应该能跨平台传播，而非为每个平台从零创作。

**适用场景**：
- 内容运营
- 跨平台发布
- 知识传播
- 教学设计
- 品牌传播
- 个人IP打造

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `source_content` | `string` | ✅ | — | 原始内容 |
| `source_format` | `enum` | ✅ | — | `article` / `video` / `podcast` / `presentation` |
| `target_format` | `enum` | ✅ | — | `short_article` / `social_post` / `video_script` / `infographic` |
| `platform` | `string` | ❌ | — | 目标平台 |
| `audience` | `string` | ❌ | — | 目标受众 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话改编建议",
  "adaptation_id": "ADPT-YYYY-MMDD-NNN",

  "content_analysis": {
    "core_message": "string",
    "key_points": ["string"],
    "supporting_evidence": ["string"],
    "target_audience": "string"
  },

  "format_strategy": {
    "source_format": "string",
    "target_format": "string",
    "adaptation_approach": "string",
    "key_transformations": ["string"]
  },

  "platform_optimization": {
    "platform": "string",
    "algorithm_considerations": ["string"],
    "best_practices": ["string"],
    "content_length": "string",
    "hashtag_strategy": ["string"]
  },

  "adapted_content": {
    "title": "string",
    "body": "string",
    "key_elements": ["string"],
    "call_to_action": "string",
    "visual_suggestions": ["string"]
  },

  "content_variants": [
    {
      "variant": "string",
      "platform": "string",
      "title": "string",
      "body": "string",
      "key_differences": "string"
    }
  ],

  "distribution_plan": {
    "timeline": "string",
    "cross_promotion": ["string"],
    "engagement_strategy": "string"
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

### Step 1: 内容分析

- **输入**：`source_content` + `source_format`
- **动作**：
  1. 提取核心信息
  2. 识别关键点
  3. 分析支撑证据
- **输出**：`content_analysis`
- **内容分析维度**：

| 维度 | 问题 | 目的 |
|------|------|------|
| 核心信息 | 最重要的一句话是什么？ | 保留精华 |
| 关键点 | 有哪些支撑点？ | 内容结构 |
| 证据 | 有哪些数据/案例？ | 可信度 |
| 受众 | 原本面向谁？ | 适配参考 |

**分支条件**：
- 若 `source_format=article` → 提取段落结构和论点
- 若 `source_format=video` → 提取时间轴和画面
- 若 `source_format=podcast` → 提取话题和金句
- 若 `source_format=presentation` → 提取页面和逻辑

### Step 2: 改编策略设计

- **输入**：`content_analysis` + `target_format`
- **动作**：
  1. 选择改编方法
  2. 确定变换重点
  3. 设计改编流程
- **输出**：`format_strategy`
- **改编方法指南**：

| 原格式 | 目标格式 | 改编方法 | 重点 |
|--------|----------|----------|------|
| 长文 | 短文 | 提炼+压缩 | 保留核心 |
| 文章 | 社交帖 | 切片+强化 | 冲击力 |
| 文章 | 视觉化 | 转化+图示 | 视觉呈现 |
| 视频 | 文字 | 提取+整理 | 信息完整 |
| 播客 | 文字 | 转录+编辑 | 可读性 |

**分支条件**：
- 若 `target_format=short_article` → 压缩至500-1000字
- 若 `target_format=social_post` → 压缩至100-300字
- 若 `target_format=video_script` → 转化为口语化脚本
- 若 `target_format=infographic` → 转化为视觉化信息

### Step 3: 平台适配优化

- **输入**：`format_strategy` + `platform`
- **动作**：
  1. 分析平台算法
  2. 应用最佳实践
  3. 优化内容参数
- **输出**：`platform_optimization`
- **平台适配指南**：

| 平台 | 内容特点 | 最佳实践 | 算法考量 |
|------|----------|----------|----------|
| 微信公众号 | 深度长文 | 标题+封面+排版 | 完读率+分享 |
| 小红书 | 图文种草 | 封面+标签+互动 | 收藏+互动 |
| 抖音 | 短视频 | 前3秒+节奏+BGM | 完播率+互动 |
| B站 | 中长视频 | 标题+封面+弹幕 | 播放量+互动 |
| 知乎 | 专业回答 | 深度+数据+案例 | 赞同+收藏 |
| 微博 | 热点话题 | 话题+图片+互动 | 转发+评论 |

**分支条件**：
- 若 `platform=微信` → 长度5000-8000字，深度分析
- 若 `platform=小红书` → 长度300-500字，图片优先
- 若 `platform=抖音` → 时长15-60秒，节奏快
- 若 `platform=B站` → 时长5-15分钟，有深度
- 若 `platform=知乎` → 长度2000-5000字，有数据
- 若 `platform=微博` → 长度140-200字，有话题

### Step 4: 内容改编生成

- **输入**：`content_analysis` + `format_strategy` + `platform_optimization`
- **动作**：
  1. 生成改编内容
  2. 优化标题和正文
  3. 设计行动号召
- **输出**：`adapted_content`
- **改编技巧**：

| 技巧 | 目的 | 示例 |
|------|------|------|
| 提炼金句 | 增加传播力 | 提取原文精华 |
| 制造冲突 | 吸引注意力 | 对比+反转 |
| 添加互动 | 提升参与 | 问题+投票 |
| 视觉化 | 增强理解 | 图表+案例 |
| 口语化 | 亲切感 | 像朋友聊天 |

**分支条件**：
- 若 `target_format=social_post` → 强化金句和互动
- 若 `target_format=short_article` → 保持结构完整
- 若 `target_format=video_script` → 口语化+画面提示
- 若 `target_format=infographic` → 视觉化+数据化

### Step 5: 多平台分发规划

- **输入**：`adapted_content` + `platform`
- **动作**：
  1. 生成多平台变体
  2. 制定分发时间线
  3. 设计交叉推广策略
- **输出**：`content_variants` + `distribution_plan`
- **分发策略**：

| 策略 | 目的 | 方法 |
|------|------|------|
| 同步发布 | 最大化覆盖 | 同时发布 |
| 错峰发布 | 持续曝光 | 分时段发布 |
| 话题串联 | 形成矩阵 | 统一话题 |
| 互动引导 | 提升参与 | 跨平台互动 |

**分支条件**：
- 若资源充足 → 同步发布+话题串联
- 若资源有限 → 错峰发布+核心平台优先
- 若需要测试 → 先小范围测试再全量发布
- 若有时间敏感性 → 立即发布核心平台

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**歪曲原意或断章取义
2. **不得**侵犯版权或知识产权
3. **必须**保留核心信息
4. **必须**适应平台特点

### 软性约束（建议遵守）
1. 建议保持内容质量
2. 建议适配平台算法
3. 建议保持品牌一致性
4. 建议跟踪效果数据

### 人工兜底点
- 当涉及版权问题时，**必须**确认授权
- 当内容敏感时，**必须**谨慎处理
- 当平台政策变化时，**必须**及时调整

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `ADPT_WARNING_ORIGINAL` | 歪曲原意 | 建议重新改编 | 🟡 |
| `ADPT_ERROR_COPYRIGHT` | 版权问题 | 建议确认授权 | 🔴 |
| `ADPT_WARNING_PLATFORM` | 不适合平台 | 建议调整格式 | 🟡 |
| `ADPT_WARNING_LENGTH` | 长度不当 | 建议调整篇幅 | 🟡 |
| `ADPT_WARNING_STYLE` | 风格不匹配 | 建议调整语调 | 🟡 |
| `ADPT_ERROR_QUALITY` | 质量下降 | 建议重新改编 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 改编内容符合平台要求

### 内容校验
- [ ] 核心信息已保留
- [ ] 适应了平台特点
- [ ] 质量未下降
- [ ] 风格一致
- [ ] 无版权问题

### OVP 验证信号
- 内容适配准确率 ≥ 90%
- 平台效果达到预期
- 用户反馈正面 ≥ 85%

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 歪曲原意 | 重新改编 | P1 |
| 平台效果差 | 优化适配 | P1 |
| 版权问题 | 确认授权 | P0 |
| 质量下降 | 重新改编 | P1 |
| 用户反馈负面 | 调整策略 | P2 |

---

## 📝 自检清单

- [ ] 原始内容是否分析完整？
- [ ] 核心信息是否保留？
- [ ] 目标格式是否明确？
- [ ] 平台适配是否到位？
- [ ] 改编内容是否清晰？
- [ ] 标题是否吸引人？
- [ ] 正文是否流畅？
- [ ] 行动号召是否明确？
- [ ] 是否有版权问题？
- [ ] 是否制定了分发计划？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-611-01",
  "name": "长文转小红书",
  "prompt": "将这篇3000字的文章改编为小红书图文",
  "input": {
    "source_content": "关于时间管理的深度文章，包含5个方法和案例",
    "source_format": "article",
    "target_format": "social_post",
    "platform": "小红书",
    "audience": "职场新人"
  },
  "assertions": [
    "content_analysis.core_message 已提取",
    "format_strategy.adaptation_approach 已确定",
    "platform_optimization.hashtag_strategy 包含标签",
    "adapted_content.body 长度 <= 500字"
  ],
  "expected_behavior": "将长文压缩为适合小红书的图文",
  "critic_attack": "是否保留了核心信息？是否适合小红书风格？"
}
```

### 测试用例 2
```json
{
  "id": "test-611-02",
  "name": "文章转短视频脚本",
  "prompt": "将这篇技术文章改编为1分钟短视频脚本",
  "input": {
    "source_content": "关于AI编程的技术文章",
    "source_format": "article",
    "target_format": "video_script",
    "platform": "抖音",
    "audience": "技术爱好者"
  },
  "assertions": [
    "content_analysis.key_points 提取关键点",
    "format_strategy.key_transformations 包含口语化",
    "adapted_content.body 包含画面提示",
    "adapted_content.body 长度适合1分钟"
  ],
  "expected_behavior": "将技术文章转化为短视频脚本",
  "critic_attack": "是否将复杂概念简化？是否适合短视频节奏？"
}
```

### 测试用例 3
```json
{
  "id": "test-611-03",
  "name": "视频转公众号文章",
  "prompt": "将这个10分钟的视频转化为公众号文章",
  "input": {
    "source_content": "产品发布会完整视频",
    "source_format": "video",
    "target_format": "article",
    "platform": "微信公众号",
    "audience": "产品用户"
  },
  "assertions": [
    "content_analysis.core_message 已提取",
    "format_strategy.adaptation_approach = 提取+整理",
    "adapted_content.body 包含完整信息",
    "adapted_content.body 长度 3000-5000字"
  ],
  "expected_behavior": "将视频内容转化为深度文章",
  "critic_attack": "是否包含了视频的关键信息？文章是否可读？"
}
```

### 测试用例 4
```json
{
  "id": "test-611-04",
  "name": "文章转信息图",
  "prompt": "将这篇数据分析文章转化为信息图",
  "input": {
    "source_content": "关于用户行为分析的数据报告",
    "source_format": "article",
    "target_format": "infographic",
    "platform": "全平台",
    "audience": "产品经理"
  },
  "assertions": [
    "content_analysis.supporting_evidence 提取数据",
    "format_strategy.key_transformations 包含视觉化",
    "adapted_content.body 包含数据可视化建议",
    "adapted_content.visual_suggestions 包含图表建议"
  ],
  "expected_behavior": "将数据文章转化为视觉化信息图",
  "critic_attack": "数据是否清晰呈现？信息图是否易于理解？"
}
```

### 测试用例 5
```json
{
  "id": "test-611-05",
  "name": "多平台分发",
  "prompt": "将这篇内容改编并分发到3个平台",
  "input": {
    "source_content": "关于个人成长的深度思考",
    "source_format": "article",
    "target_format": "social_post",
    "platform": "微信+小红书+知乎",
    "audience": "职场人士"
  },
  "assertions": [
    "content_variants.length >= 3",
    "content_variants 包含3个平台变体",
    "distribution_plan.timeline 已制定",
    "distribution_plan.cross_promotion 包含策略"
  ],
  "expected_behavior": "为不同平台生成适配内容",
  "critic_attack": "每个平台的变体是否真正适配？分发策略是否合理？"
}
```

---

## 🔗 关联文档

- [[创意写作]] — 内容的故事化改编
- [[文案写作]] — 改编内容的文案优化
- [[数据可视化]] — 数据内容的视觉化改编
- [[说服力写作]] — 改编内容的说服力增强
- [[创意发散]] — 改编创意的发散思维

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：内容分析 + 格式改编 + 平台适配 + Self-Play |

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
