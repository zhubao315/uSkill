---
name: uskill-api-tester
description: "没有自动化测试的 API——是一颗定时炸弹。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-api-tester.md"
  original_id: "SKL-6409"
  version: "3.0.0"
  trust: untrusted
---

# API测试与自动化

description: |
  当用户需要编写 API 测试用例、搭建自动化测试框架、进行接口验证时使用此 Skill。
  触发词：'API测试'、'接口测试'、'自动化测试'、'Postman'、'pytest'、'api testing'。

# API 测试与自动化

## 🎯 目标

> 建立可维护、可扩展的 API 自动化测试体系。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `api_type` | enum | ❌ | `"rest"` | 类型：`rest` / `graphql` / `grpc` / `websocket` |
| `test_level` | enum | ❌ | `"integration"` | 级别：`unit` / `integration` / `e2e` / `contract` |

## 📤 输出

```json
{
  "test_plan": {"coverage_target": "int", "test_cases": "int", "scenarios": ["string"]},
  "test_code": "string — 测试代码",
  "ci_integration": "string — CI 集成方案"
}
```

## 📋 执行步骤

### Step 1: 测试计划
1. **接口清单** — 枚举所有 API 端点
2. **用例设计** — 正常/异常/边界三种场景
3. **优先级** — 核心接口 > 普通接口 > 边缘接口
4. **检查点**：✅ 是否覆盖了核心接口？场景是否完整？

### Step 2: 测试编写
1. **正常场景** — 正确参数的请求-响应验证
2. **异常场景** — 缺失参数/错误类型/越界值
3. **边界场景** — 空值/最大值/特殊字符
4. **认证测试** — 无 Token/过期 Token/权限不足
5. **检查点**：✅ 是否包含认证测试？异常场景是否完整？

### Step 3: 自动化集成
1. **框架选择** — pytest/Jest/Newman
2. **CI 集成** — 每次 PR 自动运行
3. **测试数据隔离** — 每次测试使用独立数据
4. **检查点**：✅ 是否集成到 CI？测试数据是否隔离？

### Step 4: 报告与维护
1. **覆盖率报告** — 接口覆盖率和场景覆盖率
2. **失败分析** — 自动化失败的原因分析
3. **用例维护** — 接口变更时同步更新测试
4. **检查点**：✅ 覆盖率是否达标？失败用例是否分析？

## 💬 沟通风格
- **覆盖优先**：先保证覆盖率，再优化用例质量
- **快速反馈**：测试应该在 5 分钟内完成
- **失败即信号**：自动化失败 = 需要立即关注

## 📝 自检清单
- [ ] 是否覆盖了正常/异常/边界三种场景？
- [ ] 是否包含认证/授权测试？
- [ ] 是否集成到 CI？
- [ ] 测试数据是否隔离？
- [ ] 覆盖率是否达标？

---


#### ⚠️ 边界约束

> 此区块定义此 Skill 的硬性限制和软性约束，确保执行不越界。

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 不得在未经验证的情况下做出不可逆决策

**软性约束（建议遵守）**：
1. 优先使用已验证的方法论，避免发明新轮子
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

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

## 📝 变更日志
| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents API Tester + Accessibility Auditor |


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


**相关概念**：[[API安全设计]] · [[API网关设计]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

## 🧪 Self-Play 测试用例

| #

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
