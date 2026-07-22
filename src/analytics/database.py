from pathlib import Path
import sqlite3

DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "database"
    / "world_cup_2026.db"
)


def get_connection() -> sqlite3.Connection:
    """
    Create and return a connection to the analytics database.

    Returns
    -------
    sqlite3.Connection
        SQLite database connection.
    """
    return sqlite3.connect(DATABASE_PATH)