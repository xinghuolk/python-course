from exercises.ex1_make_parser import make_parser


def test_defaults():
    args = make_parser().parse_args(["data"])
    assert args.path == "data"
    assert args.limit == 10
    assert args.verbose is False


def test_options():
    args = make_parser().parse_args(["data", "--limit", "5", "--verbose"])
    assert args.limit == 5
    assert args.verbose is True
