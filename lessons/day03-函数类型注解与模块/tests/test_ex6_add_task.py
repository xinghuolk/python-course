from exercises.ex6_add_task import add_task


def test_adds_task_to_empty_list_when_none():
    assert add_task("write tests") == ["write tests"]


def test_default_list_is_not_shared_between_calls():
    assert add_task("read") == ["read"]
    assert add_task("write") == ["write"]


def test_returns_new_list_without_mutating_input():
    tasks = ["read"]
    result = add_task("practice", tasks=tasks)
    assert result == ["read", "practice"]
    assert tasks == ["read"]


def test_strips_task():
    assert add_task("  review  ", tasks=[]) == ["review"]


def test_ignores_empty_task():
    assert add_task("   ", tasks=["read"]) == ["read"]
