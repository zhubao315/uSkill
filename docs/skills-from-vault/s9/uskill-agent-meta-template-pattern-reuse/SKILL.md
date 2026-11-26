---
name: uskill-agent-meta-template-pattern-reuse
description: "让meta template pattern reuse变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-meta-template-pattern-reuse.md"
  original_id: "SKL-5064"
  version: "3.0.0"
  trust: untrusted
---

# meta template pattern reuse

# Apply Template-Driven Execution

## 🎯 目标
> 运用「模板即套路」的认知模型，将重复性任务和决策场景抽象为可复用的模板/套路，实现「站在前人肩膀上」的高效执行——在节约认知资源的同时避免情绪化决策，找到理性分析与直觉反应之间的最优执行路径。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `task_description` | string | ✅ | 需要执行的任务或面临决策的场景描述 |
| `task_type` | enum | ✅ | 任务类型：`decision`（决策判断）/ `creation`（内容创作）/ `process`（流程执行）/ `communication`（沟通表达）/ `analysis`（分析推理） |
| `available_templates` | array | ❌ | 用户已有的模板/套路列表（如有），每项含 name + description |
| `urgency` | enum | ❌ | 紧急程度：`immediate`（立即执行）/ `planned`（计划中）/ `recurring`（反复出现），默认 `planned` |
| `experience_level` | enum | ❌ | 在该类任务上的经验水平：`novice` / `intermediate` / `expert`，默认 `intermediate` |
| `customization_need` | enum | ❌ | 模板适配需求：`strict`（严格套用）/ `adapt`（适度调整）/ `inspire`（仅取思路），默认 `adapt` |

## 📤 输出

```json
{
  "task_analysis": {
    "task_type": "string — 任务类型识别",
    "complexity": "string — 简单/中等/复杂",
    "is_template_suitable": "boolean — 该任务是否适合使用模板",
    "reasoning": "string — 为什么适合/不适合模板化"
  },
  "template_recommendation": {
    "recommended_template": {
      "name": "string — 推荐模板名称",
      "source": "string — 模板来源（行业惯例/历史经验/最佳实践）",
      "description": "string — 模板概述",
      "steps": ["string — 模板执行步骤"],
      "success_criteria": ["string — 使用该模板的成功标志"]
    },
    "alternative_templates": [
      {
        "name": "string — 备选模板名称",
        "scenario": "string — 什么情况下选择此备选"
      }
    ],
    "customization_guide": {
      "fixed_parts": ["string — 必须保留的模板要素"],
      "flexible_parts": ["string — 可根据实际情况调整的部分"],
      "additions_needed": ["string — 需要额外补充的内容"]
    }
  },
  "execution_plan": {
    "preparation": ["string — 执行前准备事项"],
    "main_execution": [
      {
        "step": "number",
        "action": "string — 具体动作",
        "template_element": "string — 对应模板哪个环节",
        "customization": "string — 本次需要的定制化调整"
      }
    ],
    "quality_check": ["string — 执行质量检查点"]
  },
  "cognitive_positioning": {
    "system1_system2_balance": "string — 本次执行中直觉与理性的分工建议",
    "template_risks": ["string — 机械套用模板可能导致的问题"],
    "escape_conditions": ["string — 什么情况下应该跳出模板、灵活应变"]
  },
  "template_evolution": {
    "should_save_as_template": "boolean — 本次执行结果是否值得沉淀为新模板",
    "improvement_suggestions": ["string — 基于本次经验对模板的改进建议"],
    "template_name_suggestion": "string — 如值得沉淀，建议的模板名称"
  }
}
```

## 📋 执行步骤

1. **任务解构与分类** — 分析 `task_description`，识别任务本质：
   - 判断任务类型（决策/创作/流程/沟通/分析）
   - 评估复杂度：涉及多少变量？是否有明确的成功标准？
   - 判断模板适用性：重复出现、有规律可循、存在行业惯例的任务最适合模板化

2. **模板匹配与推荐** — 在已有模板（`available_templates`）和通用知识库中寻找最佳匹配：
   - 如用户已有模板：评估匹配度，推荐最佳选项
   - 如无现成模板：基于任务类型推荐行业通用模板或历史最佳实践
   - 推荐原则：**套路是前人经验的精华，不是死板的教条**
   - 为 `novice` 用户推荐更详细的步骤模板，为 `expert` 用户推荐检查清单式模板

3. **模板定制化适配** — 根据 `customization_need` 调整模板：
   - **固定部分**：模板中不可省略的核心要素（如金字塔原理的"结论先行"）
   - **灵活部分**：可根据具体情况增删的环节
   - **额外补充**：当前场景特有的内容，需要从模板之外引入
   - 参考卡尼曼双系统理论：模板化的部分由"系统1"快速处理，需要创意和判断的部分留给"系统2"

4. **执行计划编制** — 将模板转化为具体可执行的行动步骤：
   - 每一步标注对应模板的哪个环节
   - 明确每一步的定制化调整内容
   - 设置质量检查点，防止机械套用

5. **认知定位与风险提示** — 明确模板使用的边界：
   - **直觉与理性的分工**：哪些环节可以快速执行（套路成熟），哪些需要深思熟虑（场景特殊）
   - **套用风险**：提醒可能的"教条主义"陷阱——模板是工具不是目的
   - **跳出条件**：明确什么情况下应该放弃模板、灵活应变

6. **模板进化评估** — 执行后考虑模板的迭代：
   - 本次执行是否有值得沉淀为新模板的模式？
   - 现有模板是否需要根据本次经验优化？
   - **核心理念**：好的模板是活的，随经验积累不断进化

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| 任务高度创新/前所未有，无模板可参考 | 标注"首次执行"，建议以最佳实践为灵感创建初版模板，执行后沉淀 |
| 用户过度依赖模板，忽略了场景特殊性 | 强制触发"跳出模板"检查，列出当前场景与模板假设的差异 |
| 用户已有过多模板，选择困难 | 按匹配度排序 Top 3，附对比表（适用场景/复杂度/成功率） |
| 任务紧急（`urgency=immediate`），无暇定制 | 推荐"最小可行模板"——提取核心 3-5 步快速执行，事后补充完善 |
| 模板执行结果不佳 | 分析失败原因（模板本身缺陷 vs 执行偏差 vs 场景不适配），给出修正方向 |

## ✅ 自检清单

- [ ] 任务已正确分类，模板推荐与任务类型匹配
- [ ] 推荐的模板有明确来源和成功标准，非凭空编造
- [ ] 定制化适配区分了"固定部分"和"灵活部分"
- [ ] 执行计划每一步都标注了对应的模板环节
- [ ] 已提示模板套用的潜在风险和跳出条件
- [ ] 考虑了认知效率：哪些环节快速执行，哪些需要深思
- [ ] 包含模板进化评估，支持持续迭代
- [ ] 未将模板当作万能药，承认了模板的适用边界


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
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
