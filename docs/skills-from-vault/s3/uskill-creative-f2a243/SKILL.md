---
name: uskill-creative-f2a243
description: "把景深讲成可计算的四个旋钮：光圈、焦距、距离、传感器，而非玄学。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-景深.md"
  original_id: "SKL-7208"
  version: "3.0.0"
  trust: untrusted
---

# 景深

description: |
  当用户需要理解画面清晰范围、控制前景背景虚实、计算超焦距、解释为何长焦更虚化、决定对焦策略时使用此 Skill。
  触发词包括：'景深'、'DoF'、'虚化'、'散景'、'bokeh'、'超焦距'、'对焦'、'前后清晰'。
  当用户纠结"为什么背景还是清楚""怎么让背景化开"时，优先用此 Skill。
  不适用于单纯光圈选择（见 [[光圈]]）或镜头选购（见 [[摄影器材选择指南]]）。

---

# uSkill-creative-景深：前后清晰的边界由四因子决定

## 🎯 目标

> 让用户能预测并控制"从哪到哪是清晰的"，通过对光圈、焦距、物距、传感器尺寸的取舍，精确匹配创作意图（主体突出 or 全景清晰）。

**核心价值**：景深不是单靠光圈，而是四个因子共同决定。理解它，才能在不同机位/镜头下复用经验，而非死记参数。

**四控制因子**：
1. **光圈**：越大（f 值越小）景深越浅
2. **焦距**：越长焦景深越浅
3. **物距**：离主体越近景深越浅
4. **传感器**：画幅越大（全幅＞APS-C＞M43）景深越浅

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `intent` | `enum` | ✅ | — | `isolate` / `full` / `balanced` |
| `focal_length` | `number` | ❌ | — | mm，长焦更浅 |
| `subject_distance` | `number` | ❌ | — | 米，越近越浅 |
| `sensor` | `enum` | ❌ | `fullframe` | `fullframe` / `aps-c` / `m43` |
| `aperture` | `string` | ❌ | — | 如 f/2.8 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话景深方案",
  "skill_id": "SKL-7208",
  "dof_plan": {
    "forecast": "shallow|medium|deep",
    "hyperfocal_distance": "number — 米（风光用）",
    "drivers": ["aperture", "focal_length", "distance", "sensor"],
    "recommendation": "string — 调哪个因子最有效"
  },
  "linked_notes": ["摄影器材选择指南", "构图法则超越三分法"],
  "metadata": { "version": "2.0.0", "self_play_score": "number" }
}
```

---

## 🔄 执行流程

1. **判定意图**：`intent` 决定要浅还是深。
2. **四因子体检**：列出当前光圈/焦距/物距/传感器对景深的贡献。
3. **选最有效杠杆**：人像优先光圈+物距；风光优先光圈+超焦距；微距优先物距。
4. **超焦距计算**（风光）：对焦在超焦距，使远景到近景都清晰。
5. **输出与验证**：给出清晰范围预测 + 关联笔记。

**超焦距（Hyperfocal）**：当对焦距离设在超焦距 H 时，从 H/2 到无穷远都清晰。风光常用 f/8–f/11 + 对焦约 1/3 入画处。

**IF/THEN 决策分支**：

- IF `intent == isolate` THEN 建议大光圈 + 拉近物距 + 长焦；IF 镜头最大仅 f/4 THEN 改用更长焦或更近物距补偿（参见 [[人像摄影：光线与情绪的对话]]）。
- IF `intent == full` AND `sensor == fullframe` THEN 推荐 f/8–f/11 + 超焦距；IF 仍不足 THEN 后撤机位（物距增大景深变深）。
- IF `intent == full` AND 用户给 f/1.8 THEN 纠正：该组合景深极浅，改 f/8 以上或 focus stacking。
- IF `subject_distance < 0.3m`（微距）THEN 提醒景深以毫米计，需 f/8 + 三脚架 + 堆栈（参见 [[摄影拍摄执行]]）。
- IF 用户混淆"景深"与"散景质量" THEN 区分：景深是清晰范围（量化），散景是虚化美观度（主观，受光圈叶片/像差影响）。

---

## 📝 Prompt 模板

```text
你是景深顾问。意图：{intent}，焦距：{focal_length}mm，物距：{subject_distance}m，
传感器：{sensor}。请输出：
1. 当前四因子对景深的影响；
2. 达成意图最有效的一个调节杠杆；
3. 风光场景给出超焦距建议；
4. 关联真实摄影笔记。
```

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `DOF_WARNING_SHALLOW_FIXED` | 镜头光圈受限无法更浅 | 用长焦/近物距补偿 | 🟡 |
| `DOF_WARNING_DIFFRACT` | 为深景深推到 f/22 | 警告衍射，建议后退机位 | 🟡 |
| `DOF_ERROR_MISCONCEPT` | 把景深当散景质量 | 澄清概念差异 | 🔴 |
| `DOF_WARNING_MACRO` | 微距景深过浅 | 建议堆栈/三脚架 | 🟡 |

---

## ✅ 质量自检

- [ ] 已列出四控制因子（光圈/焦距/物距/传感器）
- [ ] 已区分景深（范围）与散景（美观）
- [ ] 风光场景给出超焦距思路
- [ ] 关联笔记均为真实存在的笔记
- [ ] 未声称"小传感器也能轻松虚化"

---

## 💡 使用示例

- **人像虚化**：`intent=isolate` → f/1.8 + 85mm + 近物距，背景化开（参见 [[人像摄影：光线与情绪的对话]]）。
- **风光全景**：`intent=full` → f/11 + 超焦距对焦，远近皆清（参见 [[风光摄影：构图与等待的艺术]]）。
- **微距昆虫**：`subject_distance=0.2m` → f/8 + 三脚架 + 景深堆栈。
- **街拍**：`intent=balanced` → f/8 区域对焦提高成功率（参见 [[街头摄影：决定性的瞬间]]）。
- **手机虚化**：`sensor=m43 更小` → 靠近主体 + 人像模式算法补虚化。

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 人像要主体突出 | 大光圈+长焦+近物距组合 |
| 2 | 风光要全清晰 | f/11+超焦距，必要时后退 |
| 3 | 微距极近拍摄 | 提示景深毫米级需堆栈 |
| 4 | 用户混淆景深与散景 | 澄清两概念差异 |
| 5 | 镜头光圈受限 | 用焦距/物距补偿而非谎言 |
| 6 | 为深景深用 f/22 | 警告衍射建议后退机位 |

---

## ⚠️ 边界约束

- **不得**声称小传感器能轻松获得单反级虚化。
- **不得**混淆景深（可量化范围）与散景（主观美观）。
- 原理说明**必须**引用真实摄影笔记（[[摄影器材选择指南]]、[[构图法则超越三分法]]）。

---

## ✅ 校验验收规则

- [ ] 输出含合法 JSON 字段
- [ ] 所有 IF/THEN 分支可验证
- [ ] 关联笔记 wikilink 真实存在
- [ ] 未出现"全画幅虚化不如手机"等误述

---

## 🔗 关联文档

- [[光圈]] — 景深首要因子
- [[曝光三角]] — 与快门/ISO 联动
- [[摄影器材选择指南]] — 画幅与镜头
- [[构图法则超越三分法]] — 虚实构图
- [[人像摄影：光线与情绪的对话]] — 浅景深实战
- [[风光摄影：构图与等待的艺术]] — 深景深实战
- [[手机摄影：从随手拍到作品]] — 小传感器对策

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-07-08 | 2.0.0 | Gen3 升级：9 模块 + IF/THEN + Self-Play，补真实摄影内容 |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [摄影场景] for [拍摄者水平], with [创作优先级], leaning toward [器材/环境约束]."

### 信号读取
1. **任务类型**：[用户要

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
