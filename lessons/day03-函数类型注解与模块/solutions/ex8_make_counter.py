def make_counter(start: int = 0):
    """返回一个计数器函数，每次调用返回当前值再自增。"""
    count = start

    def counter() -> int:
        nonlocal count
        value = count
        count += 1
        return value

    return counter
