def classify_number(n: int) -> str:
    """按区间给整数分类。"""
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    if 1 <= n <= 9:
        return "single"
    if 10 <= n <= 99:
        return "double"
    return "large"
