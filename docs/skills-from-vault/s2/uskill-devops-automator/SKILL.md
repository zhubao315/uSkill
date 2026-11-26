---
name: uskill-devops-automator
description: "能自动化的绝不手动——手动意味着会出错。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S2-技术架构与安全/uSkill-devops-automator.md"
  original_id: "SKL-6402"
  version: "3.0.0"
  trust: untrusted
---

# DevOps自动化

description: |
  当用户需要搭建 CI/CD 管道、容器化部署、基础设施即代码、监控告警时使用此 Skill。
  触发词：'DevOps'、'CI/CD'、'容器化'、'Docker'、'Kubernetes'、'自动化部署'、'IaC'。

# DevOps 自动化

## 🎯 目标

> 构建从代码提交到生产部署的全自动化流水线。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `pipeline_type` | enum | ❌ | `"full"` | 类型：`build` / `test` / `deploy` / `full` |
| `infra` | enum | ❌ | `"cloud"` | 基础设施：`cloud` / `self_hosted` / `hybrid` |
| `container` | boolean | ❌ | `true` | 是否容器化 |

## 📤 输出

```json
{
  "cicd_config": "string — CI/CD 配置（GitHub Actions/GitLab CI）",
  "docker_config": "string — Dockerfile + docker-compose",
  "iac_config": "string — IaC 配置（Terraform/Pulumi）",
  "monitoring": "string — 监控告警方案",
  "runbook": "string — 运维手册"
}
```

## 📋 执行步骤

### Step 1: CI 管道搭建
1. **代码检查** — Lint + 类型检查 + 单元测试
2. **构建** — 编译/打包/镜像构建
3. **安全扫描** — 依赖漏洞扫描 + 镜像扫描
4. **检查点**：✅ 是否包含自动测试和安全扫描？

### Step 2: CD 管道搭建
1. **环境管理** — Dev/Staging/Prod 分环境部署
2. **滚动部署** — 零停机部署策略
3. **回滚机制** — 一键回滚能力
4. **检查点**：✅ 是否零停机？是否有回滚机制？

### Step 3: 基础设施即代码
1. **IaC 工具** — Terraform/Pulumi/CloudFormation
2. **状态管理** — 远程状态存储 + 状态锁
3. **模块化** — 可复用的基础设施模块
4. **检查点**：✅ 基础设施是否代码化？状态是否安全存储？

### Step 4: 监控与告警
1. **指标监控** — CPU/内存/磁盘/网络
2. **日志聚合** — 集中式日志（ELK/Loki）
3. **告警规则** — 关键指标告警 + 通知渠道
4. **检查点**：✅ 关键指标是否监控？告警是否及时？

## 💬 沟通风格
- **自动化优先**：任何手动步骤都是待优化项
- **可观测性**：没有监控的系统是盲人开车
- **渐进改进**：先跑通再优化，不追求完美

## 📝 自检清单
- [ ] CI 是否包含自动测试和安全扫描？
- [ ] CD 是否零停机部署？
- [ ] 基础设施是否代码化？
- [ ] 监控是否覆盖关键路径？
- [ ] 是否有一键回滚能力？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents DevOps Automator |


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


**相关概念**：[[灰度发布与蓝绿部署]]

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
