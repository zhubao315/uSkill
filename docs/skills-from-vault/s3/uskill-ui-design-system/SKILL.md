---
name: uskill-ui-design-system
description: "组件库不是限制创造力——是让创造力在一致的框架内绽放。"
license: MIT
metadata:
  source: "private:zhubao315/obsidian-vault/02-BUILD/22-uSkill/S3-产品设计与创意/uSkill-ui-design-system.md"
  original_id: "SKL-6405"
  version: "3.0.0"
  trust: untrusted
---

# UI设计系统

description: |
  当用户需要构建设计系统、组件库、Design Token、UI 规范时使用此 Skill。
  触发词：'设计系统'、'组件库'、'Design Token'、'UI规范'、'design system'。

# UI 设计系统

## 🎯 目标

> 构建可复用、可扩展、一致的 UI 设计系统，提升设计和开发效率。

## 📥 输入

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `scope` | enum | ❌ | `"full"` | 范围：`full` / `tokens_only` / `components_only` |
| `platform` | enum | ❌ | `"web"` | 平台：`web` / `mobile` / `both` |
| `framework` | enum | ❌ | `"react"` | 框架：`react` / `vue` / `flutter` / `swift` |

## 📤 输出

```json
{
  "design_tokens": {"colors": "string", "spacing": "string", "typography": "string", "shadows": "string"},
  "component_list": ["string — 核心组件列表"],
  "component_spec": {"name": "string", "variants": ["string"], "states": ["string"], "sizes": ["string"]},
  "accessibility": "string — 无障碍规范"
}
```

## 📋 执行步骤

### Step 1: Design Token 体系
1. **颜色系统** — 主色/中性色/语义色（成功/警告/错误/信息）
2. **间距系统** — 4px 基础单位的倍数序列
3. **字体系统** — 字号/字重/行高/字间距
4. **阴影与圆角** — 层级化的阴影和圆角系统
5. **检查点**：✅ Token 是否系统化？是否有暗色模式适配？

### Step 2: 组件设计
1. **原子组件** — Button/Input/Icon/Avatar
2. **分子组件** — Card/Modal/Toast/Tooltip
3. **有机组件** — Navigation/Sidebar/Header/Footer
4. **状态变体** — 每个组件的完整状态集
5. **检查点**：✅ 组件是否覆盖了核心 UI 模式？状态变体是否完整？

### Step 3: 无障碍合规
1. **WCAG AA** — 颜色对比度 ≥4.5:1
2. **键盘导航** — 所有组件可键盘操作
3. **屏幕阅读器** — 语义化 HTML + ARIA 属性
4. **检查点**：✅ 颜色对比度是否达标？是否支持键盘导航？

### Step 4: 文档与交付
1. **组件文档** — 每个组件的使用示例和 API
2. **Figma 组件库** — 与代码组件一一对应
3. **变更日志** — 版本化管理
4. **检查点**：✅ 文档是否完整？Figma 与代码是否同步？

## 💬 沟通风格
- **系统思维**：每个决策都考虑对整个系统的影响
- **一致性优先**：统一 > 好看
- **开发者友好**：组件 API 设计考虑开发者体验

## 📝 自检清单
- [ ] Design Token 是否系统化？
- [ ] 组件状态变体是否完整？
- [ ] 颜色对比度是否 ≥4.5:1？
- [ ] 是否支持键盘导航？
- [ ] 文档是否完整？

---


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
| 2026-07-03 | 1.0.0 | 初始版本，对标 agency-agents UI Designer + UX Architect |


---


---

## 📖 Context Read `[v3新增]`

> 来源：taste-skill 的 Brief Inference + Design Read

在执行前，先输出一行判断：

> "Reading this as: [摄影场景] for [拍摄者水平], with [创作优先级], leaning toward [器材/环境约束]."

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
| ""直接给一组参数就行了"" | "不知道用户场景就给参数，是赌博不是指导" |
| ""ISO 高一点没关系"" | "后期降噪损失细节，能前期解决就别留后期" |
| ""先拍一张试试看"" | "曝光三角的价值在于拍前就知道结果" |
| ""这个场景太简单了"" | "越简单越容易犯低级错误" |
| ""用户没问安全快门"" | "安全快门是糊片第一道防线，必须主动检查" |

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



> This skill was converted from a private personal vault. The complete original text is in `references/source.md`; original frontmatter is in `references/source-metadata.md`. Scripts, if any, are never executed during import.
