from unittest.mock import patch

import pandas as pd

from src.analytics.teams import (
    get_aggresive_attacking,
    get_average_stats,
    get_defense,
    get_discipline_teams,
    get_highest_scoring_teams,
    get_squad_experience,
    get_squad_value,
    get_tournament_finish,
)


def test_get_aggresive_attacking():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "goals": [15],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_aggresive_attacking()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/aggresive_attacking.sql"
        )


def test_get_average_stats():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "avg_goals": [2.5],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_average_stats()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/average_stats.sql"
        )


def test_get_defense():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "clean_sheets": [4],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_defense()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/defense.sql"
        )


def test_get_discipline_teams():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "yellow_cards": [3],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_discipline_teams()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/discipline.sql"
        )


def test_get_highest_scoring_teams():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "goals": [15],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_highest_scoring_teams()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/highest_scoring_teams.sql"
        )


def test_get_squad_experience():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "avg_caps": [45.2],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_squad_experience()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/squad_experience.sql"
        )


def test_get_squad_value():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "squad_value": [500_000_000],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_squad_value()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/squad_value.sql"
        )


def test_get_tournament_finish():
    expected = pd.DataFrame({
        "team_name": ["Spain"],
        "finish_position": [1],
    })

    with patch(
        "src.analytics.teams.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_tournament_finish()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "teams/tournament_finish.sql"
        )