from exercises.ex2_build_user_profile import build_user_profile


def test_builds_basic_profile():
    assert build_user_profile(" Alice ") == {"name": "Alice", "email": None}


def test_normalizes_email():
    assert build_user_profile("Bob", " BOB@Example.COM ") == {
        "name": "Bob",
        "email": "bob@example.com",
    }


def test_merges_extra_fields():
    assert build_user_profile("Chen", role="admin", active=True) == {
        "name": "Chen",
        "email": None,
        "role": "admin",
        "active": True,
    }


def test_ignores_none_extra_fields():
    assert build_user_profile("Dana", city=None, role="user") == {
        "name": "Dana",
        "email": None,
        "role": "user",
    }
