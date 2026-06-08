from exercises.ex3_safe_average import safe_average


def test_average_numbers():
    assert safe_average([1, 2, 3, 4]) == 2.5


def test_empty_returns_none():
    assert safe_average([]) is None


def test_handles_negative_numbers():
    assert safe_average([-2, 2]) == 0


def test_does_not_modify_input():
    numbers = [1, 2, 3]
    safe_average(numbers)
    assert numbers == [1, 2, 3]
