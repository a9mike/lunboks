from unittest.mock import MagicMock
from unittest.mock import patch

import pandas as pd

from lunboks import plotter


@patch("plotly.graph_objs.Bar")
@patch("plotly.graph_objs.Scatter")
def test_create_trace(line: MagicMock, bar: MagicMock):
    """Should call function to create a line trace"""
    plotter.create_trace(
        df=MagicMock(), x_col="x", y_col="y", color="rainbow", trace_name="Magic"
    )

    line.assert_called_once()
    bar.assert_not_called()


@patch("plotly.graph_objs.Bar")
@patch("plotly.graph_objs.Scatter")
def test_create_bar_trace(line: MagicMock, bar: MagicMock):
    """Should call function to create a bar trace"""
    plotter.create_trace(
        df=MagicMock(),
        x_col="x",
        y_col="y",
        color="rainbow",
        trace_name="Magic",
        mode="bar",
    )

    bar.assert_called_once()
    line.assert_not_called()


@patch("lunboks.plotter.tracer.create_trace")
def test_create_traces(trace: MagicMock):
    """Should create 4 traces"""
    plot_data = pd.DataFrame(
        {
            "bts": ["Liar", "Fly", "Car", "Else"],
            "x": [1, 2, 3, 4],
            "y": [2, 3, 4, 9],
        }
    )
    colors = {
        "Liar": "blue",
        "Fly": "yellow",
        "Car": "green",
        "Else": "purple",
    }
    plotter.create_traces(
        plot_data,
        category_col="bts",
        x_col="x",
        y_col="y",
        color_mapping=colors,
        mode="bar",
    )

    assert trace.call_count == 4
