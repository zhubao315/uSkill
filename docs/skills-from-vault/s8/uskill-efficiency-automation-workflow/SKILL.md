---
name: uskill-efficiency-automation-workflow
description: "让自动化工作流变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-automation-workflow.md"
  original_id: "SKL-5205"
  version: "3.0.0"
  trust: untrusted
---

# 自动化工作流

description: |
  当用户需要识别重复任务并设计自动化方案、搭建工具链时使用此 Skill。
  触发词包括：'自动化'、'工作流'、'重复任务'、'工具链'、'效率提升'、'脚本'、'批处理'。
  当用户抱怨"每天都在做同样的事"、"这个流程太繁琐"、"有没有办法自动处理"时，
  即使未直接说"自动化"，也应使用此 Skill。
  不适用于一次性任务或需要复杂 AI 判断的决策场景。遇到重复性流程优化时优先使用。

---

# uSkill-205: 自动化工作流

## 🎯 目标

> 识别可自动化的重复任务，设计合理的自动化方案，搭建可维护的工具链。

**核心价值**：将重复性工作从人力转向机器，释放创造力用于高价值任务。

**适用场景**：
- 日常重复性数据处理
- 文件批量转换与整理
- 定期报告生成
- 跨系统数据同步
- 通知与提醒自动化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task_description` | `string` | ✅ | — | 需要自动化的任务描述 |
| `frequency` | `enum` | ❌ | `daily` | 任务频率：`daily` / `weekly` / `monthly` / `adhoc` |
| `current_steps` | `array` | ❌ | — | 当前手动执行步骤列表 |
| `tools_available` | `array` | ❌ | `[]` | 已有可用工具列表 |

**输入约束**：
- `task_description` 必须明确描述输入、处理、输出
- `current_steps` 应包含每个步骤的耗时估计
- 自动化收益应大于搭建成本

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结自动化方案",
  "auto_id": "AW-YYYY-MMDD-NNN",

  "analysis": {
    "task_name": "string",
    "current_frequency": "string",
    "manual_time_per_execution": "string",
    "estimated_automation_time": "string",
    "roi_months": "number"
  },

  "automation_plan": {
    "approach": "string",
    "tools": [
      {
        "name": "string",
        "purpose": "string",
        "setup_effort": "low|medium|high"
      }
    ],
    "workflow": [
      {
        "step": "number",
        "action": "string",
        "automation_level": "full|partial|manual"
      }
    ],
    "schedule": "string"
  },

  "implementation": {
    "prerequisites": ["string"],
    "setup_steps": ["string"],
    "configuration": "string",
    "testing_approach": "string"
  },

  "monitoring": {
    "success_criteria": ["string"],
    "alert_conditions": ["string"],
    "fallback_strategy": "string"
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

### Step 1: 任务识别与分析

- **输入**：`task_description`, `current_steps`
- **动作**：
  1. 分析任务的重复性特征
  2. 识别瓶颈和耗时环节
  3. 评估自动化可行性
- **输出**：`analysis`
- **分支条件**：
  - IF 任务步骤 < 3 → 标记为"低自动化价值"，建议手动优化
  - IF 单次执行 < 5 分钟 → 评估周总耗时是否值得自动化
  - IF 涉及复杂判断 → 标记为"部分自动化"，保留人工决策点
  - ELSE → 进入完整自动化方案设计
- **检查点**：✅ 应验证分析结论与用户预期一致

### Step 2: 方案设计

- **输入**：`analysis`
- **动作**：
  1. 选择自动化工具和方法
  2. 设计工作流步骤
  3. 定义触发条件和调度计划
- **输出**：`automation_plan`
- **分支条件**：
  - IF 已有工具可覆盖 → 优先使用现有工具，减少开发
  - IF 需要自定义脚本 → 选择合适语言，遵循团队规范
  - IF 涉及外部 API → 评估 API 稳定性和限额
  - ELSE → 使用通用自动化平台（如 n8n、Zapier）
- **检查点**：✅ 应验证方案覆盖所有步骤且无遗漏

### Step 3: 实施规划

- **输入**：`automation_plan`
- **动作**：
  1. 列出前置条件
  2. 编写实施步骤
  3. 定义测试方案
- **输出**：`implementation`
- **分支条件**：
  - IF 需要权限申请 → 标记为阻塞项，提供申请模板
  - IF 需要数据迁移 → 设计回滚方案
  - IF 依赖第三方服务 → 准备降级方案
  - ELSE → 直接进入实施
- **检查点**：✅ 应验证实施步骤可执行且顺序正确

### Step 4: 监控与告警设计

- **输入**：`implementation`
- **动作**：
  1. 定义成功标准
  2. 设计告警条件
  3. 制定降级策略
- **输出**：`monitoring`
- **检查点**：✅ 应验证告警覆盖关键失败场景

### Step 5: 文档与交接

- **输入**：`monitoring`
- **动作**：
  1. 编写操作文档
  2. 创建故障排查手册
  3. 安排知识转移
- **输出**：完整自动化文档包
- **分支条件**：
  - IF 团队多人使用 → 增加培训材料
  - IF 流程可能变更 → 设计参数化配置
  - ELSE → 标准文档即可
- **检查点**：✅ 应验证文档完整性和可读性

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**自动化未经确认的业务流程
2. **不得**在自动化中硬编码敏感信息（密码、Token）
3. **必须**为每个自动化流程设计回退方案
4. **必须**在自动化前手动验证至少 3 次流程正确性

### 软性约束（建议遵守）
1. 优先使用团队已有工具栈
2. 自动化脚本应有版本控制
3. 复杂自动化应有日志记录
4. 定期审查自动化效果

### 人工兜底点
- 当自动化连续失败 3 次时，**必须**暂停并人工介入
- 当业务规则变更时，**必须**人工确认后再更新自动化
- 当涉及资金或法律合规时，**必须**保留人工审批环节

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `AW_ERROR_TOOL_UNAVAILABLE` | 所选工具不可用或未安装 | 切换备选工具或手动执行 | 🔴 |
| `AW_ERROR_PERMISSION_DENIED` | 缺少必要权限 | 提示申请权限，暂停执行 | 🔴 |
| `AW_ERROR_DATA_FORMAT` | 输入数据格式不匹配 | 自动转换格式或报错提示 | 🟡 |
| `AW_ERROR_RATE_LIMIT` | 触发 API 限流 | 指数退避重试，最多 3 次 | 🟡 |
| `AW_WARNING_INCOMPLETE` | 部分步骤无法自动化 | 生成混合方案，标注手动步骤 | 🟢 |

### 降级策略
- 当完全自动化不可行时，生成"半自动化"方案，保留人工步骤
- 当工具链故障时，输出手动操作清单作为应急方案

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 工具依赖列表完整

### 内容校验
- [ ] 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
