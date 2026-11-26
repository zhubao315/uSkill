---
name: uskill-visionos-development
description: "空间计算不是把屏幕贴到空中——是让数字内容住进你的房间。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-visionos-development.md"
  original_id: "SKL-6202"
  version: "3.0.0"
  trust: untrusted
---

# visionOS空间计算

description: |
  当用户需要开发 Apple Vision Pro 应用、visionOS 空间计算、SwiftUI 空间界面时使用此 Skill。
  触发词：'visionOS'、'Vision Pro'、'空间计算'、'SwiftUI'、'RealityKit'、'空间应用'。

# visionOS 空间计算

## 🎯 目标

> 构建原生 visionOS 应用，利用空间计算的独特能力创造传统屏幕无法实现的体验。

**核心价值**：visionOS 不是「头戴式 iPad」。本 Skill 确保应用利用空间计算的独特能力（空间锚定、环境理解、眼动交互），而非简单移植 2D 应用。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `app_type` | enum | ✅ | — | 类型：`productivity`（效率）/ `media`（媒体）/ `utilities`（工具）/ `immersive`（沉浸式） |
| `immersion_level` | enum | ❌ | `"mixed_reality"` | 沉浸度：`full_space`（全空间）/ `mixed_reality`（混合现实）/ `windowed`（窗口） |
| `input_methods` | array | ❌ | `["eye_tracking","hand_gesture"]` | 输入方式 |
| `spatial_sharing` | boolean | ❌ | `false` | 是否需要空间共享（多设备协作） |

## 📤 输出

```json
{
  "app_architecture": {
    "scene_type": "string — 场景类型（Window/Volume/ImmersiveSpace）",
    "swiftui_structure": "string — SwiftUI 视图层级",
    "realitykit_usage": "string — RealityKit 场景描述"
  },
  "spatial_design": {
    "window_layout": "string — 窗口空间布局",
    "gaze_targets": "string — 眼动交互目标设计",
    "hand_gesture_map": "string — 手势映射方案"
  },
  "review_checklist": ["string — App Store 审核要点"]
}
```

## 📋 执行步骤

### Step 1: 场景设计
1. **窗口/体积/沉浸空间** — 根据内容选择正确的场景类型
2. **空间布局** — 多窗口的空间排列（考虑房间尺度）
3. **深度层次** — 利用 z 轴创建信息层次
4. **检查点**：✅ 场景类型是否正确？布局是否考虑了房间尺度？

### Step 2: 眼动与手势交互
1. **凝视目标** — 眼动追踪的目标尺寸 ≥44pt（舒适点击区）
2. **手势映射** — 捏合 = 点击、长捏 = 拖拽、旋转手势 = 调整
3. **舒适区** — 交互目标在视线中心 ±15° 范围内
4. **检查点**：✅ 目标尺寸是否足够大？手势是否自然？

### Step 3: 沉浸式体验
1. **环境理解** — 利用场景重建让数字内容与真实环境融合
2. **空间锚定** — 内容固定在空间中的正确位置
3. **遮挡处理** — 数字内容被真实物体遮挡时的处理
4. **检查点**：✅ 内容是否与环境融合？空间锚定是否稳定？

### Step 4: 审核与发布
1. **Human Interface Guidelines** — 严格遵循 visionOS HIG
2. **性能要求** — 确保在 M1/M2 芯片上流畅运行
3. **隐私声明** — 眼动数据/场景数据的隐私声明
4. **检查点**：✅ 是否遵循 HIG？性能是否达标？隐私声明是否完整？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 审核被拒 | 常见原因：不符合 HIG | 逐条对照 HIG 修改，重新提交 |
| 眼动精度不足 | 点击偏移大 | 增大目标尺寸，增加凝视确认时间 |
| 内存不足 | M1 设备 OOM | 降低纹理分辨率，减少同屏 3D 物体 |

## 💬 沟通风格

- **原生思维**：用 visionOS 原生范式，不移植 iPad 逻辑
- **空间优先**：先考虑空间中的信息层次，再考虑界面元素
- **人体工学**：所有交互目标都在舒适区内

## 📝 自检清单

- [ ] 是否使用了原生 visionOS 场景类型？
- [ ] 眼动目标尺寸是否 ≥44pt？
- [ ] 手势交互是否自然？
- [ ] 内容是否与真实环境融合？
- [ ] 是否遵循了 visionOS HIG？
- [ ] 隐私声明是否完整？

---


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
- 当输入数据质量不足以支撑自动化决策时，**必须**转交人工判断
- 当涉及法律/财务/医疗等高风险领域时，**必须**暂停执行等待确认

#### ✅ 校验验收规则

> 此区块定义执行后的验证标准，确保输出质量。

**格式校验**：
- [ ] 输出内容结构完整，无缺失区块
- [ ] 所有必填参数已填充
- [ ] 输出格式符合预定义规范

**内容校验**：
- [ ] 建议具有可操作性，非泛泛而谈
- [ ] 数据引用准确，无虚构内容
- [ ] 方案考虑了实际约束条件

**合规校验**：
- [ ] 未违反硬性约束
- [ ] 人工兜底点已正确识别
- [ ] 敏感信息已脱敏处理

#### 🔄 迭代触发条件

> 此区块定义 Skill 自我进化的触发机制。

**Self-Play 触发**：
- **频率**：monthly
- **触发条件**：
  - 用户反馈评分低于 7/10
  - 实际执行中发现新的异常场景
  - 相关领域出现重大变化

**版本升级触发**：
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents VisionOS Spatial Engineer + macOS Spatial Metal Engineer |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

### 信号读取
1. **任务类型**：[用户要什么？]
2. **风格关键词**：[用户用了哪些描述？]
3. **约束条件**：[时间/工具/环境限制？]

### 反默认纪律
不要默认套用：[该领域 AI 常见的偷懒模式]。必须根据用户的具体情况定制。

---

## 🚫 Anti-Rationalization Table `[v3新增]`

> 来源：addyosmani/agent-skills 的核心创新

| Agent 常见借口 | 反驳 |
|--------------|------|
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
- 检查常见错误

### ⚠️ Ask first（先问再做）
- 用户意图不明确时
- 操作不可逆时
- 涉及外部系统时

### 🚫 Never do（绝对禁止）
- 不跳过验证步骤
- 不在用户未确认时执行高风险操作
- 不伪装成功（失败就上报）

---

## 🔒 Gated Wor

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
