---
name: uskill-creative-3d-asset-creation
description: "模型的价值不在于面数多少，而在于用最少的面传达最多的信息。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-creative-3d-asset-creation.md"
  original_id: "SKL-5906"
  version: "3.0.0"
  trust: untrusted
---

# 3D资产创建

description: |
  当用户需要创建游戏 3D 模型、UV 展开、纹理烘焙、LOD 制作时使用此 Skill。
  触发词：'3D建模'、'Blender'、'模型创建'、'UV展开'、'LOD'、'3D资产'、'低模'、'高模'。

# 3D 资产创建

## 🎯 目标

> 创建符合引擎管线规范的 3D 资产，从建模到导出全链路标准化。

**核心价值**：模型在 Blender 里好看不等于在引擎里好用。本 Skill 将每个环节对齐引擎需求，确保一次导入成功。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `asset_type` | enum | ✅ | — | 类型：`prop`（道具）/ `character`（角色）/ `environment`（环境）/ `vehicle`（载具）/ `weapon`（武器） |
| `poly_budget` | int | ✅ | — | 目标面数上限 |
| `texture_size` | enum | ❌ | `"1024"` | 纹理尺寸：`512` / `1024` / `2048` / `4096` |
| `lod_levels` | int | ❌ | `3` | LOD 层级数 |
| `engine` | enum | ❌ | `"unity"` | 目标引擎 |
| `style` | enum | ❌ | `"realistic"` | 风格：`realistic`（写实）/ `stylized`（风格化）/ `lowpoly`（低多边形） |

## 📤 输出

```json
{
  "model_spec": {
    "poly_count": "int — 最终面数",
    "vertex_count": "int — 顶点数",
    "uv_channels": "int — UV 通道数",
    "materials": "int — 材质数"
  },
  "lod_chain": [{"level": "int", "poly_count": "int", "switch_distance": "float"}],
  "texture_set": {
    "albedo": "string — 基色贴图路径",
    "normal": "string — 法线贴图路径",
    "roughness": "string — 粗糙度贴图路径",
    "ao": "string — 环境光遮蔽贴图路径"
  },
  "export_file": "string — 导出文件路径（FBX/glTF）",
  "checklist_result": "string — 资产检查清单结果"
}
```

## 📋 执行步骤

### Step 1: 建模
1. **参考收集** — 收集真实/概念参考图
2. **基础造型** — 从大形开始，确定比例和轮廓
3. **细节分级** — 根据面数预算决定细节层级
4. **检查点**：✅ 轮廓是否有辨识度？面数是否在预算内？

### Step 2: UV 展开与烘焙
1. **UV 展开** — 无重叠、利用率 >70%、接缝放在不可见处
2. **法线烘焙** — 高模细节烘焙到低模法线贴图
3. **AO 烘焙** — 环境光遮蔽贴图增强体积感
4. **检查点**：✅ UV 是否无重叠？法线烘焙是否正确？

### Step 3: 纹理制作
1. **PBR 流程** — Albedo + Normal + Roughness + AO
2. **纹理尺寸** — 根据资产在画面中的占比选择尺寸
3. **压缩格式** — PC: BC7 / Mobile: ASTC 6×6
4. **检查点**：✅ 纹理是否 PBR 规范？压缩格式是否正确？

### Step 4: LOD 与导出
1. **LOD 制作** — LOD0（原始）→ LOD1（50%）→ LOD2（25%）→ LOD3（10%）
2. **导出设置** — FBX/glTF，坐标系匹配目标引擎
3. **引擎验证** — 导入引擎检查材质/碰撞/动画
4. **检查点**：✅ LOD 链是否完整？引擎导入是否一次成功？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 面数超标 | 超过预算 20% | 简化次要区域、合并相邻面 |
| UV 重叠 | 检测到重叠 | 重新展开，调整接缝位置 |
| 法线翻转 | 部分面法线方向错误 | 统一法线方向，重新烘焙 |
| 导入失败 | 引擎不识别格式 | 检查导出设置、坐标系、单位 |

## 💬 沟通风格

- **工程思维**：模型不是艺术品，是引擎里的运行时资产
- **数据驱动**：面数/UV利用率/纹理尺寸全部量化
- **管线优先**：任何决策都先评估对引擎管线的影响

## 📝 自检清单

- [ ] 面数是否在预算内？
- [ ] UV 是否无重叠且利用率 >70%？
- [ ] 法线方向是否一致？
- [ ] 纹理是否为 PBR 流程？
- [ ] LOD 链是否完整？
- [ ] 引擎导入是否一次成功？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Blender + Roblox Avatar Creator |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [任务类型] for [用户水平], with [约束条件], leaning toward [方法/工具]."

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
| ""这个我知道"" | "知道自己不知道才是认知升级的起点" |
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

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
- 涉及外部系统

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
