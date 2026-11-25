# 五层架构

## 1. 数据接入层

接收历史 SOP Prompt、Markdown、文本导出内容，并执行解析和拆分。

## 2. 标准化层

通过 `USkill` Schema 统一技能元数据、输入输出、执行模板、控制策略和溯源信息。

## 3. 驾驭引擎层

围绕超时、中断、重试、断点、Mock、Fallback 建立执行治理能力。

## 4. 技能编排层

原子技能可进一步组合成复杂 SOP 工作流。

## 5. 应用输出层

通过 CLI、SDK、适配器和 GitHub Pages 面向开发者与 Agent 系统提供能力。

---

# V2.0 模块视图

```
输入 SOP ──► converter/parse_sop（结构化解析·全量溯源）──► USkill YAML
外部技能 ──► agentskills（SKILL.md 校验/导入）──► 双层技能目录
                                    │
              schema + validator（结构 + 语义校验）
                                    │
              runtime/engine ──► 输入治理 → 计划(approval/subskill/llm)
                    │                → 超时/重试 → 输出校验 → 检查点
                    ├── providers（mock / openai-chat / openai-responses / openai-compatible / anthropic / local）
                    ├── tools（ToolRegistry + PermissionPolicy 白名单）
                    └── state（RunRecord/RunStore 事件流与恢复）
                                    │
        governance（生命周期门禁 Draft→…→Published） + audit（JSONL 审计）
                                    │
              evaluation（基线对照 + 确定性评分）──► 发布决策
```

关键原则：

1. **声明不等于授权**：技能里写的 `tools`/权限只是声明，运行时白名单才生效。
2. **适配层不实现执行**：LangChain/OpenAI 适配器一律委托 runtime。
3. **评测独立于生成**：生成技能的模型不能自证有效，评测框架使用确定性断言。
