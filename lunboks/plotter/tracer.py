"""Module to create line/bar traces for single or multiple groups"""
import typing
from functools import partial

import pandas as pd
import plotly.graph_objs as go


def create_trace(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color: str,
    trace_name: str,
    mode: str = "line",
    **kwargs,
) -> go.Trace:
    """
    Creates a trace for a plot given x and y. Default is a line plot, but a bar plot
    can be requested using `mode = 'bar'`.

    :param df:
        DataFrame with data to be plotted.
    :param x_col:
        Column name that will be used for the x-axis.
    :param y_col:
        Column name that will be used for the y-axis.
    :param color:
        HEX code for color trace should be in.
    :param mode:
        Whether plot should be line or bar.
    :param trace_name:
        Name to display for trace.
    :return:
        A list of plotly traces
    """
    trace = partial(go.Scatter, mode="lines")
    if mode == "bar":
        trace = go.Bar
    return trace(
        x=df[x_col],
        y=df[y_col],
        name=trace_name,
        marker=dict(color=color),
        **kwargs,
    )


def create_traces(
    df: pd.DataFrame,
    category_col: str,
    x_col: str,
    y_col: str,
    color_mapping: typing.Dict[str, str],
    mode: str = "line",
    trace_name_suffix: typing.Optional[str] = None,
    **kwargs,
) -> typing.List[go.Trace]:
    """
    Create multiple traces for a plot -- one trace for each level of `category_col`.
    Default is a line plot, but a bar plot can be requested using `mode = 'bar'`.

    :param df:
        DataFrame with data to be plotted.
    :param category_col:
        Column in df that contains the categories the traces should be created for.
    :param x_col:
        Column name that will be used for the x-axis.
    :param y_col:
        Column name that will be used for the y-axis.
    :param color_mapping:
        color mapping for `category_col`
    :param mode:
        Whether plot should be a line or bar plot
    :param trace_name_suffix:
        Additional trace name information. Will be appended onto category.
    :return:
        A list of plotly traces
    """
    traces = []
    categories = df[category_col].unique()
    for category in categories:
        subset = df.query(f"{category_col} == @category")
        trace_name = category
        if trace_name_suffix:
            trace_name = f"{category} {trace_name_suffix}"
        trace = create_trace(
            subset,
            x_col=x_col,
            y_col=y_col,
            trace_name=trace_name,
            color=color_mapping[category],
            mode=mode,
            **kwargs,
        )
        traces.append(trace)

    return traces
