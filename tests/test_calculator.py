import pytest

from calculator import modulus


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 3, 1),
        (12, 4, 0),
        (-10, 3, 2),
    ],
)
def test_modulus(a, b, expected):
    assert modulus(a, b) == expected


def test_modulus_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        modulus(10, 0)
