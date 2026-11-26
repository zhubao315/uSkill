---
name: uskill-efficiency-knowledge-management
description: "让知识管理系统变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-efficiency-knowledge-management.md"
  original_id: "SKL-5208"
  version: "3.0.0"
  trust: untrusted
---

# 知识管理系统

description: |
  当用户需要设计知识管理系统、应用 PARA/CODE/Zettelkasten 方法论、搭建知识库架构时使用此 Skill。
  触发词包括：'知识管理'、'笔记系统'、'第二大脑'、'PARA'、'Zettelkasten'、'知识库'、'笔记方法'。
  当用户提到"笔记太乱找不到"、"学了就忘"、"知识不成体系"时，
  即使未直接说"知识管理"，也应使用此 Skill。
  不适用于简单的笔记记录。遇到知识体系化构建和长期维护时优先使用。

---

# uSkill-208: 知识管理系统

## 🎯 目标

> 设计可持续的知识管理系统，应用 PARA/CODE/Zettelkasten 方法论，构建可检索、可关联、可复用的知识库。

**核心价值**：将碎片化信息转化为结构化知识资产，提升学习和决策效率。

**适用场景**：
- 个人知识库架构设计
- 团队知识管理系统搭建
- 学习笔记体系化
- 研究资料整理
- 经验沉淀与复用

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `methodology` | `enum` | ✅ | — | `para` / `code` / `zettelkasten` / `hybrid` |
| `use_case` | `string` | ✅ | — | 知识管理用途描述 |
| `current_notes` | `number` | ❌ | `0` | 现有笔记数量 |
| `tools` | `array` | ❌ | `[]` | 已有工具（如 Obsidian、Notion） |
| `context` | `object` | ❌ | — | `{domain, team_size, collaboration_needs}` |

**输入约束**：
- `methodology` 应与用户习惯和场景匹配
- `current_notes` 用于评估迁移复杂度
- `tools` 应列出实际使用的工具

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话总结知识管理方案",
  "km_id": "KM-YYYY-MMDD-NNN",

  "architecture": {
    "methodology": "string",
    "folder_structure": {
      "root": ["string"],
      "explained": "string"
    },
    "naming_conventions": {
      "notes": "string",
      "folders": "string",
      "tags": "string"
    },
    "metadata_schema": "string"
  },

  "workflow": {
    "capture": {
      "sources": ["string"],
      "process": "string",
      "inbox_rules": "string"
    },
    "organize": {
      "classification": "string",
      "linking_strategy": "string",
      "review_cycle": "string"
    },
    "retrieve": {
      "search_strategy": "string",
      "browsing_structure": "string",
      "quick_access": "string"
    },
    "share": {
      "export_formats": ["string"],
      "collaboration_rules": "string"
    }
  },

  "implementation": {
    "phases": [
      {
        "phase": "string",
        "duration": "string",
        "tasks": ["string"],
        "success_criteria": "string"
      }
    ],
    "migration_plan": "string",
    "training_plan": "string"
  },

  "maintenance": {
    "review_schedule": "string",
    "cleanup_rules": "string",
    "evolution_path": "string"
  },

  "metrics": {
    "target_retrieval_time": "string",
    "target_link_density": "string",
    "target_reuse_rate": "string"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 需求分析与方法论选择

- **输入**：`methodology`, `use_case`, `current_notes`
- **动作**：
  1. 分析用户知识管理痛点
  2. 评估各方法论的适用性
  3. 推荐最适合的方案
- **输出**：`architecture.methodology`
- **分支条件**：
  - IF 目标是行动导向（项目管理）→ 推荐 PARA
  - IF 目标是理解和内化 → 推荐 Zettelkasten
  - IF 需要编码规范和最佳实践 → 推荐 CODE
  - IF 多种需求并存 → 推荐混合方案
  - ELSE → 根据用户习惯定制
- **检查点**：✅ 应验证方法论与用户目标匹配

### Step 2: 架构设计

- **输入**：选定的方法论
- **动作**：
  1. 设计文件夹结构
  2. 定义命名规范
  3. 设计元数据 Schema
  4. 创建标签体系
- **输出**：`architecture`
- **分支条件**：
  - IF 笔记 < 100 → 简化结构，避免过度分类
  - IF 笔记 > 500 → 增加中间层级，便于浏览
  - IF 团队协作 → 增加共享层和权限设计
  - IF 跨领域 → 设计交叉索引机制
- **检查点**：✅ 应验证结构可扩展且不超过 3 层深度

### Step 3: 工作流设计

- **输入**：`architecture`
- **动作**：
  1. 设计捕获流程
  2. 设计组织流程
  3. 设计检索策略
  4. 设计共享机制
- **输出**：`workflow`
- **分支条件**：
  - IF 信息来源多样 → 设计统一的捕获入口
  - IF 检索需求高 → 增加搜索索引和快捷方式
  - IF 需要定期回顾 → 设计 review cycle
  - IF 有协作需求 → 设计权限和版本管理
- **检查点**：✅ 应验证工作流覆盖知识全生命周期

### Step 4: 实施规划

- **输入**：`architecture`, `workflow`
- **动作**：
  1. 分阶段实施计划
  2. 迁移现有笔记
  3. 培训和习惯养成
- **输出**：`implementation`
- **分支条件**：
  - IF 现有笔记 > 200 → 分批迁移，不一次性处理
  - IF 工具复杂 → 增加培训材料和视频教程
  - IF 团队使用 → 增加统一规范和模板
  - ELSE → 快速实施
- **检查点**：✅ 应验证实施步骤可执行且有明确里程碑

### Step 5: 维护机制设计

- **输入**：`implementation`
- **动作**：
  1. 设计定期回顾机制
  2. 设计清理规则
  3. 规划系统演进路径
- **输出**：`maintenance`
- **检查点**：✅ 应验证维护成本可控且可持续

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**设计超过 4 层的文件夹结构
2. **不得**要求每天维护超过 30 分钟
3. **必须**提供迁移方案（如已有笔记）
4. **必须**保证检索路径不超过 3 步

### 软性约束（建议遵守）
1. 每篇笔记应至少有 1 个标签
2. 每周进行一次快速回顾
3. 每月进行一次深度整理
4. 优先使用已有工具而非新建

### 人工兜底点
- 当笔记分类不确定时，**必须**放入

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
