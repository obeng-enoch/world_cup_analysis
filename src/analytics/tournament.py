from src.analytics.database import get_dataframe


def get_total_players():
    return get_dataframe("tournament_overview/total_players.sql")

def get_total_teams():
    return get_dataframe("tournament_overview/total_teams.sql")

def get_total_matches():
    return get_dataframe("tournament_overview/total_matches.sql")

def get_total_goals():
    return get_dataframe("tournament_overview/total_goals.sql")

def get_total_clubs():
    return get_dataframe("tournament_overview/total_clubs.sql")