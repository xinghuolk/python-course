from exercises.ex5_run_python_code import run_python_code


def test_runs():
    assert run_python_code("print(1 + 1)") == "2"


def test_multiline_output():
    assert run_python_code("print('a'); print('b')") == "a\nb"
