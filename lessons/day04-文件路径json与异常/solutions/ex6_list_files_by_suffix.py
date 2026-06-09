from pathlib import Path


def list_files_by_suffix(directory: Path, suffix: str) -> list[str]:
    """返回目录下指定后缀文件名，排序。"""
    return sorted(p.name for p in directory.glob(f"*{suffix}") if p.is_file())
