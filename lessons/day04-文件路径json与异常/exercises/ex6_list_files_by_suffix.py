from pathlib import Path


def list_files_by_suffix(directory: Path, suffix: str) -> list[str]:
    """返回 directory 下所有指定后缀文件的文件名（不含路径），按字母排序。

    suffix 形如 ".py"。用 pathlib 的 glob，不要手动拼路径字符串。只看当前层，不递归。
    """
    # TODO: 用 directory.glob 实现
    raise NotImplementedError
