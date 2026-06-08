import exercises.ex7_summarize_people as people

from exercises.ex7_summarize_people import count_by_field, extract_names, summarize_people


def sample_records():
    return [
        {"name": "Chen", "city": "Shanghai", "role": "admin"},
        {"name": "Alice", "city": "Beijing", "role": "user"},
        {"name": "Bob", "city": "Shanghai", "role": "user"},
        {"name": 123, "city": "Beijing", "role": None},
    ]


def test_extract_names_ignores_invalid_names():
    assert extract_names(sample_records()) == ["Chen", "Alice", "Bob"]


def test_count_by_field_counts_string_values():
    assert count_by_field(sample_records(), "city") == {"Shanghai": 2, "Beijing": 2}


def test_summarize_people():
    assert summarize_people(sample_records()) == {
        "count": 3,
        "names": ["Alice", "Bob", "Chen"],
        "cities": {"Shanghai": 2, "Beijing": 2},
        "roles": {"admin": 1, "user": 2},
    }


def test_empty_records():
    assert summarize_people([]) == {"count": 0, "names": [], "cities": {}, "roles": {}}


def test_summarize_people_uses_helper_functions(monkeypatch):
    calls: list[tuple[str, str | None]] = []

    def fake_extract_names(records):
        calls.append(("extract_names", None))
        return ["Bob", "Alice"]

    def fake_count_by_field(records, field):
        calls.append(("count_by_field", field))
        return {field: 1}

    monkeypatch.setattr(people, "extract_names", fake_extract_names)
    monkeypatch.setattr(people, "count_by_field", fake_count_by_field)

    assert people.summarize_people([{"name": "ignored"}]) == {
        "count": 2,
        "names": ["Alice", "Bob"],
        "cities": {"city": 1},
        "roles": {"role": 1},
    }
    assert calls == [
        ("extract_names", None),
        ("count_by_field", "city"),
        ("count_by_field", "role"),
    ]
