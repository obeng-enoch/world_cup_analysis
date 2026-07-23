from src.analytics.database import get_dataframe


def get_full_awards():
    return get_dataframe("awards/full_awards.sql")

def get_golden_ball():
    return get_dataframe("awards/golden_ball.sql")

def get_golden_boot():
    return get_dataframe("awards/golden_boot.sql")