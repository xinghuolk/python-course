def parse_key_values(args: list[str]) -> dict[str, str]:
    """把形如 ["a=1", "b=2"] 的参数解析成 {"a": "1", "b": "2"}。

    没有 "=" 的项忽略；只按第一个 "=" 切分（值里可以再含 "="）。
    """
    # TODO: 解析 key=value 列表
    raise NotImplementedError
