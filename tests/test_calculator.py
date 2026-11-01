from calculator import add, subtract


def test_add_remains_unchanged():
    assert add(7, 3) == 10


def test_subtracts_positive_numbers():
    assert subtract(7, 3) == 4


def test_subtracts_negative_numbers():
    assert subtract(-2, -5) == 3


def test_subtracts_to_negative_result():
    assert subtract(3, 7) == -4
