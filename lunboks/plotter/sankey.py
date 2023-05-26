"""Functions for creating sankey charts"""
import typing

import pandas as pd
import plotly.graph_objs as go


def sankey_chart(
    labels: list[typing.Union[str, int]],
    source: list[int],
    target: list[int],
    value: list[typing.Union[int, float]],
    color: str,
) -> go.Figure:
    """
    Returns a sankey chart based on labels, source, target, and value mappings.

    :param labels:
        All possible unique values for source and target
    :param source:
       Location indexes of start values (from labels)
    :param target:
       Location indexes of end values (from labels)
    :param value:
       Values that indicate the relationship between source and target--i.e.,
       the thickness of each line/mapping
    :param color:
        Color of the start end lines in the chart
    """
    return go.Figure(
        [
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="grey", width=0.5),
                    label=labels,
                    color=color,
                ),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )


def sankey_mapping(table: pd.DataFrame) -> dict[str, list]:
    """
    Generate sankey mapping labels, source, target, and values based off of
    table

    :param table:
        A summary table of data (assume groupby/aggregate was used on it
        already) that has three columns. The first two columns will be used
        to generate the labels for the chart. It is assumed the first column
        contains the starting labels and the last column contains the end
        labels. The last column will be used to generate the values.
    :return:
        a dictionary with 'labels', 'source', 'target', and 'value' lists
        that are needed to generate a sankey chart.
    """
    start_labels_col = table.columns[0]
    end_labels_col = table.columns[1]
    value_col = table.columns[2]

    start_labels = table[start_labels_col]
    end_labels = table[end_labels_col]

    unique_start_labels = list(start_labels.unique())
    unique_end_labels = list(end_labels.unique())

    labels = list(set(unique_start_labels + unique_end_labels))
    labels.sort()
    source = [labels.index(i) for i in start_labels]
    target = [labels.index(i) for i in end_labels]
    value = list(table[value_col])

    return {
        "labels": labels,
        "source": source,
        "target": target,
        "value": value,
    }
