from ast import Return

import pandas as pd
from src.config import CSV_FILES, DATE_COLUMNS

def load_csv(table_name: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    table_name : str
        Name of the table defined in config.CSV_FILES.

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame.
    """

    if table_name not in CSV_FILES:
        raise ValueError(
            f"Unknown table '{table_name}'."
            f"Available tables: {list(CSV_FILES.keys())}"
        )

    csv_path = CSV_FILES[table_name]

    # check that the csv file exists before trying to read it.
    if not csv_path.exists():
        raise FileNotFoundError(
            f"CSV file not found: {csv_path}"
        )
    
    return pd.read_csv(csv_path)

def convert_dates(
    df: pd.DataFrame,
    columns: list[str]
) -> pd.DataFrame:
    """
    Convert specified columns in a DataFrame to datetime.
    
    Parameters
    ----------
    
    df : pd.DataFrame
        The DataFrame containing the date columns.
        
    columns : list[str]
        Names of columns to convert.

    Returns
    -------
    pd.DataFrame
        DataFrame with converted datetime columns.

    Raises
    ------
    KeyError
        If a specified column does not exist.
    """

    for column in columns:
        if column not in df.columns:
            raise KeyError(
                f"Date column not found in DataFrame: {column}"
            )
        
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )
        
    return df

def clean_teams() -> pd.DataFrame:
    """
    Load and clean the teams dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned teams DataFrame.
    """

    teams = load_csv("teams")

    return teams

def clean_venues() -> pd.DataFrame:
    """
    Load and clean the venues dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned venues DataFrame.
    """

    venues = load_csv("venues")

    return venues

def clean_tournament_stages() -> pd.DataFrame:
    """
    Load and clean the tournament stages dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned tournament stages DataFrame.
    """

    tournament_stages = load_csv("tournament_stages")

    return tournament_stages

def clean_referees() -> pd.DataFrame:
    """
    Load and clean the referees dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned referees DataFrame.
    """

    referees = load_csv("referees")

    return referees

def clean_squads_and_players() -> pd.DataFrame:
    """
    Load and clean squads and players dataset.

    Returns
    -------
    pd.DataFrame
        Clean squads and players statistics DataFrame.
    """

    squads_and_players = load_csv("squads_and_players")

    squads_and_players = convert_dates(
        squads_and_players,
        DATE_COLUMNS["squads_and_players"]
    )

    return squads_and_players

def clean_player_stats() -> pd.DataFrame:
    """
    Load and clean the player statistics dataset.
    
    Returns
    -------
    pd.DataFrame
        Cleaned player statistics DataFrame.
    """

    player_stats = load_csv("player_stats")

    player_stats = convert_dates(
        player_stats,
        DATE_COLUMNS["player_stats"]
    )

    return player_stats

def clean_matches() -> pd.DataFrame:
    """
    Load and clean the matches dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned matches DataFrame.
    """

    matches = load_csv("matches")

    matches = convert_dates(
        matches,
        DATE_COLUMNS["matches"]
    )

    return matches