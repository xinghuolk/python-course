from exercises.ex7_summarize_log_levels import summarize_log_levels


def test_counts_levels(tmp_path):
    p = tmp_path / "log.txt"
    p.write_text("INFO: a\nERROR: b\nINFO: c\nDEBUG: d\n", encoding="utf-8")
    assert summarize_log_levels(p) == {"INFO": 2, "ERROR": 1}


def test_ignores_unknown(tmp_path):
    p = tmp_path / "log.txt"
    p.write_text("TRACE: x\nrandom line\n", encoding="utf-8")
    assert summarize_log_levels(p) == {}


def test_missing_file(tmp_path):
    assert summarize_log_levels(tmp_path / "nope.txt") == {}


def test_all_levels(tmp_path):
    p = tmp_path / "log.txt"
    p.write_text("INFO: a\nWARNING: b\nERROR: c\nWARNING: d\n", encoding="utf-8")
    assert summarize_log_levels(p) == {"INFO": 1, "WARNING": 2, "ERROR": 1}
