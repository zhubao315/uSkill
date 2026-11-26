---
name: uskill-cognition-value-drift-detection
description: "让价值偏离检测从模糊的'心里不踏实'变成可度量的校准动作。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognition-value-drift-detection.md"
  original_id: "SKL-7101"
  version: "3.0.0"
  trust: untrusted
---

# 价值偏离检测

description: |
  当用户需要检测个人行为/决策是否偏离核心价值观时使用此 Skill。
  触发词包括：'价值偏离'、'目标偏离'、'初心检查'、'对齐检查'、'我是不是跑偏了'。
  即使用户只是说'最近心里不踏实''感觉在忙但没意义'，只要意图涉及
  行为与价值的对照校准，也应使用此 Skill。不适用于团队/企业层面的
  战略对齐（那是 [[uSkill-value-drift-detect]] 的范围）。

---

# 🧭 [[uSkill-价值偏离检测-v1]]

> 监控个人行为是否偏离核心价值观。偏离不是'做错事'，而是行动与内心最重要的 3 个价值之间出现了持续错位。

## 🎯 目标

> 把"心里不踏实"翻译成可观察的偏离信号，给出可执行的纠偏动作，让行动重新对齐核心价值。

**适用场景**：
- 周度/月度复盘时，对照"这周我真正在意的事"检查行为
- 重大决策前的初心检查（要不要接这个项目？要不要换方向？）
- 能量持续低落、后悔频率上升时的自我诊断

**核心价值锚定**：本技能默认以用户当前最重要的 3 个价值为基准盘。若用户未显式给出，先用"每日价值观锚定"引导其确认，再做对照。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `core_values` | `array` | ✅ | 当前核心价值/目标列表（建议 ≤3 个） |
| `recent_actions` | `array` | ✅ | 近期行动/决策列表（含时间戳更佳） |
| `drift_signals` | `object` | ❌ | 偏离信号自评：后悔频率、能量感、核心圈互动质量 |

---

## 📤 输出

```json
{
  "anchored_values": ["string"],
  "aligned": [{"action": "string", "value": "string", "alignment": "strong|moderate|weak"}],
  "drifted": [{"action": "string", "value": "string", "drift_level": "high|medium|low", "evidence": "string", "suggestion": "string"}],
  "signal_diagnosis": {"regret_freq": "string", "energy": "string", "core_circle": "string"},
  "overall_alignment": "number (0-100%)"
}
```

---

## 🔄 执行流程

```
1. [价值锚定] → 确认当前最重要的价值（≤3 个）
   → 判断条件：用户是否已显式给出 core_values？
     → 是：直接使用，进入解析
      → 否：先用"每日价值观锚定"（每日晨间用 1 个问题确认当下最重要的 ≤3 个价值）提问引导，再进入解析
   → 判断条件：用户给出超过 5 个价值？
     → 是：提示"价值过多等于无优先级"，建议收敛到 3 个再评估
     → 否：正常进入下一步

2. [信号初诊] → 读取偏离信号自评
   → 后悔频率上升 + 能量感下降 + 核心圈互动质量下降
     → IF 三项中 ≥2 项明显恶化 → 标注"高偏离风险"，优先排查
     → IF 三项均平稳 → 降低偏离风险权重，进入常规对照

3. [行为解析] → 将每条 recent_action 映射到价值
   → 每个行动 → 检查是否对齐每个价值
   → 对齐度：strong(直接支撑) / moderate(间接相关) / weak(无关联)

4. [偏离识别] → 标注偏离项
   → 判断条件：是否存在行动与核心价值直接冲突？
     → 是：标注为偏离，按冲突强度定 drift_level（high/medium/low）
     → 否：标注为对齐或弱关联

5. [纠偏建议] → 为每个偏离项提供具体纠偏方法
   → 规则：建议必须具体可执行，绑定到具体行动而非"多反思"
   → 规则：high 级偏离必须给出"本周可做的 1 个动作"

6. [综合评分] → 计算整体对齐度
   → 公式：aligned_count / total_actions × 100%
   → IF 对齐度 < 50% → 标注"系统性偏离"，建议启动一次完整的价值观重锚
   → IF 对齐度 ≥ 80% → 标注"健康"，仅保留微调建议
```

---

## 📝 Prompt 模板

### 标准检测 Prompt

```
你是价值偏离检测 Agent。请基于用户的价值观，检测其近期行为是否偏离。

【核心价值】（≤3 个）
{core_values}

【近期行动/决策】
{recent_actions}

【偏离信号自评】（可选）
{drift_signals}

【检测维度】
1. 价值锚定：确认基准盘是否清晰、收敛
2. 信号初诊：后悔/能量/核心圈三项是否恶化
3. 行为解析：逐条行动对齐到价值
4. 偏离识别：high/medium/low 分级
5. 纠偏建议：每条偏离绑定一个可执行动作

【偏离分级】
- high：行动直接违反核心价值（如"为赚钱砍掉不盈利但有意义的事"）
- medium：行动与价值不完全一致（如"加班挤压了陪伴家人"）
- low：行动与价值无关联但不冲突（如"刷了半天短视频"）

【输出格式】
按标准 JSON 输出，包含 anchored_values、aligned、drifted、signal_diagnosis、overall_alignment。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 价值定义模糊（"我想好好生活"） | 用锚定提问收敛到可衡量维度 | 基于字面意思推断并标注"待澄清" |
| 行动信息不足 | 基于已有信息评估 | 标注"信息不完整"，只评可评项 |
| 无偏离 | 输出"完全对齐" + 维持建议 | 无需纠偏建议 |
| 信号全部恶化但行动正常 | 提示"可能是外部压力，非行为偏离" | 建议排查环境与精力管理 |
| 用户给出 10+ 个价值 | 请求收敛优先级 | 取前 3 个评估，其余标注"未纳入" |

---

## ✅ 质量自检

- [ ] 已确认基准价值 ≤3 个且用户认可
- [ ] 每条偏离都有行为证据（evidence），非主观臆断
- [ ] 每条纠偏建议绑定到具体动作
- [ ] high 级偏离已给出"本周可执行 1 动作"
- [ ] 整体对齐度计算口径清晰（aligned/total）
- [ ] 未把外部压力误判为行为偏离

---

## 💡 使用示例

### 示例 1：完全对齐

**输入**：
```json
{
  "core_values": ["深度陪伴家人", "长期成长", "健康"],
  "recent_actions": ["每天 19:00-20:30 陪孩子", "读完《心流》并写卡片", "保持每周 3 次跑步"]
}
```

**输出**：
```json
{
  "anchored_values": ["深度陪伴家人", "长期成长", "健康"],
  "aligned": [
    {"action": "每天陪孩子", "value": "深度陪伴家人", "alignment": "strong"},
    {"action": "读《心流》写卡片", "value": "长期成长", "alignment": "strong"},
    {"action": "每周 3 次跑步", "value": "健康", "alignment": "strong"}
  ],
  "drifted": [],
  "signal_diagnosis": {"regret_freq": "低", "energy": "稳", "core_circle": "好"},
  "overall_alignment": 100
}
```

### 示例 2：存在系统性偏离

**输入**：
```json
{
  "core_values": ["深度陪伴家人", "长期成长", "健康"],
  "recent_actions": ["连续 3 周每晚 23:00 后回家", "取消读书计划", "停跑 2 周", "接了高薪但无意义的外包"],
  "drift_signals": {"regret_freq": "高", "energy": "下降", "core_circle": "下降"}
}
```

**输出**：
```json
{
  "drifted": [
    {"action": "连续晚归", "value": "深度陪伴家人", "drift_level": "high", "evidence": "3 周未参与家庭晚餐", "suggestion": "本周设定 2 天 19:00 前到家"},

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
