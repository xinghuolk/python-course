# Python 自学课程系统

个性化、中文讲解、Claude Code + Codex 双端通用的 Python 课程。

## 用法
- 出今日课：在 Claude Code 用 `Skill` 调起 `python-course`，或在 Codex 用 `$python-course`，说"出今日课"。
- 做练习：编辑 `lessons/dayNN-*/exercises/` 下的 `.py`，把 TODO 写完。
- 批改：说"批改第 N 天练习"，会跑 pytest + AI 点评。
- 复习：说"来个复习小测"。

## 用 Notebook 学习

每天的课件有两种 notebook 用途，互不冲突：

### 1. Jupyter Notebook（`lesson.ipynb`）— 边读边跑
VS Code 原生支持，用来跟着讲解动手运行代码。

1. 在 VS Code 安装扩展 **Python** 和 **Jupyter**（Microsoft 出品）。
2. 打开 `lessons/dayNN-*/lesson.ipynb`。
3. 右上角点 **Select Kernel** → **Python Environments** → 选本项目的 `.venv`（解释器路径 `./.venv/bin/python`）。
4. 逐个单元运行：点单元左侧 ▶，或按 `Shift+Enter` 运行并跳到下一格。`Ctrl+Enter` 原地运行。
5. 想从头重跑：顶部 **Run All**；状态乱了点 **Restart** 清空内核再跑。

> 命令行备选：`uv run jupyter lab`（或 `.venv/bin/jupyter lab`）在浏览器里打开。

### 2. NotebookLM（`notes.md`）— 复习与听音频
`notes.md` 是干净的中文讲稿，适合喂给 Google NotebookLM 做复习。

1. 打开 [notebooklm.google.com](https://notebooklm.google.com)，新建 notebook。
2. **Add source** → 上传当天的 `notes.md`（或粘贴其文本）。
3. 用 **Audio Overview** 生成播客式讲解，通勤时听；或用对话框就讲稿提问、生成学习指南。

> NotebookLM 没有面向个人的官方写入 API，所以这一步是手动上传；目前够用。

## 结构
- `profile.md` 学习者画像 · `curriculum.md` 大纲 · `progress.md` 进度
- `lessons/` 每日课件 · `.claude/skills/python-course/` skill 本体
