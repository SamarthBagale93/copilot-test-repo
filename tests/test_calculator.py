from calculator import subtract


def test_subtracts_numbers():
    assert subtract(7, 3) == 4
    assert subtract(3, 7) == -4


def test_subtracts_negative_numbers():
    assert subtract(-2, -5) == 3
