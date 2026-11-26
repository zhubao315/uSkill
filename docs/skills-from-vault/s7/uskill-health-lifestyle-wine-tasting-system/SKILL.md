---
name: uskill-health-lifestyle-wine-tasting-system
description: "让lifestyle wine tasting system变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S7-健康与生活/uSkill-health-lifestyle-wine-tasting-system.md"
  original_id: "SKL-5131"
  version: "3.0.0"
  trust: untrusted
---

# lifestyle wine tasting system

# Wine Tasting System

> **角色**: 品酒师 | **核心工具**: AI大模型, 品鉴记录系统, 风味轮 | **效率目标**: 系统化红酒品鉴方法，建立个人风味记忆库

## 🎯 目标

构建**系统化的红酒品鉴方法论**，掌握WSET/ISO品鉴体系，从外观、香气、口感、余味四个维度建立标准化的品鉴流程和评分体系。

**适用场景**:
1. **系统学习品鉴** — 从零开始学习红酒品鉴的系统方法
2. **品鉴活动主持** — 组织和主持专业的红酒品鉴会
3. **选购决策辅助** — 通过品鉴能力辅助红酒购买决策

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `wine_info` | object | ✅ | 酒款信息：`{name, vintage, region, grape_variety, producer}` |
| `tasting_context` | string | ❌ | 品鉴场景：盲品/正式品鉴/日常饮用 |
| `experience_level` | enum | ❌ | `beginner` / `intermediate` / `advanced`，默认 `beginner` |
| `temperature` | number | ❌ | 品鉴时酒温（℃） |
| `decanting_time` | string | ❌ | 醒酒时间 |

## 📤 输出

```json
{
  "tasting_notes": {
    "appearance": {
      "color": "string — 颜色描述",
      "intensity": "enum — pale / medium / deep",
      "clarity": "enum — clear / hazy / cloudy",
      "other_observations": "string — 挂杯、气泡等"
    },
    "nose": {
      "condition": "enum — clean / faulty",
      "intensity": "enum — light / medium / pronounced",
      "aroma_profile": {
        "primary": ["string — 一类香气（品种/风土）"],
        "secondary": ["string — 二类香气（酿造）"],
        "tertiary": ["string — 三类香气（陈年）"]
      },
      "development": "enum — youthful / developing / fully developed / tired"
    },
    "palate": {
      "sweetness": "enum — dry / off-dry / medium-dry / medium-sweet / sweet",
      "acidity": "enum — low / medium-minus / medium / medium-plus / high",
      "tannin": "enum — low / medium-minus / medium / medium-plus / high",
      "body": "enum — light / medium-minus / medium / medium-plus / full",
      "alcohol": "enum — low / medium / high",
      "flavor_profile": ["string — 口感风味描述"],
      "finish": {
        "length": "enum — short / medium-minus / medium / medium-plus / long",
        "quality": "string — 余味质量描述"
      }
    },
    "overall_assessment": {
      "quality_level": "enum — faulty / poor / acceptable / good / very_good / outstanding",
      "readiness": "enum — too_young / ready / past_peak",
      "aging_potential": "string — 陈年潜力评估",
      "food_pairing": ["string — 推荐配餐"]
    }
  },
  "scoring": {
    "wset_systematic_score": "number — WSET系统评分",
    "personal_score": "number — 个人评分 (50-100)",
    "score_breakdown": {
      "appearance": "number / 3",
      "nose": "number / 7",
      "palate": "number / 10",
      "overall": "number / 5"
    },
    "value_rating": "enum — poor_value / fair_value / good_value / great_value"
  },
  "learning_insights": {
    "style_profile": "string — 酒款风格总结",
    "comparison_suggestion": "string — 建议对比品鉴的酒款",
    "knowledge_points": ["string — 品鉴中学到的知识点"]
  }
}
```

## 📋 执行步骤

### 阶段一：品鉴前准备

1. **环境准备** — 光线充足（白色背景）、无异味干扰、温度适宜（18-22℃）
2. **器具准备** — ISO标准品鉴杯、吐酒桶、白纸（观色用）、矿泉水、无味饼干
3. **酒款准备**:
   - 红酒适饮温度：16-18℃
   - 白酒适饮温度：8-12℃
   - 是否需要醒酒：年轻浓郁型需醒酒30-60分钟
4. **品鉴顺序** — 先白后红、先轻后重、先干后甜、先年轻后陈年

### 阶段二：系统品鉴流程（ISO/WSET方法）

5. **观色 (Appearance)**:
   - 将酒杯倾斜45°，在白色背景前观察
   - 判断颜色深浅、色调（紫红/宝石红/砖红 → 反映年份）
   - 观察挂杯（酒腿）：粗慢=高酒精/高糖度
   - 判断澄清度
6. **闻香 (Nose)**:
   - 第一次闻：静止状态下闻（判断有无缺陷：软木塞污染、氧化、挥发酸）
   - 第二次闻：轻轻摇杯后闻（释放更多香气）
   - 识别三类香气层次：
     - **一类香气**: 花香、果香（来自葡萄品种和风土）
     - **二类香气**: 面包、黄油、酵母（来自酿造过程）
     - **三类香气**: 皮革、烟草、蘑菇（来自陈年）
   - 判断香气浓郁度和发展状态
7. **品味 (Palate)**:
   - 啜饮少量（约10ml），让酒液覆盖整个口腔
   - 评估甜度（舌尖感知）
   - 评估酸度（两颊生津程度）
   - 评估单宁（牙龈和口腔的干涩感）
   - 评估酒体（轻/中/重，像水/牛奶/奶油的质感）
   - 评估酒精度（喉咙的温热感）
   - 识别口感风味（与鼻腔香气可能不同）
8. **余味 (Finish)**:
   - 吐出或吞下后，感受余味持续时间和质量
   - 优质余味：30秒以上，逐渐演变
   - 低质余味：很快消失或有苦味

### 阶段三：综合评估与记录

9. **质量等级评定** — 综合外观、香气、口感、余味给出质量等级
10. **风格判断** — 判断酒款属于哪个产区/品种的典型风格
11. **陈年潜力评估** — 根据酸度、单宁、酒精度、浓郁度判断适饮期
12. **配餐建议** — 根据酒款特征推荐搭配食物
13. **评分记录** — 使用25分制（WSET）或100分制记录评分

### 阶段四：学习与提升

14. **品鉴记录归档** — 记录每次品鉴的详细笔记，建立个人品鉴数据库
15. **对比品鉴** — 同品种不同产区/同年份不同酒庄的对比
16. **风味记忆训练** — 使用香气训练套装（Le Nez du Vin）强化嗅觉记忆
17. **产区知识积累** — 每次品鉴后学习相关产区和品种知识

## ✅ 检查清单

- [ ] 品鉴环境是否符合标准（光线、温度、无异味）
- [ ] 酒温是否调整到适饮温度
- [ ] 是否按正确顺序品鉴（白→红、轻→重）
- [ ] 每个品鉴维度（观色/闻香/品味/余味）是否都已评估
- [ ] 是否区分了一类/二类/三类香气
- [ ] 评分是否基于客观标准而非个人偏

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
