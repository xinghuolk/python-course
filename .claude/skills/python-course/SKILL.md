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
