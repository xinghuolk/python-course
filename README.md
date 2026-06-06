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
