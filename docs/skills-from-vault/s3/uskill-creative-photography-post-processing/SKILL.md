---
name: uskill-creative-photography-post-processing
description: "让creative photography post processing变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-creative-photography-post-processing.md"
  original_id: "SKL-5015"
  version: "3.0.0"
  trust: untrusted
---

# creative photography post processing

# AI-Powered Photography Post-Processing

## 🎯 目标
> 建立一套以叙事增强和风格塑造为核心、由AI全面赋能的高效非破坏性摄影后期工作流，将单张精修作品处理时间缩短60%，实现从"记录"到"表达"的跃迁。

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `raw_photos` | array[path] | ✅ | RAW格式照片文件路径列表 |
| `emotion_keyword` | string | ✅ | 情感基调关键词，如"静谧"、"史诗感"、"温暖"、"孤独" |
| `narrative_core` | string | ✅ | 一句话描述照片的"故事核心"与创作意图 |
| `output_purpose` | enum | ✅ | 输出用途：`web` / `print` / `both` |
| `series_mode` | bool | ❌ | 是否为系列作品需统一样式，默认 `false` |
| `style_reference` | string | ❌ | 参考风格描述，如"王家卫风格"、"赛博朋克" |
| `max_output_width` | int | ❌ | Web输出长边像素，默认 2048 |

## 📤 输出

```json
{
  "edited_files": [
    {
      "source": "string — 原始文件路径",
      "non_destructive_edit": "string — 非破坏性编辑文件路径 (PSD/TIFF)",
      "exports": {
        "web": "string — sRGB JPEG路径 (可选)",
        "print": "string — Adobe RGB TIFF路径 (可选)"
      }
    }
  ],
  "style_preset": "string — 本次调色参数预设路径 (可选)",
  "processing_log": "string — 关键调整参数与思路记录"
}
```

## 📋 执行步骤

1. **导入并筛选** — 将RAW照片导入Lightroom，进行筛选、评级和标记，选出最佳候选
2. **确立叙事核心** — 回顾 `narrative_core` 和 `emotion_keyword`，明确每张照片最想传达的故事与视觉焦点
3. **分析原图** — 使用AI分析原图的优点与潜在问题（过曝、噪点、构图缺陷），生成2-3个后期处理方向建议
4. **校正镜头畸变** — 启用Lightroom配置文件校正和色差校正，消除光学瑕疵
5. **执行AI降噪** — 使用Lightroom AI降噪或Topaz插件对高ISO照片进行无损降噪
6. **调整基础影调** — 调整曝光、对比度、高光、阴影、白色/黑色色阶，确保直方图无溢出、影调完整均衡
7. **增强初步质感** — 适度调整纹理、清晰度和去朦胧滑块，增强画面质感
8. **创建AI蒙版** — 使用AI智能蒙版一键创建主体、天空、背景的精确选区
9. **引导视觉焦点** — 对主体增加曝光/对比度/锐度使其突出；对背景适当降低曝光或饱和度减少干扰
10. **重塑光影** — 使用线性渐变或径向渐变蒙版模拟光线方向，增强戏剧性并引导视线
11. **校准白平衡** — 使用白平衡工具校准画面基础色温色调
12. **执行HSL调色** — 分别调整主要颜色的色相、饱和度和明亮度，服务于 `emotion_keyword` 定义的情感基调
13. **应用创意色彩分级** — 使用高光/中间调/阴影色轮注入统一的电影感色彩风格；系列作品需确保组内一致性
14. **导出多格式文件** — 按 `output_purpose` 导出：Web为sRGB JPEG（长边 `max_output_width` 像素）、打印为Adobe RGB/ProPhoto RGB TIFF（原始分辨率）
15. **归档记录** — 在uPrompt或Obsidian中记录核心参数、调色思路和生成预设，便于复用

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `raw_photos` 路径无效或文件损坏 | 返回错误：`ERROR_INVALID_FILE`，列出无效路径 |
| 照片过曝/欠曝严重无法恢复 | 返回警告 + 建议降低该照片评级，继续处理其余照片 |
| AI蒙版识别不准确 | 提示手动修正蒙版边界，记录修正点供后续优化 |
| AI降噪引入伪影 | 降低降噪强度重试，或切换至手动降噪方案 |
| 系列作品色彩不一致 | 提示运行批量同步预设，以首张为基准统一后续照片 |
| 导出色彩空间不匹配 | 自动检测并警告，确认目标色彩空间后重新导出 |

## ✅ 自检清单

- [ ] 每张照片已用一句话明确定义"故事核心"和情感基调关键词
- [ ] 直方图分布均匀，无高光/阴影溢出，最亮最暗处保留足够细节
- [ ] AI蒙版边缘自然无明显锯齿，主体与背景调整无溢色
- [ ] 最终色彩方案成功营造预期情感氛围
- [ ] 肤色（如有人物）保持自然健康，无偏色
- [ ] 已按用途导出对应格式文件（Web: sRGB JPEG / Print: Adobe RGB TIFF）
- [ ] 非破坏性编辑文件和调色预设已妥善归档


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
| 2026-05-09 | 1.0.0 | 初始版本，从 SOP-15 转化 |

---
**相关笔记**：[[内容改编]] [[数据可视化]] 


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [摄影场景] for [拍摄者水平], with [创作优先级], leaning toward [器材/环境约束]."

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
| ""直接给一组参数就行了"" | "不知道用户场景就给参数，是赌博不是指导" |
| ""ISO 高一点没关系"" | "后期降噪损失细节，能前期解决就别留后期" |
| ""先拍一张试试看"" | "曝光三角的价值在于拍前就知道结果" |
| ""这个场景太简单了"" | "越简单越容易犯低级错误" |
| ""用户没问安全快门"" | "安全快门是糊片第一道防线，必须主动检查" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/a

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
