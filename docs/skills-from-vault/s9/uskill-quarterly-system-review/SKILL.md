---
name: uskill-quarterly-system-review
description: "让季度系统评估 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-quarterly-system-review.md"
  original_id: "SKL-5308"
  version: "3.0.0"
  trust: untrusted
---

# 季度系统评估 Agent — 实施手册

description: |
  当用户需要对全系统进行季度评估时使用此 Skill。
  触发词包括：'季度评估'、'系统评估'、'健康度检查'、'架构审查'。
  当用户说"系统状态怎么样"、"做个季度review"，即使未直接说"季度评估"，也应使用此 Skill。
  不适用于日常监控（用 Agent 执行监控）。用于季度级别的系统性审查。

---

# 📊 uSkill-308: 季度系统评估

## 🎯 目标

> 全系统架构评估与升级规划，识别瓶颈、优化资源配置、制定下季度路线图。

**核心价值**：定期体检系统健康度，避免"技术债"累积到不可收拾。

**适用场景**：
- 季度末系统健康度评估
- 年中/年终系统复盘
- 重大变更前的系统评估
- 新季度规划前的现状分析

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `quarterly_okr` | `object` | ✅ | — | 季度 OKR 完成数据 |
| `system_data` | `object` | ✅ | — | 系统运行数据（各子系统指标） |
| `subsystems` | `array` | ❌ | 全部5个 | 需评估的子系统列表 |

**输入约束**：
- `quarterly_okr` 应包含各 O/KR 的完成率
- `system_data` 应包含知识库、Agent、循环工程等核心指标

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话系统状态总结",
  "quarter": "Q1|Q2|Q3|Q4",
  "health_scores": {
    "uSkill": "number (0-100)",
    "uWise": "number (0-100)",
    "uRead": "number (0-100)",
    "Agent": "number (0-100)",
    "Loop": "number (0-100)"
  },
  "bottlenecks": [
    {"subsystem": "string", "issue": "string", "impact": "high|medium|low"}
  ],
  "optimizations": [
    {"priority": "P0|P1|P2", "action": "string", "expected_impact": "string"}
  ],
  "next_quarter_roadmap": ["string"]
}
```

---

## 🔄 执行流程

```
1. [数据采集] → 收集各子系统运行数据
   → 知识库：总量、健康度、断链率、标签合规率
   → Agent：覆盖率、执行成功率、人工干预率
   → 循环工程：日完成率、异常次数

2. [健康评估] → 为每个子系统打分（0-100）
   → uSkill：数量×质量×复用率
   → uWise：数量×关联密度×调用示例覆盖率
   → uRead：数量×深度×产品化程度
   → Agent：覆盖率×自动化率×准确率
   → Loop：运行稳定性×日完成率×异常恢复率

3. [瓶颈识别] → 找出制约系统的关键瓶颈
   → 判断条件：哪个子系统分数最低？
     → 是：标注为主要瓶颈
     → 否：综合评估
   → 判断条件：是否有子系统间依赖阻塞？
     → 是：标注依赖瓶颈

4. [优化建议] → 生成按优先级排序的优化建议
   → P0：影响系统存续的瓶颈
   → P1：影响效率的关键问题
   → P2：锦上添花的改进

5. [路线规划] → 生成下季度路线图
   → 基于瓶颈识别结果
   → 每个优化建议绑定具体时间
```

---

## 📝 Prompt 模板

### 标准评估 Prompt

```
你是季度系统评估Agent。请执行季度系统评估。

【季度OKR】{quarterly_okr}
【系统数据】{system_data}

【评估维度】
1. 各子系统健康度评分（0-100）
2. 瓶颈识别（制约系统的关键因素）
3. 优化建议（按P0/P1/P2排序）
4. 下季度路线图

【输出格式】
按标准 JSON 输出，包含 health_scores、bottlenecks、optimizations、next_quarter_roadmap。
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 数据不完整 | 标注缺失数据 | 基于可用数据评估 |
| 子系统数据矛盾 | 取最新数据 | 标注数据不一致 |
| 无法判断瓶颈 | 输出"需进一步调查" | 仅输出健康度评分 |

---

## ✅ 质量自检

- [ ] 所有子系统有评分
- [ ] 瓶颈有具体证据
- [ ] 优化建议按优先级排序
- [ ] 路线图有时间节点
- [ ] 与上季度对比有进步/退步说明

---

## 💡 使用示例

### 示例 1：Q2 评估

**输入**：
```json
{
  "quarterly_okr": {"uSkill": {"target": 50, "actual": 336}, "uWise": {"target": 1000, "actual": 2265}},
  "system_data": {"knowledge_health": 96, "agent_coverage": 65, "loop_stability": 92}
}
```

**输出**：
```json
{
  "health_scores": {"uSkill": 95, "uWise": 88, "uRead": 92, "Agent": 65, "Loop": 88},
  "bottlenecks": [{"subsystem": "Agent", "issue": "覆盖率仅65%", "impact": "high"}],
  "optimizations": [{"priority": "P0", "action": "Agent覆盖率冲刺≥80%", "expected_impact": "自动化率提升15%"}]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 输入要点 | 期望输出 | 边界条件 |
|---|------|----------|----------|----------|
| 1 | 正常评估 | 完整数据 | 全维度评分 | 正常输入 |
| 2 | 数据缺失 | 部分子系统无数据 | 降级评估+警告 | 数据不全 |
| 3 | 瓶颈明显 | 某子系统分数极低 | P0瓶颈标注 | 极端值 |
| 4 | 全面优秀 | 所有子系统>90 | 聚焦质量提升 | 高分场景 |
| 5 | 全面低谷 | 所有子系统<60 | 紧急优化路线 | 低分场景 |

---

## 📊 版本记录

| 版本 | 日期 | 变更内容 | 验证结果 |
|------|------|----------|----------|
| v1.0 | 2026-06-17 | 初始 Prompt wrapper 版本 | — |
| v2.0 | 2026-06-29 | 升级为 Gen3 Schema：补齐 9 模块 | 待验证 |


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
- 当新增 ≥3 种异常处理场景时，升级 minor 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
