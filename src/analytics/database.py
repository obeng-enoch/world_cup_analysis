from pathlib import Path
import sqlite3

import pandas as pd

from src.analytics.query_loader import load_query

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


def get_dataframe(query_path: str) -> pd.DataFrame:
    """
    Load a SQL query, execute it against the analytics database,
    and return the result as a pandas DataFrame.
    """
    query = load_query(query_path)
    conn = get_connection()
    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()