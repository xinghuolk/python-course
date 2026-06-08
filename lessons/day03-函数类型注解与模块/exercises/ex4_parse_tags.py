def parse_tags(
    raw: str,
    *,
    normalize: bool = True,
    unique: bool = True,
) -> list[str]:
    """把逗号分隔的标签字符串解析成列表。

    规则：
    - 用逗号分隔；
    - 每个标签去掉首尾空白；
    - 空标签丢弃；
    - normalize=True 时转小写；
    - unique=True 时保序去重。

    注意：normalize 和 unique 是 keyword-only 参数。
    """
    # TODO: 解析标签并根据开关处理
    raise NotImplementedError
