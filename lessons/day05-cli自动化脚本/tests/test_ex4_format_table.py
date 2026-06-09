from exercises.ex4_format_table import format_table


def test_aligns():
    assert format_table([("a", 1), ("bb", 22)]) == "a : 1\nbb: 22"


def test_single_row():
    assert format_table([("x", 5)]) == "x: 5"


def test_empty():
    assert format_table([]) == ""
