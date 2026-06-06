# Python 自学课程系统 — 设计文档

- 日期：2026-06-06
- 状态：已批准，待 spec 复核
- 作者：与 Claude Code 协作

## 1. 背景与目标

学习者已有 **Lua / C / JS** 编程基础，但**没有 Python 基础**。目标是用一套**可重复、个性化、中文讲解**的课程系统自学 Python，覆盖核心语言 + 四个应用方向（AI/ML、Web/后端、自动化脚本、数据分析）。

核心需求：
- 每日课程（节奏 1–1.5 小时/天）
- 按"有编程基础"重排的概念顺序（跳过零基础废话，对比式教学）
- 练习题 + **自动判对错（pytest）+ AI 点评**
- 自动生成 Jupyter Notebook（VS Code 原生支持）
- 生成干净中文讲稿，便于上传 NotebookLM 复习/听音频
- 进度跟踪与间隔复习

## 2. 战略决策：自建课程 skill（而非用现成 skill）

现成 skill（coding-tutor / socratic-tutor）默认面向零基础、英文为主、不产出"ipynb + notes.md + pytest"这套固定管线，与本需求不匹配。

**决策：自建一个轻量的课程 skill**，但**借鉴**现成思路（socratic 的分级提示、coding-tutor 的间隔重复），不整包安装。

## 3. NotebookLM 集成方式

事实核查（2026-06）：NotebookLM **没有面向个人的官方 API**，仅有 Google Cloud 企业版 API。社区有非官方库 `notebooklm-py`（浏览器自动化）。

**方案**：课程生成干净中文 `notes.md`，**手动上传 NotebookLM** 听音频/复习。未来如需自动化，再评估接入 `notebooklm-py`。本期范围**不含**自动化接入。

## 4. 仓库结构

```
curriculum.md          # 全程教学大纲（按"有基础"排序）
profile.md             # 学习者画像：背景/节奏/约定，skill 每次读取
progress.md            # 进度 + 易错点 + 间隔复习清单
lessons/
  dayNN-主题/
    lesson.ipynb       # Jupyter 讲解，可边读边跑
    notes.md           # 干净中文讲稿 → 传 NotebookLM
    exercises/         # 练习起手文件 .py（含 TODO）
    tests/             # 对应 pytest，自动判对错
    solutions/         # 参考答案（单独存放）
.claude/skills/python-course/SKILL.md   # 自建 skill
```

## 5. 自建 skill 的能力（4 个工作流）

1. **出今日课**：读 `curriculum.md` + `progress.md` → 生成当天 `lesson.ipynb` + `notes.md` + `exercises/` + `tests/`。约 ⅓ 讲解 + ⅔ 动手。
2. **批改练习**：跑 pytest 自动判对错 → AI 点评，聚焦"是否 Pythonic、命名、复杂度、纠正从 C/JS 带来的惯性"。
3. **复习/小测**：从 `progress.md` 按间隔重复挑题。
4. **调节奏**：太快/太慢时重排后续大纲 + 重生成。

## 6. 概念顺序（为"有 C/JS 基础者"定制，对比式教学）

核心阶段：
- **P0 环境与心智**：venv/uv、pip、REPL、"一切皆对象"、与 C/JS 差异速览
- **P1 核心语法速通**：类型/f-string/真值/切片/解包/推导式（对比 C/JS）
- **P2 数据结构**：list/dict/set/tuple、collections
- **P3 函数进阶**：*args/**kwargs、默认参数陷阱、闭包、装饰器、类型注解
- **P4 OOP 与数据模型**：class、dataclass、dunder、property
- **P5 模块/异常/上下文管理器/迭代器·生成器**
- **P6 标准库与 Pythonic 工具**：pathlib、itertools、functools、typing、logging
- **P7 测试与工具链**：pytest、ruff、mypy、uv
- **P8 异步**：asyncio

分支轨道（各约一周，顺序固定）：
自动化脚本 → 数据分析(pandas/numpy) → Web(FastAPI) → AI(LLM API/管线)

## 7. 代码检查流程

- 每题配 `tests/` 下的 pytest，正确性由测试保证。
- 测试通过后，AI 点评依据 rubric：Pythonic 程度、命名、复杂度、是否残留 C/JS 惯性写法、可改进点。

## 8. 跨工具兼容（Claude Code + OpenAI Codex）

需求：同一套课程 skill 既能在 Claude Code 用，也能在 OpenAI Codex 用。

事实核查（2026-06）：Codex 已采用与 Claude Code **相同的 `SKILL.md` 格式**（YAML frontmatter 的 `name` + `description`，可选 `scripts/`、`references/`、`assets/`）。差异仅三处：

| 维度 | Claude Code | OpenAI Codex |
|---|---|---|
| skill 位置 | `.claude/skills/`、`~/.claude/skills/` | `~/.codex/skills/`、repo 内 `.codex/skills/` 或 `.agents/skills/` |
| 调用 | `Skill` 工具 | `/skills` 或 `$python-course` |
| 工具名 | Read/Edit/Bash… | Codex 工具等价物 |

**实现方式（一份内容、两边通用）：**
1. 规范 skill 只在 `.claude/skills/python-course/` 维护一份。
2. SKILL.md 用**工具中性措辞**（"运行该目录下的 pytest""创建文件"），不写死 "Bash 工具" 等 Claude 专有名词。
3. 在 repo 内放 `.codex/skills/python-course` **软链接**指向规范目录，避免重复维护；SKILL.md 末尾附一小段"调用方式速查"（Claude 用 Skill 工具 / Codex 用 `$python-course`）。
4. 验收：在 Codex 里 `$python-course` 能发现并执行"出今日课""批改练习"两个工作流。

## 9. 范围边界（YAGNI）

本期**包含**：仓库结构、profile/curriculum/progress 三个驱动文件、python-course skill 的 4 个工作流、P0–P8 + 四个分支轨道的大纲、pytest + AI 点评、Claude Code + Codex 跨工具兼容。

本期**不含**：NotebookLM 自动化接入、Gemini CLI 适配（如需另起）、Web 部署、打分排行榜/游戏化、多用户。

## 10. 验收标准

- 能用 skill 一键生成"第 1 天"完整产物（ipynb + notes.md + exercises + tests）。
- 写完练习后能一键跑测试并得到 AI 点评。
- curriculum.md 覆盖 P0–P8 + 四轨道，且顺序适配有基础学习者。
- notes.md 为干净中文、可直接上传 NotebookLM。
- 在 Claude Code 与 OpenAI Codex 两端都能发现并运行 python-course skill。
