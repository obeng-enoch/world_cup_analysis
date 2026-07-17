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

def validate_match_team_stats(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned match team statistics DataFrame.
    
    Parameters
    ----------
    df :pd.DataFrame
        Cleaned match team Statistics.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate match and team IDS,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["match_team_stats"]
    
    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Match team statistics dataset is empty.")
    
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
    
    # Check 4: match_id and team_id must be unique
    if df.duplicated(
        subset=["match_id", "team_id"]
    ).any():
        raise ValueError(
            "Duplicate match/team combinations found."
        )
    
    # Check 5: percentage percentage should be between 0 and 100
    if not df["possession_pct"].between(0, 100).all():
        raise ValueError(
            "possession_pct must be between 0 and 100."
        )
    
    # Check 6: shots shouldn't be negative
    if (df["total_shots"] < 0).any():
        raise ValueError(
            "total_shots cannot contain negative values."
        )
    
    # Check 7: coners shouldn't be negative
    if(df["corners"] < 0).any():
        raise ValueError(
            "corners cannot contain negative values."
        )
    
    # Check 8: fouls shouldn't be negative
    if (df["fouls"] < 0).any():
        raise ValueError(
            "fouls cannot contain negative values."
        )
    
    # Check 9: offsides shouldn't be negative
    if (df["offsides"] < 0).any():
        raise ValueError(
            "offsides cannot contain negative values."
        )
    
    # Check 10: saves shouldn't be negative
    if (df["saves"] < 0).any():
        raise ValueError(
            "saves cannot contain negative values."
        )

    # Check 11: last_updated should be datetime data type
    if not pd.api.types.is_datetime64_any_dtype(
        df["last_updated"]
):
        raise ValueError(
            "last_updated must be a datetime column."
        )
    
    return True

def validate_match_events(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned matche events statistics DataFrame.
    
    Parameters
    ----------
    df :pd.DataFrame
        Cleaned match events Statistics.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate match and team IDS,
        or has missing values in required columns.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["match_events"]
    
    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Match events statistics dataset is empty.")
    
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
    
    # Check 4: event_id is unique
    if not df["event_id"].is_unique:
        raise ValueError(
            "Duplicate event_id values found."
        )
    # Check 5: minute datatype should be string
    if not pd.api.types.is_string_dtype(df["minute"]):
        raise ValueError(
            "minute must be stored as string"
        )
    
    # Check 6: event_type missing values
    if df["event_type"].isna().any():
        raise ValueError(
            "event_type contains missing values"
        )
    
    return True

def validate_match_lineups(df: pd.DataFrame) -> bool:
    """
    Validate the cleaned match_lineups DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Cleaned match_lineups DataFrame.
        
    Returns
    -------
    bool
        True if all validation checks pass.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains duplicate lineup IDs,
        is_starting_xi contains only valid binary values (0 or 1),
        minutes_played is between 0 and 120, tactical position contains no missing vales.
    KeyError
        If required columns are missing.
    """

    required_columns = REQUIRED_COLUMNS["match_lineups"]

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Match_lineups dataset is empty.")
    
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

    # Check 4: lineup_id is unique
    if not df["lineup_id"].is_unique:
        raise ValueError("Duplicate lineup_id values found.")
    
    # Check 4: lineup_id is unique
    if not df["lineup_id"].is_unique:
        raise ValueError(
            "Duplicate lineup_id values found."
        )

    # Check 5: is_starting_xi contains only valid binary values
    if not df["is_starting_xi"].isin([0, 1]).all():
        raise ValueError(
            "is_starting_xi must contain only 0 or 1."
        )

    # Check 6: minutes_played is non-negative
    if (df["minutes_played"] < 0).any():
        raise ValueError(
            "minutes_played cannot contain negative values."
        )

    # Check 7: minutes_played does not exceed 120
    if (df["minutes_played"] > 120).any():
        raise ValueError(
            "minutes_played cannot exceed 120 minutes."
        )
    
    return True