# Python 自学课程系统 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 搭建一套个性化、中文讲解、Claude Code + OpenAI Codex 双端通用的 Python 自学课程系统，能按日生成 ipynb 讲解 + notes.md 讲稿 + pytest 练习 + AI 点评。

**Architecture:** 仓库由三个驱动文件（`profile.md`/`curriculum.md`/`progress.md`）+ 一个 `python-course` skill（4 个工作流）+ 按天产出的 `lessons/dayNN-*/` 构成。skill 读驱动文件生成当天课件；练习用 pytest 自动判分，再做 AI 点评。skill 内容工具中性，靠软链让 Codex 也能发现。

**Tech Stack:** Python 3.12+、uv（虚拟环境/依赖）、pytest、Jupyter（VS Code 原生）、Markdown、SKILL.md（YAML frontmatter）。

参考 spec：`docs/superpowers/specs/2026-06-06-python-course-skill-design.md`

---

### Task 0: 仓库初始化与工具链

**Files:**
- Create: `.gitignore`
- Create: `pyproject.toml`
- Create: `README.md`

- [ ] **Step 1: 初始化 git**

Run:
```bash
cd /Users/like/source/python-lesson && git init
```
Expected: `Initialized empty Git repository`

- [ ] **Step 2: 创建 `.gitignore`**

```gitignore
.venv/
__pycache__/
*.pyc
.pytest_cache/
.ipynb_checkpoints/
.DS_Store
.mypy_cache/
.ruff_cache/
```

- [ ] **Step 3: 创建 `pyproject.toml`**

```toml
[project]
name = "python-lesson"
version = "0.1.0"
description = "个性化 Python 自学课程系统"
requires-python = ">=3.12"
dependencies = []

[dependency-groups]
dev = ["pytest>=8", "ruff>=0.6", "mypy>=1.11", "jupyter>=1.0"]

[tool.pytest.ini_options]
testpaths = ["lessons"]
python_files = ["test_*.py", "*_test.py"]
```

- [ ] **Step 4: 用 uv 建环境并装开发依赖**

Run:
```bash
cd /Users/like/source/python-lesson && uv venv && uv sync --group dev
```
Expected: 创建 `.venv/`，安装 pytest/ruff/mypy/jupyter。若无 `uv`，回退：`python3 -m venv .venv && .venv/bin/pip install pytest ruff mypy jupyter`

- [ ] **Step 5: 创建 `README.md`**

```markdown
# Python 自学课程系统

个性化、中文讲解、Claude Code + Codex 双端通用的 Python 课程。

## 用法
- 出今日课：在 Claude Code 用 `Skill` 调起 `python-course`，或在 Codex 用 `$python-course`，说"出今日课"。
- 做练习：编辑 `lessons/dayNN-*/exercises/` 下的 `.py`，把 TODO 写完。
- 批改：说"批改第 N 天练习"，会跑 pytest + AI 点评。
- 复习：说"来个复习小测"。

## 结构
- `profile.md` 学习者画像 · `curriculum.md` 大纲 · `progress.md` 进度
- `lessons/` 每日课件 · `.claude/skills/python-course/` skill 本体
```

- [ ] **Step 6: 提交**

```bash
git add .gitignore pyproject.toml README.md
git commit -m "chore: 初始化仓库与 Python 工具链"
```

---

### Task 1: 三个驱动文件（profile / curriculum / progress）

**Files:**
- Create: `profile.md`
- Create: `curriculum.md`
- Create: `progress.md`

- [ ] **Step 1: 创建 `profile.md`（学习者画像，skill 每次读取）**

```markdown
# 学习者画像

- 编程背景：熟悉 Lua / C / JS，懂变量、循环、函数、控制流、数据结构等通用概念。
- Python 基础：无。
- 教学策略：**跳过零基础内容**；用**对比式**讲解（Python vs C/JS）；强调 Pythonic 惯用法。
- 语言：全程**中文**讲解；代码标识符用英文。
- 节奏：每日 1–1.5 小时，约 ⅓ 讲解 + ⅔ 动手。
- 目标方向（分支轨道顺序）：自动化脚本 → 数据分析 → Web(FastAPI) → AI/LLM。
- 代码检查：pytest 自动判分 + AI 点评（聚焦 Pythonic、命名、复杂度、纠正 C/JS 惯性）。
- 复习：采用间隔重复，从 progress.md 的易错点挑题。
```

- [ ] **Step 2: 创建 `curriculum.md`（全程大纲）**

```markdown
# 课程大纲（为有 C/JS 基础者定制）

> 每个 dayNN 对应一天（1–1.5h）。一个阶段可能跨多天。

## 核心阶段
- **P0 环境与心智**：venv/uv、pip、REPL、"一切皆对象"、与 C/JS 差异速览
- **P1 核心语法速通**：类型/f-string/真值/切片/解包/推导式（对比 C/JS）
- **P2 数据结构**：list/dict/set/tuple、collections
- **P3 函数进阶**：*args/**kwargs、默认参数陷阱、闭包、装饰器、类型注解
- **P4 OOP 与数据模型**：class、dataclass、dunder、property
- **P5 模块/异常/上下文管理器/迭代器·生成器**
- **P6 标准库与 Pythonic 工具**：pathlib、itertools、functools、typing、logging
- **P7 测试与工具链**：pytest、ruff、mypy、uv
- **P8 异步**：asyncio

## 分支轨道（各约一周）
1. 自动化脚本（文件处理、CLI、argparse、subprocess）
2. 数据分析（numpy、pandas、可视化）
3. Web/后端（FastAPI、Pydantic、SQLite）
4. AI/LLM（调用 API、数据管线、提示工程基础）

## 排期登记
| day | 阶段 | 主题 | 状态 |
|-----|------|------|------|
| 01 | P0/P1 | 环境与第一口 Python | 待生成 |
```

- [ ] **Step 3: 创建 `progress.md`（进度跟踪）**

```markdown
# 学习进度

## 已完成
（暂无）

## 当前位置
- 下一课：day01（P0/P1 环境与第一口 Python）

## 易错点 / 间隔复习清单
（批改后由 skill 追加，格式：`- [主题] 描述 — 下次复习日`）
```

- [ ] **Step 4: 提交**

```bash
git add profile.md curriculum.md progress.md
git commit -m "docs: 添加 profile/curriculum/progress 驱动文件"
```

---

### Task 2: python-course skill 本体

**Files:**
- Create: `.claude/skills/python-course/SKILL.md`

- [ ] **Step 1: 创建 `.claude/skills/python-course/SKILL.md`**

用工具中性措辞（"运行测试""创建文件"，不写"Bash 工具"），便于 Codex 复用。

````markdown
---
name: python-course
description: 个性化中文 Python 自学课程引擎。当用户说"出今日课/下一课""批改第 N 天练习""来个复习小测""调整节奏"时使用。读取 profile.md/curriculum.md/progress.md 生成或批改课件。
---

# python-course

为有 C/JS 基础、零 Python 的学习者，生成中文、对比式、每日 1–1.5h 的 Python 课程。

开始任何工作流前，先读 `profile.md`、`curriculum.md`、`progress.md` 获取背景与进度。

## 工作流 1：出今日课
1. 从 `progress.md` 读"下一课"，从 `curriculum.md` 读该主题。
2. 在 `lessons/dayNN-<主题>/` 下生成：
   - `lesson.ipynb`：中文讲解 + 可运行代码单元，按"概念→对比 C/JS→示例"组织，约占 ⅓ 时长。
   - `notes.md`：与 ipynb 同内容的干净中文讲稿（无代码输出杂质），供上传 NotebookLM。
   - `exercises/`：2–4 个 `.py` 起手文件，函数签名 + docstring + `# TODO`，约占 ⅔ 时长。
   - `tests/`：每个练习对应 `test_*.py`（pytest），覆盖正常 + 边界。
   - `solutions/`：参考答案，单独存放。
   - `conftest.py`：固定内容，把当天目录加入 sys.path，使 `from exercises.xxx import ...` 可用：
     `import pathlib, sys; sys.path.insert(0, str(pathlib.Path(__file__).parent))`
3. 更新 `curriculum.md` 排期表与 `progress.md` 当前位置。
4. 告诉用户今天要做什么、预计耗时。

## 工作流 2：批改练习
1. 运行该天 `tests/` 下的 pytest，报告通过/失败。
2. 失败：指出失败用例，给**分级提示**（先方向，再具体，最后才贴答案），不直接给完整答案。
3. 通过：做 AI 点评，依 rubric——是否 Pythonic、命名、复杂度、是否残留 C/JS 惯性写法、可改进点。
4. 把暴露的易错点按间隔重复追加到 `progress.md`。

## 工作流 3：复习小测
1. 从 `progress.md` 易错点清单挑到期项，出 3–5 道小题（含代码判断/改写）。
2. 批改并更新下次复习日。

## 工作流 4：调整节奏
1. 用户反馈太快/太慢时，重排 `curriculum.md` 后续 day 的粒度，并据此重生成。

## 约定
- 全程中文讲解；标识符用英文。
- 对比式：凡 Python 与 C/JS 显著不同处，明确点出差异。
- 测试保证正确性，点评只谈风格与改进。

## 调用方式速查
- Claude Code：用 `Skill` 工具调起本 skill。
- OpenAI Codex：`/skills` 或 `$python-course`。
````

- [ ] **Step 2: 提交**

```bash
git add .claude/skills/python-course/SKILL.md
git commit -m "feat: 添加 python-course skill"
```

---

### Task 3: 跨工具兼容（Codex 软链 + 校验）

**Files:**
- Create: `.codex/skills/python-course` (symlink)

- [ ] **Step 1: 建软链，让 Codex 发现同一份 skill**

Run:
```bash
cd /Users/like/source/python-lesson && mkdir -p .codex/skills && ln -s ../../.claude/skills/python-course .codex/skills/python-course
```
Expected: `.codex/skills/python-course` → `../../.claude/skills/python-course`

- [ ] **Step 2: 校验软链指向有效 SKILL.md**

Run:
```bash
cat /Users/like/source/python-lesson/.codex/skills/python-course/SKILL.md | head -3
```
Expected: 输出 SKILL.md 前几行（含 `name: python-course`），证明软链可读。

- [ ] **Step 3: 提交**

```bash
git add .codex
git commit -m "feat: 软链 skill 到 .codex 供 OpenAI Codex 复用"
```

---

### Task 4: Day 1 课件作为参考模板（含 pytest，TDD）

Day 1 = P0/P1「环境与第一口 Python」。两个练习用于打通 pytest 管线：`celsius_to_fahrenheit`（基础语法/f-string）与 `fizzbuzz`（控制流，对比 C/JS）。

**Files:**
- Create: `lessons/day01-环境与第一口python/notes.md`
- Create: `lessons/day01-环境与第一口python/lesson.ipynb`
- Create: `lessons/day01-环境与第一口python/exercises/ex1_temperature.py`
- Create: `lessons/day01-环境与第一口python/exercises/ex2_fizzbuzz.py`
- Create: `lessons/day01-环境与第一口python/tests/test_ex1_temperature.py`
- Create: `lessons/day01-环境与第一口python/tests/test_ex2_fizzbuzz.py`
- Create: `lessons/day01-环境与第一口python/solutions/ex1_temperature.py`
- Create: `lessons/day01-环境与第一口python/solutions/ex2_fizzbuzz.py`
- Create: `lessons/day01-环境与第一口python/conftest.py`

- [ ] **Step 0: 写 `conftest.py`，让 pytest 能 import exercises**

放在当天目录根，使无论从哪运行 pytest，`exercises` 都可作为命名空间包导入：

```python
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
```

- [ ] **Step 1: 写 `tests/test_ex1_temperature.py`（先失败）**

```python
from exercises.ex1_temperature import celsius_to_fahrenheit


def test_zero():
    assert celsius_to_fahrenheit(0) == 32.0


def test_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_negative():
    assert celsius_to_fahrenheit(-40) == -40.0
```

- [ ] **Step 2: 写练习起手文件 `exercises/ex1_temperature.py`（留 TODO，使测试失败）**

```python
def celsius_to_fahrenheit(c: float) -> float:
    """摄氏转华氏：F = C * 9/5 + 32。

    对比 C：Python 的 / 永远是浮点除法，整数除法用 //。
    """
    # TODO: 实现转换公式
    raise NotImplementedError
```

- [ ] **Step 3: 运行测试，确认失败**

Run:
```bash
cd /Users/like/source/python-lesson/lessons/day01-环境与第一口python && ../../.venv/bin/pytest tests/test_ex1_temperature.py -v
```
Expected: FAIL（`NotImplementedError`）

- [ ] **Step 4: 写参考答案 `solutions/ex1_temperature.py`**

```python
def celsius_to_fahrenheit(c: float) -> float:
    """摄氏转华氏：F = C * 9/5 + 32。"""
    return c * 9 / 5 + 32
```

- [ ] **Step 5: 写 `tests/test_ex2_fizzbuzz.py`（先失败）**

```python
from exercises.ex2_fizzbuzz import fizzbuzz


def test_plain_number():
    assert fizzbuzz(1) == "1"


def test_fizz():
    assert fizzbuzz(3) == "Fizz"


def test_buzz():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
```

- [ ] **Step 6: 写练习起手文件 `exercises/ex2_fizzbuzz.py`（留 TODO）**

```python
def fizzbuzz(n: int) -> str:
    """3 的倍数返回 'Fizz'，5 的倍数 'Buzz'，都满足 'FizzBuzz'，否则返回数字字符串。

    对比 C/JS：Python 用 f-string 格式化，用 % 取模，无 switch。
    """
    # TODO: 实现 fizzbuzz 逻辑
    raise NotImplementedError
```

- [ ] **Step 7: 运行测试，确认两个练习都失败**

Run:
```bash
cd /Users/like/source/python-lesson/lessons/day01-环境与第一口python && ../../.venv/bin/pytest -v
```
Expected: FAIL（两个练习均 `NotImplementedError`）

- [ ] **Step 8: 写参考答案 `solutions/ex2_fizzbuzz.py`**

```python
def fizzbuzz(n: int) -> str:
    """FizzBuzz。"""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
```

- [ ] **Step 9: 写 `notes.md`（中文讲稿，供 NotebookLM）**

```markdown
# Day 01 · 环境与第一口 Python

## 1. 环境
- 用 `uv venv` 建虚拟环境，`uv sync` 装依赖。对比 C：无需编译，Python 是解释执行。
- REPL：终端敲 `python` 进入交互式，可即时验证想法。

## 2. 心智模型：一切皆对象
- 整数、函数、类本身都是对象，都有类型。与 C 的"基本类型 vs 结构体"不同。
- 变量是"名字绑定到对象"，不是"内存盒子"。赋值是重新绑定。

## 3. 与 C/JS 的关键差异速览
- 缩进即代码块，无 `{}`。
- `/` 永远浮点除法，整数除法用 `//`。
- 无 `switch`；多分支用 `if/elif/else`。
- 字符串格式化首选 f-string：`f"{name} = {value}"`。

## 4. 今日练习
- `celsius_to_fahrenheit`：体会浮点除法与 f-string。
- `fizzbuzz`：体会取模与多分支，对比你熟悉的 C/JS 写法。
```

- [ ] **Step 10: 写 `lesson.ipynb`（与 notes.md 同内容 + 可运行单元）**

创建一个最小可用的 notebook（Markdown 讲解单元 + 几个代码单元演示 f-string、`//` vs `/`、`%`）。内容结构对应 notes.md 四节，代码单元示例：

```python
# 一切皆对象
print(type(3), type(print), type(int))

# 除法差异
print(7 / 2)   # 3.5  浮点
print(7 // 2)  # 3    整除

# f-string
name, value = "x", 42
print(f"{name} = {value}")
```

ipynb 用标准 nbformat v4 结构（`cells` 数组，cell 含 `cell_type`/`source`/`metadata`，代码单元加 `outputs: []` 与 `execution_count: null`）。

- [ ] **Step 11: 更新排期文件**

把 `curriculum.md` 排期表 day01 状态改为"已生成"，把 `progress.md` 当前位置改为 day02。

- [ ] **Step 12: 提交**

```bash
cd /Users/like/source/python-lesson && git add lessons curriculum.md progress.md && git commit -m "feat: day01 课件模板（环境与第一口 Python）"
```

---

### Task 5: 端到端验收

**Files:** 无新建，仅验证。

- [ ] **Step 1: 跑通 day01 全部测试（用参考答案临时验证再还原）**

Run:
```bash
cd /Users/like/source/python-lesson/lessons/day01-环境与第一口python && cp solutions/*.py exercises/ && ../../.venv/bin/pytest -v && git checkout exercises/
```
Expected: 全部 PASS，随后 exercises 还原为 TODO 版。

- [ ] **Step 2: 确认 ipynb 合法**

Run:
```bash
cd /Users/like/source/python-lesson && .venv/bin/python -c "import nbformat; nbformat.read('lessons/day01-环境与第一口python/lesson.ipynb', as_version=4); print('ipynb OK')"
```
Expected: `ipynb OK`

- [ ] **Step 3: 确认 skill 两端均可被发现**

Run:
```bash
test -f /Users/like/source/python-lesson/.claude/skills/python-course/SKILL.md && test -f /Users/like/source/python-lesson/.codex/skills/python-course/SKILL.md && echo "两端 SKILL.md 均可读"
```
Expected: `两端 SKILL.md 均可读`

- [ ] **Step 4: 对照验收标准（spec 第 10 节）逐条确认**

- [ ] 能一键生成 day01 完整产物（ipynb+notes+exercises+tests）✓
- [ ] 写完练习能跑测试 + AI 点评（工作流 2）✓
- [ ] curriculum 覆盖 P0–P8 + 四轨道 ✓
- [ ] notes.md 干净中文可上传 NotebookLM ✓
- [ ] Claude Code 与 Codex 两端可发现 skill ✓

- [ ] **Step 5: 提交验收记录（如有微调）**

```bash
cd /Users/like/source/python-lesson && git add -A && git commit -m "test: day01 端到端验收通过" --allow-empty
```
