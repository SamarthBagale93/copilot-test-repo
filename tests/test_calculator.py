import pytest

from calculator import add, divide, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
