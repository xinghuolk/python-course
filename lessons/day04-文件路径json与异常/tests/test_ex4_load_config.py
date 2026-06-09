import pytest

from exercises.ex4_load_config import load_config


def test_reads_config(tmp_path):
    p = tmp_path / "c.json"
    p.write_text('{"name": "x", "n": 3}', encoding="utf-8")
    assert load_config(p) == {"name": "x", "n": 3}


def test_missing_returns_empty(tmp_path):
    assert load_config(tmp_path / "nope.json") == {}


def test_invalid_raises(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{not json", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid config"):
        load_config(p)
