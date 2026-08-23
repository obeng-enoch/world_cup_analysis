import sqlite3

import pandas as pd
import pytest

from src.analytics.database import (
    get_connection,
    get_dataframe,
    get_scalar,
)

from src.analytics.database import AnalyticsQueryError, get_dataframe, get_scalar

def test_get_connection_returns_sqlite_connection():
    connection = get_connection()

    try:
        assert isinstance(connection, sqlite3.Connection)
    finally:
        connection.close()

def test_get_dataframe_returns_dataframe():
    df = get_dataframe("tournament_overview/total_players.sql")

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.shape == (1, 1)

def test_get_dataframe_raises_error_for_missing_query():
    with pytest.raises(AnalyticsQueryError):
        get_dataframe("tournament_overview/does_not_exist.sql")

def test_get_scalar_returns_single_value():
    result = get_scalar("tournament_overview/total_players.sql")

    assert result == 1248

def test_get_scalar_rejects_multiple_values():
    with pytest.raises(AnalyticsQueryError, match="Expected a single value"):
        get_scalar("tournament_overview/goals_per_stage.sql")