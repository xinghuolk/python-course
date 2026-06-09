from pathlib import Path


def summarize_directory(directory: Path) -> dict:
    """汇总目录当前层文件信息。"""
    file_count = 0
    total_bytes = 0
    by_suffix: dict[str, int] = {}
    for p in directory.iterdir():
        if p.is_file():
            file_count += 1
            total_bytes += p.stat().st_size
            by_suffix[p.suffix] = by_suffix.get(p.suffix, 0) + 1
    return {"file_count": file_count, "total_bytes": total_bytes, "by_suffix": by_suffix}
