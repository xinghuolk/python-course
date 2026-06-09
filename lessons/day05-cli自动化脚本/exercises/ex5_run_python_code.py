def run_python_code(code: str) -> str:
    """用子进程运行一段 Python 代码，返回它打印到 stdout 的内容（去掉首尾空白）。

    用 subprocess.run，参数用列表形式 [sys.executable, "-c", code]（不要用 shell 字符串），
    并设 capture_output=True, text=True。
    """
    # TODO: 用 subprocess.run 运行
    raise NotImplementedError
