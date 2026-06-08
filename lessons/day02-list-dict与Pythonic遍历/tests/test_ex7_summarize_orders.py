from exercises.ex7_summarize_orders import summarize_orders


def test_summarizes_orders():
    orders = [
        {"customer": "alice", "amount": 12.5},
        {"customer": "bob", "amount": 8},
        {"customer": "alice", "amount": 7.5},
    ]
    assert summarize_orders(orders) == {
        "count": 3,
        "total": 28.0,
        "by_customer": {"alice": 20.0, "bob": 8.0},
    }


def test_empty_orders():
    assert summarize_orders([]) == {"count": 0, "total": 0.0, "by_customer": {}}


def test_ignores_invalid_orders():
    orders = [
        {"customer": "alice", "amount": 10},
        {"customer": "bob"},
        {"amount": 5},
        {"customer": "chen", "amount": "9"},
    ]
    assert summarize_orders(orders) == {
        "count": 1,
        "total": 10.0,
        "by_customer": {"alice": 10.0},
    }
