# Container Deployment Pipeline

## 🎯 目标

> 将应用（尤其是AI模型服务）通过容器化技术标准化、自动化地部署到云原生环境（Kubernetes集群），将首次部署时间从数天缩短至4小时内。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `app_source` | string | ✅ | 应用源码仓库地址或本地路径 |
| `app_type` | enum | ✅ | `web-api` / `ai-inference` / `microservice` / `batch-job` |
| `tech_stack` | string | ✅ | 技术栈描述，如 `Python/FastAPI`、`Node.js/Express` |
| `target_cloud` | enum | ✅ | `aws` / `gcp` / `azure` / `private` |
| `cluster_config` | object | ❌ | 已有集群配置（kubeconfig路径），为空则新建 |
| `domain` | string | ❌ | 应用对外域名，如 `app.example.com` |
| `gpu_required` | boolean | ❌ | 是否需要GPU资源，默认 `false` |
| `replicas` | int | ❌ | 副本数，默认 `3` |

## 📤 输出

```json
{
  "dockerfile_path": "string — 生成的Dockerfile路径",
  "image_tag": "string — 构建的容器镜像标签",
  "security_scan_result": {
    "passed": "boolean — 是否通过安全扫描",
    "critical_vulns": "int — 高危漏洞数"
  },
  "infra_scripts_path": "string — Terraform脚本路径",
  "k8s_manifests_path": "string — Kubernetes YAML清单目录",
  "deployment_status": "enum — pending/deploying/running/failed",
  "endpoints": ["string — 可访问的服务端点URL列表"],
  "monitoring_dashboard": "string — 监控仪表盘地址"
}
```

## 📋 执行步骤

1. **分析部署目标** — 评估应用特性（有状态/无状态、计算密集/IO密集），确定目标环境（公有云/私有集群），预估CPU、内存、GPU资源需求与月度成本
2. **生成Dockerfile** — 使用AI生成多阶段构建的Dockerfile：基于官方slim镜像、分离构建与生产阶段、以非root用户运行、包含健康检查指令、缓存常用依赖
3. **构建与安全扫描** — 执行 `docker build` 构建镜像，使用Trivy扫描漏洞，确认无高危漏洞后推送到容器镜像仓库（Docker Hub / ghcr.io）
4. **编写基础设施代码** — 生成Terraform脚本创建VPC、Kubernetes集群（EKS/GKE）及自动伸缩节点组，确保网络和IAM遵循最小权限原则
5. **预演与应用基础设施** — 执行 `terraform plan` 预演变更，确认无误后执行 `terraform apply`，将tfstate安全存储至远端
6. **生成K8s部署清单** — 生成Deployment、Service、Ingress、ConfigMap、HPA等YAML，配置资源请求/限制、健康检查（Liveness/Readiness Probes），AI应用须配置GPU资源限制
7. **配置CI/CD自动化** — 在GitHub Actions等平台添加部署Job，代码合并到主分支后自动执行 `kubectl apply`；推荐使用ArgoCD/Flux实现GitOps同步
8. **执行部署与验证** — 执行 `kubectl apply` 部署，通过 `kubectl get pods,svc,ingress` 确认资源正常，访问健康检查端点验证服务可用性
9. **配置监控告警** — 部署Prometheus/Grafana监控，添加CPU/内存使用率、请求延迟、错误率等关键指标仪表盘，配置告警规则（如错误率 > 5%）

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 镜像构建失败 | 检查Dockerfile语法和依赖，回退到上一个成功构建的镜像层 |
| 安全扫描发现高危漏洞 | 阻断部署流程，生成漏洞修复建议，修复后重新扫描 |
| `terraform apply` 失败 | 保留tfstate，分析错误日志，修复脚本后重新plan/apply |
| Pod启动失败（CrashLoopBackOff） | 检查Pod日志 `kubectl logs`，验证环境变量和资源限制是否正确 |
| Ingress域名无法访问 | 检查DNS解析、TLS证书配置、Service端口映射是否一致 |
| GPU资源不足 | 检查节点GPU调度状态，调整 `nvidia.com/gpu` 资源请求或扩容节点池 |

## ✅ 自检清单

- [ ] Dockerfile采用多阶段构建，最终镜像以非root用户运行
- [ ] 镜像安全扫描通过，无Critical级别漏洞
- [ ] Terraform代码模块化，敏感信息通过Secrets Manager传入，无硬编码
- [ ] K8s Deployment配置了合理的资源请求/限制和副本数
- [ ] Liveness和Readiness Probes已正确配置
- [ ] 监控仪表盘可观察到新部署应用的指标数据
- [ ] 关键告警规则已配置并测试触发


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
| 2026-05-09 | 1.0.0 | 初始版本，从 SOP-06（云计算专家-容器化部署）转化 |

---
**相关笔记**：[[消息队列选型]] [[RPVI 提示词工程]] 


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
