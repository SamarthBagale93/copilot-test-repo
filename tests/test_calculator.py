from calculator import add, subtract


def test_subtract_returns_difference():
    assert subtract(7, 3) == 4
    assert subtract(3, 7) == -4


def test_add_remains_unchanged():
    assert add(7, 3) == 10
