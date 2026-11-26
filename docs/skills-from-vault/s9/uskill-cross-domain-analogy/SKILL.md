---
name: uskill-cross-domain-analogy
description: "让跨领域类比 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-cross-domain-analogy.md"
  original_id: "SKL-6905"
  version: "3.0.0"
  trust: untrusted
---

# 跨领域类比 Agent — 实施手册

description: |
  当用户需要将A领域的模型/框架迁移到B领域解决问题时使用此 Skill。
  触发词包括：'跨领域类比'、'知识迁移'、'类比推理'、'举一反三'、'模型迁移'。
  当用户说"这个思路能不能用在X上"、"Y领域有什么类似的模式"，即使未直接说"类比"，也应使用此 Skill。
  不适用于完全无关领域的强行类比。需确保源与目标存在结构性相似。

---

# 🔄 uSkill-303: 跨领域类比

## 🎯 目标

> 将A领域的模型/框架迁移到B领域解决问题，发现深层结构相似性，生成可执行的迁移建议。

**核心价值**：打破领域壁垒，用已知领域的成熟模型解决未知领域的新问题。

**适用场景**：
- 技术架构设计（借用生物进化、城市规划等模型）
- 投资策略构建（借用军事、博弈论等框架）
- 产品设计灵感（借用自然界、建筑学等原理）
- 组织管理优化（借用分布式系统、生态系统等模型）
- 个人成长方法（借用工程学、运动科学等思维）

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `source_domain` | `string` | ✅ | — | 源领域名称（如"生物进化"） |
| `target_domain` | `string` | ✅ | — | 目标领域名称（如"创业公司管理"） |
| `problem` | `string` | ✅ | — | 需要在目标领域解决的具体问题 |
| `source_model` | `string` | ❌ | — | 源领域中已知的特定模型/框架 |
| `depth` | `enum` | ❌ | `standard` | `quick`(核心映射) / `standard`(详细映射+建议) / `deep`(含局限性分析) |

**输入约束**：
- `source_domain` 和 `target_domain` 不能相同
- `problem` 应明确描述目标领域的具体挑战
- `depth=deep` 时建议提供源领域的详细模型描述

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话类比结论",
  "analogy_id": "ANL-YYYY-MMDD-NNN",
  "source_model": {
    "domain": "string",
    "model_name": "string",
    "core_logic": "string",
    "key_elements": ["string"],
    "relationships": "string"
  },
  "target_mapping": {
    "domain": "string",
    "problem": "string",
    "mapped_elements": [
      {
        "source_concept": "string",
        "target_counterpart": "string",
        "mapping_strength": "strong|moderate|weak",
        "explanation": "string"
      }
    ]
  },
  "migration_recommendations": [
    {
      "priority": "P0|P1|P2",
      "action": "string",
      "source_principle": "string",
      "expected_outcome": "string"
    }
  ],
  "limitations": ["string"],
  "confidence_level": "high|medium|low"
}
```

---

## 🔄 执行流程

```
1. [输入解析] → 理解源领域模型和目标领域问题
   → 判断条件：source_model 是否提供？
     → 是：直接使用指定模型
     → 否：从 source_domain 中识别最相关的模型
   → 判断条件：source_domain == target_domain？
     → 是：输出错误「源领域和目标领域相同，无需类比」
     → 否：继续

2. [结构提取] → 从源领域提取核心模型结构
   → 识别核心概念（实体/组件）
   → 识别关系模式（因果/反馈/层次）
   → 识别动态机制（演化/平衡/突变）
   → 产出：源领域结构化模型

3. [映射搜索] → 在目标领域寻找对应结构
   → 逐概念映射：源概念 → 目标对应物
   → 映射强度评估：strong(直接对应) / moderate(部分对应) / weak(勉强对应)
   → 判断条件：strong+moderate 映射占比 >= 60%？
     → 是：映射有效，继续
     → 否：映射薄弱，输出警告「类比结构相似性不足」

4. [迁移建议] → 基于映射关系生成可执行建议
   → 每条建议绑定源领域原理
   → 建议应具体到目标领域的操作步骤
   → 按优先级排序

5. [局限性分析] → 标注类比的边界（depth=deep时）
   → 哪些概念没有对应物？
   → 哪些映射可能误导？
   → 源领域的哪些特性在目标领域不适用？

6. [输出报告] → 生成结构化类比报告
```

---

## 📝 Prompt 模板

### 标准类比 Prompt

```
你是跨领域类比Agent。请进行跨域类比分析。

【输入】
- 源领域：{source_domain}
- 目标领域：{target_domain}
- 问题：{problem}
- 分析深度：{depth}

【类比分析步骤】
1. 提取源领域核心模型：识别关键概念、关系模式、动态机制
2. 寻找目标领域对应结构：逐概念映射，评估映射强度
3. 生成迁移建议：每条绑定源领域原理
4. 分析局限性：标注类比边界（deep模式）

【输出要求】
- 映射强度必须标注（strong/moderate/weak）
- 迁移建议必须具体可执行
- 局限性必须明确说明
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 源领域=目标领域 | 输出错误，终止分析 | — |
| 映射强度普遍偏低 | 输出警告，标注类比可能不适用 | 仅输出核心映射+局限性 |
| 源模型不明确 | 从源领域自动识别最相关模型 | 标注模型选择可能不最优 |
| 目标问题过于模糊 | 请求补充具体问题描述 | 基于领域通用问题进行类比 |

---

## ✅ 质量自检

- [ ] 源领域结构提取完整（概念+关系+机制）
- [ ] 映射关系逐一标注强度
- [ ] 迁移建议绑定源领域原理
- [ ] 局限性明确说明（deep模式）
- [ ] 无强行类比（弱映射占比不过高）

---

## 💡 使用示例

### 示例 1：生物进化 → 创业管理

**输入**：
```json
{
  "source_domain": "生物进化",
  "target_domain": "创业公司管理",
  "problem": "如何在资源有限的情况下让团队持续创新",
  "depth": "standard"
}
```

**输出**：
```json
{
  "source_model": {"model_name": "自然选择", "core_logic": "变异+选择+遗传", "key_elements": ["变异", "选择压力", "适应度", "遗传"]},
  "target_mapping": {
    "mapped_elements": [
      {"source_concept": "变异", "target_counterpart": "创新实验", "mapping_strength": "strong", "explanation": "生物变异=团队尝试新方案"},
      {"source_concept": "选择压力", "target_counterpart": "市场反馈", "mapping_strength": "strong", "explanation": "自然选择=用户/市场筛选"},
      {"source_concept": "适应度", "target_counterpart": "产品市场匹配度", "mapping_strength": "moderate", "explanation": "适应度=PMF程度"}
    ]
  },
  "migration_recommendations": [
    {"priority": "P0", "action": "鼓励'变异'：每月留出20%时间做创新实验"

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
