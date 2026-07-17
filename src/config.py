from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "worldcup"
CLEANED_DATA_DIR = PROJECT_ROOT / "data" / "cleaned"

# Database directory
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

# SQLITE database
DATABASE_PATH = DATABASE_DIR / "world_cup_2026.db"

# Tables currently being processed
TABLES = [
    "teams",
    "venues",
    "tournament_stages",
    "referees",
    "squads_and_players",
    "matches",
    "player_stats",
    "match_team_stats",
    "match_events",
    "match_lineups.csv",
]

# Registering every table here
CSV_FILES = {
    "teams": RAW_DATA_DIR / "teams.csv",
    "venues": RAW_DATA_DIR / "venues.csv",
    "tournament_stages": RAW_DATA_DIR / "tournament_stages.csv",
    "referees": RAW_DATA_DIR / "referees.csv",
    "squads_and_players": RAW_DATA_DIR / "squads_and_players.csv",
    "matches": RAW_DATA_DIR / "matches.csv",
    "player_stats": RAW_DATA_DIR / "player_stats.csv",
    "match_team_stats": RAW_DATA_DIR / "match_team_stats.csv",
    "match_events": RAW_DATA_DIR / "match_events.csv",
    "match_lineups": RAW_DATA_DIR / "match_lineups.csv",
}

# Date columns that should be converted to datetime during the cleaning step.
DATE_COLUMNS = {
    "squads_and_players": ["date_of_birth"],
    "matches": ["date"],
    "player_stats": ["last_verified"],
    "match_team_stats": ["last_updated"],
}

REQUIRED_COLUMNS = {
    "teams": [
        "team_id",
        "team_name",
        "fifa_code",
        "group_letter",
        "confederation",
        "fifa_ranking_pre_tournament",
        "elo_rating",
        "manager_name",
    ],

    "venues": [
        "venue_id",
        "stadium_name",
        "city",
        "country",
        "capacity",
        "latitude",
        "longitude",
        "elevation_meters",
    ],

    "tournament_stages": [
        "stage_id",
        "stage_name",
        "is_knockout",
    ],

    "referees": [
        "referee_id",
        "name",
        "country",
        "avg_cards_per_game",
    ],

    "squads_and_players": [
        "player_id",
        "team_id",
        "player_name",
        "position",
        "club_team",
        "market_value_eur",
        "caps",
        "date_of_birth",
        "height_cm",
        "goals",
    ],

    "matches": [
        "match_id",
        "date",
        "stage_id",
        "venue_id",
        "status",
        "referee_id",
    ],

    "player_stats": [
        "player_id",
        "player_name",
        "team_id",
        "goals",
        "last_verified",
    ],

    "match_team_stats": [
        "match_id",
        "team_id",
        "possession_pct",
        "total_shots",
        "shots_on_target",
        "corners",
        "fouls",
        "offsides",
        "saves",
        "data_source",
        "last_updated",
    ],

    "match_events": [
        "event_id",
        "match_id",
        "minute",
        "event_type",
        "team_id",
        "player_id",
    ],

    "match_lineups": [
        "lineup_id",
        "match_id",
        "player_id",
        "team_id",
        "is_starting_xi",
        "tactical_position",
        "minutes_played",
    ]
}