from src.analytics.database import get_dataframe


def get_club_medals():
    return get_dataframe("club/club_medal.sql")

def get_discipline():
    return get_dataframe("club/disciplin.sql")

def get_goal_contributions():
    return get_dataframe("club/goal_contributions.sql")

def get_minutes_played():
    return get_dataframe("club/minutes_played.sql")

def get_most_representation():
    return get_dataframe("club/most_representation.sql")

def get_valuable():
    return get_dataframe("club/valuable.sql")