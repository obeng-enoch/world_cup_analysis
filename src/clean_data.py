import pandas as pd
from src.config import CSV_FILES

def load_csv(table_name: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    parameters
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

def convert_dates(df, columns):
    """
    Convert specified columns in a DataFrame to datetime.
    
    parameters
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