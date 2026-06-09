from exercises.ex3_count_suffixes import count_suffixes


def test_counts(tmp_path):
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "b.py").write_text("", encoding="utf-8")
    (tmp_path / "c.txt").write_text("", encoding="utf-8")
    assert count_suffixes(tmp_path) == {".py": 2, ".txt": 1}


def test_skips_subdir(tmp_path):
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    assert count_suffixes(tmp_path) == {".py": 1}


def test_empty(tmp_path):
    assert count_suffixes(tmp_path) == {}
