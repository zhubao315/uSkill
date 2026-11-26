---
name: uskill-agent-skillopt-optimization
description: "把'这个 Skill 又失败了'变成一次可复用的文档进化：定位根因、对齐 Gen3 Schema、闭环验证。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-skillopt-optimization.md"
  original_id: "SKL-7110"
  version: "3.0.0"
  trust: untrusted
---

# SkillOpt 技能优化 Gen3 实施手册

description: |
  当用户需要通过闭环优化 Skill 文档时使用此 Skill：分析执行失败案例、对照 Gen3 标准
  （[[Skill开发完全规范]]、[[P0升级清单]]）识别缺陷、生成针对性修订并更新文档。
  触发词包括：'Skill优化'、'技能优化'、'Skill改进'、'执行失败分析'、'Gen3 升级'、'文档重构'。
  即使用户没有明确说"优化"，只要意图涉及"这个 Agent 老出错/不达标/要升级到 Gen3"，也应触发。
  不适用：从零新建一个完全无关的 Skill（那走创作流程而非优化流程）。

---

# 🔧 uSkill-7105: SkillOpt 技能优化（Gen3）

## 🎯 目标

> 通过分析执行失败案例与 Gen3 审计缺口，定位 Skill 文档根因缺陷，生成对齐
> [[P0升级清单]] 9 模块标准的修订方案并闭环验证，让 Skill 越用越准。

**适用场景**：`uSkill_upgrade_audit.py` 不达标项的修复、运行期 failure_cases 复盘、
把旧版 Gen2/Gen1 文档升级为 Gen3 Schema。

---

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `skill_doc` | `string` | ✅ | 待优化的 Skill 文档路径 |
| `execution_feedback` | `string` | ✅ | 执行反馈（成功/失败/部分成功 + 现象） |
| `failure_cases` | `array` | ❌ | 失败案例详情（输入/实际输出/期望） |
| `target_standard` | `string` | ❌ | 目标标准，默认 `Gen3` |

---

## 📤 输出

```json
{
  "root_cause": "string",
  "gen3_gap": [{"check": "9模块|IF/THEN|Self-Play|行数|Frontmatter", "passed": "bool", "detail": "string"}],
  "issues": [{"type": "定义不清|流程缺失|边界遗漏|Prompt缺陷|Schema不符", "severity": "P0|P1|P2", "description": "string", "section": "string"}],
  "optimizations": [{"section": "string", "change": "string", "reason": "string"}],
  "verification": {"before_score": "number", "after_score": "number", "rerun_cmd": "string"}
}
```

---

## 🔄 执行流程

```
1. [Gen3 审计] → 先对 skill_doc 跑标准校验
    → 9 模块 H2 是否齐全（🎯目标/📥输入/📤输出/🔄执行流程/📝Prompt/⚠️异常/✅自检/💡示例/🧪Self-Play）
    → IF 缺模块：标 P0 gap，记入 gen3_gap
    → IF 行数<200 或 IF/THEN<3 或 Self-Play<5：标 P0 gap
    → ELSE：进入失败分析分支

2. [失败分析] → 结合 execution_feedback 分析
    → 定义不清：概念模糊导致理解偏差
    → 流程缺失：步骤不完整导致执行遗漏
    → 边界遗漏：异常未覆盖
    → Prompt缺陷：模板槽位/指令不准确
    → IF 反馈为"超时"：优先查执行流程是否缺超时/中断分支
    → ELSE IF 反馈为"分类错"：优先查输入 Schema 与判定规则

3. [缺陷定位] → 定位到具体 section
    → 检查：输入 Schema 是否完整？执行流程是否有 IF/THEN 分支？
    → 检查：异常处理是否覆盖？Self-Play ≥5 且真实？
    → IF 缺陷跨多 section：按严重度排序后批量修订

4. [优化建议] → 生成针对性修订
    → 规则：每条建议必须指向具体 section + 修改内容 + 原因
    → IF 改动 Frontmatter：校验 title/version/created/tags 等齐全

5. [文档更新+验证] → 输出修订并闭环
    → 保持原有结构，补充缺失、修正错误
    → THEN 重跑 uSkill_upgrade_audit.py，对比 before/after_score
    → IF after_score 仍不达标：返回步骤 2 二次迭代
```

---

## 📝 Prompt 模板

### 标准优化 Prompt

```
你是 Skill 优化 Agent。请对照 Gen3 标准优化以下 Skill。

【Skill 文档】{skill_doc}
【执行反馈】{execution_feedback}
【失败案例】{failure_cases}
【目标标准】{target_standard}

【优化维度】
1. Gen3 合规：9 模块 / IF≥3 / Self-Play≥5 / ≥200 行 / Frontmatter 齐全
2. 定义清晰度：概念是否精确、无歧义
3. 流程完整性：步骤是否有遗漏、是否有决策分支
4. 边界覆盖：异常是否处理、人工兜底是否明确
5. Prompt 准确性：模板槽位与指令是否有效

【硬性要求】
- 每条优化必须具体到 section，并说明修改原因
- 修订后必须可经 uSkill_upgrade_audit.py 验证

【输出格式】
严格按标准 JSON 输出，包含 root_cause、gen3_gap、issues、optimizations、verification。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 反馈信息不足 | 请求补充或仅做静态审计 | 基于文档本身分析 Gen3 gap |
| 无法定位缺陷 | 标"需进一步调查" | 输出通用改进建议清单 |
| 多个问题并存 | 按严重度排序 | 优先修复 P0（Gen3 硬约束） |
| 审计脚本缺失 | 改用人工清单核对 | 逐项比对 9 模块标准 |
| 修订引入新冲突 | 回滚该次 edit | 保留上一版并记录冲突原因 |

---

## ✅ 质量自检

- [ ] gen3_gap 覆盖全部 5 项硬约束且结论明确
- [ ] 每条 issue 都定位到具体 section
- [ ] 每条 optimization 含 change + reason，非泛泛而谈
- [ ] 涉及 Frontmatter 的改动已校验字段齐全
- [ ] verification 含可复跑的 rerun_cmd 与前后分对比
- [ ] 无虚构失败案例，引用真实现象

---

## 💡 使用示例

### 示例 1：Gen3 模块缺失

**输入**：
```json
{
  "skill_doc": "uSkill-邮件处理-v1.md",
  "execution_feedback": "审计未通过：仅 198 行，缺 ✅质量自检 模块",
  "failure_cases": ["uSkill_upgrade_audit 报 missing_module=质量自检"]
}
```

**输出**：
```json
{
  "root_cause": "文档在重构时遗漏了 ✅ 质量自检 模块，且总行数不足 200",
  "gen3_gap": [{"check": "9模块", "passed": false, "detail": "缺 ✅质量自检"}, {"check": "行数", "passed": false, "detail": "198<200"}],
  "issues": [{"type": "Schema不符", "severity": "P0", "description": "缺少质量自检 checklist", "section": "✅ 质量自检"}],
  "optimizations": [
    {"section": "✅ 质量自检", "change": "新增输出结构/内容/合规三类 checklist（≥6 项）", "reason": "满足 Gen3 9 模块硬约束"},
    {"section": "全文", "change": "扩充使用示例至 2 个边界场景，+12 行", "reason": "行数达 200 阈值"}
  ],
  "verification": {"before_score": 71, "after_score": 100, "rerun_cmd": "python3 uSkill_upgrade_audit.py uSkill-邮件处理-v1.md"}
}
```

### 示例 2：执行超时（边

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
