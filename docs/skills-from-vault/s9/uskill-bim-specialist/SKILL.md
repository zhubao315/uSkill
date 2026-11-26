---
name: uskill-bim-specialist
description: "BIM 不是 3D 模型——它是建筑全生命周期的数据容器。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-bim-specialist.md"
  original_id: "SKL-5807"
  version: "3.0.0"
  trust: untrusted
---

# BIM与建筑信息模型

description: |
  当用户需要处理 BIM 模型、IFC 数据交换、碰撞检测、建筑信息管理时使用此 Skill。
  触发词：'BIM'、'IFC'、'建筑信息模型'、'碰撞检测'、'Revit'、'Navisworks'、'LOD'。

# BIM 与建筑信息模型

## 🎯 目标

> 将 BIM 模型从「好看的 3D」转化为「可查询、可分析、可运维」的数据资产。

**核心价值**：BIM 的价值不在模型本身，在于模型承载的信息。本 Skill 确保模型数据完整、交换标准、可服务于设计/施工/运维全生命周期。

**适用场景**：
- 建筑设计方案审查与碰撞检测
- 城市更新项目中的既有建筑信息管理
- GIS-BIM 融合（城市级建筑信息集成）
- 施工进度模拟与成本估算

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task_type` | enum | ✅ | — | 任务：`validation`（模型验证）/ `collision`（碰撞检测）/ `integration`（GIS-BIM 融合）/ `extraction`（信息提取）/ `conversion`（格式转换） |
| `input_format` | enum | ❌ | `"ifc"` | 输入格式：`ifc` / `rvt` / `nwd` / `gbxml` |
| `output_format` | enum | ❌ | `"ifc"` | 输出格式：`ifc` / `geojson` / `3dtiles` / `citygml` |
| `lod_target` | enum | ❌ | `"LOD3"` | 目标 LOD：`LOD1`（体量）/ `LOD2`（外壳）/ `LOD3`（详细）/ `LOD4`（运维） |
| `disciplines` | array | ❌ | `["structural","mep"]` | 涉及专业 |

## 📤 输出

```json
{
  "validation_report": {
    "completeness": "float — 属性完整率 (%)",
    "ifc_compliance": "string — IFC 合规性检查结果",
    "missing_properties": ["string — 缺失的关键属性"]
  },
  "collision_report": {
    "total_clashes": "int — 碰撞总数",
    "by_severity": {"critical": "int", "major": "int", "minor": "int"},
    "by_discipline": {"string": "int"},
    "resolution_plan": "string — 处理方案"
  },
  "extraction_result": {
    "file_path": "string — 输出文件路径",
    "feature_count": "int — 提取的构件数",
    "attributes": ["string — 导出的属性字段"]
  }
}
```

## 📋 执行步骤

### Step 1: 模型验证
1. **IFC 合规性** — 检查模型是否符合 IFC 2x3/4 标准
2. **属性完整性** — 检查关键构件的必要属性是否齐全
3. **几何质量** — 检查重叠面、法线方向、闭合体积
4. **LOD 检查** — 构件精度是否与目标 LOD 等级匹配
5. **检查点**：✅ IFC 合规？属性完整率 ≥90%？

### Step 2: 碰撞检测
1. **硬碰撞** — 构件之间的物理交叉
2. **软碰撞** — 间距不满足规范要求
3. **工作流碰撞** — 施工顺序冲突
4. **分级报告** — 按严重程度分级：临界/重大/轻微
5. **检查点**：✅ 是否覆盖所有专业？是否分级标注？

### Step 3: GIS-BIM 融合
1. **坐标对齐** — BIM 局部坐标 → 地理坐标（WGS84/地方坐标系）
2. **LOD 适配** — 根据 GIS 应用场景调整模型精度
3. **属性映射** — BIM 属性 → GIS 要素属性字段
4. **格式转换** — IFC → CityGML / 3D Tiles / GeoJSON
5. **检查点**：✅ 坐标是否正确对齐？属性映射是否完整？

### Step 4: 信息提取与交付
1. **按类型提取** — 提取墙体/门窗/楼板/管道等特定构件
2. **属性导出** — 材质/尺寸/造价/施工阶段等
3. **可视化验证** — 在 GIS 平台中验证提取结果
4. **检查点**：✅ 提取构件是否完整？属性是否正确？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| IFC 版本不兼容 | IFC 2x3 vs IFC4 | 使用 IfcOpenShell 进行版本转换 |
| 碰撞数过多 | >1000 个 | 先处理临界碰撞，批量排除重复 |
| 坐标偏移 | BIM 与 GIS 位置不一致 | 检查坐标系定义，手动校准控制点 |

## 💬 沟通风格

- **工程精度**：坐标精确到毫米，属性精确到字段
- **全生命周期思维**：模型不只是给设计师看，还要给施工方和运维方用
- **标准导向**：一切以 IFC/ISO 标准为准，不自创格式

## 📝 自检清单

- [ ] IFC 合规性检查是否通过？
- [ ] 关键属性完整率是否 ≥90%？
- [ ] 碰撞检测是否覆盖所有专业？
- [ ] BIM-GIS 坐标是否正确对齐？
- [ ] LOD 等级是否与项目阶段匹配？
- [ ] 输出格式是否满足下游消费者需求？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents BIM Specialist |


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
| ""这跟我无关""

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
