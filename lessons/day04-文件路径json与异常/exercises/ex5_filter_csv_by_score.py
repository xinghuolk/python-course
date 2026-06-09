from pathlib import Path


def filter_csv_by_score(in_path: Path, out_path: Path, min_score: int) -> int:
    """读入含表头 name,score 的 CSV，保留 score >= min_score 的行，写到 out_path
    （保留同样的表头）。返回保留的行数。

    用 csv.DictReader / csv.DictWriter；打开文件时加 newline=""。score 是字符串，需 int()。
    """
    # TODO: 用 csv 模块过滤
    raise NotImplementedError
