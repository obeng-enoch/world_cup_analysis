from unittest.mock import patch

import pandas as pd

from src.analytics.matches import (
    get_biggest_upsets,
    get_biggest_wins,
    get_ended_penalties,
    get_goals_per_venue,
    get_goal_timing,
    get_highest_scoring,
    get_late_goals,
    get_match_results,
    get_possession_dominant,
    get_match_result_distribution,
)


def assert_dataframe_query(function, query_path):
    expected = pd.DataFrame({
        "value": [1],
    })

    with patch(
        "src.analytics.matches.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = function()

        pd.testing.assert_frame_equal(result, expected)
        mock_get_dataframe.assert_called_once_with(query_path)


def test_get_biggest_upsets():
    assert_dataframe_query(
        get_biggest_upsets,
        "match_analysis/biggest_upsets.sql",
    )


def test_get_biggest_wins():
    assert_dataframe_query(
        get_biggest_wins,
        "match_analysis/biggest_wins.sql",
    )


def test_get_ended_penalties():
    assert_dataframe_query(
        get_ended_penalties,
        "match_analysis/ended_penalties.sql",
    )


def test_get_goals_per_venue():
    assert_dataframe_query(
        get_goals_per_venue,
        "match_analysis/goal_per_venue.sql",
    )


def test_get_goal_timing():
    assert_dataframe_query(
        get_goal_timing,
        "match_analysis/goal_timing.sql",
    )


def test_get_highest_scoring():
    assert_dataframe_query(
        get_highest_scoring,
        "match_analysis/highest_scoring.sql",
    )


def test_get_late_goals():
    assert_dataframe_query(
        get_late_goals,
        "match_analysis/late_goals.sql",
    )


def test_get_match_results():
    assert_dataframe_query(
        get_match_results,
        "match_analysis/match_results.sql",
    )


def test_get_possession_dominant():
    assert_dataframe_query(
        get_possession_dominant,
        "match_analysis/possession_dominant.sql",
    )


def test_get_match_result_distribution():
    assert_dataframe_query(
        get_match_result_distribution,
        "match_analysis/match_result_distribution.sql",
    )