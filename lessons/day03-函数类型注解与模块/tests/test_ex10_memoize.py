from exercises.ex10_memoize import memoize


def test_caches_result():
    calls = []

    @memoize
    def square(n):
        calls.append(n)
        return n * n

    assert square(4) == 16
    assert square(4) == 16
    assert calls == [4]


def test_different_args_computed_separately():
    calls = []

    @memoize
    def square(n):
        calls.append(n)
        return n * n

    assert square(2) == 4
    assert square(3) == 9
    assert calls == [2, 3]


def test_preserves_metadata():
    @memoize
    def compute(n):
        """计算。"""
        return n

    assert compute.__name__ == "compute"
    assert compute.__doc__ == "计算。"
