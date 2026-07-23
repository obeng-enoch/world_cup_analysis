from src.analytics.database import get_dataframe


def get_top_scorers():
    return get_dataframe("players/top_scorers.sql")

def get_hat_tricks():
    return get_dataframe("players/hat_tricks.sql")

def get_multi_goal_matches():
    return get_dataframe("players/multi_goal_matches.sql")

def get_penalty_goals():
    return get_dataframe("players/penalty_goals.sql")

def get_own_goals():
    return get_dataframe("players/own_goals.sql")

def get_top_assists():
    return get_dataframe("players/tops_assists.sql")

def get_goal_contributions():
    return get_dataframe("players/goal_contributions.sql")

def get_appearances():
    return get_dataframe("players/appearances.sql")

def get_starts():
    return get_dataframe("players/starts.sql")

def get_minutes_played():
    return get_dataframe("players/minutes_played.sql")

def get_yellow_cards():
    return get_dataframe("players/yellow_cards.sql")

def get_red_cards():
    return get_dataframe("players/red_cards.sql")

def get_clean_sheets():
    return get_dataframe("players/clean_sheets.sql")

def get_saves():
    return get_dataframe("players/saves.sql")

def get_goals_conceded():
    return get_dataframe("players/goals_conceded.sql")