from pathlib import Path


def summarize_directory(directory: Path) -> dict:
    """扫描 directory 当前层的文件，返回汇总：

    {"file_count": 文件数, "total_bytes": 总字节数, "by_suffix": {后缀: 数量}}
    只统计文件（跳过子目录），不递归。字节数用 p.stat().st_size。
    """
    # TODO: 综合统计目录
    raise NotImplementedError
