
description: |
  当用户需要将规则变更（AGENTS.md 硬约束、标签体系、uSkill 模块 Schema、循环工程调度契约等）
  同步至所有相关 Agent 与循环工程时使用此 Skill。
  触发词包括：'规则分发'、'规则同步'、'更新规则'、'规则漂移'、'一致性校验'、'批量下发'。
  即使用户没有说"规则"，只要意图涉及将某条规范推广到多个智能体/循环并保证一致，也应触发。
  不适用：单次性的个人笔记修改、与系统规则无关的纯内容创作。

---

# 📡 uSkill-7102: 规则分发同步（Gen3）

## 🎯 目标

> 将规则变更零误差地同步至所有相关 Agent 与 7 套循环工程（1每日+6专项），
> 生成含回滚方案的同步通知，并持续检测规则漂移，确保全系统规则一致性。

**适用场景**：修改 [[AGENTS]] 硬约束、标签体系迁移、uSkill Gen3 Schema 升级、
[[uSkill-agent-循环工程统一调度入口]] 调度契约变更后的全量下发。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `rule_change` | `object` | ✅ | 规则变更内容（路径/字段/旧值/新值/生效时间） |
| `affected_scope` | `array` | ❌ | 受影响范围（agent/loop/file），缺省则自动推导 |
| `dry_run` | `bool` | ❌ | 仅模拟分发不实际写入，默认 false |

---

## 📤 输出

```json
{
  "affected_targets": [
    {"target": "string", "type": "agent|loop|file", "sync_status": "synced|pending|failed|skipped"}
  ],
  "drift_detected": [{"target": "string", "expected": "string", "actual": "string"}],
  "rollback_plan": {"snapshot_ref": "string", "steps": ["string"]},
  "pending_confirmations": ["string"]
}
```

---

## 🔄 执行流程

```
1. [变更解析] → 提取规则变更内容
    → 变更类型：新增 / 修改 / 删除
    → 影响维度：硬约束 / 标签 / Schema / 调度契约
    → IF 变更涉及 AGENTS.md 硬约束 #1-#8：强制要求 dry_run 预演 + 人工签字
    → ELSE：进入自动识别分支

2. [目标识别] → 基于规则依赖图识别受影响目标
    → 遍历 7 套循环工程 + 全部 uSkill Agent 的依赖清单
    → IF Agent 声明依赖该规则：加入 affected_targets
    → IF 仅间接引用（如只是 wikilink）：标 skipped 并备注
    → ELSE：跳过

3. [漂移预检] → 分发前先扫描当前各目标实际值
    → IF 已存在与目标值不一致（旧漂移）：先记录 drift_detected 再覆盖
    → ELSE：直接写入

4. [通知生成] → 为每个目标生成同步通知
    → 通知内容：变更详情 + 生效时间 + rollback_plan
    → IF dry_run=true：输出模拟报告，不写入任何文件
    → ELSE：写入并标记 synced / pending

5. [状态闭环] → 确认全部接收
    → IF 全部 synced：输出"同步完成" + 漂移已清零
    → IF 存在 failed/pending：标注未同步目标 + 重试（最多3次）
    → IF 重试仍失败：升级人工，附 drift_detected 列表
```

---

## 📝 Prompt 模板

### 标准分发 Prompt

```
你是规则分发 Agent。请将以下规则变更同步到所有相关目标。

【规则变更】{rule_change}
【受影响范围】{affected_scope}
【模式】{dry_run ? "模拟" : "正式"}

【分发规则】
1. 解析变更类型与影响维度
2. 基于依赖图识别所有受影响 Agent / 循环 / 文件
3. 分发前先做漂移预检，记录已有不一致
4. 生成含回滚方案的同步通知并写入
5. 确认状态，失败重试，超次升级人工

【输出格式】
严格按标准 JSON 输出，包含 affected_targets、drift_detected、
rollback_plan、pending_confirmations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| Agent / 循环离线 | 标注 pending + 重试 | 等待上线后补同步 |
| 规则冲突（新旧互斥） | 标注冲突 + 人工确认 | 暂不生效，保留旧规 |
| 涉及 AGENTS 硬约束 | 强制 dry_run + 人工签字 | 不自动写入 |
| 批量变更(>20目标) | 分批处理 | 每批完成后校验再下一批 |
| 写入失败(权限/锁) | 记录失败目标 | 回滚已写部分，整体重放 |

---

## ✅ 质量自检

- [ ] `rule_change` 含旧值与新值，可审计
- [ ] 每个 affected_target 都有明确的 sync_status
- [ ] 分发前已完成漂移预检并写出 drift_detected
- [ ] rollback_plan 含可执行的 snapshot_ref 与步骤
- [ ] 涉及硬约束的变更已走 dry_run + 人工签字
- [ ] 无目标被误伤（skipped 已正确标注）

---

## 💡 使用示例

### 示例 1：标签体系迁移分发

**输入**：
```json
{
  "rule_change": {"rule": "标签体系", "field": "维度", "old": "维度/技能", "new": "维度/学习", "effective": "2026-07-08T08:00"},
  "affected_scope": ["uSkill-agent-*", "循环工程统一调度入口"]
}
```

**输出**：
```json
{
  "affected_targets": [
    {"target": "uSkill-agent-社交资本", "type": "agent", "sync_status": "synced"},
    {"target": "循环工程统一调度入口", "type": "loop", "sync_status": "synced"}
  ],
  "drift_detected": [],
  "rollback_plan": {"snapshot_ref": "git:HEAD~1", "steps": ["git checkout HEAD~1 -- 02-BUILD/22-uSkill/", "重新触发分发"]},
  "pending_confirmations": []
}
```

### 示例 2：硬约束变更（边界）

**输入**：
```json
{
  "rule_change": {"rule": "AGENTS硬约束#3", "field": "全局搜索替换", "old": "允许", "new": "禁止"},
  "dry_run": true
}
```

**输出**：
```json
{
  "affected_targets": [{"target": "全部 Agent", "type": "agent", "sync_status": "skipped"}],
  "drift_detected": [],
  "rollback_plan": {"snapshot_ref": "n/a", "steps": ["本变更为模拟，未写入"]},
  "pending_confirmations": ["需人工签字后方可正式分发"]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常分发 | 全部 synced |
| 2 | Agent 离线 | pending + 重试 |
| 3 | 规则冲突 | 标注冲突 + 不生效 |
| 4 | 无影响目标 | 空列表 / skipped |
| 5 | 硬约束变更 | 强制 dry_run + 签字 |
| 6 | 批量变更 | 分批校验 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 涉及 AGENTS 硬约束 #1-#8 的变更**必须** dry_run + 人工签字，禁止自动写入
4. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先复用既有的依赖图，避免漏判受影响目标
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当重试用尽仍失败时，**必须**升级人工并附 drift_detected
- 当变更涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

**格式校验**：
- [ ] 输出结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义 JSON 规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---
---

*版本：v2.0 · 2026-07-08 Gen3 升级*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [任务类型] for [用户水平], with [约束条件], leaning toward [方法/工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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


**相关概念**：[[信息管理系统]]

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
