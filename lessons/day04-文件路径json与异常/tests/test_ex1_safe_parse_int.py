from exercises.ex1_safe_parse_int import safe_parse_int


def test_valid():
    assert safe_parse_int("42") == 42


def test_invalid_returns_default():
    assert safe_parse_int("abc") == 0


def test_custom_default():
    assert safe_parse_int("x", -1) == -1


def test_whitespace():
    assert safe_parse_int("  10  ") == 10


def test_negative():
    assert safe_parse_int("-7") == -7
