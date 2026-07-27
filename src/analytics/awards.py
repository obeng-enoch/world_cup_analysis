from src.analytics.database import get_dataframe


def get_awards():
    return get_dataframe("awards/awards.sql")
