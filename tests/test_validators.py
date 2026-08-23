import pandas as pd
import pytest

from src.validators import (
    validate_teams,
    validate_venues,
    validate_tournament_stages,
    validate_referees,
    validate_squads_and_players,
    validate_matches,
    validate_player_stats,
    validate_match_team_stats,
    validate_match_events,
    validate_match_lineups,
    validate_tournament_awards,
)


def test_validate_teams_accepts_valid_data():
    df = pd.DataFrame({
        "team_id": [1],
        "team_name": ["Spain"],
        "fifa_code": ["ESP"],
        "group_letter": ["B"],
        "confederation": ["UEFA"],
        "fifa_ranking_pre_tournament": [1],
        "elo_rating": [2100],
        "manager_name": ["Manager"],
    })

    assert validate_teams(df) is True


def test_validate_teams_rejects_empty_dataframe():
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        validate_teams(df)


def test_validate_teams_rejects_duplicate_team_id():
    df = pd.DataFrame({
        "team_id": [1, 1],
        "team_name": ["Spain", "Argentina"],
        "fifa_code": ["ESP", "ARG"],
        "group_letter": ["B", "J"],
        "confederation": ["UEFA", "CONMEBOL"],
        "fifa_ranking_pre_tournament": [1, 2],
        "elo_rating": [2100, 2050],
        "manager_name": ["Manager A", "Manager B"],
    })

    with pytest.raises(ValueError):
        validate_teams(df)


def test_validate_teams_rejects_missing_required_column():
    df = pd.DataFrame({
        "team_id": [1],
        "team_name": ["Spain"],
        "fifa_code": ["ESP"],
        "group_letter": ["B"],
        "confederation": ["UEFA"],
        "fifa_ranking_pre_tournament": [1],
        "elo_rating": [2100],
        # manager_name intentionally missing
    })

    with pytest.raises(KeyError):
        validate_teams(df)


def test_validate_venues_accepts_valid_data():
    df = pd.DataFrame({
        "venue_id": [1],
        "stadium_name": ["Stadium"],
        "city": ["City"],
        "country": ["Country"],
        "capacity": [50000],
        "latitude": [40.0],
        "longitude": [-3.0],
        "elevation_meters": [100],
    })

    assert validate_venues(df) is True


def test_validate_tournament_stages_accepts_valid_data():
    df = pd.DataFrame({
        "stage_id": [1],
        "stage_name": ["Final"],
        "is_knockout": [1],
    })

    assert validate_tournament_stages(df) is True


def test_validate_referees_accepts_valid_data():
    df = pd.DataFrame({
        "referee_id": [1],
        "name": ["Referee"],
        "country": ["Spain"],
        "avg_cards_per_game": [4.2],
    })

    assert validate_referees(df) is True

def valid_player_dataframe():
    """Return a minimal valid squads_and_players DataFrame."""

    return pd.DataFrame({
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
    })


def test_validate_squads_and_players_accepts_valid_data():
    df = valid_player_dataframe()

    assert validate_squads_and_players(df) is True


def test_validate_squads_and_players_rejects_duplicate_player_id():
    df = valid_player_dataframe()
    df.loc[1] = df.loc[0]
    
    with pytest.raises(ValueError):
        validate_squads_and_players(df)


def test_validate_squads_and_players_rejects_negative_market_value():
    df = valid_player_dataframe()
    df.loc[0, "market_value_eur"] = -1

    with pytest.raises(ValueError):
        validate_squads_and_players(df)


def test_validate_squads_and_players_rejects_negative_caps():
    df = valid_player_dataframe()
    df.loc[0, "caps"] = -1

    with pytest.raises(ValueError):
        validate_squads_and_players(df)


def test_validate_squads_and_players_rejects_negative_goals():
    df = valid_player_dataframe()
    df.loc[0, "goals"] = -1

    with pytest.raises(ValueError):
        validate_squads_and_players(df)


def test_validate_squads_and_players_rejects_invalid_height():
    df = valid_player_dataframe()
    df.loc[0, "height_cm"] = 0

    with pytest.raises(ValueError):
        validate_squads_and_players(df)


def test_validate_squads_and_players_rejects_invalid_date_type():
    df = valid_player_dataframe()
    df["date_of_birth"] = ["1996-06-22"]

    with pytest.raises(ValueError):
        validate_squads_and_players(df)

def valid_matches_dataframe():
    """Return a minimal valid matches DataFrame."""

    return pd.DataFrame({
        "match_id": [1],
        "date": pd.to_datetime(["2026-06-11"]),
        "stage_id": [1],
        "venue_id": [1],
        "status": ["completed"],
        "referee_id": [1],
    })


def test_validate_matches_accepts_valid_data():
    df = valid_matches_dataframe()

    assert validate_matches(df) is True


def test_validate_matches_rejects_duplicate_match_id():
    df = valid_matches_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_matches(df)


def test_validate_matches_rejects_missing_required_column():
    df = valid_matches_dataframe()
    df = df.drop(columns=["referee_id"])

    with pytest.raises(KeyError):
        validate_matches(df)


def test_validate_matches_rejects_missing_required_value():
    df = valid_matches_dataframe()
    df.loc[0, "status"] = None

    with pytest.raises(ValueError):
        validate_matches(df)

def valid_player_stats_dataframe():
    """Return a minimal valid player_stats DataFrame."""

    return pd.DataFrame({
        "player_id": [1],
        "player_name": ["Rodri"],
        "team_id": [10],
        "goals": [3],
        "last_verified": pd.to_datetime(["2026-08-01"]),
    })


def test_validate_player_stats_accepts_valid_data():
    df = valid_player_stats_dataframe()

    assert validate_player_stats(df) is True


def test_validate_player_stats_rejects_duplicate_player_id():
    df = valid_player_stats_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_player_stats(df)


def test_validate_player_stats_rejects_missing_required_column():
    df = valid_player_stats_dataframe()
    df = df.drop(columns=["goals"])

    with pytest.raises(KeyError):
        validate_player_stats(df)


def test_validate_player_stats_rejects_missing_required_value():
    df = valid_player_stats_dataframe()
    df.loc[0, "player_name"] = None

    with pytest.raises(ValueError):
        validate_player_stats(df)

def valid_player_stats_dataframe():
    """Return a minimal valid player_stats DataFrame."""

    return pd.DataFrame({
        "player_id": [1],
        "player_name": ["Rodri"],
        "team_id": [10],
        "goals": [3],
        "last_verified": pd.to_datetime(["2026-08-01"]),
    })


def test_validate_player_stats_accepts_valid_data():
    df = valid_player_stats_dataframe()

    assert validate_player_stats(df) is True


def test_validate_player_stats_rejects_duplicate_player_id():
    df = valid_player_stats_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_player_stats(df)


def test_validate_player_stats_rejects_missing_required_column():
    df = valid_player_stats_dataframe()
    df = df.drop(columns=["goals"])

    with pytest.raises(KeyError):
        validate_player_stats(df)


def test_validate_player_stats_rejects_missing_required_value():
    df = valid_player_stats_dataframe()
    df.loc[0, "player_name"] = None

    with pytest.raises(ValueError):
        validate_player_stats(df)

def valid_match_team_stats_dataframe():
    """Return a minimal valid match_team_stats DataFrame."""

    return pd.DataFrame({
        "match_id": [1],
        "team_id": [10],
        "possession_pct": [55.0],
        "total_shots": [12],
        "shots_on_target": [5],
        "corners": [6],
        "fouls": [8],
        "offsides": [2],
        "saves": [3],
        "data_source": ["official"],
        "last_updated": pd.to_datetime(["2026-08-01"]),
    })


def test_validate_match_team_stats_accepts_valid_data():
    df = valid_match_team_stats_dataframe()

    assert validate_match_team_stats(df) is True


def test_validate_match_team_stats_rejects_duplicate_match_team():
    df = valid_match_team_stats_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_match_team_stats(df)


def test_validate_match_team_stats_rejects_possession_out_of_range():
    df = valid_match_team_stats_dataframe()
    df.loc[0, "possession_pct"] = 101

    with pytest.raises(ValueError):
        validate_match_team_stats(df)


def test_validate_match_team_stats_rejects_negative_shots():
    df = valid_match_team_stats_dataframe()
    df.loc[0, "total_shots"] = -1

    with pytest.raises(ValueError):
        validate_match_team_stats(df)

def valid_match_events_dataframe():
    """Return a minimal valid match_events DataFrame."""

    return pd.DataFrame({
        "event_id": [1],
        "match_id": [1],
        "minute": ["45"],
        "event_type": ["Goal"],
        "team_id": [10],
        "player_id": [100],
    })


def test_validate_match_events_accepts_valid_data():
    df = valid_match_events_dataframe()

    assert validate_match_events(df) is True


def test_validate_match_events_rejects_duplicate_event_id():
    df = valid_match_events_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_match_events(df)


def test_validate_match_events_rejects_non_string_minute():
    df = valid_match_events_dataframe()
    df["minute"] = [45]  # int instead of string

    with pytest.raises(ValueError):
        validate_match_events(df)


def test_validate_match_events_rejects_missing_event_type():
    df = valid_match_events_dataframe()
    df.loc[0, "event_type"] = None

    with pytest.raises(ValueError):
        validate_match_events(df)

def valid_match_lineups_dataframe():
    """Return a minimal valid match_lineups DataFrame."""

    return pd.DataFrame({
        "lineup_id": [1],
        "match_id": [1],
        "player_id": [100],
        "team_id": [10],
        "is_starting_xi": [1],
        "tactical_position": ["CM"],
        "minutes_played": [90],
    })


def test_validate_match_lineups_accepts_valid_data():
    df = valid_match_lineups_dataframe()

    assert validate_match_lineups(df) is True


def test_validate_match_lineups_rejects_duplicate_lineup_id():
    df = valid_match_lineups_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_match_lineups(df)


def test_validate_match_lineups_rejects_invalid_starting_xi():
    df = valid_match_lineups_dataframe()
    df.loc[0, "is_starting_xi"] = 2

    with pytest.raises(ValueError):
        validate_match_lineups(df)


def test_validate_match_lineups_rejects_negative_minutes():
    df = valid_match_lineups_dataframe()
    df.loc[0, "minutes_played"] = -1

    with pytest.raises(ValueError):
        validate_match_lineups(df)


def test_validate_match_lineups_rejects_minutes_above_120():
    df = valid_match_lineups_dataframe()
    df.loc[0, "minutes_played"] = 121

    with pytest.raises(ValueError):
        validate_match_lineups(df)

def valid_tournament_awards_dataframe():
    """Return a minimal valid tournament_awards DataFrame."""

    return pd.DataFrame({
        "award_id": [1],
        "award_name": ["Golden Boot"],
        "recipient_type": ["player"],
        "team": ["Spain"],
    })


def test_validate_tournament_awards_accepts_valid_data():
    df = valid_tournament_awards_dataframe()

    assert validate_tournament_awards(df) is True


def test_validate_tournament_awards_rejects_empty_dataframe():
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        validate_tournament_awards(df)


def test_validate_tournament_awards_rejects_missing_required_column():
    df = valid_tournament_awards_dataframe()
    df = df.drop(columns=["recipient_type"])

    with pytest.raises(KeyError):
        validate_tournament_awards(df)


def test_validate_tournament_awards_rejects_missing_required_value():
    df = valid_tournament_awards_dataframe()
    df.loc[0, "team"] = None

    with pytest.raises(ValueError):
        validate_tournament_awards(df)


def test_validate_tournament_awards_rejects_duplicate_award_id():
    df = valid_tournament_awards_dataframe()
    df.loc[1] = df.loc[0]

    with pytest.raises(ValueError):
        validate_tournament_awards(df)