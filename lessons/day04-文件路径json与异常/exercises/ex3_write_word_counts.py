from pathlib import Path


def write_word_counts(text: str, path: Path) -> dict[str, int]:
    """统计 text 中每个单词出现次数（按空白切分，统一转小写），
    把结果以 JSON 写到 path（中文可读：ensure_ascii=False；缩进 indent=2），并返回该字典。
    """
    # TODO: 统计词频，写 JSON，返回字典
    raise NotImplementedError
