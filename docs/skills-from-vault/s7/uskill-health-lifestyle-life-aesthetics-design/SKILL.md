---
name: uskill-health-lifestyle-life-aesthetics-design
description: "lifestyle life aesthetics design"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-lifestyle-life-aesthetics-design.md"
  original_id: "SKL-6818"
  version: ""
  trust: untrusted
---

# lifestyle life aesthetics design

name: "health-lifestyle-life-aesthetics-design"
version: "3.0.0"
vibe: "让lifestyle life aesthetics design变成可执行的行动，而非停留在想法。"
emoji: "🏃"
domain: "health"

# Life Aesthetics Design & Creative Implementation

## 🎯 目标

> AI增强的生活美学创意实现流水线——从意图定义、灵感探索、方案构思到落地执行与体验迭代，将从概念到完整设计方案的时间缩短70%。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 | 默认值 |
|------|------|------|------|--------|
| `project_type` | enum | ✅ | 项目类型：`space_renovation` / `event_planning` / `personal_styling` / `other` | — |
| `core_intent` | string | ✅ | 核心意图与功能目标（如"将书房改造为心流空间"） | — |
| `emotion_keywords` | string[] | ✅ | 期望的情感基调关键词（3-5个，如"宁静、专注、自然"） | — |
| `constraints` | object | ❌ | 约束条件（预算、时间、空间尺寸、偏好等） | `{}` |
| `inspiration_refs` | string[] | ❌ | 参考图片/风格链接 | `[]` |
| `output_format` | enum | ❌ | 输出格式：`mood_board` / `full_plan` / `action_plan` / `all` | `"all"` |

## 📤 输出

```json
{
  "design_intent": {
    "core_function": "核心功能定义",
    "emotion_tone": ["情感基调关键词"],
    "constraints": {
      "budget": "预算范围",
      "timeline": "时间周期",
      "space_size": "空间尺寸",
      "preferences": "特殊偏好"
    }
  },
  "mood_board": {
    "style_directions": [
      {
        "style_name": "风格名称",
        "description": "风格描述",
        "color_palette": ["#hex1", "#hex2", "#hex3"],
        "key_elements": ["核心元素"],
        "feeling": "置身其中的感受描述"
      }
    ],
    "recommended_style": "推荐风格"
  },
  "detailed_plan": {
    "space_layout": "空间布局方案",
    "color_material": "色彩与材质方案",
    "furniture_list": [
      {
        "item": "物品名称",
        "reason": "推荐理由",
        "estimated_price": "预估价格",
        "link": "购买链接"
      }
    ],
    "decorative_highlights": ["画龙点睛的装饰建议"]
  },
  "action_plan": {
    "tasks": [
      {
        "task": "任务描述",
        "owner": "责任人",
        "estimated_hours": 0,
        "dependencies": ["前置任务"],
        "status": "pending"
      }
    ],
    "budget_breakdown": {
      "total_estimated": 0,
      "items": []
    }
  },
  "visual_prototypes": {
    "ai_generated_prompts": ["Midjourney/SD提示词"],
    "sketch_descriptions": "草图描述"
  },
  "review_checklist": []
}
```

## 📋 执行步骤

### Step 1: 定义意图 (Define Intent)

**动作：**
- 清晰定义本次设计要实现的核心功能和目标（如"将书房改造为既能高效工作又能沉浸阅读的心流空间"）
- 定义希望空间/体验带来的核心情感：宁静、专注、温暖、高级感等3-5个关键词
- 设定约束条件：预算上限、时间周期、空间尺寸、家庭成员偏好

**战略考量：**
设计始于意图，而非风格。首先要明确"为什么做"和"希望达到什么感受"，这是所有后续创意的原点。好的意图定义能将设计效率提升数倍。

**质量检查点：**
- [ ] 设计目标是否具体、可衡量？
- [ ] 情感基调是否清晰？（3-5个关键词）
- [ ] 约束条件是否已明确列出？

**AI提示词：**

```
你是一位生活美学顾问。我想要进行一个生活美学项目，请帮我梳理和深化设计意图。

【项目类型】
{project_type}

【我的初步想法】
{raw_intent}

请帮我：
1. 将我的模糊想法提炼为一个清晰的、可执行的设计目标
2. 根据我的描述，推荐3-5个情感基调关键词
3. 提醒我可能遗漏的约束条件（预算、时间、空间、家庭成员等）
4. 用一句话概括这个项目的"设计宣言"

注意：保持我的核心意图不变，只是帮助我更清晰地表达。
```

---

### Step 2: 探索灵感 (Explore & Envision)

**动作：**
- 基于情感基调和功能目标，进行关键词联想（如"宁静"→"侘寂、冥想、森林、流水"）
- AI扮演"创意总监"，根据关键词生成3种不同风格方向的视觉参考
- 使用AI绘画工具（Midjourney/SD）生成概念性空间氛围图，快速探索视觉可能性
- 确定主导的色彩体系和关键材质

**战略考量：**
让AI成为灵感的放大器，在短时间内探索传统方法难以触及的风格组合与视觉创意，打破思维定式。至少收集3种不同风格方向的参考。

**质量检查点：**
- [ ] 是否收集了至少3种不同风格方向的视觉参考？
- [ ] 是否已确定主导的色彩体系和关键材质？
- [ ] AI生成的灵感是否与我的情感基调一致？

**AI提示词（风格探索）：**

```
你是一位顶尖的生活美学杂志《Kinfolk》的创意总监。
我希望为一个{space_type}进行设计，我期望的情感基调是"{emotion_keywords}"。

请为我：
1. 推荐3种符合该基调的设计风格（如侘寂风、现代有机风、日式极简），并简要描述其核心元素
2. 为每种风格提供一个包含6-8种颜色的色彩板（含HEX色值）
3. 生成一段富有感染力的文字，描述置身于这种空间中的感受
4. 推荐3-5种关键材质（如原木、亚麻、黄铜等）
```

**AI提示词（视觉原型）：**

```
（适用于Midjourney/SD）
A photorealistic interior design photo of a {space_type}, 
style of {style_name}, main color palette of {colors}, 
key elements include {elements}, 
atmosphere is {atmosphere_keywords}. 
--ar 16:9 --style raw
```

---

### Step 3: 构思方案 (Enact & Prototype)

**动作：**
- 进行空间布局规划：动线设计、功能分区，绘制平面布局草图
- 确定具体的色彩板（Color Palette）、家具、灯具、纺织品和装饰品
- AI扮演"顶级室内设计师"，生成详细的设计方案建议，包含具体物品搭配和理由
- 使用Figma等工具将设计方案进行可视化拼贴，形成视觉原型

**战略考量：**
此步骤将灵感"落地"为可执行的方案。运用系统思维确保空间布局兼顾美观与实用，运用摄影构图知识预演最终视觉效果。每个元素都应服务于第一步定义的情感基调。

**质量检查点：**
- [ ] 设计方案中的各元素是否和谐统一，服务于情感基调？
- [ ] 空间布局是否兼顾了美观与实用？
- [ ] 是否有明确的物品清单（含名称、链接、预算）？

**AI提示词：**

```
你是一位米兰的顶级室内设计师，擅长将功能与美学完美融合。

【已确定的信息】
设计风格：{style_name}
核心元素：{key_elements}
空间尺寸：{space_size}
功能需求：{function

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
