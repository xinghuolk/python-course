def safe_parse_int(s: str, default: int = 0) -> int:
    """把字符串解析成 int，失败时返回 default。"""
    try:
        return int(s)
    except ValueError:
        return default
