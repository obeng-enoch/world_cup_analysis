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
    "matches",
]

# Registering every table here
CSV_FILES = {
    "player_stats": RAW_DATA_DIR / "player_stats.csv",
    "matches": RAW_DATA_DIR / "matches.csv",
}

# Date columns that should be converted to datetime during the cleaning step.
DATE_COLUMNS = {
    "player_stats": ["last_verified"],
    "matches": ["date"],
}