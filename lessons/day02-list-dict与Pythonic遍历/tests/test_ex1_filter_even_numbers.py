from exercises.ex1_filter_even_numbers import filter_even_numbers


def test_filters_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_keeps_zero_and_negative_even_numbers():
    assert filter_even_numbers([0, -3, -2, 7, 8]) == [0, -2, 8]


def test_empty_list():
    assert filter_even_numbers([]) == []


def test_does_not_modify_input():
    numbers = [1, 2, 3]
    filter_even_numbers(numbers)
    assert numbers == [1, 2, 3]
