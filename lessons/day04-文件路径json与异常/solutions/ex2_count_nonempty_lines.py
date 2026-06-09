from pathlib import Path


def count_nonempty_lines(path: Path) -> int:
    """读取文本文件，返回非空行的数量。"""
    count = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                count += 1
    return count
