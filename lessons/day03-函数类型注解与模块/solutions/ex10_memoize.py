import functools


def memoize(func):
    """装饰器：缓存相同位置参数的调用结果。"""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper
