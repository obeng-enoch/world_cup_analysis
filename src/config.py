from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "worldcup"
CLEANED_DATA_DIR = PROJECT_ROOT / "data" / "cleaned"

# Database directory
DATABASE_DIR = PROJECT_ROOT / "database"

# SQLITE database
DATABASE_PATH = DATABASE_DIR / "world_cup_2026.db"

# Tables currently being processed
TABLES = [
    "teams",
    "venues",
    "tournament_stages",
    "referees",
    "squads_and_players",
    "player_stats",
    "matches",
]

# Registering every table here
CSV_FILES = {
    "teams": RAW_DATA_DIR / "teams.csv",
    "venues": RAW_DATA_DIR / "venues.csv",
    "tournament_stages": RAW_DATA_DIR / "tournament_stages.csv",
    "referees": RAW_DATA_DIR / "referees.csv",
    "squads_and_players": RAW_DATA_DIR / "squads_and_players.csv",
    "player_stats": RAW_DATA_DIR / "player_stats.csv",
    "matches": RAW_DATA_DIR / "matches.csv",
}

# Date columns that should be converted to datetime during the cleaning step.
DATE_COLUMNS = {
    "player_stats": ["last_verified"],
    "squads_and_players": ["date_of_birth"],
    "matches": ["date"],
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

    "player_stats": [
        "player_id",
        "player_name",
        "team_id",
        "goals",
        "last_verified",
    ],

    "matches": [
        "match_id",
        "date",
        "stage_id",
        "venue_id",
        "status",
        "referee_id",
    ],
}