---
name: uskill-agent-agent-7926dc
description: "让午间资讯汇总 Agent — 实施手册变成可执行的行动，而非停留在想法。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S9-专业领域与智能体/uSkill-agent-午间资讯汇总-agent-实施手册.md"
  original_id: "SKL-7020"
  version: "3.0.0"
  trust: untrusted
---

# 午间资讯汇总 Agent — 实施手册

# 📰 午间资讯汇总 Agent — 实施手册

> **定位**：每日 12:00 自动聚合 AI/投资/科技资讯，生成 5 分钟可读午报
>
> **关联**：[[uSkill-日程优化-v1]] · [[2026-07~09 Q3 OKR]]

---

## 一、Agent 定义

| 字段 | 值 |
|------|-----|
| 名称 | Midday News Digest Agent |
| 触发 | 每日 12:00 / 人工指令「生成午报」 |
| 输入 | 关注领域 + 关键词 |
| 输出 | 结构化午报（≤500字） |
| 红线 | **不构成投资建议**，所有信息标注来源 |

---

## 二、关注领域与关键词

### 领域 1：AI 与大模型
```
关键词：LLM, GPT, Claude, Gemini, Agent, RAG, 微调, 开源模型, 
        推理, 训练, 多模态, AI应用, AI安全
信源：机器之心, 量子位, AI科技评论, Hacker News AI
```

### 领域 2：投资与市场
```
关键词：A股, 半导体, 科创50, AI, 黄金, 美联储, CPI, PMI,
        财报, 估值, 行业轮动, 北向资金
信源：东方财富, 同花顺, 华尔街见闻, 36氪
```

### 领域 3：科技与工程
```
关键词：云原生, K8s, 微服务, TDD, CI/CD, 前端, 后端, 数据库,
        开源项目, GitHub Trending
信源：GitHub Trending, InfoQ, 掘金, SegmentFault
```

### 领域 4：驾驭工程与 Agent
```
关键词：uSkill, Agent, SOP, 自动化, 人机协作, Harness, Scaffold,
        Prompt Engineering, AI Coding
信源：Hugging Face, Anthropic Blog, OpenAI Blog, LangChain
```

---

## 三、每日执行 Prompt

### 主 Prompt（直接使用）

```
你是午间资讯汇总Agent。请生成今日午报。

【关注领域】
1. AI与大模型：LLM、Agent、开源模型、AI应用
2. 投资与市场：A股、半导体、科创50、黄金
3. 科技与工程：云原生、K8s、开源项目
4. 驾驭工程：Agent、自动化、人机协作

【输出要求】
1. 今日必读（≤3条最重要的新闻）
2. 四大领域各2-3条资讯
3. 每条包含：标题、一句话摘要（≤30字）、来源、可信度（高/中/低）
4. 数据速览：上证指数、美元/人民币、黄金
5. 需关注：与持仓/计划相关的风险提示
6. 总字数 ≤ 500字

【格式】
按以下结构输出：
# 📰 午间资讯 | {date}

## 🔥 今日必读
1. **[标题]** — 一句话摘要
   - 来源：XX | 可信度：高

## 🤖 AI与大模型
- **[标题]** — 摘要 | 来源 | 可信度

## 📈 投资与市场
- **[标题]** — 摘要 | 来源 | 可信度

## ⚙️ 科技与工程
- **[标题]** — 摘要 | 来源 | 可信度

## 🤖 驾驭工程
- **[标题]** — 摘要 | 来源 | 可信度

## 📊 数据速览
| 指标 | 数值 | 变化 |

## ⚠️ 需关注
- [风险提示]

---
*本报告不构成投资建议，所有信息请以原始来源为准*
```

---

## 四、信源配置

### 免费信源（可直接使用）

| 信源 | 类型 | 更新频率 | 领域 |
|------|------|:--------:|------|
| Hacker News | RSS/API | 实时 | AI/科技 |
| GitHub Trending | API | 每日 | 科技 |
| 东方财富 | 网页 | 实时 | 投资 |
| 机器之心 | RSS | 每日 | AI |
| 量子位 | RSS | 每日 | AI |

### 配置文件

在 `04-Investor/46-投资记录/午报信源配置.md` 中维护：

```yaml
# 午报信源配置
sources:
  ai:
    - name: 机器之心
      url: https://www.jiqizhixin.com/rss
      type: rss
    - name: Hacker News
      url: https://hacker-news.firebaseio.com/v0/topstories.json
      type: api
  
  investment:
    - name: 东方财富
      url: https://www.eastmoney.com
      type: web
      keywords: [半导体, 科创50, AI, 黄金]
  
  tech:
    - name: GitHub Trending
      url: https://api.github.com/search/repositories?q=created:>2026-06-16&sort=stars
      type: api

  agent:
    - name: Hugging Face Blog
      url: https://huggingface.co/blog/feed.xml
      type: rss
```

---

## 五、输出示例

```markdown
# 📰 午间资讯 | 2026-06-17

## 🔥 今日必读
1. **OpenAI 发布 GPT-5 Turbo** — 推理速度提升3倍，成本降低50%
   - 来源：机器之心 | 可信度：高 | 影响：AI全线
2. **半导体板块早盘拉升** — 中芯国际涨超5%，行业景气度回升
   - 来源：东方财富 | 可信度：高 | 影响：持仓相关
3. **美联储维持利率不变** — 鲍威尔暗示年内或降息1次
   - 来源：华尔街见闻 | 可信度：高 | 影响：黄金/美股

## 🤖 AI与大模型
- **Claude 4.5 发布** — 上下文窗口扩展至200K | Anthropic官方 | 高
- **Llama 3.1 开源** — 405B参数开源 | Meta AI | 高

## 📈 投资与市场
- **上证涨0.5%** — 科技股领涨，半导体ETF+1.2% | 东方财富 | 高
- **黄金回落至$4,280** — 美元走强压制 | 同花顺 | 中

## ⚙️ 科技与工程
- **K8s 1.31 发布** — 新增Sidecar容器GA | Kubernetes官方 | 高

## 🤖 驾驭工程
- **LangChain 0.3** — 支持多Agent编排 | LangChain官方 | 中

## 📊 数据速览
| 指标 | 数值 | 变化 |
|------|------|------|
| 上证指数 | 3,456 | +0.5% |
| 美元/人民币 | 7.25 | -0.1% |
| 黄金 | $4,280 | -0.3% |

## ⚠️ 需关注
- 半导体ETF持仓占比接近30%阈值，关注R3
- 美联储决议后续影响待观察

---
*本报告不构成投资建议，所有信息请以原始来源为准*
```

---

## 六、验收标准

| 指标 | 目标 | 验证方式 |
|------|------|----------|
| 每日生成率 | ≥95% | 30天内生成≥28天 |
| 字数控制 | ≤500字 | 自动统计 |
| 来源标注率 | 100% | 每条都有来源 |
| 今日必读准确 | ≥90% | 人工审核 |
| 领域覆盖 | 4/4 | 每个领域至少2条 |


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

**Self-P

> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
