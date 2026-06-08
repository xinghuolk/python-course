from exercises.ex6_unique_preserve_order import unique_preserve_order


def test_removes_duplicates_but_keeps_order():
    assert unique_preserve_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_empty_input():
    assert unique_preserve_order([]) == []


def test_case_sensitive():
    assert unique_preserve_order(["A", "a", "A"]) == ["A", "a"]


def test_does_not_modify_input():
    items = ["a", "a", "b"]
    unique_preserve_order(items)
    assert items == ["a", "a", "b"]
