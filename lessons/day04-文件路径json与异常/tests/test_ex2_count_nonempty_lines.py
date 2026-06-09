from exercises.ex2_count_nonempty_lines import count_nonempty_lines


def test_counts_nonempty(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hello\n\nworld\n   \nbye\n", encoding="utf-8")
    assert count_nonempty_lines(p) == 3


def test_empty_file(tmp_path):
    p = tmp_path / "e.txt"
    p.write_text("", encoding="utf-8")
    assert count_nonempty_lines(p) == 0


def test_all_blank(tmp_path):
    p = tmp_path / "b.txt"
    p.write_text("\n  \n\t\n", encoding="utf-8")
    assert count_nonempty_lines(p) == 0
