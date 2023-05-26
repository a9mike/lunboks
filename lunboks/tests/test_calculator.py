from lunboks import calculator


def test_calculate_percent():
    """Should return percent rounded to 2 decimal places"""
    result = calculator.calculate_percent(0.251, 4)

    assert result == 6.28


def test_calculate_percent_single_decimal():
    """Should return percent rounded to 1 decimal place"""
    result = calculator.calculate_percent(0.251, 4, 1)

    assert result == 6.3
