---
name: uskill-creative-copywriting
description: "让文案写作变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-copywriting.md"
  original_id: "SKL-5608"
  version: "3.0.0"
  trust: untrusted
---

# 文案写作

description: |
  当用户需要撰写营销文案、产品描述、广告创意、落地页时使用此 Skill。
  触发词包括：'文案'、'广告词'、'营销文案'、'产品描述'、'CTA'、
  '标题技巧'、'落地页'。
  不适用于演讲稿（使用演讲节奏控制）。当需要书面营销内容时优先使用。

---

# uSkill-608: 文案写作

## 🎯 目标

> 运用 AIDA/PAS/FAB 经典框架，创作高转化率的营销文案。

**核心价值**：好文案能驱动行动，差文案只能自说自话。

**适用场景**：
- 营销文案
- 产品描述
- 广告创意
- 落地页
- 邮件营销
- 社交媒体

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `product` | `string` | ✅ | — | 产品/服务描述 |
| `audience` | `string` | ✅ | — | 目标受众 |
| `goal` | `enum` | ✅ | — | `awareness` / `consideration` / `conversion` / `retention` |
| `medium` | `enum` | ❌ | `ad` | `ad` / `landing` / `email` / `social` / `product` |
| `tone` | `enum` | ❌ | `professional` | `professional` / `casual` / `humorous` / `urgent` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话文案建议",
  "copy_id": "CPY-YYYY-MMDD-NNN",

  "framework_selection": {
    "primary": "string",
    "secondary": "string",
    "rationale": "string"
  },

  "headline_options": [
    {
      "headline": "string",
      "type": "string",
      "score": "number"
    }
  ],

  "body_copy": {
    "opening": "string",
    "problem": "string",
    "solution": "string",
    "benefits": ["string"],
    "proof": ["string"],
    "closing": "string"
  },

  "cta_design": {
    "primary_cta": "string",
    "secondary_cta": "string",
    "urgency_element": "string",
    "placement": "string"
  },

  "copy_variations": [
    {
      "variant": "string",
      "tone": "string",
      "text": "string",
      "target_segment": "string"
    }
  ],

  "optimization_tips": {
    "a_b_test_suggestions": ["string"],
    "common_mistakes": ["string"],
    "improvement_areas": ["string"]
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

### Step 1: 框架选择

- **输入**：`product` + `audience` + `goal`
- **动作**：
  1. 分析产品特点
  2. 选择最适合的写作框架
  3. 确定写作策略
- **输出**：`framework_selection`
- **框架选择指南**：

| 框架 | 结构 | 适用场景 |
|------|------|----------|
| AIDA | 注意-兴趣-欲望-行动 | 广告、落地页 |
| PAS | 问题-激化-解决方案 | 痛点明确的产品 |
| FAB | 特性-优势-利益 | 技术产品、B2B |
| Before-After-Bridge | 之前-之后-桥梁 | 转化类文案 |
| PASTOR | 问题-放大-故事-转变-结果-响应 | 长文案、销售信 |

**分支条件**：
- 若 `goal=awareness` → 优先使用 AIDA
- 若 `goal=consideration` → 优先使用 PAS 或 FAB
- 若 `goal=conversion` → 优先使用 Before-After-Bridge
- 若 `goal=retention` → 优先使用 PASTOR

### Step 2: 标题创作

- **输入**：`framework_selection` + `audience`
- **动作**：
  1. 创作多个标题选项
  2. 评估标题吸引力
  3. 选择最佳标题
- **输出**：`headline_options`
- **标题技巧库**：

| 类型 | 结构 | 示例 |
|------|------|------|
| 数字型 | 数字+好处 | "5个方法让你..."
| 提问型 | 问题+答案 | "你知道...吗？" |
| 如何型 | 如何+结果 | "如何在30天内..." |
| 秘密型 | 秘密+揭示 | "专家不想让你知道的..." |
| 对比型 | 对比+结果 | "别再...试试这个" |
| 证据型 | 证据+结论 | "10000人验证的..." |

**分支条件**：
- 若 `medium=ad` → 使用短标题（<10字）
- 若 `medium=landing` → 使用长标题（15-25字）
- 若 `medium=email` → 使用疑问型标题
- 若 `medium=social` → 使用数字型或对比型
- 若 `audience=年轻人` → 使用幽默或反叛型
- 若 `audience=专业人士` → 使用数据型或证据型

### Step 3: 正文撰写

- **输入**：`framework_selection` + `headline_options`
- **动作**：
  1. 撰写开场、问题、解决方案
  2. 列出利益点和证据
  3. 设计结尾
- **输出**：`body_copy`
- **正文结构**：

| 部分 | 目的 | 长度建议 |
|------|------|----------|
| 开场 | 吸引注意力 | 1-2句 |
| 问题 | 引发共鸣 | 2-3句 |
| 解决方案 | 提供方案 | 2-3句 |
| 利益点 | 强调价值 | 3-5点 |
| 证据 | 建立信任 | 2-3个 |
| 结尾 | 推动行动 | 1-2句 |

**分支条件**：
- 若 `medium=ad` → 正文精简，重点突出
- 若 `medium=landing` → 正文详细，包含完整论证
- 若 `medium=email` → 正文分段，增加可读性
- 若 `medium=social` → 正文简短，突出核心
- 若 `medium=product` → 正文客观，突出特性

### Step 4: CTA 设计

- **输入**：`goal` + `medium`
- **动作**：
  1. 设计主CTA和备选CTA
  2. 添加紧迫感元素
  3. 确定CTA位置
- **输出**：`cta_design`
- **CTA 设计原则**：

| 原则 | 说明 | 示例 |
|------|------|------|
| 明确 | 行动具体 | "立即购买" 而非 "了解更多" |
| 紧迫 | 时间限制 | "限时优惠，仅剩3天" |
| 价值 | 强调好处 | "免费获得..." |
| 低门槛 | 降低风险 | "无需信用卡" |
| 社会证明 | 从众心理 | "已有10000人加入" |

**分支条件**：
- 若 `goal=awareness` → CTA 为 "了解更多"
- 若 `goal=consideration` → CTA 为 "免费试用"
- 若 `goal=conversion` → CTA 为 "立即购买"
- 若 `goal=retention` → CTA 为 "续费优惠"

### Step 5: 文案变体与优化

- **输入**：所有前序输出
- **动作**：
  1. 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
