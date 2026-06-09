from pathlib import Path


def count_nonempty_lines(path: Path) -> int:
    """读取文本文件，返回非空行的数量（去掉首尾空白后为空的行不算）。

    用 with open(...) 打开，加 encoding="utf-8"；逐行迭代。
    """
    # TODO: 用 with open 逐行统计
    raise NotImplementedError
