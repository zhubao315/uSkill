
description: |
  当用户需要清理数字文件、整理邮件、管理订阅、减少数字噪音时使用此 Skill。
  触发词包括：'数字断舍离'、'文件清理'、'邮件整理'、'订阅管理'、'数字极简'。
  当用户讨论效率、整理、减负时，
  即使未直接说"数字断舍离"，也应使用此 Skill。
  不适用于知识库管理（使用第二大脑 Skill）。遇到数字物品清理时优先使用。

---

# uSkill-204: 数字断舍离

## 🎯 目标

> 清理数字物品，减少信息噪音，提升数字生活效率。

**核心价值**：数字物品也会占据心智空间。清理数字物品能提升专注力。

**适用场景**：
- 文件清理
- 邮件整理
- 订阅管理
- 应用清理
- 通知优化

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `cleanup_scope` | `enum` | ❌ | `all` | `files` / `email` / `subscriptions` / `apps` / `all` |
| `current_status` | `object` | ❌ | — | 当前数字物品状况 |
| `goals` | `array` | ❌ | `[]` | 清理目标 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话清理建议",
  "detox_id": "DD-YYYY-MMDD-NNN",

  "assessment": {
    "total_files": "number",
    "total_emails": "number",
    "active_subscriptions": "number",
    "installed_apps": "number",
    "notification_sources": "number",
    "digital_clutter_score": "number — 0-100"
  },

  "cleanup_plan": {
    "files": {
      "strategy": "string",
      "categories": [
        {
          "category": "string",
          "action": "delete|archive|organize",
          "criteria": "string",
          "estimated_savings": "string"
        }
      ]
    },
    "email": {
      "strategy": "string",
      "actions": ["string"],
      "automation_rules": ["string"]
    },
    "subscriptions": {
      "strategy": "string",
      "keep": ["string"],
      "cancel": ["string"],
      "downgrade": ["string"]
    },
    "apps": {
      "strategy": "string",
      "keep": ["string"],
      "uninstall": ["string"]
    }
  },

  "automation_setup": {
    "file_management": ["string"],
    "email_rules": ["string"],
    "notification_optimization": ["string"]
  },

  "maintenance_routine": {
    "daily": ["string"],
    "weekly": ["string"],
    "monthly": ["string"],
    "quarterly": ["string"]
  },

  "benefits_tracking": {
    "storage_saved": "string",
    "time_saved_weekly": "string",
    "stress_reduction": "string"
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

### Step 1: 数字物品评估

- **输入**：`current_status`
- **动作**：
  1. 统计各类数字物品数量
  2. 评估数字杂乱程度
  3. 识别高优先级清理领域
- **输出**：`assessment`

### Step 2: 文件清理

- **输入**：`assessment.total_files`
- **动作**：
  1. 设计清理策略
  2. 制定分类标准
  3. 执行清理
- **输出**：`cleanup_plan.files`
- **文件清理原则**：

| 原则 | 描述 |
|------|------|
| 一年规则 | 超过一年未使用的文件归档 |
| 重复文件 | 检测并删除重复文件 |
| 临时文件 | 清理临时和缓存文件 |
| 大文件 | 识别并处理大文件 |

### Step 3: 邮件整理

- **输入**：`assessment.total_emails`
- **动作**：
  1. 设计清理策略
  2. 创建过滤规则
  3. 设置自动归档
- **输出**：`cleanup_plan.email`

### Step 4: 订阅管理

- **输入**：`assessment.active_subscriptions`
- **动作**：
  1. 列出所有订阅
  2. 评估使用频率
  3. 决定保留/取消/降级
- **输出**：`cleanup_plan.subscriptions`

### Step 5: 应用清理

- **输入**：`assessment.installed_apps`
- **动作**：
  1. 列出所有应用
  2. 评估使用频率
  3. 卸载不需要的应用
- **输出**：`cleanup_plan.apps`

### Step 6: 自动化设置

- **输入**：`cleanup_plan`
- **动作**：
  1. 设置文件管理自动化
  2. 创建邮件规则
  3. 优化通知设置
- **输出**：`automation_setup`

### Step 7: 维护例程

- **输入**：所有前序输出
- **动作**：
  1. 设计日常维护
  2. 安排周度整理
  3. 规划月度回顾
- **输出**：`maintenance_routine`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**删除重要数据
2. **不得**忽视数据备份
3. **必须**考虑数据安全

### 软性约束（建议遵守）
1. 建议先备份再清理
2. 建议循序渐进
3. 建议建立新习惯

### 人工兜底点
- 当涉及重要数据时，**必须**建议专业帮助
- 当清理困难时，**必须**建议分阶段进行

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `DD_WARNING_LARGE_SCOPE` | 范围过大 | 建议缩小范围 | 🟡 |
| `DD_WARNING_DATA_RISK` | 数据风险 | 建议备份 | 🟡 |
| `DD_ERROR_IMPORTANT_DATA` | 重要数据 | 建议保留 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 评估已完成
- [ ] 清理计划已制定
- [ ] 自动化已设置
- [ ] 维护例程已设计

### OVP 验证信号
- 数字物品减少 ≥ 30%
- 检索时间减少 ≥ 20%

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "文件清理",
    "prompt": "我的电脑文件太多，需要清理",
    "context": "cleanup_scope=files",
    "assertions": [
      "assessment.total_files 已统计",
      "cleanup_plan.files 包含 分类标准",
      "automation_setup.file_management 已设置"
    ],
    "expected_behavior": "设计文件清理方案",
    "critic_attack": "是否考虑了重要文件的保护？"
  },
  {
    "id": "test-002",
    "name": "邮件整理",
    "prompt": "我的邮箱有1万封未读邮件",
    "context": "cleanup_scope=email",
    "assertions": [
      "assessment.total_emails 已统计",
      "cleanup_plan.email 包含 过滤规则",
      "cleanup_plan.email 包含 自动归档"
    ],
    "expected_behavior": "设计邮件清理方案",
    "critic_attack": "是否考虑了重要邮件的保护？"
  },
  {
    "id": "test-003",
    "name": "订阅管理",
    "prompt": "我订阅了很多服务，但很少使用",
    "context": "cleanup_scope=subscriptions",
    "assertions": [
      "cleanup_plan.subscriptions.keep 已列出",
      "cleanup_plan.subscriptions.cancel 已列出",
      "maintenance_routine.monthly 包含 订阅审查"
    ],
    "expected_behavior": "设计订阅管理方案",
    "critic_attack": "是否遗漏了重要订阅？"
  }
]
```

---

## 🔗 关联文档

- [[第二大脑 PKM 管理]] — 知识管理
- [[柳比歇夫时间统计]] — 时间管理
- [[深度工作四步法——专注力炼金术]] — 专注力提升
- [[GTD执行]] — 任务管理
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：评估 + 清理计划 + 自动化 + Self-Play |

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


**相关概念**：[[注意力的有限性]] · [[正念与注意力]]

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
