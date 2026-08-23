from unittest.mock import patch

import pandas as pd

from src.analytics.tournament import (
    get_total_players,
    get_total_teams,
    get_total_matches,
    get_total_goals,
    get_world_cup_winner,
    get_runner_up,
    get_third_place,
    get_goals_per_stage,
)


def test_get_total_players():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value=1248,
    ) as mock_get_scalar:

        result = get_total_players()

        assert result == 1248
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/total_players.sql"
        )


def test_get_total_teams():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value=48,
    ) as mock_get_scalar:

        result = get_total_teams()

        assert result == 48
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/total_teams.sql"
        )


def test_get_total_matches():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value=104,
    ) as mock_get_scalar:

        result = get_total_matches()

        assert result == 104
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/total_matches.sql"
        )


def test_get_total_goals():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value=308,
    ) as mock_get_scalar:

        result = get_total_goals()

        assert result == 308
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/total_goals.sql"
        )


def test_get_world_cup_winner():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value="Spain",
    ) as mock_get_scalar:

        result = get_world_cup_winner()

        assert result == "Spain"
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/world_cup_winner.sql"
        )


def test_get_runner_up():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value="Argentina",
    ) as mock_get_scalar:

        result = get_runner_up()

        assert result == "Argentina"
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/runner_up.sql"
        )


def test_get_third_place():
    with patch(
        "src.analytics.tournament.get_scalar",
        return_value="England",
    ) as mock_get_scalar:

        result = get_third_place()

        assert result == "England"
        mock_get_scalar.assert_called_once_with(
            "tournament_overview/third_place.sql"
        )


def test_get_goals_per_stage():
    expected = pd.DataFrame({
        "stage_name": ["Group Stage", "Final"],
        "goals": [200, 5],
    })

    with patch(
        "src.analytics.tournament.get_dataframe",
        return_value=expected,
    ) as mock_get_dataframe:

        result = get_goals_per_stage()

        pd.testing.assert_frame_equal(result, expected)

        mock_get_dataframe.assert_called_once_with(
            "tournament_overview/goals_per_stage.sql"
        )