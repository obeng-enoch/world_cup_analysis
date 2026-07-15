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
    "player_stats",
    "teams",
    "matches",
]

# Registering every table here
CSV_FILES = {
    "player_stats": RAW_DATA_DIR / "player_stats.csv",
    "teams": RAW_DATA_DIR / "teams.csv",
    "matches": RAW_DATA_DIR / "matches.csv",
}

# Date columns that should be converted to datetime during the cleaning step.
DATE_COLUMNS = {
    "player_stats": ["last_verified"],
    "matches": ["date"],
}

REQUIRED_COLUMNS = {
    "player_stats": [
        "player_id",
        "player_name",
        "team_id",
        "goals",
        "last_verified",
    ],

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

    "matches": [
        "match_id",
        "date",
        "stage_id",
        "venue_id",
        "status",
        "referee_id",
    ],
}