
description: |
  当用户需要制定饮食计划、优化营养摄入、管理体重、调整饮食习惯时使用此 Skill。
  触发词包括：'营养'、'饮食'、'减肥'、'增肌'、'卡路里'、'蛋白质'、
  '营养规划'、'饮食计划'。当用户讨论健康、运动、体重管理时，
  即使未直接说"营养规划"，也应使用此 Skill。
  不适用于特殊饮食需求（如糖尿病、过敏，需咨询医生）。遇到营养规划需求时优先使用。

---

# uSkill-303: 营养规划

## 🎯 目标

> 基于营养科学，制定个性化的饮食计划，优化营养摄入，支持健康目标。

**核心价值**：营养是健康的基石。正确的饮食能提升精力、改善体态、预防疾病。

**适用场景**：
- 体重管理（减脂/增肌）
- 运动营养
- 日常健康饮食
- 精力优化
- 睡眠改善

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `health_goal` | `enum` | ✅ | — | `weight_loss` / `muscle_gain` / `maintenance` / `performance` |
| `body_metrics` | `object` | ❌ | — | `{weight, height, age, gender, body_fat}` |
| `activity_level` | `enum` | ❌ | `moderate` | `sedentary` / `light` / `moderate` / `active` / `very_active` |
| `dietary_restrictions` | `array` | ❌ | `[]` | 饮食限制 |
| `preferences` | `object` | ❌ | — | 饮食偏好 |

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话营养建议",
  "nutrition_id": "NT-YYYY-MMDD-NNN",

  "calorie_needs": {
    "basal_metabolic_rate": "number",
    "total_daily_energy_expenditure": "number",
    "target_calories": "number",
    "calorie_adjustment": "number",
    "reasoning": "string"
  },

  "macronutrient_plan": {
    "protein": {
      "grams": "number",
      "percentage": "number",
      "timing": ["string"],
      "sources": ["string"]
    },
    "carbohydrates": {
      "grams": "number",
      "percentage": "number",
      "timing": ["string"],
      "sources": ["string"]
    },
    "fats": {
      "grams": "number",
      "percentage": "number",
      "timing": ["string"],
      "sources": ["string"]
    }
  },

  "micronutrient_focus": [
    {
      "nutrient": "string",
      "importance": "string",
      "recommended_amount": "string",
      "food_sources": ["string"]
    }
  ],

  "meal_plan": [
    {
      "meal": "breakfast|lunch|dinner|snack",
      "time": "string",
      "calories": "number",
      "macronutrients": {
        "protein": "number",
        "carbs": "number",
        "fats": "number"
      },
      "suggested_foods": ["string"],
      "portion_guidance": "string"
    }
  ],

  "hydration_plan": {
    "daily_water_intake": "string",
    "timing": ["string"],
    "electrolyte_considerations": "string"
  },

  "supplement_recommendations": [
    {
      "supplement": "string",
      "dosage": "string",
      "timing": "string",
      "reasoning": "string"
    }
  ],

  "monitoring_plan": {
    "daily_checks": ["string"],
    "weekly_reviews": ["string"],
    "adjustment_triggers": ["string"]
  },

  "metadata": {
    "execution_time": "string",
    "self_play_score": "number",
    "version": "1.0.0"
  }
}
```

---

## 📋 执行步骤

### Step 1: 能量需求计算

- **输入**：`body_metrics` + `activity_level` + `health_goal`
- **动作**：
  1. 计算基础代谢率
  2. 计算总能量消耗
  3. 确定目标热量
- **输出**：`calorie_needs`
- **BMR 计算公式（Mifflin-St Jeor）**：
  - 男性：BMR = 10 × 体重(kg) + 6.25 × 身高(cm) - 5 × 年龄 - 5
  - 女性：BMR = 10 × 体重(kg) + 6.25 × 身高(cm) - 5 × 年龄 - 161

### Step 2: 宏量营养素分配

- **输入**：`calorie_needs` + `health_goal`
- **动作**：
  1. 计算蛋白质需求
  2. 计算碳水化合物需求
  3. 计算脂肪需求
- **输出**：`macronutrient_plan`
- **宏量营养素分配指南**：

| 目标 | 蛋白质 | 碳水 | 脂肪 |
|------|:------:|:----:|:----:|
| 减脂 | 30-35% | 35-40% | 25-30% |
| 增肌 | 25-30% | 45-55% | 20-25% |
| 维持 | 20-25% | 45-55% | 25-30% |
| 运动表现 | 20-25% | 55-65% | 20-25% |

### Step 3: 微量营养素关注

- **输入**：`health_goal` + `dietary_restrictions`
- **动作**：
  1. 识别关键微量营养素
  2. 推荐食物来源
  3. 评估补充剂需求
- **输出**：`micronutrient_focus`

### Step 4: 餐食计划

- **输入**：`calorie_needs` + `macronutrient_plan`
- **动作**：
  1. 分配餐次
  2. 设计每餐内容
  3. 安排进食时间
- **输出**：`meal_plan`

### Step 5: 水分计划

- **输入**：`body_metrics` + `activity_level`
- **动作**：
  1. 计算水分需求
  2. 安排饮水时间
  3. 考虑电解质
- **输出**：`hydration_plan`

### Step 6: 补充剂建议

- **输入**：`micronutrient_focus` + `dietary_restrictions`
- **动作**：
  1. 评估补充剂需求
  2. 推荐补充剂类型
  3. 确定剂量和时间
- **输出**：`supplement_recommendations`

---

## ⚠️ 边界约束

### 硬性约束（必须遵守）
1. **不得**建议极端饮食
2. **不得**忽视个体差异
3. **必须**建议咨询医生（特殊健康状况）

### 软性约束（建议遵守）
1. 建议循序渐进调整饮食
2. 建议记录饮食日记
3. 建议定期评估和调整

### 人工兜底点
- 当涉及特殊健康状况时，**必须**建议咨询医生
- 当饮食限制多时，**必须**建议咨询营养师

---

## ⚠️ 异常处理

| 异常代码 | 触发条件 | 处理方式 | 严重级别 |
|----------|----------|----------|:--------:|
| `NT_WARNING_RESTRICTIVE` | 饮食过于限制 | 建议放宽限制 | 🟡 |
| `NT_WARNING_UNBALANCED` | 营养不均衡 | 建议调整 | 🟡 |
| `NT_ERROR_HEALTH` | 健康风险 | 建议就医 | 🔴 |

---

## ✅ 校验验收规则

### 格式校验
- [ ] 输出为合法 JSON
- [ ] 所有必填字段已填充

### 内容校验
- [ ] 能量需求已计算
- [ ] 宏量营养素已分配
- [ ] 餐食计划已制定
- [ ] 水分计划已制定

### OVP 验证信号
- 营养均衡度评分 ≥ 85
- 用户满意度 ≥ 4.0/5.0

---

## 🧪 Self-Play 测试用例

```json
[
  {
    "id": "test-001",
    "name": "减脂饮食计划",
    "prompt": "帮我制定一个减脂饮食计划",
    "context": "health_goal=weight_loss, body_metrics={weight:80, height:175, age:30, gender:male}",
    "assertions": [
      "calorie_needs.target_calories < TDEE",
      "macronutrient_plan.protein.percentage >= 30",
      "meal_plan 包含 3-4 餐"
    ],
    "expected_behavior": "制定减脂导向的饮食计划",
    "critic_attack": "热量缺口是否过大？"
  },
  {
    "id": "test-002",
    "name": "增肌饮食计划",
    "prompt": "帮我制定一个增肌饮食计划",
    "context": "health_goal=muscle_gain, activity_level=active",
    "assertions": [
      "calorie_needs.target_calories > TDEE",
      "macronutrient_plan.protein.grams >= 1.6g/kg",
      "meal_plan 包含 训练后餐"
    ],
    "expected_behavior": "制定增肌导向的饮食计划",
    "critic_attack": "是否考虑了蛋白质吸收时机？"
  },
  {
    "id": "test-003",
    "name": "素食者饮食",
    "prompt": "我是素食者，帮我规划饮食",
    "context": "dietary_restrictions=[vegetarian]",
    "assertions": [
      "micronutrient_focus 包含 B12、铁",
      "macronutrient_plan.protein.sources 包含 植物蛋白",
      "supplement_recommendations 可能包含 B12"
    ],
    "expected_behavior": "为素食者设计均衡饮食",
    "critic_attack": "是否确保了蛋白质完整性？"
  }
]
```

---

## 🔗 关联文档

- [[2026-06 睡眠优化执行手册]] — 睡眠与营养
- [[心率区间训练]] — 运动营养
- [[数据驱动 Biohacking 闭环]] — 数据优化
- [[压力管理]] — 压力与饮食
- [[AI Co-Evolution 自主进化的人生操作系统]] — 系统总览

---

## 📝 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-06-23 | 1.0.0 | 初始版本：能量计算 + 营养分配 + 餐食计划 + Self-Play |

---

*模板版本: 1.0.0 · 基于 Skill Schema 模板*


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [健康任务] for [身体状况], with [生活方式], leaning toward [干预方案]."

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
| ""偶尔熬夜没关系"" | "偶尔=经常的开始" |
| ""年轻扛得住"" | "年轻时透支的，中年后加倍还" |
| ""吃保健品就行了"" | "保健品≠健康饮食+运动" |

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


**相关概念**：[[运动营养]] · [[《囚徒健身》-保罗·威德]] · [[抗炎饮食]]

---


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
