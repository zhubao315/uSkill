---
name: skill-8966071f
description: "云原生容器化部署"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S2-技术架构与安全/云原生容器化部署.md"
  original_id: ""
  version: ""
  trust: untrusted
---

# 云原生容器化部署

# 云原生容器化部署

> O-101 断链治理正本：中文入口，承接 uSkill 索引与 agency-agents 映射入链；详版见关联 uSkill。

## 一句话

将应用容器化并交付到 Kubernetes 的端到端实践：镜像构建 → 清单编排 → GitOps 发布 → 可观测回滚。

## 要点
- 流程：Dockerfile 多阶段构建 → 镜像扫描与签名 → Helm/Kustomize 清单 → CI/CD 滚动/金丝雀发布 → Prometheus/Grafana 观测。
- 一致性目标：开发/预发/生产三环境同构；首次部署从数天压到小时级（见 [[SOP-03-云计算专家-容器化部署]]）。
- 配套：CI/CD 流水线设计、微服务拆分、缓存/消息选型与本技能同属 S2 架构簇。

## 关联
- - 详版：[[uSkill-architecture-cloud-native-containerization]] · [[uSkill-architecture-containerized-app-deployment]]
- - SOP：[[SOP-03-云计算专家-容器化部署]]
- - 邻接：[[uSkill-ai-engineering-technical-deploy-containerized-cloud-native]] · [[∑ uSkill 索引]]

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
