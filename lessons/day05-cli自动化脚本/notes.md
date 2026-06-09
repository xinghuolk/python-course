# Day 05 · 小型 CLI 自动化脚本

> 今天把前几天的零件组装成"能在命令行跑的小工具"。核心心法：**把纯逻辑和 I/O 分开**——逻辑函数好测，argparse/文件/子进程只做薄薄一层壳。

## 1. 脚本结构与 `if __name__ == "__main__"`
- 一个 `.py` 既能被直接运行，也能被别的文件 import。`__name__` 在直接运行时是 `"__main__"`，被 import 时是模块名。
- 习惯写法：把逻辑放进函数，最后用 `if __name__ == "__main__": main()` 作入口。
- 好处：import 这个文件做测试时不会顺带执行 main（对比 C 的 main 是唯一入口，Python 更灵活）。

## 2. 命令行参数：从 sys.argv 到 argparse
- 原始参数在 `sys.argv`（`sys.argv[0]` 是脚本名）。能用但麻烦。
- 用标准库 `argparse`：`parser.add_argument(...)` 声明参数，`parser.parse_args()` 解析。
- 位置参数 vs 可选参数（`--name`）；`type=int` 自动转换；`default=` 默认值；`action="store_true"` 做开关。
- argparse 自动生成 `--help` 和报错，省心。
- 测试技巧：`parser.parse_args(["a", "--limit", "5"])` 直接传列表，不依赖真实命令行。

## 3. 目录扫描与批处理
- 用 pathlib：`directory.iterdir()` 列当前层，`directory.glob("*.py")` 按模式找，`rglob` 递归。
- 典型批处理：遍历文件 → 判断 `p.is_file()` → 对每个做处理 → 汇总。
- `p.suffix`、`p.stat().st_size`（字节数）在统计时很有用。

## 4. 标准输入输出与退出码
- 正常结果打到 stdout（`print`）；错误/诊断打到 stderr（`print(..., file=sys.stderr)`）。
- 退出码：`sys.exit(0)` 成功，非 0 表示失败——这样脚本能被 shell 和其他程序判断成败（对比 C 的 return code）。
- 读管道输入用 `sys.stdin`。

## 5. subprocess：调用外部命令
- `subprocess.run([...], capture_output=True, text=True)` 运行外部命令。
- **参数用列表**（`["ls", "-l"]`），不要用 shell 字符串拼接——避免注入、更可控。
- `result.stdout` / `result.stderr` 是字符串（因为 text=True）；`result.returncode` 是退出码。
- 想让非 0 退出码直接抛异常，加 `check=True`。

## 6. 让脚本可测试
- 把"算什么"（纯函数：输入→输出）和"怎么拿输入/输出到哪"（argparse、读写文件、print）分开。
- 纯函数用 pytest 直接测；argparse 用 `parse_args([...])` 测；文件用 `tmp_path` 测。
- main() 只负责把它们串起来，逻辑尽量瘦。

## 7. 今日练习（7 题，难度递增）
1. `make_parser`：用 argparse 构造解析器（位置参数 + --limit + --verbose）。
2. `filter_lines`：grep 式行过滤。
3. `count_suffixes`：遍历目录统计后缀数量。
4. `format_table`：把 (name, count) 对齐成表格字符串。
5. `run_python_code`：用 subprocess 运行代码并取 stdout。
6. `parse_key_values`：解析 key=value 参数列表。
7. `summarize_directory`：扫描目录汇总文件数/字节数/后缀（小综合）。

预计耗时：讲解 25-35 分钟，练习 60-80 分钟。
