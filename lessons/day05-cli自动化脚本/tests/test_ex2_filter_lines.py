from exercises.ex2_filter_lines import filter_lines


def test_filters():
    assert filter_lines(["apple", "banana", "grape"], "ap") == ["apple", "grape"]


def test_empty_keyword_returns_all():
    lines = ["a", "b"]
    assert filter_lines(lines, "") == ["a", "b"]


def test_no_match():
    assert filter_lines(["a", "b"], "z") == []
