
description: |
  当用户需要将数据转化为图表、制作数据报告、设计信息图、创建仪表盘时使用此 Skill。
  触发词包括：'数据可视化'、'图表'、'信息图'、'仪表盘'、'数据报告'、
  '图表选型'、'可视化叙事'。
  不适用于纯文本故事（使用故事化表达）。当需要数据支撑的视觉呈现时优先使用。

---

# uSkill-606: 数据可视化

## 🎯 目标

> 将复杂数据转化为清晰、直观、有洞察力的可视化图表。

**核心价值**：好的数据可视化能让数据自己说话，帮助决策者快速理解。

**适用场景**：
- 报告制作
- 数据汇报
- 信息图设计
- 仪表盘创建
- 学术展示
- 商业演示

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `data_description` | `string` | ✅ | — | 数据描述和来源 |
| `data_type` | `enum` | ✅ | — | `comparison` / `distribution` / `composition` / `trend` / `relationship` |
| `audience` | `string` | ✅ | — | 目标受众 |
| `purpose` | `enum` | ❌ | `inform` | `inform` / `persuade` / `explore` / `present` |
| `medium` | `enum` | ❌ | `report` | `report` / `dashboard` / `infographic` / `presentation` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话可视化建议",
  "viz_id": "VIZ-YYYY-MMDD-NNN",

  "chart_selection": {
    "primary_chart": "string",
    "secondary_charts": ["string"],
    "rationale": "string"
  },

  "data_story": {
    "headline": "string",
    "key_insights": ["string"],
    "supporting_data": ["string"],
    "call_to_action": "string"
  },

  "visual_design": {
    "color_palette": ["string"],
    "layout": "string",
    "typography": "string",
    "annotations": ["string"]
  },

  "implementation": {
    "chart_config": "object",
    "data_format": "string",
    "responsive": "boolean",
    "accessibility": "object"
  },

  "validation": {
    "accuracy_check": "boolean",
    "clarity_score": "number",
    "accessibility_score": "number"
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

### Step 1: 数据分析与图表选型

- **输入**：`data_description` + `data_type`
- **动作**：
  1. 分析数据特征
  2. 选择最适合的图表类型
  3. 确定展示维度
- **输出**：`chart_selection`
- **图表选型指南**：

| 数据类型 | 推荐图表 | 备选图表 | 不推荐 |
|----------|----------|----------|--------|
| 比较 | 柱状图 | 雷达图 | 饼图 |
| 分布 | 直方图 | 箱线图 | 折线图 |
| 占比 | 饼图 | 堆叠柱状图 | 散点图 |
| 趋势 | 折线图 | 面积图 | 饼图 |
| 关系 | 散点图 | 气泡图 | 柱状图 |

**分支条件**：
- 若 `data_type=comparison` 且类别 > 5 → 使用水平柱状图
- 若 `data_type=trend` 且时间跨度长 → 使用面积图
- 若 `data_type=relationship` 且数据点 > 1000 → 使用热力图
- 若 `data_type=composition` 且部分 > 7 → 使用树状图

### Step 2: 数据故事线设计

- **输入**：`chart_selection` + `purpose`
- **动作**：
  1. 提炼核心洞察
  2. 设计故事线
  3. 确定行动号召
- **输出**：`data_story`
- **故事线结构**：

| 元素 | 目的 | 示例 |
|------|------|------|
| 标题 | 吸引注意力 | "销售增长趋势" |
| 核心洞察 | 传达主要信息 | "Q3增长30%" |
| 支撑数据 | 提供证据 | "月度数据对比" |
| 行动号召 | 引导决策 | "建议增加投入" |

**分支条件**：
- 若 `purpose=persuade` → 强调对比和差异
- 若 `purpose=inform` → 强调全面性和准确性
- 若 `purpose=explore` → 提供交互式探索选项
- 若 `purpose=present` → 简化信息，突出重点

### Step 3: 视觉设计

- **输入**：`chart_selection` + `data_story` + `audience`
- **动作**：
  1. 选择颜色方案
  2. 设计布局
  3. 添加标注和注释
- **输出**：`visual_design`
- **颜色方案**：

| 方案 | 适用场景 | 示例 |
|------|----------|------|
| 单色 | 简洁专业 | 蓝色系 |
| 互补色 | 对比强调 | 蓝橙对比 |
| 类似色 | 协调统一 | 蓝绿渐变 |
| 分类色 | 多类别区分 | 彩色系列 |

**分支条件**：
- 若受众为高管 → 简洁风格，突出关键数字
- 若受众为分析师 → 详细风格，提供数据源
- 若受众为公众 → 视觉冲击，减少专业术语
- 若媒介为印刷 → CMYK 色彩空间
- 若媒介为屏幕 → RGB 色彩空间

### Step 4: 实现与配置

- **输入**：`chart_selection` + `visual_design`
- **动作**：
  1. 生成图表配置
  2. 确定数据格式
  3. 添加响应式和无障碍支持
- **输出**：`implementation`
- **配置模板**：

```json
{
  "chart_type": "string",
  "width": "number",
  "height": "number",
  "margin": {"top": 20, "right": 20, "bottom": 20, "left": 20},
  "axes": {"x": "string", "y": "string"},
  "legend": {"position": "string"},
  "tooltip": {"enabled": true},
  "animation": {"duration": 500}
}
```

**分支条件**：
- 若 `medium=dashboard` → 添加交互功能
- 若 `medium=infographic` → 优化为静态布局
- 若 `medium=presentation` → 优化为演示尺寸
- 若 `medium=report` → 添加图表说明文字

### Step 5: 验证与优化

- **输入**：所有前序输出
- **动作**：
  1. 验证数据准确性
  2. 评估清晰度
  3. 检查无障碍性
- **输出**：`validation`
- **验证清单**：

| 检查项 | 标准 | 工具 |
|--------|------|------|
| 数据准确性 | 100% | 数据源核对 |
| 清晰度 | ≥85/100 | 用户测试 |
| 无障碍性 | WCAG 2.1 AA | 自动化工具 |

**分支条件**：
- 若清晰度 < 85 → 重新设计布局
- 若无障碍性不达标 → 添加替代文本
- 若数据有误 → 返回数据源修正

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**扭曲数据或误导观众
2. **不得**使用3D图表（除非必要）
3. **必须**标注数据来源
4. **必须**保持坐标轴完整性

### 软性约束（建议遵守）
1. 建议使用简洁的配色方案
2. 建议添加数据标签
3. 建议考虑色盲友好
4. 建议提供数据表格

### 人工兜底点
- 当数据来源不可靠时，**必须**标注不确定性
- 当需要专业设计时，**必须**建议设计帮助
- 当涉及敏感数据时，**必须**考虑隐私保护

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `VIZ_ERROR_DATA` | 数据格式错误 | 建议修正数据格式 | 🔴 |
| `VIZ_WARNING_TYPE` | 图表类型不适合 | 建议更换图表 | 🟡 |
| `VIZ_WARNING_SCALE` | 坐标轴不完整 | 建议从0开始 | 🟡 |
| `VIZ_ERROR_COLOR` | 颜色对比度不足 | 建议更换颜色 | 🔴 |
| `VIZ_WARNING_LABEL` | 标注不清晰 | 建议简化标注 | 🟡 |
| `VIZ_ERROR_ACCESS` | 无障碍性不达标 | 建议添加替代文本 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 图表配置完整

### 内容校验
- [ ] 图表类型适合数据类型
- [ ] 颜色方案清晰易读
- [ ] 数据故事线连贯
- [ ] 标注和注释完整
- [ ] 无障碍性达标

### OVP 验证信号
- 图表洞察清晰度 ≥ 85/100
- 数据解读准确率 ≥ 95%
- 观众理解度 ≥ 80%

---

## 🔄 迭代触发

| 触发条件 | 迭代动作 | 优先级 |
|----------|----------|:------:|
| 图表类型不适合 | 重新选型 | P1 |
| 清晰度 < 85 | 重新设计布局 | P1 |
| 无障碍性不达标 | 添加替代文本 | P1 |
| 数据有误 | 返回数据源修正 | P0 |
| 受众反馈不理解 | 简化信息 | P2 |

---

## 📝 自检清单

- [ ] 数据类型是否准确分类？
- [ ] 图表类型是否最适合？
- [ ] 颜色方案是否清晰？
- [ ] 标题是否简洁有力？
- [ ] 数据标签是否完整？
- [ ] 坐标轴是否完整？
- [ ] 数据来源是否标注？
- [ ] 是否考虑了色盲友好？
- [ ] 是否提供了数据表格？
- [ ] 是否验证了数据准确性？

---

## 🧪 Self-Play 测试用例

### 测试用例 1
```json
{
  "id": "test-606-01",
  "name": "销售趋势图表",
  "prompt": "将过去12个月的销售数据可视化",
  "input": {
    "data_description": "月度销售数据，包含销售额和订单量",
    "data_type": "trend",
    "audience": "销售团队",
    "purpose": "present",
    "medium": "presentation"
  },
  "assertions": [
    "chart_selection.primary_chart = 折线图或面积图",
    "data_story.headline 包含趋势描述",
    "visual_design.color_palette 包含颜色方案",
    "implementation.chart_config 包含完整配置"
  ],
  "expected_behavior": "创建清晰的销售趋势图表",
  "critic_attack": "趋势是否清晰？是否能快速看出增长/下降？"
}
```

### 测试用例 2
```json
{
  "id": "test-606-02",
  "name": "市场份额对比",
  "prompt": "制作我们与竞争对手的市场份额对比图表",
  "input": {
    "data_description": "各公司市场份额数据",
    "data_type": "comparison",
    "audience": "管理层",
    "purpose": "persuade",
    "medium": "report"
  },
  "assertions": [
    "chart_selection.primary_chart = 柱状图",
    "data_story.key_insights 包含对比洞察",
    "visual_design.annotations 包含标注",
    "data_story.call_to_action 明确"
  ],
  "expected_behavior": "创建有说服力的市场份额对比",
  "critic_attack": "对比是否清晰？是否能支持决策？"
}
```

### 测试用例 3
```json
{
  "id": "test-606-03",
  "name": "预算分配图表",
  "prompt": "将公司预算分配可视化",
  "input": {
    "data_description": "各部门预算分配数据",
    "data_type": "composition",
    "audience": "全体员工",
    "purpose": "inform",
    "medium": "infographic"
  },
  "assertions": [
    "chart_selection.primary_chart = 饼图或树状图",
    "data_story.headline 包含总预算",
    "visual_design.color_palette 包含分类色",
    "implementation.responsive = true"
  ],
  "expected_behavior": "创建清晰的预算分配图表",
  "critic_attack": "占比是否清晰？是否能快速理解分配？"
}
```

### 测试用例 4
```json
{
  "id": "test-606-04",
  "name": "用户行为散点图",
  "prompt": "分析用户使用时长与活跃度的关系",
  "input": {
    "data_description": "用户使用时长和活跃度数据",
    "data_type": "relationship",
    "audience": "产品经理",
    "purpose": "explore",
    "medium": "dashboard"
  },
  "assertions": [
    "chart_selection.primary_chart = 散点图",
    "data_story.key_insights 包含相关性描述",
    "implementation.chart_config.tooltip.enabled = true",
    "implementation.chart_config.interaction 已定义"
  ],
  "expected_behavior": "创建可探索的用户行为分析",
  "critic_attack": "关系是否清晰？是否支持深入探索？"
}
```

### 测试用例 5
```json
{
  "id": "test-606-05",
  "name": "客户满意度分布",
  "prompt": "展示客户满意度评分的分布情况",
  "input": {
    "data_description": "客户满意度评分数据",
    "data_type": "distribution",
    "audience": "客服团队",
    "purpose": "inform",
    "medium": "report"
  },
  "assertions": [
    "chart_selection.primary_chart = 直方图或箱线图",
    "data_story.headline 包含分布特征",
    "visual_design.annotations 包含均值和中位数",
    "validation.accuracy_check = true"
  ],
  "expected_behavior": "创建清晰的满意度分布图",
  "critic_attack": "分布是否清晰？是否能识别问题区域？"
}
```

---

## 🔗 关联文档

- [[创意写作]] — 数据的故事化呈现
- [[文案写作]] — 数据图表的文字说明
- [[创意发散]] — 可视化创意的发散思维
- [[说服力写作]] — 数据驱动的说服力
- [[内容改编]] — 图表的多形态改编

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：图表选型 + 数据故事 + 视觉设计 + Self-Play |

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

## 🔄 IF/THEN 决策分支

- IF 创意方向不明确（用户仅说"帮我拍"）→ THEN 先确认拍摄主体/场景/风格偏好，再给出方案
- IF 场景光线不足（ISO > 3200 或快门 < 1/60）→ THEN 推荐补光方案或调整拍摄时间
- IF 预算有限（设备/场地受限）→ THEN 给出低成本替代方案，不推荐超出预算的设备
- ELSE（条件充足）→ THEN 输出完整拍摄方案 + 参数建议


## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常创作 | 明确主题+场景 | 完整方案+参数 | 可执行 + 参数合理 |
| 2 | 方向模糊 | 仅说"帮我拍" | 确认需求清单 | 不盲目给方案 |
| 3 | 光线不足 | 夜间/室内弱光 | 补光方案 | 实用 + 成本可控 |
| 4 | 预算受限 | 无专业设备 | 手机拍摄方案 | 效果可接受 |
| 5 | 极端天气 | 雨天/大风 | 室内替代方案 | 安全优先 |

