---
name: uskill-creative-46c607
description: "把光圈从抽象参数变成可执行的拍摄决策：先想清楚要什么景深，再定 f 值。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-光圈.md"
  original_id: "SKL-7206"
  version: "3.0.0"
  trust: untrusted
---

# 光圈

description: |
  当用户需要调整镜头进光量与景深、理解 f 值含义、在拍摄中决定光圈大小、解释虚化/锐利关系时使用此 Skill。
  触发词包括：'光圈'、'f 值'、'f-stop'、'景深'、'虚化'、'bokeh'、'大光圈'、'小光圈'。
  当用户讨论人像虚化、风光清晰、镜头选购时，即使未直接说"光圈"，也应使用此 Skill。
  不适用于单纯后期调整（参见 [[曝光调整]]）或快门/ISO 的独立问题（参见 [[曝光三角]]）。

---

# uSkill-creative-光圈：用 f 值塑造画面的明暗与景深

## 🎯 目标

> 通过选择恰当的 f 值（光圈），同时控制进光量与景深，让画面在"明暗准确"与"主体突出/全景清晰"之间达成预期。

**核心价值**：光圈是唯一同时影响**曝光**与**景深**的曝光三角参数。先想清楚"我要多浅的景深"，再反推 f 值，而不是被相机自动挡代劳。

**适用场景**：
- 人像：用 f/1.4–f/2.8 制造奶油般虚化、分离主体与杂乱背景
- 风光：用 f/8–f/11 获得从近到远的清晰范围
- 微距：用 f/5.6–f/8 在浅景深约束下尽量保留细节
- 弱光手持：开大光圈换取安全快门
- 镜头选购：理解"恒定光圈"与"浮动光圈"的差异

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `scene_type` | `enum` | ✅ | — | `portrait` / `landscape` / `macro` / `street` / `lowlight` |
| `subject_distance` | `number` | ❌ | — | 对焦面到主体距离（米），影响景深计算 |
| `focal_length` | `number` | ❌ | — | 焦距（mm），长焦更易浅景深 |
| `desired_dof` | `enum` | ❌ | `auto` | `shallow` / `medium` / `deep` / `auto` |
| `light_condition` | `enum` | ❌ | `auto` | `bright` / `dim` / `auto` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话光圈建议",
  "skill_id": "SKL-7206",
  "aperture_decision": {
    "recommended_f": "f/2.8",
    "f_scale": ["f/1.4", "f/2", "f/2.8", "f/4", "f/5.6", "f/8", "f/11", "f/16", "f/22"],
    "stop_delta": -2,
    "dof_forecast": "shallow",
    "exposure_note": "string — 与快门/ISO 的补偿关系"
  },
  "tradeoffs": {
    "sharpness": "f/16 之后衍射下降",
    "bokeh": "光圈越大越柔",
    "light": "每档光圈翻倍/减半进光"
  },
  "linked_notes": ["摄影器材选择指南", "风光摄影：构图与等待的艺术"],
  "metadata": { "version": "2.0.0", "self_play_score": "number" }
}
```

---

## 🔄 执行流程

1. **识别题材意图**：从 `scene_type` 与 `desired_dof` 判断目标景深。
2. **初选 f 值**：按题材映射到基准光圈（见下表）。
3. **联动校验**：根据 `light_condition` 检查是否需要联动快门/ISO 维持曝光（见 IF/THEN）。
4. **衍射红线检查**：长焦或风光若推到 f/22，提示锐度损失。
5. **输出并执行**：给出 f 值、补偿建议、关联笔记。

**题材 → 基准光圈映射**：

| 题材 | 基准 f 值 | 目的 |
|------|-----------|------|
| 人像 | f/1.4–f/2.8 | 浅景深、虚化背景 |
| 风光 | f/8–f/11 | 全景清晰（避开衍射） |
| 微距 | f/5.6–f/8 | 在浅景深中保留细节 |
| 街拍 | f/5.6–f/8 | 区域对焦、提高成功率 |
| 星野 | f/1.4–f/2.8 | 最大进光、短曝光 |

**IF/THEN 决策分支**：

- IF `desired_dof == shallow` THEN 选用 f/1.4–f/2.8，并提醒：进光量大增，需同步提高快门速度或降低 ISO 防过曝。
- IF `desired_dof == deep` AND `focal_length >= 50mm` THEN 推荐 f/8–f/11；IF `f >= f/16` THEN 警告衍射导致边缘锐度下降，建议改用 focus stacking（参见 [[摄影前期策划]]）。
- IF `light_condition == dim` AND 无法降低快门（手持防抖极限） THEN 开大光圈优先于拉高 ISO，以保护画质（参见 [[ISO感光度]]）。
- IF `scene_type == portrait` AND 背景杂乱 THEN 强制浅景深 + 长焦距，最大化主体分离。
- IF 用户要求"全清晰"但给了 f/2.8 THEN 纠正：该 f 值景深极浅，改 f/8 以上。

---

## 📝 Prompt 模板

```text
你是摄影光圈顾问。用户场景：{scene_type}，期望景深：{desired_dof}，
焦距：{focal_length}mm，光线：{light_condition}。
请输出：
1. 推荐 f 值及理由；
2. 需要联动调整的快门/ISO（维持曝光）；
3. 该 f 值下的景深与画质权衡；
4. 关联的摄影笔记（仅限真实存在的笔记）。
```

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `AP_WARNING_OVERDIFFRACT` | f ≥ f/16 仍要求全清晰 | 建议 focus stacking 或后撤机位 | 🟡 |
| `AP_WARNING_OVEREXPOSE` | 大光圈 + 慢快门 + 低 ISO 仍过曝 | 提示 ND 减光镜或提高快门 | 🟡 |
| `AP_ERROR_NOLENS` | 用户镜头最大光圈仅 f/4 | 说明无法获得极浅景深，给替代方案 | 🔴 |
| `AP_WARNING_SHAKE` | 大光圈也未达安全快门 | 提示提高 ISO 或开防抖/上三脚架 | 🟡 |

---

## ✅ 质量自检

- [ ] 推荐 f 值与 `desired_dof` 一致
- [ ] 已说明与快门/ISO 的曝光补偿关系
- [ ] 已提示 f/16+ 的衍射红线
- [ ] 关联笔记均为真实存在的笔记（如 [[摄影器材选择指南]]）
- [ ] 未把"大光圈"误说成"大 f 值"

---

## 💡 使用示例

- **人像虚化**：`scene_type=portrait, desired_dof=shallow` → 推荐 f/1.8，背景虚化，同步快门 1/250s 防过曝。
- **风光全景**：`scene_type=landscape` → 推荐 f/11，景深覆盖前景到远山，若需 f/22 改用景深合成。
- **弱光手持**：`light_condition=dim` 且不可降快门 → 开到 f/2.8，再不够则升 ISO（参见 [[ISO感光度]]）。
- **微距**：`scene_type=macro` → f/8 平衡景深与衍射，配合三脚架（参见 [[摄影拍摄执行]]）。
- **街拍**：`scene_type=street` → f/8 区域对焦，提升抓拍成功率（参见 [[街头摄影：决定性的瞬间]]）。

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 用户要人像极浅景深 | 推荐 f/1.4–f/2.8 并提示快门补偿 |
| 2 | 风光要求全清晰且给 f/22 | 警告衍射并建议景深合成 |
| 3 | 弱光手持无法降快门 | 优先开大光圈而非狂拉 ISO |
| 4 | 微距拍摄小昆虫 | 推荐 f/5.6–f/8 平衡景深 |
| 5 | 用户混淆"大光圈=大 f 值" | 纠正 f 值越小光圈越大 |
| 6 | 镜头最大仅 f/4 却要极虚化 | 给出替代构图方案而非谎言 |

---

## ⚠️ 边界约束

- **不得**编造镜头参数或声称某 f 值能突破物理光学限制。
- **不得**在弱光建议下强行压

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
