from exercises.ex1_temperature import celsius_to_fahrenheit


def test_zero():
    assert celsius_to_fahrenheit(0) == 32.0


def test_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_negative():
    assert celsius_to_fahrenheit(-40) == -40.0
