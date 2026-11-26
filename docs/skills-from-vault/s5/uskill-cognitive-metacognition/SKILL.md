---
name: uskill-cognitive-metacognition
description: "让元认知-Schema变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S5-认知与学习/uSkill-cognitive-metacognition.md"
  original_id: "SKL-6848"
  version: "3.0.0"
  trust: untrusted
---

# 元认知-Schema

description: |
  当用户需要启动元认知觉察、暂停自动化反应、部署认知防火墙、进行思维监控时使用此 Skill。
  触发词包括：'元认知'、'觉察'、'暂停'、'自动驾驶'、'思维监控'、'认知防火墙'、
  '自我观察'、'第三视角'、'冥想'、'反思'。当用户讨论情绪管理、习惯打断、
  决策质量提升、思维模式识别时，即使未直接说"元认知"，也应使用此 Skill。
  不适用于具体任务执行（使用对应领域 Skill）。遇到需要"停下来想一想"的场景时优先使用。

---

# uSkill-007: 元认知

## 🎯 目标

> 建立「觉察→暂停→审视→选择」的元认知操作框架，将人从自动驾驶模式切换到主动控制模式，让每一次关键选择都经过理智脑的审视。

**核心价值**：元认知是所有认知能力的"操作系统"——它不直接解决问题，但它让你有能力选择用什么方式解决问题。

**适用场景**：
- 情绪波动时（愤怒、焦虑、恐惧）的自我调节
- 习惯性反应时（刷手机、拖延、冲动消费）的打断
- 重大决策时的思维质量提升
- 日常反思与复盘的深度增强
- 冥想与专注力训练

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `trigger_type` | `enum` | ✅ | — | `emotion` / `habit` / `decision` / `reflection` / `meditation` |
| `stimulus` | `string` | ✅ | — | 触发元认知的刺激/情境描述 |
| `intensity` | `number` | ❌ | `3` | 情绪/习惯强度 1-5（5=极强） |
| `context` | `object` | ❌ | — | `{time_of_day, energy_level, recent_events}` |
| `firewall_mode` | `boolean` | ❌ | `false` | 是否启用认知防火墙模式 |

**输入约束**：
- `stimulus` 必须为非空字符串
- `intensity` 范围 1-5
- `trigger_type = emotion` 时建议提供 `intensity`

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话觉察结论",
  "metacognition_id": "MC-YYYY-MMDD-NNN",

  "trigger_analysis": {
    "type": "emotion|habit|decision|reflection|meditation",
    "stimulus": "string",
    "intensity": "number",
    "autopilot_detected": true,
    "trigger_pattern": "string — 识别到的触发模式"
  },

  "pause_window": {
    "duration_seconds": 3,
    "technique": "string — 使用的暂停技术",
    "space_created": true,
    "first_reaction": "string — 第一反应描述",
    "observed_emotion": "string — 觉察到的情绪",
    "observed_thought": "string — 觉察到的想法"
  },

  "third_person_perspective": {
    "future_self_view": "string — 1年后/5年后/80岁自己的视角",
    "observer_view": "string — 第三视角旁观者的视角",
    "values_alignment": "string — 与核心价值观的对齐度",
    "key_insight": "string — 核心洞察"
  },

  "choice_point": {
    "options": [
      {
        "option": "string",
        "consequence_short": "string",
        "consequence_long": "string",
        "aligned_with_values": true,
        "selected": false
      }
    ],
    "selected_option": "string",
    "selection_reason": "string",
    "confidence": "number"
  },

  "firewall_result": {
    "activated": false,
    "assertion_detected": "string",
    "counter_examples": ["string"],
    "weight_adjustment": "string",
    "cognitive_freedom": "number"
  },

  "post_choice_reflection": {
    "choice_quality": "string",
    "autopilot_switches": "int — 从自动驾驶切换到主动控制的次数",
    "metacognition_strength": "number — 元认知强度评估 1-10",
    "improvement_area": "string"
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

### 异常输出

```json
{
  "status": "partial",
  "error_code": "MC_WARNING_HIGH_INTENSITY",
  "error_message": "情绪强度过高（5/5），元认知介入困难",
  "suggestion": "先执行生理调节（深呼吸10次），再尝试元认知觉察",
  "partial_result": {
    "trigger_analysis": "已完成",
    "pause_window": "失败 — 情绪压过理智脑"
  }
}
```

---

## 📋 执行步骤

### Step 1: 触发识别与信号检测

- **输入**：`trigger_type` + `stimulus`
- **动作**：
  1. 识别触发类型（情绪/习惯/决策/反思/冥想）
  2. 检测自动驾驶信号
  3. 评估触发强度
- **输出**：`trigger_analysis`
- **自动驾驶信号清单**：
  - 情绪类：心跳加速、肌肉紧张、呼吸变浅、思维变窄
  - 习惯类：无意识动作（刷手机、咬指甲）、时间黑洞
  - 决策类：第一反应极快、不愿考虑替代方案、"就是觉得应该这样"
- **分支条件**：
  - IF `intensity` = 5 → 标记 `WARNING_EXTREME_INTENSITY` + 建议先做生理调节
  - IF 触发模式与历史记录匹配 → 标记 `PATTERN_DETECTED`
- **检查点**：✅ 验证触发类型已识别

### Step 2: 元认知暂停（3 秒窗口）

- **输入**：`trigger_analysis`
- **动作**：
  1. 创建暂停窗口（至少 3 秒）
  2. 执行觉察三步法：觉察→命名→选择
  3. 记录第一反应和觉察到的情绪/想法
- **输出**：`pause_window`
- **暂停技术库**：

| 技术 | 适用场景 | 操作 |
|------|----------|------|
| **3 秒呼吸法** | 通用 | 吸气 3 秒 → 屏息 3 秒 → 呼气 3 秒 |
| **5-4-3-2-1 感官锚定** | 焦虑/恐慌 | 说出 5 个看到的 + 4 个触摸到的 + 3 个听到的 + 2 个闻到的 + 1 个尝到的 |
| **命名情绪法** | 情绪波动 | 用精确词汇命名："我在焦虑"、"我在愤怒"、"我在恐惧" |
| **身体扫描法** | 习惯打断 | 从头到脚扫描身体感受，中断自动化回路 |
| **提问锚定法** | 决策场景 | 问自己："这是我真正想要的吗？" |

- **分支条件**：
  - IF `intensity` ≥ 4 → 使用 5-4-3-2-1 感官锚定（更强力的中断）
  - IF `trigger_type` = habit → 使用身体扫描法
  - IF `trigger_type` = decision → 使用提问锚定

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
