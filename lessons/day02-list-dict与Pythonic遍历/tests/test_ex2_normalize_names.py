from exercises.ex2_normalize_names import normalize_names


def test_normalizes_names():
    assert normalize_names([" Alice ", "BOB", "cHarLie"]) == ["alice", "bob", "charlie"]


def test_removes_empty_names():
    assert normalize_names(["  ", "", "\t", "Dana"]) == ["dana"]


def test_collapses_inner_whitespace():
    assert normalize_names(["  Alice   Smith ", "BOB\tLEE"]) == ["alice smith", "bob lee"]


def test_empty_input():
    assert normalize_names([]) == []
