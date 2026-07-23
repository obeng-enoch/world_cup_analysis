from src.analytics.database import get_dataframe


def get_event_counts():
    return get_dataframe("events/counts.sql")