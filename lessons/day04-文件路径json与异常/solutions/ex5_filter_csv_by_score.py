import csv
from pathlib import Path


def filter_csv_by_score(in_path: Path, out_path: Path, min_score: int) -> int:
    """过滤 CSV 中分数达标的行。"""
    kept = []
    with open(in_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["score"]) >= min_score:
                kept.append(row)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(kept)
    return len(kept)
