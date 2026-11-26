---
name: uskill-oss-ops
description: "让开源项目运维 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-oss-ops.md"
  original_id: "SKL-5318"
  version: "3.0.0"
  trust: untrusted
---

# 开源项目运维 Agent — 实施手册

description: |
  当用户需要管理开源项目的日常运维时使用此 Skill。
  触发词包括：'开源运维'、'Issue管理'、'PR审查'、'Release管理'。

---

# 🐙 uSkill-318: 开源项目运维

## 🎯 目标

> 每日 Issue 巡检 + PR 审查 + Release 管理，保障开源项目健康运行。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `repo` | `string` | ✅ | 项目仓库地址 |
| `issues` | `array` | ❌ | 新 Issue 列表 |
| `pull_requests` | `array` | ❌ | 新 PR 列表 |

---

## 📤 输出

```json
{
  "issues": [{"number": "number", "title": "string", "type": "bug|feature|question", "priority": "string", "action": "string"}],
  "prs": [{"number": "number", "title": "string", "status": "string", "review_suggestion": "string"}],
  "manual_required": ["string"]
}
```

---

## 🔄 执行流程

```
1. [Issue巡检] → 分类新Issue
   → bug：功能异常、崩溃、数据错误
   → feature：功能请求、增强建议
   → question：使用咨询、配置问题
   → 判断条件：是否涉及安全漏洞？
     → 是：立即标注P0
     → 否：按类型分类

2. [PR审查] → 检查PR是否符合规范
   → 代码规范：命名、格式、注释
   → 测试覆盖：是否有对应测试
   → 文档更新：是否更新了README/CHANGELOG
   → 判断条件：是否通过所有检查？
     → 是：建议approve
     → 否：建议request_changes

3. [Release管理] → 更新Release计划
   → 版本号：语义化版本（major.minor.patch）
   → Changelog：汇总本次变更
   → 发布检查清单

4. [输出报告] → Issue状态 + PR状态 + 需人工处理
```

---

## 📝 Prompt 模板

### 标准运维 Prompt

```
你是开源运维Agent。请执行今日巡检。

【项目仓库】{repo}
【新Issue】{issues}
【新PR】{pull_requests}

【巡检维度】
1. Issue分类：bug/feature/question + 优先级
2. PR审查：规范、测试、文档
3. Release管理：版本号、Changelog

【输出格式】
按标准 JSON 输出，包含 issues、prs、manual_required。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| GitHub API 限流 | 降级为本地分析 | 仅分析已有数据 |
| PR冲突 | 标注"需解决冲突" | 不自动合并 |
| 安全漏洞Issue | 立即P0+人工处理 | — |

---

## 💡 使用示例

### 示例 1：正常巡检

**输入**：
```json
{
  "repo": "harness-engineering-toolkit",
  "issues": [
    {"number": 42, "title": "RAG部署文档缺失", "type": "feature"},
    {"number": 43, "title": "安装脚本报错", "type": "bug"}
  ],
  "pull_requests": [
    {"number": 15, "title": "添加单元测试", "status": "open"}
  ]
}
```

**输出**：
```json
{
  "issues": [
    {"number": 42, "title": "RAG部署文档缺失", "type": "feature", "priority": "P2", "action": "评估后加入路线图"},
    {"number": 43, "title": "安装脚本报错", "type": "bug", "priority": "P0", "action": "立即修复"}
  ],
  "prs": [
    {"number": 15, "title": "添加单元测试", "status": "open", "review_suggestion": "approve"}
  ],
  "manual_required": []
}
```

### 示例 2：安全漏洞

**输入**：
```json
{
  "issues": [{"number": 44, "title": "API密钥泄露风险", "type": "bug"}]
}
```

**输出**：
```json
{
  "issues": [{"number": 44, "title": "API密钥泄露风险", "type": "bug", "priority": "P0", "action": "紧急修复+安全审计"}],
  "manual_required": [{"number": 44, "reason": "安全漏洞需人工处理"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常巡检 | 分类报告 |
| 2 | Bug Issue | P0优先 |
| 3 | PR不规范 | 修改建议 |
| 4 | 安全漏洞 | 紧急处理 |
| 5 | Release准备 | 检查清单 |


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
---

*版本：v2.0 · 2026-06-29 升级*


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
| ""年轻扛得住"" 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
