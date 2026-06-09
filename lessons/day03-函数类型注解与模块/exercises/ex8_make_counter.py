def make_counter(start: int = 0):
    """返回一个计数器函数：每次调用返回当前值，然后自增 1。

    c = make_counter(); c() -> 0; c() -> 1; c() -> 2
    c = make_counter(10); c() -> 10; c() -> 11
    两个独立的 counter 不共享状态。
    提示：闭包捕获外层 start；内层要修改它需要 nonlocal。
    """
    # TODO: 用闭包 + nonlocal 实现
    raise NotImplementedError
