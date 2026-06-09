from exercises.ex7_summarize_directory import summarize_directory


def test_summarizes(tmp_path):
    (tmp_path / "a.py").write_text("hello", encoding="utf-8")   # 5 bytes
    (tmp_path / "b.py").write_text("hi", encoding="utf-8")      # 2 bytes
    (tmp_path / "c.txt").write_text("xyz", encoding="utf-8")    # 3 bytes
    result = summarize_directory(tmp_path)
    assert result == {"file_count": 3, "total_bytes": 10, "by_suffix": {".py": 2, ".txt": 1}}


def test_skips_subdir(tmp_path):
    (tmp_path / "a.py").write_text("hi", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    result = summarize_directory(tmp_path)
    assert result["file_count"] == 1
    assert result["total_bytes"] == 2          # 子目录不计入字节数
    assert result["by_suffix"] == {".py": 1}   # 也不计入后缀统计


def test_empty(tmp_path):
    assert summarize_directory(tmp_path) == {"file_count": 0, "total_bytes": 0, "by_suffix": {}}
