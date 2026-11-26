
description: |
  当用户需要管理开源项目的日常运维时使用此 Skill：每日 Issue 巡检、PR 审查、
  Release/Changelog 管理、贡献者互动与 Stale 清理。
  触发词包括：'开源运维'、'Issue管理'、'PR审查'、'Release管理'、'GitHub巡检'、'开源贡献'。
  即使用户没有说"开源"，只要意图涉及 GitHub 仓库的健康度维护与协作治理，也应触发。
  不适用：纯私有闭源仓库的内部 CI、与 GitHub 协作无关的代码编写。

---

# 🐙 uSkill-7103: 开源项目运维（Gen3）

## 🎯 目标

> 每日 Issue 巡检 + PR 审查 + Release 管理 + 贡献者互动，保障开源项目健康运行，
> 把"有人提没人管"的损耗转化为可持续的协作飞轮。

**适用场景**：托管于 GitHub 的个人/组织开源项目（如 [[uLife OS]] 相关工具链、
知识孪生体实现仓库）；与 [[uSkill-agent-社交资本与-ip-内容爆发路线图]] 的开发者关系联动。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `repo` | `string` | ✅ | 项目仓库 `owner/name` |
| `issues` | `array` | ❌ | 新 Issue 列表（缺省则经 `gh` 拉取） |
| `pull_requests` | `array` | ❌ | 新 PR 列表 |
| `contributors` | `array` | ❌ | 近期贡献者，用于互动提醒 |

---

## 📤 输出

```json
{
  "issues": [
    {"number": "number", "title": "string", "type": "bug|feature|question|security", "priority": "P0|P1|P2", "action": "string", "draft_reply": "string"}
  ],
  "prs": [
    {"number": "number", "title": "string", "status": "open|reviewing|ready", "review_suggestion": "approve|request_changes|comment", "checklist": ["string"]}
  ],
  "release": {"version": "string", "changelog": ["string"], "blockers": ["string"]},
  "manual_required": [{"number": "number", "reason": "string"}]
}
```

---

## 🔄 执行流程

```
1. [Issue巡检] → 分类并分级新 Issue
    → bug：功能异常、崩溃、数据错误
    → feature：功能请求、增强建议
    → question：使用咨询、配置问题
    → IF 标题/正文命中 security 关键词（泄露/RCE/注入/密钥）：立即标 P0+security
    → ELSE IF 影响核心路径的 bug：P0
    → ELSE：按类型给 P1/P2

2. [PR审查] → 检查 PR 是否符合规范
    → 代码规范：命名、格式、是否引入破坏性变更
    → 测试覆盖：是否新增/修改对应测试
    → 文档：是否更新 README / CHANGELOG / 注释
    → IF 全部通过且无破坏性变更：review_suggestion=approve
    → ELSE IF 仅文档/小问题：comment + request_changes
    → ELSE IF 存在冲突或测试缺失：标 manual_required

3. [Release管理] → 汇总可发布变更
    → 语义化版本：major(破坏性) / minor(新特性) / patch(修复)
    → IF 存在未关闭 P0：阻断 Release，写入 blockers
    → ELSE：生成 changelog 草稿

4. [贡献者互动] → 维护开发者关系
    → IF 新贡献者首 PR：生成欢迎 + 指引草稿
    → IF Stale(>30天无活动)：建议 gentle reminder 或自动标记 stale

5. [输出报告] → Issue + PR + Release + 需人工处理
    → IF 存在 security Issue：报告顶部用 🔴 高亮并强制 manual_required
```

---

## 📝 Prompt 模板

### 标准运维 Prompt

```
你是开源运维 Agent。请对以下 GitHub 仓库执行今日巡检。

【项目仓库】{repo}
【新 Issue】{issues}
【新 PR】{pull_requests}
【贡献者】{contributors}

【巡检维度】
1. Issue 分类：bug/feature/question/security + 优先级
2. PR 审查：规范、测试、文档、破坏性评估
3. Release 管理：语义化版本、Changelog、阻断检查
4. 贡献者互动：欢迎、Stale 清理

【风控规则】
- 安全类 Issue：立即 P0 + 转人工，不自动关闭
- 有冲突/测试缺失的 PR：不 approve，转人工

【输出格式】
严格按标准 JSON 输出，包含 issues、prs、release、manual_required。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| GitHub API 限流/离线 | 降级为本地 git 分析 | 仅分析已 clone 数据，标注"数据可能不全" |
| PR 冲突 | 标注"需解决冲突" | 不自动合并，转人工 |
| 安全漏洞 Issue | 立即 P0 + 人工处理 | 不自动回复/关闭 |
| 贡献者情绪激动 | 生成共情草稿 | 转维护者决策，不激化 |
| Release 有未关 P0 | 阻断发布 | 输出 blockers 清单 |

---

## ✅ 质量自检

- [ ] 每个 Issue 都有 type 与 priority 且可解释
- [ ] 安全类 Issue 已升级 P0 且进入 manual_required
- [ ] PR 审查含测试/文档/破坏性三维判断
- [ ] Release 仅在无未关 P0 时生成 changelog
- [ ] 新贡献者已生成欢迎互动
- [ ] 无虚构数据，计数来自 `gh` 真实拉取

---

## 💡 使用示例

### 示例 1：正常巡检

**输入**：
```json
{
  "repo": "harness-engineering-toolkit",
  "issues": [
    {"number": 42, "title": "RAG 部署文档缺失", "type": "feature"},
    {"number": 43, "title": "安装脚本在 M1 上报错", "type": "bug"}
  ],
  "pull_requests": [
    {"number": 15, "title": "添加单元测试覆盖切分器", "status": "open"}
  ]
}
```

**输出**：
```json
{
  "issues": [
    {"number": 42, "title": "RAG 部署文档缺失", "type": "feature", "priority": "P2", "action": "评估后加入路线图", "draft_reply": "感谢建议，已记入文档改进 backlog。"},
    {"number": 43, "title": "安装脚本在 M1 上报错", "type": "bug", "priority": "P0", "action": "立即修复", "draft_reply": "已复现，本周内修复并附回归测试。"}
  ],
  "prs": [
    {"number": 15, "title": "添加单元测试覆盖切分器", "status": "reviewing", "review_suggestion": "approve", "checklist": ["测试通过", "文档已更新"]}
  ],
  "release": {"version": "v0.4.1", "changelog": ["修复 M1 安装脚本", "新增切分器测试"], "blockers": []},
  "manual_required": []
}
```

### 示例 2：安全漏洞（边界）

**输入**：
```json
{
  "repo": "harness-engineering-toolkit",
  "issues": [{"number": 44, "title": "API 密钥硬编码在示例中被泄露", "type": "bug"}]
}
```

**输出**：
```json
{
  "issues": [{"number": 44, "title": "API 密钥泄露风险", "type": "security", "priority": "P0", "action": "紧急修复+安全审计", "draft_reply": "已升级为安全事件，正在处理，请勿公开细节。"}],
  "manual_required": [{"number": 44, "reason": "安全漏洞需人工处置并轮换密钥"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常巡检 | 分类+优先级报告 |
| 2 | Bug Issue | P0 优先 |
| 3 | PR 不规范 | request_changes |
| 4 | 安全漏洞 | 紧急 P0 + 人工 |
| 5 | Release 准备 | 阻断检查 + Changelog |
| 6 | 新贡献者 | 欢迎互动草稿 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得违反 GitHub 社区准则与开源许可
2. 不得泄露用户隐私或密钥等敏感数据
3. 安全类 Issue **必须**升级 P0 并转人工，禁止自动关闭

**软性约束（建议遵守）**：
1. 优先复用项目既有的 CONTRIBUTING 与 CI 规范
2. 复杂决策应记录理由供后续审计

**人工兜底点**：
- 当 PR 涉及架构级破坏性变更时，**必须**转维护者决策
- 当涉及安全/合规时，**必须**暂停自动操作等待确认

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

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

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
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

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


**相关概念**：[[开源贡献者技能]]

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
