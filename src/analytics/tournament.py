import pandas as pd

from src.analytics.database import get_connection
from src.analytics.query_loader import load_query

def get_overview() -> pd.DataFrame:
    """
    Return tournament overview KPIs.

    Returns:
        pandas.DataFrame
    """

    query = load_query("tournament_overview.sql")

    conn = get_connection()

    try:
        return pd.read_sql_query(query, conn)

    finally:
        conn.close()

def get_results() -> pd.DataFrame:
    """
    Return tournament match results.
    """
    query = load_query("tournament_results.sql")

    conn = get_connection()

    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()

def get_awards() -> pd.DataFrame:
    """
    Return tournament awards.
    """
    query = load_query("tournament_awards.sql")

    conn = get_connection()

    try:
        return pd.read_query(query, conn)
    finally:
        conn.close()