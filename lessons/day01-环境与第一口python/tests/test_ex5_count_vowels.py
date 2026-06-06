from exercises.ex5_count_vowels import count_vowels


def test_empty():
    assert count_vowels("") == 0


def test_no_vowels():
    assert count_vowels("xyz") == 0


def test_basic():
    assert count_vowels("Hello") == 2


def test_all_vowels_upper():
    assert count_vowels("AEIOU") == 5


def test_word():
    assert count_vowels("Programming") == 3
