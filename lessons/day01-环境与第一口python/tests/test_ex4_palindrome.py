from exercises.ex4_palindrome import is_palindrome


def test_empty():
    assert is_palindrome("") is True


def test_single():
    assert is_palindrome("a") is True


def test_simple_true():
    assert is_palindrome("abba") is True


def test_simple_false():
    assert is_palindrome("abc") is False


def test_mixed_case():
    assert is_palindrome("RaceCar") is True


def test_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
