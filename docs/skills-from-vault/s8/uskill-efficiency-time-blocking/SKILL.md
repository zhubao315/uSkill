---
name: uskill-efficiency-time-blocking
description: "让时间块规划变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-time-blocking.md"
  original_id: "SKL-6914"
  version: "3.0.0"
  trust: untrusted
---

# 时间块规划

⚙️ AI-Co 运行配置块
触发场景: 用户说'时间块'、'日程安排'、'时间规划'、'番茄钟'
复用率预估: 高
一键调用: 任务分析→时间估算→时间块分配→优先级排序
输入Schema: tasks(array), available_hours(number, default: 8), energy_profile(object), constraints(array)
输出Schema: schedule(time_slot, duration, task, task_type, energy_level), energy_alignment, buffer_analysis
AI可执行度: 100%

description: |
  当用户需要按精力水平分配任务类型、安排时间块、优化日程、平衡深度与浅层工作时使用此 Skill。
  触发词包括：'时间块'、'日程安排'、'精力管理'、'时间规划'、'日程优化'、
  '时间分配'、'精力匹配'。当用户讨论时间管理、工作效率、日程安排时，
  即使未直接说"时间块规划"，也应使用此 Skill。
  不适用于简单的待办清单（使用 GTD 执行）。遇到复杂日程安排时优先使用。

---

# uSkill-203: 时间块规划

## 🎯 目标

> 将时间划分为专注的块，每块专注于特定任务类型，匹配精力水平，最大化时间利用效率。

**核心价值**：从"做什么"升级到"什么时候做"，将任务与精力水平匹配。

**适用场景**：
- 日常工作安排
- 项目时间规划
- 学习计划制定
- 创作时间管理
- 个人时间优化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `tasks` | `array` | ✅ | — | 待安排的任务列表 |
| `available_hours` | `number` | ❌ | `8` | 可用工作小时数 |
| `energy_profile` | `object` | ❌ | — | 个人精力曲线 |
| `constraints` | `array` | ❌ | `[]` | 时间约束（会议、约会等） |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话时间块规划建议",
  "time_block_id": "TB-YYYY-MMDD-NNN",

  "schedule": [
    {
      "time_slot": "string",
      "duration": "number — 分钟",
      "task": "string",
      "task_type": "deep|shallow|admin|break",
      "energy_level": "high|medium|low",
      "interruption_allowed": "boolean"
    }
  ],

  "energy_alignment": {
    "high_energy_tasks": ["string"],
    "medium_energy_tasks": ["string"],
    "low_energy_tasks": ["string"],
    "recovery_periods": ["string"]
  },

  "buffer_analysis": {
    "total_buffer_time": "number — 分钟",
    "buffer_percentage": "number — 占比",
    "adequacy": "sufficient|insufficient|excessive"
  },

  "optimization_suggestions": [
    {
      "suggestion": "string",
      "expected_impact": "string",
      "implementation": "string"
    }
  ],

  "monitoring_metrics": {
    "planned_vs_actual": "number — 偏差百分比",
    "energy_match_rate": "number — 匹配度",
    "completion_rate": "number — 完成率"
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

### Step 1: 任务分类

- **输入**：`tasks`
- **动作**：
  1. 按认知需求分类任务
  2. 评估每项任务所需精力
  3. 估计每项任务时长
- **输出**：分类后的任务列表
- **任务类型分类**：

| 类型 | 特征 | 所需精力 |
|------|------|:--------:|
| 深度工作 | 需要高度专注 | 高 |
| 浅层工作 | 常规性任务 | 中 |
| 行政工作 | 管理性任务 | 低 |
| 休息恢复 | 恢复精力 | - |

### Step 2: 精力曲线分析

- **输入**：`energy_profile`
- **动作**：
  1. 识别个人精力高峰时段
  2. 识别精力低谷时段
  3. 匹配任务与精力
- **输出**：`energy_alignment`
- **典型精力曲线**：

| 时段 | 精力水平 | 适合任务 |
|------|:--------:|----------|
| 早晨（9-12） | 高 | 深度工作 |
| 午后（13-15） | 中 | 浅层工作 |
| 下午（15-17） | 中-高 | 协作/会议 |
| 傍晚（17-19） | 低 | 行政工作 |

### Step 3: 时间块设计

- **输入**：`energy_alignment` + `constraints`
- **动作**：
  1. 安排高精力任务到高峰时段
  2. 插入休息恢复时间
  3. 添加缓冲时间
- **输出**：`schedule`
- **时间块原则**：

| 原则 | 描述 |
|------|------|
| 精力匹配 | 高精力→深度工作 |
| 批处理 | 相似任务集中处理 |
| 缓冲 | 任务间留 10-15 分钟缓冲 |
| 恢复 | 每 90 分钟休息 15 分钟 |

### Step 4: 缓冲分析

- **输入**：`schedule`
- **动作**：
  1. 计算总缓冲时间
  2. 评估缓冲充足性
  3. 调整时间块
- **输出**：`buffer_analysis`
- **缓冲建议**：
  - 总缓冲时间 ≥ 10%
  - 高风险任务后增加缓冲
  - 会议后留恢复时间

### Step 5: 优化建议

- **输入**：所有前序输出
- **动作**：
  1. 识别优化机会
  2. 生成具体建议
  3. 评估预期效果
- **输出**：`optimization_suggestions`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**安排超过 4 小时的连续深度工作
2. **不得**忽视休息和恢复
3. **必须**考虑个人精力模式

### 软性约束（建议遵守）
1. 建议每天安排 2-3 个深度工作块
2. 建议在精力高峰期安排最难的任务
3. 建议每周回顾时间块执行情况

### 人工兜底点
- 当连续 3 天无法完成时间块计划时，**必须**调整策略
- 当出现倦怠迹象时，**必须**建议增加休息

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `TB_WARNING_NO_BUFFER` | 缓冲时间 < 5% | 建议增加缓冲 | 🟡 |
| `TB_WARNING_MISMATCH` | 精力与任务不匹配 | 建议调整安排 | 🟡 |
| `TB_ERROR_OVERLOADED` | 任务超过可用时间 | 建议优先级排序 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 任务已分类
- [ ] 时间块已安排
- [ ] 缓冲时间充足
- [ ] 精力匹配合理

### OVP 验证信号
- 时间块执行率 ≥ 80%
- 精力匹配度 ≥ 75%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "典型工作日安排",
    "prompt": "安排明天的工作，

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
