import pandas as pd

REQUIRED_PLAYER_COLUMNS = (
    "player_id",
    "player_name",
    "team_id",
    "goals",
    "last_verified",
)

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

    # Check 1: DataFrame is not empty
    if df.empty:
        raise ValueError("Player statistics dataset is empty.")
    
    # Check 2: Required columns exist
    missing_columns = [
        column
        for column in REQUIRED_PLAYER_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {missing_columns}"
        )
    
    # Check 3: player_id is unique
    if df["player_id"].duplicated().any():
        raise ValueError("Duplicate player_id values found.")
    
    # Check 4: Required fields contain no missing values
    required_columns = list(REQUIRED_PLAYER_COLUMNS)
    missing_values = df[required_columns].isnull().any()

    columns_with_missing_values = missing_values[
        missing_values
    ].index.tolist()

    if columns_with_missing_values:
        raise ValueError(
            f"Missing values found in required columns: "
            f"{columns_with_missing_values}"
        )
    
    return True
