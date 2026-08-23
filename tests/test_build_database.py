import sqlite3

import pandas as pd
import pytest

import src.build_database as build_db

from datetime import datetime

VALID_DATA = {
    "venues": pd.DataFrame({
        "venue_id": [1],
        "stadium_name": ["Stadium"],
        "city": ["City"],
        "country": ["Country"],
        "capacity": [50000],
        "latitude": [40.0],
        "longitude": [-3.0],
        "elevation_meters": [100],
    }),

    "tournament_stages": pd.DataFrame({
        "stage_id": [1],
        "stage_name": ["Final"],
        "is_knockout": [1],
    }),

    "referees": pd.DataFrame({
        "referee_id": [1],
        "name": ["Referee"],
        "country": ["Spain"],
        "avg_cards_per_game": [4.2],
    }),

    "squads_and_players": pd.DataFrame({
        "player_id": [1],
        "team_id": [10],
        "player_name": ["Rodri"],
        "position": ["MID"],
        "club_team": ["Manchester City"],
        "market_value_eur": [100_000_000],
        "caps": [60],
        "date_of_birth": pd.to_datetime(["1996-06-22"]),
        "height_cm": [191],
        "goals": [10],
    }),

    "matches": pd.DataFrame({
        "match_id": [1],
        "date": pd.to_datetime(["2026-06-11"]),
        "stage_id": [1],
        "venue_id": [1],
        "status": ["completed"],
        "referee_id": [1],
    }),

    "player_stats": pd.DataFrame({
        "player_id": [1],
        "player_name": ["Rodri"],
        "team_id": [10],
        "goals": [3],
        "last_verified": pd.to_datetime(["2026-08-01"]),
    }),

    "match_team_stats": pd.DataFrame({
        "match_id": [1],
        "team_id": [10],
        "possession_pct": [55.0],
        "total_shots": [10],
        "shots_on_target": [5],
        "corners": [4],
        "fouls": [8],
        "offsides": [2],
        "saves": [3],
        "data_source": ["test"],
        "last_updated": pd.to_datetime(["2026-08-01"]),
    }),

    "match_events": pd.DataFrame({
        "event_id": [1],
        "match_id": [1],
        "minute": ["45"],
        "event_type": ["goal"],
        "team_id": [10],
        "player_id": [1],
    }),

    "match_lineups": pd.DataFrame({
        "lineup_id": [1],
        "match_id": [1],
        "player_id": [1],
        "team_id": [10],
        "is_starting_xi": [1],
        "tactical_position": ["CM"],
        "minutes_played": [90],
    }),

    "tournament_awards": pd.DataFrame({
        "award_id": [1],
        "award_name": ["Golden Ball"],
        "recipient_type": ["player"],
        "team": ["Spain"],
    }),
}

LOADERS = {
    "venues": (
        build_db.load_venues,
        "clean_venues",
    ),
    "tournament_stages": (
        build_db.load_tournament_stages,
        "clean_tournament_stages",
    ),
    "referees": (
        build_db.load_referees,
        "clean_referees",
    ),
    "squads_and_players": (
        build_db.load_squads_and_players,
        "clean_squads_and_players",
    ),
    "matches": (
        build_db.load_matches,
        "clean_matches",
    ),
    "player_stats": (
        build_db.load_player_stats,
        "clean_player_stats",
    ),
    "match_team_stats": (
        build_db.load_match_team_stats,
        "clean_match_team_stats",
    ),
    "match_events": (
        build_db.load_match_events,
        "clean_match_events",
    ),
    "match_lineups": (
        build_db.load_match_lineups,
        "clean_match_lineups",
    ),
    "tournament_awards": (
        build_db.load_tournament_awards,
        "clean_tournament_awards",
    ),
}

@pytest.fixture
def temp_connection(tmp_path, monkeypatch):
    """Create a temporary SQLite database connection for testing."""

    test_database = tmp_path / "test_world_cup.db"

    monkeypatch.setattr(
        build_db,
        "DATABASE_PATH",
        test_database,
    )

    connection = build_db.get_database_connection()

    yield connection

    connection.close()


def test_get_database_connection_returns_sqlite_connection(
    temp_connection,
):
    assert isinstance(temp_connection, sqlite3.Connection)


def test_load_teams_writes_dataframe_to_database(
    temp_connection,
    monkeypatch,
):
    teams = pd.DataFrame({
        "team_id": [1],
        "team_name": ["Spain"],
        "fifa_code": ["ESP"],
        "group_letter": ["B"],
        "confederation": ["UEFA"],
        "fifa_ranking_pre_tournament": [1],
        "elo_rating": [2100],
        "manager_name": ["Manager"],
    })

    monkeypatch.setattr(
        build_db,
        "clean_teams",
        lambda: teams,
    )

    monkeypatch.setattr(
        build_db,
        "validate_teams",
        lambda df: True,
    )

    build_db.load_teams(temp_connection)

    result = pd.read_sql_query(
        "SELECT * FROM teams",
        temp_connection,
    )

    assert len(result) == 1
    assert result.loc[0, "team_name"] == "Spain"


def test_load_teams_does_not_load_invalid_data(
    temp_connection,
    monkeypatch,
):
    teams = pd.DataFrame({
        "team_id": [1],
        "team_name": ["Spain"],
    })

    monkeypatch.setattr(
        build_db,
        "clean_teams",
        lambda: teams,
    )

    def reject_invalid_data(df):
        raise ValueError("Invalid teams data")

    monkeypatch.setattr(
        build_db,
        "validate_teams",
        reject_invalid_data,
    )

    with pytest.raises(ValueError, match="Invalid teams data"):
        build_db.load_teams(temp_connection)

    tables = pd.read_sql_query(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='teams'
        """,
        temp_connection,
    )

    assert tables.empty


def test_build_database_calls_loaders_in_order(
    monkeypatch,
):
    calls = []

    def record_call(name):
        def loader(connection):
            calls.append(name)

        return loader

    loader_names = [
        "load_teams",
        "load_venues",
        "load_tournament_stages",
        "load_referees",
        "load_squads_and_players",
        "load_matches",
        "load_player_stats",
        "load_match_team_stats",
        "load_match_events",
        "load_match_lineups",
        "load_tournament_awards",
    ]

    for name in loader_names:
        monkeypatch.setattr(
            build_db,
            name,
            record_call(name),
        )

    monkeypatch.setattr(
        build_db,
        "get_database_connection",
        lambda: sqlite3.connect(":memory:"),
    )

    build_db.build_database()

    assert calls == loader_names

@pytest.mark.parametrize(
    "table_name, loader_info",
    LOADERS.items(),
)
def test_loaders_write_expected_tables(
    temp_connection,
    monkeypatch,
    table_name,
    loader_info,
):
    loader, cleaner_name = loader_info

    dataframe = VALID_DATA[table_name]

    monkeypatch.setattr(
        build_db,
        cleaner_name,
        lambda df=dataframe: df,
    )

    loader(temp_connection)

    tables = pd.read_sql_query(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name=?
        """,
        temp_connection,
        params=(table_name,),
    )

    assert not tables.empty

    result = pd.read_sql_query(
        f"SELECT * FROM {table_name}",
        temp_connection,
    )

    assert len(result) == 1