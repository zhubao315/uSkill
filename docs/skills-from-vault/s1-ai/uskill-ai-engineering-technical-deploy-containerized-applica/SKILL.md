---
name: uskill-ai-engineering-technical-deploy-containerized-applica
description: "让technical deploy containerized application变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-deploy-containerized-application.md"
  original_id: "SKL-6866"
  version: "3.0.0"
  trust: untrusted
---

# technical deploy containerized application

# Deploy Containerized Application

## 🎯 目标
> 将任何应用（尤其是AI应用）通过容器化技术高效、可靠地部署到云原生环境，将首次部署时间从数天缩短至4小时内，实现标准化、自动化的"最后一公里"交付。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `app_source` | string | ✅ | 应用源码仓库地址或本地路径 |
| `app_type` | enum | ✅ | `web-api` / `ai-inference` / `microservice` / `batch-job` |
| `language_framework` | string | ✅ | 语言与框架，如 `python/fastapi`、`node/express` |
| `target_cloud` | enum | ❌ | `aws` / `gcp` / `azure` / `private`，默认 `aws` |
| `gpu_required` | boolean | ❌ | 是否需要GPU资源，默认 `false` |
| `replicas` | int | ❌ | 初始副本数，默认 3 |
| `domain` | string | ❌ | 自定义域名，如 `app.example.com` |
| `budget_monthly_yuan` | number | ❌ | 月度预算上限（元），用于资源约束 |

## 📤 输出

```json
{
  "cost_estimate": {
    "monthly_yuan": "number — 月度预估成本",
    "instance_type": "string — 推荐实例类型",
    "breakdown": {"compute": "number", "storage": "number", "network": "number"}
  },
  "artifacts": {
    "dockerfile": "string — 优化后的Dockerfile内容",
    "terraform_hcl": "string — IaC基础设施代码",
    "k8s_manifests": {
      "deployment": "string — K8s Deployment YAML",
      "service": "string — K8s Service YAML",
      "ingress": "string — K8s Ingress YAML",
      "hpa": "string — HPA自动伸缩配置"
    },
    "cicd_pipeline": "string — CI/CD流水线配置（GitHub Actions YAML）"
  },
  "security_scan": {
    "critical_vulns": "int — 高危漏洞数",
    "high_vulns": "int — 中危漏洞数",
    "status": "pass | fail",
    "fixes": ["string — 修复建议"]
  },
  "monitoring": {
    "dashboards": ["string — Grafana仪表盘名称"],
    "alert_rules": ["string — 告警规则描述"],
    "health_endpoints": ["string — 健康检查URL"]
  },
  "deployment_status": "success | partial | failed",
  "access_url": "string — 部署后的访问地址"
}
```

## 📋 执行步骤

1. **准备与分析** — 分析应用特性（无状态/有状态、计算/IO密集），确定目标环境（公有云/私有集群），评估GPU需求，使用FinOps思维预估资源与成本
2. **高效容器化** — 生成多阶段构建（Multi-stage build）Dockerfile，以非root用户运行，配置健康检查，使用Trivy进行镜像安全扫描，推送到镜像仓库
3. **基础设施即代码** — 使用Terraform生成模块化IaC脚本（VPC、K8s集群、节点组），执行`terraform plan`预演，敏感信息通过Secrets Manager传入
4. **编排与部署** — 生成全套K8s清单（Deployment/Service/Ingress/ConfigMap/HPA），配置资源限制（含GPU），集成CI/CD自动部署，可选接入GitOps（ArgoCD/Flux）
5. **验证与监控** — 检查Pod/Service/Ingress状态，访问健康检查端点验证可用性，配置Prometheus/Grafana监控与告警（错误率>5%自动告警）

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `app_source` 无法访问 | 返回 `ERROR_SOURCE_UNAVAILABLE` + 检查路径/权限提示 |
| 预算无法支撑任何方案 | 返回 `WARNING_BUDGET_INSUFFICIENT` + 最低成本方案及缺口金额 |
| 镜像安全扫描发现高危漏洞 | 返回 `SECURITY_VULNERABLE` + 逐项修复建议，阻止部署 |
| GPU资源不足 | 推荐模型量化方案或CPU推理替代 + 成本对比 |
| K8s集群创建失败 | 返回Terraform错误日志 + 常见问题排查清单 |
| 健康检查持续失败 | 返回应用日志 + 端口/网络诊断步骤 |

## ✅ 自检清单

- [ ] Dockerfile采用多阶段构建，最终镜像 < 500MB
- [ ] 容器以非root用户运行
- [ ] 镜像安全扫描无高危/严重漏洞
- [ ] K8s Deployment配置了合理的资源请求/限制
- [ ] 健康检查（Liveness/Readiness Probes）已配置
- [ ] HPA自动伸缩策略已启用
- [ ] CI/CD流水线可自动触发部署
- [ ] 监控仪表盘和告警规则已就绪
- [ ] 成本预估在预算范围内


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-06 转化 |

---
**相关笔记**：[[全栈特性开发实现]] [[AI时代工程团队管理-宣讲文案]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [学习任务] for [知识背景], with [学习目标], leaning toward [学习方法/输出形式]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
