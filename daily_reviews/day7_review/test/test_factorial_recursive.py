from app.factorial_recursive import factor_recur

import pytest


def test_factorial_zero_returns_one():
    assert factor_recur(0) == 1


def test_factorial_one_returns_one():
    assert factor_recur(1) == 1


def test_factorial_float_raises_error():
    with pytest.raises(ValueError):
        factor_recur(1.5)


def test_factorial_recursive_case():
    assert factor_recur(5) == 120


def test_factorial_negative_value():
    with pytest.raises(ValueError):
        factor_recur(-1)


def test_factorial_non_numeric_raises_error():
    with pytest.raises(ValueError):
        factor_recur("Three")
