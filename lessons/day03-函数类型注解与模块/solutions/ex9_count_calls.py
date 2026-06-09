import functools


def count_calls(func):
    """装饰器：记录函数被调用次数到 wrapper.calls。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
