import pandas as pd
from src.config import REQUIRED_COLUMNS

def validate_teams(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned teams DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Cleaned teams DataFrame.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate team IDs,
        contains duplicate FIFA codes, or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["teams"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Teams dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no null values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )

    # Check 4: team_id is unique
    if not df["team_id"].is_unique:
        raise ValueError("Duplicate team_id values found.")
    
    # Check 5: fifa_code must be unique
    if not df["fifa_code"].is_unique:
        raise ValueError("Duplicate fifa_code values found.")
    
    # Check 6: FIFA ranking must be postive integers
    if (df["fifa_ranking_pre_tournament"] <= 0).any():
        raise ValueError(
            "FIFA ranking must be positive."
        )
    
    # Check 7: Elo rating must be positive
    if (df["elo_rating"] <= 0).any():
        raise ValueError(
            "Elo rating must be positive."
        )
    
    return True

def validate_venues(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned venues DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Cleaned venues DataFrame.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate venue IDs,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["venues"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Venues dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no null values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )

    # Check 4: venue_id is unique
    if not df["venue_id"].is_unique:
        raise ValueError("Duplicate venue_id values found.")
    
    return True

def validate_tournament_stages(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned tournament stages DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Cleaned tournament stages DataFrame.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate stage IDs,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["tournament_stages"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Tournament stages dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no null values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )

    # Check 4: stage_id is unique
    if not df["stage_id"].is_unique:
        raise ValueError("Duplicate stage_id values found.")
    
    return True

def validate_referees(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned referees DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Cleaned referees DataFrame.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate referee IDs,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["referees"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Referees dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no null values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )

    # Check 4: referee_id is unique
    if not df["referee_id"].is_unique:
        raise ValueError("Duplicate referee_id values found.")
    
    # Check 5: avg_cards_per_game must be non-negative
    if (df["avg_cards_per_game"] < 0).any():
        raise ValueError(
            "Average cards per game must be non-negative."
        )

    return True

def validate_squads_and_players(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned squads and players statistics DataFrame.
    
    Parameters
    ----------
    df :pd.DataFrame
        Cleaned squads Statistics
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate player IDS,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["squads_and_players"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Squads_and_players dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no null values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )

    # Check 4: player_id is unique
    if not df["player_id"].is_unique:
        raise ValueError("Duplicate player_id values found.")
    
    # Check 5: market value cannot be negative
    if (df["market_value_eur"] < 0).any():
        raise ValueError(
            "market_value_eur cannot contain negative values."
        )
    
    # Check 6: caps cannot be negative
    if (df["caps"] < 0).any():
       raise ValueError(
           "caps cannot contain negative values."
       )
    
    # Check 7: goals cannot be negative
    if (df["goals"] < 0).any():
        raise ValueError(
            "goals cannot contain negative values."
        )
    
    # Check 8: height must be postive
    if (df["height_cm"] <= 0).any():
        raise ValueError(
            "height_cm must contain positive values."
        )
    
    # Check 9: date_of_birth is datetime
    if not pd.api.types.is_datetime64_any_dtype(df["date_of_birth"]):
        raise ValueError(
            "date_of_birth must be a datetime column"
        )
    
    return True

def validate_player_stats(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned player statistics DataFrame.
    
    Parameters
    ----------
    df :pd.DataFrame
        Cleaned player Statistics.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate player IDS,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["player_stats"]
    
    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Player statistics dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no missing values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            f"Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )
    
    # Check 4: player_id is unique
    if df["player_id"].duplicated().any():
        raise ValueError("Duplicate player_id values found.")
    
    return True

def validate_matches(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned matches DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Cleaned matches DataFrame.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate match IDs,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["matches"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Matches dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: Required fields contain no null values
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )

    # Check 4: match_id must be unique
    if not df["match_id"].is_unique:
        raise ValueError(
            "Duplicate match_id values found."
        )
    
    return True
