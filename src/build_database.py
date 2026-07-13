import sqlite3

import pandas as pd

from src.clean_data import clean_player_stats
from src.config import DATABASE_PATH
from src.validators import validate_player_stats

def get_database_connection():
    """
    Create and return a connection to the SQLite database.
    
    Returns
    -------
    sqlite3.Connection
        An active connection to the project database.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    return connection

def load_player_stats(
    df: pd.DataFrame,
    connection: sqlite3.Connection,
) -> None:
    """
    Load the validated player statistics DataFrame into SQLite.
    
    Parameters
    ----------
    df : pd.DataFrame
        Validated player statistics DataFrame.
        
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    df.to_sql(
        name="player_stats",
        con=connection,
        if_exists="replace",
        index=False,
    )

def build_database() -> None:
    """
    Build the SQLite database from the cleaned and validated datasets.
    """

    connection = get_database_connection()

    try:
        print("Loading player_stats")

        #Extract and transform
        players = clean_player_stats()

        #validate
        validate_player_stats(players)

        #Load
        load_player_stats(players, connection)

        print("✓ player_stats loaded successfully.")

    finally:
        connection.close()