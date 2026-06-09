import csv

from exercises.ex5_filter_csv_by_score import filter_csv_by_score


def _write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(rows)


def test_filters_and_counts(tmp_path):
    src = tmp_path / "in.csv"
    out = tmp_path / "out.csv"
    _write_csv(src, [{"name": "a", "score": "90"}, {"name": "b", "score": "50"}, {"name": "c", "score": "70"}])
    assert filter_csv_by_score(src, out, 70) == 2


def test_output_content(tmp_path):
    src = tmp_path / "in.csv"
    out = tmp_path / "out.csv"
    _write_csv(src, [{"name": "a", "score": "90"}, {"name": "b", "score": "50"}])
    filter_csv_by_score(src, out, 60)
    with open(out, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows == [{"name": "a", "score": "90"}]


def test_none_kept(tmp_path):
    src = tmp_path / "in.csv"
    out = tmp_path / "out.csv"
    _write_csv(src, [{"name": "a", "score": "10"}])
    assert filter_csv_by_score(src, out, 50) == 0
