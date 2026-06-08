from exercises.ex4_merge_scores import merge_scores


def test_merges_names_and_scores():
    assert merge_scores(["alice", "bob"], [90, 82]) == {"alice": 90, "bob": 82}


def test_zip_uses_shorter_length():
    assert merge_scores(["alice", "bob", "chen"], [90, 82]) == {"alice": 90, "bob": 82}


def test_duplicate_name_uses_last_score():
    assert merge_scores(["alice", "bob", "alice"], [70, 80, 95]) == {"alice": 95, "bob": 80}


def test_empty_input():
    assert merge_scores([], []) == {}
