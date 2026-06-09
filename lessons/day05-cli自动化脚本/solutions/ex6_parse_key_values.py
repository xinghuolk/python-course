def parse_key_values(args: list[str]) -> dict[str, str]:
    """解析 key=value 形式的参数列表。"""
    result: dict[str, str] = {}
    for item in args:
        if "=" in item:
            key, value = item.split("=", 1)
            result[key] = value
    return result
