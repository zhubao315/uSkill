---
name: uskill-creative-f0b94b
description: "把曝光三角讲成可执行的平衡游戏：定死一个，其余两个围着它转。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-曝光三角.md"
  original_id: "SKL-7207"
  version: "3.0.0"
  trust: untrusted
---

# 曝光三角

description: |
  当用户需要理解光圈、快门、ISO 三者关系、在曝光与画质/景深/动感之间取舍、手动设置曝光、解释过曝欠曝时使用此 Skill。
  触发词包括：'曝光三角'、'曝光补偿'、'曝光锁定'、'直方图'、'欠曝'、'过曝'、'档'、'stop'。
  当用户同时纠结"虚化 vs 噪点 vs 糊片"时，优先用此 Skill 做整体权衡。
  不适用于单一参数深入（分别见 [[光圈]]、[[快门速度]]、[[ISO感光度]]）或纯后期（见 [[曝光调整]]）。

---

# uSkill-creative-曝光三角：在三个旋钮间寻找平衡

## 🎯 目标

> 让用户在光圈、快门、ISO 三者之间做出有意识的权衡，使总曝光正确，同时最大化"景深 / 动感 / 画质"中最重要的那一项。

**核心价值**：三者此消彼长——总曝光（EV）恒定。改一个，必须反向改另一个来补偿。先问"你最在乎哪个维度"，再决定谁让步。

**适用场景**：
- 人像：保景深（定光圈）→ 用快门/ISO 补光
- 运动/宠物：保快门（冻动作）→ 用光圈/ISO 补光
- 夜景/弱光：保画质（低 ISO）→ 用光圈/快门补光（常需三脚架）
- 风光：保小光圈全景 → 用低 ISO + 慢门/三脚架

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `priority` | `enum` | ✅ | — | `dof` / `motion` / `noise` 用户最在乎的维度 |
| `light` | `enum` | ✅ | — | `bright` / `dim` / `night` |
| `subject_speed` | `enum` | ❌ | `still` | `still` / `slow` / `fast` |
| `has_tripod` | `bool` | ❌ | `false` | 是否可用慢门 |
| `target_ev` | `number` | ❌ | `0` | 目标曝光补偿值 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话曝光方案",
  "skill_id": "SKL-7207",
  "exposure_plan": {
    "priority_lock": "dof",
    "aperture": "f/2.8",
    "shutter": "1/250s",
    "iso": 400,
    "ev_balance": "0",
    "stop_relations": "光圈-1档 ⇒ 快门+1档 或 ISO-1档"
  },
  "compensation_note": "string — 谁在让步、为何",
  "linked_notes": ["曝光调整", "风光摄影：构图与等待的艺术"],
  "metadata": { "version": "2.0.0", "self_play_score": "number" }
}
```

---

## 🔄 执行流程

1. **锁定优先级**：从 `priority` 确定不可妥协的维度（景深/动感/画质）。
2. **定基准值**：给优先级维度赋值（如保景深 → 先定光圈）。
3. **测光定 EV**：依据 `light` 与 `target_ev` 算总曝光需求。
4. **补偿另外两个**：按"档"互偿，维持 EV 不变（见 IF/THEN）。
5. **物理红线检查**：快门低于防抖极限或 ISO 过高则报警。
6. **输出方案**：给出三参数 + 补偿说明 + 笔记。

**档（stop）基础**：每档 = 进光量翻倍或减半。光圈每档（f/2→f/2.8→f/4…）、快门每档（1/1000→1/500→1/250…）、ISO 每档（100→200→400…）均等价互偿。

**IF/THEN 决策分支**：

- IF `priority == dof` THEN 先定光圈，再让快门/ISO 让步；IF 快门低于安全值 THEN 升 ISO 而非缩光圈（保景深）。
- IF `priority == motion` AND `subject_speed == fast` THEN 先定高速快门（≥1/500s），用开大光圈 + 升 ISO 补光；IF 仍欠曝 THEN 建议补光或放弃保画质。
- IF `priority == noise` AND `light == night` THEN 先定最低可用 ISO，开满光圈，若快门过慢 THEN 强制要求三脚架（参见 [[风光摄影：构图与等待的艺术]]）。
- IF `has_tripod == false` AND 需要慢门 THEN 警告糊片，建议升 ISO 或开大光圈。
- IF `target_ev < 0`（刻意欠曝保高光）THEN 提醒后期拉回空间有限，谨慎低于 -2 档。

---

## 📝 Prompt 模板

```text
你是曝光三角顾问。优先级：{priority}，光线：{light}，
主体速度：{subject_speed}，有三脚架：{has_tripod}。
请输出：
1. 被锁定的参数及其值；
2. 另两个参数如何按"档"互偿以维持 EV={target_ev}；
3. 物理红线（快门/ISO）警告；
4. 关联真实摄影笔记。
```

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `ET_WARNING_SHAKE` | 无三脚架却需慢门 | 升 ISO 或开大光圈 | 🟡 |
| `ET_WARNING_NOISE` | ISO 被迫 ≥ 6400 | 提示噪点，建议补光/三脚架 | 🟡 |
| `ET_ERROR_CONFLICT` | 既要浅景深又要高速又要低 ISO 且弱光 | 说明物理不可能，请用户取舍 | 🔴 |
| `ET_WARNING_BLOWN` | 强逆光仍坚持 +EV | 提醒高光溢出，建议点测光 |

---

## ✅ 质量自检

- [ ] 已明确 `priority` 并锁定对应参数
- [ ] 另两个参数按"档"互偿，EV 维持 `target_ev`
- [ ] 已检查快门安全线与 ISO 噪点红线
- [ ] 关联笔记均为真实存在的笔记
- [ ] 未声称可同时"全虚化+零噪点+冻动作+弱光"

---

## 💡 使用示例

- **人像夜景**：`priority=dof, light=night` → 定 f/1.8，开 ISO 1600 + 1/125s，上防抖。
- **飞鸟**：`priority=motion, subject_speed=fast` → 定 1/2000s，开 f/4 + ISO 800。
- **星空**：`priority=noise, light=night, has_tripod=true` → 定 ISO 1600（双原生），f/2.8，20s 曝光。
- **风光白天**：`priority=dof`（全清晰）→ f/11，ISO 100，1/125s 三脚架。
- **室内宠物**：`priority=motion` → 1/500s，f/2.8，ISO 3200 控噪（参见 [[ISO感光度]]）。

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 人像弱光要虚化 | 锁光圈开大，用 ISO 补光而非缩光圈 |
| 2 | 飞鸟高速运动 | 锁高速快门，光圈+ISO 补偿 |
| 3 | 夜景要低噪点无脚架 | 触发糊片警告或建议补光 |
| 4 | 同时要求全虚化+零噪点+弱光 | 指出物理冲突请取舍 |
| 5 | 风光全清晰白天 | f/11 + 低 ISO + 三脚架方案 |
| 6 | 强逆光坚持加曝光 | 警告高光溢出建议点测光 |

---

## ⚠️ 边界约束

- **不得**承诺突破曝光三角的物理约束。
- **不得**在弱光无脚架下诱导用户牺牲一切换虚化。
- 原理说明**必须**引用真实摄影笔记（[[曝光调整]]、[[摄影拍摄执行]]）。

---

## ✅ 校验验收规则

- [ ] 输出含合法 JSON 字段
- [ ] 所有 IF/THEN 分支可验证
- [ ] 关联笔记 wikilink 真实存在
- [ ] 未出现"无损同时满足全部"的伪科学表述

---

## 🔗 关联文档

- [[光圈]] — 景深与进光
- [[快门速度]] — 动感与冻结
- [[ISO感光度]] — 画质与噪点
- [[曝光调整]] — 后期修正
- [[风光摄影：构图与等待的艺术]] — 小光圈实战
- [[街头摄影：决定性的瞬间]] — 快门优先实战
- [[摄影器材选择指南]] — 机身 ISO 表现

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
