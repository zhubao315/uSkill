
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
- 当笔记分类不确定时，**必须**放入 Inbox 待处理
- 当系统变得难以维护时，**必须**简化结构
- 当工具限制导致方案不可行时，**必须**调整方案

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `KM_ERROR_OVER_ENGINEERED` | 系统过于复杂 | 简化结构，减少层级 | 🟡 |
| `KM_WARNING_LOW_ADOPTION` | 用户未坚持使用 | 降低维护成本，增加自动化 | 🟡 |
| `KM_ERROR_TOOL_LIMIT` | 工具功能不足 | 调整方案或建议替代工具 | 🟡 |
| `KM_WARNING孤岛笔记` | 笔记无关联 | 建议添加链接和标签 | 🟢 |
| `KM_ERROR_MIGRATION_FAILED` | 迁移失败 | 分批迁移，保留原始备份 | 🔴 |

### 降级策略
- 当完整系统不可行时，先建立最小可用系统（收件箱 + 标签）
- 当工具限制时，使用通用格式（Markdown）保证可迁移性

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充
- [ ] 文件夹结构不超过 4 层

### 内容校验
- [ ] 方法论应用正确
- [ ] 工作流覆盖全生命周期
- [ ] 检索路径 ≤ 3 步
- [ ] 维护成本合理

### 合规校验
- [ ] 迁移方案已提供
- [ ] 备份策略已设计
- [ ] 人工兜底点已标注

### OVP 验证信号
- 知识检索时间减少 ≥ 50%
- 笔记复用率 ≥ 30%
- 知识关联密度 ≥ 2 个链接/篇

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "PARA 系统设计",
    "prompt": "我是项目经理，需要管理多个项目的文档和笔记",
    "context": "methodology=para, current_notes=200, tools=['Obsidian']",
    "assertions": [
      "architecture.folder_structure 包含 P/A/R/A 四层",
      "workflow.capture 覆盖项目文档来源",
      "implementation.phases 包含迁移计划"
    ],
    "expected_behavior": "设计基于 PARA 的项目知识管理系统",
    "critic_attack": "是否过度设计？是否考虑了项目生命周期？"
  },
  {
    "id": "test-002",
    "name": "Zettelkasten 实施",
    "prompt": "我想用卡片笔记法整理读书笔记，让知识产生连接",
    "context": "methodology=zettelkasten, current_notes=50",
    "assertions": [
      "architecture 包含原子笔记和链接策略",
      "workflow.organize.linking_strategy 明确",
      "maintenance 包含定期回顾机制"
    ],
    "expected_behavior": "设计 Zettelkasten 卡片笔记系统",
    "critic_attack": "链接策略是否可操作？是否会导致链接泛滥？"
  },
  {
    "id": "test-003",
    "name": "团队知识库设计",
    "prompt": "我们 10 人技术团队需要共享技术文档和最佳实践",
    "context": "methodology=hybrid, context={team_size: 10, collaboration_needs: true}",
    "assertions": [
      "architecture 包含共享层和权限设计",
      "workflow.share 包含协作规则",
      "implementation 包含培训计划"
    ],
    "expected_behavior": "设计支持团队协作的知识管理系统",
    "critic_attack": "权限设计是否合理？维护成本是否可控？"
  },
  {
    "id": "test-004",
    "name": "笔记迁移方案",
    "prompt": "我有 300 篇笔记散落在 Notion 和 Apple Notes，怎么整理？",
    "context": "methodology=para, current_notes=300, tools=['Notion', 'Apple Notes']",
    "assertions": [
      "implementation.migration_plan 分批进行",
      "保留原始备份",
      "迁移不丢失关联信息"
    ],
    "expected_behavior": "设计安全的笔记迁移方案",
    "critic_attack": "迁移是否完整？是否丢失了格式和链接？"
  },
  {
    "id": "test-005",
    "name": "极简知识系统",
    "prompt": "我不想花太多时间维护系统，能不能简单点？",
    "context": "methodology=para, current_notes=50",
    "assertions": [
      "maintenance.review_schedule 简洁",
      "workflow 每日维护 < 15 分钟",
      "structure 不超过 3 层"
    ],
    "expected_behavior": "设计极简知识管理系统，最小化维护成本",
    "critic_attack": "是否过于简单导致无法有效检索？"
  },
  {
    "id": "test-006",
    "name": "CODE 方法论应用",
    "prompt": "我想把工作中的经验和最佳实践沉淀下来",
    "context": "methodology=code, use_case='技术经验沉淀'",
    "assertions": [
      "architecture 包含 Capture/Organize/Distill/Express 四阶段",
      "workflow.capture 覆盖工作场景",
      "workflow.share 包含知识输出机制"
    ],
    "expected_behavior": "设计基于 CODE 的经验管理系统",
    "critic_attack": "是否区分了原始信息和提炼后的知识？"
  },
  {
    "id": "test-007",
    "name": "研究资料管理",
    "prompt": "我在做学术研究，需要管理大量论文和文献",
    "context": "methodology=zettelkasten, use_case='学术研究'",
    "assertions": [
      "architecture 包含文献管理机制",
      "workflow.capture 支持引用格式",
      "workflow.retrieve 支持按主题检索"
    ],
    "expected_behavior": "设计适合学术研究的知识管理系统",
    "critic_attack": "是否支持引用管理？是否便于写论文？"
  },
  {
    "id": "test-008",
    "name": "跨工具整合",
    "prompt": "我用 Obsidian 写笔记，Notion 管项目，怎么统一？",
    "context": "methodology=hybrid, tools=['Obsidian', 'Notion']",
    "assertions": [
      "workflow 包含跨工具同步策略",
      "architecture 设计工具无关的元数据",
      "提供了统一检索方案"
    ],
    "expected_behavior": "设计跨工具的知识整合方案",
    "critic_attack": "同步是否可靠？是否会产生冲突？"
  },
  {
    "id": "test-009",
    "name": "知识输出驱动",
    "prompt": "我想把笔记变成文章和演讲稿",
    "context": "methodology=code",
    "assertions": [
      "workflow.share 包含输出模板",
      "workflow.organize 支持按输出主题组织",
      "maintenance 包含输出频率目标"
    ],
    "expected_behavior": "设计以输出为驱动的知识管理系统",
    "critic_attack": "输出目标是否具体可衡量？"
  },
  {
    "id": "test-010",
    "name": "系统演进规划",
    "prompt": "我的笔记系统用了 2 年，感觉越来越乱了",
    "context": "methodology=hybrid, current_notes=500",
    "assertions": [
      "maintenance.evolution_path 明确",
      "提供了诊断当前问题的方法",
      "演进方案渐进式，不推倒重来"
    ],
    "expected_behavior": "诊断现有系统问题，设计渐进式改进方案",
    "critic_attack": "是否考虑了用户习惯？改进成本是否合理？"
  }
]
```

---

## 📝 自检清单

- [ ] Frontmatter 完整（name/description/tags）
- [ ] 输入输出 Schema 明确
- [ ] 推理链路每步有检查点
- [ ] 异常处理覆盖 ≥4 种场景
- [ ] 人工兜底点已标注
- [ ] 校验规则可执行
- [ ] Self-play 测试用例 ≥5 个
- [ ] 与至少 1 个现有 Skill 有双向链接

---

## 🔗 关联文档

- [[第二大脑 PKM 管理]] — PKM 方法论
- [[深度阅读方法论]] — 阅读与笔记
- [[第二大脑知识系统构建]] — 知识系统架构
- [[GTD执行]] — 任务管理
- [[自动化工作流]] — 流程自动化

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：PARA/CODE/Zettelkasten + 架构设计 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


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


**相关概念**：[[卢曼卡片笔记法]] · [[信息管理系统]] · [[双链笔记与概念挖坑]]


**相关概念**：[[三大Agent-Skills框架方法论对比]]

---



## 🔄 执行流程

1. **准备阶段**：收集输入数据，确认参数完整性
2. **分析阶段**：对输入进行分析处理，识别关键信息
3. **执行阶段**：按照标准流程执行操作
4. **验证阶段**：检查输出是否符合预期
5. **输出阶段**：生成最终结果并记录日志


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
