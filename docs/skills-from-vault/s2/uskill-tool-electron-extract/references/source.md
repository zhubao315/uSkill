
description: |
  当用户需要逆向工程/应用分析时使用此 Skill。
  触发词包括：'提取Electron'、'反编译Electron'、'asar提取'、'看应用源码'。
  这是一个已安装的可执行工具参考卡片，指向实际工具：`baoyu-electron-extract`。

---

# 📦 Electron应用源码提取

## 🎯 目标

> 从已安装的 Electron 应用中提取资源和 JavaScript，支持 .asar 解包和 .js.map 源码还原。

**工具类型**：已安装可执行技能 | **实际路径**：`~/.claude/skills/baoyu-electron-extract/SKILL.md`

---

## 📥 触发条件

| 条件 | 说明 |
|------|------|
| 触发词 | '提取Electron'、'反编译Electron'、'asar提取'、'看应用源码' |
| 工具依赖 | bun/npx |
| 分类 | 逆向工程/应用分析 |

---

## 🔧 执行方式

此技能已作为 Claude Code skill 安装在 `~/.claude/skills/baoyu-electron-extract/` 目录下。

**调用方法**：在对话中使用 `/electron-extract` 或直接描述需求，Agent 会自动加载对应 skill 执行。

**完整文档**：`~/.claude/skills/baoyu-electron-extract/SKILL.md`

---

## 📋 与其他 uSkill 的关系

- **上游**：此工具可被 `uSkill-agent-循环工程统一调度入口` 调度使用
- **下游**：生成的内容可流入 `uWise` 知识词条或 `uRead` 读书笔记
- **协作**：与同类别 uSkill 配合使用，如配图类工具可组合使用

---

## 📝 自检清单

- [ ] 是否在正确的场景触发了此工具？
- [ ] 工具参数是否正确配置？
- [ ] 输出是否符合预期格式？
- [ ] 是否需要与其他工具组合使用？

---

*关联：[[uSkill-agent-循环工程统一调度入口]] · [[uSkill-agent-全局审计专项循环]] · [[Home]]*


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

---


## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |


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
