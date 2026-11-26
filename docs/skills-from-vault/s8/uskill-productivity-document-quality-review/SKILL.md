---
name: uskill-productivity-document-quality-review
description: "让productivity document quality review变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S8-效率与工具/uSkill-productivity-document-quality-review.md"
  original_id: "SKL-5062"
  version: "3.0.0"
  trust: untrusted
---

# productivity document quality review

# Review Document Quality with Writing Checklist

## 🎯 目标
> 运用 Why-Who-How-What 四维文档质量检查框架，对用户提供的文档进行系统性审查，输出结构化评审意见和具体改进建议，适用于方案文档、技术文档、汇报材料、产品文档等各类书面内容。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `document` | string | ✅ | 待审查的文档内容 |
| `doc_type` | enum | ✅ | 文档类型：`proposal`（方案/建议书）/ `report`（汇报/总结）/ `technical`（技术文档）/ `product`（产品文档）/ `general`（通用） |
| `audience` | string | ❌ | 目标读者描述，如"CEO""跨部门协作者""技术团队"，影响评审侧重点 |
| `review_focus` | array | ❌ | 重点关注维度，可选：`why`（目标清晰度）/ `who`（读者适配）/ `how`（结构逻辑）/ `what`（内容质量）/ `format`（格式规范），默认全部 |
| `strictness` | enum | ❌ | 评审严格度：`gentle`（温和建议）/ `standard`（标准评审）/ `strict`（严格审查），默认 `standard` |

## 📤 输出

```json
{
  "overall_score": {
    "total": "number — 总分 1-10",
    "breakdown": {
      "why_purpose_clarity": "number — 目标清晰度 1-10",
      "who_reader_fit": "number — 读者适配度 1-10",
      "how_structure": "number — 结构逻辑 1-10",
      "what_content_quality": "number — 内容质量 1-10",
      "format_polish": "number — 格式规范 1-10"
    }
  },
  "checklist_results": {
    "why_section": {
      "core_problem_clear": {
        "pass": "boolean",
        "comment": "string — 核心问题是否一句话说清"
      },
      "key_points_identified": {
        "pass": "boolean",
        "comment": "string — 核心观点是否明确，不超过3个"
      }
    },
    "who_section": {
      "audience_identified": {
        "pass": "boolean",
        "comment": "string — 目标读者是否明确"
      },
      "reader_needs_addressed": {
        "pass": "boolean",
        "comment": "string — 是否针对不同角色的关注点"
      },
      "background_context_provided": {
        "pass": "boolean",
        "comment": "string — 背景信息是否充分"
      }
    },
    "how_section": {
      "structure_clear": {
        "pass": "boolean",
        "comment": "string — 是否可参考金字塔原理"
      },
      "conclusion_first": {
        "pass": "boolean",
        "comment": "string — 关键结论是否前置"
      },
      "toc_navigable": {
        "pass": "boolean",
        "comment": "string — 目录是否可快速定位重点"
      }
    },
    "what_section": {
      "key_points_highlighted": {
        "pass": "boolean",
        "comment": "string — 段落要点是否醒目"
      },
      "charts_where_needed": {
        "pass": "boolean",
        "comment": "string — 复杂信息是否有图表辅助"
      },
      "redundancy_removed": {
        "pass": "boolean",
        "comment": "string — 是否已精简读者已知信息"
      },
      "points_consolidated": {
        "pass": "boolean",
        "comment": "string — 要点是否控制在7±2条"
      },
      "language_accessible": {
        "pass": "boolean",
        "comment": "string — 是否避免了不必要的黑话"
      },
      "reader_questions_anticipated": {
        "pass": "boolean",
        "comment": "string — 是否预见并回答了读者疑问"
      }
    },
    "format_section": {
      "alignment_ok": {
        "pass": "boolean",
        "comment": "string — 标题/正文/图表对齐"
      },
      "typo_free": {
        "pass": "boolean",
        "comment": "string — 错别字检查"
      },
      "punctuation_consistent": {
        "pass": "boolean",
        "comment": "string — 标点符号和单位统一"
      }
    }
  },
  "priority_fixes": [
    {
      "issue": "string — 问题描述",
      "severity": "critical / major / minor",
      "location": "string — 问题所在段落/位置",
      "suggestion": "string — 具体修改建议",
      "example": "string — 修改示例（可选）"
    }
  ],
  "iteration_advice": {
    "peer_review_suggestion": "string — 是否建议先给同事预览",
    "reference_docs": "string — 可参考的优秀文档方向",
    "top_3_improvements": ["string — 最值得做的3项改进"]
  }
}
```

## 📋 执行步骤

1. **文档预读** — 快速通读全文，建立整体印象：
   - 识别文档类型和目的
   - 判断目标读者（若有 `audience` 参数则以此为准）
   - 形成初步结构认知

2. **Why 维度审查 — 目标清晰度**：
   - 核心问题是否一句话能说清？
   - 核心观点/建议是否明确？不超过3个要点？
   - 读者读完能否回答"所以呢？"

3. **Who 维度审查 — 读者适配度**：
   - 目标读者是否明确？
   - 是否为不同角色（决策者/协作者/信息同步对象）提供了对应信息？
   - 背景信息是否充分，新读者能否理解？
   - 专业术语使用是否匹配读者水平？

4. **How 维度审查 — 结构逻辑**：
   - 整体结构是否清晰？（参考金字塔原理：结论先行，以上统下）
   - 关键结论是否前置？
   - 目录是否一目了然、可快速定位？
   - 段落间逻辑是否连贯（因果/并列/递进）？

5. **What 维度审查 — 内容质量**：
   - **突出重点**：关键结论前置？段落要点醒目？复杂信息有图表？
   - **精简内容**：读者已知信息是否可删减？要点控制在7±2条？去掉该部分是否造成信息减损？（不是肯定Yes就是肯定No）
   - **清晰表达*

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
