
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
        expected: "截断处理"
      - input: "特殊字符"
        expected: "转义处理"

  - name: "adversarial"
    description: "对抗性输入"
    weight: 0.4
    cases:
      - input: "Prompt 注入尝试"
        expected: "拒绝执行"
      - input: "矛盾指令"
        expected: "识别冲突"
      - input: "超出能力范围"
        expected: "明确拒绝"
```

### Self-Play 执行流程

```
┌─────────────────────────────────────────────────┐
│              Self-Play Test Runner               │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. 加载 Skill Prompt + Schema                  │
│           ↓                                     │
│  2. 加载测试集（happy_path + edge + adversarial）│
│           ↓                                     │
│  3. 逐条执行：                                  │
│     ├── 注入测试输入到 Prompt                    │
│     ├── 获取 LLM 输出                           │
│     ├── 对比期望输出                            │
│     └── 记录通过/失败                           │
│           ↓                                     │
│  4. 计算通过率                                  │
│     ├── happy_path 通过率                       │
│     ├── edge_cases 通过率                       │
│     ├── adversarial 通过率                      │
│     └── 综合得分 = 0.3×H + 0.3×E + 0.4×A      │
│           ↓                                     │
│  5. 生成测试报告                                │
└─────────────────────────────────────────────────┘
```

---

## 五、Phase 4：C 级清零（9/16 → 9/30）

### 目标
C 级 Skill 全部重构或淘汰，归零。

### 处置策略

| C 级原因 | 处置方式 | 执行标准 |
|----------|---------|---------|
| 孤岛（无引用） | 淘汰 | 删除文件 + 移除索引 |
| Schema 残缺 | 重构 | 补全后重新评级 |
| 功能重复 | 合并 | 保留高质量版本 |
| 过时废弃 | 归档 | 移至 `88-Archive/` |

### 清零验收

```
C 级 Skill 清零验收：
  1. 审计脚本运行：python skill_audit_score.py --grade C
  2. 期望输出：0 个 C 级 Skill
  3. 验证：全库 Skill 均为 A 或 B 级
```

---

## 六、文件产出物清单

| 文件 | 路径 | 说明 |
|------|------|------|
| 分级标准 | `02-BUILD/22-uSkill/智能体任务/skill_grading_rubric.yaml` | 评分维度 |
| 审计脚本 | `02-BUILD/22-uSkill/智能体任务/skill_audit_score.py` | 综合评分 |
| 复用率计算 | `02-BUILD/22-uSkill/智能体任务/skill_audit_reuse.py` | 复用率 |
| Schema 检查 | `02-BUILD/22-uSkill/智能体任务/skill_audit_schema.py` | Schema 完整度 |
| Self-Play 引擎 | `02-BUILD/22-uSkill/智能体任务/skill_self_play.py` | 对抗测试 |
| 测试集 | `02-BUILD/22-uSkill/智能体任务/self_play_test_set.yaml` | 测试用例 |
| 路线图 | `02-BUILD/22-uSkill/智能体任务/uSkill-质量分级与Self-Play框架-v1.md` | 本文件 |


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
---

*版本：v1.0 · 2026-07-02 创建 · Q3 里程碑：8/15 审计脚本 → 8/31 Top20 优化 → 9/15 Self-Play → 9/30 C级清零*


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
| ""这跟我无关"" | "跨领域知识是创新的最大来源" |
| ""直觉告诉我这样做"" | "直觉是过去的偏见，数据才是现在的真相" |
| ""大家都这样做"" | "从众是认知懒惰的最常见表现" |

---

## 🛡️ Three-Tier Boundaries `[v3新增]`

> 来源：addyosmani/agent-skills 的边界系统

### ✅ Always do（自动执行）
- 执行核心功能（见原技能流程）
- 输出结构化结果
- 检查常见错误

### ⚠️ Ask first（先问再做）
- 用户意图不明确时
- 操作不可逆时
- 涉及外部系统时

### 🚫 Never do（绝对禁止）
- 不跳过验证步骤
- 不在用户未确认时执行高风险操作
- 不伪装成功（失败就上报）

---

## 🔒 Gated Workflow `[v3新增]`

> 来源：addyosmani 的门禁 + claude-skills 的 Agent Harness

```
DISCUSS → PLAN → EXECUTE → VERIFY → CLOSE
   ↓         ↓        ↓          ↓        ↓
 Context   方案     执行      证据     Done/
 Read     确认     任务      检查    Escalate
```

### Phase 1: DISCUSS
- [ ] 输出 Context Read 一行判断
- [ ] 确认用户意图
- [ ] 确认约束条件

### Phase 2: PLAN
- [ ] 制定执行方案
- [ ] 确认资源可用
- [ ] 人工审批计划

### Phase 3: EXECUTE
- [ ] 逐个任务实现
- [ ] 每步有输出记录

### Phase 4: VERIFY
- [ ] 检查核心输出
- [ ] 验证完整性
- [ ] 输出证据

### Phase 5: CLOSE
- [ ] 所有检查通过 → 标记完成
- [ ] 有未通过项 → 升级给人类
- [ ] 预算耗尽 → 强制升级，不伪装成功

---


## 📥 输入 Schema

| 参数 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| input_data | string | ✅ | 核心输入数据 |
| context | string | ❌ | 上下文信息 |

## 📤 输出 Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| result | string | 分析/执行结果 |
| confidence | number | 置信度（0-1） |


## 🔄 IF/THEN 决策分支

- IF 输入数据质量不足以支撑自动化决策 → THEN 转交人工判断，输出不确定性说明
- IF 执行过程中遇到未预期的异常 → THEN 记录异常 + 降级处理 + 升级给人类
- IF 输出结果置信度 < 0.6 → THEN 标记低置信度 + 要求人工验证
- ELSE（所有检查通过）→ THEN 输出结果 + 验证证据

## 🧪 Self-Play 测试用例

| # | 场景 | 输入 | 预期输出 | 验证点 |
|---|------|------|----------|--------|
| 1 | 正常执行 | 标准输入数据 | 符合预期的输出 | 格式正确 + 内容准确 |
| 2 | 边界输入 | 极端/空/超长输入 | 降级处理或错误提示 | 不崩溃 + 有明确反馈 |
| 3 | 数据缺失 | 缺少必填参数 | 参数补全提示 | 不编造数据 |
| 4 | 异常场景 | 非预期的输入类型 | 友好的错误处理 | 不泄露内部信息 |
| 5 | 并发场景 | 多个相同请求同时到达 | 结果一致或正确排队 | 无数据竞争 |

## 📋 Verification Evidence `[v3新增]`

> 来源：addyosmani 的证据要求 + claude-skills 的 verify

### 完成标志
- [ ] 核心输出已生成
- [ ] 输出格式符合预期
- [ ] 无明显错误

### 失败处理
- 输出不完整 → 继续补充，不标记完成
- 连续 3 次失败 → 升级给人类，附上当前状态
- 绝不伪装成功
