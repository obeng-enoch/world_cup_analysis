import pandas as pd
import pytest

from src.clean_data import (
    load_csv,
    convert_dates,
    clean_teams,
    clean_matches,
    clean_player_stats,
    clean_match_team_stats,
)


def test_load_csv_returns_dataframe():
    """Loading a known table should return a DataFrame."""

    result = load_csv("teams")

    assert isinstance(result, pd.DataFrame)
    assert not result.empty


def test_load_csv_rejects_unknown_table():
    """An unknown table name should raise ValueError."""

    with pytest.raises(ValueError):
        load_csv("unknown_table")


def test_convert_dates_converts_column_to_datetime():
    """Specified date columns should be converted to datetime."""

    df = pd.DataFrame(
        {
            "date": ["2026-06-11", "2026-06-12"],
        }
    )

    result = convert_dates(df, ["date"])

    assert pd.api.types.is_datetime64_any_dtype(result["date"])


def test_convert_dates_rejects_missing_column():
    """A missing date column should raise KeyError."""

    df = pd.DataFrame(
        {
            "date": ["2026-06-11"],
        }
    )

    with pytest.raises(KeyError):
        convert_dates(df, ["missing_date"])


def test_clean_teams_returns_expected_data():
    """clean_teams should return the teams dataset."""

    teams = clean_teams()

    assert isinstance(teams, pd.DataFrame)
    assert len(teams) == 48
    assert "team_id" in teams.columns
    assert "team_name" in teams.columns


def test_clean_matches_converts_date():
    """clean_matches should convert the match date column."""

    matches = clean_matches()

    assert isinstance(matches, pd.DataFrame)
    assert len(matches) == 104
    assert pd.api.types.is_datetime64_any_dtype(matches["date"])


def test_clean_player_stats_converts_last_verified():
    """clean_player_stats should convert last_verified to datetime."""

    player_stats = clean_player_stats()

    assert isinstance(player_stats, pd.DataFrame)
    assert len(player_stats) == 1248
    assert pd.api.types.is_datetime64_any_dtype(
        player_stats["last_verified"]
    )


def test_clean_match_team_stats_converts_last_updated():
    """clean_match_team_stats should convert last_updated to datetime."""

    match_team_stats = clean_match_team_stats()

    assert isinstance(match_team_stats, pd.DataFrame)
    assert len(match_team_stats) == 208
    assert pd.api.types.is_datetime64_any_dtype(
        match_team_stats["last_updated"]
    )