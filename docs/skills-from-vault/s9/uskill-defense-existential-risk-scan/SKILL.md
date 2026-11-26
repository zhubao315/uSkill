---
name: uskill-defense-existential-risk-scan
description: "在系统真的崩掉之前，先把那个低概率高影响的'要是……怎么办'想清楚、写下来、备好预案。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-defense-existential-risk-scan.md"
  original_id: "SKL-7109"
  version: "3.0.0"
  trust: untrusted
---

# 存在性风险扫描 Gen3 实施手册

description: |
  当用户需要识别可能危及系统存续的尾部风险时使用此 Skill：知识库/投资系统/线上服务的
  低概率高影响事件扫描、最坏情景推演、应急预案生成。
  触发词包括：'存在性风险'、'尾部风险'、'黑天鹅'、'系统安全'、'崩溃预案'、'最坏情况'。
  即使用户没有明确说"风险"，只要意图涉及"如果 X 崩了怎么办""我们的单点在哪里"，也应触发。
  不适用：日常的、可逆的小故障处理（那属于运维而非存在性风险）。

---

# ☠️ uSkill-7104: 存在性风险扫描（Gen3）

## 🎯 目标

> 识别低概率高影响事件，评估最坏情景，生成"预防—检测—响应—恢复"四步应急预案，
> 让系统在真正的尾部冲击到来前具备韧性。

**适用场景**：[[uLife OS]] 知识库（Obsidian + Syncthing）数据资产保全、个人投资系统
（见 [[我的交易系统]]、[[对冲信号监测器]]）回撤与集中度风险、线上服务可用性。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `system` | `string` | ✅ | 系统描述（含关键依赖） |
| `status` | `object` | ✅ | 当前状态数据（资产/备份/集中度/依赖） |
| `horizon` | `string` | ❌ | 评估时间窗，默认 `12m` |

---

## 📤 输出

```json
{
  "risks": [
    {"risk": "string", "layer": "技术|运营|市场|外部", "probability": "极低|低|中|高", "impact": "可忽略|中等|严重|致命", "mitigation": "string"}
  ],
  "worst_case": "string",
  "defense_measures": [{"phase": "预防|检测|响应|恢复", "action": "string"}],
  "early_warning_signals": ["string"]
}
```

---

## 🔄 执行流程

```
1. [风险扫描] → 四层扫描系统脆弱点
    → 技术层：数据丢失、系统崩溃、安全漏洞、单点依赖
    → 运营层：关键人离开、资金链断裂、流程失效
    → 市场层：竞品颠覆、政策变化、系统性回调
    → 外部层：自然灾害、法律诉讼、供应链中断
    → IF 系统依赖外部 API：必查 API 停服/限流/涨价风险
    → IF 系统存储用户/个人数据：必查隐私合规与勒索风险

2. [概率评估] → 量化每个风险发生概率
    → 极低：<1%/年 | 低：1-5% | 中：5-20% | 高：>20%
    → IF 历史曾发生同类事件：概率上调一档

3. [影响评估] → 量化最坏影响
    → 可忽略：轻微不便 | 中等：需额外资源 | 严重：核心功能受损 | 致命：系统无法运行
    → IF impact=致命：强制进入应急预案分支（不可跳过）

4. [应急预案] → 四步法生成
    → 预防：降低发生概率的具体动作
    → 检测：可观测的早期预警信号
    → 响应：发生后的前 30 分钟处置步骤
    → 恢复：回到正常运营的回滚/重建步骤
    → THEN 输出 预防+检测+响应+恢复 四段方案

5. [输出报告] → 风险清单 + 最坏情景 + 防御措施 + 预警信号
    → IF 任一风险 impact=致命：报告顶部用 ☠️ 高亮
```

---

## 📝 Prompt 模板

### 标准扫描 Prompt

```
你是存在性风险扫描 Agent。请扫描以下系统的存在性风险。

【系统描述】{system}
【当前状态】{status}
【评估窗口】{horizon}

【扫描维度】
1. 技术风险：数据、安全、可用性、外部依赖
2. 运营风险：人员、资金、流程
3. 市场风险：竞争、政策、趋势
4. 外部风险：自然、法律、供应链

【风险分级】
- 致命：系统无法运行 | 严重：核心功能受损
- 中等：需额外资源 | 可忽略：轻微不便

【硬性要求】
- 致命风险必须给出 预防/检测/响应/恢复 四步预案
- 每个风险须给出可观测的早期预警信号

【输出格式】
严格按标准 JSON 输出，包含 risks、worst_case、defense_measures、early_warning_signals。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 系统信息不完整 | 基于已有信息评估 | 标注"信息不完整"，缺口列明 |
| 无法评估概率 | 标为"待评估" | 用历史同类事件推断并标注置信度 |
| 多致命风险叠加 | 按影响×概率排序 | 输出优先级处置序列 |
| 涉及监管/法律 | 仅给框架不替决策 | 强制转人工合规审查 |

---

## ✅ 质量自检

- [ ] 四层（技术/运营/市场/外部）均已覆盖，无遗漏
- [ ] 每个风险含 layer、probability、impact 三维
- [ ] 致命风险 100% 有四步预案
- [ ] 每个风险至少 1 个 early_warning_signal
- [ ] worst_case 描述具体、可想象
- [ ] 无虚构概率，推断均标注来源

---

## 💡 使用示例

### 示例 1：知识库风险扫描

**输入**：
```json
{
  "system": "uLife 知识库（Obsidian 本地 + Syncthing 多端同步，约 8,200 篇笔记）",
  "status": {"total_notes": 8200, "backup_last": "2026-07-07", "sync_conflicts": 0, "external_api": false}
}
```

**输出**：
```json
{
  "risks": [
    {"risk": "Syncthing 同步冲突导致笔记被错误覆盖", "layer": "技术", "probability": "低", "impact": "致命", "mitigation": "每日自动备份 + 冲突检测告警"},
    {"risk": "磁盘/设备物理损坏致本地数据丢失", "layer": "技术", "probability": "低", "impact": "严重", "mitigation": "3-2-1 备份策略（本地+异地+离线）"}
  ],
  "worst_case": "本地数据 + 云端备份同时失效，知识库完全损毁且无法恢复",
  "defense_measures": [
    {"phase": "预防", "action": "每日 02:00 增量备份到异地加密存储"},
    {"phase": "检测", "action": "监控 sync-conflict 文件与备份任务失败"},
    {"phase": "响应", "action": "暂停同步，隔离损坏库，启用上一日备份"},
    {"phase": "恢复", "action": "从异地备份重建并逐篇 diff 校验"}
  ],
  "early_warning_signals": ["出现 sync-conflict 文件", "备份任务连续失败", "磁盘 SMART 告警"]
}
```

### 示例 2：投资系统风险扫描（边界）

**输入**：
```json
{
  "system": "个人投资系统（ETF + 个股，总资约 277 万）",
  "status": {"total_assets": 2770000, "concentration": 0.7, "external_api": true}
}
```

**输出**：
```json
{
  "risks": [
    {"risk": "行业集中度过高(70%)，科技板块系统性回调", "layer": "市场", "probability": "中", "impact": "严重", "mitigation": "降集中度至 30% 以内"},
    {"risk": "行情/交易 API 停服致无法调仓", "layer": "技术", "probability": "低", "impact": "中等", "mitigation": "备用数据源 + 手动下单预案"}
  ],
  "worst_case": "集中持仓遭遇板块黑天鹅，单月回撤超 30% 且流动性枯竭",
  "defense_measures": [
    {"phase": "预防", "action": "设置单行业上限 30%，触发即再平衡"},
    {"phase": "检测", "action": "每日监控集中度与回撤，超阈告警"},
    {"phase": "响应", "action": "启动对冲/减仓，暂停新开仓"},
    {"p

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
