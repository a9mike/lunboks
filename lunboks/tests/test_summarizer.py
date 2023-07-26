import pandas as pd
from pandas import testing

from lunboks import summarizer

_INDEX = ["intercept", "agreeableness"]


class Fit:
    """Mock statsmodel regression output"""

    params = pd.Series([2.05, 1.50], index=_INDEX)

    def conf_int(self):
        """Confidence intervals"""
        return pd.DataFrame({"0": [2.03, 1.47], "1": [2.07, 1.53]}, index=_INDEX)


def test_format_params():
    """
    Should return a DataFrame with name of variable, coefficients, and confidence
    intervals
    """
    result = summarizer.format_params(Fit())
    expected = pd.DataFrame(
        {
            "name": _INDEX,
            "coef": [2.05, 1.50],
            "lower_ci": [2.03, 1.47],
            "upper_ci": [2.07, 1.53],
        }
    )

    testing.assert_frame_equal(result, expected)
