from pathlib import Path


def summarize_log_levels(path: Path) -> dict[str, int]:
    """读取日志文件，统计每个级别出现次数。

    每行形如 "INFO: started" / "ERROR: boom"。级别是冒号前的第一个词。
    只统计级别属于 {"INFO", "WARNING", "ERROR"} 的行，其他行忽略。
    返回如 {"INFO": 2, "ERROR": 1}（出现过的级别才在 dict 里）。文件不存在时返回 {}。
    """
    # TODO: 读文件按级别计数，处理 FileNotFoundError
    raise NotImplementedError
