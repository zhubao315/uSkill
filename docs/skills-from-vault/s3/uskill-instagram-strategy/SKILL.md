---
name: uskill-instagram-strategy
description: "Instagram 不是照片墙，是你的视觉名片。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-instagram-strategy.md"
  original_id: "SKL-5709"
  version: "3.0.0"
  trust: untrusted
---

# Instagram视觉运营

description: |
  当用户需要运营 Instagram 账号、打造视觉风格、提升互动率时使用此 Skill。
  触发词：'Instagram'、'ins运营'、'Reels'、'Stories'、'视觉风格'。

# [[Instagram视觉运营]]

## 🎯 目标

> 建立统一的视觉语言体系，利用 Feed/Reels/Stories 三种内容形态实现品牌表达和粉丝增长。

**核心价值**：Instagram 是视觉优先的平台，本 Skill 将内容策略对齐算法偏好（Reels 优先）和视觉一致性。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `brand_theme` | string | ✅ | — | 品牌/个人主题（如"极简科技""城市探索"） |
| `content_mix` | enum | ❌ | `"reels_first"` | 内容比例：`reels_first`（Reels为主）/ `feed_first`（Feed为主）/ `balanced`（均衡） |
| `visual_style` | enum | ❌ | `"clean"` | 视觉风格：`clean`（干净）/ `moody`（氛围感）/ `vibrant`（鲜艳）/ `minimal`（极简） |
| `posting_freq` | enum | ❌ | `"daily"` | 发布频率：`daily` / `3x_weekly` / `weekly` |

## 📤 输出

```json
{
  "visual_guidelines": {
    "color_palette": ["string — 主色调"],
    "fonts": "string — 字体规范",
    "editing_style": "string — 修图风格描述",
    "grid_pattern": "string — Feed 排列规律"
  },
  "content_calendar": [{"day": "string", "type": "string", "topic": "string"}],
  "caption_template": "string — 文案模板（含 CTA 和 hashtag 位置）",
  "hashtag_sets": [{"tier": "string", "tags": ["string"]}],
  "reels_concept": "string — Reels 内容方向和拍摄建议",
  "stories_plan": "string — Stories 日常内容规划"
}
```

## 📋 执行步骤

### Step 1: 视觉体系建立
1. **色调统一** — 选定 3-5 个主色调，所有图片使用一致的滤镜/调色
2. **Grid 规划** — Feed 排列规律：棋盘格/三行一循环/渐变色排列
3. **字体规范** — 选定 1-2 个字体，用于 Story 和图文叠加
4. **检查点**：✅ 视觉风格是否有辨识度？Grid 是否统一？

### Step 2: Reels 内容策略
1. **算法偏好** — Instagram 优先推荐 Reels，时长 15-60 秒最佳
2. **钩子设计** — 前 3 秒必须抓住注意力（动态画面/悬念/反差）
3. **趋势利用** — 关注热门音频/挑战，结合自身内容参与
4. **检查点**：✅ Reels 前 3 秒是否足够吸引？是否利用了热门趋势？

### Step 3: 文案与标签
1. **文案结构** — Hook（开头钩子）→ 价值（核心内容）→ CTA（互动引导）
2. **标签策略** — 3 个大标签（100万+）+ 5 个中标签（10-100万）+ 7 个小标签（1-10万）
3. **互动引导** — "Save this for later""Tag a friend""Drop a comment"
4. **检查点**：✅ 文案是否有 CTA？标签是否覆盖三个层级？

### Step 4: Stories 运营
1. **日常分享** — 幕后花絮/日常片段/真实瞬间
2. **互动功能** — 善用投票/问答/测验等互动贴纸
3. **Highlight 整理** — 将重要 Stories 归类到 Highlight
4. **检查点**：✅ Stories 是否有互动功能？Highlight 是否分类整理？

## ⚠️ 异常处理

| 异常 | 条件 | 处理方式 |
|------|------|----------|
| 互动率低 | <2% | 优化视觉质量、增加 CTA、参与热门趋势 |
| 粉丝增长慢 | 月增 <2% | 增加 Reels 比例、参与热门挑战、跨平台推广 |
| Reach 下降 | 连续下降 | 检查发布频率、优化标签策略、增加互动 |

## 💬 沟通风格

- **视觉优先**：先说画面怎么拍，再说文案怎么写
- **简洁优雅**：文案精炼，用 emoji 增加可读性
- **国际范**：用英文关键词覆盖全球受众，中文内容辅助说明

## 📝 自检清单

- [ ] 视觉风格是否统一？
- [ ] Grid 排列是否有规律？
- [ ] Reels 前 3 秒是否有钩子？
- [ ] 文案是否包含 CTA？
- [ ] 标签是否覆盖大/中/小三个层级？
- [ ] Stories 是否有互动功能？

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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents Instagram Curator |


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

## 🛡️ Three-Tier Boundaries `[v3

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
