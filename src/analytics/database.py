from pathlib import Path
import logging
import sqlite3

import pandas as pd

from src.analytics.query_loader import load_query

logger = logging.getLogger(__name__)

DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "database"
    / "world_cup_2026.db"
)


class AnalyticsQueryError(Exception):
    """Raised when a SQL analytics query fails to load or execute."""


def get_connection() -> sqlite3.Connection:
    """
    Create and return a connection to the analytics database.
    """
    return sqlite3.connect(DATABASE_PATH)


def get_dataframe(query_path: str) -> pd.DataFrame:
    """
    Load a SQL query, execute it against the analytics database,
    and return the result as a pandas DataFrame.
    """
    try:
        query = load_query(query_path)
        conn = get_connection()
        try:
            return pd.read_sql_query(query, conn)
        finally:
            conn.close()
    except Exception as exc:
        logger.error("Failed to load query '%s': %s", query_path, exc)
        raise AnalyticsQueryError(
            f"Could not load data for '{query_path}'."
        ) from exc


def get_scalar(query_path):
    """
    Execute a SQL query that returns a single value.
    """
    df = get_dataframe(query_path)

    if df.empty:
        raise AnalyticsQueryError(f"Query '{query_path}' returned no rows.")

    if df.shape != (1, 1):
        raise AnalyticsQueryError(
            f"Expected a single value from '{query_path}', "
            f"but got {df.shape[0]} rows and {df.shape[1]} columns."
        )

    return df.iat[0, 0]