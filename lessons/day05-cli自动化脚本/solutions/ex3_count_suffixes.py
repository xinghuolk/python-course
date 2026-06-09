from pathlib import Path


def count_suffixes(directory: Path) -> dict[str, int]:
    """统计目录当前层文件后缀数量。"""
    counts: dict[str, int] = {}
    for p in directory.iterdir():
        if p.is_file():
            counts[p.suffix] = counts.get(p.suffix, 0) + 1
    return counts
