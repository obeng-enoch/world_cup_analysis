from unittest.mock import patch

import pandas as pd

from src.analytics.players import (
    get_top_scorers,
    get_hat_tricks,
    get_multi_goal_matches,
    get_penalty_goals,
    get_own_goals,
    get_top_assists,
    get_goal_contributions,
    get_appearances,
    get_starts,
    get_minutes_played,
    get_yellow_cards,
    get_red_cards,
    get_clean_sheets,
    get_saves,
    get_goals_conceded,
)


def assert_dataframe_query(function, query_path):
    expected = pd.DataFrame({"player_name": ["Rodri"], "value": [1]})

    with patch(
        "src.analytics.players.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = function()

        pd.testing.assert_frame_equal(result, expected)
        mock_get_dataframe.assert_called_once_with(query_path)


def test_get_top_scorers():
    assert_dataframe_query(
        get_top_scorers,
        "players/top_scorers.sql",
    )


def test_get_hat_tricks():
    assert_dataframe_query(
        get_hat_tricks,
        "players/hat_tricks.sql",
    )


def test_get_multi_goal_matches():
    assert_dataframe_query(
        get_multi_goal_matches,
        "players/multi_goal_matches.sql",
    )


def test_get_penalty_goals():
    assert_dataframe_query(
        get_penalty_goals,
        "players/penalty_goals.sql",
    )


def test_get_own_goals():
    assert_dataframe_query(
        get_own_goals,
        "players/own_goals.sql",
    )


def test_get_top_assists():
    assert_dataframe_query(
        get_top_assists,
        "players/tops_assists.sql",
    )


def test_get_goal_contributions():
    assert_dataframe_query(
        get_goal_contributions,
        "players/goal_contributions.sql",
    )


def test_get_appearances():
    assert_dataframe_query(
        get_appearances,
        "players/appearances.sql",
    )


def test_get_starts():
    assert_dataframe_query(
        get_starts,
        "players/starts.sql",
    )


def test_get_minutes_played():
    assert_dataframe_query(
        get_minutes_played,
        "players/minutes_played.sql",
    )


def test_get_yellow_cards():
    assert_dataframe_query(
        get_yellow_cards,
        "players/yellow_cards.sql",
    )


def test_get_red_cards():
    assert_dataframe_query(
        get_red_cards,
        "players/red_cards.sql",
    )


def test_get_clean_sheets():
    assert_dataframe_query(
        get_clean_sheets,
        "players/clean_sheets.sql",
    )


def test_get_saves():
    assert_dataframe_query(
        get_saves,
        "players/saves.sql",
    )


def test_get_goals_conceded():
    assert_dataframe_query(
        get_goals_conceded,
        "players/goals_conceded.sql",
    )