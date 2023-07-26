import pandas as pd
from pandas import testing

from lunboks import transformer


DF = pd.DataFrame(
    {
        "animal": ["opossum", "bat", "frog", "owl", "hawk"],
        "class": ["mammal", "mammal", "amphibian", "bird", "bird"],
        "count": [2, 2, 1, 2, 3],
    }
)


def test_group_mean():
    """Should return mean of animals grouped by class"""
    result = transformer.group_mean(DF, "class", "count")
    expected = pd.DataFrame(
        {"class": ["bird", "mammal", "amphibian"], "mean": [2.5, 2.0, 1.0]}
    )

    testing.assert_frame_equal(result, expected)


def test_groups_mean():
    """Should return mean of data grouped by animals and class"""
    result = transformer.group_mean(DF, ["class", "animal"], "count")
    expected = pd.Series([3.0, 2, 2, 2, 1], name="mean")

    testing.assert_series_equal(result["mean"], expected)


def test_group_count():
    """Should return count of animals grouped by class"""
    result = transformer.group_count(DF, "class", "animal")
    expected = pd.DataFrame(
        {"class": ["bird", "mammal", "amphibian"], "count": [2, 2, 1]}
    )

    testing.assert_frame_equal(result, expected)


def test_groups_count():
    """Should return count of data grouped by animals and class"""
    result = transformer.group_count(DF, ["class", "animal"], "count")

    assert all(result["count"] == 1)


def test_group_sum():
    """Should return sum of counts grouped by class"""
    result = transformer.group_sum(DF, "class", "count")
    expected = pd.DataFrame(
        {"class": ["bird", "mammal", "amphibian"], "sum": [5, 4, 1]}
    )

    testing.assert_frame_equal(result, expected)


def test_groups_sum():
    """Should return sum of data grouped by animals and class"""
    result = transformer.group_sum(DF, ["class", "animal"], "count")
    expected = pd.Series([3, 2, 2, 2, 1], name="sum")

    testing.assert_series_equal(result["sum"], expected)


def test_group_nunique():
    """Should return unique counts of count by class"""
    result = transformer.group_nunique(DF, "count", "animal")
    expected = pd.DataFrame({"count": [2, 1, 3], "n_unique": [3, 1, 1]})

    testing.assert_frame_equal(result, expected)


def test_groups_nunique():
    """Should return unique counts of count by class"""
    result = transformer.group_nunique(DF, ["class", "count"], "animal")
    expected = pd.DataFrame(
        {
            "class": ["mammal", "amphibian", "bird", "bird"],
            "count": [2, 1, 2, 3],
            "n_unique": [2, 1, 1, 1],
        }
    )

    testing.assert_frame_equal(result, expected)
