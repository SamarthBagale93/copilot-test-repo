from calculator import power


def test_power_with_positive_exponent():
    assert power(2, 3) == 8


def test_power_with_zero_exponent():
    assert power(5, 0) == 1


def test_power_with_negative_exponent():
    assert power(2, -2) == 0.25


def test_power_with_fractional_exponent():
    assert power(9, 0.5) == 3
