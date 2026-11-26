---
name: uskill-productivity-draft-patent-application
description: "让productivity draft patent application变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-draft-patent-application.md"
  original_id: "SKL-6908"
  version: "3.0.0"
  trust: untrusted
---

# productivity draft patent application

# Draft AI/Software Patent Application

## 🎯 目标
> 建立一套专门针对 AI 算法、软件架构等复杂技术创新的标准化流程，高效、精准地完成高价值专利申请文件撰写，最大化保护范围和授权成功率。将单个专利申请文件撰写周期缩短 60%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `technical_disclosure` | string | ✅ | 技术交底书：算法流程、系统架构、数据流等详细描述 |
| `invention_problem` | string | ✅ | 本发明要解决的技术问题 |
| `prior_art_hints` | list | ❌ | 已知的现有技术或相关专利线索 |
| `protection_scope` | object | ❌ | 期望的保护范围偏好（方法/系统/介质） |
| `jurisdiction` | list | ❌ | 目标申请国家/地区，默认 ["CN"] |
| `deadline` | string | ❌ | 截止日期 |

## 📤 输出

```json
{
  "innovation_points": [
    {
      "point": "string — 核心创新点描述",
      "technical_problem": "string — 解决的技术问题",
      "beneficial_effect": "string — 有益效果"
    }
  ],
  "prior_art_report": {
    "search_strategy": {
      "keywords_cn": ["string"],
      "keywords_en": ["string"],
      "ipc_cpc_codes": ["string"],
      "boolean_queries": ["string"]
    },
    "references": [
      {
        "id": "string",
        "title": "string",
        "source": "string",
        "relevance": "string"
      }
    ],
    "patentability_analysis": {
      "novelty": "string — 新颖性分析",
      "inventive_step": "string — 创造性分析",
      "distinguishing_features": ["string"]
    }
  },
  "claims": {
    "independent_claims": [
      {
        "type": "method | system | medium",
        "text": "string — 权利要求全文"
      }
    ],
    "dependent_claims": [
      {
        "refers_to": "string — 引用的权利要求编号",
        "text": "string — 权利要求全文"
      }
    ]
  },
  "specification": {
    "technical_field": "string",
    "background_art": "string",
    "invention_summary": "string",
    "detailed_description": "string — 含至少一个完整实施例",
    "beneficial_effects": "string"
  },
  "abstract": "string — 300字以内",
  "drawings_description": [
    {
      "figure_id": "string",
      "description": "string"
    }
  ],
  "review_checklist": {
    "terminology_consistent": "boolean",
    "figure_marks_complete": "boolean",
    "format_compliant": "boolean",
    "issues": ["string"]
  }
}
```

## 📋 执行步骤

1. **技术交底与创新点挖掘** — 详细描述技术方案（算法流程、系统架构、数据流），明确解决的技术问题，提炼 3-5 个可能具有新颖性和创造性的核心技术特征
2. **AI 辅助现有技术检索与专利性分析** — 基于创新点制定多维度检索策略（关键词+IPC/CPC 分类号+布尔检索式），检索中美欧等主要专利局数据库，找出 3-5 篇最相关对比文件，逐一对比并论证创造性
3. **权利要求布局与迭代** — 围绕最小创新点撰写独立权利要求（方法/系统/介质多类型），层次化布局从属权利要求（≥5 项），针对假想侵权场景和规避设计反复优化
4. **说明书与附图撰写** — 围绕权利要求书撰写说明书，包含至少一个完整可复现的实施例，确保每个技术特征在说明书中有对应描述，绘制流程图/架构图作为附图
5. **最终审核与提交** — 交叉验证权利要求与现有技术，全文术语一致性检查，附图标记完整性检查，格式合规性检查，最终通读确认技术逻辑和法律文本

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `technical_disclosure` 信息不足 | 返回所需信息清单，请求补充算法细节和架构图 |
| 检索发现高度相似的现有技术 | 重新评估创新点，调整保护策略或建议放弃申请 |
| 权利要求保护范围过窄 | 回到创新点挖掘，寻找更上位的抽象描述 |
| 说明书无法支撑权利要求 | 补充实施例细节，或回退权利要求范围 |
| AI 生成内容存在事实错误 | 人工逐条验证后修正，标记为待审 |

## ✅ 自检清单

- [ ] 技术问题足够具体，非泛泛而谈
- [ ] 核心创新点与现有技术有清晰可描述的区别
- [ ] 检索覆盖中美欧等主要专利局数据
- [ ] 专利性分析客观，非一厢情愿
- [ ] 独立权利要求包含最少必要技术特征
- [ ] 从属权利要求对独立权利要求形成有效层次限定
- [ ] 权利要求书覆盖方法、系统、介质等多种类型
- [ ] 说明书至少描述一个完整可复现的实施例
- [ ] 权利要求中每个技术术语在说明书中有定义
- [ ] 全文术语统一，附图标记完整
- [ ] 符合目标专利局的官方格式要求


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
| 2026-05-08 | 1.0.0 | 初始版本，从 SOP-07 转化 |

---
**相关笔记**：[[默读式会议]] [[P4 Agentic 金融]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "R

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
