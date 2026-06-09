import subprocess
import sys


def run_python_code(code: str) -> str:
    """用子进程运行 Python 代码，返回 stdout。"""
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
