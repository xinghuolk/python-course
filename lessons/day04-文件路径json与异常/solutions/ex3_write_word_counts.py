import json
from pathlib import Path


def write_word_counts(text: str, path: Path) -> dict[str, int]:
    """统计词频并写成 JSON。"""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(counts, f, ensure_ascii=False, indent=2)
    return counts
