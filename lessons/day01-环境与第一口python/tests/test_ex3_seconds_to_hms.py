from exercises.ex3_seconds_to_hms import seconds_to_hms


def test_zero():
    assert seconds_to_hms(0) == "0:00:00"


def test_minute_and_second():
    assert seconds_to_hms(61) == "0:01:01"


def test_full():
    assert seconds_to_hms(3661) == "1:01:01"


def test_exact_hour():
    assert seconds_to_hms(3600) == "1:00:00"


def test_max():
    assert seconds_to_hms(86399) == "23:59:59"
