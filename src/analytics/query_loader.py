from pathlib import Path

SQL_DIRECTORY = (
    Path(__file__).resolve().parents[2]
    / "sql"
)

def load_query(filename: str) -> str:
    """
    Load a SQL query from the sql directory.
    
    Parameters
    ----------
    filename : str
        Name of the SQL file.
        
    Returns
    -------
    str
        SQL query as a string.
    """
    
    query_path = SQL_DIRECTORY / filename

    if not query_path.exists():
        raise FileNotFoundError(
            f"SQL file not found: {query_path}"
        )
    
    return query_path.read_text(
        encoding="utf-8"
    )