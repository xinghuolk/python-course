def merge_scores(names: list[str], scores: list[int]) -> dict[str, int]:
    """把名字和分数合并成 dict。

    使用 zip(names, scores) 并行遍历。
    如果长度不一致，zip 会自动以较短列表为准。
    如果名字重复，后面的分数覆盖前面的分数。
    """
    # TODO: 用 zip 构造 dict
    raise NotImplementedError
