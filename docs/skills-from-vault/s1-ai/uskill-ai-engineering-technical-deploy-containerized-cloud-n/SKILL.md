---
name: uskill-ai-engineering-technical-deploy-containerized-cloud-n
description: "让technical deploy containerized cloud native变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-technical-deploy-containerized-cloud-native.md"
  original_id: "SKL-6869"
  version: "3.0.0"
  trust: untrusted
---

# technical deploy containerized cloud native

# Cloud-Native Containerized Deployment

## 🎯 目标
> 建立标准化、自动化的 AI 赋能五步部署流水线，将任何应用（尤其是 AI 模型服务）通过容器化技术高效、可靠地部署到云原生环境，新应用首次部署时间从数天缩短至 4 小时内。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `app_info` | object | ✅ | `{name: "string", language: "string", framework: "string", port: "int", stateful: "boolean"}` — 应用基本信息 |
| `deployment_target` | enum | ✅ | `aws` / `gcp` / `azure` / `private_k8s` — 目标部署环境 |
| `ai_workload` | object | ❌ | `{model_name: "string", model_size_gb: "number", gpu_required: "boolean", gpu_type: "string"}` — AI 应用特有参数 |
| `budget_monthly_yuan` | number | ❌ | 月度预算上限（元），用于 FinOps 成本约束 |
| `replicas` | int | ❌ | 期望副本数，默认 3 |
| `domain` | string | ❌ | 自定义域名，如 `app.example.com` |
| `ci_cd_platform` | enum | ❌ | `github_actions` / `gitlab_ci` / `jenkins`，默认 `github_actions` |

## 📤 输出

```json
{
  "finops_estimation": {
    "cpu_cores": "int",
    "memory_gb": "number",
    "gpu_count": "int",
    "storage_gb": "number",
    "instance_type": "string",
    "monthly_cost_yuan": "number",
    "cost_breakdown": {"compute": "number", "storage": "number", "network": "number"}
  },
  "dockerfile": {
    "content": "string — 多阶段构建 Dockerfile 内容",
    "base_image": "string",
    "final_image_size_mb": "number",
    "runs_as_non_root": "boolean",
    "health_check_included": "boolean",
    "security_scan": {"passed": "boolean", "critical_vulns": "int", "high_vulns": "int"}
  },
  "terraform": {
    "modules": ["string — Terraform 模块列表"],
    "vpc_config": "string — VPC/子网配置摘要",
    "cluster_config": "string — K8s 集群配置摘要",
    "estimated_monthly_yuan": "number",
    "plan_preview": "string — terraform plan 输出摘要"
  },
  "k8s_manifests": {
    "deployment": "string — Deployment YAML",
    "service": "string — Service YAML",
    "ingress": "string — Ingress YAML",
    "hpa": "string — HPA YAML",
    "configmap": "string — ConfigMap YAML (if needed)",
    "secret_template": "string — Secret YAML 模板"
  },
  "cicd_pipeline": {
    "platform": "string",
    "config_file": "string — CI/CD 配置文件内容",
    "stages": ["build", "test", "scan", "push", "deploy"]
  },
  "monitoring": {
    "metrics": ["string — 关键监控指标"],
    "alert_rules": ["string — 告警规则"],
    "dashboard_url": "string — Grafana 仪表盘链接"
  },
  "validation": {
    "pod_status": "string",
    "service_accessible": "boolean",
    "health_endpoint_ok": "boolean",
    "deployment_notes": ["string"]
  }
}
```

## 📋 执行步骤

1. **准备与分析** — 分析 `app_info` 特性（无状态/有状态、计算密集/IO 密集），判断 AI 应用是否需要 GPU，使用 FinOps 思维预估资源需求和成本，输出资源估算表
2. **高效容器化** — 生成多阶段构建 Dockerfile（slim 基础镜像、非 root 用户、健康检查、依赖缓存），使用 Trivy 进行安全扫描，将镜像推送到容器仓库
3. **基础设施即代码** — 生成模块化 Terraform 脚本（VPC、K8s 集群、节点组），执行 `terraform plan` 预演确认变更，敏感信息通过 Secrets Manager 管理
4. **编排与部署** — 生成全套 Kubernetes YAML 清单（Deployment/Service/Ingress/HPA/ConfigMap/Secret），AI 应用特别配置 GPU 资源限制，配置 CI/CD 自动部署作业，可选启用 GitOps（ArgoCD/Flux）
5. **验证与监控** — 执行 `kubectl get pods,svc,ingress` 验证资源状态，访问健康检查端点确认服务可用，配置 Prometheus/Grafana 监控和告警规则（错误率 >5%、延迟 P99 >500ms）

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `app_info` 缺少关键字段（如端口、语言） | 返回 `ERROR_MISSING_APP_INFO` + 需补充字段清单 |
| 预算无法支撑最低配置 | 返回 `WARNING_BUDGET_INSUFFICIENT` + 最低成本方案及缺口金额 |
| 镜像安全扫描发现高危漏洞 | 返回 `BLOCK_CRITICAL_VULN` + 漏洞修复建议，阻止部署 |
| GPU 资源不足或不可用 | 降级到 CPU 推理方案 + 量化优化建议（如 INT8/INT4） |
| `terraform apply` 失败 | 输出错误日志 + 回滚命令 + 常见修复方案 |
| 部署后健康检查持续失败 | 自动回滚到上一版本 + 输出 Pod 日志用于排查 |

## ✅ 自检清单

- [ ] Dockerfile 采用多阶段构建，最终镜像 <500MB
- [ ] 容器以非 root 用户运行，安全扫描无高危漏洞
- [ ] Terraform 代码模块化，敏感信息未硬编码
- [ ] K8s Deployment 配置了合理的资源请求/限制和健康检查
- [ ] HPA 自动伸缩策略已配置（CPU >75% 触发扩容）
- [ ] CI/CD 流水线覆盖 build→test→scan→push→deploy 全流程
- [ ] 监控仪表盘和告警规则已就绪
- [ ] FinOps 成本预估已输出，含 Token/GPU 费用（AI 应用场景）


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
- [ ] 输出

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
