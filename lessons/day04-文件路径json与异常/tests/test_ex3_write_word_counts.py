import json

from exercises.ex3_write_word_counts import write_word_counts


def test_returns_counts(tmp_path):
    result = write_word_counts("a b a c a", tmp_path / "w.json")
    assert result == {"a": 3, "b": 1, "c": 1}


def test_case_insensitive(tmp_path):
    result = write_word_counts("Hi hi HI", tmp_path / "w.json")
    assert result == {"hi": 3}


def test_writes_valid_json(tmp_path):
    p = tmp_path / "w.json"
    write_word_counts("x y x", p)
    loaded = json.loads(p.read_text(encoding="utf-8"))
    assert loaded == {"x": 2, "y": 1}


def test_empty_text(tmp_path):
    assert write_word_counts("", tmp_path / "w.json") == {}
