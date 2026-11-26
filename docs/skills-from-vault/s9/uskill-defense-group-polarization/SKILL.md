---
name: uskill-defense-group-polarization
description: "让群体极化防御变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-defense-group-polarization.md"
  original_id: "SKL-6884"
  version: "3.0.0"
  trust: untrusted
---

# 群体极化防御

description: |
  当用户需要识别信息茧房、回声室效应、群体极化、观点单一化时使用此 Skill。
  触发词包括：'信息茧房'、'回声室'、'群体极化'、'观点单一'、'信息偏食'、
  '算法推荐'、'同温层'、'认知封闭'。当用户讨论社交媒体算法、社群观点趋同、
  意识形态极化时，即使未直接说"群体极化"，也应使用此 Skill。
  不适用于正常的社群学习和知识共享。遇到信息多样性评估需求时优先使用。

---

# uSkill-104: 群体极化防御

## 🎯 目标

> 识别并防御信息茧房、回声室效应、群体极化，帮助用户保持认知开放性和观点多样性。

**核心价值**：在算法推荐和社群同质化的时代，主动打破信息壁垒，保持独立思考。

**适用场景**：
- 社交媒体信息流评估
- 社群观点多样性分析
- 个人信息消费习惯审计
- 投资决策中的从众风险识别
- 意识形态极化预警

---

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `information_environment` | `object` | ✅ | — | 信息环境描述 |
| `user_profile` | `object` | ❌ | — | 用户信息消费画像 |
| `analysis_depth` | `enum` | ❌ | `standard` | `quick` / `standard` / `deep` |

**information_environment 结构**：
```json
{
  "platforms": ["string"],
  "content_sources": ["string"],
  "social_circle": ["string"],
  "algorithm_feed": true
}
```

**user_profile 结构**：
```json
{
  "political_leaning": "left|center|right|unknown",
  "content_diversity_score": "number — 0-100",
  "echo_chamber_risk": "low|medium|high"
}
```

---

## 📤 输出

### 标准输出

```json
{
  "status": "success",
  "summary": "string — 一句话极化风险评估",
  "polarization_id": "GP-YYYY-MMDD-NNN",

  "echo_chamber_analysis": {
    "risk_level": "low|medium|high|critical",
    "risk_factors": [
      {
        "factor": "string",
        "description": "string",
        "severity": "low|medium|high"
      }
    ],
    "information_diversity": {
      "score": "number — 0-100",
      "dimensions": {
        "ideological": "number — 0-100",
        "source_variety": "number — 0-100",
        "topic_range": "number — 0-100",
        "viewpoint_diversity": "number — 0-100"
      }
    }
  },

  "algorithm_bias_detection": {
    "detected": false,
    "bias_types": ["filter_bubble", "reinforcement", "polarization"],
    "evidence": ["string"],
    "impact_assessment": "string"
  },

  "social_influence_analysis": {
    "conformity_pressure": "low|medium|high",
    "groupthink_risk": "low|medium|high",
    "dissent_availability": "low|medium|high",
    "critical_mass_of_diversity": "number — 0-100"
  },

  "defense_strategies": [
    {
      "strategy": "string",
      "description": "string",
      "effectiveness": "high|medium|low",
      "implementation_difficulty": "easy|moderate|hard"
    }
  ],

  "monitoring_plan": {
    "weekly_checks": ["string"],
    "monthly_audits": ["string"],
    "red_flags": ["string"]
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

### Step 1: 信息环境扫描

- **输入**：`information_environment`
- **动作**：
  1. 识别信息来源的多样性
  2. 分析算法推荐的影响
  3. 评估社交圈的同质性
- **输出**：`echo_chamber_analysis`
- **信息茧房风险因素**：

| 风险因素 | 特征 | 检测方法 |
|----------|------|----------|
| **单一平台依赖** | 主要信息来自一个平台 | 平台分布分析 |
| **算法强化** | 只看到相似内容 | 内容相似度分析 |
| **社交同质性** | 朋友圈观点趋同 | 社交网络分析 |
| **信息回避** | 主动回避不同观点 | 内容选择模式 |

- **检查点**：✅ 验证信息环境已扫描

### Step 2: 算法偏见检测

- **输入**：`information_environment`
- **动作**：
  1. 检测过滤气泡（Filter Bubble）
  2. 检测强化效应（Reinforcement）
  3. 检测极化效应（Polarization）
- **输出**：`algorithm_bias_detection`
- **算法偏见类型**：

| 类型 | 机制 | 影响 |
|------|------|------|
| **过滤气泡** | 只显示符合偏好的内容 | 视野狭窄 |
| **强化效应** | 不断强化已有观点 | 观点固化 |
| **极化效应** | 推送极端内容吸引点击 | 观点极端化 |

- **检查点**：✅ 验证算法偏见已检测

### Step 3: 社会影响力分析

- **输入**：`information_environment` + `user_profile`
- **动作**：
  1. 评估从众压力
  2. 检测群体思维风险
  3. 评估异议可用性
- **输出**：`social_influence_analysis`
- **群体思维（Groupthink）信号**：

| 信号 | 特征 | 检测方法 |
|------|------|----------|
| **自我审查** | 压制不同意见 | 发言模式分析 |
| **错觉一致** | 假设所有人都同意 | 观点分布分析 |
| **合理化** | 集体为错误决策辩护 | 事后分析 |
| **对外刻板** | 对外部群体有偏见 | 语言分析 |

- **检查点**：✅ 验证社会影响力已分析

### Step 4: 防御策略生成

- **输入**：所有前序输出
- **动作**：
  1. 生成个性化防御策略
  2. 评估策略有效性
  3. 生成实施计划
- **输出**：`defense_strategies`
- **防御策略库**：

| 策略 | 描述 | 有效性 | 难度 |
|------|------|:------:|:----:|
| **信息多样化** | 主动订阅不同立场的信息源 | 高 | 中 |
| **反向推荐** | 定期查看"不喜欢"的内容 | 中 | 低 |
| **跨圈社交** | 与不同背景的人交流 | 高 | 高 |
| **定期审计** | 每月评估信息消费多样性 | 中 | 低 |
| **批判性消费** | 对每条信息保持质疑 | 高

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
