import sqlite3

from src.config import DATABASE_PATH

from src.clean_data import (
    clean_teams,
    clean_venues,
    clean_tournament_stages,
    clean_referees,
    clean_squads_and_players,
    clean_player_stats,
    clean_matches,
)

from src.validators import (
    validate_teams,
    validate_venues,
    validate_tournament_stages,
    validate_referees,
    validate_squads_and_players,
    validate_player_stats,
    validate_matches,
)

def get_database_connection() -> sqlite3.Connection:
    """
    Create and return a connection to the SQLite database.
    
    Returns
    -------
    sqlite3.Connection
        An active connection to the project database.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    return connection

def load_teams(connection: sqlite3.Connection) -> None:
    """
    Load the validated teams DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading teams")

    #Extract and transform
    teams = clean_teams()

    #validate
    validate_teams(teams)

    #Load
    teams.to_sql(
        name="teams",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ teams loaded successfully.")

def load_venues(connection: sqlite3.Connection) -> None:
    """
    Load the validated venues DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading venues")

    #Extract and transform
    venues = clean_venues()

    #validate
    validate_venues(venues)

    #Load
    venues.to_sql(
        name="venues",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ venues loaded successfully.")

def load_tournament_stages(connection: sqlite3.Connection) -> None:
    """
    Load the validated tournament stages DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading tournament_stages")

    #Extract and transform
    tournament_stages = clean_tournament_stages()

    #validate
    validate_tournament_stages(tournament_stages)

    #Load
    tournament_stages.to_sql(
        name="tournament_stages",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ tournament_stages loaded successfully.")

def load_referees(connection: sqlite3.Connection) -> None:
    """
    Load the validated referees DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading referees")

    #Extract and transform
    referees = clean_referees()

    #validate
    validate_referees(referees)

    #Load
    referees.to_sql(
        name="referees",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ referees loaded successfully.")

def load_squads_and_players(connection: sqlite3.Connection) -> None:
    """
    Load the validated squads DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading squads_and_players")

    #Extract and transform
    squads_and_players = clean_squads_and_players()

    #validate
    validate_squads_and_players(squads_and_players)

    #Load
    squads_and_players.to_sql(
        name="squads_and_players",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ squads_and_players loaded successfully.")

def load_player_stats(connection: sqlite3.Connection) -> None:
    """
    Load the validated player statistics DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading player_stats")

    #Extract and transform
    players = clean_player_stats()

    #validate
    validate_player_stats(players)

    #Load
    players.to_sql(
        name="player_stats",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ player_stats loaded successfully.")

def load_matches(connection: sqlite3.Connection) -> None:
    """
    Load the validated matches DataFrame into SQLite.
    
    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.
    """

    print("Loading matches")

    #Extract and transform
    matches = clean_matches()

    #validate
    validate_matches(matches)

    #Load
    matches.to_sql(
        name="matches",
        con=connection,
        if_exists="replace",
        index=False,
    )

    print("✓ matches loaded successfully.")

def build_database() -> None:
    """
    Build the SQLite database from the cleaned and validated datasets.
    """

    connection = get_database_connection()

    try:
        load_teams(connection)
        load_venues(connection)
        load_tournament_stages(connection)
        load_referees(connection)
        load_squads_and_players(connection)
        load_player_stats(connection)
        load_matches(connection)
    finally:
        connection.close()