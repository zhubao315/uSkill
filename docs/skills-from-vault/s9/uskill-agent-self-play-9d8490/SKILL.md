---
name: uskill-agent-self-play-9d8490
description: "让uSkill 质量分级与 Self-Play 框架变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-质量分级与-self-play-框架.md"
  original_id: "SKL-7052"
  version: "3.0.0"
  trust: untrusted
---

# uSkill 质量分级与 Self-Play 框架

# 🧠 uSkill 质量分级与 Self-Play 框架

> **Q3 目标**：复用率审计 + 质量分级（A/B/C）+ Self-Play 首轮 + C 级清零
> **时间跨度**：2026-07-01 → 2026-09-30
> **关联**：[[uSkill-agent-技能推理器孤岛审计]] · [[uSkill-系统熵增检测-v1]] · [[2026-Q3-OKR-草稿]]

---

## 一、质量分级体系

### 1.1 三级分级标准

| 级别 | 定义 | 复用率 | Schema 完整度 | Self-Play 通过率 |
|:----:|------|:------:|:-------------:|:----------------:|
| **A** | 生产级，可直接调用 | ≥30% | 100% | ≥80% |
| **B** | 可用级，需小幅优化 | 10%-30% | ≥80% | ≥50% |
| **C** | 孤岛级，需重构或淘汰 | <10% | <80% | <50% |

### 1.2 评分维度

```yaml
# skill_grading_rubric.yaml
dimensions:
  - name: "复用率"
    weight: 0.35
    metrics:
      - "调用次数（季度）"
      - "被其他 Agent 引用次数"
      - "触发词匹配命中率"

  - name: "Schema 完整度"
    weight: 0.25
    metrics:
      - "input_variables 定义完整"
      - "output_format 明确"
      - "trigger_words 覆盖"
      - "dependencies 声明"

  - name: "Self-Play 得分"
    weight: 0.25
    metrics:
      - "对抗测试集通过率"
      - "边界 case 处理"
      - "错误恢复能力"

  - name: "文档质量"
    weight: 0.15
    metrics:
      - "frontmatter 规范"
      - "使用示例完整"
      - "关联链接有效"
```

### 1.3 综合评分公式

```
Skill Score = 复用率得分 × 0.35 + Schema得分 × 0.25 + Self-Play得分 × 0.25 + 文档得分 × 0.15

分级阈值：
  A 级：Score ≥ 0.7
  B 级：0.4 ≤ Score < 0.7
  C 级：Score < 0.4
```

---

## 二、Phase 1：复用率审计脚本（7/1 → 8/15）

### 目标
开发审计脚本，首次完成全库复用率测量。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T1.1 | 审计脚本设计 | `skill_audit_spec.md` | 7/15 | — |
| T1.2 | 复用率计算模块 | `skill_audit_reuse.py` | 7/31 | T1.1 |
| T1.3 | Schema 检查模块 | `skill_audit_schema.py` | 8/5 | T1.1 |
| T1.4 | 综合评分模块 | `skill_audit_score.py` | 8/10 | T1.2+T1.3 |
| T1.5 | 首次全库审计 | `审计报告-2026-08.md` | 8/15 | T1.4 |

### 复用率计算逻辑

```python
def calculate_reuse_rate(skill_path: str) -> float:
    """
    计算单个 Skill 的复用率

    复用率 = (被引用次数 + 调用次数) / (总 Skill 数 × 季度周数)
    """
    skill_name = extract_name(skill_path)

    # 1. 统计被引用次数（wikilink）
    ref_count = count_wikilinks(skill_name, vault_path)

    # 2. 统计调用次数（从 twin_distill_log.jsonl 提取）
    call_count = count_skill_calls(skill_name, log_path)

    # 3. 计算复用率
    total_possible = total_skills * weeks_in_quarter
    reuse_rate = (ref_count + call_count) / total_possible

    return min(reuse_rate, 1.0)  # 上限 100%
```

### 审计报告模板

```markdown
# uSkill 审计报告 — 2026 Q3

## 总览
| 指标 | 数值 |
|------|:----:|
| 总 Skill 数 | XXX |
| A 级 | XX (XX%) |
| B 级 | XX (XX%) |
| C 级 | XX (XX%) |
| 平均复用率 | XX% |

## Top 20 高频 Skill
| 排名 | Skill | 复用率 | 级别 |
|:----:|-------|:------:|:----:|
| 1 | ... | XX% | A |

## C 级 Skill 清单（需重构/淘汰）
| Skill | 复用率 | 问题 | 建议 |
|-------|:------:|------|------|
| ... | X% | 孤岛 | 重构 |

## 改进建议
```

---

## 三、Phase 2：Top 20 优化（8/16 → 8/31）

### 目标
Top 20 高频 Skill 复用率提升至 ≥30%。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T2.1 | Top 20 Skill 诊断 | 诊断报告 | 8/20 | Phase 1 |
| T2.2 | 优化方案设计 | `skill_optimization_plan.md` | 8/23 | T2.1 |
| T2.3 | 批量优化执行 | 20 个 Skill 更新 | 8/28 | T2.2 |
| T2.4 | 优化效果验证 | 验证报告 | 8/31 | T2.3 |

### 优化策略矩阵

| 问题类型 | 诊断信号 | 优化策略 | 预期效果 |
|----------|---------|---------|---------|
| Schema 不完整 | 缺少 input/output 定义 | 补全 Schema 字段 | +10% 复用率 |
| 触发词缺失 | 无 trigger_words | 添加 3-5 个触发词 | +15% 命中率 |
| 文档缺失 | 无使用示例 | 添加 2-3 个示例 | +5% 可理解性 |
| 关联断裂 | 无 wikilink | 织入 3+ 关联链接 | +10% 发现率 |
| Prompt 低质 | 模糊/过长 | 精简 + 结构化 | +20% 执行质量 |

---

## 四、Phase 3：Self-Play 首轮（9/1 → 9/15）

### 目标
10 个 Skill 通过对抗测试集，验证生产级质量。

### 任务分解

| # | 任务 | 产出物 | 截止 | 依赖 |
|---|------|--------|:----:|------|
| T3.1 | 对抗测试集设计 | `self_play_test_set.yaml` | 9/3 | Phase 2 |
| T3.2 | Self-Play 引擎 | `skill_self_play.py` | 9/8 | T3.1 |
| T3.3 | 首轮测试执行 | 测试报告 | 9/12 | T3.2 |
| T3.4 | 问题修复 | Skill 更新 | 9/15 | T3.3 |

### 对抗测试集设计

```yaml
# self_play_test_set.yaml
test_categories:
  - name: "happy_path"
    description: "正常输入场景"
    weight: 0.3
    cases:
      - input: "标准输入"
        expected: "符合 output_format"

  - name: "edge_cases"
    description: "边界情况"
    weight: 0.3
    cases:
      - input: "空输入"
        expected: "优雅降级"
      - input: "超长输入"
        expect

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
