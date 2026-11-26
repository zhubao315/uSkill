---
name: uskill-open-world-builder
description: "开放世界的秘密不是大，而是每个角落都有内容。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-open-world-builder.md"
  original_id: "SKL-5908"
  version: "3.0.0"
  trust: untrusted
---

# 开放世界构建

description: |
  当用户需要构建开放世界环境、设计流式加载系统、实现程序化植被分布、管理大规模关卡时使用此 Skill。
  触发词：'开放世界'、'open world'、'流式加载'、'World Partition'、'HLOD'、'程序化生成'、'大世界'。

# 开放世界构建

## 🎯 目标

> 构建无缝流式加载的大规模开放世界环境，保证性能和沉浸感。

**核心价值**：开放世界的挑战不是「做多大」，而是「在目标硬件上流畅运行多大」。本 Skill 将流式加载、LOD、程序化生成标准化为可控的工程流程。

**适用场景**：
- 城市沙盒游戏（北京/其他城市复刻）
- 生存/探索类开放世界
- 大型 RPG 地图
- 模拟经营类游戏世界

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `world_size_km2` | float | ✅ | — | 世界面积（平方公里） |
| `detail_level` | enum | ❌ | `"medium"` | 细节密度：`sparse`（荒野）/ `medium`（郊外）/ `dense`（城市） |
| `streaming_method` | enum | ❌ | `"grid"` | 流式方法：`grid`（网格分区）/ `quadtree`（四叉树）/ `fixed`（固定区块） |
| `target_platform` | enum | ❌ | `"pc"` | 目标平台 |
| `foliage_method` | enum | ❌ | `"procedural"` | 植被方式：`manual`（手工）/ `procedural`（程序化）/ `hybrid`（混合） |
| `has_interior` | boolean | ❌ | `false` | 是否需要室内场景（影响内存预算） |

## 📤 输出

```json
{
  "world_config": {
    "cell_size": "int — 流式单元格大小（米）",
    "streaming_layers": ["string — 流式层级描述"],
    "always_loaded_zones": ["string — 常驻加载区域"],
    "memory_budget": "string — 内存预算分配"
  },
  "lod_plan": {
    "terrain_lod": "string — 地形 LOD 方案",
    "object_lod": "string — 物体 LOD 方案",
    "foliage_lod": "string — 植被 LOD 方案",
    "hlod_config": "string — HLOD 配置"
  },
  "foliage_plan": {
    "density_maps": "string — 密度图描述",
    "species_list": ["string — 植被种类列表"],
    "rules": ["string — 分布规则"]
  },
  "optimization_report": {
    "draw_call_budget": "int — Draw Call 预算",
    "tri_budget": "int — 三角面预算",
    "streaming_test": "string — 流式加载测试方案"
  }
}
```

## 📋 执行步骤

### Step 1: 世界分区设计
1. **网格尺寸** — 城市 64m、郊外 128m、荒野 256m+
2. **常驻区域** — 游戏关键内容（存档点/NPC/任务触发器）必须常驻加载
3. **边界规避** — 关键内容不要放在单元格边界，防止流式加载时短暂消失
4. **检查点**：✅ 单元格尺寸是否匹配内容密度？关键内容是否常驻？

### Step 2: LOD 体系
1. **地形 LOD** — 从高精度 Mesh 到低精度简化，配合法线贴图
2. **物体 LOD** — 4 级 LOD（LOD0 精细 → LOD3 极简）
3. **植被 LOD** — 远处用 Billboard 替代 3D 模型
4. **HLOD** — 合并远处多个物体为一个简化模型，消除 pop-in
5. **检查点**：✅ LOD 是否覆盖完整距离范围？是否有 pop-in？

### Step 3: 程序化植被
1. **密度图** — 根据地形类型/海拔/坡度绘制植被密度
2. **分布规则** — 树木不长在路上、草地不在水面、花丛在阳光处
3. **多样性** — 每种植物有 3-5 个变体，避免重复感
4. **性能控制** — 远处植被用 GPU Instancing 渲染
5. **检查点**：✅ 植被分布是否自然？是否有重复感？GPU Instancing 是否启用？

### Step 4: 流式加载测试
1. **快速穿越测试** — 骑马/开车快速穿越世界，监控卡顿
2. **内存监控** — 确保峰值内存不超预算
3. **远景测试** — 站在高处远眺，检查 pop-in 和 LOD 切换
4. **检查点**：✅ 快速穿越是否有卡顿？远景是否自然？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 流式卡顿 | 单元格加载 >100ms | 减小单元格尺寸、增加预加载范围 |
| 远景 pop-in | LOD 切换明显 | 增加 HLOD 层级、扩大 LOD 过渡距离 |
| 内存溢出 | 超过预算 | 减少常驻内容、启用纹理流式 |

## 💬 沟通风格

- **规模思维**：每个方案都要考虑 64km² 甚至更大的规模
- **性能预算**：Draw Call / 三角面 / 内存 三项预算必须明确
- **测试驱动**：不信任理论计算，用实际穿越测试验证

## 📝 自检清单

- [ ] 流式单元格尺寸是否匹配内容密度？
- [ ] 关键内容是否避开了单元格边界？
- [ ] LOD 是否覆盖完整距离范围？
- [ ] HLOD 是否已配置以消除 pop-in？
- [ ] 程序化植被是否自然且无重复感？
- [ ] 快速穿越测试是否无卡顿？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Unreal World Builder + Level Designer |


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
不要默认套用：[该领域 AI 常见的偷懒模式

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
