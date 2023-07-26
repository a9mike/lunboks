import typing


def calculate_percent(
    numerator: typing.Union[float, int],
    denominator: typing.Union[float, int],
    decimals: int = 2,
) -> float:
    """Calculates percentage rounded to `decimals` decimal places"""
    return round(numerator * 100 / denominator, decimals)
