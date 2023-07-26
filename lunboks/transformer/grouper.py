"""Wrappers for aggregate groupby functions"""
import pandas as pd


def as_list(group_var: str | list[str]) -> list[str]:
    group_vars = group_var
    if isinstance(group_var, str):
        group_vars = [group_var]
    return group_vars


def group_mean(
    df: pd.DataFrame, group_var: str | list[str], target: str
) -> pd.DataFrame:
    """
    Returns a DataFrame with counts of values in target by `group_var` column.
    """
    group_vars = as_list(group_var)
    return (
        df[group_vars + [target]]
        .groupby(group_vars)
        .mean(numeric_only=True)
        .sort_values(target, ascending=False)
        .reset_index()
        .rename(columns={target: "mean"})
    )


def group_count(
    df: pd.DataFrame, group_var: str | list[str], target: str
) -> pd.DataFrame:
    """
    Returns a DataFrame with counts of values in target by `group_var` column.
    """
    group_vars = as_list(group_var)
    return (
        df[group_vars + [target]]
        .groupby(group_vars)
        .count()
        .sort_values(target, ascending=False)
        .reset_index()
        .rename(columns={target: "count"})
    )


def group_sum(
    df: pd.DataFrame, group_var: str | list[str], target: str
) -> pd.DataFrame:
    """Returns a DataFrame with sum of values in target by group_var."""
    group_vars = as_list(group_var)
    return (
        df[group_vars + [target]]
        .groupby(group_vars)
        .sum(numeric_only=True)
        .sort_values(target, ascending=False)
        .reset_index()
        .rename(columns={target: "sum"})
    )


def group_nunique(
    df: pd.DataFrame, group_var: str | list[str], target: str
) -> pd.DataFrame:
    """
    Returns a DataFrame with number of unique values in target by `group_var`
    """
    group_vars = as_list(group_var)
    return (
        df[group_vars + [target]]
        .groupby(group_vars)
        .nunique()
        .sort_values(target, ascending=False)
        .reset_index()
        .rename(columns={target: "n_unique"})
    )
