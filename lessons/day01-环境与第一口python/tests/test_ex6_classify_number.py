from exercises.ex6_classify_number import classify_number


def test_negative():
    assert classify_number(-5) == "negative"


def test_zero():
    assert classify_number(0) == "zero"


def test_single():
    assert classify_number(7) == "single"


def test_single_boundary():
    assert classify_number(9) == "single"


def test_double():
    assert classify_number(42) == "double"


def test_double_boundary():
    assert classify_number(10) == "double"


def test_large():
    assert classify_number(100) == "large"
