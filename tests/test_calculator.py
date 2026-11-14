import pytest

from calculator import power


@pytest.mark.parametrize(
    ("base", "exponent", "expected"),
    [
        (2, 3, 8),
        (5, 0, 1),
        (2, -2, 0.25),
        (2.5, 2, 6.25),
    ],
)
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected
