from exercises.ex6_parse_key_values import parse_key_values


def test_basic():
    assert parse_key_values(["a=1", "b=2"]) == {"a": "1", "b": "2"}


def test_ignores_no_equals():
    assert parse_key_values(["a=1", "nope", "b=2"]) == {"a": "1", "b": "2"}


def test_value_with_equals():
    assert parse_key_values(["url=http://x?a=1"]) == {"url": "http://x?a=1"}
