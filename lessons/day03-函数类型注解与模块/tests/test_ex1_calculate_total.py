from exercises.ex1_calculate_total import calculate_total


def test_calculates_total_without_options():
    assert calculate_total([10, 20, 5]) == 35.0


def test_applies_discount_before_tax():
    assert calculate_total([100], tax_rate=0.1, discount=0.2) == 88.0


def test_rounds_to_two_decimals():
    assert calculate_total([0.1, 0.2], tax_rate=0.1) == 0.33


def test_empty_prices():
    assert calculate_total([]) == 0.0
