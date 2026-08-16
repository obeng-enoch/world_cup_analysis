from src.analytics.database import get_dataframe


def get_awards():
    return get_dataframe("awards/awards.sql")

def get_man_of_the_match_players():
    return get_dataframe("awards/man_of_the_match_players.sql")

def get_man_of_the_match_teams():
    return get_dataframe("awards/man_of_the_match_teams.sql")

def get_man_of_the_match_clubs():
    return get_dataframe("awards/man_of_the_match_clubs.sql")