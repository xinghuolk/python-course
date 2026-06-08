from exercises.ex5_top_students import top_students


def test_returns_names_above_threshold_in_order():
    records = [
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 81},
        {"name": "Chen", "score": 95},
    ]
    assert top_students(records, 90) == ["Alice", "Chen"]


def test_threshold_is_inclusive():
    assert top_students([{"name": "Alice", "score": 90}], 90) == ["Alice"]


def test_ignores_missing_fields():
    records = [{"name": "Alice"}, {"score": 99}, {"name": "Bob", "score": 88}]
    assert top_students(records, 80) == ["Bob"]


def test_empty_records():
    assert top_students([], 60) == []
