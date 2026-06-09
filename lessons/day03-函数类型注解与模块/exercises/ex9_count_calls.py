def count_calls(func):
    """装饰器：记录被装饰函数被调用了多少次，存到 wrapper.calls。

    @count_calls
    def greet(name): ...
    调用 3 次后 greet.calls == 3，且返回值原样透传。
    必须用 functools.wraps 保留原函数的 __name__ 和 __doc__。
    """
    # TODO: 实现装饰器，记得 functools.wraps
    raise NotImplementedError
