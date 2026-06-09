from pathlib import Path


def count_suffixes(directory: Path) -> dict[str, int]:
    """统计 directory 当前层各文件后缀的数量，返回如 {".py": 2, ".txt": 1}。

    无后缀的文件后缀算 ""。只统计文件（跳过子目录），不递归。用 directory.iterdir()。
    """
    # TODO: 遍历目录统计后缀
    raise NotImplementedError
