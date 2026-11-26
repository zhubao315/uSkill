---
name: uskill-creative-iso-d0965c
description: "把 ISO 讲成画质与曝光的最后一道闸：能低则低，逼不得已才升。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-iso感光度.md"
  original_id: "SKL-7209"
  version: "3.0.0"
  trust: untrusted
---

# ISO感光度

description: |
  当用户需要理解 ISO、控制噪点、在弱光下决定感光度、解释画质下降、使用高 ISO 或双原生 ISO 时使用此 Skill。
  触发词包括：'ISO'、'感光度'、'噪点'、'颗粒'、'原生 ISO'、'双原生'、'降噪'、'画质'。
  当用户纠结"要不要拉高 ISO 怕噪点"时，优先用此 Skill 做画质/曝光的权衡。
  不适用于光圈/快门独立问题（见 [[曝光三角]]、[[光圈]]）或纯后期降噪（见 [[锐化降噪]]）。

---

# uSkill-creative-ISO感光度：画质与曝光的最后闸门

## 🎯 目标

> 让用户在弱光与画质之间做出有意识决策：优先保持最低可用 ISO 以压制噪点，仅在快门/光圈已到物理红线时才提升 ISO，并理解原生与双原生 ISO 的机制。

**核心价值**：ISO 是曝光三角中"最后让步"的参数。光圈管景深、快门管动感，二者用尽后才动 ISO——因为每升一档都在用画质换亮度。

**关键概念**：
- **原生 ISO（Base ISO）**：传感器最佳画质点，多为 ISO 100（或 64）。
- **双原生 ISO（Dual Gain）**：部分机身有两个低噪点基准（如 100 与 640/800），在其附近提 ISO 噪点增长极小。
- **扩展 ISO**：超出原生范围的"虚拟"感光度，画质劣化明显，慎用。

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `light` | `enum` | ✅ | — | `bright` / `dim` / `night` |
| `shake_risk` | `enum` | ✅ | — | `none` / `low` / `high`（糊片风险） |
| `sensor_base_iso` | `number` | ❌ | `100` | 机身原生最低 ISO |
| `dual_native` | `number` | ❌ | `null` | 双原生第二基准，如 800 |
| `acceptable_noise` | `enum` | ❌ | `low` | `low` / `medium` / `high` |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话 ISO 建议",
  "skill_id": "SKL-7209",
  "iso_plan": {
    "recommended_iso": 800,
    "use_dual_native": true,
    "noise_forecast": "medium",
    "why": "string — 光圈/快门已到红线，被迫升 ISO"
  },
  "linked_notes": ["摄影器材选择指南", "锐化降噪"],
  "metadata": { "version": "2.0.0", "self_play_score": "number" }
}
```

---

## 🔄 执行流程

1. **定底线**：先锁定原生最低 ISO（如 100），这是画质最优起点。
2. **耗尽其他两旋钮**：在光圈/快门允许范围内先满足曝光（见 IF/THEN）。
3. **被迫升 ISO**：仅当快门低于安全值或光圈已全开仍欠曝时提升。
4. **跳双原生点**：若机身有双原生，优先提到第二基准附近（噪点跃升小）。
5. **预后与降噪**：给出噪点预期 + 后期降噪提示（[[锐化降噪]]）。

**IF/THEN 决策分支**：

- IF `light == bright` THEN 固定最低原生 ISO（100），其余靠光圈/快门。
- IF `shake_risk == high` AND 快门低于安全线 THEN 升 ISO 优先于继续降快门，避免糊片（参见 [[快门速度]]）。
- IF `dual_native != null` AND 必须升 ISO THEN 直接提到双原生第二基准（如 800），跳过中间高噪点区间。
- IF `light == night` AND `has_tripod == true` THEN 保持低 ISO + 慢门，绝不为亮度升 ISO（参见 [[风光摄影：构图与等待的艺术]]）。
- IF 用户要求 ISO 25600 且非必要 THEN 警告噪点失控，建议补光/三脚架/降预期。

---

## 📝 Prompt 模板

```text
你是 ISO 顾问。光线：{light}，糊片风险：{shake_risk}，
原生基准：{sensor_base_iso}，双原生：{dual_native}。
请输出：
1. 是否应保持在最低 ISO；
2. 什么条件下才升 ISO（快门/光圈红线）；
3. 若有双原生，建议跳到哪个点；
4. 噪点预期与后期降噪笔记。
```

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `ISO_WARNING_SHAKE` | 低 ISO 导致快门过慢 | 升 ISO 保清晰 | 🟡 |
| `ISO_WARNING_NOISE` | 被迫 ≥ 6400 | 提示噪点，建议补光/脚架 | 🟡 |
| `ISO_ERROR_EXTENDED` | 用户用扩展 ISO | 说明画质劣化，建议原生范围 | 🔴 |
| `ISO_WARNING_MISCONCEPT` | 认为"ISO 越亮越好" | 澄清 ISO 不增光只增增益 | 🟡 |

---

## ✅ 质量自检

- [ ] 已优先建议最低原生 ISO
- [ ] 已说明"先耗尽光圈/快门再升 ISO"
- [ ] 双原生机身已提示跳点
- [ ] 关联笔记均为真实存在的笔记
- [ ] 未声称 ISO 能"增加进光量"（仅放大信号）

---

## 💡 使用示例

- **棚拍静物**：`light=bright` → ISO 100，画质优先（参见 [[摄影器材选择指南]]）。
- **夜景三脚架**：`light=night, has_tripod=true` → ISO 100 + 20s 慢门，零噪点。
- **室内运动**：`shake_risk=high` → 开大光圈仍不足则升 ISO 3200。
- **双原生机身弱光**：`dual_native=800` → 直接提到 800，噪点跳变最小。
- **手持街拍**：`light=dim` → f/2.8 + 1/125s + ISO 1600 控噪（参见 [[街头摄影：决定性的瞬间]]）。

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 白天棚拍静物 | 固定最低原生 ISO 100 |
| 2 | 夜景有三脚架 | 保持低 ISO 用慢门 |
| 3 | 手持弱光高糊片风险 | 升 ISO 保清晰而非糊片 |
| 4 | 双原生机身弱光 | 跳到双原生第二基准 |
| 5 | 用户误认 ISO 增光 | 澄清仅信号增益 |
| 6 | 用户要用扩展 ISO | 警告画质劣化建议原生 |

---

## ⚠️ 边界约束

- **不得**声称提高 ISO 能"增加进光量"（仅放大信号，伴随噪点）。
- **不得**鼓励滥用扩展 ISO。
- 原理说明**必须**引用真实摄影笔记（[[摄影器材选择指南]]、[[锐化降噪]]）。

---

## ✅ 校验验收规则

- [ ] 输出含合法 JSON 字段
- [ ] 所有 IF/THEN 分支可验证
- [ ] 关联笔记 wikilink 真实存在
- [ ] 未出现"ISO 越高画质越好"等误述

---

## 🔗 关联文档

- [[曝光三角]] — 三参数联动
- [[光圈]] — 优先用光圈换光
- [[快门速度]] — 优先用快门换光
- [[锐化降噪]] — 后期控噪
- [[摄影器材选择指南]] — 机身 ISO 表现
- [[风光摄影：构图与等待的艺术]] — 低 ISO 慢门
- [[街头摄影：决定性的瞬间]] — 高 ISO 手持

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
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
