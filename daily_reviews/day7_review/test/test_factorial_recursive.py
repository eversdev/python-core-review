from app.factorial_recursive import factor_recur


def test_factorial_zero_returns_one():
    assert factor_recur(0) == 1


def test_factorial_one_returns_one():
    pass


def test_factorial_float_raises_error():
    pass


def test_factorial_non_numeric_raises_error():
    pass
