---
name: uskill-agent-community-ops
description: "让社群从\"每日巡检\"变成可持续发酵的社交资本资产，而非停留在台账记录。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-community-ops.md"
  original_id: "SKL-7106"
  version: "3.0.0"
  trust: untrusted
---

# 社群运维 Gen3 实施手册

description: |
  当用户需要执行社群日常运维、巡检群组活跃度、识别高价值内容、生成互动回复或
  触发关系衰减预警时使用此 Skill。
  触发词包括：'社群巡检'、'社群运维'、'社群管理'、'群活跃度'、'关系衰减'、'高价值内容'。
  即使用户没有明确说"社群"，只要意图涉及多人群组运营、IP 私域沉淀、社交资本积累，也应触发。
  不适用：单人群发广告、纯客服工单系统、与社群无关的内容创作。

---

# 👥 uSkill-7101: 社群运维（Gen3）

## 🎯 目标

> 基于规则完成社群日常运维：巡检活跃度、识别高价值互动、生成语境化回复建议，
> 并对进入衰减期的群组提前发出预警，把社群沉淀为可持续发酵的社交资本。

**适用场景**：知识星球 / 微信群 / Discord / 私域社群的每日巡检；KOL-IP 内容爆发路线图中的
关系网络运营；与 [[uSkill-agent-社交资本与-ip-内容爆发路线图]] 协同。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `communities` | `array` | ✅ | 待巡检社群列表（名称/平台/近30天基线） |
| `window` | `string` | ❌ | 巡检时间窗，默认 `24h` |
| `pending_items` | `array` | ❌ | 待处理 @提及 / 私信 / 常见问题 |
| `identity` | `object` | ❌ | 该群运营身份定位（专家/陪伴/资源枢纽） |

---

## 📤 输出

```json
{
  "activity": [
    {"community": "string", "active_users": "number", "new_members": "number",
     "delta_vs_baseline": "number", "trend": "up|flat|down"}
  ],
  "high_value_content": [
    {"content": "string", "author": "string", "type": "技术分享|问题讨论|资源推荐|情绪共鸣", "score": "number"}
  ],
  "reply_suggestions": [{"to": "string", "draft": "string", "tone": "string"}],
  "decay_alerts": [{"community": "string", "silence_days": "number", "reason": "string"}],
  "pending_actions": [{"action": "string", "priority": "P0|P1|P2"}]
}
```

---

## 🔄 执行流程

```
1. [活跃度巡检] → 拉取各群近 window 消息、活跃用户、新增成员
    → 计算 delta_vs_baseline（环比近30天均值）
    → IF delta < -30%：标注"低活跃预警"，进入衰减分析分支
    → IF delta >= 0：标记正常，写入趋势字段
    → IF 无消息且历史基线>20条/日：直接触发 decay_alert（静默=异常）

2. [待处理回复] → 处理 @提及 / 私信 / 常见问题
    → 识别意图：答疑 / 求助 / 投诉 / 商务
    → IF 意图=投诉或负面：生成"先共情+转人工"草稿，不自动发布
    → IF 意图=商务合作：标注 P0，建议私密对接而非群内回复
    → ELSE：按 identity.tone 生成语境化草稿

3. [高价值识别] → 识别值得放大的内容
    → 计分：点赞>5(+2) 评论>3(+2) 被引用(+3) 引发二次讨论(+2)
    → IF score >= 7：标注为"可二创素材"，联动 IP 内容爆发路线图
    → ELSE IF 3<=score<7：标为普通优质，纳入周报
    → ELSE：不收录

4. [衰减预警] → 对低活跃/静默群归因
    → IF 连续静默 >= 7天：发 decay_alert，归因（话题枯竭/关键人流失/季节）
    → IF 归因=关键人流失：建议定向唤醒（私信核心成员）
    → ELSE：建议发起话题/活动重启

5. [输出报告] → 组装 activity + high_value + reply + decay + pending
    → IF 任一 decay_alert：在报告顶部用 ⚠️ 高亮
```

---

## 📝 Prompt 模板

### 标准巡检 Prompt

```
你是社群运维 Agent。请对以下社群执行今日巡检并产出结构化报告。

【社群列表】{communities}
【巡检窗口】{window}
【待处理事项】{pending_items}
【运营身份】{identity}

【巡检维度】
1. 活跃度：消息数、活跃用户、新增成员、环比基线
2. 待回复：@提及、私信、常见问题（按意图分类）
3. 高价值内容：点赞>5、评论>3、被引用、二次讨论
4. 衰减信号：连续静默天数、关键人发言频率

【风控规则】
- 负面/投诉内容：只出草稿，转人工，禁止自动发布
- 商务内容：P0 私密对接，不在群内公开回复

【输出格式】
严格按标准 JSON 输出，包含 activity、high_value_content、
reply_suggestions、decay_alerts、pending_actions。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 社群无消息 | 判为静默，触发衰减分析 | 不生成活跃度报告，仅出 decay_alert |
| 负面/冲突内容 | 标注+生成安抚草稿 | 不自动回复，强制转人工 |
| 大量待处理(>50) | 按意图+紧急度排序 | 仅处理 P0/P1，其余入队列 |
| 平台 API 限流 | 记录断点 | 基于本地已有缓存分析，标注"数据可能不全" |
| 身份定位缺失 | 用默认"陪伴型"语气 | 输出提示用户补全 identity |

---

## ✅ 质量自检

- [ ] 每个社群都有 `delta_vs_baseline` 与 `trend` 字段
- [ ] 高价值内容 `score` 可解释（列出加分项）
- [ ] 负面内容未被自动发布，已转人工
- [ ] 静默群均进入衰减分支并给出归因
- [ ] 回复草稿语气与 `identity.tone` 一致
- [ ] 无虚构数据，所有计数来自真实拉取

---

## 💡 使用示例

### 示例 1：正常巡检 + 高价值识别

**输入**：
```json
{
  "communities": [{"name": "AI技术群", "platform": "wechat", "baseline_msgs": 45}],
  "window": "24h",
  "pending_items": [{"type": "question", "content": "如何部署 RAG 系统？", "from": "user123"}],
  "identity": {"tone": "专家型"}
}
```

**输出**：
```json
{
  "activity": [{"community": "AI技术群", "active_users": 12, "new_members": 3, "delta_vs_baseline": 5, "trend": "up"}],
  "high_value_content": [{"content": "RAG 架构最佳实践长文", "author": "user456", "type": "技术分享", "score": 9}],
  "reply_suggestions": [{"to": "user123", "draft": "建议先固定切分策略再调召回，附一篇我之前写的对比表。", "tone": "专家型"}],
  "decay_alerts": [],
  "pending_actions": [{"action": "将 user456 长文纳入周报二创候选", "priority": "P2"}]
}
```

### 示例 2：衰减预警（边界）

**输入**：
```json
{
  "communities": [{"name": "读书会", "platform": "wechat", "baseline_msgs": 30}],
  "window": "24h"
}
```

**输出**：
```json
{
  "activity": [{"community": "读书会", "active_users": 0, "new_members": 0, "delta_vs_baseline": -100, "trend": "down"}],


> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
