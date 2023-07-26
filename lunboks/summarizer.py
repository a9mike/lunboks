import pandas as pd


def format_params(fit) -> pd.DataFrame:
    """
    Return regression results in a formatted DataFrame, showing predictor
    name, coefficients, and confidence intervals.

    :param fit:
        params from statsmodels regression .fit() output
    :return:
        DataFrame with coefficients and confidence intervals
    """
    formatted_params = pd.concat(
        [pd.DataFrame(fit.params), fit.conf_int()], axis=1
    ).reset_index()
    formatted_params.columns = ["name", "coef", "lower_ci", "upper_ci"]

    return formatted_params
