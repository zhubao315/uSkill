
description: |
  当用户需要分析某个领域或产品的竞争对手时使用此 Skill。
  触发词包括：'竞品分析'、'竞争对手'、'市场格局'、'差异化策略'、'SWOT分析'。
  当用户说"这个领域有哪些玩家"、"我们和XX比怎么样"，即使未直接说"竞品分析"，也应使用此 Skill。
  不适用于纯学术研究。用于产品战略、投资调研、创业规划等商业场景。

---

# 🔍 uSkill-305: 竞品分析

## 🎯 目标

> AI驱动的竞品情报采集与分析，从海量噪音中提炼战略洞察，生成差异化策略。

**核心价值**：用系统化框架替代直觉判断，确保竞争分析的全面性和客观性。

**适用场景**：
- 新产品立项前的市场格局分析
- 现有产品的竞争定位评估
- 投资调研中的行业竞争分析
- 创业方向选择的可行性评估
- 技术选型的竞品对比

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `domain` | `string` | ✅ | — | 目标领域/赛道名称 |
| `known_competitors` | `array` | ❌ | — | 已知竞品列表 |
| `analysis_depth` | `enum` | ❌ | `standard` | `quick`(3家) / `standard`(5家) / `deep`(8家) |
| `focus_aspects` | `array` | ❌ | 全部 | 重点关注维度（技术/定价/用户/渠道） |
| `our_position` | `object` | ❌ | — | 我方定位（如有） |

**输入约束**：
- `domain` 应明确到具体赛道（如"AI代码助手"而非"AI"）
- `analysis_depth=deep` 时建议提供 our_position 以便差异化分析
- known_competitors 如未提供，将自动识别

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话竞争格局结论",
  "analysis_id": "CMP-YYYY-MMDD-NNN",
  "market_landscape": {
    "total_players": "number",
    "segmentation": [
      {
        "segment": "string",
        "players": ["string"],
        "market_share": "string",
        "growth_trend": "growing|stable|declining"
      }
    ]
  },
  "competitor_profiles": [
    {
      "name": "string",
      "positioning": "string",
      "strengths": ["string"],
      "weaknesses": ["string"],
      "pricing": "string",
      "user_reviews_summary": "string",
      "threat_level": "high|medium|low"
    }
  ],
  "feature_matrix": {
    "headers": ["功能", "竞品A", "竞品B", "我方"],
    "rows": [
      {"feature": "string", "values": ["string"], "importance": "must|should|nice"}
    ]
  },
  "swot_analysis": {
    "strengths": ["string"],
    "weaknesses": ["string"],
    "opportunities": ["string"],
    "threats": ["string"]
  },
  "differentiation_strategies": [
    {
      "type": "offensive|defensive|niche",
      "strategy": "string",
      "rationale": "string",
      "expected_outcome": "string"
    }
  ],
  "action_items": [
    {
      "priority": "P0|P1|P2",
      "action": "string",
      "deadline": "string"
    }
  ]
}
```

---

## 🔄 执行流程

```
1. [竞品识别] → 识别3-8个核心竞品
   → 直接竞品：同赛道、同模式、同用户群
   → 间接竞品：不同模式但解决同一问题
   → 潜在替代品：可能降维打击的新进入者
   → 判断条件：known_competitors 是否提供？
     → 是：以此为基础扩展
     → 否：基于领域知识自动识别
   → 判断条件：识别数量 < analysis_depth要求？
     → 是：继续扩展识别
     → 否：进入步骤2

2. [竞品画像] → 每个竞品深度分析
   → 定位：核心价值主张、目标用户
   → 优势：技术壁垒、品牌、渠道、资金
   → 劣势：短板、用户投诉、增长瓶颈
   → 定价：价格策略、免费/付费模式
   → 用户评价：应用商店评分、核心好评/差评

3. [功能对比矩阵] → 构建结构化对比表
   → 识别核心功能维度（must/should/nice分级）
   → 逐功能对比各竞品
   → 标注差异化机会点

4. [SWOT分析] → 面向我方的竞争定位
   → S: 我方相对竞品的优势
   → W: 我方相对竞品的劣势
   → O: 市场中未被满足的机会
   → T: 竞品可能的威胁（如降价、新功能）
   → 判断条件：our_position 是否提供？
     → 是：基于我方定位做SWOT
     → 否：做通用市场SWOT

5. [差异化策略] → 生成竞争策略
   → 进攻策略：找到竞品薄弱点，集中突破
   → 防御策略：巩固我方优势，防止被蚕食
   → 利基策略：找到未被服务的细分市场
   → 判断条件：我方份额 < 20%？
     → 是：建议利基/进攻策略
     → 否：建议防御+差异化策略

6. [行动建议] → 生成可执行的行动清单
   → 按优先级排序
   → 每条有明确截止日期

7. [输出报告] → 生成结构化竞品分析报告
```

---

## 📝 Prompt 模板

### 标准竞品分析 Prompt

```
你是竞品分析Agent。请分析以下领域的竞争格局。

【输入】
- 目标领域：{domain}
- 已知竞品：{known_competitors}
- 分析深度：{analysis_depth}
- 我方定位：{our_position}

【分析步骤】
1. 识别3-8个核心竞品（直接+间接+替代品）
2. 每个竞品：定位、优势、劣势、定价、用户评价
3. 构建功能对比矩阵（must/should/nice分级）
4. SWOT分析（面向我方）
5. 生成差异化策略（进攻/防御/利基）
6. 输出行动建议（P0/P1/P2优先级）

【输出要求】
- 竞品信息需标注数据来源
- SWOT必须有数据支撑
- 策略必须具体可执行
```

---

## ⚠️ 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|----------|----------|----------|
| 竞品信息不足 | 标注信息缺口，建议补充调研 | 基于公开信息分析，标注置信度低 |
| 领域过于宽泛 | 请求缩小范围 | 聚焦top 3竞品做quick分析 |
| 无法识别竞品 | 输出「该领域竞品格局不明确」 | 基于替代品分析 |
| 我方定位缺失 | 做通用市场分析 | 不生成差异化策略，仅输出格局+SWOT |

---

## ✅ 质量自检

- [ ] 竞品覆盖直接+间接+替代品
- [ ] 每个竞品有数据支撑（非纯主观判断）
- [ ] 功能矩阵重要性分级（must/should/nice）
- [ ] SWOT有具体证据
- [ ] 差异化策略可执行
- [ ] 行动建议有截止日期

---

## 💡 使用示例

### 示例 1：AI代码助手竞品分析

**输入**：
```json
{
  "domain": "AI代码助手",
  "analysis_depth": "standard",
  "focus_aspects": ["技术", "定价", "用户体验"]
}
```

**输出**：
```json
{
  "market_landscape": {"total_players": 12, "segmentation": [{"segment": "IDE集成型", "players": ["GitHub Copilot", "Cursor", "Codeium"], "growth_trend": "growing"}]},
  "competitor_profiles": [
    {"name": "GitHub Copilot", "strengths": ["生态整合", "代码补全准确率高"], "weaknesses": ["价格高", "隐私担忧"], "threat_level": "high"}
  ],
  "differentiation_strategies": [
    {"type": "niche", "strategy": "聚焦中国市场+私有化部署", "rationale": "竞品普遍不支持国内私有化"}
  ]
}
```

---

## 🧪 Self-Play 测试

| # | 场景 | 输入要点 | 期望输出 | 边界条件 |
|---|------|----------|----------|----------|
| 1 | 标准分析 | 5家竞品 | 完整SWOT+矩阵 | 正常输入 |
| 2 | 竞品未知 | 无known_competitors | 自动识别+分析 | 无先验信息 |
| 3 | 领域模糊 | "AI" | 请求缩小范围 | 过于宽泛 |
| 4 | 深度分析 | deep+our_position | 差异化策略 | 完整输入 |
| 5 | 新兴领域 | 竞品很少 | 替代品分析 | 竞品不足 |

---

## 📊 版本记录

| 版本 | 日期 | 变更内容 | 验证结果 |
|------|------|----------|----------|
| v1.0 | 2026-06-17 | 初始版本（81行，结构较好） | — |
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
- 当新增 ≥3 种异常处理场景时，升级 minor 版本
- 当核心方法论发生根本性变化时，升级 major 版本

**废弃触发**：
- 当所依赖的平台/工具停止维护时，标记为 deprecated
- 当有更好的替代方案出现时，评估迁移

---
---

*Agent可读性标记：search_keywords=[竞品分析；竞争对手；市场格局；SWOT；差异化策略]；context_triggers=[产品战略；投资调研；创业规划；技术选型]*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [效率任务] for [工具熟悉度], with [时间约束], leaning toward [工具/方法]."

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
| ""以后再优化流程"" | "以后不会来，现在就做" |
| ""手动操作更快"" | "手动=不可重复=不可审计" |
| ""这个工具太复杂了"" | "复杂是暂时的，低效是永久的" |

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
