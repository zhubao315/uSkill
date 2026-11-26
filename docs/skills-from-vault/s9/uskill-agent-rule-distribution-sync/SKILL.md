---
name: uskill-agent-rule-distribution-sync
description: "让一次规则变更在 7 套循环工程与全部 Agent 间零误差落地，杜绝'有人还在用旧规'的漂移。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-rule-distribution-sync.md"
  original_id: "SKL-7107"
  version: "3.0.0"
  trust: untrusted
---

# 规则分发同步 Gen3 实施手册

description: |
  当用户需要将规则变更（AGENTS.md 硬约束、标签体系、uSkill 模块 Schema、循环工程调度契约等）
  同步至所有相关 Agent 与循环工程时使用此 Skill。
  触发词包括：'规则分发'、'规则同步'、'更新规则'、'规则漂移'、'一致性校验'、'批量下发'。
  即使用户没有说"规则"，只要意图涉及将某条规范推广到多个智能体/循环并保证一致，也应触发。
  不适用：单次性的个人笔记修改、与系统规则无关的纯内容创作。

---

# 📡 uSkill-7102: 规则分发同步（Gen3）

## 🎯 目标

> 将规则变更零误差地同步至所有相关 Agent 与 7 套循环工程（1每日+6专项），
> 生成含回滚方案的同步通知，并持续检测规则漂移，确保全系统规则一致性。

**适用场景**：修改 [[AGENTS]] 硬约束、标签体系迁移、uSkill Gen3 Schema 升级、
[[uSkill-agent-循环工程统一调度入口]] 调度契约变更后的全量下发。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `rule_change` | `object` | ✅ | 规则变更内容（路径/字段/旧值/新值/生效时间） |
| `affected_scope` | `array` | ❌ | 受影响范围（agent/loop/file），缺省则自动推导 |
| `dry_run` | `bool` | ❌ | 仅模拟分发不实际写入，默认 false |

---

## 📤 输出

```json
{
  "affected_targets": [
    {"target": "string", "type": "agent|loop|file", "sync_status": "synced|pending|failed|skipped"}
  ],
  "drift_detected": [{"target": "string", "expected": "string", "actual": "string"}],
  "rollback_plan": {"snapshot_ref": "string", "steps": ["string"]},
  "pending_confirmations": ["string"]
}
```

---

## 🔄 执行流程

```
1. [变更解析] → 提取规则变更内容
    → 变更类型：新增 / 修改 / 删除
    → 影响维度：硬约束 / 标签 / Schema / 调度契约
    → IF 变更涉及 AGENTS.md 硬约束 #1-#8：强制要求 dry_run 预演 + 人工签字
    → ELSE：进入自动识别分支

2. [目标识别] → 基于规则依赖图识别受影响目标
    → 遍历 7 套循环工程 + 全部 uSkill Agent 的依赖清单
    → IF Agent 声明依赖该规则：加入 affected_targets
    → IF 仅间接引用（如只是 wikilink）：标 skipped 并备注
    → ELSE：跳过

3. [漂移预检] → 分发前先扫描当前各目标实际值
    → IF 已存在与目标值不一致（旧漂移）：先记录 drift_detected 再覆盖
    → ELSE：直接写入

4. [通知生成] → 为每个目标生成同步通知
    → 通知内容：变更详情 + 生效时间 + rollback_plan
    → IF dry_run=true：输出模拟报告，不写入任何文件
    → ELSE：写入并标记 synced / pending

5. [状态闭环] → 确认全部接收
    → IF 全部 synced：输出"同步完成" + 漂移已清零
    → IF 存在 failed/pending：标注未同步目标 + 重试（最多3次）
    → IF 重试仍失败：升级人工，附 drift_detected 列表
```

---

## 📝 Prompt 模板

### 标准分发 Prompt

```
你是规则分发 Agent。请将以下规则变更同步到所有相关目标。

【规则变更】{rule_change}
【受影响范围】{affected_scope}
【模式】{dry_run ? "模拟" : "正式"}

【分发规则】
1. 解析变更类型与影响维度
2. 基于依赖图识别所有受影响 Agent / 循环 / 文件
3. 分发前先做漂移预检，记录已有不一致
4. 生成含回滚方案的同步通知并写入
5. 确认状态，失败重试，超次升级人工

【输出格式】
严格按标准 JSON 输出，包含 affected_targets、drift_detected、
rollback_plan、pending_confirmations。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| Agent / 循环离线 | 标注 pending + 重试 | 等待上线后补同步 |
| 规则冲突（新旧互斥） | 标注冲突 + 人工确认 | 暂不生效，保留旧规 |
| 涉及 AGENTS 硬约束 | 强制 dry_run + 人工签字 | 不自动写入 |
| 批量变更(>20目标) | 分批处理 | 每批完成后校验再下一批 |
| 写入失败(权限/锁) | 记录失败目标 | 回滚已写部分，整体重放 |

---

## ✅ 质量自检

- [ ] `rule_change` 含旧值与新值，可审计
- [ ] 每个 affected_target 都有明确的 sync_status
- [ ] 分发前已完成漂移预检并写出 drift_detected
- [ ] rollback_plan 含可执行的 snapshot_ref 与步骤
- [ ] 涉及硬约束的变更已走 dry_run + 人工签字
- [ ] 无目标被误伤（skipped 已正确标注）

---

## 💡 使用示例

### 示例 1：标签体系迁移分发

**输入**：
```json
{
  "rule_change": {"rule": "标签体系", "field": "维度", "old": "维度/技能", "new": "维度/学习", "effective": "2026-07-08T08:00"},
  "affected_scope": ["uSkill-agent-*", "循环工程统一调度入口"]
}
```

**输出**：
```json
{
  "affected_targets": [
    {"target": "uSkill-agent-社交资本", "type": "agent", "sync_status": "synced"},
    {"target": "循环工程统一调度入口", "type": "loop", "sync_status": "synced"}
  ],
  "drift_detected": [],
  "rollback_plan": {"snapshot_ref": "git:HEAD~1", "steps": ["git checkout HEAD~1 -- 02-BUILD/22-uSkill/", "重新触发分发"]},
  "pending_confirmations": []
}
```

### 示例 2：硬约束变更（边界）

**输入**：
```json
{
  "rule_change": {"rule": "AGENTS硬约束#3", "field": "全局搜索替换", "old": "允许", "new": "禁止"},
  "dry_run": true
}
```

**输出**：
```json
{
  "affected_targets": [{"target": "全部 Agent", "type": "agent", "sync_status": "skipped"}],
  "drift_detected": [],
  "rollback_plan": {"snapshot_ref": "n/a", "steps": ["本变更为模拟，未写入"]},
  "pending_confirmations": ["需人工签字后方可正式分发"]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | 正常分发 | 全部 synced |
| 2 | Agent 离线 | pending + 重试 |
| 3 | 规则冲突 | 标注冲突 + 不生效 |
| 4 | 无影响目标 | 空列表 / skipped |
| 5 | 硬约束变更 | 强制 dry_run + 签字 |
| 6 | 批量变更 | 分批校验 |

---

#### ⚠️ 边界约束

**硬性约束（必须遵守）**：
1. 不得违反相关法律法规和平台规则
2. 不得泄露用户隐私数据
3. 涉及 AGENTS 硬约束 #1-#8 的变更**必须*

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
