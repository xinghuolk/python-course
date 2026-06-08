import inspect

from exercises.ex5_format_report import format_report


def test_title_only():
    assert format_report(" Daily ") == "Daily"


def test_formats_numbered_lines():
    assert format_report("Daily", " done ", "next") == "Daily\n1. done\n2. next"


def test_drops_empty_lines():
    assert format_report("Daily", "", "  ", "ship") == "Daily\n1. ship"


def test_uppercase_title():
    assert format_report("Daily", "ship", uppercase_title=True) == "DAILY\n1. ship"


def test_uppercase_title_is_keyword_only():
    signature = inspect.signature(format_report)
    assert signature.parameters["uppercase_title"].kind is inspect.Parameter.KEYWORD_ONLY
