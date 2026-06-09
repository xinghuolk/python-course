from exercises.ex9_count_calls import count_calls


def test_counts_calls():
    @count_calls
    def greet(name):
        return f"hi {name}"

    greet("a")
    greet("b")
    greet("c")
    assert greet.calls == 3


def test_return_value_passes_through():
    @count_calls
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_preserves_metadata():
    @count_calls
    def original():
        """原始文档。"""
        return 1

    assert original.__name__ == "original"
    assert original.__doc__ == "原始文档。"
