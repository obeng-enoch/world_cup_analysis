from src.analytics.database import get_dataframe


def get_fouls():
    return get_dataframe("referee/fouls.sql")


def get_matches_officiated():
    return get_dataframe("referee/matches_officiated.sql")


def get_red_cards():
    return get_dataframe("referee/red_card.sql")


def get_country_distribution():
    return get_dataframe("referee/country_distribution.sql")


def get_card_comparison():
    return get_dataframe("referee/card_comparison.sql")


def get_stage_workload():
    return get_dataframe("referee/stage_workload.sql")