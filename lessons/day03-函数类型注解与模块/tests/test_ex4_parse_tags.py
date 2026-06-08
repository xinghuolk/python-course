import pytest

from exercises.ex4_parse_tags import parse_tags


def test_parses_and_normalizes_tags():
    assert parse_tags(" Python, web ,PYTHON") == ["python", "web"]


def test_allows_duplicates_when_unique_false():
    assert parse_tags("a, A, b", unique=False) == ["a", "a", "b"]


def test_can_disable_normalize():
    assert parse_tags("Py, py", normalize=False) == ["Py", "py"]


def test_drops_empty_tags():
    assert parse_tags("a,, ,b,") == ["a", "b"]


def test_options_are_keyword_only():
    with pytest.raises(TypeError):
        parse_tags("a,b", False)
