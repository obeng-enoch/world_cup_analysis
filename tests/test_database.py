import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/world_cup_2026.db")


def test_database_exists():
    """The analytics database should exist in the expected location."""
    assert DATABASE_PATH.exists()


def test_database_contains_expected_tables():
    """The analytics database should contain all required tables."""

    expected_tables = {
        "tournament_stages",
        "venues",
        "referees",
        "teams",
        "squads_and_players",
        "matches",
        "player_stats",
        "match_team_stats",
        "match_events",
        "match_lineups",
        "tournament_awards",
    }

    with sqlite3.connect(DATABASE_PATH) as connection:
        rows = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            """
        ).fetchall()

    actual_tables = {row[0] for row in rows}

    assert expected_tables.issubset(actual_tables)

def test_database_contains_expected_row_counts():
    """Core database tables should contain the expected number of rows."""

    expected_counts = {
        "teams": 48,
        "squads_and_players": 1248,
        "matches": 104,
        "player_stats": 1248,
        "match_events": 834,
        "match_lineups": 5408,
    }

    with sqlite3.connect(DATABASE_PATH) as connection:
        for table, expected_count in expected_counts.items():
            actual_count = connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]

            assert actual_count == expected_count, (
                f"{table}: expected {expected_count} rows, "
                f"found {actual_count}"
            )

def test_match_team_stats_cover_all_matches():
    """Every match should have team statistics."""

    with sqlite3.connect(DATABASE_PATH) as connection:
        match_count = connection.execute(
            "SELECT COUNT(*) FROM matches"
        ).fetchone()[0]

        stats_match_count = connection.execute(
            "SELECT COUNT(DISTINCT match_id) FROM match_team_stats"
        ).fetchone()[0]

    assert stats_match_count == match_count

def test_each_match_has_two_team_stats():
    """Every match should have exactly two team-stat records."""

    with sqlite3.connect(DATABASE_PATH) as connection:
        rows = connection.execute(
            """
            SELECT match_id, COUNT(*) AS team_count
            FROM match_team_stats
            GROUP BY match_id
            """
        ).fetchall()

    assert rows, "match_team_stats should contain records"

    for match_id, team_count in rows:
        assert team_count == 2, (
            f"Match {match_id} has {team_count} team-stat records; "
            "expected exactly 2."
        )