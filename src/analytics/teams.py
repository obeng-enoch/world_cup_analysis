from src.analytics.database import get_dataframe

def get_aggresive_attacking():
    return get_dataframe("teams/aggresive_attacking.sql")

def get_average_stats():
    return get_dataframe("teams/average_stats.sql")

def get_defense():
    return get_dataframe("teams/defense.sql")

def get_discipline():
    return get_dataframe("teams/discipline.sql")

def get_highest_scoring_teams():
    return get_dataframe("teams/highest_scoring_teams.sql")

def get_most_clinicals():
    return get_dataframe("teams/most_clinicals.sql")

def get_pre_tournament_ranking():
    return get_dataframe("teams/pre_tournament_ranking.sql")

def get_squad_experience():
    return get_dataframe("teams/squad_experience.sql")

def get_squad_value():
    return get_dataframe("teams/squad_value.sql")

def get_tournament_finish():
    return get_dataframe("teams/tournament_finish.sql")