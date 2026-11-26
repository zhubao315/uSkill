
description: |
  当用户需要文档/格式转换时使用此 Skill。
  触发词包括：'markdown转html'、'md转html'、'convert md to html'、'微信外链转底部引用'、
  '转word'、'转docx'、'md转word'、'技术方案word'、'生成word文档'。
  v3.1.0 起指向库内本地组件：`09-REFERENCE/93-脚本/md_to_docx.py`
  （Markdown → 封面 + 目录 + 中文专业版式的 .docx；HTML 走 pandoc 单行）。

---

# 🌐 Markdown转文档（HTML · Word）

## 🎯 目标

> 将 Markdown 转换为可交付文档：**Word（.docx，封面 + 目录 + 中文专业版式）** 或 带样式 HTML（兼容微信主题）。

**工具类型**：库内本地组件（v3.1.0 升级） | **实际路径**：`09-REFERENCE/93-脚本/md_to_docx.py`

> ⚠️ v3.0.0 指向的 `~/.claude/skills/baoyu-markdown-to-html` 已不存在（死链），本版改为本地 pandoc + python-docx 组件，离线可用、验收内置。

---

## 📥 触发条件

| 条件 | 说明 |
|------|------|
| 触发词 | 'markdown转html'、'md转html'、'转word'、'md转docx'、'技术方案word'、'生成word文档' |
| 工具依赖 | pandoc ≥2.x + python-docx ≥1.0（组件自动校验，缺失即报错） |
| 分类 | 文档/格式转换 |

---

## 🔧 执行方式

**Word 技术方案（主能力）**：

```bash
python3 09-REFERENCE/93-脚本/md_to_docx.py INPUT.md [-o OUT.docx] \
    [--title 封面标题] [--subtitle "技术方案 · v1.0"] [--date YYYY-MM-DD] \
    [--header 页眉] [--no-toc] [--toc-depth 2] [--force-ref]
```

- 自动预处理：去 YAML frontmatter · `[[wikilink]]` → 纯文本 · 首个 H1 提为封面标题 · 其余标题提升一级（避开代码围栏）
- 自动版式：A4 · 封面独立页 · 目录（打开时自动更新域）· 黑体标题 / 宋体正文 1.5 倍行距 · 表格网格 + 表头底纹 + 跨页重复 · 页眉 + 页脚页码
- 样式缓存：`.runtime/cache/md_to_docx/reference_v1.docx`（`--force-ref` 重建）
- 内置验收：封面/目录/页眉/页码四项 + 段落表格计数，失败非零退出

**HTML（辅助能力）**：

```bash
pandoc INPUT.md -f gfm -s -o OUTPUT.html --metadata title="标题"
```

---

## 📋 与其他 uSkill 的关系

- **上游**：此工具可被 `uSkill-agent-循环工程统一调度入口` 调度使用
- **下游**：生成的内容可流入 `uWise` 知识词条或 `uRead` 读书笔记
- **协作**：与同类别 uSkill 配合使用，如配图类工具可组合使用

---

## 📝 自检清单

- [ ] 是否在正确的场景触发了此工具？
- [ ] 工具参数是否正确配置？
- [ ] 输出是否符合预期格式？
- [ ] 是否需要与其他工具组合使用？

---

*关联：[[uSkill-agent-循环工程统一调度入口]] · [[uSkill-agent-全局审计专项循环]] · [[Home]]*


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


**相关概念**：[[信息管理系统]]

---


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
