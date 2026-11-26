# CI/CD Pipeline Design

> **角色**: DevOps工程师 | **核心工具**: AI大模型, GitHub Actions, GitLab CI | **效率目标**: 自动化构建、测试、部署全流程，将发布周期从天级缩短到小时级

## 🎯 目标

设计**高效的CI/CD流水线**，实现代码提交到生产部署的全自动化，包含代码检查、自动化测试、安全扫描、构建打包、多环境部署和回滚机制。

**适用场景**:
1. **新建CI/CD流水线** — 为新项目从零搭建自动化流水线
2. **优化现有流水线** — 改善构建速度、可靠性、安全性
3. **多环境部署管理** — 设计dev/staging/production多环境发布流程

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `project_info` | object | ✅ | 项目信息：`{language, framework, build_tool, repo_platform}` |
| `deployment_target` | object | ✅ | 部署目标：`{platform, environment, containerized}` |
| `team_workflow` | object | ✅ | 团队工作流：`{branching_model, review_required, release_frequency}` |
| `quality_gates` | array | ❌ | 质量门禁：`{type, threshold}` 列表 |
| `security_requirements` | array | ❌ | 安全扫描需求 |
| `notification_config` | object | ❌ | 通知配置：`{channels, events}` |

## 📤 输出

```json
{
  "pipeline_design": {
    "stages": [
      {
        "name": "string — 阶段名称",
        "jobs": [
          {
            "name": "string",
            "trigger": "string — 触发条件",
            "steps": ["string — 执行步骤"],
            "artifacts": ["string — 产出物"],
            "estimated_duration": "string"
          }
        ],
        "parallel": "boolean — 是否并行执行"
      }
    ],
    "total_estimated_duration": "string"
  },
  "workflow_triggers": {
    "on_push": {"branches": ["string"], "actions": ["string"]},
    "on_pr": {"target_branches": ["string"], "actions": ["string"]},
    "on_schedule": {"cron": "string", "actions": ["string"]},
    "on_manual": {"parameters": ["string"]}
  },
  "environment_strategy": {
    "environments": [
      {
        "name": "string",
        "deployment_trigger": "string",
        "approval_required": "boolean",
        "rollback_strategy": "string"
      }
    ]
  },
  "quality_gates": [
    {"gate": "string", "threshold": "string", "blocking": "boolean"}
  ],
  "config_templates": {
    "github_actions": "string — GitHub Actions workflow YAML",
    "gitlab_ci": "string — .gitlab-ci.yml"
  },
  "best_practices": ["string — 针对项目的最佳实践建议"]
}
```

## 📋 执行步骤

### 阶段一：流水线需求分析

1. **代码质量门禁定义** — 确定必须通过的质量检查：
   - 代码风格检查（ESLint/Prettier/Black）
   - 静态代码分析（SonarQube）
   - 单元测试覆盖率阈值（≥80%）
   - 安全漏洞扫描（Dependabot/Snyk）
2. **构建策略确定** — 增量构建 vs 全量构建、构建缓存策略
3. **部署策略确定** — 蓝绿部署/金丝雀发布/滚动更新
4. **环境管理策略** — 定义dev/staging/production环境及其晋升规则

### 阶段二：流水线阶段设计

5. **Stage 1: 代码检查 (Lint & Format)**
   - 代码风格自动检查和修复提示
   - Commit message格式检查
   - 预计耗时：< 2分钟
6. **Stage 2: 构建与单元测试 (Build & Test)**
   - 依赖安装（利用缓存加速）
   - 编译构建
   - 单元测试执行（并行分片加速）
   - 覆盖率报告生成
   - 预计耗时：5-10分钟
7. **Stage 3: 集成测试 (Integration Test)**
   - 数据库/中间件容器化启动（Testcontainers）
   - API集成测试
   - 预计耗时：5-15分钟
8. **Stage 4: 安全扫描 (Security Scan)**
   - 依赖漏洞扫描
   - 容器镜像扫描
   - SAST静态安全分析
   - 预计耗时：3-5分钟
9. **Stage 5: 构建制品 (Build Artifacts)**
   - Docker镜像构建与推送
   - 版本号自动标记（Git tag/SHA）
   - 预计耗时：2-5分钟
10. **Stage 6: 部署 (Deploy)**
    - 自动部署到dev环境
    - Staging环境部署（可选需审批）
    - Production环境部署（需审批+自动回滚配置）
    - 部署后冒烟测试

### 阶段三：高级特性设计

11. **缓存优化** — 依赖缓存、构建缓存、Docker层缓存
12. **矩阵构建** — 多语言版本/多操作系统并行测试
13. **环境变量管理** — Secrets管理（Vault/GitHub Secrets）
14. **通知集成** — 构建结果推送（Slack/钉钉/邮件）
15. **制品管理** — 版本化存储、保留策略

### 阶段四：可靠性与可观测性

16. **失败重试机制** — 网络抖动等临时失败的自动重试
17. **流水线监控** — 构建时长趋势、成功率、队列等待时间
18. **回滚机制** — 一键回滚到上一个成功版本
19. **审计日志** — 记录谁在何时触发了什么部署

## ✅ 检查清单

- [ ] 代码提交是否自动触发流水线
- [ ] 单元测试覆盖率是否达到设定阈值
- [ ] 安全扫描是否集成到流水线
- [ ] 构建缓存是否已优化（构建时间 < 15分钟）
- [ ] 生产部署是否有审批门禁
- [ ] 是否支持一键回滚
- [ ] Secrets是否通过安全方式管理（不硬编码）
- [ ] 构建失败是否及时通知相关人员
- [ ] 是否有完整的构建审计日志

## ⚠️ 常见陷阱

| 陷阱 | 说明 | 规避方法 |
|------|------|---------|
| 流水线过慢 | 构建时间超过30分钟，开发者不愿等待 | 并行化、缓存优化、测试分片 |
| 测试不稳定 | Flaky test导致误报，开发者忽略失败 | 立即修复或删除不稳定测试 |
| 缺少回滚机制 | 部署失败无法快速恢复 | 每次部署保留前一版本镜像，支持一键回滚 |
| Secrets泄露 | 密钥硬编码或日志打印 | 使用Secrets管理，扫描敏感信息 |
| 分支策略混乱 | 没有清晰的分支和发布策略 | 明确Git Flow或Trunk-Based策略 |
| 忽略构建安全 | 依赖漏洞不扫描 | 集成依赖扫描和容器镜像扫描 |

## 🔗 关联

- **相关技能**: 微服务拆分决策, 缓存架构设计, 消息队列选型
- **推荐工具**: GitHub Actions, GitLab CI, ArgoCD, Tekton
- **经典著作**: 《Accelerate》— Nicole Forsgren, 《Continuous Delivery》— Jez Humble


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
**相关笔记**：[[RPVI 提示词工程]] [[SOP-03-云计算专家-容器化部署]] 


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

---


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据


## 📝 Prompt 模板

> 用于调用 AI 辅助执行本技能的标准提示词模板。

**核心提示词**：
```
你是一位资深 DevOps 工程师，精通 CI/CD 流水线设计与基础设施即代码实践。请根据以下输入设计 CI/CD 流水线：
输入：项目技术栈、代码仓库结构、部署目标环境（K8s/VM/Serverless）、团队规模与发布频率
要求：设计从代码提交到生产部署的完整流水线，涵盖构建、测试、安全扫描、制品管理、部署策略（蓝绿/金丝雀）和回滚机制，兼顾效率与安全
输出格式：流水线阶段图、各阶段详细配置说明、工具选型对比、环境变量与密钥管理方案、监控与告警集成方案
```

**使用说明**：
- 替换方括号内的占位符为实际内容
- 根据具体场景调整要求部分
- 输出格式可根据需要修改

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
