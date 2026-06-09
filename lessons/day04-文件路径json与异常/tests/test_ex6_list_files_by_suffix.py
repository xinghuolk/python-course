from exercises.ex6_list_files_by_suffix import list_files_by_suffix


def test_lists_sorted(tmp_path):
    (tmp_path / "b.py").write_text("", encoding="utf-8")
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "c.txt").write_text("", encoding="utf-8")
    assert list_files_by_suffix(tmp_path, ".py") == ["a.py", "b.py"]


def test_empty(tmp_path):
    assert list_files_by_suffix(tmp_path, ".py") == []


def test_other_suffix(tmp_path):
    (tmp_path / "note.md").write_text("", encoding="utf-8")
    assert list_files_by_suffix(tmp_path, ".md") == ["note.md"]


def test_ignores_directories(tmp_path):
    (tmp_path / "real.py").write_text("", encoding="utf-8")
    (tmp_path / "fake.py").mkdir()  # 后缀像 .py 但是目录，应被排除
    assert list_files_by_suffix(tmp_path, ".py") == ["real.py"]
