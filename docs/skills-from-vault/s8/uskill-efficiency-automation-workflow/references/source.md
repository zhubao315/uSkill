
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
- [ ] 自动化方案覆盖所有重复步骤
- [ ] ROI 分析合理（自动化收益 > 搭建成本）
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 回退方案已设计

### 合规校验
- [ ] 未硬编码敏感信息
- [ ] 权限需求已列出
- [ ] 人工兜底点已标注

### OVP 验证信号
- 自动化覆盖率 ≥ 80%
- 人工干预次数相比手动下降 ≥ 50%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "日报自动生成",
    "prompt": "我每天需要从 3 个系统导出数据，合并成日报发给老板，太烦了",
    "context": "frequency=daily, current_steps=['导出A系统数据', '导出B系统数据', '导出C系统数据', 'Excel合并', '邮件发送']",
    "assertions": [
      "automation_plan.workflow 覆盖全部 5 个步骤",
      "tools 列表包含数据导出和邮件发送工具",
      "monitoring.success_criteria 包含数据完整性检查"
    ],
    "expected_behavior": "设计完整的日报自动化方案，包含数据采集、合并、发送全流程",
    "critic_attack": "方案是否考虑了数据源变更的情况？降级策略是否可行？"
  },
  {
    "id": "test-002",
    "name": "文件批量重命名",
    "prompt": "我有 500 张照片需要按日期重命名，手动改太慢了",
    "context": "frequency=adhoc, current_steps=['查看文件日期', '手动重命名']",
    "assertions": [
      "automation_plan.approach 包含批量处理方案",
      "implementation.testing_approach 包含预览模式",
      "monitoring 包含回滚方案"
    ],
    "expected_behavior": "生成安全的批量重命名脚本，支持预览和回滚",
    "critic_attack": "是否考虑了重命名冲突？是否支持预览？"
  },
  {
    "id": "test-003",
    "name": "低价值任务识别",
    "prompt": "我每周花 10 分钟整理会议笔记，要不要自动化？",
    "context": "frequency=weekly, current_steps=['打开录音', '转文字', '整理格式']",
    "assertions": [
      "analysis 标记为低自动化价值或提供替代方案",
      "如果建议自动化，ROI 分析显示收益合理",
      "如果建议不自动化，提供手动优化建议"
    ],
    "expected_behavior": "根据 ROI 判断是否值得自动化，给出合理建议",
    "critic_attack": "ROI 计算是否准确？是否忽略了隐性成本？"
  },
  {
    "id": "test-004",
    "name": "跨系统数据同步",
    "prompt": "CRM 和 ERP 的客户数据经常不一致，需要每周手动对账",
    "context": "frequency=weekly, current_steps=['导出CRM数据', '导出ERP数据', 'Excel VLOOKUP', '标记差异', '人工修正']",
    "assertions": [
      "automation_plan 包含数据比对逻辑",
      "monitoring.alert_conditions 包含数据不一致告警",
      "implementation 包含权限和 API 配置要求"
    ],
    "expected_behavior": "设计自动对账方案，包含差异检测和告警",
    "critic_attack": "方案是否处理了数据冲突的解决规则？"
  },
  {
    "id": "test-005",
    "name": "过度工程化防御",
    "prompt": "帮我设计一个系统，每天自动检查 5 个网站的内容更新",
    "context": "frequency=daily, current_steps=['逐个访问网站', '肉眼对比变化']",
    "assertions": [
      "automation_plan.approach 选择简单方案而非复杂框架",
      "tools 不超过 3 个核心依赖",
      "implementation.setup_steps 不超过 10 步"
    ],
    "expected_behavior": "推荐轻量级方案（如 cron + curl + diff），避免过度工程化",
    "critic_attack": "是否过度设计？最简方案是什么？"
  },
  {
    "id": "test-006",
    "name": "合规场景识别",
    "prompt": "我想自动化发票审批流程",
    "context": "frequency=daily, current_steps=['收到发票', '核实金额', '领导签字', '财务入账']",
    "assertions": [
      "monitoring 包含人工审批环节",
      "automation_plan.workflow 标注 manual 步骤",
      "硬性约束触发：涉及资金需保留人工审批"
    ],
    "expected_behavior": "识别合规要求，保留人工审批环节，自动化其他步骤",
    "critic_attack": "是否遗漏了审计追踪要求？"
  },
  {
    "id": "test-007",
    "name": "失败恢复设计",
    "prompt": "自动化脚本执行到一半失败了怎么办？",
    "context": "frequency=daily",
    "assertions": [
      "monitoring.fallback_strategy 明确",
      "implementation 包含断点续传或重试机制",
      "异常处理覆盖执行中断场景"
    ],
    "expected_behavior": "设计包含重试、回滚、断点续传的容错机制",
    "critic_attack": "恢复机制是否覆盖了部分成功的场景？"
  },
  {
    "id": "test-008",
    "name": "团队协作场景",
    "prompt": "我们团队 5 个人都需要用这个自动化工具",
    "context": "frequency=weekly, tools_available=['Python', 'Airflow']",
    "assertions": [
      "documentation 包含多人使用说明",
      "implementation 包含权限管理方案",
      "monitoring 包含多用户监控"
    ],
    "expected_behavior": "设计支持多人协作的自动化方案，含权限和文档",
    "critic_attack": "是否考虑了不同用户的技术水平差异？"
  },
  {
    "id": "test-009",
    "name": "工具选型决策",
    "prompt": "Python 脚本、n8n、Zapier 选哪个？",
    "context": "frequency=daily, tools_available=['Python', 'n8n', 'Zapier']",
    "assertions": [
      "方案包含工具对比分析",
      "选择理由基于具体场景而非偏好",
      "提供了降级方案"
    ],
    "expected_behavior": "根据场景特点推荐最合适的工具，给出选择理由",
    "critic_attack": "是否考虑了维护成本和团队技术栈？"
  },
  {
    "id": "test-010",
    "name": "边界任务处理",
    "prompt": "帮我自动化写周报",
    "context": "frequency=weekly",
    "assertions": [
      "analysis 标记为部分自动化",
      "方案保留人工编辑和审核环节",
      "不尝试完全替代创意性工作"
    ],
    "expected_behavior": "识别创意性任务的自动化边界，提供辅助而非替代方案",
    "critic_attack": "是否过度自动化了需要人工判断的任务？"
  }
]
```

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🔗 关联文档

- [[GTD执行]] — 任务管理方法论
- [[时间块规划]] — 时间分配策略
- [[深度工作四步法——专注力炼金术]] — 专注力保护
- [[数字断舍离]] — 信息简化
- [[SOP-23-效率分析]] — 效率诊断工具

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：任务识别→方案设计→实施→监控→文档 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

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
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

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


**相关概念**：[[编程自动化]] · [[信息管理系统]]

---



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


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
