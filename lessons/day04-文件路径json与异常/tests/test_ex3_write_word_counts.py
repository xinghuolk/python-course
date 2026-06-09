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


def test_chinese_not_escaped(tmp_path):
    p = tmp_path / "w.json"
    write_word_counts("你好 你好 世界", p)
    content = p.read_text(encoding="utf-8")
    assert "你好" in content       # ensure_ascii=False 才会保留中文字符
    assert "\\u" not in content    # 而不是转义成 你 这种
