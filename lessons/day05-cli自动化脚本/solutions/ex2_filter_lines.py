def filter_lines(lines: list[str], keyword: str) -> list[str]:
    """类似 grep 的行过滤。"""
    if not keyword:
        return list(lines)
    return [line for line in lines if keyword in line]
