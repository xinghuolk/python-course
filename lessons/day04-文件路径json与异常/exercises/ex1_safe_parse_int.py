def safe_parse_int(s: str, default: int = 0) -> int:
    """把字符串解析成 int，失败时返回 default。

    "42" -> 42；"abc" -> default；" 10 " -> 10（int 能处理首尾空白）。
    用 try/except 捕获 ValueError（EAFP：先做，错了再处理）。
    """
    # TODO: 用 try/except 实现
    raise NotImplementedError
