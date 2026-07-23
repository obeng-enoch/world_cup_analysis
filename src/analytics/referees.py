from src.analytics.database import get_dataframe


def get_fouls():
    return get_dataframe("referee/fouls.sql")

def get_matches_officiated():
    return get_dataframe("referee/matches_officiated.sql")

def get_red_cards():
    return get_dataframe("referee/red_card.sql")