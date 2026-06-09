# Day 04 · 文件、路径、JSON/CSV 与异常

> 今天学怎么和"外部世界"打交道：读写文件、处理路径、解析 JSON/CSV、优雅地处理出错。这是自动化脚本和数据管线的地基。

## 1. pathlib：用对象表示路径
- 别再用字符串拼路径。用 `from pathlib import Path`。
- `Path("data") / "a.txt"` 用 `/` 拼接，跨平台安全（对比 C/JS 手动拼 `/` 或 `\`）。
- 常用属性：`.name`、`.stem`、`.suffix`、`.parent`；判断 `.exists()`、`.is_file()`。
- 便捷读写：`p.read_text(encoding="utf-8")`、`p.write_text(s, encoding="utf-8")`。
- 找文件：`p.glob("*.py")` 返回匹配的路径。

## 2. 文件读写与上下文管理器
- 标准开法：`with open(path, encoding="utf-8") as f:`。`with` 块结束自动关文件，哪怕中途异常（对比 C 要手动 fclose，忘了就泄漏）。
- 文本文件可直接 `for line in f:` 逐行迭代，省内存。
- 写文件用 `open(path, "w", ...)`，追加用 `"a"`。
- 永远显式写 `encoding="utf-8"`，避免平台默认编码坑（尤其中文）。
- 上下文管理器是通用机制：任何 `with ... as ...` 都保证"进入/退出"成对。

## 3. 异常处理
- `try / except / else / finally`：try 放可能出错的代码，except 抓特定异常类型。
- **抓具体异常**，别用裸 `except:`：`except ValueError:`、`except FileNotFoundError:`。
- 主动抛：`raise ValueError("说明")`；链式 `raise ... from exc` 保留原因。
- Python 风格 **EAFP**（先做，错了再处理）优于 C/JS 常见的 **LBYL**（先一堆 if 检查）。例：直接 `int(s)` 配 `except`，而不是先验证。
- `else`：try 没出错才执行；`finally`：无论如何都执行（清理）。

## 4. JSON
- `import json`。字符串 ↔ 对象：`json.loads(s)` / `json.dumps(obj)`。
- 文件 ↔ 对象：`json.load(f)` / `json.dump(obj, f)`。
- 中文别被转义：`json.dumps(obj, ensure_ascii=False)`；好看缩进：`indent=2`。
- dict/list/str/int/float/bool/None 直接对应 JSON；其他类型要先转换。

## 5. CSV
- `import csv`。**打开 CSV 文件时加 `newline=""`**（避免 Windows 多空行）。
- 推荐按字典读写：`csv.DictReader(f)` 每行是 dict；`csv.DictWriter(f, fieldnames=[...])` 配 `writeheader()` + `writerows()`。
- CSV 里所有值都是字符串，数字要自己 `int()`/`float()`。

## 6. logging 入门
- 比 `print` 调试更专业：能分级别、带时间、可开关。
- 起步：`import logging; logging.basicConfig(level=logging.INFO)`，然后 `logging.info(...)` / `warning` / `error`。
- 大项目里用 `logger = logging.getLogger(__name__)`，每个模块一个 logger。
- 经验：临时排查可以 print，但要留在代码里的诊断信息用 logging。

## 7. 今日练习（7 题，难度递增）
1. `safe_parse_int`：try/except 处理 ValueError。
2. `count_nonempty_lines`：with open 逐行读、统计非空行。
3. `write_word_counts`：词频 dict 写成 JSON（ensure_ascii=False）。
4. `load_config`：读 JSON，缺文件返回 {}，坏 JSON 抛 ValueError。
5. `filter_csv_by_score`：DictReader/DictWriter 过滤 CSV。
6. `list_files_by_suffix`：pathlib glob 找文件。
7. `summarize_log_levels`：读日志，按级别计数（小综合）。

预计耗时：讲解 25-35 分钟，练习 60-80 分钟。
