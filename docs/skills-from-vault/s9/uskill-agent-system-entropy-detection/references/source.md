
# uSkill-系统熵增检测-v1

> 监控知识库无序度增长趋势并触发治理的技能。熵增是静默的：断链率回升、孤岛增加、标签漂移、重复内容、短文件膨胀——单个信号微弱，组合信号致命。

## 🎯 目标

在系统热熵突破治理阈值之前给出**可溯源、可量化**的预警，使 [[uSkill-agent-全局审计专项循环]] 能按"结构→内容→体系"三层精准投放治理资源，而非盲目全量扫描。

核心交付：
- 一份**熵增指数（Entropy Index, EI）** 综合评分（0–100，越高越混乱）。
- 每个构成指标的**方向标注**（higher-better / lower-better）与**阈值触发状态**。
- 一张**治理优先级队列**（按 EI 贡献度排序）。

## 📥 输入

| 参数 | 含义 | 方向 | 来源 |
|------|------|------|------|
| `broken_link_rate` | 断链率（断链数 / 总 wikilink 数） | lower-better | L1 结构扫描 |
| `orphan_rate` | 孤岛率（无出入链笔记 / 总笔记） | lower-better | L1 结构扫描 |
| `tag_compliance` | 标签合规率 | higher-better | L1 结构扫描 |
| `short_file_rate` | 短文件率（<500B 笔记占比） | lower-better | L1 结构扫描 |
| `dup_signal` | 重复内容信号（近似文本簇数） | lower-better | L2 内容扫描 |
| `dominant_domain_pct` | 单一领域标签权重 | lower-better（≤40%） | L3 体系扫描 |
| `moc_coverage` | MOC 路由覆盖率 | higher-better | L3 体系扫描 |
| `trend_delta` | 较上期的指标变化 | 见各指标 | trend.json |

> 所有输入来自 `00-META/审计/trend.json`，结合 [[uSkill-agent-循环工程-审计-调度数据契约]] 字段契约。

## 📤 输出

```json
{
  "audit_date": "2026-07-08",
  "entropy_index": 12.4,
  "grade": "A",
  "signals": [
    {"metric": "broken_link_rate", "value": 0.019, "direction": "lower-better",
     "threshold": 0.02, "status": "normal", "ei_contrib": 3.1},
    {"metric": "dominant_domain_pct", "value": 39.4, "direction": "lower-better",
     "threshold": 40.0, "status": "warning", "ei_contrib": 5.2}
  ],
  "govern_queue": [
    {"action": "偏科阻尼", "target": "维度/学习", "priority": "P1"}
  ]
}
```

## 🔄 执行流程

1. **采集**：从 trend.json 拉取最新 L1/L2/L3 指标与 `trend_delta`。
2. **归一化**：每个指标按方向映射到 [0,1] 的"混乱度"分量（higher-better 反向计分）。
3. **加权合成**：EI = Σ(分量 × 权重)，权重见下方质量自检。
4. **阈值判定**：逐项对比阈值，产出 `normal / warning / critical`。
5. **队列生成**：按 `ei_contrib` 降序排列治理动作。
6. **回流**：将 `govern_queue` 写入次日晨间计划置顶（P0/P1）。

### 决策分支（IF / THEN）

- IF `broken_link_rate` ≥ 0.10 → THEN 触发审计熔断，纳入 P0，立即启动死链收容。
- IF `dominant_domain_pct` ≥ 40 → THEN 红色熔断，强制重分类骨架笔记至其他维度（偏科治理）。
- IF `tag_compliance` < 1.0 → THEN 启动脏标签零容忍，阻断并提示归类（Yellow 预警在 35%–40% 限流）。
- IF `trend_delta` 中任一指标恶化 > 10% → THEN 标注 `📈 趋势异常` 并生成对应行动建议。
- IF `short_file_rate` 连续 2 周上升 → THEN 触发骨架折叠 SOP，合并 D1-A3-I3 空壳。

## 📝 Prompt 模板

```markdown
# 角色
你是知识库熵增侦探，只认数字不认感觉。

# 输入
- 指标快照：{{signals}}
- 上期对比：{{trend_delta}}
- 契约：[[uSkill-agent-循环工程-审计-调度数据契约]]

# 任务
1. 对每个 metric 判定 direction，计算混乱度分量。
2. 合成 EI，给出 grade。
3. 逐项阈值判定，输出 status。
4. 按 ei_contrib 降序生成 govern_queue。

# 硬性规则
- higher-better 指标：值越低混乱度越高（反向计分）。
- lower-better 指标：值越高混乱度越高（正向计分）。
- 任何数字必须来自 trend.json，禁止捏造。
```

## ⚠️ 异常处理

- **trend.json 缺失/损坏**：回退上次成功缓存，标注 `⚠️ 基于缓存`，EI 置信度下调。
- **某指标为 null**：该分量计 0 贡献但标记 `⚪ 缺源`，不强行估算。
- **指标互相矛盾**（如断链降但孤岛升）：分别独立判定，不在合成中相互抵消，避免掩盖单点恶化。
- **写入冲突**：trend.json 文件锁时重试 3 次（间隔 1s），失败写 `trend.json.pending`。

## ✅ 质量自检

EI 合成权重（可溯源，合计 1.0）：
- `broken_link_rate` 0.25（lower-better，阈值 0.02）
- `orphan_rate` 0.20（lower-better，阈值 0.05）
- `tag_compliance` 0.15（higher-better，目标 1.0）
- `short_file_rate` 0.10（lower-better，阈值 0.01）
- `dup_signal` 0.10（lower-better）
- `dominant_domain_pct` 0.20（lower-better，阈值 40%）

判定矩阵：
- EI < 15 → A（健康）；15–30 → B（温和）；30–50 → C（预警）；> 50 → D（危机）。

自检项：
- [ ] 每个 signal 明确标注 direction。
- [ ] EI 分量求和 = 1.0。
- [ ] 数字 100% 来自 trend.json。
- [ ] govern_queue 按 ei_contrib 降序。

## 💡 使用示例

**输入**（节选自 2026-06-25 真实全量）：`broken_link_rate`=0.0158、`orphan_rate`=0.148、`tag_compliance`=1.0、`dominant_domain_pct`=39.4。

**输出**：EI≈12.4（A）。`dominant_domain_pct` 39.4% 触发 warning（临界 40%），govern_queue 生成"偏科阻尼 / 维度-学习 / P1"。断链率 1.58% 已达标，不触发治理。

**逻辑闭环**：该结果与 [[uSkill-agent-全局审计专项循环]] 月报一致——学习域 39.4% 处于橙色预警带，验证了指标方向（lower-better）与阈值（40%）的可追踪性。

## 🧪 Self-Play 测试

| # | 场景 | 期望 |
|---|------|------|
| 1 | broken_link_rate=0.0158, orphan=0.148 | EI≈12.4,A，无 P0 |
| 2 | dominant_domain_pct=42.0 | 红色熔断，强制重分类，P0 |
| 3 | tag_compliance=0.93 | 脏标签预警，阻断归类 |
| 4 | trend_delta 断链 +18% | 标注趋势异常并给行动建议 |
| 5 | 某指标为 null | 该分量 0 贡献，标记缺源，不估算 |
| 6 | broken_link_rate=0.11 | 审计熔断，P0 立即死链收容 |

### 熵增信号字典（可追踪定义）

- **断链率** `broken_link_rate = 断链数 / 总 wikilink 数`（lower-better）。剔除 `audit_exceptions.json` 豁免项后计算。
- **孤岛率** `orphan_rate = 无出入链笔记 / 总笔记`（lower-better）。排除 08-CALENDAR 与 7 天内新创闪念。
- **标签合规率** `tag_compliance`（higher-better）。非标标签即时阻断，目标 100%。
- **短文件率** `short_file_rate = <500B 笔记 / 总笔记`（lower-better）。
- **领域主导度** `dominant_domain_pct`（lower-better）。单一维度标签权重，阈值 40%。
- **MOC 覆盖率** `moc_coverage`（higher-better）。核心 MOC 对子域高频笔记覆盖率，阈值 85%。

> 任一数字均来自 `00-META/审计/trend.json`，与 [[uSkill-agent-全局审计专项循环]] 同源，保证可溯源。

### EI 合成示例（可反推验证）

取 2026-06-25 快照：broken_link_rate=1.58% → 分量=1.58/2×0.25≈0.20；orphan_rate=14.8% → 分量=14.8/5×0.20≈0.59；tag_compliance=100% → 分量=0；short_file_rate 假设 0.8% → 0.8/1×0.10≈0.08；dominant_domain_pct=39.4% → 39.4/40×0.20≈0.20。EI 原始和≈1.07，归一化到 0–100 后约 10.7，评级 A，与月报健康度 93.0(A) 方向一致。

### 熵增信号 ↔ 三层审计映射

| 信号 | 来源层 | 治理循环 |
|------|------|------|
| broken_link_rate | L1 结构 | 死链收容（每日） |
| orphan_rate | L1 结构 | 孤岛硬收容（每日） |
| tag_compliance | L1 结构 | 脏标签阻断（每日） |
| dup_signal | L2 内容 | 折叠/合并（每周） |
| dominant_domain_pct | L3 体系 | 偏科治理（每月） |
| moc_coverage | L3 体系 | MOC 路由补全（每月） |

## 边界约束

- 只读 trend.json 与扫描报告，不修改笔记正文。
- 偏科治理的强制重分类需经调度中枢路由，本技能只产出队列不执行。
- 豁免白名单（`audit_exceptions.json`）中的故意过时/骨架/模板指令不计入熵增。

## 校验验收规则

- 每个 metric 必须带 direction 与 threshold。
- EI 与 grade 必须可由信号反推（数字可溯源）。
- govern_queue 动作必须对应真实审计 SOP。

## 迭代触发条件

- 新增指标类型（如语义漂移）时升 minor 版本并重算权重。
- 阈值经验证失真（连续误报）时回调阈值。

---

## 相关

- [[uSkill-agent-系统熵增检测-agent-实施手册]]
- [[uSkill-agent-全局审计专项循环]]
- [[系统结构决定行为法则]]
- [[∑ uSkill]]
- [[循环工程]]


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
