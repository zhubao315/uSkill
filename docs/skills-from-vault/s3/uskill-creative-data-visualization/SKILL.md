---
name: uskill-creative-data-visualization
description: "让数据可视化变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-data-visualization.md"
  original_id: "SKL-5606"
  version: "3.0.0"
  trust: untrusted
---

# 数据可视化

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
- 若数

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
