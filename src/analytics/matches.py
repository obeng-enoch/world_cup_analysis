from src.analytics.database import get_dataframe


def get_biggest_upsets():
    return get_dataframe("match_analysis/biggest_upsets.sql")

def get_biggest_wins():
    return get_dataframe("match_analysis/biggest_wins.sql")

def get_ended_penalties():
    return get_dataframe("match_analysis/ended_penalties.sql")

def get_goals_per_venue():
    return get_dataframe("match_analysis/goal_per_venue.sql")

def get_goals_per_stage():
    return get_dataframe("match_analysis/goals_per_stage.sql")

def get_goal_timing():
    return get_dataframe("match_analysis/goal_timing.sql")

def get_highest_scoring():
    return get_dataframe("match_analysis/highest_scoring.sql")

def get_late_goals():
    return get_dataframe("match_analysis/late_goals.sql")

def get_match_results():
    return get_dataframe("match_analysis/match_results.sql")

def get_possession_dominant():
    return get_dataframe("match_analysis/possession_dominant.sql")