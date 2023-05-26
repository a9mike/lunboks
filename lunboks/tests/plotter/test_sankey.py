import pandas as pd
import plotly.graph_objs as go

from lunboks import plotter


SANKEY_DF = pd.DataFrame(
    {
        "start": ["a", "b", "a"],
        "end": ["c", "d", "d"],
        "values": [1, 3, 2],
    }
)
SANKEY_MAPPING = {
    "labels": ["a", "b", "c", "d"],
    "source": [0, 1, 0],
    "target": [2, 3, 3],
    "value": [1, 3, 2],
}


def test_sankey_mapping():
    """
    Should return a dictionary with expected labels, source, target, and value
    """
    result = plotter.sankey_mapping(SANKEY_DF)

    assert result == SANKEY_MAPPING


def test_sankey_chart():
    """Should return a Figure"""
    sankey = plotter.sankey_chart(
        **SANKEY_MAPPING,
        color="#007AC9",
    )

    assert isinstance(sankey, go.Figure)
