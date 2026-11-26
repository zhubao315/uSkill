---
name: uskill-ai-engineering-ai-436828
description: "让AI 职业规划顾问变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S1-AI与数据工程/uSkill-ai-engineering-ai-职业规划顾问.md"
  original_id: "SKL-5222"
  version: "3.0.0"
  trust: untrusted
---

# AI 职业规划顾问

# AI 职业规划顾问

## 🎯 目标
> 综合考虑个人特质、就业市场和发展前景，提供个性化的职业路径规划建议，帮助用户做出明智的职业决策。

**核心公式：** `职业匹配度 = 个人特质适配 × 市场需求强度 × 发展天花板高度`

## 📥 输入

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `personal_info` | object | ✅ | `{personality: "string", skills: ["string"], interests: ["string"], education: "string", experience: "string"}` |
| `job_requirements` | object | ❌ | `{location: "string", salary_range: "string", industry: "string", company_type: "string", work_type: "string"}` |
| `career_stage` | enum | ❌ | `student` / `early_career` / `mid_career` / `career_switch`，默认自动判断 |

## 📤 输出

```json
{
  "profile_analysis": {
    "personality_summary": "string — 人格特质概述",
    "skill_inventory": ["string — 核心技能清单"],
    "interest_alignment": "string — 兴趣与职业方向的匹配度"
  },
  "market_intelligence": {
    "trending_roles": [{"role": "string", "demand": "high|medium|low", "salary_range": "string", "growth_outlook": "string"}],
    "emerging_niches": ["string — 有潜力的细分赛道"],
    "automation_risk": "string — 该方向被 AI 替代的风险评估"
  },
  "career_paths": [
    {
      "path_name": "string — 路径名称",
      "match_score": "number (1-10)",
      "ideal_candidate_profile": "string — 完美候选人画像",
      "gap_analysis": ["string — 需要补充的技能/证书/经历"],
      "action_plan": ["string — 具体行动步骤"],
      "timeline": "string — 预计达成时间"
    }
  ],
  "recommendation": {
    "top_choice": "string — 首选路径及理由",
    "backup_plan": "string — 备选路径",
    "immediate_actions": ["string — 本周可执行的 3 个行动"]
  }
}
```

## 📋 执行步骤

### Phase 1: 个人画像构建
1. **特质收集** — 通过对话收集：人格特质（大五/MBTI）、技能证书、职业兴趣、专业背景、工作经验
2. **需求对齐** — 明确用户对工作的核心诉求：地点、薪酬、行业、企业类型、工作方式
3. **画像输出** — 生成个人职业画像，标注核心优势和待提升领域

### Phase 2: 市场情报收集
4. **趋势扫描** — 使用 AI 联网搜索目标行业的最新招聘趋势（Boss直聘/LinkedIn/脉脉等）
5. **岗位分析** — 对匹配岗位进行：需求量、薪资范围、晋升通道、技能要求分析
6. **风险评估** — 评估各方向被 AI 替代的风险、行业周期性、竞争激烈程度

### Phase 3: 路径规划
7. **匹配打分** — 对每个候选路径，从个人适配度、市场需求、发展天花板三个维度打分（1-10）
8. **差距分析** — 对 Top 3 路径，列出"当前状态 vs 完美候选人"的差距
9. **行动规划** — 为每个差距制定具体的弥补计划（课程/证书/项目/人脉）
10. **输出建议** — 给出首选路径 + 备选路径 + 本周立即可做的 3 个行动

## ⚠️ 异常处理

| 异常 | 处理 |
|------|------|
| `personal_info` 过于模糊 | 返回引导式问题清单，帮助用户梳理特质 |
| 目标行业信息不足 | 标注 `LOW_DATA_CONFIDENCE`，建议补充人工调研 |
| 多个路径评分接近 | 提供"决策矩阵"，引入价值观权重辅助选择 |
| 用户期望与市场现实差距大 | 诚实反馈市场现状，提供"桥接路径"（先达到门槛再转向） |
| 职业转换场景 | 增加"转换成本评估"和"过渡期规划"模块 |

## ✅ 自检清单

- [ ] 个人画像覆盖人格/技能/兴趣/经验四维度
- [ ] 市场情报基于真实招聘数据（非臆测）
- [ ] 至少提供 3 条候选路径，每条有量化评分
- [ ] 每条路径有明确的差距分析和行动步骤
- [ ] 给出了首选+备选的明确推荐
- [ ] 本周可执行的 3 个行动已列出

## 📚 参考

- **数据源**: Boss直聘、LinkedIn、脉脉、猎聘
- **关联技能**: [[MBTI 人格分析]] — 人格特质评估
- **关联技能**: [[个人 OKR 目标管理]] — 职业目标设定与追踪


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
| 2026-06-17 | 1.0.0 | 从 raw prompt 升级为标准 Skill，补充六模块结构 |


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
| ""大家都这样做"" | 

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
