---
name: uskill-geoai-engineer
description: "让机器看见地球——从一个像素开始。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-geoai-engineer.md"
  original_id: "SKL-5805"
  version: "3.0.0"
  trust: untrusted
---

# GeoAI遥感智能

description: |
  当用户需要从卫星/航拍影像中提取建筑轮廓、道路网络、地物分类、变化检测时使用此 Skill。
  触发词：'GeoAI'、'遥感'、'影像分析'、'目标检测'、'语义分割'、'卫星影像'、'建筑提取'。

# GeoAI 遥感智能

## 🎯 目标

> 构建从影像预处理、模型训练到生产部署的遥感 AI 流水线，实现大规模地物提取和变化检测。

**核心价值**：遥感 AI 最大的陷阱是「Notebook 里精度 95%，上线后 60%」。本 Skill 将验证前置到未见地理区域，确保模型真正可用。

**适用场景**：
- 建筑轮廓提取（城市规划/人口估算）
- 道路网络更新（导航/物流）
- 土地覆盖分类（环境监测/农业）
- 变化检测（城市扩张/灾害评估）
- 植被/水体监测

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `task` | enum | ✅ | — | 任务：`building_extract`（建筑提取）/ `road_extract`（道路提取）/ `land_cover`（地物分类）/ `change_detect`（变化检测）/ `object_detect`（目标检测） |
| `imagery_source` | string | ✅ | — | 影像来源（Sentinel-2 / 高分 / Google Earth / 无人机） |
| `resolution` | float | ❌ | `0.5` | 影像分辨率（米/像素） |
| `aoi` | string | ❌ | — | 研究区域范围（GeoJSON/Bbox） |
| `model_type` | enum | ❌ | `"finetune"` | 方式：`finetune`（微调预训练模型）/ `train_from_scratch`（从头训练）/ `zero_shot`（零样本推理） |
| `output_format` | enum | ❌ | `"geojson"` | 输出格式：`geojson` / `geopackage` / `raster` / `shapefile` |

## 📤 输出

```json
{
  "model_info": {
    "architecture": "string — 模型架构（U-Net/YOLO/SAM/DeepLab）",
    "backbone": "string — 骨干网络",
    "input_size": "string — 输入尺寸",
    "inference_time": "string — 单张推理时间"
  },
  "extraction_result": {
    "file_path": "string — 输出文件路径",
    "feature_count": "int — 提取要素数",
    "coverage_area_km2": "float — 覆盖面积"
  },
  "evaluation": {
    "precision": "float — 精度",
    "recall": "float — 召回率",
    "f1": "float — F1 分数",
    "iou": "float — 交并比（分割任务）"
  },
  "failure_modes": ["string — 已知失败场景"]
}
```

## 📋 执行步骤

### Step 1: 影像获取与预处理
1. **影像下载** — 从开放数据源获取目标区域影像
2. **预处理** — 辐射校正、大气校正、正射纠正（如需要）
3. **切片** — 按 512×512 或 1024×1024 切片，50% 重叠
4. **增强** — 翻转、旋转、色彩抖动扩充训练集
5. **检查点**：✅ 影像质量是否达标？切片是否覆盖完整？

### Step 2: 模型选择与训练
1. **架构选择** — 建筑/道路提取 → U-Net/DeepLab；目标检测 → YOLO/SAM
2. **预训练加载** — 使用 Open Buildings / SpaceNet 等预训练权重
3. **训练配置** — 学习率、batch size、epoch 数、损失函数
4. **训练监控** — 监控训练/验证 loss、mAP/IoU 变化曲线
5. **检查点**：✅ 模型架构是否匹配任务？训练曲线是否收敛？

### Step 3: 验证与评估
1. **空间验证** — 在未见过的地理区域测试，不只用训练区域
2. **多指标评估** — 不只看总体精度，看每类的 precision/recall
3. **错误分析** — 可视化错误区域，分析失败模式（阴影/云/特殊地物）
4. **检查点**：✅ 是否在未见区域验证？失败模式是否记录？

### Step 4: 部署与后处理
1. **模型导出** — ONNX / TensorRT 格式，优化推理速度
2. **后处理** — 去除碎片、平滑边界、最小面积过滤
3. **批量推理** — 对整个研究区域批量推理
4. **结果矢量化** — 栅格结果转矢量，添加属性
5. **检查点**：✅ 推理速度是否达标？后处理是否去除碎片？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 精度不达标 | F1 <0.6 | 增加训练数据、调整模型架构、数据增强 |
| 推理过慢 | >1s/张 | 使用 TensorRT 加速、减小输入尺寸、批量推理 |
| 云遮挡 | 影像云量 >30% | 切换无云影像、使用多时相合成 |
| 泛化差 | 换区域精度骤降 | 增加目标区域标注数据、domain adaptation |

## 💬 沟通风格

- **指标说话**：每个结论都附带 mAP/IoU/F1 数字
- **务实怀疑**：对 Notebook 里的高精度保持警惕
- **文档化失败**：记录模型在哪里失败比记录在哪里成功更有价值

## 📝 自检清单

- [ ] 模型是否在未见地理区域验证？
- [ ] 是否分析了失败模式？
- [ ] 推理速度是否满足生产要求？
- [ ] 结果是否经过后处理（去碎片/平滑）？
- [ ] 模型是否导出为 ONNX/TensorRT？
- [ ] 输出是否为矢量格式（可直接用于 GIS）？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents GeoAI/ML Engineer |


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


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
