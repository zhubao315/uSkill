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
    "prompt": "安排明天的工作，有5个任务需要完成",
    "context": "available_hours=8, tasks=[编程、邮件、会议、写作、学习]",
    "assertions": [
      "schedule 包含 所有任务",
      "energy_alignment.high_energy_tasks 包含 编程和写作",
      "buffer_analysis.buffer_percentage >= 10"
    ],
    "expected_behavior": "合理安排所有任务，匹配精力水平",
    "critic_attack": "是否为所有任务都安排了足够时间？"
  },
  {
    "id": "test-002",
    "name": "会议密集日",
    "prompt": "明天有4个会议，还需要完成2个任务",
    "context": "available_hours=8, constraints=[4个会议]",
    "assertions": [
      "schedule 包含 所有会议和任务",
      "buffer_analysis 包含 会议间缓冲",
      "optimization_suggestions 包含 建议"
    ],
    "expected_behavior": "在会议间隙安排可执行任务",
    "critic_attack": "是否过度压缩了任务时间？"
  },
  {
    "id": "test-003",
    "name": "精力低谷日",
    "prompt": "今天状态不好，精力很低",
    "context": "available_hours=8, energy_level=low",
    "assertions": [
      "energy_alignment.low_energy_tasks 安排在主要时段",
      "schedule 包含 更多休息时间",
      "optimization_suggestions 包含 降低难度建议"
    ],
    "expected_behavior": "根据低精力状态调整安排",
    "critic_attack": "是否正确识别了精力状态并调整？"
  }
]
```

---

## 🔗 关联文档

- [[深度工作四步法——专注力炼金术]] — 深度专注方法
- [[GTD执行]] — 任务管理方法
- [[柳比歇夫时间统计]] — 时间统计方法
- [[uSkill-日程优化-v1]] — 日程优化
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：任务分类 + 精力匹配 + 时间块设计 + Self-Play |

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


**相关概念**：[[注意力的有限性]] · [[生产力系统]]

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
