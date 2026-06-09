from exercises.ex8_make_counter import make_counter


def test_counts_from_zero():
    c = make_counter()
    assert c() == 0
    assert c() == 1
    assert c() == 2


def test_custom_start():
    c = make_counter(10)
    assert c() == 10
    assert c() == 11


def test_counters_are_independent():
    a = make_counter()
    b = make_counter()
    assert a() == 0
    assert a() == 1
    assert b() == 0
