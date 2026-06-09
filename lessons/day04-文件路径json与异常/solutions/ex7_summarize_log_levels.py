from pathlib import Path


def summarize_log_levels(path: Path) -> dict[str, int]:
    """按日志级别统计行数。"""
    levels = {"INFO", "WARNING", "ERROR"}
    counts: dict[str, int] = {}
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                level = line.split(":", 1)[0].strip()
                if level in levels:
                    counts[level] = counts.get(level, 0) + 1
    except FileNotFoundError:
        return {}
    return counts
